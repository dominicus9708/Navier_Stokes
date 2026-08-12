#!/usr/bin/env python3
"""Audit the pairwise projective vorticity balance algebra.

The samples are synthetic vectors/tensors. They verify the integrated algebra,
not a numerical Navier--Stokes solution.
"""
from __future__ import annotations

import argparse, json
from pathlib import Path
import numpy as np

SCHEMA_VERSION='0.1.0'


def audit(seed=9708,npts=96,nu=0.83):
    rng=np.random.default_rng(seed)
    wgt=rng.random(npts)+0.1
    omega=rng.normal(size=(npts,3))
    raw=rng.normal(size=(npts,3,3))
    S=0.5*(raw+np.swapaxes(raw,1,2))
    tr=np.trace(S,axis1=1,axis2=2)/3
    S-=tr[:,None,None]*np.eye(3)[None,:,:]
    grad=rng.normal(size=(npts,3,3)) # point, vector-component, derivative-direction

    E=float(np.sum(wgt*np.sum(omega*omega,axis=1)))
    N=np.einsum('n,ni,nj->ij',wgt,omega,omega)
    C=N/E
    J=float(1-np.trace(C@C)); K=E*E*J

    Somega=np.einsum('nij,nj->ni',S,omega)
    A=np.einsum('n,ni,nj->ij',wgt,Somega,omega)
    Q=float(np.trace(A))

    H=np.zeros((3,3))
    for m in range(3):
        gm=grad[:,:,m]
        H+=np.einsum('n,ni,nj->ij',wgt,gm,gm)
    P=float(np.trace(H))

    # Pairwise cross-product tensor.
    a=omega[:,None,:]
    b=omega[None,:,:]
    cross=np.cross(a,b)
    ww=wgt[:,None]*wgt[None,:]
    Kpair=float(np.sum(ww*np.sum(cross*cross,axis=2)))

    c=Somega[:,None,:]
    d=Somega[None,:,:]
    term=np.cross(c,b)+np.cross(a,d)
    nonlinear_pair=float(2*np.sum(ww*np.sum(cross*term,axis=2)))
    nonlinear_cov=float(4*(E*Q-np.trace(N@A)))

    R=0.0
    for m in range(3):
        ga=grad[:,:,m][:,None,:]
        R+=float(np.sum(ww*np.sum(np.cross(ga,b)**2,axis=2)))
    visc_pair=float(-4*nu*R)
    visc_cov=float(4*nu*(np.trace(N@H)-E*P))

    C1=H/P
    Pi=float(1-np.max(np.linalg.eigvalsh(C)))
    Rcov=float(E*P*(1-np.trace(C@C1)))
    coercive_floor=float(0.5*E*P*J)

    source_bound=float(4*np.sqrt(max(K*E,0))*np.sqrt(np.sum(wgt*np.sum(Somega*Somega,axis=1))))

    return {
      'E':E,'J':J,'K':K,'K_pair':Kpair,'K_error':abs(K-Kpair),
      'nonlinear_pair':nonlinear_pair,'nonlinear_covariance':nonlinear_cov,'nonlinear_error':abs(nonlinear_pair-nonlinear_cov),
      'R_pair':R,'R_covariance':Rcov,'R_error':abs(R-Rcov),
      'viscous_pair':visc_pair,'viscous_covariance':visc_cov,'viscous_error':abs(visc_pair-visc_cov),
      'Pi':Pi,'coercive_floor':coercive_floor,'coercive_margin':R-coercive_floor,
      'nonlinear_source_bound':source_bound,'nonlinear_bound_margin':source_bound-abs(nonlinear_pair),
    }


def one_axis_case(seed=17,npts=80):
    rng=np.random.default_rng(seed); wgt=rng.random(npts)+.1; f=rng.normal(size=npts); omega=np.zeros((npts,3)); omega[:,2]=f
    E=float(np.sum(wgt*f*f)); N=np.einsum('n,ni,nj->ij',wgt,omega,omega); J=float(1-np.trace((N/E)@(N/E)))
    a=omega[:,None,:]; b=omega[None,:,:]; K=float(np.sum((wgt[:,None]*wgt[None,:])*np.sum(np.cross(a,b)**2,axis=2)))
    return {'J':J,'K':K}


def run_checks():
    a=audit(); one=one_axis_case()
    checks={
      'pairwise_K_identity':a['K_error']<1e-10,
      'nonlinear_pair_covariance_identity':a['nonlinear_error']<1e-9,
      'viscous_pair_covariance_identity':a['viscous_error']<1e-9,
      'pair_dissipation_covariance_identity':a['R_error']<1e-9,
      'pair_dissipation_projective_coercivity':a['coercive_margin']>-1e-10,
      'nonlinear_pair_source_bound':a['nonlinear_bound_margin']>-1e-10,
      'one_axis_pair_content_zero':abs(one['J'])<1e-12 and abs(one['K'])<1e-12,
    }
    checks={k:bool(v) for k,v in checks.items()}
    return {'schema_version':SCHEMA_VERSION,'status':'DERIVED PAIRWISE PROJECTIVE BALANCE / ALGEBRA AUDIT','checks':checks,'passed':sum(checks.values()),'total':len(checks),'audit':a,'one_axis':one,'identity':'K=double integral |omega(x) x omega(y)|^2; stretching and viscosity preserve explicit pairwise cross-axis factors.','claim_boundary':'Synthetic finite sums verify integrated vector/matrix identities only. They do not close the singular Biot-Savart stretching kernel.'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args(); out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True); d=run_checks(); (out/'pairwise_projective_balance_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8'); (out/'pairwise_projective_balance_gate.md').write_text(f"# Pairwise projective balance audit\n\nChecks passed: **{d['passed']}/{d['total']}**\n\n{d['identity']}\n",encoding='utf-8'); print(f"Pairwise projective balance: {d['passed']}/{d['total']} checks passed");
    if d['passed']!=d['total']: raise SystemExit(1)
if __name__=='__main__': main()
