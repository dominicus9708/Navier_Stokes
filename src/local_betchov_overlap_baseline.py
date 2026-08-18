#!/usr/bin/env python3
"""Symbolic regression audit for the local Betchov overlap identity.

The script checks the exact algebraic strain/vorticity decomposition and the
local divergence form on an explicit 3D divergence-free polynomial field.
It does not prove global Navier--Stokes regularity.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def generic_matrix_identity():
    a, b, c, d, e, f, g, h = sp.symbols("a b c d e f g h", real=True)
    A = sp.Matrix(
        [
            [a, b, c],
            [d, e, f],
            [g, h, -a - e],
        ]
    )
    S = (A + A.T) / 2
    omega = sp.Matrix([h - f, c - g, d - b])

    r1 = sp.simplify(
        sp.trace(A**3)
        - sp.trace(S**3)
        - sp.Rational(3, 4) * (omega.T * S * omega)[0]
    )
    r2 = sp.simplify(sp.trace(A**3) - 3 * A.det())
    return bool(r1 == 0), bool(r2 == 0)


def polynomial_divergence_audit():
    x, y, z = sp.symbols("x y z", real=True)
    coords = (x, y, z)

    # Curl of an explicit polynomial vector potential.
    potential = sp.Matrix(
        [
            x * y * z + z**3,
            x**2 * z + y * z**2,
            x * y**2 + x**2 * y,
        ]
    )
    u = sp.Matrix(
        [
            sp.diff(potential[2], y) - sp.diff(potential[1], z),
            sp.diff(potential[0], z) - sp.diff(potential[2], x),
            sp.diff(potential[1], x) - sp.diff(potential[0], y),
        ]
    )

    div_u = sp.simplify(sum(sp.diff(u[i], coords[i]) for i in range(3)))
    A = sp.Matrix([[sp.diff(u[i], coords[j]) for j in range(3)] for i in range(3)])
    S = (A + A.T) / 2
    omega = sp.Matrix(
        [
            sp.diff(u[2], y) - sp.diff(u[1], z),
            sp.diff(u[0], z) - sp.diff(u[2], x),
            sp.diff(u[1], x) - sp.diff(u[0], y),
        ]
    )

    F = (A**2 - sp.Rational(1, 2) * sp.trace(A**2) * sp.eye(3)) * u
    div_F = sp.simplify(sum(sp.diff(F[i], coords[i]) for i in range(3)))

    r3 = sp.simplify(sp.trace(A**3) - div_F)
    r4 = sp.simplify(
        (omega.T * S * omega)[0] + 4 * S.det() - sp.Rational(4, 3) * div_F
    )

    return {
        "divergence_free": bool(div_u == 0),
        "trA3_local_divergence": bool(r3 == 0),
        "local_betchov_identity": bool(r4 == 0),
        "velocity": [str(sp.expand(v)) for v in u],
    }


def run_checks():
    generic_betchov, cayley_hamilton = generic_matrix_identity()
    poly = polynomial_divergence_audit()
    checks = {
        "generic_strain_vorticity_decomposition": generic_betchov,
        "tracefree_trA3_equals_3detA": cayley_hamilton,
        "polynomial_divergence_free": poly["divergence_free"],
        "polynomial_trA3_is_divergence": poly["trA3_local_divergence"],
        "polynomial_local_betchov": poly["local_betchov_identity"],
    }
    return {
        "status": "EXACT SYMBOLIC AUDIT / LOCAL BETCHOV OVERLAP GATE / NO GLOBAL REGULARITY CLAIM",
        "checks": checks,
        "passed": sum(bool(v) for v in checks.values()),
        "total": len(checks),
        "identity": "omega.S.omega + 4 det(S) = (4/3) div(F_B)",
        "flux": "F_B = (A^2 - 0.5 tr(A^2) I) u",
        "polynomial_test_field": poly["velocity"],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", default="results")
    args = ap.parse_args()

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    data = run_checks()
    (out / "local_betchov_overlap_baseline.json").write_text(
        json.dumps(data, indent=2), encoding="utf-8"
    )
    print(f"Local Betchov overlap: {data['passed']}/{data['total']} checks passed")
    if data["passed"] != data["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
