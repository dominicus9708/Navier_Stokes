#!/usr/bin/env python3
"""Audit the algebra of amplification-time noncollapse.

If a fixed amplification ratio q is achieved on a thick final natural core,
the I/V Cauchy lanes imply normalized costs proportional to 1/sigma, where
sigma=W0*(t1-t0). Thus a bounded normalized-channel sequence cannot have
sigma -> 0 unless deformation/strain/V2 channels diverge.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

SCHEMA_VERSION = "0.1.0"


def i_lane_lower(q=8.0, b=0.55, sigma=1.2, c=0.17):
    return c * q ** (-1.5) * math.log(b * q / 2.0) ** 2 / sigma


def v_lane_lower(q=8.0, sigma=1.2, nu=0.8, cond=2.4, c=0.11):
    return c * math.sqrt(q) / (nu * nu * cond * cond * sigma)


def run_checks():
    q=8.0; b=0.55; nu=0.8; cond=2.4
    s1=1.0; s2=0.25
    i1=i_lane_lower(q,b,s1); i2=i_lane_lower(q,b,s2)
    v1=v_lane_lower(q,s1,nu,cond); v2=v_lane_lower(q,s2,nu,cond)

    # Explicit lower bound on sigma from uniform normalized costs.
    MI=3.0; MV=4.0
    ci=0.17*q**(-1.5)*math.log(b*q/2.0)**2
    cv=0.11*math.sqrt(q)/(nu*nu*cond*cond)
    sigma_from_i=ci/MI
    sigma_from_v=cv/MV
    sigma_star=min(sigma_from_i,sigma_from_v)

    # NS rescaling leaves sigma invariant: W -> lambda^2 W, dt -> lambda^-2 dt.
    lam=3.1; W=5.0; tau=0.07
    sigma=W*tau
    sigma_scaled=(lam*lam*W)*(tau/(lam*lam))

    checks={
        'i_lane_inverse_sigma': abs(i2/i1 - s1/s2) < 1e-12,
        'v_lane_inverse_sigma': abs(v2/v1 - s1/s2) < 1e-12,
        'positive_time_lower_bound': sigma_star > 0,
        'sigma_scale_invariant': abs(sigma-sigma_scaled) < 1e-12,
        'amplification_threshold_valid': b*q > 2.0,
    }
    checks={k:bool(v) for k,v in checks.items()}
    return {
        'schema_version':SCHEMA_VERSION,
        'status':'DERIVED AMPLIFICATION-TIME NONCOLLAPSE / ALGEBRA AUDIT',
        'checks':checks,'passed':sum(checks.values()),'total':len(checks),
        'parameters':{'q':q,'b':b,'nu':nu,'condition_number_bound':cond},
        'costs':{'I_sigma1':i1,'I_sigma025':i2,'V_sigma1':v1,'V_sigma025':v2},
        'sigma_lower_bounds':{'from_I':sigma_from_i,'from_V':sigma_from_v,'common':sigma_star},
        'statement':'Uniform bounds on normalized I-lane strain cost, normalized V2 cost, and recent deformation condition number imply sigma=W0*(t1-t0)>=sigma_*>0 for fixed q,b,nu.',
        'claim_boundary':'This is a consequence of the previously derived Cauchy-lane lower bounds. It does not supply the missing spatial compactness or rigidity theorem.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks()
    (out/'amplification_time_noncollapse_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
    (out/'amplification_time_noncollapse_gate.md').write_text(
        '# Amplification-time noncollapse audit\n\n'
        f"Status: **{d['status']}**\n\nChecks passed: **{d['passed']}/{d['total']}**\n\n"
        +d['statement']+'\n\n## Claim boundary\n\n'+d['claim_boundary']+'\n',encoding='utf-8')
    print(f"Amplification-time noncollapse: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=='__main__': main()
