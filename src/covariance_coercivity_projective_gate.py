#!/usr/bin/env python3
"""Audit the covariance coercivity J(D)+||D-C||_F^2 >= 3/8 J(C)^2."""
from __future__ import annotations

import argparse, json
from pathlib import Path
import numpy as np

SCHEMA_VERSION='0.1.0'


def random_cov(rng):
    M=rng.normal(size=(3,3)); C=M@M.T; C/=np.trace(C); return C


def audit(seed=9708,samples=1000):
    rng=np.random.default_rng(seed); min_margin=1e9; min_exact=1e9; worst=None
    for _ in range(samples):
        C=random_cov(rng); D=random_cov(rng)
        vals=np.linalg.eigvalsh(C)[::-1]; Pi=float(1-vals[0]); J=float(1-np.trace(C@C))
        Jd=float(1-np.trace(D@D)); delta2=float(np.linalg.norm(D-C)**2)
        lhs=Jd+delta2; exact=2*Pi-J; quad=3/8*J*J
        min_margin=min(min_margin,lhs-quad); min_exact=min(min_exact,lhs-exact)
        if worst is None or lhs-quad<worst['margin']:
            worst={'eigenvalues':vals.tolist(),'J':J,'Pi':Pi,'lhs':lhs,'exact_floor':exact,'quadratic_floor':quad,'margin':lhs-quad}
    return {'samples':samples,'min_quadratic_margin':min_margin,'min_exact_optimization_margin':min_exact,'worst':worst}


def sharp_order():
    eps=np.logspace(-8,-2,80); ratios=[]
    for e in eps:
        C=np.diag([1-e,e/2,e/2]); vals=np.diag(C); Pi=e; J=float(1-np.trace(C@C)); exact=2*Pi-J; ratios.append(exact/(J*J))
    return {'last_small_epsilon_ratio':ratios[0],'target':3/8,'error':abs(ratios[0]-3/8),'min_ratio':min(ratios)}


def optimized_D_case(seed=99):
    rng=np.random.default_rng(seed); C=random_cov(rng); vals,vecs=np.linalg.eigh(C); i=np.argmax(vals); n=vecs[:,i]; D=np.outer(n,n)
    mu1=float(vals[i]); Pi=1-mu1; J=float(1-np.trace(C@C)); lhs=float(1-np.trace(D@D)+np.linalg.norm(D-C)**2); exact=2*Pi-J
    return {'lhs':lhs,'exact':exact,'error':abs(lhs-exact)}


def run_checks():
    a=audit(); s=sharp_order(); o=optimized_D_case()
    checks={
      'random_quadratic_coercivity':a['min_quadratic_margin']>-1e-12,
      'random_exact_floor':a['min_exact_optimization_margin']>-1e-12,
      'rank_one_optimizer_attains_floor':o['error']<1e-12,
      'three_eighths_small_defect_sharp_order':s['error']<1e-6,
    }
    checks={k:bool(v) for k,v in checks.items()}
    return {'schema_version':SCHEMA_VERSION,'status':'DERIVED COVARIANCE COERCIVITY / MATRIX AUDIT','checks':checks,'passed':sum(checks.values()),'total':len(checks),'random':a,'sharp_order':s,'optimizer':o,'identity':'J(D)+||D-C||_F^2 >= 2 Pi(C)-J(C) >= (3/8)J(C)^2.','claim_boundary':'Finite-dimensional matrix inequality only; its PDE use is through the separately derived energy-weighted covariance chain.'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args(); out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True); d=run_checks(); (out/'covariance_coercivity_projective_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8'); (out/'covariance_coercivity_projective_gate.md').write_text(f"# Covariance coercivity audit\n\nChecks passed: **{d['passed']}/{d['total']}**\n\n{d['identity']}\n",encoding='utf-8'); print(f"Covariance coercivity: {d['passed']}/{d['total']} checks passed");
    if d['passed']!=d['total']: raise SystemExit(1)
if __name__=='__main__': main()
