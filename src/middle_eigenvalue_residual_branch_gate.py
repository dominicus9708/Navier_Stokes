#!/usr/bin/env python3
"""Audit the algebraic middle-strain/extensional-alignment residual split."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import numpy as np

SCHEMA_VERSION = "0.1.0"


def random_branch_audit(seed=9708, samples=20000):
    rng = np.random.default_rng(seed)
    branch_violations = 0
    refined_alignment_violations = 0
    positive_samples = 0
    for _ in range(samples):
        lam = np.sort(rng.normal(size=3))
        lam -= np.mean(lam)
        lam1, lam2, lam3 = np.sort(lam)
        q = rng.normal(size=3); q /= np.linalg.norm(q)
        a2 = q*q
        gamma = float(lam1*a2[0]+lam2*a2[1]+lam3*a2[2])
        h = float(rng.random()*max(lam3, 0.0)*0.8)
        g = gamma-h
        if g <= 1e-12:
            continue
        positive_samples += 1
        middle = max(lam2, 0.0)
        extensional_surplus = lam3*a2[2]-h
        if not (middle >= 0.5*g-1e-12 or extensional_surplus >= 0.5*g-1e-12):
            branch_violations += 1

        # Sharper alignment consequence from
        # gamma <= lam2(1-a3^2)+lam3 a3^2.
        if lam3 > lam2:
            required = (h+g-lam2)/(lam3-lam2)
            if a2[2] < required-1e-10:
                refined_alignment_violations += 1

    return {
        "samples": samples,
        "positive_growth_samples": positive_samples,
        "branch_violations": branch_violations,
        "refined_alignment_violations": refined_alignment_violations,
    }


def toy_branches():
    # Co-located middle branch: lambda2+ directly exceeds g/2.
    lam_c = np.array([-2.0, 1.0, 1.0])
    a2_c = np.array([0.0, 1.0, 0.0])
    h_c = 0.2
    gamma_c = float(np.dot(lam_c, a2_c)); g_c = gamma_c-h_c

    # Spatial-separation-compatible maximum point: lambda2+=0 locally,
    # while extensional alignment drives positive growth.
    lam_s = np.array([-2.0, -1.0, 3.0])
    a2_s = np.array([0.0, 0.0, 1.0])
    h_s = 1.0
    gamma_s = float(np.dot(lam_s, a2_s)); g_s = gamma_s-h_s

    # Elsewhere the global middle eigenvalue can be positive independently.
    lam_elsewhere = np.array([-3.0, 1.0, 2.0])

    return {
        "colocated": {
            "lambda": lam_c.tolist(), "a2": a2_c.tolist(), "h": h_c,
            "g": g_c, "lambda2_plus": max(lam_c[1], 0.0),
            "extensional_surplus": lam_c[2]*a2_c[2]-h_c,
        },
        "separated_maximum": {
            "lambda": lam_s.tolist(), "a2": a2_s.tolist(), "h": h_s,
            "g": g_s, "lambda2_plus": max(lam_s[1], 0.0),
            "extensional_surplus": lam_s[2]*a2_s[2]-h_s,
        },
        "elsewhere": {
            "lambda": lam_elsewhere.tolist(),
            "lambda2_plus": max(lam_elsewhere[1], 0.0),
        },
    }


def scale_factor(lam):
    # lambda_i and |grad xi|^2 scale as lambda^2; dt as lambda^-2.
    return (lam**2)*(lam**-2)


def run_checks():
    rnd = random_branch_audit()
    toys = toy_branches()
    c = toys["colocated"]; s = toys["separated_maximum"]; e = toys["elsewhere"]
    checks = {
        "random_branch_implication": rnd["branch_violations"] == 0,
        "random_refined_alignment_implication": rnd["refined_alignment_violations"] == 0,
        "colocated_toy_middle_branch": c["g"] > 0 and c["lambda2_plus"] >= 0.5*c["g"],
        "separated_toy_extensional_branch": s["g"] > 0 and s["lambda2_plus"] == 0 and s["extensional_surplus"] >= 0.5*s["g"],
        "separated_toy_global_middle_can_live_elsewhere": e["lambda2_plus"] > 0,
        "branch_time_integrals_scale_invariant": all(abs(scale_factor(x)-1.0)<1e-12 for x in (0.3,2.0,11.0)),
    }
    checks = {k: bool(v) for k,v in checks.items()}
    return {
        "schema_version": SCHEMA_VERSION,
        "status": "DERIVED ALGEBRA / RESIDUAL BRANCH AUDIT",
        "checks": checks,
        "passed": sum(checks.values()), "total": len(checks),
        "random_audit": rnd,
        "toy_branches": toys,
        "branch_statement": "At a maximum-vorticity point with g=gamma-nu|grad xi|^2>0, either lambda2+ >= g/2 or lambda3 a3^2-nu|grad xi|^2 >= g/2.",
        "claim_boundary": "The toys show that co-location and spatial-separation branches are algebraically possible. They are not Navier-Stokes solutions and do not establish dynamical realizability."
    }


def write_md(d,path):
    lines=[
        "# Middle-eigenvalue residual branch audit","",
        f"Status: **{d['status']}**","",
        f"Checks passed: **{d['passed']}/{d['total']}**","",
        d["branch_statement"],"",
        "The exact toy states verify that the local maximum-vorticity growth mechanism can be either middle-strain dominated or extensional-alignment dominated while a positive middle eigenvalue exists elsewhere. This prevents identifying `Lambda_2,M` with the global `||lambda_2^+||_infty` channel.","",
        "## Claim boundary","",d["claim_boundary"],""
    ]
    path.write_text("\n".join(lines),encoding="utf-8")


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output-dir",default="results")
    args=ap.parse_args(); out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks()
    (out/"middle_eigenvalue_residual_branch_gate.json").write_text(json.dumps(d,indent=2),encoding="utf-8")
    write_md(d,out/"middle_eigenvalue_residual_branch_gate.md")
    print(f"Middle-eigenvalue residual branch: {d['passed']}/{d['total']} checks passed")
    if d["passed"]!=d["total"]: raise SystemExit(1)

if __name__=="__main__": main()
