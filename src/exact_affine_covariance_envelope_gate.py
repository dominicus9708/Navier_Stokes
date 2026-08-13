#!/usr/bin/env python3
"""Audit the exact fixed-purity affine strain/covariance coupling envelope."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

SCHEMA_VERSION = "0.1.0"


def envelope(eigs: np.ndarray, p: float) -> float:
    lam = np.sort(np.asarray(eigs, dtype=float))
    if abs(lam.sum()) > 1e-10:
        raise ValueError("strain eigenvalues must be trace free")
    s2 = float(np.dot(lam, lam))
    if s2 <= 0:
        return 0.0
    p0 = 1.0 / 3.0 + s2 / (9.0 * lam[0] ** 2)
    if p <= p0 + 1e-14:
        return math.sqrt(s2) * math.sqrt(max(0.0, p - 1.0 / 3.0))
    d = math.sqrt(max(0.0, 2.0 * p - 1.0))
    return 0.5 * (lam[1] + lam[2]) + 0.5 * (lam[2] - lam[1]) * d


def brute_aligned(eigs: np.ndarray, p: float, samples: int = 200000) -> float:
    """Brute force over c_i>=0, sum c=1 near the requested purity."""
    lam = np.sort(np.asarray(eigs, dtype=float))
    best = -1e99
    # Parameterize the circle in the sum=1 plane.
    center = np.ones(3) / 3.0
    u = np.array([1.0, -1.0, 0.0]) / math.sqrt(2.0)
    v = np.array([1.0, 1.0, -2.0]) / math.sqrt(6.0)
    radius = math.sqrt(max(0.0, p - 1.0 / 3.0))
    # c-center has Euclidean norm radius because sum(c_i-1/3)^2=p-1/3.
    for theta in np.linspace(0.0, 2.0 * math.pi, samples, endpoint=False):
        c = center + radius * (math.cos(theta) * u + math.sin(theta) * v)
        if c.min() >= -2e-5:
            best = max(best, float(np.dot(lam, c)))
    return best


def run_checks():
    cases = [
        np.array([-2.0, 1.0, 1.0]),
        np.array([-1.5, 0.4, 1.1]),
        np.array([-1.0, -0.2, 1.2]),
    ]
    purities = [1.0 / 3.0, 0.4, 0.5, 0.65, 0.8, 1.0]
    max_brute_error = 0.0
    for lam in cases:
        for p in purities:
            exact = envelope(lam, p)
            brute = brute_aligned(lam, p, samples=8000)
            max_brute_error = max(max_brute_error, max(0.0, brute - exact), abs(brute - exact))

    # Betchov-optimal special branch.
    a = 1.7
    lam = np.array([-2.0 * a, a, a])
    betchov_errors = []
    for J in [0.0, 0.1, 0.25, 0.49, 0.5]:
        p = 1.0 - J
        betchov_errors.append(abs(envelope(lam, p) - a))

    # At J=1/2, plane-isotropic covariance already saturates the affine coupling.
    C = np.diag([0.0, 0.5, 0.5])
    S = np.diag(lam)
    coupling = float(np.trace(S @ C))
    J = 1.0 - float(np.trace(C @ C))

    # Elementary top-eigenvalue cap at pure state.
    pure = envelope(np.array([-1.5, 0.4, 1.1]), 1.0)

    checks = {
        "brute_force_matches_piecewise_envelope": max_brute_error < 2e-3,
        "betchov_boundary_envelope_constant": max(betchov_errors) < 1e-12,
        "plane_isotropic_J_half": abs(J - 0.5) < 1e-12,
        "plane_isotropic_saturates_betchov_coupling": abs(coupling - a) < 1e-12,
        "pure_covariance_recovers_lambda_max": abs(pure - 1.1) < 1e-12,
    }
    checks = {k: bool(v) for k, v in checks.items()}
    return {
        "schema_version": SCHEMA_VERSION,
        "status": "EXACT AFFINE-COVARIANCE ENVELOPE / NUMERICAL ALGEBRA AUDIT",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "max_brute_error": max_brute_error,
        "betchov_example": {
            "a": a,
            "J_plane_isotropic": J,
            "coupling": coupling,
        },
        "statement": (
            "At fixed covariance purity, affine strain/covariance coupling has a piecewise exact envelope. "
            "For Betchov shape (-2a,a,a), every covariance supported in the extensional plane reaches the maximal coupling a, including J=1/2."
        ),
        "claim_boundary": (
            "This is finite-dimensional covariance optimization. It does not prove that a Navier-Stokes core can or cannot dynamically maintain the biaxial extensional-plane geometry."
        ),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", default="results")
    args = ap.parse_args()
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    d = run_checks()
    (out / "exact_affine_covariance_envelope_gate.json").write_text(json.dumps(d, indent=2), encoding="utf-8")
    (out / "exact_affine_covariance_envelope_gate.md").write_text(
        "# Exact affine covariance envelope audit\n\n"
        f"Status: **{d['status']}**\n\nChecks passed: **{d['passed']}/{d['total']}**\n\n"
        + d["statement"] + "\n\n## Claim boundary\n\n" + d["claim_boundary"] + "\n",
        encoding="utf-8",
    )
    print(f"Exact affine covariance envelope: {d['passed']}/{d['total']} checks passed")
    if d["passed"] != d["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
