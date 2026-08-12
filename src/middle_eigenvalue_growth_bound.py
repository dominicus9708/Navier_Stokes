#!/usr/bin/env python3
"""Middle strain eigenvalue growth-channel bound and Gaussian benchmark audit."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp


def run_checks():
    b,c=sp.symbols('b c', positive=True)
    # lambda2=b>0, lambda3=c>=b, lambda1=-(b+c)
    det_growth=b*c*(b+c) # -det S
    norm2=(b+c)**2+b**2+c**2
    rhs=sp.Rational(1,2)*b*norm2
    gap=sp.factor(rhs-det_growth)

    rho,z=sp.symbols('rho z', nonnegative=True)
    r2=rho**2+z**2; g=sp.exp(-r2)
    lam2=4*z*g
    Snorm2=8*(4*rho**6+8*rho**4*z**2-12*rho**4+4*rho**2*z**4-12*rho**2*z**2+9*rho**2+12*z**2)*sp.exp(-2*r2)
    minusdet=16*z*sp.exp(-3*r2)*(8*z**2+rho**2*(2*r2-3)**2)

    I_growth=sp.simplify(2*sp.pi*sp.integrate(sp.integrate(minusdet*rho,(rho,0,sp.oo)),(z,0,sp.oo)))
    I_bound=sp.simplify(2*sp.pi*sp.integrate(sp.integrate(sp.Rational(1,2)*lam2*Snorm2*rho,(rho,0,sp.oo)),(z,0,sp.oo)))

    checks={
        'general_positive_middle_gap_exact':bool(sp.simplify(gap-b**3)==0),
        'benchmark_positive_growth_integral':bool(sp.simplify(I_growth-sp.Rational(248,81)*sp.pi)==0),
        'benchmark_bound_integral':bool(sp.simplify(I_bound-sp.Rational(344,81)*sp.pi)==0),
        'benchmark_bound_strict':bool(sp.simplify(I_bound-I_growth)>0),
    }
    return {
        'status':'DERIVED INEQUALITY + EXACT BENCHMARK / MIDDLE EIGENVALUE CHANNEL',
        'checks':checks,'passed':sum(checks.values()),'total':len(checks),
        'general_bound':'-det(S) <= (1/2) lambda_2^+ |S|^2 for ordered trace-free eigenvalues',
        'positive_middle_case_gap':str(gap),
        'benchmark_upper_half':{
            'integral_minus_det':str(I_growth),
            'integral_half_lambda2_S2':str(I_bound),
            'ratio_bound_to_growth':str(sp.simplify(I_bound/I_growth)),
        },
        'interpretation':(
            'For a trace-free strain tensor, positive determinant-growth contribution can only arise '
            'where the middle eigenvalue is positive. The benchmark reproduces this sign split exactly.'
        ),
        'proof_boundary':'This elementary bound does not provide the required time-space control of lambda_2^+ for arbitrary solutions.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks(); (out/'middle_eigenvalue_growth_bound.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
    print(f"Middle eigenvalue growth bound: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=='__main__': main()
