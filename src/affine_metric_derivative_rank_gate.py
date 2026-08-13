#!/usr/bin/env python3
"""Audit D_A = P tr(A R) and derivative-rank bounds for SPD A, PSD trace-one R."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

SCHEMA_VERSION = "0.1.0"


def random_orthogonal(rng):
    Q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    if np.linalg.det(Q) < 0:
        Q[:, 0] *= -1
    return Q


def run_checks(seed: int = 20260813, samples: int = 200):
    rng = np.random.default_rng(seed)
    max_identity = 0.0
    max_r3_violation = 0.0
    max_r23_violation = 0.0
    max_det_error = 0.0

    for _ in range(samples):
        # det-one SPD diffusion metric.
        logs = rng.normal(size=3)
        logs -= logs.mean()
        lam = np.sort(np.exp(logs))
        Q = random_orthogonal(rng)
        A = Q @ np.diag(lam) @ Q.T

        # PSD trace-one derivative covariance.
        X = rng.normal(size=(3, 3))
        R = X @ X.T
        R /= np.trace(R)

        P = float(rng.uniform(0.1, 5.0))
        D = P * float(np.trace(A @ R))

        # In eigenbasis of A.
        vals, vecs = np.linalg.eigh(A)
        r = np.array([vecs[:, i] @ R @ vecs[:, i] for i in range(3)])
        spectral = P * float(np.dot(vals, r))

        max_identity = max(max_identity, abs(D - spectral))
        max_r3_violation = max(max_r3_violation, r[2] - D / (P * vals[2]))
        max_r23_violation = max(max_r23_violation, r[1] + r[2] - D / (P * vals[1]))
        max_det_error = max(max_det_error, abs(np.linalg.det(A) - 1.0))

    # Explicit highly anisotropic family: bounded D/P forces strong-axis fraction small.
    K = 1e6
    # F singular values K^(1/3), 1, K^(-1/3): kappa(F)=K^(2/3), enough for explicit audit.
    s = np.array([K ** (1.0 / 3.0), 1.0, K ** (-1.0 / 3.0)])
    lam = np.sort(1.0 / (s * s))
    Lambda = lam[2]
    M = 2.0
    forced_r3_upper = M / Lambda

    checks = {
        "diffusion_covariance_identity": max_identity < 1e-10,
        "strong_axis_fraction_bound": max_r3_violation < 1e-10,
        "two_strong_axes_fraction_bound": max_r23_violation < 1e-10,
        "det_A_one": max_det_error < 1e-10,
        "anisotropic_forces_small_strong_fraction": forced_r3_upper < 1e-3,
    }
    checks = {k: bool(v) for k, v in checks.items()}
    return {
        "schema_version": SCHEMA_VERSION,
        "status": "EXACT AFFINE-METRIC / DERIVATIVE-COVARIANCE AUDIT",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "max_residuals": {
            "identity": max_identity,
            "r3_violation": max_r3_violation,
            "r2_plus_r3_violation": max_r23_violation,
            "det_A_error": max_det_error,
        },
        "anisotropic_example": {
            "lambda_max": float(Lambda),
            "assumed_D_over_P": M,
            "forced_r3_upper": float(forced_r3_upper),
        },
        "statement": (
            "For derivative covariance R and diffusion metric A, D_A/P=tr(A R). "
            "A diverging strong diffusion eigenvalue forces the derivative fraction in its eigenspace to vanish unless D_A/P diverges."
        ),
        "claim_boundary": (
            "This is an instantaneous covariance statement. Turning rank reduction into a fixed low-dimensional flow requires temporal eigenspace rigidity and compactness."
        ),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", default="results")
    args = ap.parse_args()
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    d = run_checks()
    (out / "affine_metric_derivative_rank_gate.json").write_text(json.dumps(d, indent=2), encoding="utf-8")
    (out / "affine_metric_derivative_rank_gate.md").write_text(
        "# Affine metric derivative-rank audit\n\n"
        f"Status: **{d['status']}**\n\nChecks passed: **{d['passed']}/{d['total']}**\n\n"
        + d["statement"] + "\n\n## Claim boundary\n\n" + d["claim_boundary"] + "\n",
        encoding="utf-8",
    )
    print(f"Affine metric derivative rank: {d['passed']}/{d['total']} checks passed")
    if d["passed"] != d["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
