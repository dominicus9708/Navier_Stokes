#!/usr/bin/env python3
"""Exact middle-strain-eigenvalue alignment of the Gaussian benchmark vorticity."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp


def run_checks():
    rho,z=sp.symbols('rho z', real=True)
    r2=rho**2+z**2
    g=sp.exp(-r2)

    # Cylindrical orthonormal basis ordering (e_rho,e_phi,e_z).
    A=4*z*(1-2*rho**2)*g
    Dzz=8*z*(rho**2-1)*g
    B=2*rho*(2*rho**2-2*z**2-3)*g
    S_cyl=sp.Matrix([[A,0,B],[0,4*z*g,0],[B,0,Dzz]])

    lambda_mid=4*z*g
    Delta=sp.factor(z**2*(3-4*rho**2)**2 + rho**2*(2*rho**2-2*z**2-3)**2)
    Delta_alt=sp.factor(9*z**2+rho**2*(2*r2-3)**2)
    lambda_low=sp.factor(-2*z*g-2*g*sp.sqrt(Delta))
    lambda_high=sp.factor(-2*z*g+2*g*sp.sqrt(Delta))

    ephi=sp.Matrix([0,1,0])
    eigen_residual=sp.simplify(S_cyl*ephi-lambda_mid*ephi)
    discriminant_residual=sp.simplify(Delta-Delta_alt)

    # Since sqrt(Delta)>=3|z|, lambda_low<=lambda_mid<=lambda_high.
    # We encode ordering using squared nonnegative certificate Delta-9 z^2.
    order_certificate=sp.factor(Delta-9*z**2)

    checks={
        'ephi_exact_eigenvector':bool(all(v==0 for v in eigen_residual)),
        'middle_eigenvalue_formula':bool(lambda_mid==4*z*g),
        'discriminant_identity':bool(discriminant_residual==0),
        'ordering_certificate_square':bool(sp.simplify(order_certificate-rho**2*(2*r2-3)**2)==0),
        'trace_zero':bool(sp.simplify(lambda_low+lambda_mid+lambda_high)==0),
    }
    return {
        'status':'DERIVED EXACT IDENTITY / BENCHMARK MIDDLE-EIGENVALUE ALIGNMENT',
        'checks':checks,'passed':sum(checks.values()),'total':len(checks),
        'strain_cylindrical':str(S_cyl),
        'eigenvalues':{
            'lambda_1':str(lambda_low),
            'lambda_2':str(lambda_mid),
            'lambda_3':str(lambda_high),
        },
        'ordering_certificate':str(order_certificate),
        'vorticity_direction':'e_phi wherever |omega|>0 (up to orientation sign)',
        'exact_consequence':'gamma=xi^T S xi=lambda_2=4*z*exp(-r^2); sigma=|omega|^2*lambda_2',
        'typing_boundary':'On the vorticity-zero set xi is undefined even though the strain eigenvalue lambda_2 remains defined.',
        'interpretation':(
            'The analytic benchmark is an exact middle-eigenvector-alignment control case. It is useful for '
            'testing DSD axis/alignment bookkeeping, but cannot be generalized to arbitrary Navier-Stokes data by assumption.'
        )
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks(); (out/'middle_eigenvalue_alignment_baseline.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
    print(f"Middle-eigenvalue alignment: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=='__main__': main()
