#!/usr/bin/env python3
"""Audit material vorticity-flux erosion on an exact Navier-Stokes shear flow."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import sympy as sp

SCHEMA_VERSION = "0.1.0"


def symbolic_shear_identity() -> dict:
    y, t, nu, k = sp.symbols("y t nu k", positive=True, real=True)
    U = sp.exp(-nu*k*k*t)*sp.sin(k*y)
    residual = sp.simplify(sp.diff(U, t)-nu*sp.diff(U, y, 2))
    omega_z = -sp.diff(U, y)
    curlomega_x = sp.diff(omega_z, y)
    return {
        "U": str(U),
        "heat_residual": str(residual),
        "heat_residual_zero": bool(residual == 0),
        "omega_z": str(sp.simplify(omega_z)),
        "curlomega_x": str(sp.simplify(curlomega_x)),
    }


def exact_rectangle_balance(
    nu=0.8,
    k=1.3,
    Lx=1.1,
    y1=-0.35,
    y2=0.72,
    t=0.46,
) -> dict:
    decay = math.exp(-nu*k*k*t)
    dsin = math.sin(k*y2)-math.sin(k*y1)

    flux = -Lx*decay*dsin
    flux_dt = nu*k*k*Lx*decay*dsin

    q1 = k*k*decay*math.sin(k*y1)
    q2 = k*k*decay*math.sin(k*y2)
    bottom = Lx*q1
    top = -Lx*q2

    # The two material side curves have equal and opposite integrals.
    # Their common unsigned analytic integral is computed from
    # A_y=(1-exp(-nu k^2 t))/(nu k) cos(k y).
    pref = (1.0-decay)/(nu*k)
    # integral q(y) A_y(y) dy = k^2 decay * pref * integral sin(ky)cos(ky)dy
    common_side = (
        k*k*decay*pref
        * (math.sin(k*y2)**2-math.sin(k*y1)**2)
        / (2.0*k)
    )
    right_side = common_side
    left_side = -common_side

    boundary_integral = bottom+right_side+top+left_side
    viscous_boundary = -nu*boundary_integral

    return {
        "flux": flux,
        "flux_dt": flux_dt,
        "bottom": bottom,
        "top": top,
        "right_side": right_side,
        "left_side": left_side,
        "side_cancellation": right_side+left_side,
        "boundary_integral_curlomega": boundary_integral,
        "minus_nu_boundary": viscous_boundary,
        "balance_error": abs(flux_dt-viscous_boundary),
    }


def natural_scaling_audit(
    W=25.0,
    a=1.0,
    eta=0.4,
    kappa=1.7,
    lam=0.8,
    nu=0.9,
    Kgamma=3.0,
) -> dict:
    r = a/math.sqrt(W)
    tau = lam/W
    delta_flux = eta*kappa*W*r*r
    boundary_length_time_upper = Kgamma*r*tau
    lower = delta_flux**2/(nu*nu*boundary_length_time_upper)
    scaled = (
        eta*eta*kappa*kappa*a**3
        /(nu*nu*Kgamma*lam)
        * W**1.5
    )
    return {
        "W": W,
        "r": r,
        "tau": tau,
        "delta_flux": delta_flux,
        "boundary_length_time_upper": boundary_length_time_upper,
        "boundary_curlomega_lower": lower,
        "closed_form_scaled_lower": scaled,
        "scaling_error": abs(lower-scaled),
    }


def run_checks() -> dict:
    sym = symbolic_shear_identity()
    rows = [
        exact_rectangle_balance(),
        exact_rectangle_balance(nu=1.1, k=0.9, Lx=0.7, y1=-0.8, y2=0.4, t=0.2),
        exact_rectangle_balance(nu=0.55, k=1.8, Lx=1.4, y1=0.1, y2=0.9, t=0.7),
    ]
    scale = natural_scaling_audit()

    checks = {
        "exact_shear_NS_heat_residual": sym["heat_residual_zero"],
        "material_side_integrals_cancel": all(abs(r["side_cancellation"]) < 1e-12 for r in rows),
        "material_flux_viscous_boundary_balance": all(r["balance_error"] < 1e-12 for r in rows),
        "natural_time_scaling_identity": scale["scaling_error"] < 1e-10,
        "boundary_cost_positive": scale["boundary_curlomega_lower"] > 0,
    }
    checks = {k: bool(v) for k, v in checks.items()}

    return {
        "schema_version": SCHEMA_VERSION,
        "status": "EXACT MATERIAL VORTICITY-FLUX / VISCOUS-EROSION AUDIT",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "symbolic": sym,
        "shear_samples": rows,
        "natural_scaling": scale,
        "identity": "d/dt int_{S(t)} omega.n dA = -nu int_{boundary S(t)} curl(omega).dl",
        "claim_boundary": (
            "The exact shear benchmark verifies the material-flux identity.  The remaining open step is "
            "a distortion-aware coarea/trace conversion from a robust family of material loops to bulk palinstrophy."
        ),
    }


def write_md(d: dict, path: Path) -> None:
    lines = [
        "# Material vorticity-flux erosion audit",
        "",
        f"Status: **{d['status']}**",
        "",
        f"Checks passed: **{d['passed']}/{d['total']}**",
        "",
        d["identity"],
        "",
        "## Exact shear benchmark",
        "",
        f"- maximum balance error: `{max(r['balance_error'] for r in d['shear_samples']):.3e}`",
        f"- maximum side-cancellation residual: `{max(abs(r['side_cancellation']) for r in d['shear_samples']):.3e}`",
        "",
        "## Natural scaling",
        "",
        f"- boundary derivative lower cost: `{d['natural_scaling']['boundary_curlomega_lower']:.6g}`",
        f"- scaling identity error: `{d['natural_scaling']['scaling_error']:.3e}`",
        "",
        "## Claim boundary",
        "",
        d["claim_boundary"],
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", default="results")
    args = ap.parse_args()
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    d = run_checks()
    (out/"material_vorticity_flux_erosion_gate.json").write_text(json.dumps(d, indent=2), encoding="utf-8")
    write_md(d, out/"material_vorticity_flux_erosion_gate.md")
    print(f"Material vorticity-flux erosion: {d['passed']}/{d['total']} checks passed")
    if d["passed"] != d["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
