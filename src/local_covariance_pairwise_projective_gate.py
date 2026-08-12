#!/usr/bin/env python3
"""Audit the local covariance / smoothed pairwise projective identity."""
from __future__ import annotations

import argparse
import json
import numpy as np
from pathlib import Path

SCHEMA_VERSION="0.1.0"


def periodic_gaussian_kernel(X,Y,Z,r):
    K=np.exp(-(X*X+Y*Y+Z*Z)/(2*r*r))
    K/=np.sum(K)
    return K


def seed_field(X,Y,Z):
    # Smooth non-collinear deterministic vorticity-like field; the identity is algebraic.
    w=np.empty((3,)+X.shape)
    w[0]=np.sin(Y)+0.3*np.cos(Z)
    w[1]=np.sin(Z)+0.2*np.cos(X)
    w[2]=np.sin(X)+0.4*np.cos(Y)
    amp=np.exp(-0.08*(X*X+Y*Y+Z*Z))
    return w*amp


def conv_periodic(a,khat):
    return np.fft.ifftn(np.fft.fftn(a)*khat).real


def audit(N=16,L=4.0,r=0.9):
    x=np.linspace(-L,L,N,endpoint=False); h=2*L/N
    X,Y,Z=np.meshgrid(x,x,x,indexing='ij')
    w=seed_field(X,Y,Z)
    eta=periodic_gaussian_kernel(X,Y,Z,r)
    # Shift kernel so index zero is convolution origin for FFT.
    eta=np.fft.ifftshift(eta); kh=np.fft.fftn(eta)
    mag2=np.sum(w*w,axis=0)
    Er=conv_periodic(mag2,kh)
    Nr=np.empty((3,3,N,N,N))
    for i in range(3):
        for j in range(3):
            Nr[i,j]=conv_periodic(w[i]*w[j],kh)
    trN2=np.einsum('ij...,ji...->...',Nr,Nr)
    point_lhs=Er*Er-trN2

    # Integrated covariance side.
    lhs=float(np.sum(point_lhs))

    # Pairwise side using convolution K=eta*eta and identity
    # integral K(x-y)[|w(x)|^2|w(y)|^2-(w(x).w(y))^2].
    # Compute efficiently by convolving each scalar/tensor component with K.
    Khat=kh*kh
    pair_mag=float(np.sum(mag2*conv_periodic(mag2,Khat)))
    pair_dot=0.0
    for i in range(3):
        for j in range(3):
            tij=w[i]*w[j]
            pair_dot+=float(np.sum(tij*conv_periodic(tij,Khat)))
    rhs=pair_mag-pair_dot

    J=np.zeros_like(Er); mask=Er>1e-12
    J[mask]=point_lhs[mask]/(Er[mask]*Er[mask])
    return {
        'N':N,'r':r,
        'integrated_covariance_side':lhs,
        'pairwise_convolution_side':rhs,
        'relative_error':abs(lhs-rhs)/max(abs(lhs),1e-12),
        'min_point_defect':float(np.min(point_lhs)),
        'min_J':float(np.min(J[mask])),
        'max_J':float(np.max(J[mask])),
        'J_upper_margin':float(2/3-np.max(J[mask])),
    }


def exact_axis_cases():
    # Covariance algebra only.
    one=np.diag([1.,0.,0.]); planar=np.diag([.5,.5,0.]); iso=np.eye(3)/3
    def J(C): return float(1-np.trace(C@C))
    return {'one_axis':J(one),'planar':J(planar),'isotropic':J(iso)}


def run_checks():
    a=audit(); ex=exact_axis_cases()
    checks={
        'integrated_pair_identity':a['relative_error']<1e-10,
        'point_defect_nonnegative':a['min_point_defect']>-1e-10,
        'local_J_nonnegative':a['min_J']>-1e-10,
        'local_J_at_most_two_thirds':a['J_upper_margin']>-1e-10,
        'one_axis_zero':abs(ex['one_axis'])<1e-12,
        'planar_half':abs(ex['planar']-.5)<1e-12,
        'isotropic_two_thirds':abs(ex['isotropic']-2/3)<1e-12,
    }
    checks={k:bool(v) for k,v in checks.items()}
    return {
        'schema_version':SCHEMA_VERSION,
        'status':'DERIVED LOCAL COVARIANCE / PAIRWISE PROJECTIVE IDENTITY AUDIT',
        'checks':checks,'passed':sum(checks.values()),'total':len(checks),
        'audit':a,'exact_cases':ex,
        'identity':'Integral E_r(z)^2 J_r(z) dz = double integral (eta_r*eta_r)(x-y)|omega(x) x omega(y)|^2 dxdy.',
        'claim_boundary':'Periodic FFT quadrature checks the covariance/convolution identity only; it does not estimate the singular Biot-Savart stretching kernel.',
    }


def write_md(d,path):
    a=d['audit']; lines=['# Local covariance pairwise-projective audit','',f"Status: **{d['status']}**",'',f"Checks passed: **{d['passed']}/{d['total']}**",'',d['identity'],'',f"Relative identity error: `{a['relative_error']:.3e}`; local J range: `{a['min_J']:.6g}` to `{a['max_J']:.6g}`.",'','## Claim boundary','',d['claim_boundary'],'']; path.write_text('\n'.join(lines),encoding='utf-8')


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args(); out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks(); (out/'local_covariance_pairwise_projective_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8'); write_md(d,out/'local_covariance_pairwise_projective_gate.md')
    print(f"Local covariance pairwise-projective: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=='__main__': main()
