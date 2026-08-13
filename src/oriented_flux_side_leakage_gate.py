#!/usr/bin/env python3
"""Audit the oriented-vorticity-flux side-leakage/persistence trichotomy.

The continuum lemma is documented in
notes/2026-08-13-oriented-flux-side-leakage-trichotomy.md.
This script checks exact benchmark identities and scale algebra only.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import sympy as sp

SCHEMA_VERSION = "0.1.0"


def symbolic_divergence_and_flux() -> dict:
    x, y, z, rho, a0, a1 = sp.symbols("x y z rho a0 a1", real=True)
    f = a0 + a1*z
    omega = sp.Matrix([-a1*x/2, -a1*y/2, f])
    div = sp.diff(omega[0], x) + sp.diff(omega[1], y) + sp.diff(omega[2], z)

    flux = sp.pi*rho**2*f
    dflux_dz = sp.diff(flux, z)
    # Radial side flux per unit axial length at radius rho.
    radial = -a1*rho/2
    side_per_length = 2*sp.pi*rho*radial

    return {
        "divergence": str(sp.simplify(div)),
        "divergence_zero": bool(sp.simplify(div) == 0),
        "flux": str(flux),
        "dflux_dz": str(sp.simplify(dflux_dz)),
        "negative_side_flux_per_length": str(sp.simplify(-side_per_length)),
        "flux_balance_match": bool(sp.simplify(dflux_dz + side_per_length) == 0),
    }


def leakage_benchmark(r=0.4, L=0.7, W=None) -> dict:
    if W is None:
        W = 1.0/(r*r)  # natural-scale normalization W r^2 = 1
    # f(z)=W(1-z/L), so a1=-W/L.
    a1 = -W/L

    # Off-axis energy in r<rho<2r, 0<z<L.
    annular_offaxis = (15.0*math.pi/8.0)*(a1*a1)*L*(r**4)

    # Coarea-select rho*=r, which is below the radial average because side energy ~rho^3.
    rho = r
    side_l2 = (math.pi/2.0)*(a1*a1)*(rho**3)*L
    coarea_average = annular_offaxis/r

    delta_flux = math.pi*(rho**2)*abs(a1)*L
    coarea_cauchy_lower = delta_flux**2/(4.0*math.pi*L)

    # The robust-loss formula with eta=1, kappa=pi, lambda=L/r.
    eta = 1.0
    kappa = math.pi
    lam = L/r
    normalized_actual = r*annular_offaxis
    normalized_lower = (eta*eta*kappa*kappa/(4.0*math.pi*lam))*((W*r*r)**2)

    return {
        "r": r,
        "L": L,
        "W": W,
        "Wr2": W*r*r,
        "annular_offaxis": annular_offaxis,
        "side_l2_at_r": side_l2,
        "coarea_average": coarea_average,
        "coarea_selection_margin": coarea_average-side_l2,
        "delta_flux_at_r": delta_flux,
        "coarea_cauchy_lower": coarea_cauchy_lower,
        "leakage_margin": annular_offaxis-coarea_cauchy_lower,
        "normalized_actual": normalized_actual,
        "normalized_lower": normalized_lower,
        "normalized_margin": normalized_actual-normalized_lower,
    }


def persistence_benchmark(r=0.4, N=6.0, W=None) -> dict:
    if W is None:
        W = 1.0/(r*r)
    L = N*r
    rho = 2.0*r
    flux = math.pi*(rho**2)*W
    exact_energy = math.pi*(rho**2)*L*(W**2)
    lower = L*(flux**2)/(4.0*math.pi*(r**2))
    normalized = r*exact_energy
    # Here kappa=4*pi because flux=(4*pi) W r^2.
    kappa = 4.0*math.pi
    normalized_formula = (kappa*kappa/(4.0*math.pi))*((W*r*r)**2)*N
    return {
        "r": r,
        "N": N,
        "L": L,
        "W": W,
        "flux": flux,
        "exact_energy": exact_energy,
        "persistence_lower": lower,
        "persistence_equality_error": abs(exact_energy-lower),
        "normalized_energy": normalized,
        "normalized_formula": normalized_formula,
        "normalized_equality_error": abs(normalized-normalized_formula),
    }


def radial_cancellation_benchmark(r=0.4, eta=0.6, W=None) -> dict:
    if W is None:
        W = 1.0/(r*r)
    # Core D_r has alpha=W.  The annulus D_2r\D_r has constant
    # alpha=-(eta/3)W, so it cancels the fraction eta of the core flux.
    core_flux = math.pi*(r**2)*W
    annulus_area = 3.0*math.pi*(r**2)
    alpha_annulus = -(eta/3.0)*W
    annulus_flux = annulus_area*alpha_annulus
    outer_flux = core_flux+annulus_flux
    negative_l1 = annulus_area*abs(alpha_annulus)
    negative_l2 = annulus_area*(alpha_annulus**2)

    kappa = math.pi
    l1_lower = eta*kappa*W*(r**2)
    l2_lower = (eta*eta*kappa*kappa/(3.0*math.pi))*(W**2)*(r**2)
    return {
        "r": r,
        "eta": eta,
        "W": W,
        "core_flux": core_flux,
        "annulus_flux": annulus_flux,
        "outer_flux": outer_flux,
        "target_outer_flux": (1.0-eta)*core_flux,
        "negative_l1": negative_l1,
        "negative_l1_lower": l1_lower,
        "negative_l2": negative_l2,
        "negative_l2_lower": l2_lower,
        "outer_flux_error": abs(outer_flux-(1.0-eta)*core_flux),
        "l1_error": abs(negative_l1-l1_lower),
        "l2_error": abs(negative_l2-l2_lower),
    }


def run_checks() -> dict:
    sym = symbolic_divergence_and_flux()
    leak = leakage_benchmark()
    persist = persistence_benchmark()
    cancel = radial_cancellation_benchmark()

    checks = {
        "benchmark_divergence_free": sym["divergence_zero"],
        "exact_flux_side_balance": sym["flux_balance_match"],
        "coarea_radius_selection": leak["coarea_selection_margin"] >= -1e-12,
        "leakage_volume_bound": leak["leakage_margin"] >= -1e-12,
        "natural_scale_leakage_bound": leak["normalized_margin"] >= -1e-12,
        "persistent_tube_cauchy_equality": persist["persistence_equality_error"] < 1e-12,
        "persistent_natural_length_scaling": persist["normalized_equality_error"] < 1e-12,
        "radial_cancellation_flux": cancel["outer_flux_error"] < 1e-12,
        "radial_cancellation_l1": cancel["l1_error"] < 1e-12,
        "radial_cancellation_l2": cancel["l2_error"] < 1e-12,
    }
    checks = {k: bool(v) for k, v in checks.items()}

    return {
        "schema_version": SCHEMA_VERSION,
        "status": "DERIVED ORIENTED-FLUX SIDE-LEAKAGE TRICHOTOMY / COMPUTATIONAL ALGEBRA AUDIT",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "symbolic": sym,
        "leakage": leak,
        "persistence": persist,
        "radial_cancellation": cancel,
        "trichotomy": [
            "robust short-range flux loss -> off-axis L2 projective cost",
            "long flux persistence -> scale-invariant enstrophy occupancy linear in L/r",
            "radial flux cancellation -> opposite-polarity axial population",
        ],
        "claim_boundary": (
            "The audit verifies exact benchmark and scale algebra.  It does not prove a time-integrated "
            "bound on the dimensionless persistence length L/r for arbitrary Navier-Stokes solutions."
        ),
    }


def write_md(d: dict, path: Path) -> None:
    lines = [
        "# Oriented-flux side-leakage audit",
        "",
        f"Status: **{d['status']}**",
        "",
        f"Checks passed: **{d['passed']}/{d['total']}**",
        "",
        "## Trichotomy",
        "",
    ]
    for item in d["trichotomy"]:
        lines.append(f"- {item}")
    lines += [
        "",
        "## Natural-scale benchmark",
        "",
        f"- leakage normalized margin: `{d['leakage']['normalized_margin']:.6g}`",
        f"- persistent length N: `{d['persistence']['N']:.6g}`",
        f"- persistent normalized energy: `{d['persistence']['normalized_energy']:.6g}`",
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
    (out/"oriented_flux_side_leakage_gate.json").write_text(json.dumps(d, indent=2), encoding="utf-8")
    write_md(d, out/"oriented_flux_side_leakage_gate.md")
    print(f"Oriented-flux side-leakage: {d['passed']}/{d['total']} checks passed")
    if d["passed"] != d["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
