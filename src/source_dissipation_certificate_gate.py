#!/usr/bin/env python3
"""Audit the combined dimensionless source/dissipation certificate algebra."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np

SCHEMA_VERSION='0.1.0'


def certificate(E,P,eta,chi,nu=0.7,C=1.9):
    return (nu**4*P/(C**4*E**3))*((1+chi)**2/((1-eta)**3))


def ratio_upper(E,P,eta,chi,nu=0.7,C=1.9):
    return (C/nu)*E**0.75*P**(-0.25)*(1-eta)**0.75*(1+chi)**-0.5


def scaling_trial(lam=3.4):
    E=2.3; P=7.2; eta=.31; chi=.44
    d0=certificate(E,P,eta,chi)
    d1=certificate(lam*E,lam**3*P,eta,chi)
    return {'base':d0,'scaled':d1,'error':abs(d0-d1)}


def random_trials(seed=9708,N=1000):
    rng=np.random.default_rng(seed); maxerr=0.; violations=0
    for _ in range(N):
        E=float(np.exp(rng.normal())); P=float(np.exp(rng.normal())); eta=float(rng.uniform(0,.95)); chi=float(rng.uniform(0,3)); nu=float(rng.uniform(.2,2)); C=float(rng.uniform(.5,3))
        D=certificate(E,P,eta,chi,nu,C); R=ratio_upper(E,P,eta,chi,nu,C)
        maxerr=max(maxerr,abs(R**4-1/D))
        if D>1 and R>=1+1e-12: violations+=1
    return {'max_fourth_power_error':maxerr,'violations_Dgt1':violations}


def deficit_monotonicity():
    E=2.; P=5.; nu=.8; C=1.7
    base=certificate(E,P,0,0,nu,C); directional=certificate(E,P,.3,0,nu,C); magnitude=certificate(E,P,0,.7,nu,C); both=certificate(E,P,.3,.7,nu,C)
    return {'base':base,'directional':directional,'magnitude':magnitude,'both':both}


def run_checks():
    sc=scaling_trial(); rt=random_trials(); dm=deficit_monotonicity()
    checks={
      'certificate_scale_invariant':sc['error']<1e-12,
      'ratio_fourth_power_inverse_certificate':rt['max_fourth_power_error']<1e-10,
      'D_gt_one_forces_upper_ratio_below_one':rt['violations_Dgt1']==0,
      'directional_deficit_increases_D':dm['directional']>dm['base'],
      'magnitude_deficit_increases_D':dm['magnitude']>dm['base'],
      'combined_deficits_strongest':dm['both']>max(dm['directional'],dm['magnitude']),
    }
    checks={k:bool(v) for k,v in checks.items()}
    return {'schema_version':SCHEMA_VERSION,'status':'DERIVED SOURCE/DISSIPATION CERTIFICATE / ALGEBRA AUDIT','checks':checks,'passed':sum(checks.values()),'total':len(checks),'scaling':sc,'random':rt,'deficits':dm,'certificate':'D=nu^4 P (1+chi_mag)^2 / [C_*^4 E^3 (1-eta_ang)^3].','implication':'D>1 implies the refined source upper bound is < nu P, hence global enstrophy decreases.','claim_boundary':'The analytical source constant C_* and local shell/far-field remainders are not established by this algebra audit.'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args(); out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks(); (out/'source_dissipation_certificate_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8'); (out/'source_dissipation_certificate_gate.md').write_text('# Source/dissipation certificate audit\n\nChecks passed: **%d/%d**\n\n%s\n\n%s\n\n## Claim boundary\n\n%s\n'%(d['passed'],d['total'],d['certificate'],d['implication'],d['claim_boundary']),encoding='utf-8'); print(f"Source/dissipation certificate: {d['passed']}/{d['total']} checks passed");
    if d['passed']!=d['total']: raise SystemExit(1)
if __name__=='__main__': main()
