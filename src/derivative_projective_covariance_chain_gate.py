#!/usr/bin/env python3
"""Audit the derivative-order projective covariance chain algebra."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import numpy as np

SCHEMA_VERSION = "0.1.0"


def one_level(seed: int, nwords: int, nu: float = 0.65):
    rng = np.random.default_rng(seed)
    # Current derivative family w_I and nonlinear forcing F_I.
    w = rng.normal(size=(nwords, 3))
    F = rng.normal(size=(nwords, 3))

    # One additional ordered spatial derivative for each current word.
    # Shape: (word, derivative-direction, vector-component).
    dw = rng.normal(size=(nwords, 3, 3))
    wnext = dw.reshape(nwords * 3, 3)

    E = float(np.sum(w * w))
    N = w.T @ w
    C = N / E
    J = float(1.0 - np.trace(C @ C))
    s = 1.0 - J

    A = F.T @ w
    Q = float(np.trace(A))
    B = A / E
    q = Q / E

    Enext = float(np.sum(wnext * wnext))
    Nnext = wnext.T @ wnext
    Cnext = Nnext / Enext
    r = Enext / E
    Delta = float(np.linalg.norm(Cnext - C))

    Ndot = A + A.T - 2.0 * nu * Nnext
    Edot = float(np.trace(Ndot))
    Edot_expected = 2.0 * Q - 2.0 * nu * Enext

    Cdot_direct = Ndot / E - (Edot / E) * C
    Cdot_formula = B + B.T - 2.0 * nu * r * Cnext - 2.0 * (q - nu * r) * C

    Jdot_direct = float(-2.0 * np.trace(C @ Cdot_direct))
    Mnl = float(q * s - np.trace(C @ B))
    Achain = float(np.trace(C @ Cnext) - s)
    Jdot_formula = 4.0 * Mnl + 4.0 * nu * r * Achain

    # Generic nonlinear-mixing bound.
    L = float(np.sqrt(np.sum(F * F) / E))
    Mnl_bound = float(np.sqrt(max(J * (1.0 - J), 0.0)) * L)

    # Neighboring covariance mismatch bound.
    Achain_bound = float(np.sqrt(max(1.0 - J, 0.0)) * Delta)

    return {
        "nwords": nwords,
        "E": E,
        "Enext": Enext,
        "r": r,
        "J": J,
        "Jnext": float(1.0 - np.trace(Cnext @ Cnext)),
        "Delta": Delta,
        "Edot_error": abs(Edot - Edot_expected),
        "Cdot_error": float(np.linalg.norm(Cdot_direct - Cdot_formula)),
        "trace_Cdot": float(np.trace(Cdot_direct)),
        "Jdot_direct": Jdot_direct,
        "Jdot_formula": Jdot_formula,
        "Jdot_error": abs(Jdot_direct - Jdot_formula),
        "Mnl": Mnl,
        "L": L,
        "Mnl_bound": Mnl_bound,
        "Mnl_margin": Mnl_bound - abs(Mnl),
        "Achain": Achain,
        "Achain_bound": Achain_bound,
        "Achain_margin": Achain_bound - abs(Achain),
        "combined_upper": 4.0 * np.sqrt(max(1.0 - J, 0.0)) * (np.sqrt(max(J, 0.0)) * L + nu * r * Delta),
    }


def matched_chain_case():
    # C_{k+1}=C_k implies zero viscous directional mixing.
    mu = np.array([0.7, 0.2, 0.1])
    C = np.diag(mu)
    Cnext = C.copy()
    J = float(1.0 - np.trace(C @ C))
    Achain = float(np.trace(C @ Cnext) - np.trace(C @ C))
    return {"J": J, "Achain": Achain, "Delta": float(np.linalg.norm(Cnext - C))}


def run_checks():
    rows = [one_level(9708 + k, 3 ** min(k + 1, 5)) for k in range(5)]
    matched = matched_chain_case()
    checks = {
        "all_enstrophy_trace_evolution": all(r["Edot_error"] < 1e-10 for r in rows),
        "all_covariance_evolution": all(r["Cdot_error"] < 1e-10 for r in rows),
        "all_covariance_trace_preserved": all(abs(r["trace_Cdot"]) < 1e-12 for r in rows),
        "all_projective_chain_budgets": all(r["Jdot_error"] < 1e-10 for r in rows),
        "all_nonlinear_mixing_bounds": all(r["Mnl_margin"] >= -1e-12 for r in rows),
        "all_neighbor_mismatch_bounds": all(r["Achain_margin"] >= -1e-12 for r in rows),
        "all_combined_upper_bounds": all(r["combined_upper"] - r["Jdot_direct"] >= -1e-12 for r in rows),
        "matched_covariance_zero_viscous_mixing": abs(matched["Achain"]) < 1e-12 and matched["Delta"] < 1e-12,
    }
    checks = {k: bool(v) for k, v in checks.items()}
    return {
        "schema_version": SCHEMA_VERSION,
        "status": "DERIVED DERIVATIVE-ORDER PROJECTIVE COVARIANCE CHAIN / ALGEBRA AUDIT",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "levels": rows,
        "matched_case": matched,
        "chain_identity": "Jdot_k/4 = M_N,k + nu(E_{k+1}/E_k)[tr(C_k C_{k+1})-tr(C_k^2)].",
        "nonlinear_bound": "|M_N,k| <= sqrt(J_k(1-J_k)) L_k.",
        "neighbor_bound": "|tr(C_k(C_{k+1}-C_k))| <= sqrt(1-J_k)||C_{k+1}-C_k||_F.",
        "claim_boundary": "This audit checks the normalized matrix-chain algebra. The PDE step defining F_I and the exact viscous nesting is documented analytically; no uniform-k spacetime closure is claimed.",
    }


def write_md(d, path: Path):
    lines = [
        "# Derivative projective covariance-chain audit",
        "",
        f"Status: **{d['status']}**",
        "",
        f"Checks passed: **{d['passed']}/{d['total']}**",
        "",
        d["chain_identity"],
        "",
        d["nonlinear_bound"],
        "",
        d["neighbor_bound"],
        "",
        "## Level summaries",
        "",
    ]
    for i, r in enumerate(d["levels"]):
        lines.append(f"- k={i}: J=`{r['J']:.6g}`, r_k=`{r['r']:.6g}`, Delta_k=`{r['Delta']:.6g}`, Jdot error=`{r['Jdot_error']:.3e}`")
    lines += ["", "## Claim boundary", "", d["claim_boundary"], ""]
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", default="results")
    args = ap.parse_args()
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    d = run_checks()
    (out / "derivative_projective_covariance_chain_gate.json").write_text(json.dumps(d, indent=2), encoding="utf-8")
    write_md(d, out / "derivative_projective_covariance_chain_gate.md")
    print(f"Derivative projective covariance chain: {d['passed']}/{d['total']} checks passed")
    if d["passed"] != d["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
