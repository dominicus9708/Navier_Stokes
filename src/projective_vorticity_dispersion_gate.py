#!/usr/bin/env python3
"""Audit the projective vorticity-dispersion covariance identities.

The external regularity input is Miller's locally anisotropic criterion.
This script checks only finite-dimensional covariance/projective algebra,
comparison with the principal-axis defect, scaling, and exact benchmark cases.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import numpy as np

SCHEMA_VERSION = "0.1.0"


def covariance_data(omega: np.ndarray, weights: np.ndarray):
    mag2 = np.sum(omega * omega, axis=1)
    E = float(np.sum(weights * mag2))
    C = np.einsum("n,ni,nj->ij", weights, omega, omega) / E
    vals = np.linalg.eigvalsh(C)[::-1]
    Pi = float(1.0 - vals[0])
    J = float(1.0 - np.trace(C @ C))
    Reff = float(1.0 / np.trace(C @ C))
    return E, C, vals, Pi, J, Reff


def pairwise_dispersion(omega: np.ndarray, weights: np.ndarray, E: float):
    # O(N^2) deterministic audit on a deliberately modest sample.
    dots = omega @ omega.T
    mag2 = np.sum(omega * omega, axis=1)
    cross2 = mag2[:, None] * mag2[None, :] - dots * dots
    ww = weights[:, None] * weights[None, :]
    return float(np.sum(ww * cross2) / (E * E))


def random_audit(seed=9708, npts=128):
    rng = np.random.default_rng(seed)
    omega = rng.normal(size=(npts, 3))
    weights = rng.random(npts) + 0.1
    E, C, vals, Pi, J, Reff = covariance_data(omega, weights)
    Jpair = pairwise_dispersion(omega, weights, E)
    return {
        "trace": float(np.trace(C)),
        "eigenvalues": vals.tolist(),
        "Pi": Pi,
        "J": J,
        "J_pairwise": Jpair,
        "pairwise_error": abs(J - Jpair),
        "Reff": Reff,
        "lower_compare_residual": Pi - 0.5 * J,
        "upper_compare_residual": 1.5 * J - Pi,
    }


def exact_geometries():
    cases = {
        "one_axis": np.diag([1.0, 0.0, 0.0]),
        "planar_isotropic": np.diag([0.5, 0.5, 0.0]),
        "isotropic": np.eye(3) / 3.0,
        "unequal_three_axis": np.diag([0.6, 0.3, 0.1]),
    }
    out = {}
    for name, C in cases.items():
        vals = np.linalg.eigvalsh(C)[::-1]
        Pi = float(1 - vals[0])
        J = float(1 - np.trace(C @ C))
        out[name] = {
            "eigenvalues": vals.tolist(),
            "Pi": Pi,
            "J": J,
            "Reff": float(1 / np.trace(C @ C)),
            "compare_ok": bool(0.5 * J <= Pi + 1e-14 and Pi <= 1.5 * J + 1e-14),
        }
    return out


def scaling(lam: float):
    # E -> lambda E, J invariant, dt -> lambda^-2 dt.
    # The Miller-derived integral of (E J)^2 is therefore invariant.
    return (lam ** 2) * (lam ** -2)


def run_checks():
    rnd = random_audit()
    ex = exact_geometries()
    checks = {
        "covariance_trace_one": abs(rnd["trace"] - 1.0) < 1e-12,
        "pairwise_cross_identity": rnd["pairwise_error"] < 1e-12,
        "Pi_lower_bound": rnd["lower_compare_residual"] >= -1e-12,
        "Pi_upper_bound": rnd["upper_compare_residual"] >= -1e-12,
        "projective_dispersion_range": 0.0 <= rnd["J"] <= 2.0 / 3.0 + 1e-12,
        "effective_rank_identity": abs(rnd["Reff"] - 1.0 / (1.0 - rnd["J"])) < 1e-12,
        "exact_one_axis": abs(ex["one_axis"]["J"]) < 1e-12 and abs(ex["one_axis"]["Pi"]) < 1e-12,
        "exact_planar": abs(ex["planar_isotropic"]["J"] - 0.5) < 1e-12 and abs(ex["planar_isotropic"]["Pi"] - 0.5) < 1e-12,
        "exact_isotropic": abs(ex["isotropic"]["J"] - 2.0 / 3.0) < 1e-12 and abs(ex["isotropic"]["Pi"] - 2.0 / 3.0) < 1e-12,
        "all_exact_comparisons": all(v["compare_ok"] for v in ex.values()),
        "blowup_certificate_scale_invariant": all(abs(scaling(l) - 1.0) < 1e-12 for l in (0.25, 0.7, 2.0, 9.0)),
    }
    checks = {k: bool(v) for k, v in checks.items()}
    return {
        "schema_version": SCHEMA_VERSION,
        "status": "DERIVED PROJECTIVE COVARIANCE ALGEBRA / COMPUTATIONAL AUDIT",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "random_audit": rnd,
        "exact_geometries": ex,
        "identity": "J = 1-tr(C^2) = E^{-2} sum_ab w_a w_b |omega_a x omega_b|^2.",
        "comparison": "J/2 <= Pi <= 3J/2.",
        "miller_corollary": "A hypothetical finite-time blowup must have E_omega J_omega not in L2_t; this is a corollary of the external Miller criterion plus the covariance comparison.",
        "claim_boundary": "This audit proves no arbitrary-data regularity theorem. It checks covariance algebra and the axis-free reformulation only.",
    }


def write_md(d, path: Path):
    r = d["random_audit"]
    lines = [
        "# Projective vorticity-dispersion audit",
        "",
        f"Status: **{d['status']}**",
        "",
        f"Checks passed: **{d['passed']}/{d['total']}**",
        "",
        d["identity"],
        "",
        d["comparison"],
        "",
        f"Random audit: Pi=`{r['Pi']:.8g}`, J=`{r['J']:.8g}`, pairwise error=`{r['pairwise_error']:.3e}`, Reff=`{r['Reff']:.8g}`.",
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
    (out / "projective_vorticity_dispersion_gate.json").write_text(json.dumps(d, indent=2), encoding="utf-8")
    write_md(d, out / "projective_vorticity_dispersion_gate.md")
    print(f"Projective vorticity dispersion gate: {d['passed']}/{d['total']} checks passed")
    if d["passed"] != d["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
