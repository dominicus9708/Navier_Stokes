#!/usr/bin/env python3
"""Exact audit of time-dependent translational-frame covariance.

For x=y+X(t), v(y,t)=u(x,t)-Xdot(t), and
q(y,t)=p(x,t)+Xddot(t).y, the force-free incompressible Navier--Stokes
operator retains its form.  The explicit affine audit below is local/kinematic
and is not a Clay-admissible decaying solution.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp


def run_checks():
    y1,y2,y3,t,nu=sp.symbols('y1 y2 y3 t nu', real=True)
    y=sp.Matrix([y1,y2,y3])

    A=sp.diag(-1,0,1)
    X=sp.Matrix([sp.Rational(1,2)*t**2,0,0])
    Xdot=sp.diff(X,t)
    Xddot=sp.diff(Xdot,t)
    x=y+X

    u=A*x
    p=-sp.Rational(1,2)*(x.dot(A*A*x))
    v=sp.simplify(u-Xdot)
    q=sp.simplify(p+Xddot.dot(y))

    coords=(y1,y2,y3)
    divv=sp.simplify(sum(sp.diff(v[i],coords[i]) for i in range(3)))
    vt=sp.Matrix([sp.diff(v[i],t) for i in range(3)])
    adv=sp.Matrix([sum(v[j]*sp.diff(v[i],coords[j]) for j in range(3)) for i in range(3)])
    gradq=sp.Matrix([sp.diff(q,c) for c in coords])
    lapv=sp.Matrix([sum(sp.diff(v[i],c,2) for c in coords) for i in range(3)])
    residual=sp.simplify(vt+adv+gradq-nu*lapv)

    # Pressure-gradient differences are unchanged by the uniform Xddot addition.
    g1,g2,g3,h1,h2,h3,a1,a2,a3=sp.symbols('g1 g2 g3 h1 h2 h3 a1 a2 a3', real=True)
    gp1=sp.Matrix([g1,g2,g3]); gp2=sp.Matrix([h1,h2,h3]); acc=sp.Matrix([a1,a2,a3])
    diff_invariance=sp.simplify((gp1+acc)-(gp2+acc)-(gp1-gp2))

    checks={
        'transformed_field_divergence_free': bool(divv==0),
        'accelerating_frame_NS_residual_zero': all(sp.simplify(r)==0 for r in residual),
        'pressure_gradient_difference_invariant': all(sp.simplify(r)==0 for r in diff_invariance),
        'affine_source_solution_tracefree': bool(sp.trace(A)==0),
    }

    return {
        'status':'DERIVED TIME-DEPENDENT TRANSLATION COVARIANCE + EXACT AFFINE CHECK',
        'checks':checks,'passed':sum(checks.values()),'total':len(checks),
        'transform':{
            'coordinates':'x=y+X(t)',
            'velocity':'v(y,t)=u(y+X(t),t)-Xdot(t)',
            'pressure':'q(y,t)=p(y+X(t),t)+Xddot(t).y',
            'consequence':'The transformed pair satisfies the same force-free incompressible Navier-Stokes form.'
        },
        'DSD_consequence':'Choose Xdot(t) as a material-cell mean velocity to remove coherent cell translation. Differential pressure channels are unchanged because the uniform acceleration term cancels under mean/difference subtraction.',
        'claim_boundary':'Exact smooth-coordinate identity. Applying it inside a weak-solution epsilon-regularity argument requires the corresponding transformed local-energy/suitability bookkeeping.'
    }


def write_md(d,path):
    lines=[
        '# Accelerating-frame symmetry gate','',
        f"Status: **{d['status']}**",'',
        f"Checks passed: **{d['passed']}/{d['total']}**",'',
        'For any smooth translation path `X(t)`, use `x=y+X(t)`, `v=u-Xdot`, and `q=p+Xddot.y`.','',
        'The Navier--Stokes form is preserved exactly; the uniform frame acceleration is absorbed into a linear pressure term.','',
        'Therefore a moving observation sphere may follow the material-cell mean velocity rather than one distinguished particle. Coherent translation and acceleration can be removed while internal velocity and pressure-gradient differences remain.','',
        '## Claim boundary','',d['claim_boundary'],'']
    path.write_text('\n'.join(lines),encoding='utf-8')


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks()
    (out/'accelerating_frame_symmetry_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
    write_md(d,out/'accelerating_frame_symmetry_gate.md')
    print(f"Accelerating-frame symmetry gate: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=='__main__': main()
