#!/usr/bin/env python3
"""Audit the weighted optimal-affine representative identities."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

SCHEMA_VERSION = "0.1.0"


def run_checks(seed: int = 20260813):
    rng = np.random.default_rng(seed)
    n = 200
    weights = rng.uniform(0.1, 2.0, size=n)
    grads = rng.normal(size=(n, 3, 3))
    # Project each sample to trace free, mimicking incompressibility.
    tr = np.trace(grads, axis1=1, axis2=2) / 3.0
    grads = grads - tr[:, None, None] * np.eye(3)[None, :, :]

    M = float(weights.sum())
    L = np.tensordot(weights, grads, axes=(0, 0)) / M
    residual = grads - L

    mean_residual = np.tensordot(weights, residual, axes=(0, 0))
    lhs = float(np.sum(weights[:, None, None] * grads * grads))
    coherent = M * float(np.sum(L * L))
    variance = float(np.sum(weights[:, None, None] * residual * residual))

    # Verify minimization numerically against random trace-free perturbations.
    base_error = variance
    min_gap = math.inf
    for _ in range(100):
        D = rng.normal(size=(3, 3))
        D -= np.trace(D) / 3.0 * np.eye(3)
        candidate = L + D
        err = float(np.sum(weights[:, None, None] * (grads - candidate) ** 2))
        min_gap = min(min_gap, err - base_error)

    S = 0.5 * (L + L.T)
    A = 0.5 * (L - L.T)

    checks = {
        "representative_trace_free": abs(float(np.trace(L))) < 1e-12,
        "weighted_residual_mean_zero": float(np.linalg.norm(mean_residual)) < 1e-11,
        "pythagorean_identity": abs(lhs - coherent - variance) < 1e-10,
        "least_squares_minimizer": min_gap >= -1e-10,
        "sym_skew_orthogonality": abs(float(np.sum(S * A))) < 1e-12,
        "strain_below_total_gradient": M * float(np.sum(S * S)) <= lhs + 1e-10,
    }
    checks = {k: bool(v) for k, v in checks.items()}
    return {
        "schema_version": SCHEMA_VERSION,
        "status": "EXACT OPTIMAL LOCAL AFFINE REPRESENTATIVE / ALGEBRA AUDIT",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "residuals": {
            "weighted_mean_norm": float(np.linalg.norm(mean_residual)),
            "pythagorean_error": abs(lhs - coherent - variance),
            "minimum_random_competitor_gap": min_gap,
        },
        "statement": (
            "The weighted mean gradient is the least-squares constant affine representative; "
            "the total weighted gradient energy splits exactly into coherent affine energy plus residual variance."
        ),
        "claim_boundary": (
            "This gate audits finite-dimensional weighted algebra. The time-integrated condition-number estimate "
            "uses standard singular-value growth inequalities and Cauchy-Schwarz separately."
        ),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", default="results")
    args = ap.parse_args()
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    d = run_checks()
    (out / "optimal_affine_representative_gate.json").write_text(json.dumps(d, indent=2), encoding="utf-8")
    (out / "optimal_affine_representative_gate.md").write_text(
        "# Optimal affine representative audit\n\n"
        f"Status: **{d['status']}**\n\nChecks passed: **{d['passed']}/{d['total']}**\n\n"
        + d["statement"] + "\n\n## Claim boundary\n\n" + d["claim_boundary"] + "\n",
        encoding="utf-8",
    )
    print(f"Optimal affine representative: {d['passed']}/{d['total']} checks passed")
    if d["passed"] != d["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
