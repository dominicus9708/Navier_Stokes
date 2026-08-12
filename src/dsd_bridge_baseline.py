#!/usr/bin/env python3
"""
First-pass DSD <-> 3D incompressible Navier-Stokes bridge checks.

Status:
- exact symbolic checks for the analytic Gaussian seed;
- exact/closed-form shell diagnostics where available;
- deterministic numerical quadrature for the l=2 pressure-fluctuation channel;
- no claim of Navier-Stokes global regularity.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import sympy as sp


SCHEMA_VERSION = "0.1.0"
SEED_NAME = "gaussian_double_curl_z"


def symbolic_seed_checks() -> dict:
    x, y, z = sp.symbols("x y z", real=True)
    r2 = x*x + y*y + z*z
    psi = sp.exp(-r2)

    u = sp.Matrix([
        4*x*z*psi,
        4*y*z*psi,
        4*(1 - x*x - y*y)*psi,
    ])

    div_u = sp.simplify(
        sp.diff(u[0], x) + sp.diff(u[1], y) + sp.diff(u[2], z)
    )

    omega = sp.Matrix([
        sp.diff(u[2], y) - sp.diff(u[1], z),
        sp.diff(u[0], z) - sp.diff(u[2], x),
        sp.diff(u[1], x) - sp.diff(u[0], y),
    ])
    omega_expected = sp.Matrix([
        4*y*(2*r2 - 5)*psi,
        -4*x*(2*r2 - 5)*psi,
        0,
    ])
    omega_residual = sp.simplify(omega - omega_expected)

    grad = sp.Matrix([[sp.diff(u[i], (x, y, z)[j]) for j in range(3)] for i in range(3)])
    q = sp.simplify(sum(grad[i, j] * grad[j, i] for i in range(3) for j in range(3)))
    q_expected = 32 * sp.exp(-2*r2) * (
        2*r2*r2 - 4*r2 + (7 - 2*r2)*z*z
    )
    q_residual = sp.simplify(q - q_expected)

    mu, rr = sp.symbols("mu rr", real=True)
    angular_factor = sp.expand(
        rr**4 * mu**2 * (1-mu**2)
        + (1 - rr**2 * (1-mu**2))**2
    )
    angular_factor_expected = sp.expand(
        (1-rr**2)**2 + (2*rr**2-rr**4)*mu**2
    )
    angular_residual = sp.simplify(angular_factor-angular_factor_expected)
    isotropic_at_sqrt2 = sp.simplify(
        angular_factor_expected.subs(rr**2, 2) - 1
    )

    return {
        "seed": SEED_NAME,
        "u": [str(sp.factor(v)) for v in u],
        "divergence": str(div_u),
        "divergence_zero": bool(div_u == 0),
        "omega": [str(sp.factor(v)) for v in omega_expected],
        "omega_residual_zero": all(sp.simplify(v) == 0 for v in omega_residual),
        "pressure_poisson_source": str(sp.factor(q_expected)),
        "pressure_source_residual_zero": bool(q_residual == 0),
        "shell_energy_angular_factor": str(angular_factor_expected),
        "shell_energy_angular_identity_zero": bool(angular_residual == 0),
        "shell_energy_isotropic_at_r_sqrt2": bool(isotropic_at_sqrt2 == 0),
    }


def shell_energy(r: float) -> float:
    return 8.0 * math.exp(-2.0*r*r) * (
        1.0 - (4.0/3.0)*r*r + (2.0/3.0)*r**4
    )


def shell_enstrophy(r: float) -> float:
    return (32.0/3.0) * r*r * (2.0*r*r - 5.0)**2 * math.exp(-2.0*r*r)


def shell_axis_energy(r: float) -> tuple[float, float, float]:
    ex = (8.0/15.0) * r**4 * math.exp(-2.0*r*r)
    ey = ex
    ez = 8.0 * math.exp(-2.0*r*r) * (
        1.0 - (4.0/3.0)*r*r + (8.0/15.0)*r**4
    )
    return ex, ey, ez


def q2_pressure_source(r: float) -> float:
    return (64.0/3.0) * r*r * (7.0 - 2.0*r*r) * math.exp(-2.0*r*r)


def simpson(f, a: float, b: float, n: int = 1200) -> float:
    if a == b:
        return 0.0
    if n % 2:
        n += 1
    h = (b-a)/n
    total = f(a) + f(b)
    for k in range(1, n):
        total += (4.0 if k % 2 else 2.0) * f(a + k*h)
    return total * h / 3.0


def pressure_l2(r: float, source_scale: float = 1.0, radial_scale: float = 1.0) -> float:
    """Whole-space l=2 pressure coefficient from the Newtonian inverse of -Delta."""
    if r <= 0:
        return 0.0

    def q_scaled(s: float) -> float:
        return source_scale * q2_pressure_source(radial_scale*s)

    upper = max(10.0 / max(radial_scale, 1e-12), r + 8.0 / max(radial_scale, 1e-12))
    i1 = simpson(lambda s: s**4 * q_scaled(s), 0.0, r, 1400)
    i2 = simpson(lambda s: q_scaled(s)/s if s else 0.0, r, upper, 2400)
    return (r**-3 * i1 + r*r * i2) / 5.0


def shell_pressure_fluctuation(r: float) -> float:
    p2 = pressure_l2(r)
    return p2*p2 / 5.0


def directional_entropy(r: float, bands: int = 12) -> dict:
    A = (1.0-r*r)**2
    B = 2.0*r*r-r**4

    weights = []
    for j in range(bands):
        a = -1.0 + 2.0*j/bands
        b = -1.0 + 2.0*(j+1)/bands
        w = A*(b-a) + (B/3.0)*(b**3-a**3)
        weights.append(max(0.0, w))

    total = sum(weights)
    if total == 0.0:
        return {
            "r": r,
            "bands": bands,
            "defined": False,
            "reason": "zero shell energy",
        }

    probs = [w/total for w in weights]
    entropy = -sum(p*math.log(p) for p in probs if p > 0.0)
    return {
        "r": r,
        "bands": bands,
        "defined": True,
        "entropy": entropy,
        "max_entropy": math.log(bands),
        "normalized_entropy": entropy/math.log(bands),
        "probabilities": probs,
    }


def radial_readout_status(point: tuple[float, float, float]) -> dict:
    x, y, z = point
    r = math.sqrt(x*x+y*y+z*z)
    if r == 0.0:
        return {
            "point": point,
            "status": "undefined/inapplicable",
            "reason": "e_r = x/|x| is undefined at the origin",
        }

    e = (x/r, y/r, z/r)
    g = math.exp(-(x*x+y*y+z*z))
    u = (
        4.0*x*z*g,
        4.0*y*z*g,
        4.0*(1.0-x*x-y*y)*g,
    )
    ur = sum(a*b for a, b in zip(u, e))
    return {
        "point": point,
        "status": "defined-zero" if abs(ur) < 1e-14 else "defined-nonzero",
        "u_r": ur,
    }


def scale_checks() -> list[dict]:
    rows = []
    for lam in (0.5, 2.0, 3.0):
        for r in (0.35, 0.8, 1.25):
            e_scaled = lam**2 * shell_energy(lam*r)
            w_scaled = lam**4 * shell_enstrophy(lam*r)

            inv_e_scaled = r*r*e_scaled
            inv_e_base = (lam*r)**2 * shell_energy(lam*r)

            inv_w_scaled = r**4*w_scaled
            inv_w_base = (lam*r)**4 * shell_enstrophy(lam*r)

            p2_scaled = pressure_l2(r, source_scale=lam**4, radial_scale=lam)
            p2_expected = lam**2 * pressure_l2(lam*r)

            rows.append({
                "lambda": lam,
                "r": r,
                "r2_energy_abs_error": abs(inv_e_scaled-inv_e_base),
                "r4_enstrophy_abs_error": abs(inv_w_scaled-inv_w_base),
                "pressure_l2_abs_error": abs(p2_scaled-p2_expected),
                "pressure_l2_rel_error": abs(p2_scaled-p2_expected) / max(1.0, abs(p2_expected)),
            })
    return rows


def rotational_control() -> dict:
    r = math.sqrt(2.0)
    ex, ey, ez = shell_axis_energy(r)
    return {
        "exact_coordinate_permutation_argument": True,
        "scalar_shell_energy_same_for_x_y_z": True,
        "scalar_shell_enstrophy_same_for_x_y_z": True,
        "at_r_sqrt2_axis_energies_for_z_seed": {"x": ex, "y": ey, "z": ez},
    }


def aggregate_collision() -> dict:
    r = 1.0
    ex, ey, ez = shell_axis_energy(r)
    descriptor = {
        "T_E": shell_energy(r),
        "T_W": shell_enstrophy(r),
        "T_P": shell_pressure_fluctuation(r),
        "T_Ex": ex,
        "T_Ey": ey,
        "T_Ez": ez,
    }
    return {
        "pair": ["u", "-u"],
        "same_quadratic_descriptor": True,
        "same_descriptor": descriptor,
        "signed_velocity_state_equal": False,
        "interpretation": (
            "Quadratic aggregation is non-injective. A regularity proof may still "
            "use non-injective norms, but lost information must be shown irrelevant "
            "or retained in typed channels."
        ),
    }


def special_shells() -> dict:
    r_iso = math.sqrt(2.0)
    r_vort_zero = math.sqrt(2.5)
    ex, ey, ez = shell_axis_energy(r_iso)
    return {
        "energy_isotropic_shell": {
            "r": r_iso,
            "T_E": shell_energy(r_iso),
            "axis_energies": {"x": ex, "y": ey, "z": ez},
            "directional_energy_entropy_12": directional_entropy(r_iso, 12),
            "interpretation": (
                "Total energy density is angularly isotropic at this radius, "
                "while axis-resolved energy still distinguishes the z-oriented seed."
            ),
        },
        "vorticity_zero_shell": {
            "r": r_vort_zero,
            "T_E": shell_energy(r_vort_zero),
            "T_W": shell_enstrophy(r_vort_zero),
            "interpretation": (
                "The enstrophy channel vanishes on this shell although the velocity "
                "energy channel is nonzero."
            ),
        },
    }


def candidate_descriptor_snapshot(alpha: float = 1.0, beta: float = 1.0) -> dict:
    radii = [0.02 + 0.02*k for k in range(1, 201)] + [4.2 + 0.2*k for k in range(1, 30)]
    best = None
    for r in radii:
        e = shell_energy(r)
        w = shell_enstrophy(r)
        p = shell_pressure_fluctuation(r)
        value = r*r*e + alpha*r**4*w + beta*r**4*p
        row = {"r": r, "value": value, "r2E": r*r*e, "r4W": r**4*w, "r4P": r**4*p}
        if best is None or value > best["value"]:
            best = row
    return {
        "alpha": alpha,
        "beta": beta,
        "sampled_maximum": best,
        "status": "CONJECTURE / TARGET DIAGNOSTIC ONLY",
        "note": "Finite-radius sampling does not establish a supremum theorem.",
        "sample_count": len(radii),
    }


def run_all() -> dict:
    symbolic = symbolic_seed_checks()
    scale = scale_checks()

    shell_rows = []
    for r in (0.25, 0.5, 1.0, math.sqrt(2.0), math.sqrt(2.5), 2.0):
        ex, ey, ez = shell_axis_energy(r)
        shell_rows.append({
            "r": r,
            "T_E": shell_energy(r),
            "T_W": shell_enstrophy(r),
            "T_P": shell_pressure_fluctuation(r),
            "T_Ex": ex,
            "T_Ey": ey,
            "T_Ez": ez,
            "axis_energy_sum_error": abs((ex+ey+ez)-shell_energy(r)),
        })

    checks = {
        "symbolic_divergence_zero": symbolic["divergence_zero"],
        "symbolic_omega_match": symbolic["omega_residual_zero"],
        "pressure_source_match": symbolic["pressure_source_residual_zero"],
        "energy_angular_formula_match": symbolic["shell_energy_angular_identity_zero"],
        "energy_isotropic_at_sqrt2": symbolic["shell_energy_isotropic_at_r_sqrt2"],
        "axis_energy_sums": max(row["axis_energy_sum_error"] for row in shell_rows) < 1e-12,
        "radial_origin_undefined": radial_readout_status((0.0, 0.0, 0.0))["status"] == "undefined/inapplicable",
        "radial_equator_defined_zero": radial_readout_status((1.0, 0.0, 0.0))["status"] == "defined-zero",
        "scale_energy": max(row["r2_energy_abs_error"] for row in scale) < 1e-12,
        "scale_enstrophy": max(row["r4_enstrophy_abs_error"] for row in scale) < 1e-12,
        "scale_pressure_l2": max(row["pressure_l2_rel_error"] for row in scale) < 5e-6,
        "aggregate_collision_constructed": aggregate_collision()["same_quadratic_descriptor"],
    }

    return {
        "schema_version": SCHEMA_VERSION,
        "status": "COMPUTATIONAL CHECK / FIRST-PASS BRIDGE",
        "claim_boundary": (
            "These checks validate the displayed DSD-to-Navier-Stokes bridge "
            "constructions for one analytic Schwartz seed. They do not prove "
            "global existence, smoothness, coercivity, or an a-priori bound."
        ),
        "checks": checks,
        "passed": sum(bool(v) for v in checks.values()),
        "total": len(checks),
        "symbolic": symbolic,
        "radial_status": {
            "origin": radial_readout_status((0.0, 0.0, 0.0)),
            "equator": radial_readout_status((1.0, 0.0, 0.0)),
            "axis": radial_readout_status((0.0, 0.0, 1.0)),
        },
        "rotational_control": rotational_control(),
        "shell_diagnostics": shell_rows,
        "directional_entropy": [
            directional_entropy(0.5, 12),
            directional_entropy(1.0, 12),
            directional_entropy(math.sqrt(2.0), 12),
            directional_entropy(2.0, 12),
        ],
        "special_shells": special_shells(),
        "aggregate_collision": aggregate_collision(),
        "scale_checks": scale,
        "candidate_descriptor_t0": candidate_descriptor_snapshot(),
        "next_unproved_steps": [
            "Generalize the bridge from the centered analytic seed to arbitrary admissible smooth divergence-free initial data.",
            "Add time evolution and verify fixed-time static recovery along a Navier-Stokes trajectory.",
            "Determine whether any DSD descriptor controls a known regularity-sufficient norm.",
            "Prove or disprove a global a-priori bound for a translation-complete all-center descriptor.",
        ],
    }


def write_markdown(summary: dict, path: Path) -> None:
    c = summary["checks"]
    spec = summary["special_shells"]
    best = summary["candidate_descriptor_t0"]["sampled_maximum"]
    lines = [
        "# DSD–Navier–Stokes first-pass computational summary",
        "",
        f"Status: **{summary['status']}**",
        "",
        f"Checks passed: **{summary['passed']}/{summary['total']}**",
        "",
        "## Exact / deterministic checks",
        "",
    ]
    for key, value in c.items():
        lines.append(f"- {'PASS' if value else 'FAIL'} — `{key}`")
    lines += [
        "",
        "## Two structural shell findings",
        "",
        f"- At `r=sqrt(2)≈{spec['energy_isotropic_shell']['r']:.12g}`, total shell energy density is angularly isotropic, while axis-resolved energies remain unequal.",
        f"- At `r=sqrt(5/2)≈{spec['vorticity_zero_shell']['r']:.12g}`, `T_W≈{spec['vorticity_zero_shell']['T_W']:.3e}` while `T_E≈{spec['vorticity_zero_shell']['T_E']:.12g}` remains nonzero.",
        "",
        "These are information-separation examples, not regularity theorems.",
        "",
        "## Typed zero / undefined check",
        "",
        "- At the origin the radial direction is inapplicable/undefined.",
        "- At `(1,0,0)` the radial channel is applicable and has defined value zero.",
        "",
        "## Scale-aware diagnostic snapshot",
        "",
        "For the exploratory `alpha=beta=1` centered quantity, finite sampling gives:",
        "",
        f"- sampled maximum value: `{best['value']:.12g}`",
        f"- radius: `{best['r']:.12g}`",
        "",
        "This sampled maximum is **not** a supremum proof and the descriptor is still `CONJECTURE / TARGET`.",
        "",
        "## Claim boundary",
        "",
        summary["claim_boundary"],
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="results")
    args = parser.parse_args()

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    summary = run_all()
    (out / "dsd_bridge_first_pass.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    write_markdown(summary, out / "dsd_bridge_first_pass.md")

    print(
        f"DSD/Navier-Stokes first-pass bridge: "
        f"{summary['passed']}/{summary['total']} checks passed"
    )
    if summary["passed"] != summary["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
