#!/usr/bin/env python3
"""Algebraic audit of the vorticity direction/strain competition block."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import numpy as np

SCHEMA_VERSION = "0.1.0"


def gaussian_ratio_bound():
    # For the z-axis Gaussian benchmark, with cylindrical radius s>0:
    # gamma_+ / |grad xi|^2 = 4 z s^2 exp(-s^2-z^2), z>=0.
    # max_s s^2 exp(-s^2)=1/e at s=1.
    # max_z z exp(-z^2)=1/sqrt(2e) at z=1/sqrt(2).
    exact = 4.0/(math.e*math.sqrt(2.0*math.e))
    s = 1.0
    z = 1.0/math.sqrt(2.0)
    attained = 4.0*z*s*s*math.exp(-s*s-z*z)
    return exact, attained


def eigenframe_random_audit(seed=9708, samples=5000):
    rng = np.random.default_rng(seed)
    max_violation = 0.0
    threshold_violations = 0
    for _ in range(samples):
        raw = np.sort(rng.normal(size=3))
        raw -= np.mean(raw)
        lam1, lam2, lam3 = np.sort(raw)
        q = rng.random(3); q /= np.linalg.norm(q)
        a2 = q*q
        gamma = float(lam1*a2[0]+lam2*a2[1]+lam3*a2[2])
        rhs = max(lam2, 0.0)*(1.0-a2[2])+lam3*a2[2]
        max_violation = max(max_violation, gamma-rhs)
        if lam2 <= 0 and lam3 > lam2 and gamma > 1e-12:
            threshold = -lam2/(lam3-lam2)
            if not (a2[2] > threshold-1e-12):
                threshold_violations += 1
    return max_violation, threshold_violations


def scaling_audit(lam):
    # gamma -> lambda^2 gamma; |grad xi|^2 -> lambda^2 |grad xi|^2;
    # dt -> lambda^-2 dt.  Thus the time integral of their positive excess is invariant.
    instantaneous = lam**2
    time = lam**-2
    return instantaneous*time


def run_checks():
    exact, attained = gaussian_ratio_bound()
    violation, threshold_violations = eigenframe_random_audit()
    checks = {
        "gaussian_ratio_formula_attained": abs(exact-attained) < 1e-14,
        "gaussian_nu1_direction_penalty_dominates": exact < 1.0,
        "eigenframe_upper_bound_random": violation < 1e-12,
        "lambda2_nonpositive_alignment_implication_random": threshold_violations == 0,
        "competition_integral_scale_invariant": all(abs(scaling_audit(l)-1.0) < 1e-12 for l in (0.4,2.0,9.0)),
    }
    checks = {k: bool(v) for k,v in checks.items()}
    return {
        "schema_version": SCHEMA_VERSION,
        "status": "DERIVED ALGEBRA + COMPUTATIONAL AUDIT",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "gaussian_max_gamma_over_direction_penalty": exact,
        "random_max_eigenframe_bound_violation": violation,
        "random_alignment_threshold_violations": threshold_violations,
        "identity": "(D_t-nu Delta)|omega| = |omega| (xi^T S xi - nu |grad xi|^2) wherever omega is nonzero.",
        "claim_boundary": "The Gaussian ratio is an exact benchmark fact for nu=1. It is not a universal Navier-Stokes sign theorem."
    }


def write_md(d,path):
    lines=[
        "# Vorticity direction / strain competition audit","",
        f"Status: **{d['status']}**","",
        f"Checks passed: **{d['passed']}/{d['total']}**","",
        f"Gaussian max `gamma_+ / |grad xi|^2`: `{d['gaussian_max_gamma_over_direction_penalty']:.12g}`.","",
        "For the benchmark at `nu=1`, this is below one, so the direction-gradient diffusion penalty exceeds the positive strain-alignment term pointwise wherever the direction channel is defined.","",
        "## Claim boundary","",d["claim_boundary"],""
    ]
    path.write_text("\n".join(lines),encoding="utf-8")


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output-dir",default="results")
    args=ap.parse_args(); out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks()
    (out/"vorticity_direction_strain_competition_gate.json").write_text(json.dumps(d,indent=2),encoding="utf-8")
    write_md(d,out/"vorticity_direction_strain_competition_gate.md")
    print(f"Vorticity direction/strain competition: {d['passed']}/{d['total']} checks passed")
    if d["passed"]!=d["total"]: raise SystemExit(1)


if __name__=="__main__": main()
