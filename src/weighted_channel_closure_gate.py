#!/usr/bin/env python3
"""Audit the one-step weighted channel closure on an asymmetric Gaussian benchmark.

The theorem-level estimates live in
notes/2026-08-12-weighted-one-step-channel-closure.md.
This script only checks numerical bookkeeping of the near/far pressure split.
All derivatives used in the FFT audit are evaluated by the same spectral operator.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import numpy as np

SCHEMA_VERSION = "0.3.0"


def seed_grid(X, Y, Z, axis, center, amp=1.0):
    q = [X-center[0], Y-center[1], Z-center[2]]
    r2 = sum(v*v for v in q)
    g = np.exp(-r2)
    u = np.empty((3,) + X.shape, dtype=float)
    for j in range(3):
        if j == axis:
            transverse = sum(q[k]**2 for k in range(3) if k != axis)
            u[j] = 4*amp*(1-transverse)*g
        else:
            u[j] = 4*amp*q[j]*q[axis]*g
    return u


def pressure_from_tensor(T, K, k2):
    rhs_hat = np.zeros(T.shape[2:], dtype=complex)
    for i in range(3):
        for j in range(3):
            rhs_hat += -(K[i]*K[j])*np.fft.fftn(T[i, j])
    ph = np.zeros_like(rhs_hat)
    nz = k2 > 0
    ph[nz] = rhs_hat[nz]/k2[nz]
    return np.fft.ifftn(ph).real


def cinf_cutoff(r, inner, outer):
    out = np.zeros_like(r)
    out[r <= inner] = 1.0
    m = (r > inner) & (r < outer)
    s = (r[m]-inner)/(outer-inner)
    a = np.exp(-1.0/s)
    b = np.exp(-1.0/(1.0-s))
    out[m] = 1.0-a/(a+b)
    return out


def compact_bump(X, Y, Z, ell):
    r2 = X*X+Y*Y+Z*Z
    s2 = r2/(ell*ell)
    phi = np.zeros_like(X)
    m = s2 < 1.0
    phi[m] = np.exp(-1.0/(1.0-s2[m]))
    return phi


def audit(N=64, L=6.0, ell=0.9, nu=1.0):
    x = np.linspace(-L, L, N, endpoint=False)
    h = 2*L/N
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    r = np.sqrt(X*X+Y*Y+Z*Z)
    dv = h**3

    u = (
        seed_grid(X, Y, Z, 2, (0.0, 0.0, 0.0), 1.0)
        + seed_grid(X, Y, Z, 0, (-1.0, 0.0, 0.0), 1.0)
    )

    k = 2*np.pi*np.fft.fftfreq(N, d=h)
    K = np.meshgrid(k, k, k, indexing="ij")
    k2 = K[0]**2+K[1]**2+K[2]**2

    grads = np.empty((3, 3, N, N, N), dtype=float)
    for i in range(3):
        uh = np.fft.fftn(u[i])
        for j in range(3):
            grads[i, j] = np.fft.ifftn(1j*K[j]*uh).real
    divu = np.trace(grads, axis1=0, axis2=1)

    phi = compact_bump(X, Y, Z, ell)
    phih = np.fft.fftn(phi)
    gradphi = np.array([np.fft.ifftn(1j*K[j]*phih).real for j in range(3)])
    lapphi = np.fft.ifftn(-k2*phih).real

    mass = float(np.sum(phi)*dv)
    Ubar = np.array([float(np.sum(phi*u[i])*dv/mass) for i in range(3)])
    v = u-Ubar[:, None, None, None]
    mean_v = np.array([float(np.sum(phi*v[i])*dv/mass) for i in range(3)])

    Tfull = np.einsum("i...,j...->ij...", u, u)
    p = pressure_from_tensor(Tfull, K, k2)

    chi = cinf_cutoff(r, 2.0*ell, 3.0*ell)
    Tnear = chi[None, None, ...]*np.einsum("i...,j...->ij...", v, v)
    pnear = pressure_from_tensor(Tnear, K, k2)
    pfar = p-pnear

    pfh = np.fft.fftn(pfar)
    lap_pfar = np.fft.ifftn(-k2*pfh).real
    inner = r < 0.75*ell
    full_source = np.fft.ifftn(k2*np.fft.fftn(p)).real
    source_rms = float(np.sqrt(np.mean(full_source[inner]**2)))
    harmonic_rms = float(np.sqrt(np.mean(lap_pfar[inner]**2)))
    harmonic_relative = harmonic_rms/max(source_rms, 1e-14)

    vdotgradphi = np.sum(v*gradphi, axis=0)
    Pfull = float(ell*np.sum(p*vdotgradphi)*dv)
    Pnear = float(ell*np.sum(pnear*vdotgradphi)*dv)
    Pfar = float(ell*np.sum(pfar*vdotgradphi)*dv)

    paff = 0.37+0.6*X-0.4*Y+0.2*Z
    Paff = float(ell*np.sum(paff*vdotgradphi)*dv)

    cidx = N//2
    grad_pfar = np.array([np.fft.ifftn(1j*K[j]*pfh).real for j in range(3)])
    p0 = float(pfar[cidx, cidx, cidx])
    gp0 = np.array([float(grad_pfar[j, cidx, cidx, cidx]) for j in range(3)])
    affine_far = p0+gp0[0]*X+gp0[1]*Y+gp0[2]*Z
    Pfar_free = float(ell*np.sum((pfar-affine_far)*vdotgradphi)*dv)

    R = 4.0*ell
    parent = r < R
    volR = float(np.sum(parent)*dv)
    cR = np.array([float(np.sum(u[i][parent])*dv/volR) for i in range(3)])
    osc2 = np.sum((u-cR[:, None, None, None])**2, axis=0)
    C_R = float(np.sum(osc2[parent])*dv/R)
    grad2 = np.sum(grads*grads, axis=(0, 1))
    E_R = float(R*np.sum(grad2[parent])*dv)

    local = r < 2.0*ell
    v2 = np.sum(v*v, axis=0)
    int_v3 = float(np.sum(v2[local]**1.5)*dv)
    cubic = float((C_R*E_R)**0.75)
    interp_ratio = int_v3/max(cubic, 1e-14)
    pnear_l32 = float((np.sum(np.abs(pnear[local])**1.5)*dv)**(2.0/3.0))
    v_l3 = float((np.sum(v2[local]**1.5)*dv)**(1.0/3.0))
    cz_ratio = pnear_l32/max(v_l3*v_l3, 1e-14)

    A = float(ell*np.sum(0.5*v2*vdotgradphi)*dv)
    B = float(0.5*nu*ell*np.sum(v2*lapphi)*dv)

    return {
        "N": N, "L": L, "ell": ell, "h": h,
        "weighted_mean_velocity": Ubar.tolist(),
        "weighted_mean_v_norm": float(np.linalg.norm(mean_v)),
        "max_divergence": float(np.max(np.abs(divu))),
        "P_full": Pfull, "P_near": Pnear, "P_far": Pfar,
        "pressure_split_error": float(abs(Pfull-(Pnear+Pfar))),
        "P_affine_test": Paff,
        "P_far_affine_free": Pfar_free,
        "far_affine_work_difference": float(abs(Pfar-Pfar_free)),
        "far_harmonic_rms": harmonic_rms,
        "far_harmonic_relative": harmonic_relative,
        "C_R": C_R, "E_R": E_R,
        "int_v3_local": int_v3,
        "cubic_parent_scale": cubic,
        "l3_interpolation_ratio": interp_ratio,
        "near_pressure_L32": pnear_l32,
        "v_L3": v_l3,
        "near_CZ_ratio": cz_ratio,
        "A_advective_signed": A,
        "B_cutoff_viscous_signed": B,
    }


def run_checks():
    a48, a64 = audit(48), audit(64)
    raw = {
        "weighted_mean_zero_48": a48["weighted_mean_v_norm"] < 1e-12,
        "weighted_mean_zero_64": a64["weighted_mean_v_norm"] < 1e-12,
        "pressure_split_48": a48["pressure_split_error"] < 1e-10,
        "pressure_split_64": a64["pressure_split_error"] < 1e-10,
        "affine_pressure_negligible_48": abs(a48["P_affine_test"]) < 2e-3,
        "affine_pressure_negligible_64": abs(a64["P_affine_test"]) < 2e-3,
        "affine_far_work_invariant_48": a48["far_affine_work_difference"] < 2e-3,
        "affine_far_work_invariant_64": a64["far_affine_work_difference"] < 2e-3,
        "far_harmonic_relative_48": a48["far_harmonic_relative"] < 0.25,
        "far_harmonic_relative_64": a64["far_harmonic_relative"] < 0.20,
        "finite_parent_interpolation": np.isfinite(a48["l3_interpolation_ratio"]) and np.isfinite(a64["l3_interpolation_ratio"]),
        "finite_near_CZ_ratio": np.isfinite(a48["near_CZ_ratio"]) and np.isfinite(a64["near_CZ_ratio"]),
    }
    checks = {k: bool(v) for k, v in raw.items()}
    failed = [k for k, v in checks.items() if not v]
    return {
        "schema_version": SCHEMA_VERSION,
        "status": "COMPUTATIONAL CHECK / WEIGHTED ONE-STEP CHANNEL CLOSURE",
        "checks": checks, "failed_checks": failed,
        "passed": sum(checks.values()), "total": len(checks),
        "resolution_48": a48, "resolution_64": a64,
        "interpretation": "A single spectral derivative operator is used for velocity, pressure and the sampled cutoff. The audit checks weighted mean removal, pressure reconstruction, affine-pressure irrelevance, inner harmonicity of the far piece, and finite interpolation/CZ ratios.",
        "claim_boundary": "Numerical ratios are benchmark audits, not universal constants; theorem-level estimates are documented separately."
    }


def write_md(d, path):
    a = d["resolution_64"]
    lines = [
        "# Weighted one-step channel closure audit", "",
        f"Status: **{d['status']}**", "",
        f"Checks passed: **{d['passed']}/{d['total']}**", "",
        f"Failed checks: `{d['failed_checks']}`", "",
        "## N=64 benchmark", "",
        f"- weighted mean residual: `{a['weighted_mean_v_norm']:.6g}`",
        f"- pressure split error: `{a['pressure_split_error']:.6g}`",
        f"- affine pressure work: `{a['P_affine_test']:.6g}`",
        f"- far affine-subtraction work difference: `{a['far_affine_work_difference']:.6g}`",
        f"- far harmonic relative residual: `{a['far_harmonic_relative']:.6g}`",
        f"- parent interpolation ratio: `{a['l3_interpolation_ratio']:.6g}`",
        f"- near-pressure CZ benchmark ratio: `{a['near_CZ_ratio']:.6g}`",
        f"- full / near / far pressure work: `{a['P_full']:.6g}` / `{a['P_near']:.6g}` / `{a['P_far']:.6g}`",
        "", "## Claim boundary", "", d["claim_boundary"], ""
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--output-dir", default="results")
    args = ap.parse_args(); out = Path(args.output_dir); out.mkdir(parents=True, exist_ok=True)
    d = run_checks()
    (out/"weighted_channel_closure_gate.json").write_text(json.dumps(d, indent=2), encoding="utf-8")
    write_md(d, out/"weighted_channel_closure_gate.md")
    print(f"Weighted channel closure: {d['passed']}/{d['total']} checks passed")
    print("Failed checks:", d["failed_checks"])
    print("N=48 far harmonic relative:", d["resolution_48"]["far_harmonic_relative"])
    print("N=64 far harmonic relative:", d["resolution_64"]["far_harmonic_relative"])
    if d["passed"] != d["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
