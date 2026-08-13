#!/usr/bin/env python3
"""Audit rotation-independent affine diffusion reservoir algebra.

This checks the singular-value identity behind the two-dimensional heat-area
lower bound and an explicit rapidly rotating biaxial model showing that the
q^(1/2) residual amplification exponent is qualitatively sharp at the linear
level.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

SCHEMA_VERSION = "0.1.0"


def expm2(B: np.ndarray, t: float) -> np.ndarray:
    vals, vecs = np.linalg.eig(B)
    D = np.diag(np.exp(vals * t))
    E = vecs @ D @ np.linalg.inv(vecs)
    return np.real_if_close(E, tol=1000).astype(float)


def run_checks(seed: int = 20260813):
    rng = np.random.default_rng(seed)
    max_product_error = 0.0

    # Random determinant-one singular spectra with prescribed top q.
    for _ in range(100):
        q = float(rng.uniform(1.2, 50.0))
        # sigma2 must lie in [q^(-1/2), q] for ordered determinant-one spectra;
        # choose it so sigma3=1/(q sigma2) <= sigma2.
        lo = q ** (-0.5)
        sigma2 = math.exp(rng.uniform(math.log(lo), math.log(q)))
        sigma3 = 1.0 / (q * sigma2)
        sig = np.array([q, sigma2, sigma3])
        sig.sort()
        sig = sig[::-1]
        alpha = np.sort(1.0 / (sig * sig))
        max_product_error = max(max_product_error, abs(alpha[1] * alpha[2] - sig[0] ** 2))

    # Scalar coefficient c_q and mixed smoothing factor.
    M = 1.7
    nu = 0.8
    qs = np.array([2.0, 4.0, 16.0, 128.0])
    cqs = (1.0 - qs ** -2) / (2.0 * M)
    smoothing_factor = qs * (nu * cqs * qs) ** (-0.5)
    normalized = smoothing_factor / np.sqrt(qs)
    expected = np.sqrt(2.0 * M / (nu * (1.0 - qs ** -2)))
    factor_error = float(np.max(np.abs(normalized - expected)))

    # Explicit rapidly rotating biaxial strain around a fixed extensional axis.
    # In the rotating frame, e1 grows at rate a. The perpendicular block is
    # B=[[-2a, Omega],[-Omega,a]]. For Omega > 3a/2 its eigenvalues have
    # real part -a/2, so both transverse singular exponents approach -a/2.
    a = 1.0
    Omega = 4.0
    B2 = np.array([[-2.0 * a, Omega], [-Omega, a]])
    eig = np.linalg.eigvals(B2)
    real_parts = np.sort(np.real(eig))
    eig_real_error = float(np.max(np.abs(real_parts + 0.5 * a)))

    t = 12.0
    E2 = expm2(B2, t)
    sv2 = np.linalg.svd(E2, compute_uv=False)
    # The product is exactly exp(trace(B2)t)=exp(-a t).
    product_error = abs(float(np.prod(sv2)) - math.exp(-a * t))
    # Both logarithmic singular exponents should be close to -a/2 at long time.
    exponents = np.log(sv2) / t
    exponent_spread = float(np.max(np.abs(exponents + 0.5 * a)))

    checks = {
        "terminal_two_strong_metric_product_equals_q2": max_product_error < 1e-10,
        "mixed_smoothing_factor_formula": factor_error < 1e-12,
        "rapid_rotation_block_eigen_real_part_minus_a_over_2": eig_real_error < 1e-12,
        "rapid_rotation_transverse_area_contraction": product_error < 1e-9,
        "rapid_rotation_transverse_singular_exponents_near_minus_a_over_2": exponent_spread < 0.08,
    }
    checks = {k: bool(v) for k, v in checks.items()}

    return {
        "schema_version": SCHEMA_VERSION,
        "status": "ROTATION-INDEPENDENT AFFINE DIFFUSION / ALGEBRA AUDIT",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "max_product_error": max_product_error,
        "mixed_factor_error": factor_error,
        "rapid_rotation_example": {
            "a": a,
            "Omega": Omega,
            "B2_eigenvalues": [[float(np.real(z)), float(np.imag(z))] for z in eig],
            "transverse_singular_values_at_t": sv2.tolist(),
            "transverse_log_exponents": exponents.tolist(),
            "area_product_error": product_error,
        },
        "statement": (
            "Volume preservation forces the product of the two strongest terminal diffusion-metric eigenvalues to equal q^2. "
            "A fast rotating biaxial example can distribute transverse compression roughly evenly, but cannot eliminate its total area contraction."
        ),
        "claim_boundary": (
            "This gate audits the matrix algebra and an explicit linear rotating example. The nonlinear Navier-Stokes perturbative transfer remains open."
        ),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", default="results")
    args = ap.parse_args()
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    d = run_checks()
    (out / "rotation_independent_affine_diffusion_gate.json").write_text(json.dumps(d, indent=2), encoding="utf-8")
    (out / "rotation_independent_affine_diffusion_gate.md").write_text(
        "# Rotation-independent affine diffusion audit\n\n"
        f"Status: **{d['status']}**\n\nChecks passed: **{d['passed']}/{d['total']}**\n\n"
        + d["statement"] + "\n\n## Claim boundary\n\n" + d["claim_boundary"] + "\n",
        encoding="utf-8",
    )
    print(f"Rotation-independent affine diffusion: {d['passed']}/{d['total']} checks passed")
    if d["passed"] != d["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
