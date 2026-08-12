#!/usr/bin/env python3
"""Audit the local occupancy/projective probability inequalities."""
from __future__ import annotations

import argparse, json
from pathlib import Path
import numpy as np

SCHEMA_VERSION='0.1.0'


def audit(seed=9708,n=400):
    rng=np.random.default_rng(seed)
    v=rng.normal(size=(n,3)); v/=np.linalg.norm(v,axis=1)[:,None]
    weights=rng.random(n)+0.02; weights/=np.sum(weights)
    C=np.einsum('n,ni,nj->ij',weights,v,v)
    vals,vecs=np.linalg.eigh(C); i=np.argmax(vals); mu1=float(vals[i]); axis=vecs[:,i]
    Pi=1-mu1; J=float(1-np.trace(C@C))
    off=np.sum(np.cross(v,axis)**2,axis=1)
    Pi_direct=float(np.sum(weights*off))

    # Define an "intense" core from an independent positive amplitude marker.
    amp=rng.lognormal(mean=0.0,sigma=0.8,size=n)
    thresh=np.quantile(amp,0.65); H=amp>=thresh
    h=float(np.sum(weights[H]))
    cond_off=float(np.sum(weights[H]*off[H])/h)

    theta=.55; bad=H & (np.sqrt(off)>=theta)
    bad_cond=float(np.sum(weights[bad])/h)
    bad_bound=Pi/(h*theta*theta)

    # Pairwise projective defect.
    dot=v@v.T; pair=1-dot*dot; ww=weights[:,None]*weights[None,:]
    Jpair=float(np.sum(ww*pair))
    wh=weights[H]; vh=v[H]; doth=vh@vh.T; pairh=1-doth*doth
    JHH=float(np.sum((wh[:,None]*wh[None,:])*pairh)/(h*h))

    return {
      'trace_C':float(np.trace(C)),'Pi':Pi,'Pi_direct':Pi_direct,'Pi_error':abs(Pi-Pi_direct),
      'J':J,'J_pair':Jpair,'J_pair_error':abs(J-Jpair),
      'Pi_lower_margin':Pi-.5*J,'Pi_upper_margin':1.5*J-Pi,
      'h':h,'conditional_off_axis':cond_off,'conditional_off_bound':Pi/h,'conditional_margin':Pi/h-cond_off,
      'theta':theta,'bad_conditional_fraction':bad_cond,'bad_fraction_bound':bad_bound,'bad_margin':bad_bound-bad_cond,
      'JHH':JHH,'core_pair_margin':J-h*h*JHH,
    }


def volume_to_mass_toy(a=.6,rho=.3,ceta=.4):
    # Algebraic implication h >= c_eta a^2 rho under E_r<=W^2 and eta lower bound.
    lower=ceta*a*a*rho
    return {'a':a,'rho':rho,'c_eta':ceta,'lower_bound':lower}


def run_checks():
    a=audit(); v=volume_to_mass_toy()
    checks={
      'principal_axis_defect_identity':a['Pi_error']<1e-12,
      'pairwise_projective_identity':a['J_pair_error']<1e-12,
      'Pi_J_comparison':a['Pi_lower_margin']>-1e-12 and a['Pi_upper_margin']>-1e-12,
      'conditional_axis_bound':a['conditional_margin']>-1e-12,
      'conditional_bad_angle_markov':a['bad_margin']>-1e-12,
      'core_pair_defect_restriction':a['core_pair_margin']>-1e-12,
      'volume_mass_lower_bound_positive':v['lower_bound']>0,
    }
    checks={k:bool(x) for k,x in checks.items()}
    return {'schema_version':SCHEMA_VERSION,'status':'DERIVED OCCUPANCY--PROJECTIVE TRICHOTOMY / PROBABILITY AUDIT','checks':checks,'passed':sum(checks.values()),'total':len(checks),'audit':a,'volume_toy':v,'claim_boundary':'Finite weighted samples verify the probability/covariance inequalities. They do not upgrade averaged alignment to a pointwise regularity criterion.'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args(); out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True); d=run_checks(); (out/'occupancy_projective_trichotomy_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8'); (out/'occupancy_projective_trichotomy_gate.md').write_text(f"# Occupancy-projective trichotomy audit\n\nChecks passed: **{d['passed']}/{d['total']}**\n",encoding='utf-8'); print(f"Occupancy-projective trichotomy: {d['passed']}/{d['total']} checks passed");
    if d['passed']!=d['total']: raise SystemExit(1)
if __name__=='__main__': main()
