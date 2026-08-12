#!/usr/bin/env python3
"""Exact direction-gradient audit for the Gaussian vorticity benchmark."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp


def run_checks():
    x,y,z=sp.symbols('x y z', real=True)
    rho2=x*x+y*y
    r2=rho2+z*z
    xi=sp.Matrix([y,-x,0])/sp.sqrt(rho2)
    grad=sp.Matrix([[sp.diff(xi[i],q) for q in (x,y,z)] for i in range(3)])
    grad2=sp.factor(sp.simplify(sum(v**2 for v in grad)))
    omega2=16*rho2*(2*r2-5)**2*sp.exp(-2*r2)
    weighted=sp.factor(sp.simplify(omega2*grad2))
    expected=16*(2*r2-5)**2*sp.exp(-2*r2)
    total=sp.simplify(sp.integrate(expected,(x,-sp.oo,sp.oo),(y,-sp.oo,sp.oo),(z,-sp.oo,sp.oo)))
    checks={
        'direction_gradient': bool(sp.simplify(grad2-1/rho2)==0),
        'weighted_cancellation': bool(sp.simplify(weighted-expected)==0),
        'whole_space_integral': bool(sp.simplify(total-55*sp.sqrt(2)*sp.pi**sp.Rational(3,2))==0),
    }
    return {
        'status':'DERIVED IDENTITY / MAGNITUDE-WEIGHTED DIRECTION VARIATION',
        'checks':checks,'passed':sum(checks.values()),'total':len(checks),
        'direction_gradient_squared':str(grad2),
        'omega_squared':str(omega2),
        'weighted_direction_gradient':str(weighted),
        'weighted_whole_space_integral':str(total),
        'interpretation':(
            'The derived vorticity direction has a 1/rho^2 axis singularity, while the vorticity magnitude '
            'vanishes strongly enough that |omega|^2|grad xi|^2 is finite and integrable in this benchmark. '
            'Undefined/singular direction data must therefore not be identified automatically with a singular fluid state.'
        ),
        'proof_boundary':'Benchmark identity only; no general Constantin-Fefferman type coherence estimate is proved.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks(); (out/'vorticity_direction_gradient_baseline.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
    print(f"Vorticity direction-gradient audit: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=='__main__': main()
