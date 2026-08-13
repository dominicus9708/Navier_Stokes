#!/usr/bin/env python3
"""Audit exact multicore projective and magnitude-variance aggregation laws."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np

SCHEMA_VERSION='0.1.0'


def random_psd_trace1(rng):
    A=rng.normal(size=(3,3)); C=A@A.T; return C/np.trace(C)


def covariance_trial(seed=9708,N=7):
    rng=np.random.default_rng(seed); w=rng.random(N); w/=w.sum(); Cs=[random_psd_trace1(rng) for _ in range(N)]
    C=sum(w[i]*Cs[i] for i in range(N)); J=lambda X: float(1-np.trace(X@X))
    lhs=J(C); within=sum(w[i]*J(Cs[i]) for i in range(N)); between=0.5*sum(w[i]*w[j]*np.linalg.norm(Cs[i]-Cs[j],'fro')**2 for i in range(N) for j in range(N))
    return {'lhs':lhs,'rhs':within+between,'error':abs(lhs-within-between),'within':within,'between':between}


def rankone_trial(seed=12,N=6):
    rng=np.random.default_rng(seed); w=rng.random(N); w/=w.sum(); ns=[]
    for _ in range(N):
        n=rng.normal(size=3); n/=np.linalg.norm(n); ns.append(n)
    Cs=[np.outer(n,n) for n in ns]; C=sum(w[i]*Cs[i] for i in range(N)); J=float(1-np.trace(C@C))
    rhs=sum(w[i]*w[j]*(1-float(np.dot(ns[i],ns[j])**2)) for i in range(N) for j in range(N))
    return {'J':J,'rhs':rhs,'error':abs(J-rhs)}


def variance_trial(seed=99,N=5):
    rng=np.random.default_rng(seed); w=rng.random(N); w/=w.sum(); means=rng.uniform(.2,3,size=N); vars_=rng.uniform(0,1,size=N)
    m=float(np.sum(w*means)); total=float(np.sum(w*(vars_+(means-m)**2))); second=float(np.sum(w*(vars_+means**2))); direct=second-m*m
    return {'total_variance':total,'direct':direct,'error':abs(total-direct),'within':float(np.sum(w*vars_)),'between':float(np.sum(w*(means-m)**2))}


def finite_core_bound(ME=12.0,b=.6,theta=.2):
    Nmax=ME/(b*b*theta); return {'Nmax':Nmax,'floor':b*b*theta,'product':Nmax*b*b*theta}


def run_checks():
    cov=[covariance_trial(9708+i) for i in range(30)]; rk=[rankone_trial(300+i) for i in range(20)]; var=[variance_trial(700+i) for i in range(30)]; fc=finite_core_bound()
    checks={
      'covariance_total_dispersion_identity':max(r['error'] for r in cov)<1e-11,
      'within_between_nonnegative':all(r['within']>=-1e-12 and r['between']>=-1e-12 for r in cov),
      'rankone_axis_mismatch_identity':max(r['error'] for r in rk)<1e-11,
      'law_of_total_variance':max(r['error'] for r in var)<1e-12,
      'variance_parts_nonnegative':all(r['within']>=0 and r['between']>=-1e-12 for r in var),
      'finite_thick_core_budget':abs(fc['product']-12.0)<1e-12,
    }
    checks={k:bool(v) for k,v in checks.items()}
    return {
      'schema_version':SCHEMA_VERSION,'status':'EXACT MULTICORE STATIC-AGGREGATION / ALGEBRA AUDIT','checks':checks,'passed':sum(checks.values()),'total':len(checks),
      'max_covariance_error':max(r['error'] for r in cov),'max_rankone_error':max(r['error'] for r in rk),'max_variance_error':max(r['error'] for r in var),'finite_core':fc,
      'projective_identity':'J(sum w_i C_i)=sum w_i J(C_i)+(1/2)sum_ij w_i w_j ||C_i-C_j||_F^2.',
      'magnitude_identity':'Var_mu(rho)=sum_i w_i Var_{mu_i}(rho)+sum_i w_i(m_i-m)^2.',
      'claim_boundary':'These are exact finite-component aggregation identities. Geometric decomposition of a PDE dangerous set into retained thick components is handled separately.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args(); out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks(); (out/'multicore_static_aggregation_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
    (out/'multicore_static_aggregation_gate.md').write_text('# Multicore static aggregation audit\n\nChecks passed: **%d/%d**\n\n%s\n\n%s\n\n## Claim boundary\n\n%s\n'%(d['passed'],d['total'],d['projective_identity'],d['magnitude_identity'],d['claim_boundary']),encoding='utf-8')
    print(f"Multicore aggregation: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)
if __name__=='__main__': main()
