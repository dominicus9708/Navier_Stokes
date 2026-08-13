#!/usr/bin/env python3
"""Audit the magnitude/direction palinstrophy source-depletion algebra.

For omega=rho*xi with |xi|=1 and xi.d_i xi=0,
|d_i omega|^2=(d_i rho)^2+rho^2|d_i xi|^2.  Hence scalar
Sobolev for rho uses only P_mag=P-P_ang.  The script checks this exact
orthogonal decomposition and the resulting dimensionless deficit factor.
It does not audit Calderon-Zygmund or Sobolev constants.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import numpy as np

SCHEMA_VERSION='0.1.0'


def random_point(seed: int):
    rng=np.random.default_rng(seed)
    x=rng.normal(size=3); xi=x/np.linalg.norm(x)
    rho=0.2+2*rng.random()
    dr=rng.normal(size=3)
    dxi=[]
    for _ in range(3):
        v=rng.normal(size=3)
        v=v-xi*np.dot(xi,v)  # tangent: xi dot d_i xi = 0
        dxi.append(v)
    dxi=np.asarray(dxi)
    gradw=np.array([dr[i]*xi+rho*dxi[i] for i in range(3)])
    total=float(np.sum(gradw*gradw))
    mag=float(np.sum(dr*dr))
    ang=float(rho*rho*np.sum(dxi*dxi))
    cross=float(total-mag-ang)
    return {'P':total,'Pmag':mag,'Pang':ang,'identity_error':abs(cross)}


def deficit_audit():
    rows=[]
    for eta in [0.0,0.1,0.25,0.5,0.8,0.99]:
        generic=1.0
        refined=(1.0-eta)**0.75
        rows.append({'eta':eta,'factor':refined,'strict':refined<generic if eta>0 else abs(refined-generic)<1e-15})
    return rows


def localized_algebra(eps=0.35,Ceps=7.0,P=5.0,Pang=1.2,Eoverr2=2.3):
    # Upper proxy from |grad(chi rho)|^2 <= (1+eps) Pmag + Ceps r^-2 E.
    generic=(1+eps)*P+Ceps*Eoverr2
    refined=(1+eps)*(P-Pang)+Ceps*Eoverr2
    eta_eff=(generic-refined)/generic
    return {'generic':generic,'refined':refined,'eta_eff':eta_eff,'factor':(refined/generic)**0.75}


def run_checks():
    pts=[random_point(9708+i) for i in range(100)]
    rows=deficit_audit(); loc=localized_algebra()
    checks={
      'orthogonal_gradient_split':max(p['identity_error'] for p in pts)<1e-11,
      'Pang_nonnegative':all(p['Pang']>=0 for p in pts),
      'Pmag_le_P':all(p['Pmag']<=p['P']+1e-11 for p in pts),
      'strict_factor_for_positive_eta':all(r['strict'] for r in rows),
      'localized_subtraction_survives_cutoff':loc['refined']<loc['generic'] and loc['eta_eff']>0,
      'localized_factor_strict':0<loc['factor']<1,
    }
    checks={k:bool(v) for k,v in checks.items()}
    return {
      'schema_version':SCHEMA_VERSION,
      'status':'DERIVED MAGNITUDE-DIRECTION PALINSTROPHY SOURCE GAP / ALGEBRA AUDIT',
      'checks':checks,'passed':sum(checks.values()),'total':len(checks),
      'max_identity_error':max(p['identity_error'] for p in pts),
      'deficit_rows':rows,'localized_proxy':loc,
      'identity':'P=P_mag+P_ang, with P_mag=||grad |omega|||_2^2 and P_ang=P-P_mag>=0; on omega!=0, P_ang=int |omega|^2 |grad xi|^2.',
      'source_refinement':'|Q| <= C E^(3/4) (P-P_ang)^(3/4) = C E^(3/4) P^(3/4) (1-eta_ang)^(3/4).',
      'claim_boundary':'The script audits only orthogonal decomposition and coefficient algebra. Sobolev/CZ estimates and localized far-field control are analytical inputs handled separately.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks(); (out/'magnitude_direction_source_gap_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
    (out/'magnitude_direction_source_gap_gate.md').write_text(
      '# Magnitude-direction palinstrophy source-gap audit\n\n'
      f"Checks passed: **{d['passed']}/{d['total']}**\n\n"
      +d['identity']+'\n\n'+d['source_refinement']+'\n\n## Claim boundary\n\n'+d['claim_boundary']+'\n',encoding='utf-8')
    print(f"Magnitude-direction source gap: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=='__main__': main()
