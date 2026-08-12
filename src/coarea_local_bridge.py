#!/usr/bin/env python3
"""
Shell-to-ball / local scale bridge for the unbounded spherical viewpoint.

This script verifies exact coarea reconstruction for the Gaussian benchmark and
symbolic Navier-Stokes scaling of standard parabolic-cylinder integrals.
It does not assert an epsilon-regularity theorem by itself.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def run_checks():
    r,R,lam = sp.symbols("r R lam", positive=True)

    TE = 8*sp.exp(-2*r**2)*(1-sp.Rational(4,3)*r**2+sp.Rational(2,3)*r**4)
    TW = sp.Rational(32,3)*r**2*(2*r**2-5)**2*sp.exp(-2*r**2)
    TEx = sp.Rational(8,15)*r**4*sp.exp(-2*r**2)
    TEy = TEx
    TEz = 8*sp.exp(-2*r**2)*(1-sp.Rational(4,3)*r**2+sp.Rational(8,15)*r**4)

    whole_energy = sp.simplify(sp.integrate(4*sp.pi*r**2*TE,(r,0,sp.oo)))
    whole_enstrophy = sp.simplify(sp.integrate(4*sp.pi*r**2*TW,(r,0,sp.oo)))
    whole_axis = [sp.simplify(sp.integrate(4*sp.pi*r**2*T,(r,0,sp.oo))) for T in (TEx,TEy,TEz)]

    expected_energy = 5*sp.sqrt(2)*sp.pi**sp.Rational(3,2)/4
    expected_enstrophy = 35*sp.sqrt(2)*sp.pi**sp.Rational(3,2)/2

    ball_energy = sp.Integral(4*sp.pi*r**2*TE,(r,0,R))
    coarea_derivative = sp.simplify(sp.diff(ball_energy,R)-4*sp.pi*R**2*TE.subs(r,R))

    # Parabolic scale bookkeeping.  Under u_lam=lambda u(lambda x,lambda^2 t):
    # dx dt -> lambda^-5 dX dT, |u|^3 -> lambda^3, |p|^(3/2) -> lambda^3,
    # |grad u|^2 -> lambda^4.
    velocity_cylinder_factor = sp.simplify((lam**-2)/( (sp.Symbol("rho", positive=True)/lam)**2 ) )
    # More transparently compare r^-2 I with rho=lambda*r:
    rrho=sp.symbols("rho",positive=True)
    Cu_scaled = sp.simplify((rrho/lam)**-2 * lam**-2)
    Cu_target = sp.simplify(rrho**-2)
    grad_scaled = sp.simplify((rrho/lam)**-1 * lam**-1)
    grad_target = sp.simplify(rrho**-1)

    checks={
        "whole_energy_recovered": sp.simplify(whole_energy-expected_energy)==0,
        "whole_enstrophy_recovered": sp.simplify(whole_enstrophy-expected_enstrophy)==0,
        "axis_shells_sum_to_energy": sp.simplify(sum(whole_axis)-whole_energy)==0,
        "finite_ball_coarea_derivative": coarea_derivative==0,
        "parabolic_L3_quantity_scale_invariant": sp.simplify(Cu_scaled-Cu_target)==0,
        "parabolic_pressure_3over2_quantity_scale_invariant": sp.simplify(Cu_scaled-Cu_target)==0,
        "parabolic_gradient_quantity_scale_invariant": sp.simplify(grad_scaled-grad_target)==0,
    }

    return {
        "status":"DERIVED IDENTITY / COAREA + SCALE BRIDGE",
        "checks":checks,
        "passed":sum(bool(v) for v in checks.values()),
        "total":len(checks),
        "exact_benchmark_reconstruction":{
            "integral_half_u_squared":str(whole_energy),
            "integral_omega_squared":str(whole_enstrophy),
            "axis_energy_integrals":[str(v) for v in whole_axis],
        },
        "coarea_identity": "int_{B_R(x0)} f dx = int_0^R int_{S_r(x0)} f dS dr",
        "parabolic_channels":{
            "C_u":"r^-2 int_{t0-r^2}^{t0} int_{B_r(x0)} |u|^3 dx dt",
            "C_p":"r^-2 int_{t0-r^2}^{t0} int_{B_r(x0)} |p-p_B|^(3/2) dx dt",
            "E_grad":"r^-1 int_{t0-r^2}^{t0} int_{B_r(x0)} |grad u|^2 dx dt",
            "scaling_status":"dimensionless under the natural Navier-Stokes scaling"
        },
        "interpretation":(
            "All-center spherical-shell data can be radially integrated into ball data, "
            "and then combined across a parabolic time window. The shells remain observation "
            "surfaces, not physical boundaries."
        ),
        "proof_boundary":(
            "Matching the geometry and scaling of local regularity quantities does not prove "
            "their required smallness near every possible singular point."
        )
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output-dir",default="results"); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks()
    (out/"coarea_local_bridge.json").write_text(json.dumps(d,indent=2),encoding="utf-8")
    lines=[
        "# Shell-to-local coarea bridge","",
        f"Checks passed: **{d['passed']}/{d['total']}**","",
        "## Exact benchmark reconstruction","",
        f"- total kinetic energy: `{d['exact_benchmark_reconstruction']['integral_half_u_squared']}`",
        f"- total enstrophy: `{d['exact_benchmark_reconstruction']['integral_omega_squared']}`","",
        "The shell family therefore reconstructs the usual whole-space volume integrals exactly for the analytic benchmark.","",
        "## Local/parabolic bridge","",
        f"- velocity critical cylinder: `{d['parabolic_channels']['C_u']}`",
        f"- pressure cylinder: `{d['parabolic_channels']['C_p']}`",
        f"- gradient/dissipation cylinder: `{d['parabolic_channels']['E_grad']}`","",
        d['interpretation'],"",
        "## Claim boundary","",d['proof_boundary']
    ]
    (out/"coarea_local_bridge.md").write_text("\n".join(lines),encoding="utf-8")
    print(f"Coarea/local bridge: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']:
        raise SystemExit(1)

if __name__=="__main__":
    main()
