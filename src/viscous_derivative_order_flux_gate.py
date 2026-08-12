#!/usr/bin/env python3
"""Audit the exact neighboring-covariance viscous flux identity."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import numpy as np

SCHEMA_VERSION = "0.1.0"


def random_covariance(rng):
    M = rng.normal(size=(3, 3))
    C = M @ M.T
    C /= np.trace(C)
    return C


def pair_identity_audit(seed=9708, samples=200):
    rng = np.random.default_rng(seed)
    max_error = 0.0
    sign_violations = 0
    rows = []
    for _ in range(samples):
        C = random_covariance(rng)
        D = random_covariance(rng)
        J = float(1.0 - np.trace(C @ C))
        Jn = float(1.0 - np.trace(D @ D))
        delta2 = float(np.linalg.norm(D - C) ** 2)
        A = float(np.trace(C @ D) - np.trace(C @ C))
        pred = 0.5 * (J - Jn - delta2)
        err = abs(A - pred)
        max_error = max(max_error, err)
        if A > 1e-12 and not (Jn < J - delta2 + 1e-12):
            sign_violations += 1
        if len(rows) < 5:
            rows.append({"J_k": J, "J_next": Jn, "Delta2": delta2, "A": A, "predicted": pred, "error": err})
    return {"max_error": max_error, "sign_violations": sign_violations, "samples": rows}


def positive_block():
    # A monotone family becoming increasingly one-axis concentrated.
    a = np.linspace(0.55, 0.91, 7)
    C = [np.diag([x, (1.0 - x) / 2.0, (1.0 - x) / 2.0]) for x in a]
    Js = [float(1.0 - np.trace(M @ M)) for M in C]
    As = []
    deltas2 = []
    for k in range(len(C) - 1):
        d2 = float(np.linalg.norm(C[k + 1] - C[k]) ** 2)
        Ak = float(np.trace(C[k] @ C[k + 1]) - np.trace(C[k] @ C[k]))
        As.append(Ak)
        deltas2.append(d2)
    lhs = float(sum(As))
    rhs = 0.5 * (Js[0] - Js[-1] - sum(deltas2))
    return {
        "J": Js,
        "A": As,
        "Delta2": deltas2,
        "all_positive": bool(all(v > 0 for v in As)),
        "sum_A": lhs,
        "telescoped": rhs,
        "telescoping_error": abs(lhs - rhs),
        "one_third_margin": 1.0 / 3.0 - lhs,
    }


def quantitative_length_bound(nu=0.7, R=4.0, eta=0.02):
    # Pure algebraic implication: if V_k=nu r_k A_k>=eta and r_k<=R,
    # then A_k>=eta/(nu R), so a positive block has bounded length.
    max_length = nu * R / (3.0 * eta)
    per_link_A = eta / (nu * R)
    return {"nu": nu, "R": R, "eta": eta, "per_link_A": per_link_A, "max_length": max_length}


def run_checks():
    rnd = pair_identity_audit()
    block = positive_block()
    q = quantitative_length_bound()
    checks = {
        "neighbor_identity_random": rnd["max_error"] < 1e-12,
        "positive_A_forces_dispersion_drop": rnd["sign_violations"] == 0,
        "constructed_positive_block": block["all_positive"],
        "positive_block_telescopes": block["telescoping_error"] < 1e-12,
        "positive_block_budget_below_one_third": block["one_third_margin"] >= -1e-12,
        "quantitative_length_formula_positive": q["max_length"] > 0 and q["per_link_A"] > 0,
    }
    checks = {k: bool(v) for k, v in checks.items()}
    return {
        "schema_version": SCHEMA_VERSION,
        "status": "DERIVED VISCOUS DERIVATIVE-ORDER FLUX / COMPUTATIONAL ALGEBRA AUDIT",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "random_audit": rnd,
        "positive_block": block,
        "length_bound_example": q,
        "identity": "A_k = tr(C_k C_{k+1})-tr(C_k^2) = 0.5[J_k-J_{k+1}-||C_{k+1}-C_k||_F^2].",
        "flux_form": "Jdot_k + 2 nu r_k Delta_k^2 = 4 M_N,k - 2 nu r_k (J_{k+1}-J_k).",
        "claim_boundary": "The geometric positive-V budget is unweighted in derivative order. Large r_k can still amplify the actual viscous rate; controlling that escalation remains open.",
    }


def write_md(d, path: Path):
    b = d["positive_block"]
    lines = [
        "# Viscous derivative-order flux audit",
        "",
        f"Status: **{d['status']}**",
        "",
        f"Checks passed: **{d['passed']}/{d['total']}**",
        "",
        d["identity"],
        "",
        d["flux_form"],
        "",
        f"Constructed positive block: sum A=`{b['sum_A']:.8g}`, telescoping error=`{b['telescoping_error']:.3e}`, one-third margin=`{b['one_third_margin']:.8g}`.",
        "",
        "## Claim boundary",
        "",
        d["claim_boundary"],
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", default="results")
    args = ap.parse_args()
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    d = run_checks()
    (out / "viscous_derivative_order_flux_gate.json").write_text(json.dumps(d, indent=2), encoding="utf-8")
    write_md(d, out / "viscous_derivative_order_flux_gate.md")
    print(f"Viscous derivative-order flux: {d['passed']}/{d['total']} checks passed")
    if d["passed"] != d["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
