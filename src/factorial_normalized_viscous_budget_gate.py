#!/usr/bin/env python3
"""Audit the factorial-normalized viscous derivative-order budget."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import numpy as np

SCHEMA_VERSION = "0.1.0"


def radius_certificate(E0=2.5, R=1.7, K=10):
    # Saturating model: rho_k = R^-2, so E_k = E0 (k!)^2 R^-2k.
    E = [E0 * (math.factorial(k) ** 2) * (R ** (-2 * k)) for k in range(K + 1)]
    rho = []
    for k in range(K):
        r = E[k + 1] / E[k]
        rho.append(r / ((k + 1) ** 2))
    return {"E": E, "rho": rho, "target": R ** -2, "max_error": max(abs(x - R ** -2) for x in rho)}


def positive_block_budget(nu=0.9, R=1.4):
    # Use the same monotone covariance block as the raw viscous-flux audit.
    a = np.linspace(0.55, 0.91, 7)
    C = [np.diag([x, (1.0 - x) / 2.0, (1.0 - x) / 2.0]) for x in a]
    A = []
    for k in range(len(C) - 1):
        A.append(float(np.trace(C[k] @ C[k + 1]) - np.trace(C[k] @ C[k])))
    # Saturate rho_k <= R^-2.
    rho = [R ** -2 for _ in A]
    Vhat = [nu * rho[k] * A[k] for k in range(len(A))]
    total = float(sum(Vhat))
    bound = nu / (3.0 * R * R)
    return {"A": A, "rho": rho, "sum_Vhat": total, "bound": bound, "margin": bound - total}


def log_convexity_audit(seed=9708, nfreq=200, K=8):
    rng = np.random.default_rng(seed)
    radii = np.exp(rng.normal(size=nfreq))
    weights = rng.random(nfreq) + 0.01
    # Fourier-moment model E_k = sum w r^{2k}.
    E = [float(np.sum(weights * radii ** (2 * k))) for k in range(K + 1)]
    residual = []
    for k in range(1, K):
        residual.append(E[k - 1] * E[k + 1] - E[k] ** 2)
    raw_ratios = [E[k + 1] / E[k] for k in range(K)]
    monotone = all(raw_ratios[k + 1] + 1e-12 >= raw_ratios[k] for k in range(len(raw_ratios) - 1))
    return {"E": E, "residual": residual, "min_residual": min(residual), "raw_ratios": raw_ratios, "monotone": monotone}


def generating_series_bound(E0=1.3, R=1.8, tau=1.2, K=20):
    E = [E0 * (math.factorial(k) ** 2) * R ** (-2 * k) for k in range(K + 1)]
    partial = sum((tau ** (2 * k)) * E[k] / (math.factorial(k) ** 2) for k in range(K + 1))
    geometric_infinite = E0 / (1.0 - (tau / R) ** 2)
    return {"partial": partial, "infinite_bound": geometric_infinite, "margin": geometric_infinite - partial}


def run_checks():
    rad = radius_certificate()
    block = positive_block_budget()
    logc = log_convexity_audit()
    series = generating_series_bound()
    checks = {
        "factorial_ratio_certificate": rad["max_error"] < 1e-12,
        "positive_block_factorial_budget": block["margin"] >= -1e-12,
        "moment_log_convexity": logc["min_residual"] >= -1e-8,
        "raw_ratio_monotonicity": logc["monotone"],
        "factorial_generating_series_bound": series["margin"] >= -1e-12,
    }
    checks = {k: bool(v) for k, v in checks.items()}
    return {
        "schema_version": SCHEMA_VERSION,
        "status": "DERIVED FACTORIAL V-BUDGET / COMPUTATIONAL ALGEBRA AUDIT",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "radius_certificate": rad,
        "positive_block": block,
        "log_convexity": logc,
        "series": series,
        "identity": "rho_k = (E_{k+1}/E_k)/(k+1)^2 = Ehat_{k+1}/Ehat_k.",
        "budget": "If rho_k<=R^-2 on a positive-V block, sum V_k/(k+1)^2 <= nu/(3R^2).",
        "claim_boundary": "This is a factorial derivative-radius and positive-V budget audit, not a proof that rho_k remains uniformly bounded for Navier-Stokes solutions.",
    }


def write_md(d, path: Path):
    b = d["positive_block"]
    lines = [
        "# Factorial-normalized viscous budget audit",
        "",
        f"Status: **{d['status']}**",
        "",
        f"Checks passed: **{d['passed']}/{d['total']}**",
        "",
        d["identity"],
        "",
        d["budget"],
        "",
        f"Positive-block audit: sum=`{b['sum_Vhat']:.8g}`, bound=`{b['bound']:.8g}`, margin=`{b['margin']:.8g}`.",
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
    (out / "factorial_normalized_viscous_budget_gate.json").write_text(json.dumps(d, indent=2), encoding="utf-8")
    write_md(d, out / "factorial_normalized_viscous_budget_gate.md")
    print(f"Factorial-normalized viscous budget: {d['passed']}/{d['total']} checks passed")
    if d["passed"] != d["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
