#!/usr/bin/env python3
"""Exact/algebraic audit of the vorticity occupancy -> line-sparseness bridge.

No Navier-Stokes regularity theorem is proved here.  The external geometric
criterion is treated as an anchor; this script checks only the repository's
geometry, scale bookkeeping, and derived threshold arithmetic.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


SCHEMA_VERSION = "0.1.0"


def centered_ball_example(delta: float) -> dict:
    # In B_r, take S=B_{delta r}.  Every center line intersects S in length
    # 2 delta r and the volume fraction is delta^3, so the geometric lemma is sharp.
    rho_vol = delta**3
    rho_line = delta
    return {
        "delta": delta,
        "rho_volume": rho_vol,
        "rho_volume_cuberoot": rho_vol**(1.0/3.0),
        "rho_line_every_direction": rho_line,
        "sharp_error": abs(rho_line-rho_vol**(1.0/3.0)),
    }


def scaling_audit(lam: float) -> dict:
    # NS scaling: x -> x/lambda, t -> t/lambda^2,
    # omega -> lambda^2 omega.
    # int |omega|^2 dx -> lambda; r -> r/lambda.
    local_enstrophy_factor = (lam**-1)*lam

    # W=||omega||_infty -> lambda^2 W, hence W^(1/2) -> lambda.
    # ||omega||_2^2 dt -> lambda * lambda^-2 = lambda^-1.
    z_window_factor = lam*(lam*lam**-2)

    # Natural vorticity radius W^-1/2 scales like lambda^-1.
    natural_radius_factor = (lam**2)**-0.5
    return {
        "lambda": lam,
        "local_enstrophy_factor": local_enstrophy_factor,
        "z_window_factor": z_window_factor,
        "natural_radius_factor": natural_radius_factor,
        "expected_radius_factor": lam**-1,
    }


def thresholds(delta=0.4, d0=2.0, alpha=1.0) -> dict:
    # Derived constants from the repository notes.
    K = (math.pi/6.0)*delta**3*d0**(-(2.0*alpha+6.0))
    Zcrit = (math.pi/8.0)*delta**3*d0**(-(2.0*alpha+8.0))
    # Since |I_t|=3/(4 d0^2 W), the averaging bridge says
    # Z < (3/(4 d0^2))*K.  Verify it equals the stated Zcrit.
    Z_from_K = (3.0/(4.0*d0*d0))*K
    return {
        "delta": delta,
        "d0": d0,
        "alpha": alpha,
        "K_packing": K,
        "Z_critical": Zcrit,
        "Z_from_K": Z_from_K,
        "constant_identity_error": abs(Zcrit-Z_from_K),
    }


def run_checks() -> dict:
    examples = [centered_ball_example(d) for d in (0.2, 0.5, 0.8)]
    scales = [scaling_audit(lam) for lam in (0.5, 2.0, 7.0)]
    th = thresholds()

    # Strict implication test: rho_vol < delta^3 => rho_vol^(1/3) < delta.
    delta_test = 0.35
    rho_test = 0.5*delta_test**3

    checks = {
        "centered_ball_sharp_examples": all(e["sharp_error"] < 1e-12 for e in examples),
        "strict_volume_to_line_implication": rho_test**(1.0/3.0) < delta_test,
        "local_enstrophy_scale_invariant": all(abs(s["local_enstrophy_factor"]-1.0) < 1e-12 for s in scales),
        "window_dissipation_scale_invariant": all(abs(s["z_window_factor"]-1.0) < 1e-12 for s in scales),
        "natural_radius_scaling": all(abs(s["natural_radius_factor"]-s["expected_radius_factor"]) < 1e-12 for s in scales),
        "packing_constant_positive": th["K_packing"] > 0.0,
        "window_threshold_positive": th["Z_critical"] > 0.0,
        "window_threshold_constant_identity": th["constant_identity_error"] < 1e-15,
    }
    checks = {k: bool(v) for k, v in checks.items()}

    return {
        "schema_version": SCHEMA_VERSION,
        "status": "DERIVED GEOMETRIC/SCALING BRIDGE + COMPUTATIONAL AUDIT",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "sharp_centered_ball_examples": examples,
        "scaling_examples": scales,
        "threshold_example": th,
        "geometry_statement": "inf_d rho_line(d) <= rho_volume^(1/3); equality is attained by a concentric active ball.",
        "critical_local_enstrophy": "W_r = r * int_{B_r} |omega|^2 dx is NS-scale invariant.",
        "critical_window_channel": "Z_omega(t)=||omega(t)||_infty^(1/2) * int_{I_t} ||omega(s)||_2^2 ds is NS-scale invariant.",
        "claim_boundary": "The script audits derived geometry and scaling only. The final regularity implication belongs to the external vorticity sparseness theorem and is not reproduced by this computation."
    }


def write_md(d, path: Path):
    lines = [
        "# Vorticity occupancy / sparseness gate audit", "",
        f"Status: **{d['status']}**", "",
        f"Checks passed: **{d['passed']}/{d['total']}**", "",
        "## Sharp geometry control", "",
        "For a concentric active ball of relative radius `delta`, volume occupancy is `delta^3` and every center-line occupancy is `delta`, so the bound `rho_line,min <= rho_vol^(1/3)` is sharp.", "",
        "## Critical channels", "",
        "- `W_r = r int_{B_r}|omega|^2`: scale invariant.",
        "- `Z_omega = ||omega(t)||_infty^(1/2) int_{I_t}||omega(s)||_2^2 ds`: scale invariant.", "",
        "## Claim boundary", "", d["claim_boundary"], ""
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--output-dir", default="results")
    args = ap.parse_args(); out = Path(args.output_dir); out.mkdir(parents=True, exist_ok=True)
    d = run_checks()
    (out/"vorticity_occupancy_sparseness_gate.json").write_text(json.dumps(d, indent=2), encoding="utf-8")
    write_md(d, out/"vorticity_occupancy_sparseness_gate.md")
    print(f"Vorticity occupancy/sparseness gate: {d['passed']}/{d['total']} checks passed")
    if d["passed"] != d["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
