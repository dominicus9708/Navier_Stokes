#!/usr/bin/env python3
"""Audit constant-axis strain/off-axis Fourier identities.

This is a symbol-level audit on random divergence-free Fourier modes.
"""
from __future__ import annotations

import argparse, json
from pathlib import Path
import numpy as np

SCHEMA_VERSION='0.1.0'


def unit(v):
    return v/np.linalg.norm(v)


def mode_audit(rng,k=0):
    xi=rng.normal(size=3)
    while np.linalg.norm(xi)<1e-3:
        xi=rng.normal(size=3)
    n=unit(rng.normal(size=3))
    w0=rng.normal(size=3)
    # Project onto xi-perp to enforce div omega=0.
    w=w0-xi*np.dot(xi,w0)/np.dot(xi,xi)
    if np.linalg.norm(w)<1e-8:
        w=np.cross(xi,n)
    r=np.linalg.norm(xi)
    # Ignore harmless Fourier i/sign factors.
    u=np.cross(xi,w)/(r*r)
    Sn=0.5*((np.dot(xi,n))*u + xi*np.dot(u,n))
    off=np.cross(n,w)
    weight=r**(2*k)
    return {
      'xi':xi.tolist(),'n':n.tolist(),
      'symbol_error':abs(4*np.dot(Sn,Sn)-np.dot(off,off)),
      'weighted_symbol_error':abs(4*weight*np.dot(Sn,Sn)-weight*np.dot(off,off)),
      'u2':float(np.dot(u,u)),
      'O':float(np.dot(off,off)),
      'G':float(r*r*np.dot(off,off)),
    }


def ensemble(seed=9708,nmodes=500):
    rng=np.random.default_rng(seed)
    rows=[mode_audit(rng,k=(j%5)) for j in range(nmodes)]
    U=sum(r['u2'] for r in rows)
    O=sum(r['O'] for r in rows)
    G=sum(r['G'] for r in rows)
    return {
      'max_symbol_error':max(r['symbol_error'] for r in rows),
      'max_weighted_symbol_error':max(r['weighted_symbol_error'] for r in rows),
      'U':U,'O':O,'G':G,
      'Hminus1_margin':U*G-O*O,
    }


def exact_one_axis_mode(seed=42):
    rng=np.random.default_rng(seed); n=unit(rng.normal(size=3))
    # Choose xi perpendicular to n, so w=n is divergence-free and exactly one-axis.
    q=rng.normal(size=3); xi=q-n*np.dot(n,q)
    if np.linalg.norm(xi)<1e-8:
        xi=np.cross(n,[1.,0.,0.])
    w=n.copy(); r=np.linalg.norm(xi); u=np.cross(xi,w)/(r*r); Sn=.5*(np.dot(xi,n)*u+xi*np.dot(u,n)); off=np.cross(n,w)
    return {'off_norm':float(np.linalg.norm(off)),'Sn_norm':float(np.linalg.norm(Sn))}


def run_checks():
    a=ensemble(); z=exact_one_axis_mode()
    checks={
      'pointwise_fourier_isometry':a['max_symbol_error']<1e-10,
      'derivative_weighted_isometry':a['max_weighted_symbol_error']<1e-8,
      'Hminus1_Riccati_coercivity':a['Hminus1_margin']>-1e-8,
      'exact_one_axis_zero_Sn':z['off_norm']<1e-12 and z['Sn_norm']<1e-12,
    }
    checks={k:bool(v) for k,v in checks.items()}
    return {'schema_version':SCHEMA_VERSION,'status':'DERIVED CONSTANT-AXIS STRAIN/OFF-AXIS FOURIER AUDIT','checks':checks,'passed':sum(checks.values()),'total':len(checks),'ensemble':a,'one_axis':z,'identity':'4|S_hat(xi)n|^2=|n x omega_hat(xi)|^2 for xi·omega_hat=0.','coercivity':'||grad(n x omega)||_2^2 >= ||n x omega||_2^4/||u||_2^2.','claim_boundary':'Symbol/sequence audit only. The optimal-axis time evolution is justified separately by fixed-axis balances and an upper-Dini minimization argument.'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args(); out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True); d=run_checks(); (out/'constant_axis_strain_offaxis_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8'); (out/'constant_axis_strain_offaxis_gate.md').write_text(f"# Constant-axis strain/off-axis Fourier audit\n\nChecks passed: **{d['passed']}/{d['total']}**\n\n{d['identity']}\n\n{d['coercivity']}\n",encoding='utf-8'); print(f"Constant-axis strain/off-axis: {d['passed']}/{d['total']} checks passed");
    if d['passed']!=d['total']: raise SystemExit(1)
if __name__=='__main__': main()
