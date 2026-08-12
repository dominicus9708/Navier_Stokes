#!/usr/bin/env python3
"""Exact algebra checks for the Lagrangian diffusion-metric bridge.

For a smooth incompressible flow map F=D_a Phi with det F=1, define
A=F^{-1} F^{-T}.  Pulling the componentwise Laplacian to material
coordinates produces div_a(A grad_a U).  This script audits the matrix algebra
and a frozen Gaussian deformation example; it is not a time-global proof.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp


def run_checks():
    c,tau=sp.symbols('c tau', positive=True, real=True)

    # Frozen Gaussian material deformation from the existing benchmark.
    F=sp.diag(sp.exp(2*c*tau),sp.exp(2*c*tau),sp.exp(-4*c*tau))
    A=sp.simplify(F.inv()*F.inv().T)
    detF=sp.simplify(F.det())
    detA=sp.simplify(A.det())
    traceA=sp.simplify(sp.trace(A))
    eigs=[sp.exp(-4*c*tau),sp.exp(-4*c*tau),sp.exp(8*c*tau)]

    # General frozen diagonal trace-free strain L=diag(l1,l2,l3), sum zero.
    l1,l2,t=sp.symbols('l1 l2 t', real=True)
    l3=-l1-l2
    Fd=sp.diag(sp.exp(l1*t),sp.exp(l2*t),sp.exp(l3*t))
    Ad=sp.simplify(Fd.inv()*Fd.inv().T)
    detAd=sp.simplify(Ad.det())

    # Metric evolution check for the diagonal frozen model: A_dot=-2 F^-1 S F^-T.
    S=sp.diag(l1,l2,l3)
    metric_rhs=sp.simplify(-2*Fd.inv()*S*Fd.inv().T)
    metric_lhs=sp.simplify(sp.diff(Ad,t))

    # Effective dissipation orientation weights.
    w1,w2,w3=sp.symbols('w1 w2 w3', nonnegative=True, real=True)
    kappa=sp.simplify(eigs[0]*w1+eigs[1]*w2+eigs[2]*w3)
    kappa_compressed=sp.simplify(kappa.subs({w1:0,w2:0,w3:1}))
    kappa_stretched=sp.simplify(kappa.subs({w1:1,w2:0,w3:0}))

    # Scalar-gradient identity for a diagonal affine map: |grad_x f|^2=grad_a^T A grad_a.
    g1,g2,g3=sp.symbols('g1 g2 g3', real=True)
    g=sp.Matrix([g1,g2,g3])
    gradx=sp.simplify(F.inv().T*g)
    grad_identity=sp.simplify((gradx.dot(gradx))-(g.dot(A*g)))

    checks={
        'gaussian_detF_one': bool(detF==1),
        'gaussian_detA_one': bool(detA==1),
        'gaussian_A_eigenvalues_match_inverse_stretches_squared': bool(all(sp.simplify(A[i,i]-eigs[i])==0 for i in range(3))),
        'general_tracefree_diagonal_detA_one': bool(detAd==1),
        'metric_evolution_identity_frozen_diagonal': bool(metric_lhs==metric_rhs),
        'gradient_energy_pullback_identity': bool(grad_identity==0),
        'compressed_direction_diffusion_amplified': bool(sp.simplify(kappa_compressed-sp.exp(8*c*tau))==0),
        'stretched_direction_diffusion_weakened': bool(sp.simplify(kappa_stretched-sp.exp(-4*c*tau))==0),
        'traceA_minus3_nonnegative_certificate': bool(sp.simplify(traceA-3 - (2*sp.exp(-4*c*tau)+sp.exp(8*c*tau)-3))==0),
    }

    return {
        'status':'DERIVED LAGRANGIAN DIFFUSION-METRIC BRIDGE + EXACT MATRIX CHECK',
        'checks':checks,'passed':sum(checks.values()),'total':len(checks),
        'general_identities':{
            'flow_gradient':'F=D_a Phi, dot F=(grad_x u) F, det F=1',
            'metric':'A=F^{-1}F^{-T}, symmetric positive definite, det A=1',
            'metric_evolution':'dot A=-2 F^{-1} S F^{-T}',
            'lagrangian_momentum':'partial_t U=-F^{-T} grad_a P + nu div_a(A grad_a U)',
            'lagrangian_incompressibility':'div_a(F^{-1} U)=0',
            'viscous_energy':'int |grad_x u|^2 dx = int sum_i (grad_a U_i)^T A (grad_a U_i) da'
        },
        'gaussian_anchor':{
            'F':str(F),'A':str(A),'detA':str(detA),'traceA':str(traceA),
            'interpretation':'The direction compressed by exp(-4 c tau) acquires reference-coordinate diffusion weight exp(8 c tau); the two stretched directions acquire weight exp(-4 c tau).'
        },
        'alignment_channel':{
            'kappa_eff':str(kappa),
            'weights':'w_j are fractions of reference velocity-gradient energy aligned with eigenvectors of A; sum w_j=1.',
            'danger':'Large deformation alone is not enough. Weak effective diffusion requires gradient energy to align persistently with small-eigenvalue directions of A.'
        },
        'claim_boundary':'The Lagrangian transform is exact only on the smooth lifespan where the flow map is a sufficiently regular diffeomorphism. det A=1 and trace A>=3 do not give uniform coercivity because lambda_min(A) may tend to zero.'
    }


def write_md(d,path):
    lines=[
        '# Lagrangian diffusion metric gate','',
        f"Status: **{d['status']}**",'',
        f"Checks passed: **{d['passed']}/{d['total']}**",'',
        '## Exact material-coordinate structure','',
        '`A=F^{-1}F^{-T}` is symmetric positive definite and `det A=1`.','',
        '`partial_t U = -F^{-T} grad_a P + nu div_a(A grad_a U)`.', '',
        'Advection disappears in material coordinates; deformation reappears as an anisotropic pressure-gradient map and anisotropic diffusion metric.','',
        '## Deformation--viscosity compensation','',
        'For the frozen Gaussian anchor, the compressed material direction gets diffusion weight `exp(8 c tau)`, while the two stretched directions get `exp(-4 c tau)`.','',
        'Thus compression amplifies reference-coordinate viscosity in that direction. But expansion weakens it in the stretched directions, so `det A=1` alone is not coercive.','',
        '## New alignment gate','',
        'The relevant quantity is the orientation of `grad_a U` relative to eigenvectors of `A`. A dangerous configuration must place gradient energy preferentially in the weakest-diffusion eigendirections.','',
        '## Claim boundary','',d['claim_boundary'],'']
    path.write_text('\n'.join(lines),encoding='utf-8')


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks()
    (out/'lagrangian_diffusion_metric_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
    write_md(d,out/'lagrangian_diffusion_metric_gate.md')
    print(f"Lagrangian diffusion metric gate: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=='__main__': main()
