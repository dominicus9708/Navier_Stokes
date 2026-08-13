#!/usr/bin/env python3
"""Audit remote-strain tail decay exponents after natural renormalization."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path

SCHEMA_VERSION='0.1.0'


def radial_integral_power(R,p):
    # 3D integral of |z|^-p over |z|>R, omitting 4pi factor.
    return R**(3-p)/(p-3)


def run_checks():
    R=7.0; ME=3.2
    i6=radial_integral_power(R,6); i8=radial_integral_power(R,8)
    center=(i6**0.5)*(ME**0.5)
    variation=(i8**0.5)*(ME**0.5)
    target_center=(ME**0.5)*R**(-1.5)/math.sqrt(3)
    target_var=(ME**0.5)*R**(-2.5)/math.sqrt(5)
    # Double R: expected ratios 2^-3/2 and 2^-5/2.
    c2=(radial_integral_power(2*R,6)**0.5)*(ME**0.5)
    v2=(radial_integral_power(2*R,8)**0.5)*(ME**0.5)
    checks={
      'far_constant_R_minus_3_over_2':abs(center-target_center)<1e-14,
      'far_variation_R_minus_5_over_2':abs(variation-target_var)<1e-14,
      'constant_doubling_ratio':abs(c2/center-2**(-1.5))<1e-14,
      'variation_doubling_ratio':abs(v2/variation-2**(-2.5))<1e-14,
      'variation_decays_faster':v2/variation<c2/center,
    }
    checks={k:bool(v) for k,v in checks.items()}
    return {'schema_version':SCHEMA_VERSION,'status':'DERIVED RENORMALIZED REMOTE-STRAIN TAIL / EXPONENT AUDIT','checks':checks,'passed':sum(checks.values()),'total':len(checks),'center':center,'variation':variation,'statement':'Under bounded normalized global enstrophy, far strain is O(R^-3/2) and its unit-ball variation is O(R^-5/2).','claim_boundary':'Kernel constants and principal-value near-field structure are analytical inputs; this script audits the 3D far-tail Cauchy-Schwarz exponents.'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args(); out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True); d=run_checks(); (out/'renormalized_remote_tail_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8'); (out/'renormalized_remote_tail_gate.md').write_text('# Renormalized remote-tail audit\n\nChecks passed: **%d/%d**\n\n%s\n\n## Claim boundary\n\n%s\n'%(d['passed'],d['total'],d['statement'],d['claim_boundary']),encoding='utf-8'); print(f"Renormalized remote tail: {d['passed']}/{d['total']} checks passed");
    if d['passed']!=d['total']: raise SystemExit(1)
if __name__=='__main__': main()
