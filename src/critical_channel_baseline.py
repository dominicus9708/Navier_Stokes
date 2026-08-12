#!/usr/bin/env python3
"""
Critical-channel and vortex-stretching bridge for the DSD/Navier-Stokes project.

Exact symbolic checks for the Gaussian double-curl benchmark.
No global-regularity claim.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def run_checks() -> dict:
    x, y, z, r, mu = sp.symbols("x y z r mu", real=True)
    r2 = x*x + y*y + z*z
    psi = sp.exp(-r2)
    u = sp.Matrix([
        4*x*z*psi,
        4*y*z*psi,
        4*(1-x*x-y*y)*psi,
    ])
    coords = (x, y, z)
    G = sp.Matrix([[sp.diff(u[i], coords[j]) for j in range(3)] for i in range(3)])
    S = sp.simplify((G + G.T)/2)
    omega = sp.Matrix([
        sp.diff(u[2], y) - sp.diff(u[1], z),
        sp.diff(u[0], z) - sp.diff(u[2], x),
        sp.diff(u[1], x) - sp.diff(u[0], y),
    ])

    trace_S = sp.simplify(sp.trace(S))
    stretch = sp.factor((omega.T*S*omega)[0])
    stretch_expected = 64*z*(x*x+y*y)*(2*r2-5)**2*sp.exp(-3*r2)
    stretch_residual = sp.simplify(stretch-stretch_expected)

    shell_stretch = 64*r**3*mu*(1-mu**2)*(2*r**2-5)**2*sp.exp(-3*r**2)
    shell_signed = sp.simplify(sp.Rational(1,2)*sp.integrate(shell_stretch, (mu, -1, 1)))
    shell_positive = sp.simplify(sp.Rational(1,2)*sp.integrate(shell_stretch, (mu, 0, 1)))
    shell_positive_expected = 8*r**3*(2*r**2-5)**2*sp.exp(-3*r**2)

    global_positive = sp.simplify(
        sp.integrate(4*sp.pi*r**2*shell_positive_expected, (r, 0, sp.oo))
    )

    gradw = sp.Matrix([[sp.diff(omega[i], coords[j]) for j in range(3)] for i in range(3)])
    gradw2 = sp.expand(sum(v**2 for v in gradw))
    w2 = sp.expand(sum(v**2 for v in omega))
    u2 = sp.expand(sum(v**2 for v in u))

    def whole(expr):
        return sp.simplify(
            sp.integrate(expr, (x, -sp.oo, sp.oo), (y, -sp.oo, sp.oo), (z, -sp.oo, sp.oo))
        )

    int_u2 = whole(u2)
    int_w2 = whole(w2)
    int_gradw2 = whole(gradw2)
    global_signed = whole(stretch)

    Q = sp.simplify(sum(G[i,j]*G[j,i] for i in range(3) for j in range(3)))
    adv = sp.Matrix([
        sum(u[j]*sp.diff(u[i], coords[j]) for j in range(3))
        for i in range(3)
    ])
    div_minus_adv = sp.simplify(-sum(sp.diff(adv[i], coords[i]) for i in range(3)))
    pressure_closure_residual = sp.simplify(div_minus_adv + Q)

    checks = {
        "trace_strain_zero": trace_S == 0,
        "stretch_formula": stretch_residual == 0,
        "signed_shell_stretch_zero": shell_signed == 0,
        "positive_shell_stretch_formula": sp.simplify(shell_positive-shell_positive_expected) == 0,
        "global_signed_stretch_zero": global_signed == 0,
        "global_positive_stretch_exact": sp.simplify(global_positive-992*sp.pi/81) == 0,
        "pressure_closure_advective_divergence": pressure_closure_residual == 0,
        "whole_space_energy_exact": sp.simplify(int_u2-5*sp.sqrt(2)*sp.pi**sp.Rational(3,2)/2) == 0,
        "whole_space_enstrophy_exact": sp.simplify(int_w2-35*sp.sqrt(2)*sp.pi**sp.Rational(3,2)/2) == 0,
        "whole_space_grad_enstrophy_exact": sp.simplify(int_gradw2-315*sp.sqrt(2)*sp.pi**sp.Rational(3,2)/2) == 0,
    }

    return {
        "status": "COMPUTATIONAL CHECK / CRITICAL-CHANNEL BRIDGE",
        "checks": checks,
        "passed": sum(bool(v) for v in checks.values()),
        "total": len(checks),
        "strain_trace": str(trace_S),
        "vortex_stretching_density": str(stretch),
        "normalized_shell_signed_stretch": str(shell_signed),
        "normalized_shell_positive_stretch": str(shell_positive),
        "global_positive_stretch": str(global_positive),
        "global_negative_stretch": str(-global_positive),
        "global_net_stretch": str(global_signed),
        "whole_space_integrals": {
            "int_|u|^2": str(int_u2),
            "int_|omega|^2": str(int_w2),
            "int_|grad_omega|^2": str(int_gradw2),
        },
        "pressure_closure": {
            "Q": str(sp.factor(Q)),
            "div_R_adv": str(sp.factor(div_minus_adv)),
            "statement": "div R_adv = -Q, div R_pres = +Q when -Delta p=Q, and div R_visc=0.",
        },
        "interpretation": {
            "aggregate_cancellation": "Global signed vortex stretching is zero for this benchmark, but positive and negative stretching are separately nonzero and cancel.",
            "proof_boundary": "This is a benchmark cancellation witness. It is not a general bound on vortex stretching."
        }
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", default="results")
    args = ap.parse_args()
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    d = run_checks()
    (out/"critical_channel_baseline.json").write_text(json.dumps(d, indent=2), encoding="utf-8")
    md = [
        "# Critical-channel baseline",
        "",
        f"Checks passed: **{d['passed']}/{d['total']}**",
        "",
        "## Key exact findings",
        "",
        f"- `tr S = {d['strain_trace']}`.",
        f"- `omega^T S omega = {d['vortex_stretching_density']}`.",
        f"- normalized signed shell stretching = `{d['normalized_shell_signed_stretch']}`.",
        f"- normalized positive-part shell stretching = `{d['normalized_shell_positive_stretch']}`.",
        f"- global positive stretching = `{d['global_positive_stretch']}` and the negative part is its exact opposite.",
        "",
        "The zero global sum therefore hides nonzero local stretching. This is an aggregation-cancellation witness, not a regularity theorem.",
        "",
        "## Pressure closure",
        "",
        d["pressure_closure"]["statement"],
        "",
        "## Claim boundary",
        "",
        d["interpretation"]["proof_boundary"],
    ]
    (out/"critical_channel_baseline.md").write_text("\n".join(md), encoding="utf-8")
    print(f"Critical-channel bridge: {d['passed']}/{d['total']} checks passed")
    if d["passed"] != d["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
