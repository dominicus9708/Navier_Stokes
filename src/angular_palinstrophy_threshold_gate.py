#!/usr/bin/env python3
"""Audit the one-variable source/dissipation optimization.

For fixed E and angular palinstrophy A, the refined source ratio contains
f(x)=(x-1)^(3/4)/x with x=P/A>1. Its unique maximum is at x=4,
with value 3^(3/4)/4. This script checks that algebra and the fourth-power
threshold 27/256. It does not determine the analytical Sobolev/CZ constant.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np

SCHEMA_VERSION='0.1.0'


def f(x): return (x-1.0)**0.75/x


def run_checks():
    xs=np.linspace(1.0001,20.0,300000)
    vals=np.array([f(float(x)) for x in xs])
    idx=int(np.argmax(vals)); xmax=float(xs[idx]); vmax=float(vals[idx])
    target=3**0.75/4
    fourth=target**4

    # symbolic-equivalent derivative sign samples around x=4:
    # d log f/dx = 3/[4(x-1)] - 1/x.
    left=3/(4*(3.0-1))-1/3.0
    at=3/(4*(4.0-1))-1/4.0
    right=3/(4*(6.0-1))-1/6.0

    # Including an interpolation deficit h multiplies the fourth-power threshold by h^4.
    chi=0.7; h=(1+chi)**-0.5
    threshold_ratio=h**4
    target_ratio=(1+chi)**-2

    checks={
      'numeric_max_near_four':abs(xmax-4.0)<2e-4,
      'max_value_exact':abs(vmax-target)<1e-9,
      'fourth_power_27_over_256':abs(fourth-27/256)<1e-14,
      'derivative_changes_sign':left>0 and abs(at)<1e-14 and right<0,
      'heterogeneity_threshold_factor':abs(threshold_ratio-target_ratio)<1e-14,
    }
    checks={k:bool(v) for k,v in checks.items()}
    return {
      'schema_version':SCHEMA_VERSION,
      'status':'DERIVED ANGULAR-PALINSTROPHY SOURCE/DISSIPATION OPTIMIZATION / ALGEBRA AUDIT',
      'checks':checks,'passed':sum(checks.values()),'total':len(checks),
      'xmax_numeric':xmax,'vmax_numeric':vmax,'target_max':target,'fourth_power':fourth,
      'identity':'max_{P>A} (P-A)^(3/4)/P = (3^(3/4)/4) A^(-1/4), attained at P=4A.',
      'threshold':'If A > [27 C_*^4/(256 nu^4)] E^3, the refined source upper bound is strictly below nu P for every P>A.',
      'claim_boundary':'C_* is an analytical Sobolev/Calderon-Zygmund constant and is not evaluated by this script.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args(); out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks(); (out/'angular_palinstrophy_threshold_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
    (out/'angular_palinstrophy_threshold_gate.md').write_text('# Angular palinstrophy threshold audit\n\nChecks passed: **%d/%d**\n\n%s\n\n%s\n\n## Claim boundary\n\n%s\n'%(d['passed'],d['total'],d['identity'],d['threshold'],d['claim_boundary']),encoding='utf-8')
    print(f"Angular palinstrophy threshold: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)
if __name__=='__main__': main()
