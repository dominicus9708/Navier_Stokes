#!/usr/bin/env python3
"""Symbolic/scaling checks for local/far pressure-difference localization.

The main mathematical point is kernel cancellation: subtracting pressure (or
pressure-gradient) values at nearby points gains one far-field decay power.
This module checks homogeneity and Navier--Stokes scaling, not a full singular
integral theorem.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp


def run_checks():
    x,y,z,L,d,R,M=sp.symbols('x y z L d R M', positive=True, real=True)
    r=sp.sqrt(x*x+y*y+z*z)

    # Representative Hessian component of the Newtonian potential, constants omitted.
    # Homogeneous degree -3, matching the pressure Riesz kernel K_ij.
    K11=sp.simplify(r**-3-3*x*x*r**-5)
    K11_scaled=sp.simplify(K11.subs({x:L*x,y:L*y,z:L*z}))
    gradK=sp.Matrix([sp.diff(K11,q) for q in (x,y,z)])
    gradK_scaled=sp.simplify(gradK.subs({x:L*x,y:L*y,z:L*z}))
    hessK=sp.Matrix([[sp.diff(K11,q1,q2) for q2 in (x,y,z)] for q1 in (x,y,z)])
    hessK_scaled=sp.simplify(hessK.subs({x:L*x,y:L*y,z:L*z}))

    # Scaling bookkeeping for the far gradient-difference estimate
    # d * int |u|^2 / distance^5 dz.
    # Under NS scaling: d -> L^-1 d, u^2 -> L^2, kernel -> L^5, dz -> L^-3.
    far_grad_scale=sp.simplify(L**-1 * L**2 * L**5 * L**-3)

    # Critical Morrey dyadic estimate: if int_{B_r}|u|^2 <= M r,
    # then d sum_{k>=0} M (2^k R)^(-4) = C d M R^-4.
    k=sp.symbols('k', integer=True, nonnegative=True)
    geometric_sum=sp.simplify(sp.summation(2**(-4*k),(k,0,sp.oo)))
    dyadic_bound=sp.simplify(d*M*R**-4*geometric_sum)

    # If d <= R ~ ell, pointwise far delta grad p is O(M ell^-3).
    # Then Gp_far = ell^3 int_cell |delta grad p_far|^2 is O(M^2).
    ell=sp.symbols('ell', positive=True, real=True)
    pointwise_model=M*ell**-3
    cell_volume_scale=ell**3
    Gp_far_model=sp.simplify(ell**3 * cell_volume_scale * pointwise_model**2)

    checks={
        'pressure_kernel_degree_minus3': bool(sp.simplify(K11_scaled-L**-3*K11)==0),
        'pressure_gradient_kernel_degree_minus4': all(sp.simplify(v)==0 for v in (gradK_scaled-L**-4*gradK)),
        'pressure_hessian_kernel_degree_minus5': all(sp.simplify(v)==0 for v in (hessK_scaled-L**-5*hessK)),
        'far_gradient_difference_NS_scaling': bool(far_grad_scale==L**3),
        'dyadic_decay_sum_finite': bool(geometric_sum==sp.Rational(16,15)),
        'far_critical_pressure_channel_model': bool(sp.simplify(Gp_far_model-M**2)==0),
    }

    return {
        'status':'PRESSURE-DIFFERENCE LOCALIZATION BRIDGE + EXACT HOMOGENEITY CHECK',
        'checks':checks,'passed':sum(checks.values()),'total':len(checks),
        'kernel':{
            'K_degree':'-3',
            'gradK_degree':'-4',
            'hessK_degree':'-5',
            'far_pressure_difference':'|K(x-z)-K(y-z)| <= C |x-y| |z-X|^-4',
            'far_gradient_difference':'|grad K(x-z)-grad K(y-z)| <= C |x-y| |z-X|^-5'
        },
        'morrey_model':{
            'assumption':'int_{B_R(X)} |u|^2 <= M R on dyadic radii',
            'dyadic_sum_factor':str(geometric_sum),
            'far_delta_grad_p_model':str(dyadic_bound),
            'critical_Gp_far_model':str(Gp_far_model)
        },
        'interpretation':'Differential pressure channels suppress far-field nonlocality by one extra kernel power. Under a critical L2-Morrey bound, the far pressure-gradient oscillation is scale-critically controlled; the near pressure source remains the main unresolved piece.',
        'claim_boundary':'This is a kernel homogeneity/dyadic bridge. Constants, principal values, cutoffs, deformed-cell geometry, and the near-field singular integral must be handled in a rigorous proof.'
    }


def write_md(d,path):
    lines=[
        '# Pressure-difference localization gate','',
        f"Status: **{d['status']}**",'',
        f"Checks passed: **{d['passed']}/{d['total']}**",'',
        '## Far-field cancellation','',
        'The pressure kernel has degree `-3`; its gradient has degree `-4`. Subtracting values at two nearby points introduces one additional derivative in a far-field mean-value estimate.','',
        '`|delta grad p_far| <= C d int_far |u(z)|^2 / |z-X|^5 dz`.','',
        '## Critical Morrey consequence','',
        'If the dyadic local energy obeys `int_{B_R}|u|^2 <= M R`, then the far differential-pressure contribution is bounded at the correct critical scale.','',
        'In the model bookkeeping, `G_p,far = ell^3 int |delta grad p_far|^2` is `O(M^2)`.','',
        '## Route consequence','',
        'The far nonlocal pressure is not automatically harmless, but kernel cancellation makes it a controllable secondary channel once the critical local-energy channel is controlled. The unresolved pressure obstruction is pushed toward the near field.','',
        '## Claim boundary','',d['claim_boundary'],'']
    path.write_text('\n'.join(lines),encoding='utf-8')


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks()
    (out/'pressure_difference_kernel_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
    write_md(d,out/'pressure_difference_kernel_gate.md')
    print(f"Pressure-difference kernel gate: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=='__main__': main()
