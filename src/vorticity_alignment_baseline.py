#!/usr/bin/env python3
"""Vorticity-direction / strain-axis bridge for the DSD-assisted Navier-Stokes audit.

Exact benchmark identities plus deterministic eigenframe checks.
No general regularity claim is made.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp


def symbolic_identities() -> dict:
    x,y,z=sp.symbols("x y z", real=True)
    rho2=x*x+y*y
    r2=rho2+z*z
    g=sp.exp(-r2)
    coords=(x,y,z)
    u=sp.Matrix([4*x*z*g,4*y*z*g,4*(1-x*x-y*y)*g])
    G=sp.Matrix([[sp.diff(u[i],coords[j]) for j in range(3)] for i in range(3)])
    S=sp.simplify((G+G.T)/2)
    omega=sp.Matrix([
        sp.diff(u[2],y)-sp.diff(u[1],z),
        sp.diff(u[0],z)-sp.diff(u[2],x),
        sp.diff(u[1],x)-sp.diff(u[0],y),
    ])
    omega_expected=4*(2*r2-5)*g*sp.Matrix([y,-x,0])
    omega2=sp.factor((omega.T*omega)[0])
    sigma=sp.factor((omega.T*S*omega)[0])

    # This xi is a representative of the local azimuthal line.  It equals the
    # signed vorticity direction only after multiplication by sign(2r^2-5).
    xi_line=sp.Matrix([y,-x,0])/sp.sqrt(rho2)
    gamma_line=sp.factor((xi_line.T*S*xi_line)[0])
    gamma_expected=4*z*g

    return {
        "omega_formula_match": bool(all(sp.simplify(v)==0 for v in omega-omega_expected)),
        "omega_squared": str(omega2),
        "stretching_sigma": str(sigma),
        "azimuthal_line_rate": str(gamma_line),
        "azimuthal_line_rate_match": bool(sp.simplify(gamma_line-gamma_expected)==0),
        "factorization_match": bool(sp.simplify(sigma-omega2*gamma_expected)==0),
        "vorticity_zero_set": "x^2+y^2=0 OR 2*(x^2+y^2+z^2)-5=0",
        "removable_extension": str(gamma_expected),
        "typing_warning": (
            "gamma=sigma/|omega|^2 and xi=omega/|omega| are applicable only where |omega|>0. "
            "The simplified expression 4*z*exp(-r^2) is a removable algebraic extension across "
            "parts of the vorticity-zero set, not a defined vorticity-direction channel there."
        ),
    }


def field_and_strain(point):
    x,y,z=point
    r2=x*x+y*y+z*z
    g=math.exp(-r2)
    u=np.array([4*x*z*g,4*y*z*g,4*(1-x*x-y*y)*g],dtype=float)

    # Analytic gradient generated once from the exact seed formulas.
    # Rows: velocity component; columns: x,y,z derivatives.
    G=np.array([
        [4*z*g*(1-2*x*x), -8*x*y*z*g, 4*x*g*(1-2*z*z)],
        [-8*x*y*z*g, 4*z*g*(1-2*y*y), 4*y*g*(1-2*z*z)],
        [8*x*g*(x*x+y*y-2), 8*y*g*(x*x+y*y-2), -8*z*g*(1-x*x-y*y)],
    ],dtype=float)
    S=0.5*(G+G.T)
    omega=4*(2*r2-5)*g*np.array([y,-x,0.0])
    return u,S,omega


def typed_alignment(point,tol=1e-12):
    _,S,omega=field_and_strain(point)
    wmag=float(np.linalg.norm(omega))
    evals,evecs=np.linalg.eigh(S)
    if wmag<=tol:
        return {
            "point":list(point),
            "status":"undefined/inapplicable",
            "omega_magnitude":wmag,
            "strain_eigenvalues":[float(v) for v in evals],
            "reason":"vorticity direction xi=omega/|omega| is undefined where |omega|=0",
        }
    xi=omega/wmag
    align=np.array([(float(np.dot(xi,evecs[:,i])))**2 for i in range(3)])
    gamma=float(xi@S@xi)
    spectral_gamma=float(np.dot(evals,align))
    sigma=float(omega@S@omega)
    return {
        "point":list(point),
        "status":"defined",
        "omega_magnitude":wmag,
        "xi":[float(v) for v in xi],
        "strain_eigenvalues":[float(v) for v in evals],
        "alignment_weights":[float(v) for v in align],
        "alignment_sum":float(np.sum(align)),
        "gamma_xi_S_xi":gamma,
        "gamma_spectral_sum":spectral_gamma,
        "gamma_closed_form":4*point[2]*math.exp(-sum(q*q for q in point)),
        "sigma":sigma,
        "sigma_factorized":wmag*wmag*gamma,
    }


def run_checks() -> dict:
    sym=symbolic_identities()
    defined_points=[(1.0,0.0,1.0),(1.0,0.0,-1.0),(1.0,0.0,0.0),(0.7,0.4,0.8)]
    undefined_points=[
        (0.0,0.0,1.0), # z axis: x^2+y^2=0
        (1.0,0.0,math.sqrt(1.5)), # r^2=5/2 vorticity-zero shell
    ]
    drows=[typed_alignment(p) for p in defined_points]
    urows=[typed_alignment(p) for p in undefined_points]

    checks={
        "omega_formula":sym["omega_formula_match"],
        "gamma_closed_form":sym["azimuthal_line_rate_match"],
        "sigma_factorization":sym["factorization_match"],
        "defined_alignment_weights_sum_one":all(abs(r["alignment_sum"]-1.0)<1e-12 for r in drows),
        "defined_spectral_reconstruction":all(abs(r["gamma_xi_S_xi"]-r["gamma_spectral_sum"])<1e-12 for r in drows),
        "defined_closed_form_reconstruction":all(abs(r["gamma_xi_S_xi"]-r["gamma_closed_form"])<1e-12 for r in drows),
        "defined_sigma_reconstruction":all(abs(r["sigma"]-r["sigma_factorized"])<1e-11 for r in drows),
        "positive_negative_zero_samples":bool(drows[0]["gamma_xi_S_xi"]>0 and drows[1]["gamma_xi_S_xi"]<0 and abs(drows[2]["gamma_xi_S_xi"])<1e-12),
        "zero_vorticity_typed_undefined":all(r["status"]=="undefined/inapplicable" for r in urows),
        "strain_trace_zero_samples":all(abs(sum(r["strain_eigenvalues"]))<1e-12 for r in drows+urows),
    }
    return {
        "status":"DERIVED IDENTITY + COMPUTATIONAL CHECK / VORTICITY-DIRECTION AXIS BRIDGE",
        "checks":checks,"passed":sum(bool(v) for v in checks.values()),"total":len(checks),
        "symbolic":sym,
        "defined_samples":drows,
        "undefined_samples":urows,
        "channel_factorization":{
            "magnitude_channel":"|omega|^2",
            "direction_channel":"xi=omega/|omega| (only where |omega|>0)",
            "strain_axis_channels":"lambda_i, e_i from S e_i=lambda_i e_i",
            "alignment_channels":"a_i=(xi dot e_i)^2, sum_i a_i=1",
            "directional_stretch_rate":"gamma=sum_i lambda_i a_i=xi^T S xi",
            "stretching":"sigma=|omega|^2 gamma",
        },
        "proof_boundary":(
            "This exact decomposition exposes magnitude, direction, eigenvalue and alignment channels. "
            "It does not prove that these channels remain controlled for arbitrary Navier-Stokes data."
        ),
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output-dir",default="results"); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks()
    (out/"vorticity_alignment_baseline.json").write_text(json.dumps(d,indent=2),encoding="utf-8")
    lines=[
        "# Vorticity-direction / strain-axis baseline","",
        f"Checks passed: **{d['passed']}/{d['total']}**","",
        "## Exact benchmark factorization","",
        "Where `|omega|>0`,","",
        "`sigma = |omega|^2 gamma`, with `gamma = xi^T S xi = 4 z exp(-|x|^2)`.","",
        "The vorticity direction is azimuthal (up to sign) around the z axis.","",
        "## Typed undefined set","",
        "The direction channel is undefined on the z axis and on the shell `|x|^2=5/2`, because there `|omega|=0`.",
        "Although the simplified gamma formula has a smooth algebraic extension, that extension is not treated as an actually defined vorticity-direction value.","",
        "## Eigenframe decomposition","",
        "At defined points, `gamma = sum_i lambda_i (xi·e_i)^2` and the alignment weights sum to one.",
        "This separates vorticity magnitude from strain eigenvalues and vorticity/strain alignment.","",
        "## Claim boundary","",d["proof_boundary"],
    ]
    (out/"vorticity_alignment_baseline.md").write_text("\n".join(lines),encoding="utf-8")
    print(f"Vorticity alignment bridge: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=="__main__":
    main()
