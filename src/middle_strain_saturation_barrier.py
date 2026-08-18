#!/usr/bin/env python3
"""Symbolic/numerical audit for the middle-strain saturation defect.

This module verifies only the algebraic pieces of the 2026-08-19 M-branch
refinement. It does not prove global Navier--Stokes regularity.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp


def symbolic_checks():
    l2, l3, x = sp.symbols("l2 l3 x", positive=True, real=True)
    l1 = -(l2 + l3)
    norm2 = sp.expand(l1**2 + l2**2 + l3**2)

    defect_identity = sp.simplify(
        -l1 * l2 * l3 - (sp.Rational(1, 2) * l2 * norm2 - l2**3)
    )

    y = (-x + sp.sqrt(2 - 3 * x**2)) / 2
    gap32 = sp.simplify(y - x)
    gap31 = sp.simplify(2 * y + x)

    checks = {
        "positive_middle_exact_defect": bool(defect_identity == 0),
        "frobenius_formula": bool(
            sp.simplify(norm2 - 2 * (l2**2 + l2 * l3 + l3**2)) == 0
        ),
        "principal_gap_32_formula": bool(
            sp.simplify(gap32 - (sp.sqrt(2 - 3 * x**2) - 3 * x) / 2) == 0
        ),
        "principal_gap_31_formula": bool(
            sp.simplify(gap31 - sp.sqrt(2 - 3 * x**2)) == 0
        ),
    }
    return checks


def numerical_ordered_inequality(samples: int = 10000, seed: int = 11):
    rng = np.random.default_rng(seed)
    worst = -math.inf
    failures = 0

    for _ in range(samples):
        vals = np.sort(rng.normal(size=3))
        vals -= vals.mean()
        vals = np.sort(vals)
        l1, l2, l3 = map(float, vals)
        norm2 = l1 * l1 + l2 * l2 + l3 * l3
        f = max(l2, 0.0)
        lhs = -(l1 * l2 * l3)
        rhs = 0.5 * f * norm2 - f**3
        residual = lhs - rhs
        worst = max(worst, residual)
        if residual > 1e-12:
            failures += 1

    return {
        "samples": samples,
        "failures": failures,
        "max_lhs_minus_rhs": worst,
        "passed": failures == 0,
    }


def spectral_gap_samples(kappa: float = 0.2, samples: int = 1000):
    # kappa must lie below 1/sqrt(6), the endpoint where lambda_2=lambda_3.
    endpoint = 1.0 / math.sqrt(6.0)
    if not (0.0 < kappa < endpoint):
        raise ValueError("Require 0 < kappa < 1/sqrt(6).")

    c_kappa = (math.sqrt(2.0 - 3.0 * kappa * kappa) - 3.0 * kappa) / 2.0
    xs = np.linspace(0.0, kappa, samples + 1)[1:]
    gaps = (np.sqrt(2.0 - 3.0 * xs * xs) - 3.0 * xs) / 2.0
    return {
        "kappa": kappa,
        "c_kappa": c_kappa,
        "minimum_sampled_gap": float(gaps.min()),
        "passed": bool(gaps.min() + 1e-12 >= c_kappa and c_kappa > 0.0),
    }


def run_checks(samples: int = 10000, kappa: float = 0.2):
    symbolic = symbolic_checks()
    ordered = numerical_ordered_inequality(samples=samples)
    gaps = spectral_gap_samples(kappa=kappa)

    all_passed = all(symbolic.values()) and ordered["passed"] and gaps["passed"]

    return {
        "status": (
            "DERIVED ALGEBRAIC AUDIT / MIDDLE-STRAIN SATURATION DEFECT / "
            "NO GLOBAL REGULARITY CLAIM"
        ),
        "symbolic_checks": symbolic,
        "ordered_tracefree_random_audit": ordered,
        "spectral_gap_audit": gaps,
        "exact_defect": "-det(S) = 0.5*lambda_2*|S|^2 - lambda_2^3 when lambda_2>0",
        "global_one_sided_bound": "-det(S) <= 0.5*lambda_2^+*|S|^2 - (lambda_2^+)^3",
        "refined_ledger": (
            "0.5*d/dt||omega||_2^2 + 4||lambda_2^+||_3^3 "
            "<= (C_S||lambda_2^+||_(3/2)-nu)||grad omega||_2^2"
        ),
        "critical_barrier": (
            "positive enstrophy growth requires ||lambda_2^+||_(3/2) > nu/C_S"
        ),
        "passed": all_passed,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", default="results")
    ap.add_argument("--samples", type=int, default=10000)
    ap.add_argument("--kappa", type=float, default=0.2)
    args = ap.parse_args()

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    data = run_checks(samples=args.samples, kappa=args.kappa)
    (out / "middle_strain_saturation_barrier.json").write_text(
        json.dumps(data, indent=2), encoding="utf-8"
    )
    print("Middle-strain saturation barrier:", "PASS" if data["passed"] else "FAIL")
    if not data["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
