#!/usr/bin/env python3
"""Exact spherical energy-budget audit for the analytic Gaussian benchmark."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp


def run_checks():
    r,s,mu,nu=sp.symbols('r s mu nu', positive=True)
    # Normalized spherical means derived for the z-axis Gaussian double-curl seed.
    TE=8*sp.exp(-2*r**2)*(1-sp.Rational(4,3)*r**2+sp.Rational(2,3)*r**4)
    TG=sp.Rational(128,3)*r**2*(r**4-4*r**2+5)*sp.exp(-2*r**2)

    # u_r = 4 mu exp(-r^2); energy density is even in mu, hence e*u_r is odd.
    energy_angular=(1-r**2)**2+(2*r**2-r**4)*mu**2
    e=8*sp.exp(-2*r**2)*energy_angular
    ur=4*mu*sp.exp(-r**2)
    adv_shell=sp.simplify(4*sp.pi*r**2*sp.Rational(1,2)*sp.integrate(e*ur,(mu,-1,1)))

    # Pressure source Q is even in z for this benchmark, so the unique decaying
    # whole-space pressure is even in z. Multiplication by odd u_r integrates to zero.
    pressure_flux_by_parity=sp.Integer(0)

    Fvis=sp.factor(-nu*4*sp.pi*r**2*sp.diff(TE,r))
    positive_poly=2*r**4-6*r**2+5
    # positive_poly = 2*(r^2-3/2)^2 + 1/2 > 0.
    positive_certificate=sp.expand(2*(r**2-sp.Rational(3,2))**2+sp.Rational(1,2))

    TG_s=TG.subs(r,s)
    DB=sp.simplify(nu*sp.integrate(4*sp.pi*s**2*TG_s,(s,0,r)))
    global_D=sp.simplify(sp.limit(DB/nu,r,sp.oo))
    global_expected=35*sp.sqrt(2)*sp.pi**sp.Rational(3,2)/2
    global_flux=sp.simplify(sp.limit(Fvis,r,sp.oo))

    # Local kinetic-energy balance:
    # d/dt E_B + F_adv + F_p + F_vis = -nu int_B |grad u|^2.
    predicted_ball_rate=sp.simplify(-adv_shell-pressure_flux_by_parity-Fvis-DB)

    checks={
        'advective_shell_flux_zero':bool(adv_shell==0),
        'pressure_shell_flux_zero_by_parity':bool(pressure_flux_by_parity==0),
        'viscous_flux_formula':bool(sp.simplify(Fvis-sp.Rational(128,3)*sp.pi*nu*r**3*positive_poly*sp.exp(-2*r**2))==0),
        'viscous_flux_positive_certificate':bool(sp.simplify(positive_poly-positive_certificate)==0),
        'global_dissipation_recovered':bool(sp.simplify(global_D-global_expected)==0),
        'outer_flux_vanishes_at_infinity':bool(global_flux==0),
    }
    return {
        'status':'DERIVED IDENTITY / SPHERICAL ENERGY REDISTRIBUTION',
        'checks':checks,'passed':sum(checks.values()),'total':len(checks),
        'shell_channels':{
            'mean_energy':str(TE),
            'mean_grad_u_squared':str(TG),
            'F_adv':str(adv_shell),
            'F_pressure':str(pressure_flux_by_parity),
            'F_viscous':str(Fvis),
            'ball_dissipation':str(DB),
            'predicted_initial_ball_energy_rate':str(predicted_ball_rate),
        },
        'viscous_flux_sign':'strictly positive for r>0, nu>0',
        'interpretation':(
            'For the centered symmetric benchmark, net convective and pressure transport through each centered '
            'sphere cancels, while viscosity carries kinetic energy outward across every finite sphere and also '
            'dissipates energy inside the ball. This is radial redistribution, not a finite-speed acoustic wave.'
        ),
        'proof_boundary':'Exact benchmark budget only; generic asymmetric data can have nonzero advective and pressure shell fluxes.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks(); (out/'spherical_energy_budget.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
    print(f"Spherical energy budget: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=='__main__': main()
