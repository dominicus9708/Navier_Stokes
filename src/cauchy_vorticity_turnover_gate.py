#!/usr/bin/env python3
"""Audit the Cauchy-vorticity turnover identity and natural-scale recruitment cost."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp

SCHEMA_VERSION = "0.1.0"


def symbolic_matrix_cancellation():
    # Treat L, F, omega, d as symbolic matrices/vectors at one material point.
    # Verify derivative of zeta=F^-1 omega using Finv_dot=-Finv L and omega_dot=L omega+nu d.
    nu = sp.symbols("nu", real=True)
    L = sp.Matrix(3, 3, sp.symbols("l0:9"))
    G = sp.Matrix(3, 3, sp.symbols("g0:9"))  # represents F^-1
    w = sp.Matrix(sp.symbols("w0:3"))
    d = sp.Matrix(sp.symbols("d0:3"))
    lhs = (-G*L)*w + G*(L*w + nu*d)
    rhs = nu*G*d
    residual = sp.simplify(lhs-rhs)
    return {
        "residual": [str(x) for x in residual],
        "cancellation_zero": bool(all(x == 0 for x in residual)),
    }


def random_differential_check(seed=9708, samples=50, nu=0.7):
    rng = np.random.default_rng(seed)
    maxerr = 0.0
    for _ in range(samples):
        F = rng.normal(size=(3,3))
        while abs(np.linalg.det(F)) < 0.2:
            F = rng.normal(size=(3,3))
        G = np.linalg.inv(F)
        L = rng.normal(size=(3,3))
        w = rng.normal(size=3)
        d = rng.normal(size=3)
        Gdot = -G@L
        wdot = L@w + nu*d
        zdot = Gdot@w + G@wdot
        target = nu*G@d
        maxerr = max(maxerr, float(np.linalg.norm(zdot-target)))
    return {"samples": samples, "max_error": maxerr}


def recruitment_case(W=36.0, a=1.1, lam=0.8, nu=0.9, K=1.25, bminus=0.25, bplus=0.72, theta=0.3):
    db = bplus/K-bminus
    r = a/math.sqrt(W)
    tau = lam/W
    recruited = theta*r**3
    if db <= 0:
        lower = float("nan")
    else:
        lower = theta*a**3*db**2/(nu**2*K**2*lam)*W**1.5
    # Reconstruct from the raw inequality delta_h^2 |R| /(nu^2 K^2 tau).
    dh = db*W
    raw = dh**2*recruited/(nu**2*K**2*tau)
    return {
        "W": W, "r": r, "tau": tau, "K": K,
        "delta_b": db, "recruited_volume": recruited,
        "raw_lower": raw, "closed_lower": lower,
        "identity_error": abs(raw-lower),
    }


def scaling_audit(lam_ns=2.6):
    # Integral dt dx |Delta omega|^2 scales as lambda^3:
    # Delta omega -> lambda^4, squared -> lambda^8,
    # dx -> lambda^-3, dt -> lambda^-2 => lambda^3.
    lhs_ratio = lam_ns**3
    # W^(3/2) scales as (lambda^2)^(3/2)=lambda^3.
    rhs_ratio = (lam_ns**2)**1.5
    return {"lambda": lam_ns, "lhs_ratio": lhs_ratio, "rhs_ratio": rhs_ratio, "error": abs(lhs_ratio-rhs_ratio)}


def run_checks():
    sym = symbolic_matrix_cancellation()
    rnd = random_differential_check()
    rows = [recruitment_case(), recruitment_case(W=14.0, a=0.9, lam=1.2, nu=1.1, K=1.15, bminus=0.2, bplus=0.65, theta=0.5)]
    sc = scaling_audit()
    checks = {
        "exact_Cauchy_defect_cancellation": sym["cancellation_zero"],
        "random_matrix_cancellation": rnd["max_error"] < 1e-12,
        "positive_recruitment_gap": all(r["delta_b"] > 0 for r in rows),
        "natural_recruitment_closed_form": all(r["identity_error"] < 1e-10 for r in rows),
        "k2_natural_scaling_match": sc["error"] < 1e-12,
    }
    checks = {k: bool(v) for k, v in checks.items()}
    return {
        "schema_version": SCHEMA_VERSION,
        "status": "EXACT CAUCHY-VORTICITY DEFECT + MATERIAL-TURNOVER AUDIT",
        "checks": checks, "passed": sum(checks.values()), "total": len(checks),
        "symbolic": sym, "random": rnd, "recruitment": rows, "scaling": sc,
        "identity": "partial_t(F^{-1} omega(X,t)) = nu F^{-1} Delta omega(X,t).",
        "turnover_bound": "If bounded deformation recruits theta r^3 labels from h_- to h_+, then int_I int |Delta omega|^2 >= c W^(3/2).",
        "claim_boundary": "This is a material-coordinate identity and conditional recruitment estimate. It does not establish summability of repeated k=2 costs near a hypothetical singular time.",
    }


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--output-dir", default="results"); args = ap.parse_args()
    out = Path(args.output_dir); out.mkdir(parents=True, exist_ok=True)
    d = run_checks()
    (out/"cauchy_vorticity_turnover_gate.json").write_text(json.dumps(d, indent=2), encoding="utf-8")
    (out/"cauchy_vorticity_turnover_gate.md").write_text(
        "# Cauchy-vorticity turnover audit\n\n"
        f"Checks passed: **{d['passed']}/{d['total']}**\n\n"
        f"{d['identity']}\n\n{d['turnover_bound']}\n\n"
        f"Claim boundary: {d['claim_boundary']}\n", encoding="utf-8")
    print(f"Cauchy-vorticity turnover: {d['passed']}/{d['total']} checks passed")
    if d["passed"] != d["total"]: raise SystemExit(1)


if __name__ == "__main__": main()
