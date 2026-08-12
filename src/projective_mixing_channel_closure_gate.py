#!/usr/bin/env python3
"""Audit the projective S/V mixing-channel closure inequalities."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import numpy as np

SCHEMA_VERSION = "0.1.0"


def random_audit(seed=9708, npts=600, nu=0.8):
    rng = np.random.default_rng(seed)
    weights = rng.random(npts) + 0.05
    omega = rng.normal(size=(npts, 3))

    raw = rng.normal(size=(npts, 3, 3))
    S = 0.5 * (raw + np.swapaxes(raw, 1, 2))
    trS = np.trace(S, axis1=1, axis2=2) / 3.0
    S = S - trS[:, None, None] * np.eye(3)[None, :, :]

    grad = rng.normal(size=(npts, 3, 3))

    mag2 = np.sum(omega * omega, axis=1)
    E = float(np.sum(weights * mag2))
    N = np.einsum("n,ni,nj->ij", weights, omega, omega)
    C = N / E
    J = float(1.0 - np.trace(C @ C))
    s = 1.0 - J

    Somega = np.einsum("nij,nj->ni", S, omega)
    A = np.einsum("n,ni,nj->ij", weights, Somega, omega)
    B = A / E
    q = float(np.trace(B))
    Ms = float(q * s - np.trace(C @ B))
    Ls2 = float(np.sum(weights * np.sum(Somega * Somega, axis=1)) / E)
    Ls = float(np.sqrt(max(Ls2, 0.0)))
    Ms_bound = float(np.sqrt(max(J * (1.0 - J), 0.0)) * Ls)

    # Verify the eigenbasis factor used in the proof.
    vals, vecs = np.linalg.eigh(C)
    order = np.argsort(vals)[::-1]
    vals = vals[order]
    vecs = vecs[:, order]
    factor_exact = float(np.sum(vals * (s - vals) ** 2))
    factor_invariant = float(np.sum(vals ** 3) - s * s)
    factor_bound = float(s * J)

    # Gradient covariance and viscous branch.
    H = np.zeros((3, 3), dtype=float)
    for k in range(3):
        gk = grad[:, :, k]
        H += np.einsum("n,ni,nj->ij", weights, gk, gk)
    P = float(np.trace(H))
    p = P / E
    Cgrad = H / P
    G = H / E
    Mnu = float(np.trace(C @ G) - p * s)
    Delta = float(np.linalg.norm(Cgrad - C))
    Mnu_bound = float(p * np.sqrt(max(1.0 - J, 0.0)) * Delta)

    # Enstrophy-weighted pointwise decomposition |S xi|^2 = gamma^2 + chi^2.
    mask = mag2 > 1e-14
    xi = np.zeros_like(omega)
    xi[mask] = omega[mask] / np.sqrt(mag2[mask])[:, None]
    Sxi = np.einsum("nij,nj->ni", S, xi)
    gamma = np.sum(xi * Sxi, axis=1)
    perp = Sxi - gamma[:, None] * xi
    decomp_lhs = float(np.sum(weights[mask] * mag2[mask] * np.sum(Sxi[mask] ** 2, axis=1)) / E)
    decomp_rhs = float(np.sum(weights[mask] * mag2[mask] * (gamma[mask] ** 2 + np.sum(perp[mask] ** 2, axis=1))) / E)

    Jdot_upper = 4.0 * np.sqrt(max(1.0 - J, 0.0)) * (np.sqrt(max(J, 0.0)) * Ls + nu * p * Delta)
    Jdot_exact = 4.0 * Ms + 4.0 * nu * Mnu

    return {
        "E": E,
        "J": J,
        "Ms": Ms,
        "Ls": Ls,
        "Ms_bound": Ms_bound,
        "Ms_margin": Ms_bound - abs(Ms),
        "factor_exact": factor_exact,
        "factor_invariant": factor_invariant,
        "factor_bound": factor_bound,
        "P": P,
        "p": p,
        "Mnu": Mnu,
        "Delta_nu": Delta,
        "Mnu_bound": Mnu_bound,
        "Mnu_margin": Mnu_bound - abs(Mnu),
        "pointwise_decomp_lhs": decomp_lhs,
        "pointwise_decomp_rhs": decomp_rhs,
        "pointwise_decomp_error": abs(decomp_lhs - decomp_rhs),
        "Jdot_exact": Jdot_exact,
        "Jdot_upper": Jdot_upper,
        "Jdot_upper_margin": Jdot_upper - Jdot_exact,
    }


def matched_covariance_viscous_zero(seed=17):
    rng = np.random.default_rng(seed)
    raw = rng.random(3) + 0.2
    mu = raw / np.sum(raw)
    C = np.diag(mu)
    p = 2.7
    Cgrad = C.copy()
    G = p * Cgrad
    J = float(1.0 - np.trace(C @ C))
    Mnu = float(np.trace(C @ G) - p * (1.0 - J))
    return {"eigenvalues": mu.tolist(), "J": J, "Mnu": Mnu}


def strain_factorial_examples():
    # Purely algebraic covariance spectra to test the factor inequality.
    spectra = [
        np.array([1.0, 0.0, 0.0]),
        np.array([0.8, 0.15, 0.05]),
        np.array([0.5, 0.5, 0.0]),
        np.array([0.6, 0.25, 0.15]),
        np.array([1/3, 1/3, 1/3]),
    ]
    out = []
    for mu in spectra:
        s = float(np.sum(mu * mu))
        J = 1.0 - s
        F = float(np.sum(mu * (s - mu) ** 2))
        out.append({"mu": mu.tolist(), "J": J, "F": F, "sJ": s * J, "ok": bool(F <= s * J + 1e-14)})
    return out


def run_checks():
    r = random_audit()
    z = matched_covariance_viscous_zero()
    ex = strain_factorial_examples()
    checks = {
        "strain_factor_invariant_identity": abs(r["factor_exact"] - r["factor_invariant"]) < 1e-12,
        "strain_factor_bounded_by_sJ": r["factor_exact"] <= r["factor_bound"] + 1e-12,
        "strain_mixing_bound": r["Ms_margin"] >= -1e-12,
        "pointwise_strain_exposure_decomposition": r["pointwise_decomp_error"] < 1e-12,
        "viscous_mixing_bound": r["Mnu_margin"] >= -1e-12,
        "matched_gradient_covariance_zero_mixing": abs(z["Mnu"]) < 1e-12,
        "combined_Jdot_upper_bound": r["Jdot_upper_margin"] >= -1e-12,
        "example_factor_bounds": all(v["ok"] for v in ex),
    }
    checks = {k: bool(v) for k, v in checks.items()}
    return {
        "schema_version": SCHEMA_VERSION,
        "status": "DERIVED PROJECTIVE MIXING-CLOSURE INEQUALITIES / COMPUTATIONAL ALGEBRA AUDIT",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "random_audit": r,
        "matched_covariance_case": z,
        "spectral_examples": ex,
        "strain_bound": "|M_S| <= sqrt(J(1-J)) L_S.",
        "viscous_bound": "|M_nu| <= (P/E) sqrt(1-J) ||C_grad-C||_F.",
        "combined_bound": "Jdot <= 4 sqrt(1-J)[sqrt(J)L_S + nu(P/E)Delta_nu].",
        "claim_boundary": "These are exact/derived inequalities for smooth whole-space covariance moments; no spacetime integrability closure for the right-hand side has been proved.",
    }


def write_md(d, path: Path):
    r = d["random_audit"]
    lines = [
        "# Projective mixing-channel closure audit",
        "",
        f"Status: **{d['status']}**",
        "",
        f"Checks passed: **{d['passed']}/{d['total']}**",
        "",
        d["strain_bound"],
        "",
        d["viscous_bound"],
        "",
        d["combined_bound"],
        "",
        f"Random margins: S=`{r['Ms_margin']:.3e}`, V=`{r['Mnu_margin']:.3e}`, combined=`{r['Jdot_upper_margin']:.3e}`.",
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
    (out / "projective_mixing_channel_closure_gate.json").write_text(json.dumps(d, indent=2), encoding="utf-8")
    write_md(d, out / "projective_mixing_channel_closure_gate.md")
    print(f"Projective mixing closure: {d['passed']}/{d['total']} checks passed")
    if d["passed"] != d["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
