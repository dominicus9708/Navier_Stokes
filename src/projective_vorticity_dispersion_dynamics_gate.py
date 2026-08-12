#!/usr/bin/env python3
"""Audit the exact covariance/projective-dispersion evolution algebra.

This does not solve the Navier--Stokes regularity problem. It checks the matrix
identities obtained after whole-space integration of the vorticity equation.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import numpy as np

SCHEMA_VERSION = "0.1.0"


def random_matrix_audit(seed=9708, npts=400, nu=0.73):
    rng = np.random.default_rng(seed)
    weights = rng.random(npts) + 0.05
    omega = rng.normal(size=(npts, 3))

    # Synthetic symmetric trace-free strain tensors at the sample points.
    raw = rng.normal(size=(npts, 3, 3))
    S = 0.5 * (raw + np.swapaxes(raw, 1, 2))
    tr = np.trace(S, axis1=1, axis2=2) / 3.0
    S = S - tr[:, None, None] * np.eye(3)[None, :, :]

    # Synthetic spatial derivatives d_k omega_i. Only the covariance algebra is
    # tested here; these samples are not claimed to form an actual PDE field.
    grad = rng.normal(size=(npts, 3, 3))

    mag2 = np.sum(omega * omega, axis=1)
    E = float(np.sum(weights * mag2))
    N = np.einsum("n,ni,nj->ij", weights, omega, omega)
    C = N / E

    Somega = np.einsum("nij,nj->ni", S, omega)
    A = np.einsum("n,ni,nj->ij", weights, Somega, omega)

    H = np.zeros((3, 3), dtype=float)
    for k in range(3):
        gk = grad[:, :, k]
        H += np.einsum("n,ni,nj->ij", weights, gk, gk)

    Q = float(np.trace(A))
    P = float(np.trace(H))
    B = A / E
    G = H / E
    q = Q / E
    p = P / E

    Ndot = A + A.T - 2.0 * nu * H
    Edot = float(np.trace(Ndot))
    Edot_expected = 2.0 * Q - 2.0 * nu * P

    Cdot_direct = Ndot / E - (Edot / E) * C
    Cdot_formula = B + B.T - 2.0 * nu * G - 2.0 * (q - nu * p) * C

    J = float(1.0 - np.trace(C @ C))
    Jdot_direct = float(-2.0 * np.trace(C @ Cdot_direct))
    Ms = float(q * (1.0 - J) - np.trace(C @ B))
    Mnu = float(np.trace(C @ G) - p * (1.0 - J))
    Jdot_formula = 4.0 * Ms + 4.0 * nu * Mnu

    K = E * E * J
    Kdot_from_product = 2.0 * E * Edot * J + E * E * Jdot_direct
    Kdot_formula = 4.0 * (
        E * Q - np.trace(N @ A) + nu * (np.trace(N @ H) - E * P)
    )

    return {
        "E": E,
        "J": J,
        "Edot": Edot,
        "Edot_expected": Edot_expected,
        "Edot_error": abs(Edot - Edot_expected),
        "Cdot_error": float(np.linalg.norm(Cdot_direct - Cdot_formula)),
        "Ms": Ms,
        "Mnu": Mnu,
        "Jdot_direct": Jdot_direct,
        "Jdot_formula": Jdot_formula,
        "Jdot_error": abs(Jdot_direct - Jdot_formula),
        "K": K,
        "Kdot_from_product": Kdot_from_product,
        "Kdot_formula": Kdot_formula,
        "Kdot_error": abs(Kdot_from_product - Kdot_formula),
        "trace_Cdot": float(np.trace(Cdot_direct)),
        "C_symmetry_error": float(np.linalg.norm(C - C.T)),
        "Cdot_symmetry_error": float(np.linalg.norm(Cdot_direct - Cdot_direct.T)),
    }


def one_axis_invariant(npts=200, nu=1.0):
    # Exact common-axis sample: omega=f e3, S diagonal, gradients parallel e3.
    x = np.linspace(-2.0, 2.0, npts)
    weights = np.exp(-x * x)
    f = np.exp(-0.4 * x * x) * (1.0 + 0.2 * x)
    omega = np.zeros((npts, 3), dtype=float)
    omega[:, 2] = f

    S = np.zeros((npts, 3, 3), dtype=float)
    a = 0.3 * np.sin(x)
    S[:, 0, 0] = -0.5 * a
    S[:, 1, 1] = -0.5 * a
    S[:, 2, 2] = a

    dfdx = np.gradient(f, x)
    grad = np.zeros((npts, 3, 3), dtype=float)
    grad[:, 2, 0] = dfdx

    E = float(np.sum(weights * np.sum(omega * omega, axis=1)))
    N = np.einsum("n,ni,nj->ij", weights, omega, omega)
    C = N / E
    Somega = np.einsum("nij,nj->ni", S, omega)
    A = np.einsum("n,ni,nj->ij", weights, Somega, omega)
    H = np.zeros((3, 3), dtype=float)
    for k in range(3):
        gk = grad[:, :, k]
        H += np.einsum("n,ni,nj->ij", weights, gk, gk)

    Q = float(np.trace(A)); P = float(np.trace(H))
    B = A / E; G = H / E
    q = Q / E; p = P / E
    J = float(1.0 - np.trace(C @ C))
    Ms = float(q * (1.0 - J) - np.trace(C @ B))
    Mnu = float(np.trace(C @ G) - p * (1.0 - J))
    Jdot = 4.0 * Ms + 4.0 * nu * Mnu
    return {
        "C": C.tolist(),
        "J": J,
        "Ms": Ms,
        "Mnu": Mnu,
        "Jdot": Jdot,
    }


def run_checks():
    rnd = random_matrix_audit()
    one = one_axis_invariant()
    checks = {
        "enstrophy_trace_evolution": rnd["Edot_error"] < 1e-10,
        "covariance_evolution_formula": rnd["Cdot_error"] < 1e-10,
        "covariance_trace_preserved": abs(rnd["trace_Cdot"]) < 1e-12,
        "covariance_symmetric": rnd["C_symmetry_error"] < 1e-12,
        "covariance_derivative_symmetric": rnd["Cdot_symmetry_error"] < 1e-12,
        "projective_budget_formula": rnd["Jdot_error"] < 1e-10,
        "unnormalized_pairwise_budget_formula": rnd["Kdot_error"] < 1e-8,
        "one_axis_J_zero": abs(one["J"]) < 1e-12,
        "one_axis_stretch_mixing_zero": abs(one["Ms"]) < 1e-12,
        "one_axis_viscous_mixing_zero": abs(one["Mnu"]) < 1e-12,
        "one_axis_Jdot_zero": abs(one["Jdot"]) < 1e-12,
    }
    checks = {k: bool(v) for k, v in checks.items()}
    return {
        "schema_version": SCHEMA_VERSION,
        "status": "DERIVED GLOBAL COVARIANCE DYNAMICS / COMPUTATIONAL ALGEBRA AUDIT",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "random_audit": rnd,
        "one_axis_invariant": one,
        "identity": "Jdot = 4[q tr(C^2)-tr(CB)] + 4 nu[tr(CG)-p tr(C^2)].",
        "claim_boundary": "The random sample tests matrix algebra after the PDE integration step; it is not a numerical Navier-Stokes solution and gives no global closure.",
    }


def write_md(d, path: Path):
    r = d["random_audit"]
    lines = [
        "# Projective vorticity-dispersion dynamics audit",
        "",
        f"Status: **{d['status']}**",
        "",
        f"Checks passed: **{d['passed']}/{d['total']}**",
        "",
        d["identity"],
        "",
        f"Random algebra errors: Cdot=`{r['Cdot_error']:.3e}`, Jdot=`{r['Jdot_error']:.3e}`, Kdot=`{r['Kdot_error']:.3e}`.",
        "",
        "The exact common-axis benchmark has J=Ms=Mnu=Jdot=0.",
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
    (out / "projective_vorticity_dispersion_dynamics_gate.json").write_text(json.dumps(d, indent=2), encoding="utf-8")
    write_md(d, out / "projective_vorticity_dispersion_dynamics_gate.md")
    print(f"Projective vorticity dispersion dynamics: {d['passed']}/{d['total']} checks passed")
    if d["passed"] != d["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
