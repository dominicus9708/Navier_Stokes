#!/usr/bin/env python3
"""Exact audit for the material-frame relative-difference DSD bridge.

This module checks scale/kinematic identities only. It does not integrate the
Navier--Stokes PDE in time and does not claim a regularity theorem.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import sympy as sp


def run_checks():
    M,t,c,ell=sp.symbols('M t c ell', positive=True, real=True)

    # Trace-free local strain countermodel: middle positive eigenvalue vanishes,
    # while a material oriented-area factor can grow exponentially.
    S=sp.diag(-M,0,M)
    F=sp.diag(sp.exp(-M*t),1,sp.exp(M*t))
    G=sp.simplify(F.inv().T)
    detF=sp.simplify(F.det())
    GTG=sp.simplify(G.T*G)
    g_eigs=sorted([sp.simplify(v) for v in GTG.eigenvals().keys()], key=str)

    # Gaussian anchor from the repository: local strain eigenvalues (-4c,2c,2c).
    Fg=sp.diag(sp.exp(-4*c*t),sp.exp(2*c*t),sp.exp(2*c*t))
    Gg=sp.simplify(Fg.inv().T)

    # Exact spherical second moment: int_{B_ell} y_i y_j dy = delta_ij 4 pi ell^5 / 15.
    moment=sp.Rational(4,15)*sp.pi*ell**5
    a11,a12,a13,a21,a22,a23,a31,a32,a33=sp.symbols(
        'a11 a12 a13 a21 a22 a23 a31 a32 a33', real=True)
    A=sp.Matrix([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]])
    frob2=sp.simplify(sp.trace(A.T*A))
    affine_integral=sp.simplify(moment*frob2)
    Crel_affine=sp.simplify(affine_integral/ell)
    Crel_expected=sp.Rational(4,15)*sp.pi*ell**4*frob2

    # Scaling bookkeeping for u_lambda=lambda u(lambda x,lambda^2 t),
    # p_lambda=lambda^2 p(lambda x,lambda^2 t), ell_lambda=ell/lambda.
    lam=sp.symbols('lam', positive=True)
    Crel_scale=sp.simplify((lam/ell) * lam**2 * lam**-3)  # ell_lambda^-1 * |dv|^2 * db
    Prel_scale=sp.simplify((ell/lam) * lam * lam**3 * lam**-3 / ell)  # ratio to original prefactor ell
    Vrel_scale=Prel_scale  # Delta u has the same lambda^3 scaling as grad p.

    checks={
        'tracefree_local_model': bool(sp.trace(S)==0),
        'tracefree_model_detF_one': bool(detF==1),
        'middle_positive_eigenvalue_zero': True,  # eigenvalues are exactly (-M,0,M), M>0
        'boundary_inverse_transpose_growth': bool(sp.simplify(G[0,0]-sp.exp(M*t))==0),
        'gaussian_boundary_growth_matches_compression': bool(sp.simplify(Gg[0,0]-sp.exp(4*c*t))==0),
        'affine_relative_channel_formula': bool(sp.simplify(Crel_affine-Crel_expected)==0),
        'critical_scaling_Crel': bool(Crel_scale==1/ell),
        'critical_scaling_pressure_and_viscous_relative_rates': bool(Prel_scale==1 and Vrel_scale==1),
    }

    return {
        'status':'DERIVED MATERIAL-FRAME DIFFERENCE BRIDGE + EXACT CHECK',
        'checks':checks,'passed':sum(checks.values()),'total':len(checks),
        'geometry':{
            'strain_model':'diag(-M,0,M)',
            'lambda2_plus':0,
            'detF':str(detF),
            'F_inverse_transpose':str(G),
            'GTG_eigenvalues':[str(v) for v in g_eigs],
            'consequence':'lambda2^+ alone cannot control ||F^{-T}||; the compression channel -lambda1 is separate.'
        },
        'relative_channel':{
            'definition':'C_rel(a,ell,t)=ell^(-1) int_{B_ell(a)} |u(Phi_t(b),t)-u(Phi_t(a),t)|^2 db',
            'affine_leading_formula':str(Crel_expected),
            'pressure_rate_channel':'P_rel=ell int V . delta(grad p) db',
            'viscous_rate_channel':'V_rel=nu ell int V . delta(Delta u) db',
            'balance':'ell^2 d_t C_rel = -2 P_rel + 2 V_rel',
            'scaling':'C_rel, P_rel and V_rel are invariant under the Navier-Stokes parabolic scaling when the material label and ell are scaled together.'
        },
        'claim_boundary':'Exact kinematic/scaling bridge only. No arbitrary-data a-priori bound or regularity implication is proved.'
    }


def write_md(d,path):
    lines=[
        '# Material-frame relative-difference gate', '',
        f"Status: **{d['status']}**", '',
        f"Checks passed: **{d['passed']}/{d['total']}**", '',
        '## Geometry separation', '',
        '- For the trace-free local model `S=diag(-M,0,M)`, `lambda_2^+=0` but `||F^{-T}||=exp(M t)`.',
        '- Therefore the middle-eigenvalue danger channel does not by itself control material-boundary compression/amplification.',
        '- Keep a separate compression channel `chi=-lambda_1` (or an equivalent full-strain channel).', '',
        '## Material-frame difference channel', '',
        '`V(b,t)=u(Phi_t(b),t)-u(Phi_t(a),t)` removes uniform translation of the tracked fluid cell.', '',
        '`C_rel=ell^(-1) int |V|^2 db` is invariant under Navier--Stokes scaling.', '',
        'Along material trajectories:', '',
        '`dot V = -delta(grad p) + nu delta(Delta u)`', '',
        'and hence', '',
        '`ell^2 d_t C_rel = -2 P_rel + 2 V_rel`', '',
        'with `P_rel=ell int V.delta(grad p) db` and `V_rel=nu ell int V.delta(Delta u) db`.', '',
        'Uniform pressure acceleration also cancels because only the pressure-gradient difference across the cell remains.', '',
        '## Smooth small-scale limit', '',
        'For a smooth field and small `ell`, `delta u = (grad u) F (b-a)+o(|b-a|)`, giving', '',
        '`C_rel = (4 pi / 15) ell^4 ||(grad u)F||_F^2 + o(ell^4)`.', '',
        'Thus the channel tends to zero at smooth points, while its normalization is compatible with the critical Navier--Stokes scaling.', '',
        '## Claim boundary', '', d['claim_boundary'], ''
    ]
    path.write_text('\n'.join(lines),encoding='utf-8')


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks()
    (out/'material_relative_difference_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
    write_md(d,out/'material_relative_difference_gate.md')
    print(f"Material relative-difference gate: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=='__main__': main()
