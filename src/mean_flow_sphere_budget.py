#!/usr/bin/env python3
"""Instantaneous critical oscillation budget on rigid mean-flow spheres.

For each radius ell, subtract the actual ball-average velocity Ubar_ell from the
asymmetric two-Gaussian benchmark.  The resulting v has zero mean in the ball.
We audit the dimensionless contributions to ell^2/2 * d C_sph/dt.

The Cartesian FFT box is only a numerical device for derivatives/pressure.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np


def seed_grid(X,Y,Z,axis,center,amp=1.0):
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
    u=(seed_grid(X,Y,Z,2,(0,0,0),1.0)+seed_grid(X,Y,Z,0,(-1,0,0),1.0))

    k=2*np.pi*np.fft.fftfreq(N,d=h); K=np.meshgrid(k,k,k,indexing='ij')
    k2=K[0]**2+K[1]**2+K[2]**2
    grads=np.empty((3,3,N,N,N)); uh=[]
    for i in range(3):
        U=np.fft.fftn(u[i]); uh.append(U)
        for j in range(3): grads[i,j]=np.fft.ifftn(1j*K[j]*U).real
    divu=np.trace(grads,axis1=0,axis2=1)
    Q=np.einsum('ij...,ji...->...',grads,grads)
    qh=np.fft.fftn(Q); ph=np.zeros_like(qh); nz=k2>0; ph[nz]=qh[nz]/k2[nz]
    gradp=np.array([np.fft.ifftn(1j*K[j]*ph).real for j in range(3)])
    lapu=np.array([np.fft.ifftn(-k2*uh[i]).real for i in range(3)])
    grad2=np.sum(grads*grads,axis=(0,1))

    R2=X*X+Y*Y+Z*Z; dv=h**3
    rows=[]
    for ell in radii:
        m=R2<ell*ell
        vol=float(np.sum(m)*dv)
        Ubar=np.array([float(np.sum(u[i][m])*dv/vol) for i in range(3)])
        v=u-Ubar[:,None,None,None]
        mean_v=np.array([float(np.sum(v[i][m])*dv/vol) for i in range(3)])

        # v dot (v dot grad)u
        adv_v=np.einsum('j...,ij...->i...',v,grads)
        adv_density=np.sum(v*adv_v,axis=0)
        p_density=np.sum(v*gradp,axis=0)
        visc_density=np.sum(v*lapu,axis=0)

        int_v2=float(np.sum(np.sum(v*v,axis=0)[m])*dv)
        int_v3=float(np.sum(np.sum(v*v,axis=0)[m]**1.5)*dv)
        C=int_v2/ell
        E=ell*float(np.sum(grad2[m])*dv)
        A=ell*float(np.sum(adv_density[m])*dv)
        P=ell*float(np.sum(p_density[m])*dv)
        V=nu*ell*float(np.sum(visc_density[m])*dv)
        rate=-2.0*(A+P-V)  # ell^2 * d C/dt
        interp=(C*E)**0.75 if C>0 and E>0 else 0.0

        rows.append({
            'ell':ell,'volume_grid':vol,'Ubar':Ubar.tolist(),
            'mean_v_norm':float(np.linalg.norm(mean_v)),
            'C_sph':C,'E_sph':E,'I3':int_v3,
            'I3_over_CE_3_4':float(int_v3/interp) if interp>0 else None,
            'A_adv':A,'P_pressure':P,'V_viscous_volume':V,
            'ell2_dCdt':rate,
        })

    return {
        'N':N,'L':L,'h':h,
        'max_divergence_grid':float(np.max(np.abs(divu))),
        'rows':rows,
    }


def run_checks():
    a48=audit(48); a64=audit(64)
    r48={q['ell']:q for q in a48['rows']}; r64={q['ell']:q for q in a64['rows']}
    checks={
        'mean_zero_48':max(q['mean_v_norm'] for q in a48['rows'])<1e-12,
        'mean_zero_64':max(q['mean_v_norm'] for q in a64['rows'])<1e-12,
        'positive_C_and_E':all(q['C_sph']>0 and q['E_sph']>0 for q in a48['rows']+a64['rows']),
        'finite_interpolation_ratio':all(np.isfinite(q['I3_over_CE_3_4']) for q in a48['rows']+a64['rows']),
        'nonzero_advective_channel_asymmetric':abs(r64[1.0]['A_adv'])>1e-4,
        'nonzero_pressure_channel_asymmetric':abs(r64[1.0]['P_pressure'])>1e-4,
        'rate_resolution_consistency_r1':abs(r48[1.0]['ell2_dCdt']-r64[1.0]['ell2_dCdt'])/max(1.0,abs(r64[1.0]['ell2_dCdt']))<0.08,
    }
    return {
        'status':'COMPUTATIONAL CHECK / MEAN-FLOW SPHERE OSCILLATION BUDGET',
        'identity':'For v=u-Ubar_ell in the sphere-mean translating frame: (ell^2/2) d_t C_sph = -A_adv - P_pressure + V_viscous, where A=ell int v.(v.grad)u, P=ell int v.grad p, V=nu ell int v.Delta u. The uniform frame-acceleration term vanishes because int_B v=0.',
        'checks':checks,'passed':sum(checks.values()),'total':len(checks),
        'resolution_48':a48,'resolution_64':a64,
        'interpretation':'Removing the ball mean eliminates coherent translation but does not eliminate nonlinear crossing or pressure redistribution. These become signed critical channels in the oscillation budget; viscosity supplies the third signed contribution.',
        'claim_boundary':'FFT pressure/derivative evaluation and Cartesian ball masks are deterministic numerical audits. No sign theorem or a-priori regularity bound is claimed.'
    }


def write_md(d,path):
    by={q['ell']:q for q in d['resolution_64']['rows']}
    lines=['# Mean-flow sphere oscillation budget','',f"Status: **{d['status']}**",'',f"Checks passed: **{d['passed']}/{d['total']}**",'',
           '## Exact smooth-frame identity','',d['identity'],'',
           '## N=64 asymmetric benchmark','']
    for ell in (0.75,1.0,1.25,1.5,2.0):
        q=by[ell]
        lines.append(f"- ell={ell:g}: C={q['C_sph']:.9g}, E={q['E_sph']:.9g}, A={q['A_adv']:.9g}, P={q['P_pressure']:.9g}, V={q['V_viscous_volume']:.9g}, ell^2 dC/dt={q['ell2_dCdt']:.9g}")
    lines += ['', 'The mean-zero condition is satisfied to numerical roundoff. Both advection and pressure remain active in the asymmetric case.', '', '## Claim boundary','',d['claim_boundary'],'']
    path.write_text('\n'.join(lines),encoding='utf-8')


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default='results'); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks()
    (out/'mean_flow_sphere_budget.json').write_text(json.dumps(d,indent=2),encoding='utf-8')
    write_md(d,out/'mean_flow_sphere_budget.md')
    print(f"Mean-flow sphere budget: {d['passed']}/{d['total']} checks passed")
    if d['passed']!=d['total']: raise SystemExit(1)

if __name__=='__main__': main()
