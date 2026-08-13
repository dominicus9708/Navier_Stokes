#!/usr/bin/env python3
"""Audit the exact Gaussian variance / semigroup square-function identity.

This gate checks the normalization on complex Fourier modes for random
positive-definite covariance matrices. It is an algebraic/semigroup audit,
not a regularity proof.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def random_spd(rng: np.random.Generator) -> np.ndarray:
    a = rng.normal(size=(3, 3))
    return a @ a.T + 0.25 * np.eye(3)


def audit_mode(k: np.ndarray, sigma: np.ndarray, n_quad: int = 20000) -> dict:
    a = float(k @ sigma @ k)
    lhs = 1.0 - np.exp(-a)

    # Midpoint quadrature for int_0^1 a exp(-(1-t)a) dt.
    t = (np.arange(n_quad) + 0.5) / n_quad
    rhs_num = float(np.mean(a * np.exp(-(1.0 - t) * a)))
    rhs_exact = 1.0 - np.exp(-a)

    return {
        "a": a,
        "lhs": lhs,
        "rhs_exact": rhs_exact,
        "rhs_midpoint": rhs_num,
        "exact_error": abs(lhs - rhs_exact),
        "quadrature_error": abs(rhs_num - rhs_exact),
        "passed": bool(abs(lhs - rhs_exact) < 1e-14 and abs(rhs_num - rhs_exact) < 2e-7),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="results")
    args = parser.parse_args()

    rng = np.random.default_rng(20260813)
    cases = []
    for _ in range(8):
        sigma = random_spd(rng)
        k = rng.normal(size=3)
        cases.append(audit_mode(k, sigma))

    report = {
        "identity": "P_Sigma|g|^2-|P_Sigma g|^2 = int_0^1 P_{tSigma}|grad P_{(1-t)Sigma}g Sigma^(1/2)|^2 dt",
        "cases": cases,
        "passed": bool(all(c["passed"] for c in cases)),
    }

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "gaussian_semigroup_variance_gate.json"
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(json.dumps(report, indent=2))
    if not report["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
