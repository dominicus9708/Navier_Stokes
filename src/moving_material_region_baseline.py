#!/usr/bin/env python3
"""
Moving observer sphere vs material-region baseline for the DSD-assisted
3D incompressible Navier-Stokes proof challenge.

The exact general identities are kinematic identities for smooth incompressible
flows.  The Gaussian benchmark is evaluated only at t=0 and with a frozen local
linearization to visualize deformation; it is not a Navier-Stokes time solution.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import sympy as sp


SCHEMA_VERSION = "0.1.0"


def gaussian_seed_symbolics() -> dict:
    x, y, z, tau = sp.symbols("x y z tau", real=True)
    r2 = x*x + y*y + z*z
    g = sp.exp(-r2)

    u = sp.Matrix([
        4*x*z*g,
        4*y*z*g,
        4*(1-x*x-y*y)*g,
    ])
    variables = (x, y, z)
    grad = sp.Matrix([[sp.diff(u[i], variables[j]) for j in range(3)] for i in range(3)])
    S = sp.simplify((grad + grad.T) / 2)
    Omega = sp.simplify((grad - grad.T) / 2)

    a0 = {x: 0, y: 0, z: sp.Rational(1, 2)}
    c = sp.exp(-sp.Rational(1, 4))
    u0 = sp.simplify(u.subs(a0))
    A0 = sp.simplify(grad.subs(a0))
    S0 = sp.simplify(S.subs(a0))
    O0 = sp.simplify(Omega.subs(a0))

    expected_S0 = sp.diag(2*c, 2*c, -4*c)
    F = sp.diag(sp.exp(2*c*tau), sp.exp(2*c*tau), sp.exp(-4*c*tau))
    C = sp.simplify(F.T * F)
    det_F = sp.simplify(F.det())
    principal_stretches = [
        sp.exp(2*c*tau),
        sp.exp(2*c*tau),
        sp.exp(-4*c*tau),
    ]
    log_shape_sq = sp.simplify(sum(sp.log(s)**2 for s in principal_stretches))
    # Under tau >= 0, max/min = exp(6 c tau).
    aspect_ratio = sp.exp(6*c*tau)

    return {
        "divergence": str(sp.simplify(sp.trace(grad))),
        "divergence_zero": sp.simplify(sp.trace(grad)) == 0,
        "anchor": ["0", "0", "1/2"],
        "anchor_velocity": [str(sp.simplify(v)) for v in u0],
        "anchor_gradient": [[str(sp.simplify(A0[i, j])) for j in range(3)] for i in range(3)],
        "anchor_strain": [[str(sp.simplify(S0[i, j])) for j in range(3)] for i in range(3)],
        "anchor_rotation": [[str(sp.simplify(O0[i, j])) for j in range(3)] for i in range(3)],
        "anchor_strain_expected": [[str(sp.simplify(expected_S0[i, j])) for j in range(3)] for i in range(3)],
        "anchor_strain_match": all(
            sp.simplify(S0[i, j] - expected_S0[i, j]) == 0
            for i in range(3) for j in range(3)
        ),
        "anchor_rotation_zero": all(sp.simplify(O0[i, j]) == 0 for i in range(3) for j in range(3)),
        "anchor_trace_strain": str(sp.simplify(sp.trace(S0))),
        "anchor_trace_zero": sp.simplify(sp.trace(S0)) == 0,
        "anchor_eigenvalues_ordered": [
            str(-4*c),
            str(2*c),
            str(2*c),
        ],
        "frozen_local_F": [[str(sp.simplify(F[i, j])) for j in range(3)] for i in range(3)],
        "frozen_local_C": [[str(sp.simplify(C[i, j])) for j in range(3)] for i in range(3)],
        "frozen_local_det_F": str(det_F),
        "frozen_local_volume_preserved": det_F == 1,
        "frozen_local_log_shape_sq": str(log_shape_sq),
        "frozen_local_log_shape_sq_expected": str(24*c*c*tau*tau),
        "frozen_local_log_shape_match": sp.simplify(log_shape_sq - 24*c*c*tau*tau) == 0,
        "frozen_local_aspect_ratio_tau_nonnegative": str(aspect_ratio),
        "classification": "LOCAL FROZEN-GRADIENT MODEL / NOT A TIME-SOLVED NS TRAJECTORY",
    }


def generic_matrix_identities() -> dict:
    # Exact symbolic placeholder matrix entries, enough to verify the key
    # length-rate identity v^T Omega v = 0 and tr(S)=tr(A).
    a11,a12,a13,a21,a22,a23,a31,a32,a33 = sp.symbols(
        "a11 a12 a13 a21 a22 a23 a31 a32 a33", real=True
    )
    v1,v2,v3 = sp.symbols("v1 v2 v3", real=True)
    A = sp.Matrix([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]])
    S = (A + A.T)/2
    O = (A - A.T)/2
    v = sp.Matrix([v1,v2,v3])

    skew_quad = sp.simplify((v.T * O * v)[0])
    length_rate_residual = sp.simplify((v.T * A * v)[0] - (v.T * S * v)[0])

    return {
        "vT_Omega_v": str(skew_quad),
        "rotation_does_not_change_instantaneous_length": skew_quad == 0,
        "vT_A_v_minus_vT_S_v": str(length_rate_residual),
        "length_rate_depends_only_on_strain": length_rate_residual == 0,
        "trace_S_minus_trace_A": str(sp.simplify(sp.trace(S)-sp.trace(A))),
        "trace_identity": sp.simplify(sp.trace(S)-sp.trace(A)) == 0,
    }


def frozen_local_numeric(times=(0.0,0.05,0.1,0.2,0.5)) -> list[dict]:
    c = math.exp(-0.25)
    rows = []
    for t in times:
        sx = math.exp(2*c*t)
        sy = sx
        sz = math.exp(-4*c*t)
        det = sx*sy*sz
        log_shape = math.sqrt((math.log(sx))**2 + (math.log(sy))**2 + (math.log(sz))**2)
        rows.append({
            "tau": t,
            "sigma_x": sx,
            "sigma_y": sy,
            "sigma_z": sz,
            "det_F": det,
            "aspect_ratio": max(sx,sy,sz)/min(sx,sy,sz),
            "log_shape_gap": log_shape,
        })
    return rows


def dsd_channels() -> dict:
    return {
        "q_center": "X(a,t) = Phi_t(a)",
        "q_observer_shell": "S_ell^obs(t) = {x: |x-X(a,t)|=ell}",
        "q_material_cell": "Omega_ell^mat(t) = Phi_t(B_ell(a))",
        "q_F": "F(a,t) = D_a Phi_t(a)",
        "q_J": "J(a,t) = det F(a,t)",
        "q_C": "C(a,t) = F(a,t)^T F(a,t)",
        "q_sigma": "principal stretches sigma_1,sigma_2,sigma_3",
        "q_shape": "Delta_shape = ||log U||_F, U=sqrt(C)",
        "q_strain": "ordered eigenvalues lambda_1<=lambda_2<=lambda_3 of S",
        "q_middle_positive": "lambda_2^+",
        "q_rotation": "Omega=(grad u-grad u^T)/2",
        "typed_status": (
            "J=1 is a defined nonzero volume-preservation channel; "
            "radial direction at a shell center remains inapplicable exactly at the center."
        ),
    }


def run_all() -> dict:
    sym = gaussian_seed_symbolics()
    generic = generic_matrix_identities()
    numeric = frozen_local_numeric()

    checks = {
        "gaussian_divergence_zero": sym["divergence_zero"],
        "anchor_strain_match": sym["anchor_strain_match"],
        "anchor_rotation_zero": sym["anchor_rotation_zero"],
        "anchor_trace_zero": sym["anchor_trace_zero"],
        "frozen_local_volume_preserved": sym["frozen_local_volume_preserved"],
        "frozen_local_log_shape_formula": sym["frozen_local_log_shape_match"],
        "rotation_no_length_change": generic["rotation_does_not_change_instantaneous_length"],
        "length_rate_strain_only": generic["length_rate_depends_only_on_strain"],
        "trace_S_equals_trace_grad": generic["trace_identity"],
        "numeric_det_close_one": max(abs(row["det_F"]-1.0) for row in numeric) < 1e-12,
    }

    return {
        "schema_version": SCHEMA_VERSION,
        "status": "DERIVED KINEMATIC BRIDGE + COMPUTATIONAL CHECK",
        "claim_boundary": (
            "The flow-map/Jacobian identities are exact for a smooth incompressible flow "
            "up to the lifespan on which the flow map is a diffeomorphism. The Gaussian "
            "frozen-gradient ellipsoid is only a local t=0 deformation model and is not "
            "a time-integrated Navier-Stokes solution."
        ),
        "exact_general_identities": {
            "center_trajectory": "dX/dt = u(X,t)",
            "flow_map": "d Phi_t(a)/dt = u(Phi_t(a),t)",
            "deformation_gradient": "dF/dt = (grad u)(Phi_t(a),t) F",
            "jacobian": "dJ/dt = (div u)(Phi_t(a),t) J; hence J=1 if J(0)=1",
            "cauchy_green": "dC/dt = 2 F^T S F",
            "material_volume": "|Phi_t(B)|=|B| for incompressible smooth flow",
            "material_scalar_transport": (
                "d/dt integral_{Omega(t)} f dx = integral_{Omega(t)} D_t f dx "
                "when div u=0"
            ),
            "line_element": (
                "d/dt |Fv|^2 = 2 (Fv)^T S (Fv); "
                "instantaneous stretching is strain-controlled"
            ),
        },
        "checks": checks,
        "passed": sum(bool(v) for v in checks.values()),
        "total": len(checks),
        "generic_matrix_checks": generic,
        "gaussian_anchor": sym,
        "frozen_local_numeric": numeric,
        "dsd_channels": dsd_channels(),
        "proof_relevance": {
            "translation_completeness": (
                "Before a candidate blow-up time, Phi_t is a bijective material labeling. "
                "Thus all-center local tracking can be written with initial labels a rather "
                "than a single preferred Eulerian origin."
            ),
            "shape_channel": (
                "The moving rigid observer sphere removes pure translation, while the "
                "material cell records strain-induced deformation. Their difference is a "
                "local deformation/describability channel."
            ),
            "middle_eigenvalue_link": (
                "At the benchmark anchor (0,0,1/2), lambda=(-4c,2c,2c), c=e^-1/4. "
                "The material cell expands in two directions and contracts in one while "
                "preserving volume, directly realizing the positive-middle-eigenvalue gate."
            ),
        },
        "next_targets": [
            "Replace the frozen local model by integration of the coupled center/F equations along a numerical NS trajectory.",
            "Seed material cells over many initial labels a and radii ell to obtain a Lagrangian all-center/all-scale diagnostic.",
            "Couple Delta_shape and lambda_2^+ to the existing local pressure, vorticity-alignment, and critical L3 channels.",
            "Search for an a-priori bound on accumulated positive strain or a known regularity-sufficient local gate.",
        ],
    }


def write_markdown(summary: dict, path: Path) -> None:
    rows = summary["frozen_local_numeric"]
    lines = [
        "# Moving observer sphere / material-cell baseline",
        "",
        f"Status: **{summary['status']}**",
        "",
        f"Checks passed: **{summary['passed']}/{summary['total']}**",
        "",
        "## Exact kinematic split",
        "",
        "- Co-moving observer sphere: center follows `dX/dt=u(X,t)` but radius/shape are held spherical.",
        "- Material cell: `Omega_ell^mat(t)=Phi_t(B_ell(a))` follows the same fluid particles and may deform.",
        "- For incompressible smooth flow, `det D_a Phi_t = 1`; volume is preserved even when shape changes.",
        "",
        "## Gaussian anchor",
        "",
        "At `a=(0,0,1/2)`, with `c=e^(-1/4)`: ",
        "",
        "- center velocity: `(0,0,4c)`;",
        "- strain eigenvalues: `(-4c, 2c, 2c)`;",
        "- local rotation tensor: `0`;",
        "- trace of strain: `0`.",
        "",
        "The frozen local model therefore has principal stretches",
        "",
        "`(exp(2 c tau), exp(2 c tau), exp(-4 c tau))`,",
        "",
        "whose product is exactly `1`.  Two directions expand while one contracts.",
        "",
        "## Local DSD shape gap",
        "",
        "For `U=sqrt(F^T F)`, use the bridge quantity",
        "",
        "`Delta_shape = ||log U||_F`.",
        "",
        "In the frozen anchor model,",
        "",
        "`Delta_shape = 2 sqrt(6) e^(-1/4) |tau|`.",
        "",
        "This is zero for pure co-translation but positive for strain-driven deformation.",
        "",
        "## Sample values",
        "",
    ]
    for row in rows:
        lines.append(
            f"- tau={row['tau']:.2f}: "
            f"sigma=({row['sigma_x']:.6g},{row['sigma_y']:.6g},{row['sigma_z']:.6g}), "
            f"detF={row['det_F']:.12g}, aspect={row['aspect_ratio']:.6g}, "
            f"Delta_shape={row['log_shape_gap']:.6g}"
        )
    lines += [
        "",
        "## Claim boundary",
        "",
        summary["claim_boundary"],
        "",
        "The next proof-relevant step is not to keep one sphere centered at one origin, "
        "but to label local cells by every initial material point `a` and scale `ell`, then "
        "track deformation/pressure/vorticity channels along their trajectories.",
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
    (out / "moving_material_region_baseline.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    write_markdown(summary, out / "moving_material_region_baseline.md")
    print(f"moving material-region baseline: {summary['passed']}/{summary['total']} checks passed")
    if summary["passed"] != summary["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
