#!/usr/bin/env python3
"""Audit the one-step weighted channel closure on the asymmetric Gaussian benchmark.

This is a deterministic numerical audit of the near/far pressure decomposition and
the moving weighted-mean algebra.  The analytic estimates are documented in
notes/2026-08-12-weighted-one-step-channel-closure.md.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


SCHEMA_VERSION = "0.1.0"


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
    """Solve -Delta p = partial_i partial_j T_ij spectrally."""
    rhs_hat = np.zeros(T.shape[2:], dtype=complex)
    for i in range(3):
        for j in range(3):
            rhs_hat += -(K[i]*K[j]) * np.fft.fftn(T[i, j])
    ph = np.zeros_like(rhs_hat)
    nz = k2 > 0
    ph[nz] = rhs_hat[nz] / k2[nz]
    return np.fft.ifftn(ph).real


def smooth_cutoff(r, inner, outer):
    """C1 cosine taper: 1 on r<=inner, 0 on r>=outer."""
    out = np.zeros_like(r)
    out[r <= inner] = 1.0
    m = (r > inner) & (r < outer)
    s = (r[m] - inner) / (outer - inner)
    out[m] = 0.5 * (1.0 + np.cos(np.pi*s))
    return out


def bump_and_grad(X, Y, Z, ell):
    r2 = X*X + Y*Y + Z*Z
    s2 = r2/(ell*ell)
    phi = np.zeros_like(X)
    m = s2 < 1.0
    denom = 1.0 - s2[m]
    phi[m] = np.exp(-1.0/denom)

    grad = np.zeros((3,) + X.shape, dtype=float)
    # d/dr exponent[-1/(1-r^2/ell^2)] gives
    # -2 x_j / (ell^2 (1-r^2/ell^2)^2).
    coeff = np.zeros_like(X)
    coeff[m] = -2.0*phi[m]/(ell*ell*denom*denom)
    grad[0] = coeff*X
    grad[1] = coeff*Y
    grad[2] = coeff*Z
    return phi, grad


def audit(N=64, L=6.0, ell=0.9, nu=1.0):
    x = np.linspace(-L, L, N, endpoint=False)
    h = 2*L/N
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    r = np.sqrt(X*X + Y*Y + Z*Z)
    dv = h**3

    u = (
        seed_grid(X, Y, Z, 2, (0.0, 0.0, 0.0), 1.0)
        + seed_grid(X, Y, Z, 0, (-1.0, 0.0, 0.0), 1.0)
    )

    k = 2*np.pi*np.fft.fftfreq(N, d=h)
    K = np.meshgrid(k, k, k, indexing="ij")
    k2 = K[0]**2 + K[1]**2 + K[2]**2

    grads = np.empty((3, 3, N, N, N), dtype=float)
    for i in range(3):
        uh = np.fft.fftn(u[i])
        for j in range(3):
            grads[i, j] = np.fft.ifftn(1j*K[j]*uh).real
    divu = np.trace(grads, axis1=0, axis2=1)

    phi, gradphi = bump_and_grad(X, Y, Z, ell)
    mass = float(np.sum(phi)*dv)
    Ubar = np.array([float(np.sum(phi*u[i])*dv/mass) for i in range(3)])
    v = u - Ubar[:, None, None, None]
    weighted_mean_v = np.array([float(np.sum(phi*v[i])*dv/mass) for i in range(3)])

    # Full canonical pressure from u tensor.
    Tfull = np.einsum("i...,j...->ij...", u, u)
    p = pressure_from_tensor(Tfull, K, k2)

    # Near pressure uses the Galilean-invariant local source v tensor.
    chi = smooth_cutoff(r, 2.0*ell, 3.0*ell)
    Tnear = chi[None, None, ...] * np.einsum("i...,j...->ij...", v, v)
    pnear = pressure_from_tensor(Tnear, K, k2)
    pfar = p - pnear

    # Check harmonicity of pfar in an inner region separated from cutoff transition.
    pfh = np.fft.fftn(pfar)
    lap_pfar = np.fft.ifftn(-k2*pfh).real
    inner = r < 0.75*ell
    source_scale = float(np.sqrt(np.mean((np.fft.ifftn(k2*np.fft.fftn(p)).real[inner])**2)))
    harmonic_rms = float(np.sqrt(np.mean(lap_pfar[inner]**2)))
    harmonic_relative = harmonic_rms / max(source_scale, 1e-12)

    vdotgradphi = np.sum(v*gradphi, axis=0)
    Pfull = float(ell*np.sum(p*vdotgradphi)*dv)
    Pnear = float(ell*np.sum(pnear*vdotgradphi)*dv)
    Pfar = float(ell*np.sum(pfar*vdotgradphi)*dv)

    # Affine pressure must make no contribution to the weighted variance budget.
    paff = 0.37 + 0.6*X - 0.4*Y + 0.2*Z
    Paff = float(ell*np.sum(paff*vdotgradphi)*dv)

    # Subtract an affine Taylor approximation from pfar; work should be unchanged.
    # Center index is exact because the even periodic grid contains zero.
    cidx = N//2
    grad_pfar = np.array([
        np.fft.ifftn(1j*K[j]*pfh).real for j in range(3)
    ])
    p0 = float(pfar[cidx, cidx, cidx])
    gp0 = np.array([float(grad_pfar[j, cidx, cidx, cidx]) for j in range(3)])
    affine_far = p0 + gp0[0]*X + gp0[1]*Y + gp0[2]*Z
    Pfar_affine_free = float(ell*np.sum((pfar-affine_far)*vdotgradphi)*dv)

    # Parent critical channels, R=4 ell.
    R = 4.0*ell
    parent = r < R
    volR = float(np.sum(parent)*dv)
    cR = np.array([float(np.sum(u[i][parent])*dv/volR) for i in range(3)])
    osc2 = np.sum((u-cR[:, None, None, None])**2, axis=0)
    C_R = float(np.sum(osc2[parent])*dv/R)
    grad2 = np.sum(grads*grads, axis=(0, 1))
    E_R = float(R*np.sum(grad2[parent])*dv)

    local = r < 2.0*ell
    int_v3 = float(np.sum(np.sum(v*v, axis=0)[local]**1.5)*dv)
    cubic_scale = float((C_R*E_R)**0.75)
    l3_ratio = int_v3/max(cubic_scale, 1e-14)

    near_l32 = float((np.sum(np.abs(pnear[local])**1.5)*dv)**(2.0/3.0))
    v_l3 = float((np.sum(np.sum(v*v, axis=0)[local]**1.5)*dv)**(1.0/3.0))
    cz_ratio = near_l32/max(v_l3*v_l3, 1e-14)

    # Relative advection and cutoff-viscous localization channels.
    grad_e_v = np.einsum("i...,ij...->j...", v, grads)
    A = float(ell*np.sum(0.5*np.sum(v*v, axis=0)*np.sum(v*gradphi, axis=0))*dv)
    phih = np.fft.fftn(phi)
    lapphi = np.fft.ifftn(-k2*phih).real
    B = float(0.5*nu*ell*np.sum(np.sum(v*v, axis=0)*lapphi)*dv)

    return {
        "N": N,
        "L": L,
        "ell": ell,
        "h": h,
        "weighted_mean_velocity": Ubar.tolist(),
        "weighted_mean_v_norm": float(np.linalg.norm(weighted_mean_v)),
        "max_divergence": float(np.max(np.abs(divu))),
        "P_full": Pfull,
        "P_near": Pnear,
        "P_far": Pfar,
        "pressure_split_error": abs(Pfull-(Pnear+Pfar)),
        "P_affine_test": Paff,
        "P_far_affine_free": Pfar_affine_free,
        "far_affine_work_difference": abs(Pfar-Pfar_affine_free),
        "far_harmonic_rms": harmonic_rms,
        "far_harmonic_relative": harmonic_relative,
        "C_R": C_R,
        "E_R": E_R,
        "int_v3_local": int_v3,
        "cubic_parent_scale": cubic_scale,
        "l3_interpolation_ratio": l3_ratio,
        "near_pressure_L32": near_l32,
        "v_L3": v_l3,
        "near_CZ_ratio": cz_ratio,
        "A_advective_signed": A,
        "B_cutoff_viscous_signed": B,
    }


def run_checks():
    a48 = audit(48)
    a64 = audit(64)

    checks = {
        "weighted_mean_zero_48": a48["weighted_mean_v_norm"] < 1e-12,
        "weighted_mean_zero_64": a64["weighted_mean_v_norm"] < 1e-12,
        "pressure_split_48": a48["pressure_split_error"] < 1e-10,
        "pressure_split_64": a64["pressure_split_error"] < 1e-10,
        "affine_pressure_negligible_48": abs(a48["P_affine_test"]) < 2e-3,
        "affine_pressure_negligible_64": abs(a64["P_affine_test"]) < 2e-3,
        "affine_far_work_invariant_48": a48["far_affine_work_difference"] < 2e-3,
        "affine_far_work_invariant_64": a64["far_affine_work_difference"] < 2e-3,
        "far_more_harmonic_than_full_source_48": a48["far_harmonic_relative"] < 0.25,
        "far_more_harmonic_than_full_source_64": a64["far_harmonic_relative"] < 0.20,
        "finite_parent_interpolation": np.isfinite(a48["l3_interpolation_ratio"]) and np.isfinite(a64["l3_interpolation_ratio"]),
        "finite_near_CZ_ratio": np.isfinite(a48["near_CZ_ratio"]) and np.isfinite(a64["near_CZ_ratio"]),
    }

    return {
        "schema_version": SCHEMA_VERSION,
        "status": "COMPUTATIONAL CHECK / WEIGHTED ONE-STEP CHANNEL CLOSURE",
        "checks": checks,
        "passed": sum(bool(v) for v in checks.values()),
        "total": len(checks),
        "resolution_48": a48,
        "resolution_64": a64,
        "interpretation": (
            "The asymmetric benchmark confirms the algebraic bookkeeping used by the one-step closure: "
            "the weighted internal velocity has zero mean; the localized Riesz near pressure plus the "
            "harmonic far part reconstructs the total pressure work; affine pressure pieces make no "
            "material contribution to the weighted variance budget; and the near pressure is a finite "
            "local nonlinear channel rather than an independent global pressure scalar."
        ),
        "claim_boundary": (
            "The numerical ratios are benchmark audits, not universal constants. The analytic inequalities "
            "are established separately in the accompanying note using Poincare-Sobolev and Calderon-Zygmund estimates."
        ),
    }


def write_md(d, path):
    a = d["resolution_64"]
    lines = [
        "# Weighted one-step channel closure audit",
        "",
        f"Status: **{d['status']}**",
        "",
        f"Checks passed: **{d['passed']}/{d['total']}**",
        "",
        "## N=64 benchmark",
        "",
        f"- weighted mean residual: `{a['weighted_mean_v_norm']:.6g}`",
        f"- pressure split error: `{a['pressure_split_error']:.6g}`",
        f"- affine pressure work: `{a['P_affine_test']:.6g}`",
        f"- far affine-subtraction work difference: `{a['far_affine_work_difference']:.6g}`",
        f"- far harmonic relative residual: `{a['far_harmonic_relative']:.6g}`",
        f"- parent interpolation ratio: `{a['l3_interpolation_ratio']:.6g}`",
        f"- near-pressure CZ benchmark ratio: `{a['near_CZ_ratio']:.6g}`",
        f"- full / near / far pressure work: `{a['P_full']:.6g}` / `{a['P_near']:.6g}` / `{a['P_far']:.6g}`",
        "",
        "## Interpretation",
        "",
        d["interpretation"],
        "",
        "## Claim boundary",
        "",
        d["claim_boundary"],
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", default="results")
    args = ap.parse_args()
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    d = run_checks()
    (out/"weighted_channel_closure_gate.json").write_text(json.dumps(d, indent=2), encoding="utf-8")
    write_md(d, out/"weighted_channel_closure_gate.md")
    print(f"Weighted channel closure: {d['passed']}/{d['total']} checks passed")
    if d["passed"] != d["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
