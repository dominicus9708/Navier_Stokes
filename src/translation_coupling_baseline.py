#!/usr/bin/env python3
"""
Translation-completeness and nonlinear cross-coupling checks.

The numerical sphere is only a quadrature surface inside R^3; it is not a wall.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import sympy as sp


def base_seed_vec(pt, axis=2):
    y = list(pt)
    rr = sum(v*v for v in y)
    g = math.exp(-rr)
    out = []
    for j in range(3):
        if j == axis:
            out.append(4.0*(1.0-sum(y[k]*y[k] for k in range(3) if k != axis))*g)
        else:
            out.append(4.0*y[j]*y[axis]*g)
    return out


def scaled_translated_seed(pt, axis=2, center=(0.0,0.0,0.0), lam=1.0, amp=1.0):
    y = tuple(lam*(pt[i]-center[i]) for i in range(3))
    return [amp*lam*v for v in base_seed_vec(y, axis)]


def fibonacci_dirs(n):
    golden = (1.0+5.0**0.5)/2.0
    for i in range(n):
        z = 1.0-2.0*(i+0.5)/n
        rho = math.sqrt(max(0.0, 1.0-z*z))
        phi = 2.0*math.pi*i/golden
        yield (rho*math.cos(phi), rho*math.sin(phi), z)


def shell_energy_stats(obs_center, radius, field, n=6000):
    vals = []
    for d in fibonacci_dirs(n):
        pt = tuple(obs_center[i]+radius*d[i] for i in range(3))
        u = field(pt)
        vals.append(0.5*sum(v*v for v in u))
    mean = sum(vals)/n
    var = sum((v-mean)**2 for v in vals)/n
    cv = (var**0.5/mean) if mean else 0.0
    return {"mean": mean, "coefficient_of_variation": cv}


def analytic_shell_energy(r):
    return 8.0*math.exp(-2.0*r*r)*(1.0-4.0*r*r/3.0+2.0*r**4/3.0)


def symbolic_cross_coupling():
    x, y, z = sp.symbols("x y z", real=True)
    coords = (x, y, z)

    def seed(axis, center=(0,0,0), amp=sp.Integer(1)):
        Y = [coords[i]-sp.sympify(center[i]) for i in range(3)]
        rr = sum(v*v for v in Y)
        g = sp.exp(-rr)
        out = []
        for j in range(3):
            if j == axis:
                out.append(4*(1-sum(Y[k]**2 for k in range(3) if k != axis))*g)
            else:
                out.append(4*Y[j]*Y[axis]*g)
        return sp.Matrix([amp*v for v in out])

    def divergence(U):
        return sp.simplify(sum(sp.diff(U[i], coords[i]) for i in range(3)))

    def Q(U):
        G = sp.Matrix([[sp.diff(U[i], coords[j]) for j in range(3)] for i in range(3)])
        return sp.simplify(sum(G[i,j]*G[j,i] for i in range(3) for j in range(3)))

    u1 = seed(2, (0,0,0), sp.Integer(1))
    u2 = seed(0, (1,0,0), sp.Rational(1,2))
    total = u1+u2
    q1, q2, qt = Q(u1), Q(u2), Q(total)
    cross = sp.factor(sp.simplify(qt-q1-q2))
    point = {x: sp.Rational(2,5), y: sp.Rational(1,5), z: sp.Rational(-3,10)}
    return {
        "div_u1": str(divergence(u1)),
        "div_u2": str(divergence(u2)),
        "div_total": str(divergence(total)),
        "cross_Q": str(cross),
        "cross_Q_at_test_point": float(sp.N(cross.subs(point), 16)),
    }


def run_checks():
    center = (1.5, 0.0, 0.0)
    lam = 1.2
    amp = 0.8
    radius = math.sqrt(2.0)/lam
    field = lambda pt: scaled_translated_seed(pt, axis=2, center=center, lam=lam, amp=amp)
    centered = shell_energy_stats(center, radius, field)
    wrong = shell_energy_stats((0.0,0.0,0.0), radius, field)
    expected = amp**2*lam**2*analytic_shell_energy(math.sqrt(2.0))
    cross = symbolic_cross_coupling()
    checks = {
        "translated_center_shell_mean": abs(centered["mean"]-expected) < 1e-10,
        "translated_center_isotropic": centered["coefficient_of_variation"] < 1e-10,
        "wrong_center_not_isotropic": wrong["coefficient_of_variation"] > 1e-2,
        "superposed_seed_divergence_free": cross["div_total"] == "0",
        "nonlinear_cross_Q_nonzero": abs(cross["cross_Q_at_test_point"]) > 1e-6,
    }
    return {
        "status": "COMPUTATIONAL CHECK / TRANSLATION + CROSS-COUPLING",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "translated_seed": {
            "physical_center": center,
            "lambda": lam,
            "amplitude": amp,
            "isotropic_shell_radius": radius,
            "centered_shell": centered,
            "expected_centered_mean": expected,
            "origin_centered_shell": wrong,
            "interpretation": "The special shell is recovered around the translated seed center, not around an arbitrary fixed origin."
        },
        "superposition": {
            **cross,
            "interpretation": "Velocity composition is linear and remains divergence-free, but the pressure/advection closure source Q contains a nonzero cross term. Static composition therefore does not imply dynamical independence."
        },
        "proof_boundary": "Finite translated/superposed benchmarks establish covariance and a cross-coupling witness only; they do not cover arbitrary initial data."
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", default="results")
    args = ap.parse_args()
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    d = run_checks()
    (out/"translation_coupling_baseline.json").write_text(json.dumps(d, indent=2), encoding="utf-8")
    md = [
        "# Translation and cross-coupling baseline", "",
        f"Checks passed: **{d['passed']}/{d['total']}**", "",
        "## Translation completeness", "",
        f"- translated seed center: `{d['translated_seed']['physical_center']}`",
        f"- centered special-shell CV: `{d['translated_seed']['centered_shell']['coefficient_of_variation']:.3e}`",
        f"- same-radius shell about the old origin CV: `{d['translated_seed']['origin_centered_shell']['coefficient_of_variation']:.6g}`",
        "",
        "This confirms that a fixed-origin shell analysis is not translation complete.",
        "",
        "## Nonlinear coupling", "",
        f"- `Q_cross = {d['superposition']['cross_Q']}`",
        f"- test-point value: `{d['superposition']['cross_Q_at_test_point']:.12g}`",
        "",
        d["superposition"]["interpretation"], "",
        "## Claim boundary", "", d["proof_boundary"]
    ]
    (out/"translation_coupling_baseline.md").write_text("\n".join(md), encoding="utf-8")
    print(f"Translation/coupling bridge: {d['passed']}/{d['total']} checks passed")
    if d["passed"] != d["total"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
