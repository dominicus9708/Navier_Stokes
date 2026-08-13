#!/usr/bin/env python3
"""Audit the affine/material deformation factorization ledger.

For H=FG, verify the condition-number triangle inequalities and the explicit
counter-deformation example showing that a large affine factor need not imply
large full material deformation: the residual factor can cancel it, but then
its own condition number must be comparably large.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

SCHEMA_VERSION = "0.1.0"


def cond2(M: np.ndarray) -> float:
    return float(np.linalg.cond(M, 2))


def normalize_det_one(M: np.ndarray) -> np.ndarray:
    det = float(np.linalg.det(M))
    if abs(det) < 1e-10:
        raise ValueError("singular sample")
    # Multiplying by a scalar does not change the condition number.  Use the
    # real cube root so determinant becomes +1 even for negative det.
    scale = math.copysign(abs(det) ** (-1.0 / 3.0), det)
    N = scale * M
    if np.linalg.det(N) < 0:
        N[:, 0] *= -1.0
    N /= float(np.linalg.det(N)) ** (1.0 / 3.0)
    return N


def run_checks(seed: int = 20260813, samples: int = 100):
    rng = np.random.default_rng(seed)

    max_submult_residual = 0.0
    max_reverse_f_residual = 0.0
    max_reverse_g_residual = 0.0
    max_log_triangle_residual = 0.0

    for _ in range(samples):
        while True:
            A = rng.normal(size=(3, 3))
            B = rng.normal(size=(3, 3))
            if abs(np.linalg.det(A)) > 0.1 and abs(np.linalg.det(B)) > 0.1:
                break
        F = normalize_det_one(A)
        G = normalize_det_one(B)
        H = F @ G

        kF, kG, kH = cond2(F), cond2(G), cond2(H)
        max_submult_residual = max(max_submult_residual, kH - kF * kG)
        max_reverse_f_residual = max(max_reverse_f_residual, kF - kH * kG)
        max_reverse_g_residual = max(max_reverse_g_residual, kG - kF * kH)

        dF, dG, dH = math.log(kF), math.log(kG), math.log(kH)
        max_log_triangle_residual = max(
            max_log_triangle_residual,
            abs(dF - dG) - dH,
            dH - dF - dG,
        )

    # Explicit exact cancellation family.
    M = 25.0
    F = np.diag([M, 1.0 / M, 1.0])
    G = np.linalg.inv(F)
    H = F @ G
    kF, kG, kH = cond2(F), cond2(G), cond2(H)

    # Quantitative bookkeeping consequence: dG >= dF-dH.
    dF, dG, dH = math.log(kF), math.log(kG), math.log(kH)

    tol = 2e-10
    checks = {
        "condition_submultiplicative": max_submult_residual <= tol,
        "reverse_F_bookkeeping": max_reverse_f_residual <= tol,
        "reverse_G_bookkeeping": max_reverse_g_residual <= tol,
        "log_condition_triangle": max_log_triangle_residual <= tol,
        "explicit_full_cancellation": np.linalg.norm(H - np.eye(3)) < 1e-12,
        "explicit_large_affine_condition": abs(kF - M * M) < 1e-10,
        "explicit_large_residual_condition": abs(kG - M * M) < 1e-10,
        "explicit_full_condition_one": abs(kH - 1.0) < 1e-12,
        "counter_deformation_lower_bound": dG + 1e-12 >= dF - dH,
    }
    checks = {k: bool(v) for k, v in checks.items()}

    return {
        "schema_version": SCHEMA_VERSION,
        "status": "EXACT DEFORMATION FACTORIZATION LEDGER / ALGEBRA AUDIT",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "random_samples": samples,
        "max_residuals": {
            "kH_minus_kF_kG": max_submult_residual,
            "kF_minus_kH_kG": max_reverse_f_residual,
            "kG_minus_kF_kH": max_reverse_g_residual,
            "log_triangle": max_log_triangle_residual,
        },
        "explicit_cancellation": {
            "M": M,
            "kappa_F": kF,
            "kappa_G": kG,
            "kappa_H": kH,
            "d_F": dF,
            "d_G": dG,
            "d_H": dH,
        },
        "statement": (
            "For H=FG, logarithmic condition-number distortion obeys "
            "|d(F)-d(G)|<=d(H)<=d(F)+d(G). Thus a large coarse affine "
            "distortion that is absent from the full material map must reappear "
            "as comparably large residual counter-deformation."
        ),
        "claim_boundary": (
            "This is matrix/deformation bookkeeping only. It does not convert "
            "large residual-frame condition number into a physical L2 strain or "
            "palinstrophy cost when F itself is poorly conditioned."
        ),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", default="results")
    args = ap.parse_args()
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    d = run_checks()
    (out / "deformation_factorization_ledger_gate.json").write_text(
        json.dumps(d, indent=2), encoding="utf-8"
    )
    (out / "deformation_factorization_ledger_gate.md").write_text(
        "# Deformation factorization ledger audit\n\n"
        f"Status: **{d['status']}**\n\n"
        f"Checks passed: **{d['passed']}/{d['total']}**\n\n"
        + d["statement"]
        + "\n\n## Claim boundary\n\n"
        + d["claim_boundary"]
        + "\n",
        encoding="utf-8",
    )
    print(f"Deformation factorization ledger: {d['passed']}/{d['total']} checks passed")
    if d["passed"] != d["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
