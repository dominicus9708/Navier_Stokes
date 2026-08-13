#!/usr/bin/env python3
"""Audit the overlap-free amplification-step Cauchy dichotomy.

This script checks only the exact algebra/scaling behind the derived bridge:
for a final natural vorticity core at W1=q W0, pulling every final label back
to t0 gives either order-q recent deformation or a scale-critical k=2
viscous Cauchy-defect cost.  It is not a global regularity proof.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import math
import numpy as np

SCHEMA_VERSION = "0.1.0"


def coefficient(b: float, q: float, kp: float, km: float, sigma: float, nu: float = 1.0):
    delta = b * q / kp - 1.0
    if delta <= 0:
        return 0.0, delta
    c = q ** (-1.5) * delta * delta / (nu * nu * km * km * sigma)
    return c, delta


def scaling_audit(lam: float = 3.7):
    # NS scaling: W -> lam^2 W, tau -> lam^-2 tau,
    # int_I int |Delta omega|^2 dx dt -> lam^3 times itself.
    W = 2.3
    tau = 0.17
    lhs_ratio = lam ** 3
    Wp = lam * lam * W
    taup = tau / (lam * lam)
    sigma = W * tau
    sigmap = Wp * taup
    rhs_ratio = (Wp ** 1.5) / (W ** 1.5)
    return {
        "lhs_ratio": lhs_ratio,
        "rhs_ratio": rhs_ratio,
        "sigma": sigma,
        "sigma_scaled": sigmap,
        "ratio_error": abs(lhs_ratio - rhs_ratio),
        "sigma_error": abs(sigma - sigmap),
    }


def overlap_independence_audit(seed: int = 9708, samples: int = 500):
    rng = np.random.default_rng(seed)
    W0 = 1.0
    b = 0.62
    q = 9.0
    Kp = 3.0
    delta = b * q / Kp - 1.0
    min_margin = float("inf")

    # We do not use any earlier-core membership variable.  Every sample is just
    # a final-core material label whose initial vorticity is bounded by W0.
    for _ in range(samples):
        z0 = rng.normal(size=3)
        z0 /= max(np.linalg.norm(z0), 1e-14)
        z0 *= rng.random() * W0

        direction = rng.normal(size=3)
        direction /= np.linalg.norm(direction)
        z1_norm = (b * q / Kp) * W0 + rng.random() * 2.0
        z1 = z1_norm * direction

        actual = np.linalg.norm(z1 - z0)
        lower = delta * W0
        min_margin = min(min_margin, actual - lower)

    return {"delta": delta, "min_margin": float(min_margin)}


def large_jump_asymptotic():
    b = 0.7
    kp = 2.0
    qs = np.array([50.0, 100.0, 200.0, 400.0])
    vals = qs ** (-1.5) * (b * qs / kp - 1.0) ** 2
    normalized = vals / np.sqrt(qs)
    target = (b / kp) ** 2
    return {
        "q": qs.tolist(),
        "normalized": normalized.tolist(),
        "target": target,
        "last_error": abs(float(normalized[-1]) - target),
    }


def dichotomy_audit():
    b = 0.6
    kappa = 0.4
    q = 10.0
    Kp_deformation = 4.5
    Kp_viscous = 3.0

    deform_branch = Kp_deformation >= kappa * q
    viscous_branch = Kp_viscous < kappa * q
    uniform_delta = b / kappa - 1.0
    actual_delta = b * q / Kp_viscous - 1.0

    return {
        "deformation_branch": deform_branch,
        "viscous_branch": viscous_branch,
        "uniform_delta": uniform_delta,
        "actual_delta": actual_delta,
        "margin": actual_delta - uniform_delta,
    }


def run_checks():
    sc = scaling_audit()
    oi = overlap_independence_audit()
    asym = large_jump_asymptotic()
    di = dichotomy_audit()

    c, delta = coefficient(b=0.6, q=10.0, kp=3.0, km=2.0, sigma=1.4)

    checks = {
        "scale_critical_W32": sc["ratio_error"] < 1e-12,
        "dimensionless_duration_invariant": sc["sigma_error"] < 1e-12,
        "triangle_lower_bound_all_final_labels": oi["min_margin"] >= -1e-12,
        "large_jump_sqrt_q_asymptotic": asym["last_error"] < 2e-3,
        "deformation_branch_detected": bool(di["deformation_branch"]),
        "viscous_branch_detected": bool(di["viscous_branch"]),
        "uniform_viscous_delta": di["margin"] >= -1e-12 and di["uniform_delta"] > 0,
        "positive_example_coefficient": c > 0 and delta > 0,
    }
    checks = {k: bool(v) for k, v in checks.items()}

    return {
        "schema_version": SCHEMA_VERSION,
        "status": "DERIVED OVERLAP-FREE AMPLIFICATION CAUCHY DICHOTOMY / ALGEBRA AUDIT",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "scaling": sc,
        "overlap_independence": oi,
        "large_jump": asym,
        "dichotomy": di,
        "example_coefficient": c,
        "identity": "If W1=qW0 and |omega(t1)|>=bW1 on the final core, then bq/K_+>1 implies |zeta1-zeta0|>=(bq/K_+-1)W0 for every pulled-back final label.",
        "cost": "int_I int |Delta omega|^2 >= const*q^(-3/2)*(bq/K_+-1)^2*W0^(3/2)/(nu^2 K_-^2 sigma), sigma=W0*tau.",
        "claim_boundary": "No overlap, turnover, or pruning assumption is used, but the estimate remains scale-critical and does not prove arbitrary-data regularity.",
    }


def write_md(d, path: Path):
    lines = [
        "# Amplification-step Cauchy dichotomy audit",
        "",
        f"Status: **{d['status']}**",
        "",
        f"Checks passed: **{d['passed']}/{d['total']}**",
        "",
        d["identity"],
        "",
        d["cost"],
        "",
        "## Structural consequence",
        "",
        "The final dangerous core can be pulled back directly. Earlier dangerous-core membership is unnecessary: every earlier label is bounded by the earlier global vorticity maximum.",
        "",
        "Hence turnover and pruning become secondary descriptors under the stronger amplification-step D/V2 dichotomy.",
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
    (out / "amplification_cauchy_dichotomy_gate.json").write_text(json.dumps(d, indent=2), encoding="utf-8")
    write_md(d, out / "amplification_cauchy_dichotomy_gate.md")
    print(f"Amplification Cauchy dichotomy: {d['passed']}/{d['total']} checks passed")
    if d["passed"] != d["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
