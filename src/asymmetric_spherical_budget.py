#!/usr/bin/env python3
"""Computational spherical energy-flux audit for an asymmetric two-seed state.

Fluxes are evaluated through divergence-theorem volume equivalents on a large decay
window using spectral derivatives/Poisson inversion. The cube is a numerical device,
not a physical container. Results are computational checks, not exact sphere theorems.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np


def seed_grid(X,Y,Z,axis,center,amp):
    q=[X-center[0],Y-center[1],Z-center[2]]
    r2=sum(v*v for v in q); g=np.exp(-r2)
    u=np.empty((3,)+X.shape,dtype=float)
    for j in range(3):
        if j==axis:
            transverse=sum(q[k]**2 for k in range(3) if k!=axis)
            u[j]=4*amp*(1-transverse)*g
        else:
            u[j]=4*amp*q[j]*q[axis]*g
    return u


def audit(N=64,L=6.0,radii=(0.75,1.0,1.25,1.5,2.0),nu=1.0):
    x=np.linspace(-L,L,N,endpoint=False); h=2*L/N
    X,Y,Z=np.meshgrid(x,x,x,indexing='ij')
    u=(seed_grid(X,Y,Z,2,(0,0,0),1.0)+
       seed_grid(X,Y,Z,0,(-1,0,0),1.0))
    k=2*np.pi*np.fft.fftfreq(N,d=h); K=np.meshgrid(k,k,k,indexing='ij')
    k2=K[0]**2+K[1]**2+K[2]**2
    grads=np.empty((3,3,N,N,N)); uh=[]
    for i in range(3):
        U=np.fft.fftn(u[i]); uh.append(U)
        for j in range(3): grads[i,j]=np.fft.ifftn(1j*K[j]*U).real
    adv=np.einsum('j...,ij...->i...',u,grads)
    Q=np.einsum('ij...,ji...->...',grads,grads)
    qh=np.fft.fftn(Q); ph=np.zeros_like(qh); nz=k2>0; ph[nz]=qh[nz]/k2[nz]
    gradp=np.array([np.fft.ifftn(1j*K[j]*ph).real for j in range(3)])
    e=.5*np.sum(u*u,axis=0); eh=np.fft.fftn(e); lape=np.fft.ifftn(-k2*eh).real
    lapu=np.array([np.fft.ifftn(-k2*uh[i]).real for i in range(3)])
    grad2=np.sum(grads*grads,axis=(0,1))
    dt_e=np.sum(u*(-adv-gradp+nu*lapu),axis=0)
    adv_density=np.sum(u*adv,axis=0)
    pressure_density=np.sum(u*gradp,axis=0)
    R2=X*X+Y*Y+Z*Z; dv=h**3
    rows=[]
    for r in radii:
        m=R2<r*r
        Fadv=float(np.sum(adv_density[m])*dv)
        Fp=float(np.sum(pressure_density[m])*dv)
        Fvis=float(-nu*np.sum(lape[m])*dv)
        D=float(nu*np.sum(grad2[m])*dv)
        dE=float(np.sum(dt_e[m])*dv)
        residual=dE+Fadv+Fp+Fvis+D
        rows.append({'r':r,'F_adv':Fadv,'F_pressure':Fp,'F_viscous':Fvis,
                     'D_inside':D,'dE_ball_dt':dE,'budget_residual':float(residual)})
    return {'N':N,'L':L,'h':h,'rows':rows}


def run_checks():
    a64=audit(64); a80=audit(80)
    by64={r['r']:r for r in a64['rows']}; by80={r['r']:r for r in a80['rows']}
    checks={
        'budget_residual_64':max(abs(r['budget_residual']) for r in a64['rows'])<1e-9,
        'budget_residual_80':max(abs(r['budget_residual']) for r in a80['rows'])<1e-9,
        'advective_flux_inward_at_r1_both':by64[1.0]['F_adv']<0 and by80[1.0]['F_adv']<0,
        'pressure_flux_outward_at_r1_both':by64[1.0]['F_pressure']>0 and by80[1.0]['F_pressure']>0,
        'pressure_flux_sign_changes_with_radius_64':by64[0.75]['F_pressure']<0 and by64[1.25]['F_pressure']>0 and by64[2.0]['F_pressure']<0,
        'pressure_flux_sign_changes_with_radius_80':by80[0.75]['F_pressure']<0 and by80[1.25]['F_pressure']>0 and by80[2.0]['F_pressure']<0,
        'viscous_flux_outward_sampled':all(r['F_viscous']>0 for r in a64['rows']+a80['rows']),
    }
    return {
        'status':'COMPUTATIONAL CHECK / ASYMMETRIC SPHERICAL ENERGY BUDGET',
        'checks':checks,'passed':sum(checks.values()),'total':len(checks),
        'resolution_64':a64,'resolution_80':a80,
        'interpretation':(
            'In the asymmetric two-seed state the signed advective and pressure fluxes are nonzero. '
            'Pressure transport changes sign across sampled radii, and at r=1 advection transports '
            'energy inward while pressure transports it outward. Radial redistribution is therefore '
            'not a one-way outward cascade in general.'
        ),
        'route_status':'Any proof shortcut assuming nonnegative outward advective/pressure flux on all centered spheres is a FAILED-ROUTE CANDIDATE.',
        'numerical_boundary':'Sphere fluxes are computed via volume divergence equivalents on Cartesian masks; sign persistence is checked at N=64 and N=80 but is not an interval-certified theorem.'
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks(); (out/'asymmetric_spherical_budget.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
    print(f"Asymmetric spherical budget: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=='__main__': main()
