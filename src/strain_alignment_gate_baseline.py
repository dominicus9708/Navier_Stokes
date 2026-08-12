#!/usr/bin/env python3
"""General strain/alignment upper gate plus deterministic two-seed benchmark samples."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np
import sympy as sp


def abstract_identity():
    l1,l2,l3,a1,a2=sp.symbols('l1 l2 l3 a1 a2', real=True)
    a3=1-a1-a2
    gamma=l1*a1+l2*a2+l3*a3
    U=l2+(l3-l2)*a3
    return bool(sp.simplify(U-gamma-(l2-l1)*a1)==0)


def seed_S_omega(point,axis,center,amp):
    y=np.array(point,dtype=float)-np.array(center,dtype=float)
    r2=float(np.dot(y,y)); g=math.exp(-r2)
    G=np.zeros((3,3),dtype=float)
    rp2=sum(y[m]**2 for m in range(3) if m!=axis)
    for j in range(3):
        for k in range(3):
            if j!=axis:
                G[j,k]=4*amp*g*((1.0 if j==k else 0.0)*y[axis]+y[j]*(1.0 if axis==k else 0.0)-2*y[j]*y[axis]*y[k])
            elif k==axis:
                G[j,k]=-8*amp*g*y[k]*(1-rp2)
            else:
                G[j,k]=-8*amp*g*y[k]*(2-rp2)
    S=.5*(G+G.T)
    ea=np.zeros(3); ea[axis]=1.0
    omega=4*amp*(2*r2-5)*g*np.cross(y,ea)
    return S,omega


def gate_at(point):
    S1,w1=seed_S_omega(point,2,(0,0,0),1.0)
    S2,w2=seed_S_omega(point,0,(1,0,0),0.5)
    S=S1+S2; w=w1+w2
    wm=float(np.linalg.norm(w))
    vals,vecs=np.linalg.eigh(S)
    xi=w/wm
    a=np.array([(float(np.dot(xi,vecs[:,i])))**2 for i in range(3)])
    gamma=float(xi@S@xi)
    U=float(vals[1]+(vals[2]-vals[1])*a[2])
    Uplus=max(U,0.0)
    row={
        'point':list(point),'lambda':[float(v) for v in vals],
        'alignment':[float(v) for v in a],'gamma':gamma,'U':U,'U_plus':Uplus,
        'gate_residual':U-gamma,
    }
    if vals[1]<0:
        theta=float(-vals[1]/(vals[2]-vals[1]))
        row['theta']=theta; row['a3_minus_theta']=float(a[2]-theta)
        row['negative_middle_gate_reconstruction']=float((vals[2]-vals[1])*max(a[2]-theta,0.0))
    return row


def run_checks():
    # Sample A: middle eigenvalue positive, strong max-axis alignment.
    A=gate_at((0.25,0.5,0.0))
    # Sample B: middle eigenvalue negative but max-axis alignment exceeds threshold.
    B=gate_at((0.125,0.125,0.125))
    checks={
        'abstract_gate_identity':abstract_identity(),
        'gate_bounds_sample_A':A['gamma']<=A['U_plus']+1e-12,
        'sample_A_middle_positive':A['lambda'][1]>0,
        'sample_A_strong_max_alignment':A['alignment'][2]>0.9,
        'gate_bounds_sample_B':B['gamma']<=B['U_plus']+1e-12,
        'sample_B_middle_negative':B['lambda'][1]<0,
        'sample_B_positive_stretch':B['gamma']>0,
        'sample_B_exceeds_alignment_threshold':B['a3_minus_theta']>0,
        'sample_B_threshold_reconstruction':abs(B['U_plus']-B['negative_middle_gate_reconstruction'])<1e-12,
    }
    return {
        'status':'DERIVED BOUND + COMPUTATIONAL CHECK / STRAIN-ALIGNMENT GATE',
        'checks':checks,'passed':sum(bool(v) for v in checks.values()),'total':len(checks),
        'general_bound':'gamma_+ <= [lambda_2 + (lambda_3-lambda_2)*a_3]_+',
        'negative_middle_threshold':'if lambda_2<0, positive stretching requires a_3 > -lambda_2/(lambda_3-lambda_2)',
        'sample_middle_positive':A,'sample_middle_negative_but_stretching_positive':B,
        'proof_boundary':'The gate is exact linear algebra; no a-priori control of its scale-local integral is proved.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks(); (out/'strain_alignment_gate_baseline.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
    print(f"Strain alignment gate: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=='__main__': main()
