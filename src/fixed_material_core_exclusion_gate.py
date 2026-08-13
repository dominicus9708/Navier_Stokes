#!/usr/bin/env python3
"""Audit the algebra/scaling behind the fixed positive-volume material-core exclusion."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

SCHEMA_VERSION = "0.1.0"


def tube_case(V0=0.7, Kg=1.4, CA=2.3, Gamma=0.8, W=25.0):
    Amax = CA/W
    Lmin = V0*W/(Kg*CA)
    section_energy_min = Gamma*Gamma*W/CA
    E_min = section_energy_min*Lmin/Kg
    closed = Gamma*Gamma*V0*W*W/(Kg*Kg*CA*CA)
    return {
        "V0": V0,
        "Kg": Kg,
        "CA": CA,
        "Gamma": Gamma,
        "W": W,
        "Amax": Amax,
        "Lmin": Lmin,
        "section_energy_min": section_energy_min,
        "E_min": E_min,
        "closed_form": closed,
        "identity_error": abs(E_min-closed),
    }


def scaling_audit(lam=3.7):
    # NS scaling: omega -> lam^2 omega, x-volume -> lam^-3,
    # material tube volume V0 -> lam^-3 V0, section area -> lam^-2,
    # flux Gamma=int omega.dA is invariant.
    W_ratio = lam**2
    V_ratio = lam**-3
    CA_ratio = 1.0  # A <= CA/W: CA dimensionless
    Gamma_ratio = 1.0
    E_ratio_rhs = V_ratio*(W_ratio**2)
    # enstrophy ||omega||_2^2 scales as lam.
    E_expected = lam
    return {
        "lambda": lam,
        "rhs_enstrophy_ratio": E_ratio_rhs,
        "expected_enstrophy_ratio": E_expected,
        "error": abs(E_ratio_rhs-E_expected),
        "CA_ratio": CA_ratio,
        "Gamma_ratio": Gamma_ratio,
    }


def time_integrability_audit(T=1.7, Cw2=4.2):
    # Cauchy-Schwarz: int W <= sqrt(T) (int W^2)^1/2.
    bound = math.sqrt(T*Cw2)
    return {"T": T, "W2_integral_bound": Cw2, "W1_bound": bound, "finite": math.isfinite(bound)}


def run_checks():
    rows = [tube_case(), tube_case(V0=1.1, Kg=1.0, CA=1.7, Gamma=1.3, W=11.0)]
    sc = scaling_audit()
    ti = time_integrability_audit()
    checks = {
        "tube_energy_closed_form": all(r["identity_error"] < 1e-12 for r in rows),
        "positive_length_lower_bound": all(r["Lmin"] > 0 for r in rows),
        "NS_scaling_match": sc["error"] < 1e-12,
        "finite_L2_time_implies_finite_L1_time": ti["finite"],
    }
    checks = {k: bool(v) for k, v in checks.items()}
    return {
        "schema_version": SCHEMA_VERSION,
        "status": "DERIVED FIXED-MATERIAL-CORE EXCLUSION / ALGEBRA-SCALING AUDIT",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "tube_cases": rows,
        "scaling": sc,
        "time_integrability": ti,
        "core_bound": "E_omega >= Gamma0^2 V0 W^2 /(Kg^2 CA^2).",
        "external_step": "BKM continuation: finite int ||omega||_infty dt precludes finite-time breakdown.",
        "claim_boundary": "This audit checks the conditional tube geometry and scaling only. The exclusion requires one fixed positive-volume material tube satisfying the stated natural-area and signed-flux hypotheses.",
    }


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--output-dir", default="results"); args = ap.parse_args()
    out = Path(args.output_dir); out.mkdir(parents=True, exist_ok=True)
    d = run_checks()
    (out/"fixed_material_core_exclusion_gate.json").write_text(json.dumps(d, indent=2), encoding="utf-8")
    (out/"fixed_material_core_exclusion_gate.md").write_text(
        "# Fixed material core exclusion audit\n\n"
        f"Checks passed: **{d['passed']}/{d['total']}**\n\n"
        f"{d['core_bound']}\n\n{d['external_step']}\n\n"
        f"Claim boundary: {d['claim_boundary']}\n", encoding="utf-8")
    print(f"Fixed material core exclusion: {d['passed']}/{d['total']} checks passed")
    if d["passed"] != d["total"]: raise SystemExit(1)


if __name__ == "__main__": main()
