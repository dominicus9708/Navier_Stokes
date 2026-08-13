#!/usr/bin/env python3
"""Audit the enstrophy-weighted magnitude interpolation deficit.

For dmu=f^2/int f^2, define m=E_mu[f] and v=Var_mu(f). Then the
L2-L3-L6 interpolation ratio obeys R <= (1+v/m^2)^(-1/2).
This script checks the moment identity/inequality on random finite samples and
its Navier--Stokes scaling invariance.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np

SCHEMA_VERSION='0.1.0'


def sample(seed=0,n=5000):
    rng=np.random.default_rng(seed)
    f=np.abs(rng.normal(size=n))+0.02
    E=float(np.sum(f**2)); mu=f**2/E
    m=float(np.sum(mu*f)); m2=float(np.sum(mu*f**2)); m4=float(np.sum(mu*f**4)); v=m2-m*m
    R=m/(m4**0.25)
    bound=(1+v/(m*m))**-0.5
    return {'m':m,'v':v,'R':R,'bound':bound,'margin':bound-R,'moment_margin':m4-m2*m2}


def constant_sample(n=1000,c=2.3):
    f=np.full(n,c); E=np.sum(f**2); mu=f**2/E; m=np.sum(mu*f); m2=np.sum(mu*f**2); m4=np.sum(mu*f**4); v=m2-m*m
    R=m/m4**0.25
    return {'v':float(v),'R':float(R)}


def scaling_sample(seed=33,lam=4.7,n=2000):
    rng=np.random.default_rng(seed); f=np.abs(rng.normal(size=n))+0.1
    def chi(a):
        E=np.sum(a*a); mu=a*a/E; m=np.sum(mu*a); v=np.sum(mu*a*a)-m*m; return v/(m*m)
    return {'base':float(chi(f)),'scaled':float(chi((lam**2)*f))}


def run_checks():
    rows=[sample(9708+i) for i in range(30)]; const=constant_sample(); sc=scaling_sample()
    checks={
      'moment_Cauchy_nonnegative':all(r['moment_margin']>=-1e-11 for r in rows),
      'interpolation_deficit_bound':all(r['margin']>=-1e-11 for r in rows),
      'constant_profile_saturates':abs(const['v'])<1e-11 and abs(const['R']-1)<1e-12,
      'chi_scale_invariant':abs(sc['base']-sc['scaled'])<1e-12,
    }
    checks={k:bool(v) for k,v in checks.items()}
    return {
      'schema_version':SCHEMA_VERSION,
      'status':'DERIVED MAGNITUDE-HETEROGENEITY INTERPOLATION GAP / MOMENT AUDIT',
      'checks':checks,'passed':sum(checks.values()),'total':len(checks),
      'min_margin':min(r['margin'] for r in rows),'constant':const,'scaling':sc,
      'identity':'R_int=||f||_3^3/(||f||_2^(3/2)||f||_6^(3/2)) <= (1+chi_mag)^(-1/2), chi_mag=Var_mu(f)/(E_mu f)^2, dmu=f^2 dx/int f^2.',
      'claim_boundary':'The finite-sample audit checks the moment inequality. The functional compactness-rigidity step for cutoff H_0^1 profiles is analytical and documented separately.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args(); out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks(); (out/'magnitude_heterogeneity_gap_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
    (out/'magnitude_heterogeneity_gap_gate.md').write_text('# Magnitude heterogeneity gap audit\n\nChecks passed: **%d/%d**\n\n%s\n\n## Claim boundary\n\n%s\n'%(d['passed'],d['total'],d['identity'],d['claim_boundary']),encoding='utf-8')
    print(f"Magnitude heterogeneity gap: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)
if __name__=='__main__': main()
