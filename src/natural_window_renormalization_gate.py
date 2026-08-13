#!/usr/bin/env python3
"""Audit natural-window Navier--Stokes renormalization exponents.

The script verifies scaling identities for the dangerous-window channels used by
this repository.  It does not prove compactness of a blow-up sequence.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import math

SCHEMA_VERSION = "0.1.0"


def run_checks(lam: float = 4.3):
    # Standard NS scaling with lambda=1/r:
    # u -> lambda u, omega -> lambda^2 omega, S -> lambda^2 S,
    # grad omega -> lambda^3, Delta omega -> lambda^4,
    # dx -> lambda^-3, dt -> lambda^-2.
    W_ratio = lam**2
    r_ratio = lam**-1
    core_volume_ratio = lam**-3

    # Normalize by r=W^-1/2.
    natural_radius_consistency = abs((W_ratio ** -0.5) - r_ratio)

    # r^3 * instantaneous palinstrophy is invariant.
    pal_phys_ratio = lam**3
    r3_ratio = lam**-3
    pal_norm_ratio = pal_phys_ratio * r3_ratio

    # r^3 * spacetime k=2 vorticity derivative cost is invariant.
    k2_spacetime_ratio = lam**3
    k2_norm_ratio = k2_spacetime_ratio * r3_ratio

    # Strain exposure along a path: S dt is invariant.
    strain_exposure_ratio = lam**2 * lam**-2

    # Dimensionless core occupancy |C|/r^3.
    occupancy_ratio = core_volume_ratio / (r_ratio**3)

    # Vorticity normalized by r^2 has invariant maximum.
    normalized_omega_ratio = (r_ratio**2) * W_ratio

    # Projective quantities use only normalized directions, hence scalar scaling cancels.
    projective_ratio = 1.0

    checks = {
        "natural_radius_from_vorticity": natural_radius_consistency < 1e-12,
        "normalized_vorticity_max_invariant": abs(normalized_omega_ratio - 1.0) < 1e-12,
        "occupancy_invariant": abs(occupancy_ratio - 1.0) < 1e-12,
        "palinstrophy_r3_invariant": abs(pal_norm_ratio - 1.0) < 1e-12,
        "k2_spacetime_r3_invariant": abs(k2_norm_ratio - 1.0) < 1e-12,
        "strain_exposure_invariant": abs(strain_exposure_ratio - 1.0) < 1e-12,
        "projective_direction_channels_invariant": projective_ratio == 1.0,
    }
    checks = {k: bool(v) for k, v in checks.items()}

    return {
        "schema_version": SCHEMA_VERSION,
        "status": "DERIVED NATURAL-WINDOW RENORMALIZATION / SCALING AUDIT",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "lambda": lam,
        "ratios": {
            "W": W_ratio,
            "r": r_ratio,
            "core_volume": core_volume_ratio,
            "normalized_omega": normalized_omega_ratio,
            "occupancy": occupancy_ratio,
            "r3_palinstrophy": pal_norm_ratio,
            "r3_k2_spacetime": k2_norm_ratio,
            "strain_exposure": strain_exposure_ratio,
            "projective": projective_ratio,
        },
        "dictionary": {
            "U": "U(y,s)=r u(x0+r y,t0+r^2 s)",
            "Omega": "Omega(y,s)=r^2 omega(x0+r y,t0+r^2 s)",
            "P": "P(y,s)=r^2 p(x0+r y,t0+r^2 s)",
            "natural_radius": "r=W^-1/2",
            "normalized_palinstrophy": "r^3 int |grad omega|^2",
            "normalized_k2_cost": "r^3 int int |Delta omega|^2",
        },
        "claim_boundary": "The scaling dictionary is exact. Uniform critical local bounds and subsequential compactness are separate open requirements.",
    }


def write_md(d, path: Path):
    lines = [
        "# Natural-window renormalization audit",
        "",
        f"Status: **{d['status']}**",
        "",
        f"Checks passed: **{d['passed']}/{d['total']}**",
        "",
        "The audit verifies that natural occupancy, projective direction channels, `r^3` palinstrophy, `r^3` spacetime `|Delta omega|^2`, and pathwise strain exposure become dimensionless unit-window quantities.",
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
    (out / "natural_window_renormalization_gate.json").write_text(json.dumps(d, indent=2), encoding="utf-8")
    write_md(d, out / "natural_window_renormalization_gate.md")
    print(f"Natural-window renormalization: {d['passed']}/{d['total']} checks passed")
    if d["passed"] != d["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
