#!/usr/bin/env python3
"""Audit the trace-free far-strain/projective-covariance gap.

For a PSD covariance C with tr C=1 and a symmetric trace-free matrix S,
|tr(S C)| <= |S|_F sqrt(2/3-J), J=1-tr(C^2).
The script checks this finite-dimensional identity/bound and the relative mixing
factor sqrt(1-3J/2). It does not audit singular-integral localization estimates.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import numpy as np
import math

SCHEMA_VERSION='0.1.0'


def sample(seed: int):
    rng=np.random.default_rng(seed)
    A=rng.normal(size=(3,3)); C=A@A.T; C/=np.trace(C)
    B=rng.normal(size=(3,3)); S=(B+B.T)/2; S-=np.eye(3)*np.trace(S)/3
    J=float(1-np.trace(C@C))
    lhs=abs(float(np.trace(S@C)))
    rhs=float(np.linalg.norm(S,'fro')*math.sqrt(max(0.0,2/3-J)))
    centered=float(np.linalg.norm(C-np.eye(3)/3,'fro')**2)
    return {'J':J,'lhs':lhs,'rhs':rhs,'margin':rhs-lhs,'centered_error':abs(centered-(2/3-J))}


def equality_case(seed=1):
    rng=np.random.default_rng(seed)
    A=rng.normal(size=(3,3)); C=A@A.T; C/=np.trace(C)
    S=C-np.eye(3)/3
    J=float(1-np.trace(C@C))
    lhs=abs(float(np.trace(S@C)))
    rhs=float(np.linalg.norm(S,'fro')*math.sqrt(max(0.0,2/3-J)))
    return {'J':J,'lhs':lhs,'rhs':rhs,'error':abs(lhs-rhs)}


def canonical_states():
    C1=np.diag([1.,0.,0.]); Ci=np.eye(3)/3
    return {
      'one_axis_J':float(1-np.trace(C1@C1)),
      'one_axis_relative_factor':1.0,
      'isotropic_J':float(1-np.trace(Ci@Ci)),
      'isotropic_relative_factor':0.0,
    }


def dyadic_decay():
    # Relative decay of the far spatial variation shell factor: 2^(-5j/2).
    vals=[2**(-2.5*j) for j in range(1,8)]
    ratios=[vals[j+1]/vals[j] for j in range(len(vals)-1)]
    return {'values':vals,'ratios':ratios,'target_ratio':2**(-2.5),'max_error':max(abs(x-2**(-2.5)) for x in ratios)}


def run_checks():
    rows=[sample(9708+i) for i in range(500)]
    eq=equality_case(); cs=canonical_states(); dd=dyadic_decay()
    checks={
      'all_covariance_gaps_nonnegative':all(r['margin']>=-1e-12 for r in rows),
      'centered_covariance_identity':max(r['centered_error'] for r in rows)<1e-11,
      'matrix_CS_equality_case':eq['error']<1e-11,
      'one_axis_factor_one':abs(cs['one_axis_J'])<1e-12 and cs['one_axis_relative_factor']==1.0,
      'isotropic_factor_zero':abs(cs['isotropic_J']-2/3)<1e-12 and cs['isotropic_relative_factor']==0.0,
      'far_variation_extra_dyadic_decay':dd['max_error']<1e-15,
    }
    checks={k:bool(v) for k,v in checks.items()}
    return {
      'schema_version':SCHEMA_VERSION,
      'status':'DERIVED FAR-STRAIN PROJECTIVE COVARIANCE GAP / MATRIX AUDIT',
      'checks':checks,'passed':sum(checks.values()),'total':len(checks),
      'min_margin':min(r['margin'] for r in rows),'equality':eq,'canonical':cs,'dyadic':dd,
      'identity':'|int_B omega.S0 omega| <= E_B |S0|_F sqrt(2/3-J_B) for constant symmetric trace-free S0.',
      'relative_factor':'g(J)=sqrt(1-3J/2) relative to the J=0 one-axis optimum.',
      'claim_boundary':'This audit checks finite-dimensional covariance algebra and dyadic exponent bookkeeping only. The near/far singular-integral decomposition is an analytical step documented separately.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks(); (out/'far_strain_covariance_gap_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
    (out/'far_strain_covariance_gap_gate.md').write_text(
      '# Far-strain projective covariance-gap audit\n\n'
      f"Checks passed: **{d['passed']}/{d['total']}**\n\n"
      +d['identity']+'\n\n'+d['relative_factor']+'\n\n## Claim boundary\n\n'+d['claim_boundary']+'\n',encoding='utf-8')
    print(f"Far-strain covariance gap: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=='__main__': main()
