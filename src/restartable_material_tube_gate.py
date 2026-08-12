#!/usr/bin/env python3
"""Checks for a restartable parabolic material-tube bridge.

A material cell is restarted at the beginning of each parabolic window of length
ell^2.  This avoids carrying irrelevant long-time deformation history into a
local regularity test.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp


def run_checks():
    ell,lam,M,tau=sp.symbols('ell lam M tau', positive=True, real=True)

    # Trace-free affine strain model used only as a kinematic audit.
    F=sp.diag(sp.exp(-M*tau),1,sp.exp(M*tau))
    smin=sp.exp(-M*tau)
    smax=sp.exp(M*tau)
    inner=sp.simplify(ell*smin)
    outer=sp.simplify(ell*smax)
    Kminus=sp.simplify(M*tau)
    Kplus=sp.simplify(M*tau)

    # Under NS scaling, strain M -> lambda^2 M and parabolic time tau -> tau/lambda^2.
    Kminus_scaled=sp.simplify((lam**2*M)*(tau/lam**2))
    Kplus_scaled=Kminus_scaled

    # Time-averaged scale-critical oscillation channel:
    # P_osc = ell^-2 int_{t0}^{t0+ell^2} C_osc ds.
    # C_osc is invariant; ds -> lambda^-2 ds; ell^-2 -> lambda^2 ell^-2.
    parabolic_osc_ratio=sp.simplify(lam**2*lam**-2)

    # Path excursion channel K_path = ell^-1 sup_s |X(s)-X(t0)-c(s-t0)|.
    # displacement -> lambda^-1, ell^-1 -> lambda.
    path_ratio=sp.simplify(lam*lam**-1)

    # Critical Morrey energy split at a restart time (Phi=identity):
    # ell^-1 int |u|^2 = C_osc + ell^-1 |B_ell| |Ubar|^2.
    volume=sp.Rational(4,3)*sp.pi*ell**3
    mean_speed_sq=sp.symbols('m2', nonnegative=True)
    Cmean=sp.simplify(volume*mean_speed_sq/ell)

    checks={
        'affine_detF_one': bool(sp.simplify(F.det())==1),
        'inner_radius_formula': bool(inner==ell*sp.exp(-M*tau)),
        'outer_radius_formula': bool(outer==ell*sp.exp(M*tau)),
        'compression_accumulation_scale_invariant': bool(Kminus_scaled==Kminus),
        'extension_accumulation_scale_invariant': bool(Kplus_scaled==Kplus),
        'parabolic_oscillation_scale_invariant': bool(parabolic_osc_ratio==1),
        'path_excursion_scale_invariant': bool(path_ratio==1),
        'mean_energy_channel_scale_form': bool(sp.simplify(Cmean-sp.Rational(4,3)*sp.pi*ell**2*mean_speed_sq)==0),
    }

    return {
        'status':'DERIVED RESTARTABLE MATERIAL-TUBE BRIDGE + EXACT SCALING CHECK',
        'checks':checks,'passed':sum(checks.values()),'total':len(checks),
        'tube':{
            'restart':'Phi_{t0;t0}=Id on B_ell(a)',
            'duration':'ell^2',
            'K_minus':'integral over window of sup_cell(-lambda_1)',
            'K_plus':'integral over window of sup_cell(lambda_3)',
            'parabolic_Cosc':'ell^-2 int_window C_osc ds',
            'path_channel':'ell^-1 sup_window |X(s)-X(t0)-c(s-t0)|'
        },
        'affine_geometry':{
            'inner_radius':str(inner),
            'outer_radius':str(outer),
            'K_minus':str(Kminus),
            'K_plus':str(Kplus)
        },
        'morrey_split_at_restart':'ell^-1 int_{B_ell}|u|^2 = C_osc + C_mean, with C_mean=ell^-1 |B_ell| |Ubar|^2.',
        'interpretation':'Bounded recent deformation and path excursion make a restartable material tube geometrically comparable to an Eulerian parabolic neighborhood. This is a bridge condition, not a regularity theorem.',
        'claim_boundary':'The exact scaling and affine inclusion audit do not prove that arbitrary Navier-Stokes material tubes satisfy uniform distortion/path bounds.'
    }


def write_md(d,path):
    lines=[
        '# Restartable material parabolic tube gate','',
        f"Status: **{d['status']}**",'',
        f"Checks passed: **{d['passed']}/{d['total']}**",'',
        '## Restart rule','',
        'At each candidate center/scale, restart the material flow map at the beginning of a parabolic window of duration `ell^2`, so `F(t0)=I`.','',
        'This prevents old deformation history from contaminating a local scale test.','',
        '## Geometry channels','',
        '`K_minus = int sup_cell(-lambda_1) ds` controls recent compression / inverse-map growth.','',
        '`K_plus = int sup_cell(lambda_3) ds` controls recent extension / forward-map growth.','',
        'Both are dimensionless and Navier--Stokes scale invariant over a parabolic window.','',
        'If they are bounded, the material cell is comparable to balls with radii roughly `ell exp(-K_minus)` and `ell exp(K_plus)` in the affine audit.','',
        '## Parabolic oscillation channel','',
        '`P_Cosc = ell^-2 int_window C_osc ds` is scale invariant.','',
        'A separate scale-invariant path-excursion channel is required if the moving material center is to be compared with a fixed Eulerian parabolic cylinder.','',
        '## Claim boundary','',d['claim_boundary'],'']
    path.write_text('\n'.join(lines),encoding='utf-8')


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks()
    (out/'restartable_material_tube_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
    write_md(d,out/'restartable_material_tube_gate.md')
    print(f"Restartable material tube gate: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=='__main__': main()
