#!/usr/bin/env python3
"""Algebra audit for pressure-free one-scale exponent bridges.

For 5/2 < p <= 3, interpolate the mean-zero moving-sphere velocity between
L2 and L6 and express the scale-invariant spacetime Lp channel through the
DSD oscillation and local dissipation channels.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp


def exponent_data(p):
    p=sp.Rational(p) if isinstance(p,int) else sp.sympify(p)
    theta=sp.simplify(3/p-sp.Rational(1,2))
    alpha=sp.simplify(theta*p/2)
    beta=sp.simplify((1-theta)*p/2)
    return theta,alpha,beta


def run_checks():
    p,ell,C,E=sp.symbols('p ell C E', positive=True, real=True)
    theta=3/p-sp.Rational(1,2)
    alpha=sp.simplify(theta*p/2)
    beta=sp.simplify((1-theta)*p/2)

    # Fixed-time ell exponent after L2/L6 interpolation.
    ell_power=sp.simplify(alpha-beta)
    expected_ell_power=3-p

    # Total parabolic ell power after multiplying by scale factor ell^(p-5)
    # and normalizing time interval ell^2.
    combined_ell=sp.simplify((p-5)+(3-p))

    th3,a3,b3=exponent_data(sp.Integer(3))
    th11,a11,b11=exponent_data(sp.Rational(11,4))
    thlim=sp.limit(theta,p,sp.Rational(5,2),dir='+')
    alim=sp.limit(alpha,p,sp.Rational(5,2),dir='+')
    blim=sp.limit(beta,p,sp.Rational(5,2),dir='+')

    # Scaling of A_p = ell^(p-5) int_{Q_ell}|v|^p.
    lam=sp.symbols('lam', positive=True)
    Ap_scale=sp.simplify(lam**(5-p)*lam**p*lam**-5)

    checks={
        'theta_formula': bool(sp.simplify(1/p-(theta/2+(1-theta)/6))==0),
        'alpha_formula': bool(sp.simplify(alpha-(6-p)/4)==0),
        'beta_formula': bool(sp.simplify(beta-3*(p-2)/4)==0),
        'fixed_time_radius_power': bool(sp.simplify(ell_power-expected_ell_power)==0),
        'parabolic_radius_power_is_minus2_before_time_average': bool(combined_ell==-2),
        'critical_Ap_scaling': bool(Ap_scale==1),
        'p3_exponents': bool(a3==sp.Rational(3,4) and b3==sp.Rational(3,4)),
        'p11_over4_exponents': bool(a11==sp.Rational(13,16) and b11==sp.Rational(9,16)),
        'p_to_5_over2_limit': bool(alim==sp.Rational(7,8) and blim==sp.Rational(3,8)),
    }

    return {
        'status':'DERIVED PRESSURE-FREE EXPONENT FAMILY BRIDGE + EXACT ALGEBRA CHECK',
        'checks':checks,'passed':sum(checks.values()),'total':len(checks),
        'general':{
            'range':'5/2 < p <= 3',
            'theta_L2':str(sp.simplify(theta)),
            'alpha_Cosc':str(sp.simplify(alpha)),
            'beta_Egrad':str(sp.simplify(beta)),
            'fixed_time':'int_B |v|^p <= C ell^(3-p) C_sph^alpha E_sph^beta',
            'parabolic':'A_p := ell^(p-5) int_window int_B |v|^p <= C (sup C_sph)^alpha (Ebar_sph)^beta'
        },
        'examples':{
            'p=3':{'alpha':str(a3),'beta':str(b3)},
            'p=11/4 (delta=1/4)':{'alpha':str(a11),'beta':str(b11)},
            'p->5/2+':{'alpha':str(alim),'beta':str(blim)}
        },
        'interpretation':'Lowering p toward 5/2 shifts the sufficient smallness bridge toward internal oscillation C_sph and away from local dissipation Ebar. The epsilon threshold depends on the chosen exponent, so one cannot optimize over p without tracking theorem constants.',
        'claim_boundary':'The interpolation family is exact up to standard Sobolev constants. The external pressure-free epsilon-regularity theorem supplies the regularity implication, but this code does not prove arbitrary-data smallness of any channel product.'
    }


def write_md(d,path):
    lines=[
        '# Pressure-free exponent family bridge','',
        f"Status: **{d['status']}**",'',
        f"Checks passed: **{d['passed']}/{d['total']}**",'',
        'For `5/2 < p <= 3`, define `A_p=ell^(p-5) int_{Q_ell}|v|^p`.','',
        '`A_p <= C (sup C_sph)^((6-p)/4) (Ebar_sph)^(3(p-2)/4)`.','',
        'Examples:','',
        '- `p=3`: exponents `(3/4, 3/4)`;',
        '- `p=11/4`: exponents `(13/16, 9/16)`;',
        '- `p -> 5/2+`: exponents approach `(7/8, 3/8)`.','',
        'Thus the pressure-free criteria near exponent `5/2` emphasize small internal oscillation more strongly and require a lower power of local dissipation.','',
        '## Claim boundary','',d['claim_boundary'],'']
    path.write_text('\n'.join(lines),encoding='utf-8')


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks()
    (out/'pressure_free_exponent_bridge.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
    write_md(d,out/'pressure_free_exponent_bridge.md')
    print(f"Pressure-free exponent bridge: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=='__main__': main()
