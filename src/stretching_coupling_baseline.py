#!/usr/bin/env python3
"""Exact off-diagonal vortex-stretching coupling audit.

Uses two analytic Gaussian double-curl seeds and verifies that the stretching of the
superposed state is not the sum of the self-stretching channels.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def seed(axis, center, amp, X, Y, Z):
    coords=(X,Y,Z)
    q=[coords[i]-sp.sympify(center[i]) for i in range(3)]
    r2=sum(v*v for v in q)
    g=sp.exp(-r2)
    U=[]
    for j in range(3):
        if j==axis:
            U.append(4*amp*(1-sum(q[k]**2 for k in range(3) if k!=axis))*g)
        else:
            U.append(4*amp*q[j]*q[axis]*g)
    U=sp.Matrix(U)
    G=sp.Matrix([[sp.diff(U[i],coords[j]) for j in range(3)] for i in range(3)])
    S=sp.simplify((G+G.T)/2)
    W=sp.Matrix([
        sp.diff(U[2],Y)-sp.diff(U[1],Z),
        sp.diff(U[0],Z)-sp.diff(U[2],X),
        sp.diff(U[1],X)-sp.diff(U[0],Y),
    ])
    return U,S,sp.simplify(W)


def run_checks():
    X,Y,Z=sp.symbols("x y z", real=True)
    u1,S1,w1=seed(2,(0,0,0),sp.Integer(1),X,Y,Z)
    u2,S2,w2=seed(0,(1,0,0),sp.Rational(1,2),X,Y,Z)

    S=S1+S2
    w=w1+w2
    sigma1=sp.factor((w1.T*S1*w1)[0])
    sigma2=sp.factor((w2.T*S2*w2)[0])
    sigma=sp.factor((w.T*S*w)[0])

    cross_expanded=sp.simplify(
        2*(w1.T*S1*w2)[0]
        +(w2.T*S1*w2)[0]
        +(w1.T*S2*w1)[0]
        +2*(w1.T*S2*w2)[0]
    )
    cross_residual=sp.simplify(sigma-sigma1-sigma2-cross_expanded)

    point={X:sp.Rational(1,4),Y:sp.Rational(1,2),Z:0}
    vals={
        "sigma1":sp.simplify(sigma1.subs(point)),
        "sigma2":sp.simplify(sigma2.subs(point)),
        "self_sum":sp.simplify((sigma1+sigma2).subs(point)),
        "cross":sp.simplify(cross_expanded.subs(point)),
        "sigma_total":sp.simplify(sigma.subs(point)),
        "omega_total_squared":sp.simplify((w.T*w)[0].subs(point)),
    }
    vals["gamma_total"]=sp.simplify(vals["sigma_total"]/vals["omega_total_squared"])

    # Exact expected closed forms at the chosen rational point.
    expected_sigma1=sp.Integer(0)
    expected_sigma2=-sp.Rational(2187,128)*sp.exp(-sp.Rational(39,16))
    expected_cross=sp.Rational(37975,128)*sp.exp(-sp.Rational(23,16))
    expected_total=sp.Rational(1,128)*(-2187+37975*sp.E)*sp.exp(-sp.Rational(39,16))

    checks={
        "cross_expansion_identity":bool(cross_residual==0),
        "sigma1_exact":bool(sp.simplify(vals["sigma1"]-expected_sigma1)==0),
        "sigma2_exact":bool(sp.simplify(vals["sigma2"]-expected_sigma2)==0),
        "cross_exact":bool(sp.simplify(vals["cross"]-expected_cross)==0),
        "total_exact":bool(sp.simplify(vals["sigma_total"]-expected_total)==0),
        "self_sum_negative":bool(vals["self_sum"]<0),
        "cross_positive":bool(vals["cross"]>0),
        "total_positive":bool(vals["sigma_total"]>0),
        "cross_flips_sign":bool(vals["self_sum"]<0 and vals["sigma_total"]>0),
        "gamma_total_positive":bool(vals["gamma_total"]>0),
    }

    return {
        "status":"DERIVED IDENTITY + EXACT COUNTER-WITNESS / STRETCHING COUPLING",
        "checks":checks,"passed":sum(bool(v) for v in checks.values()),"total":len(checks),
        "seed_pair":{
            "u1":"z-axis Gaussian double-curl seed at origin, amplitude 1",
            "u2":"x-axis Gaussian double-curl seed centered at (1,0,0), amplitude 1/2",
        },
        "test_point":["1/4","1/2","0"],
        "exact_values":{k:str(v) for k,v in vals.items()},
        "numeric_values":{k:float(sp.N(v,16)) for k,v in vals.items()},
        "cross_identity":(
            "sigma(u1+u2)=sigma1+sigma2+2*w1^T*S1*w2+w2^T*S1*w2+"
            "w1^T*S2*w1+2*w1^T*S2*w2"
        ),
        "interpretation":(
            "At the chosen point the self-stretching sum is negative, while the exact off-diagonal "
            "coupling is positive and large enough to make the total stretching positive. "
            "A DSD dynamic matrix that stores only diagonal/self channels would predict the wrong sign."
        ),
        "proof_boundary":(
            "This is an exact finite analytic witness for one two-seed state. It proves the need to "
            "retain nonlinear stretching cross terms in this representation, not a global bound on them."
        ),
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output-dir",default="results"); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks()
    (out/"stretching_coupling_baseline.json").write_text(json.dumps(d,indent=2),encoding="utf-8")
    n=d["numeric_values"]
    lines=[
        "# Exact vortex-stretching cross-coupling baseline","",
        f"Checks passed: **{d['passed']}/{d['total']}**","",
        "At the rational test point `(1/4,1/2,0)`: ","",
        f"- self sum `sigma1+sigma2 ≈ {n['self_sum']:.12g}`",
        f"- off-diagonal coupling `≈ {n['cross']:.12g}`",
        f"- total stretching `≈ {n['sigma_total']:.12g}`",
        f"- total directional rate `gamma≈{n['gamma_total']:.12g}`","",
        "The exact cross term reverses the sign predicted by the diagonal/self terms alone.","",
        "## Claim boundary","",d["proof_boundary"],
    ]
    (out/"stretching_coupling_baseline.md").write_text("\n".join(lines),encoding="utf-8")
    print(f"Stretching coupling bridge: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=="__main__":
    main()
