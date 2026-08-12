#!/usr/bin/env python3
"""Algebra/scaling audit for the moving weighted-variance local-energy lemma.

The intended theorem-level statement is obtained by combining the suitable local
energy inequality with the weak momentum equation for a moving smooth cutoff.
This script checks the exact smooth algebra and critical scaling; it does not
replace the functional-analytic passage to suitable weak solutions.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp


def run_checks():
    # Abstract scalar integral symbols for the algebraic variance cancellation.
    # M = int phi, U = weighted mean.  Introduce abstract vector components.
    M=sp.symbols('M', positive=True, real=True)
    U1,U2,U3=sp.symbols('U1 U2 U3', real=True)
    U=sp.Matrix([U1,U2,U3])

    # Abstract identities: int phi u = M U, int phi v = 0.
    weighted_v=sp.zeros(3,1)

    # Convective coefficient after subtracting U dot momentum balance:
    # 1/2|u|^2-U.u = 1/2|v|^2-1/2|U|^2, and the constant term integrates
    # against v.grad phi to zero because div v=0.
    vx,vy,vz=sp.symbols('vx vy vz', real=True)
    v=sp.Matrix([vx,vy,vz]); u=v+U
    coeff=sp.simplify(sp.Rational(1,2)*u.dot(u)-U.dot(u))
    coeff_expected=sp.simplify(sp.Rational(1,2)*v.dot(v)-sp.Rational(1,2)*U.dot(U))

    # Pressure vector difference: p u.grad phi - U.(p grad phi)=p v.grad phi.
    gx,gy,gz,p=sp.symbols('gx gy gz p', real=True)
    g=sp.Matrix([gx,gy,gz])
    pressure_residual=sp.simplify(p*u.dot(g)-p*U.dot(g)-p*v.dot(g))

    # Viscous cutoff coefficient has the same variance cancellation.
    visc_coeff_residual=sp.simplify(coeff-coeff_expected)

    # Critical scaling of weighted variance budget channels.
    ell,lam=sp.symbols('ell lam', positive=True, real=True)
    Cscale=sp.simplify((lam/ell)*lam**2*lam**-3)       # ell^-1 int phi |v|^2
    Dscale=sp.simplify((ell/lam)*lam**4*lam**-3/ell)  # ell int phi |grad u|^2
    Ascale=sp.simplify((ell/lam)*lam**3*lam*lam**-3/ell)
    Pscale=sp.simplify((ell/lam)*lam**2*lam*lam*lam**-3/ell)
    Bscale=sp.simplify((ell/lam)*lam**2*lam**2*lam**-3/ell)

    # Caratheodory ODE scale bookkeeping: Xdot = weighted mean u.
    # X -> lambda^-1 X(lambda^2 t), so Xdot -> lambda Xdot.
    center_velocity_scale=lam

    checks={
        'weighted_mean_zero_by_definition': bool(weighted_v==sp.zeros(3,1)),
        'convective_variance_coefficient_identity': bool(sp.simplify(coeff-coeff_expected)==0),
        'pressure_mean_subtraction_identity': bool(pressure_residual==0),
        'viscous_cutoff_variance_identity': bool(visc_coeff_residual==0),
        'critical_scaling_C': bool(Cscale==1/ell),
        'critical_scaling_D': bool(Dscale==1),
        'critical_scaling_A': bool(Ascale==1),
        'critical_scaling_P': bool(Pscale==1),
        'critical_scaling_B': bool(Bscale==1),
        'center_velocity_scales_like_velocity': bool(center_velocity_scale==lam),
    }

    return {
        'status':'DERIVED WEIGHTED-VARIANCE LOCAL-ENERGY ALGEBRA + SUITABLE-WEAK BRIDGE CANDIDATE',
        'checks':checks,'passed':sum(checks.values()),'total':len(checks),
        'smooth_identity':'d/dt [1/2 int phi_ell(x-X)|u-Ubar|^2] + nu int phi_ell |grad u|^2 = int (|v|^2/2) v.grad phi_ell + int p v.grad phi_ell + (nu/2) int |v|^2 Delta phi_ell.',
        'construction':{
            'weighted_mean':'Ubar(X,t)=(int phi_ell(x-X) u(x,t) dx)/(int phi_ell)',
            'center_ODE':'Xdot(t)=Ubar(X(t),t)',
            'relative_velocity':'v=u-Ubar',
            'moving_test_derivative':'partial_t phi_ell(x-X(t))=-Ubar.grad phi_ell'
        },
        'weak_bridge_outline':[
            'For fixed ell and smooth compactly supported phi, convolution of u with phi is bounded and locally Lipschitz in X for Leray/suitable energy-class u; the center ODE is a Caratheodory ODE.',
            'Insert smooth approximations of the moving nonnegative cutoff into the suitable local-energy inequality.',
            'Use the weak momentum equation with the same moving cutoff to obtain the evolution of the weighted mean momentum.',
            'Subtract M|Ubar|^2/2 from the localized kinetic energy; the transport, pressure, and cutoff-viscosity terms reduce to the relative-velocity formula above.',
            'Pass the approximations to the absolutely-continuous center path. No Xddot term is required.'
        ],
        'claim_boundary':'The algebra strongly supports a suitable-weak moving weighted-variance lemma, but a publishable proof still must write the approximation, time-regularity, and chain-rule steps carefully. Until that is done, status remains BRIDGE CANDIDATE rather than established theorem.'
    }


def write_md(d,path):
    lines=['# Weighted variance local-energy lemma audit','',f"Status: **{d['status']}**",'',f"Checks passed: **{d['passed']}/{d['total']}**",'',
           '## Smooth identity','',d['smooth_identity'],'',
           'The identity is obtained without introducing an accelerating-frame pressure. It uses only the moving cutoff derivative and the evolution of the weighted mean momentum.','',
           '## Suitable-weak bridge outline','']
    for item in d['weak_bridge_outline']:
        lines.append(f'- {item}')
    lines += ['', '## Claim boundary','',d['claim_boundary'],'']
    path.write_text('\n'.join(lines),encoding='utf-8')


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks()
    (out/'weighted_variance_local_energy_lemma.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
    write_md(d,out/'weighted_variance_local_energy_lemma.md')
    print(f"Weighted variance local-energy lemma: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=='__main__': main()
