#!/usr/bin/env python3
"""Audit the Fourier interpolation from derivative covariance to base anisotropy."""
from __future__ import annotations

import argparse, json, math
from pathlib import Path
import numpy as np

SCHEMA_VERSION='0.1.0'


def optimize(A,B,k):
    if B<=0: return 0.0, float('inf')
    K=(k*B/A)**(1/(2*k+2))
    val=A*K*K+B*K**(-2*k)
    ck=(k+1)*k**(-k/(k+1))
    pred=ck*A**(k/(k+1))*B**(1/(k+1))
    return val,pred


def scalar_audit():
    rows=[]; maxerr=0
    for k in range(1,8):
        for A,B in [(0.7,1.3),(4.2,0.08),(2.0,3.0)]:
            val,pred=optimize(A,B,k); err=abs(val-pred); maxerr=max(maxerr,err); rows.append({'k':k,'A':A,'B':B,'minimum':val,'formula':pred,'error':err})
    return {'rows':rows,'max_error':maxerr}


def covariance_comparison(seed=9708,samples=200):
    rng=np.random.default_rng(seed); minmargin=1e9
    for _ in range(samples):
        M=rng.normal(size=(3,3)); C=M@M.T; C/=np.trace(C)
        vals=np.linalg.eigvalsh(C)[::-1]; Pi=1-vals[0]; J=1-np.trace(C@C); minmargin=min(minmargin,1.5*J-Pi)
    return {'min_margin_Pi_le_3J2':float(minmargin)}


def k1_constant():
    k=1; ck=(k+1)*k**(-k/(k+1)); C=ck**2*(1.5)**(2/(k+1)); return {'c1':ck,'projective_constant':C,'target':6.0,'error':abs(C-6.0)}


def synthetic_frequency_split(seed=77,k=2,N=10000):
    rng=np.random.default_rng(seed)
    # Synthetic Fourier samples with radii and vector amplitudes; validates low/high inequalities.
    rad=np.exp(rng.normal(size=N)); uhat=rng.normal(size=(N,3));
    # Build omega amplitudes with |omega|<=|xi||u|, not exact curl orientation; enough for scalar bound audit.
    om=rng.normal(size=(N,3)); om_norm=np.linalg.norm(om,axis=1); u_norm=np.linalg.norm(uhat,axis=1)
    scale=np.minimum(1.0, rad*u_norm/np.maximum(om_norm,1e-12)); om*=scale[:,None]
    n=np.array([1.,0.,0.]); perp=om.copy(); perp[:,0]=0
    A=float(np.sum(u_norm*u_norm)); B=float(np.sum((rad**(2*k))*np.sum(perp*perp,axis=1)))
    K=(k*B/A)**(1/(2*k+2)); low=rad<=K; high=~low
    actual=float(np.sum(np.sum(perp*perp,axis=1)))
    low_bound=A*K*K; high_bound=B*K**(-2*k)
    return {'actual':actual,'bound':low_bound+high_bound,'margin':low_bound+high_bound-actual,'K':K}


def run_checks():
    s=scalar_audit(); c=covariance_comparison(); k1=k1_constant(); f=synthetic_frequency_split()
    checks={
      'optimized_threshold_formula':s['max_error']<1e-10,
      'Pi_projective_comparison':c['min_margin_Pi_le_3J2']>-1e-12,
      'k1_constant_six':k1['error']<1e-12,
      'synthetic_low_high_bound':f['margin']>-1e-10,
    }
    checks={k:bool(v) for k,v in checks.items()}
    return {'schema_version':SCHEMA_VERSION,'status':'DERIVED HIGH-ORDER-TO-BASE FOURIER ANISOTROPY / ALGEBRA AUDIT','checks':checks,'passed':sum(checks.values()),'total':len(checks),'optimization':s,'covariance':c,'k1':k1,'frequency':f,'bridge':'||n_k x omega||_2^4 <= C_k ||u||_2^(4k/(k+1)) D_k^(2/(k+1)).','k1_bridge':'||n_1 x omega||_2^4 <= 6 ||u||_2^2 D_1.','claim_boundary':'The external regularity implication uses Miller Theorem 1.6. This script audits only the Fourier/covariance interpolation algebra.'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args(); out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True); d=run_checks(); (out/'high_order_to_base_anisotropy_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8'); (out/'high_order_to_base_anisotropy_gate.md').write_text(f"# High-order to base anisotropy audit\n\nChecks passed: **{d['passed']}/{d['total']}**\n\n{d['bridge']}\n\n{d['k1_bridge']}\n",encoding='utf-8'); print(f"High-order to base anisotropy: {d['passed']}/{d['total']} checks passed");
    if d['passed']!=d['total']: raise SystemExit(1)
if __name__=='__main__': main()
