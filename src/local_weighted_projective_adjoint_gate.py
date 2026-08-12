#!/usr/bin/env python3
"""Audit the local weighted projective covariance/window algebra."""
from __future__ import annotations

import argparse, json
from pathlib import Path
import numpy as np

SCHEMA_VERSION='0.1.0'


def audit(seed=9708,n=500,nu=.77,Lambda=.6):
    rng=np.random.default_rng(seed)
    phi=rng.random(n)+.1
    # Signed observation defect satisfying |Psi| <= Lambda phi.
    psi=Lambda*phi*rng.uniform(-1,1,size=n)
    omega=rng.normal(size=(n,3))
    raw=rng.normal(size=(n,3,3)); S=.5*(raw+np.swapaxes(raw,1,2)); tr=np.trace(S,axis1=1,axis2=2)/3; S-=tr[:,None,None]*np.eye(3)[None,:,:]
    grad=rng.normal(size=(n,3,3))

    mag2=np.sum(omega*omega,axis=1)
    E=float(np.sum(phi*mag2)); N=np.einsum('n,ni,nj->ij',phi,omega,omega); C=N/E; J=float(1-np.trace(C@C)); D=E*J
    Somega=np.einsum('nij,nj->ni',S,omega)
    A=np.einsum('n,ni,nj->ij',phi,Somega,omega); Q=float(np.trace(A)); B=A/E; q=Q/E
    H=np.zeros((3,3))
    for m in range(3):
        gm=grad[:,:,m]; H+=np.einsum('n,ni,nj->ij',phi,gm,gm)
    P=float(np.trace(H)); C1=H/P; J1=float(1-np.trace(C1@C1)); Delta2=float(np.linalg.norm(C1-C)**2)
    R=np.einsum('n,ni,nj->ij',psi,omega,omega); R0=float(np.trace(R))

    Ndot=A+A.T-2*nu*H+R; Edot=float(np.trace(Ndot)); Cdot=Ndot/E-(Edot/E)*C; Jdot=float(-2*np.trace(C@Cdot)); Ddot_direct=Edot*J+E*Jdot
    M=float(q*(1-J)-np.trace(C@B)); W=float(R0*(2-J)-2*np.trace(C@R))
    Ddot_formula=float(2*Q*J+4*E*M+W-2*nu*P*(J1+Delta2))

    F=float(np.sqrt(np.sum(phi*np.sum(Somega*Somega,axis=1))))
    nonlin=float(2*Q*J+4*E*M); nonlin_bound=2*np.sqrt(5)*np.sqrt(max(D,0))*F
    window_bound=Lambda*D
    coercive=3/8*J*J

    # Verify the coefficient identity behind |W|<=Lambda D.
    vals,vecs=np.linalg.eigh(C)
    betas=[]; coeff=[]
    for i in range(3):
        e=vecs[:,i]; betas.append(float(e@R@e/E)); coeff.append(float(2-J-2*vals[i]))
    coeff_mass=float(np.dot(vals,coeff))

    return {
      'E':E,'J':J,'D':D,'P':P,'J1':J1,'Delta2':Delta2,
      'Ddot_direct':Ddot_direct,'Ddot_formula':Ddot_formula,'Ddot_error':abs(Ddot_direct-Ddot_formula),
      'nonlinear_source':nonlin,'nonlinear_bound':nonlin_bound,'nonlinear_margin':nonlin_bound-nonlin,
      'W':W,'window_bound':window_bound,'window_margin':window_bound-abs(W),
      'coeff_min':min(coeff),'coeff_mass':coeff_mass,'coeff_mass_error':abs(coeff_mass-J),
      'coercive_margin':J1+Delta2-coercive,
      'max_relative_psi':float(np.max(np.abs(psi)/phi)),
    }


def adjoint_case(seed=13,n=200):
    rng=np.random.default_rng(seed); phi=rng.random(n)+.1; omega=rng.normal(size=(n,3)); psi=np.zeros(n)
    E=float(np.sum(phi*np.sum(omega*omega,axis=1))); N=np.einsum('n,ni,nj->ij',phi,omega,omega); C=N/E; J=float(1-np.trace(C@C)); R=np.einsum('n,ni,nj->ij',psi,omega,omega); R0=float(np.trace(R)); W=float(R0*(2-J)-2*np.trace(C@R))
    return {'W':W,'R_norm':float(np.linalg.norm(R))}


def run_checks():
    a=audit(); z=adjoint_case()
    checks={
      'weighted_projective_identity':a['Ddot_error']<1e-9,
      'weighted_nonlinear_source_bound':a['nonlinear_margin']>-1e-9,
      'relative_window_hypothesis':a['max_relative_psi']<=.6+1e-12,
      'window_bound':a['window_margin']>-1e-9,
      'window_coefficients_nonnegative':a['coeff_min']>-1e-12,
      'window_coefficient_mass_equals_J':a['coeff_mass_error']<1e-12,
      'local_covariance_coercivity':a['coercive_margin']>-1e-12,
      'adjoint_window_error_zero':abs(z['W'])<1e-12 and z['R_norm']<1e-12,
    }
    checks={k:bool(v) for k,v in checks.items()}
    return {'schema_version':SCHEMA_VERSION,'status':'DERIVED LOCAL WEIGHTED PROJECTIVE / ADJOINT-WINDOW ALGEBRA AUDIT','checks':checks,'passed':sum(checks.values()),'total':len(checks),'audit':a,'adjoint':z,'identity':'Ddot_phi + 2 nu P_phi(J1_phi+Delta_phi^2) = nonlinear_projective_source + W_phi.','window_bound':'If |Psi_phi|<=Lambda phi, then |W_phi|<=Lambda D_phi; if Psi_phi=0, W_phi=0.','claim_boundary':'Synthetic weighted tensors audit the normalized covariance/window algebra. The PDE integration-by-parts and adjoint equation are documented analytically.'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args(); out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True); d=run_checks(); (out/'local_weighted_projective_adjoint_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8'); (out/'local_weighted_projective_adjoint_gate.md').write_text(f"# Local weighted projective adjoint audit\n\nChecks passed: **{d['passed']}/{d['total']}**\n\n{d['identity']}\n\n{d['window_bound']}\n",encoding='utf-8'); print(f"Local weighted projective adjoint: {d['passed']}/{d['total']} checks passed");
    if d['passed']!=d['total']: raise SystemExit(1)
if __name__=='__main__': main()
