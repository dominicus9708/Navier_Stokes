#!/usr/bin/env python3
"""Audit the energy-weighted projective defect identity and factorial sum."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import numpy as np

SCHEMA_VERSION = "0.1.0"


def random_level(seed=9708, nwords=100, nu=0.71):
    rng=np.random.default_rng(seed)
    w=rng.normal(size=(nwords,3))
    F=rng.normal(size=(nwords,3))
    dw=rng.normal(size=(nwords,3,3))
    wn=dw.reshape(nwords*3,3)

    E=float(np.sum(w*w)); N=w.T@w; C=N/E
    J=float(1-np.trace(C@C)); D=E*J
    A=F.T@w; Q=float(np.trace(A)); B=A/E; q=Q/E
    M=float(q*(1-J)-np.trace(C@B))

    En=float(np.sum(wn*wn)); Nn=wn.T@wn; Cn=Nn/En
    Jn=float(1-np.trace(Cn@Cn)); delta2=float(np.linalg.norm(Cn-C)**2)
    r=En/E
    Achain=float(np.trace(C@Cn)-np.trace(C@C))

    Edot=2*Q-2*nu*En
    Jdot=4*M+4*nu*r*Achain
    Ddot_direct=Edot*J+E*Jdot
    Ddot_formula=2*Q*J+4*E*M-2*nu*En*(Jn+delta2)

    Fnorm=float(np.sqrt(np.sum(F*F)))
    rhs_nonlin=2*Q*J+4*E*M
    bound=2*math.sqrt(5)*math.sqrt(max(D,0))*Fnorm

    return {
        'E':E,'J':J,'D':D,'Enext':En,'Jnext':Jn,'Delta2':delta2,
        'Ddot_direct':Ddot_direct,'Ddot_formula':Ddot_formula,
        'Ddot_error':abs(Ddot_direct-Ddot_formula),
        'viscous_dissipation':2*nu*En*(Jn+delta2),
        'nonlinear_source':rhs_nonlin,'nonlinear_bound':bound,
        'nonlinear_margin':bound-rhs_nonlin,
    }


def coefficient_constant_grid():
    xs=np.linspace(0,2/3,10001)
    f=2*np.sqrt(xs)+4*np.sqrt(1-xs)
    idx=int(np.argmax(f))
    return {'J_at_max':float(xs[idx]),'value':float(f[idx]),'target':2*math.sqrt(5),'error':abs(float(f[idx])-2*math.sqrt(5))}


def factorial_sum_audit(seed=100, K=7, ell=0.8, nu=0.9):
    # Independent synthetic levels; audits only summation/scaling algebra.
    rows=[random_level(seed+k,nwords=40+5*k,nu=nu) for k in range(K)]
    Dhat=[]; Fhat=[]; diss=[]
    rng=np.random.default_rng(seed+500)
    # Recreate compatible positive F magnitudes for Cauchy-Schwarz bookkeeping.
    for k,r in enumerate(rows):
        fac=ell**(2*k)/(math.factorial(k)**2)
        Dhat.append(fac*r['D'])
        # Recover an allowed forcing upper proxy from nonlinear bound coefficient.
        if r['D']>1e-14:
            fn=r['nonlinear_bound']/(2*math.sqrt(5)*math.sqrt(r['D']))
        else:
            fn=0.0
        Fhat.append((ell**k/math.factorial(k))*fn)
        diss.append(fac*r['viscous_dissipation'])
    lhs_source=sum(2*math.sqrt(5)*math.sqrt(Dhat[k])*Fhat[k] for k in range(K))
    cs=2*math.sqrt(5)*math.sqrt(sum(Dhat))*math.sqrt(sum(x*x for x in Fhat))
    return {'sum_Dhat':sum(Dhat),'sum_diss':sum(diss),'source_sum':lhs_source,'cauchy_bound':cs,'margin':cs-lhs_source}


def run_checks():
    rows=[random_level(9708+k) for k in range(6)]
    const=coefficient_constant_grid(); fs=factorial_sum_audit()
    checks={
        'all_energy_weighted_identities':all(r['Ddot_error']<1e-10 for r in rows),
        'all_viscous_terms_nonnegative':all(r['viscous_dissipation']>=-1e-12 for r in rows),
        'all_nonlinear_source_bounds':all(r['nonlinear_margin']>=-1e-10 for r in rows),
        'sharp_scalar_constant':const['error']<2e-4,
        'factorial_sum_cauchy_bound':fs['margin']>=-1e-12,
    }
    checks={k:bool(v) for k,v in checks.items()}
    return {
        'schema_version':SCHEMA_VERSION,
        'status':'DERIVED ENERGY-WEIGHTED PROJECTIVE DISSIPATION / ALGEBRA AUDIT',
        'checks':checks,'passed':sum(checks.values()),'total':len(checks),
        'levels':rows,'constant_audit':const,'factorial_sum':fs,
        'identity':'Ddot_k + 2 nu E_{k+1}(J_{k+1}+Delta_k^2) = 2 Q_k J_k + 4 E_k M_N,k.',
        'bound':'RHS <= 2 sqrt(5) sqrt(D_k) ||F_k||_2.',
        'claim_boundary':'This audit checks the finite-dimensional/sequence algebra. It does not control the nonlinear analytic forcing norm for arbitrary Navier-Stokes data.',
    }


def write_md(d,path):
    lines=['# Energy-weighted projective dissipation audit','',f"Status: **{d['status']}**",'',f"Checks passed: **{d['passed']}/{d['total']}**",'',d['identity'],'',d['bound'],'',f"Factorial Cauchy margin: `{d['factorial_sum']['margin']:.3e}`.",'','## Claim boundary','',d['claim_boundary'],'']
    path.write_text('\n'.join(lines),encoding='utf-8')


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args(); out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks(); (out/'energy_weighted_projective_dissipation_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8'); write_md(d,out/'energy_weighted_projective_dissipation_gate.md')
    print(f"Energy-weighted projective dissipation: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=='__main__': main()
