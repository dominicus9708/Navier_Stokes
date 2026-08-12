#!/usr/bin/env python3
"""Audit the exact variable-axis Helmholtz commutator decomposition.

The Calderon commutator L2 bound is analytic/external. This script checks only
that the operator decomposition is implemented consistently on periodic smooth fields.
"""
from __future__ import annotations

import argparse, json
from pathlib import Path
import numpy as np

SCHEMA_VERSION='0.1.0'


def project_divfree(u,K,k2):
    uh=np.array([np.fft.fftn(u[i]) for i in range(3)])
    dot=sum(K[i]*uh[i] for i in range(3))
    nz=k2>0
    for i in range(3):
        corr=np.zeros_like(dot)
        corr[nz]=K[i][nz]*dot[nz]/k2[nz]
        uh[i]-=corr
    return np.array([np.fft.ifftn(uh[i]).real for i in range(3)])


def Qproj(f,K,k2):
    fh=np.array([np.fft.fftn(f[i]) for i in range(3)])
    dot=sum(K[i]*fh[i] for i in range(3))
    out=np.zeros_like(fh)
    nz=k2>0
    for i in range(3):
        out[i][nz]=K[i][nz]*dot[nz]/k2[nz]
    return np.array([np.fft.ifftn(out[i]).real for i in range(3)])


def curl(u,K):
    uh=[np.fft.fftn(u[i]) for i in range(3)]
    wx=np.fft.ifftn(1j*(K[1]*uh[2]-K[2]*uh[1])).real
    wy=np.fft.ifftn(1j*(K[2]*uh[0]-K[0]*uh[2])).real
    wz=np.fft.ifftn(1j*(K[0]*uh[1]-K[1]*uh[0])).real
    return np.array([wx,wy,wz])


def strain(u,K):
    grads=np.empty((3,3)+u.shape[1:])
    for i in range(3):
        uh=np.fft.fftn(u[i])
        for j in range(3):
            grads[i,j]=np.fft.ifftn(1j*K[j]*uh).real
    return .5*(grads+np.swapaxes(grads,0,1))


def cross(a,b):
    # vector fields with vector index first
    return np.array([
        a[1]*b[2]-a[2]*b[1],
        a[2]*b[0]-a[0]*b[2],
        a[0]*b[1]-a[1]*b[0],
    ])


def norm2(f,dv):
    return float(np.sqrt(np.sum(f*f)*dv))


def audit(N=28,L=2*np.pi):
    x=np.linspace(0,L,N,endpoint=False); h=L/N
    X,Y,Z=np.meshgrid(x,x,x,indexing='ij'); dv=h**3
    k=2*np.pi*np.fft.fftfreq(N,d=h); K=np.meshgrid(k,k,k,indexing='ij'); k2=K[0]**2+K[1]**2+K[2]**2

    u0=np.array([
        np.sin(Y)+.25*np.cos(2*Z)+.17*np.sin(X+Z),
        np.sin(Z)+.31*np.cos(2*X)+.13*np.cos(X+Y),
        np.sin(X)+.29*np.cos(2*Y)+.11*np.sin(Y+Z),
    ])
    u=project_divfree(u0,K,k2)
    omega=curl(u,K); S=strain(u,K)

    nraw=np.array([
        1.0+.16*np.sin(Y)+.05*np.cos(Z),
        .22*np.sin(Z+.3)+.04*np.cos(X),
        .18*np.cos(X-.2)+.03*np.sin(Y),
    ])
    nmag=np.sqrt(np.sum(nraw*nraw,axis=0)); n=nraw/nmag

    Sn=np.einsum('ij...,j...->i...',S,n)
    nxw=cross(n,omega)
    Tnxw=Qproj(nxw,K,k2)-.5*nxw

    comm=np.zeros_like(Sn)
    basis=np.eye(3)
    for a in range(3):
        ea=np.zeros_like(n); ea[a]=1.0
        f=cross(ea,omega)
        Qf=Qproj(f,K,k2)
        comm += n[a]*Qf - Qproj(n[a]*f,K,k2)

    rhs=Tnxw+comm
    err=norm2(Sn-rhs,dv)
    rel=err/max(norm2(Sn,dv),1e-14)

    # Constant-axis isometry control on the same field.
    nc=np.array([.3,-.4,.8660254037844386]); nc/=np.linalg.norm(nc)
    ncf=np.zeros_like(n); ncf[0]=nc[0]; ncf[1]=nc[1]; ncf[2]=nc[2]
    Snc=np.einsum('ij...,j...->i...',S,ncf)
    fc=cross(ncf,omega)
    iso=abs(norm2(Snc,dv)-.5*norm2(fc,dv))

    # Record, but do not theorem-gate, the sample commutator/Lipschitz ratio.
    grads_n=[]
    for i in range(3):
        nh=np.fft.fftn(n[i])
        for j in range(3):
            grads_n.append(np.fft.ifftn(1j*K[j]*nh).real)
    lip=float(np.max(np.sqrt(sum(g*g for g in grads_n))))
    ratio=norm2(comm,dv)/max(lip*norm2(u,dv),1e-14)

    return {
        'N':N,
        'relative_decomposition_error':rel,
        'absolute_decomposition_error':err,
        'constant_axis_isometry_error':iso,
        'commutator_norm':norm2(comm,dv),
        'axis_lipschitz_sample':lip,
        'velocity_L2':norm2(u,dv),
        'sample_commutator_ratio':ratio,
    }


def run_checks():
    a=audit()
    checks={
        'variable_axis_operator_decomposition':a['relative_decomposition_error']<2e-10,
        'constant_axis_half_isometry':a['constant_axis_isometry_error']<2e-10,
        'sample_commutator_ratio_finite':np.isfinite(a['sample_commutator_ratio']),
    }
    checks={k:bool(v) for k,v in checks.items()}
    return {
        'schema_version':SCHEMA_VERSION,
        'status':'DERIVED VARIABLE-AXIS HELMHOLTZ COMMUTATOR / SPECTRAL AUDIT',
        'checks':checks,'passed':sum(checks.values()),'total':len(checks),
        'audit':a,
        'identity':'S n = (Q-1/2 I)(n x omega) + sum_a [n_a,Q](e_a x omega).',
        'claim_boundary':'The FFT audit checks the exact decomposition. The Lipschitz L2 commutator estimate is an analytic Calderon-commutator input and is not inferred from the sample ratio.',
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args(); out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks(); (out/'variable_axis_strain_commutator_gate.json').write_text(json.dumps(d,indent=2),encoding='utf-8'); (out/'variable_axis_strain_commutator_gate.md').write_text(f"# Variable-axis strain commutator audit\n\nChecks passed: **{d['passed']}/{d['total']}**\n\n{d['identity']}\n",encoding='utf-8'); print(f"Variable-axis strain commutator: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=='__main__': main()
