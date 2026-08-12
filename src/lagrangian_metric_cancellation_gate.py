#!/usr/bin/env python3
"""Exact algebra showing that the Lagrangian diffusion metric is a coordinate rewrite.

A=F^{-1}F^{-T} and grad_a U=(grad_x u)F imply
(grad_a U) A (grad_a U)^T=(grad_x u)(grad_x u)^T pointwise.
Thus large/small eigenvalues of A do not create extra physical viscosity by
themselves.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp


def run_checks():
    # General invertible symbolic 2x2 block is enough to audit the matrix cancellation
    # without making SymPy invert a fully generic 3x3 symbolic matrix.
    a,b,c,d=sp.symbols('a b c d', real=True)
    l11,l12,l21,l22=sp.symbols('l11 l12 l21 l22', real=True)
    F=sp.Matrix([[a,b],[c,d]])
    L=sp.Matrix([[l11,l12],[l21,l22]])
    det=sp.simplify(F.det())
    A=sp.simplify(F.inv()*F.inv().T)
    Ga=sp.simplify(L*F)
    lhs=sp.simplify(Ga*A*Ga.T)
    rhs=sp.simplify(L*L.T)
    residual=sp.simplify(lhs-rhs)

    # Diagonal 3D incompressible example.
    M,t=sp.symbols('M t', positive=True, real=True)
    S=sp.diag(-M,0,M)
    F3=sp.diag(sp.exp(-M*t),1,sp.exp(M*t))
    A3=sp.simplify(F3.inv()*F3.inv().T)
    Ga3=sp.simplify(S*F3)
    diss_ref=sp.simplify(sp.trace(Ga3*A3*Ga3.T))
    diss_phys=sp.simplify(sp.trace(S*S.T))

    checks={
        'general_block_metric_cancellation': all(sp.simplify(v)==0 for v in residual),
        'diagonal_3d_metric_det_one': bool(sp.simplify(A3.det())==1),
        'diagonal_3d_reference_metric_dissipation_equals_physical': bool(sp.simplify(diss_ref-diss_phys)==0),
        'diagonal_3d_physical_dissipation_constant': bool(diss_phys==2*M**2),
    }

    return {
        'status':'DERIVED COORDINATE-CANCELLATION IDENTITY / ROUTE PRUNING',
        'checks':checks,'passed':sum(checks.values()),'total':len(checks),
        'identity':'With grad_a U=(grad_x u)F and A=F^{-1}F^{-T}, one has (grad_a U)A(grad_a U)^T=(grad_x u)(grad_x u)^T pointwise.',
        'consequence':'The anisotropic Lagrangian diffusion metric is an exact coordinate representation of the original physical viscous dissipation. Its large eigenvalues are not an independent source of enhanced viscosity, and its small eigenvalues are not independently a loss of physical viscosity.',
        'retained_value':'Material coordinates remain useful because they remove explicit advection and keep the reference domain fixed, but any proof gain must come from estimates on the coupled transformed system rather than eigenvalues of A alone.',
        'route_status':'A-eigenvalue-only deformation-viscosity compensation as a new coercive mechanism: FAILED ROUTE (algebraic coordinate cancellation).'
    }


def write_md(d,path):
    lines=['# Lagrangian metric cancellation gate','',f"Status: **{d['status']}**",'',f"Checks passed: **{d['passed']}/{d['total']}**",'',d['identity'],'',d['consequence'],'',f"**Route status:** {d['route_status']}",'',d['retained_value'],'']
    path.write_text('\n'.join(lines),encoding='utf-8')


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks()
    (out/'lagrangian_metric_cancellation_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
    write_md(d,out/'lagrangian_metric_cancellation_gate.md')
    print(f"Lagrangian metric cancellation gate: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=='__main__': main()
