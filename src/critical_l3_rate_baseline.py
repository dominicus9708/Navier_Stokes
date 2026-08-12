#!/usr/bin/env python3
"""Critical L3 pressure-rate audit for smooth Gaussian double-curl benchmarks.

The FFT window is a numerical approximation to the whole-space Poisson inversion for
rapidly decaying data. It is not a physical periodic container and not a time solver.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp


def symbolic_single_seed_parity() -> dict:
    x,y,z=sp.symbols("x y z",real=True)
    coords=(x,y,z); r2=x*x+y*y+z*z; g=sp.exp(-r2)
    u=sp.Matrix([4*x*z*g,4*y*z*g,4*(1-x*x-y*y)*g])
    G=sp.Matrix([[sp.diff(u[i],coords[j]) for j in range(3)] for i in range(3)])
    adv=sp.Matrix([sp.simplify(sum(u[j]*G[i,j] for j in range(3))) for i in range(3)])
    numerator=sp.factor((u.T*adv)[0])
    mag2=sp.factor((u.T*u)[0])
    Q=sp.factor(sum(G[i,j]*G[j,i] for i in range(3) for j in range(3)))
    refl=lambda expr: sp.simplify(expr.subs(z,-z))
    return {
        "Q_even_in_z": bool(sp.simplify(refl(Q)-Q)==0),
        "speed_squared_even_in_z": bool(sp.simplify(refl(mag2)-mag2)==0),
        "u_dot_adv_odd_in_z": bool(sp.simplify(refl(numerator)+numerator)==0),
        "Q":str(Q),
        "u_dot_adv":str(numerator),
        "consequence":"Even whole-space pressure times odd u·grad|u| gives Pi3=0 for the symmetric seed.",
    }


def seed_field_grid(X,Y,Z,axis=2,center=(0.0,0.0,0.0),amplitude=1.0):
    ys=[X-center[0],Y-center[1],Z-center[2]]
    rr=ys[0]**2+ys[1]**2+ys[2]**2
    g=np.exp(-rr)
    u=np.empty((3,)+X.shape,dtype=float)
    for j in range(3):
        if j==axis:
            transverse=sum(ys[k]**2 for k in range(3) if k!=axis)
            u[j]=amplitude*4.0*(1.0-transverse)*g
        else:
            u[j]=amplitude*4.0*ys[j]*ys[axis]*g
    return u


def spectral_diagnostics(specs,N=80,L=6.0):
    x=np.linspace(-L,L,N,endpoint=False); h=2.0*L/N
    X,Y,Z=np.meshgrid(x,x,x,indexing="ij")
    u=np.zeros((3,N,N,N),dtype=float)
    for axis,center,amplitude in specs:
        u+=seed_field_grid(X,Y,Z,axis,center,amplitude)

    k=2.0*np.pi*np.fft.fftfreq(N,d=h)
    K=np.meshgrid(k,k,k,indexing="ij")
    grads=np.empty((3,3,N,N,N),dtype=float)
    for i in range(3):
        uh=np.fft.fftn(u[i])
        for j in range(3):
            grads[i,j]=np.fft.ifftn(1j*K[j]*uh).real

    divergence=sum(grads[i,i] for i in range(3))
    Q=np.einsum("ij...,ji...->...",grads,grads)
    qhat=np.fft.fftn(Q); k2=K[0]**2+K[1]**2+K[2]**2
    phat=np.zeros_like(qhat); nz=k2>0; phat[nz]=qhat[nz]/k2[nz]
    p=np.fft.ifftn(phat).real

    adv=np.einsum("j...,ij...->i...",u,grads)
    speed=np.linalg.norm(u,axis=0)
    u_dot_grad_speed=np.divide(
        np.sum(u*adv,axis=0),speed,
        out=np.zeros_like(speed),where=speed>1e-14,
    )
    grad_norm2=np.sum(grads*grads,axis=(0,1))
    directional=np.zeros_like(speed)
    for j in range(3):
        directional+=np.sum(u*grads[:,j],axis=0)**2
    d3_density=speed*grad_norm2+np.divide(
        directional,speed,out=np.zeros_like(speed),where=speed>1e-14
    )
    dv=h**3
    boundary_speed=max(
        np.max(speed[0,:,:]),np.max(speed[-1,:,:]),
        np.max(speed[:,0,:]),np.max(speed[:,-1,:]),
        np.max(speed[:,:,0]),np.max(speed[:,:,-1]),
    )
    return {
        "N":int(N),"L":float(L),"h":float(h),
        "T3":float(np.sum(speed**3)*dv),
        "Pi3":float(np.sum(p*u_dot_grad_speed)*dv),
        "D3":float(np.sum(d3_density)*dv),
        "divergence_max_abs":float(np.max(np.abs(divergence))),
        "boundary_speed_max":float(boundary_speed),
    }


def run_checks() -> dict:
    parity=symbolic_single_seed_parity()
    single=[(2,(0.0,0.0,0.0),1.0)]
    positive=[(2,(0.0,0.0,0.0),1.0),(0,(-1.0,0.0,0.0),1.0)]
    negative=[(2,(0.0,0.0,0.0),1.0),(0,(1.0,0.0,0.0),1.0)]

    single_hi=spectral_diagnostics(single,N=80,L=6.0)
    pos_conv=[spectral_diagnostics(positive,N=N,L=6.0) for N in (48,64,80,96)]
    neg_hi=spectral_diagnostics(negative,N=80,L=6.0)
    pos=pos_conv[-1]
    pi_values=[row["Pi3"] for row in pos_conv]
    rel_spread=float((max(pi_values)-min(pi_values))/max(abs(float(np.mean(pi_values))),1e-30))

    nu=1.0
    threshold=float(nu*pos["D3"]/pos["Pi3"])
    A_test=120.0
    rate=float(3.0*(A_test**4*pos["Pi3"]-nu*A_test**3*pos["D3"]))

    checks={
        "single_Q_even":bool(parity["Q_even_in_z"]),
        "single_speed_even":bool(parity["speed_squared_even_in_z"]),
        "single_u_dot_adv_odd":bool(parity["u_dot_adv_odd_in_z"]),
        "single_numeric_Pi3_near_zero":bool(abs(single_hi["Pi3"])<1e-8),
        "asymmetric_positive_Pi3_all_resolutions":bool(min(pi_values)>0.0),
        "asymmetric_Pi3_resolution_spread_small":bool(rel_spread<0.01),
        "reflection_related_negative_Pi3":bool(neg_hi["Pi3"]<0.0),
        "opposite_sign_magnitudes_close":bool(abs(pos["Pi3"]+neg_hi["Pi3"])/abs(pos["Pi3"])<0.01),
        "amplitude_threshold_finite":bool(math.isfinite(threshold) and threshold>0.0),
        "amplified_initial_L3_rate_positive_candidate":bool(rate>0.0),
    }
    return {
        "status":"COMPUTATIONAL CHECK + DERIVED SYMMETRY / CRITICAL-L3 RATE",
        "checks":checks,"passed":int(sum(checks.values())),"total":int(len(checks)),
        "single_seed":{"parity":parity,"numerical":single_hi,"Pi3_exact_by_symmetry":0.0},
        "positive_pressure_shape":{
            "specification":"z-seed at 0 plus x-seed at (-1,0,0), equal amplitudes",
            "resolution_convergence":pos_conv,"representative":pos,
            "Pi3_relative_spread_48_to_96":rel_spread,
        },
        "negative_pressure_shape":{
            "specification":"z-seed at 0 plus x-seed at (1,0,0), equal amplitudes",
            "representative":neg_hi,
        },
        "amplitude_homogeneity":{
            "T3":"A^3","D3":"A^3","Pi3":"A^4","nu":nu,
            "computational_threshold_A_for_positive_initial_rate":threshold,
            "test_amplitude":A_test,"predicted_initial_dT3_dt_at_test_amplitude":rate,
        },
        "interpretation":{
            "single_seed":"Symmetry hides the pressure obstruction.",
            "asymmetric_seed":"Breaking symmetry gives sign-indefinite Pi3 in the deterministic audit.",
            "route_status":"Naive monotone global-L3 decay is a FAILED-ROUTE CANDIDATE, not yet a rigorous counterexample theorem.",
            "next_target":"Control Pi3 without assuming the critical norm bound being sought.",
        },
        "numerical_boundary":"Spectral inversion on a large decay window approximates the whole-space Poisson solve; it is not a physical periodic-domain model.",
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output-dir",default="results"); args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks()
    (out/"critical_l3_rate_baseline.json").write_text(json.dumps(d,indent=2),encoding="utf-8")
    pos=d["positive_pressure_shape"]["representative"]; neg=d["negative_pressure_shape"]["representative"]; amp=d["amplitude_homogeneity"]
    lines=[
        "# Critical L3 pressure-rate baseline","",f"Checks passed: **{d['passed']}/{d['total']}**","",
        "## Symmetric seed","","Reflection parity gives `Pi3=0` exactly for the single benchmark.",f"Spectral check: `Pi3≈{d['single_seed']['numerical']['Pi3']:.3e}`.","",
        "## Asymmetric superposition","",f"Positive shape: `Pi3≈{pos['Pi3']:.12g}`, `D3≈{pos['D3']:.12g}`, `T3≈{pos['T3']:.12g}`.",f"Reflection-related shape: `Pi3≈{neg['Pi3']:.12g}`.",f"Resolution spread: `{d['positive_pressure_shape']['Pi3_relative_spread_48_to_96']:.3%}`.","",
        "## Amplitude homogeneity","","`T3,D3 ~ A^3`; `Pi3 ~ A^4` for a fixed shape.",f"For `nu=1`, crossover `A≈{amp['computational_threshold_A_for_positive_initial_rate']:.6g}`.",f"At `A={amp['test_amplitude']:.0f}`, predicted initial `dT3/dt≈{amp['predicted_initial_dT3_dt_at_test_amplitude']:.12g}>0`.","",
        "Status: **FAILED-ROUTE CANDIDATE / COMPUTATIONAL COUNTEREXAMPLE**, not a theorem-level counterexample.","",
        "## Numerical boundary","",d["numerical_boundary"],
    ]
    (out/"critical_l3_rate_baseline.md").write_text("\n".join(lines),encoding="utf-8")
    print(f"Critical L3 rate audit: {d['passed']}/{d['total']} checks passed")
    if d["passed"]!=d["total"]: raise SystemExit(1)

if __name__=="__main__":
    main()
