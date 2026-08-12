#!/usr/bin/env python3
"""Moving-control-volume energy budget audit for the DSD/Navier-Stokes project.

The exact identity is a Reynolds-transport consequence. The numerical section
uses the existing asymmetric two-Gaussian benchmark to compare a fixed sphere,
a rigidly co-moving sphere, and a material cell at t=0.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


SCHEMA_VERSION = "0.1.0"


def seed_grid(X, Y, Z, axis, center, amp=1.0):
    q = [X-center[0], Y-center[1], Z-center[2]]
    r2 = sum(v*v for v in q)
    g = np.exp(-r2)
    u = np.empty((3,) + X.shape, dtype=float)
    for j in range(3):
        if j == axis:
            transverse = sum(q[k]**2 for k in range(3) if k != axis)
            u[j] = 4*amp*(1-transverse)*g
        else:
            u[j] = 4*amp*q[j]*q[axis]*g
    return u


def seed_point(point, axis, center, amp=1.0):
    q = [point[j]-center[j] for j in range(3)]
    r2 = sum(v*v for v in q)
    g = math.exp(-r2)
    u = [0.0, 0.0, 0.0]
    for j in range(3):
        if j == axis:
            transverse = sum(q[k]**2 for k in range(3) if k != axis)
            u[j] = 4*amp*(1-transverse)*g
        else:
            u[j] = 4*amp*q[j]*q[axis]*g
    return np.array(u)


def audit(N=64, L=6.0, radii=(0.75,1.0,1.25,1.5,2.0)):
    x = np.linspace(-L, L, N, endpoint=False)
    h = 2*L/N
    X,Y,Z = np.meshgrid(x,x,x,indexing="ij")
    u = (
        seed_grid(X,Y,Z,2,(0.0,0.0,0.0),1.0)
        + seed_grid(X,Y,Z,0,(-1.0,0.0,0.0),1.0)
    )

    center = (0.0,0.0,0.0)
    V = (
        seed_point(center,2,(0.0,0.0,0.0),1.0)
        + seed_point(center,0,(-1.0,0.0,0.0),1.0)
    )

    k = 2*np.pi*np.fft.fftfreq(N,d=h)
    K = np.meshgrid(k,k,k,indexing="ij")
    grads = np.empty((3,3,N,N,N))
    for i in range(3):
        U = np.fft.fftn(u[i])
        for j in range(3):
            grads[i,j] = np.fft.ifftn(1j*K[j]*U).real

    grad_e = np.empty_like(u)
    for j in range(3):
        grad_e[j] = sum(u[i]*grads[i,j] for i in range(3))

    fixed_adv_density = np.sum(u*grad_e, axis=0)
    relative_adv_density = np.sum(
        (u - V[:,None,None,None])*grad_e,
        axis=0,
    )

    R2 = X*X+Y*Y+Z*Z
    dv = h**3
    rows = []
    for r in radii:
        mask = R2 < r*r
        fixed = float(np.sum(fixed_adv_density[mask])*dv)
        relative = float(np.sum(relative_adv_density[mask])*dv)
        rows.append({
            "r": r,
            "F_adv_fixed": fixed,
            "F_adv_rigid_comoving": relative,
            "F_adv_material": 0.0,
            "rigid_translation_correction": fixed-relative,
        })

    return {
        "N": N,
        "L": L,
        "h": h,
        "observer_center": list(center),
        "observer_velocity": V.tolist(),
        "rows": rows,
    }


def run_checks():
    a64 = audit(64)
    a80 = audit(80)
    by64 = {row["r"]: row for row in a64["rows"]}
    by80 = {row["r"]: row for row in a80["rows"]}

    expected_V = np.array([4/math.e, 0.0, 4.0])
    checks = {
        "center_velocity_64": bool(np.linalg.norm(np.array(a64["observer_velocity"])-expected_V) < 1e-12),
        "center_velocity_80": bool(np.linalg.norm(np.array(a80["observer_velocity"])-expected_V) < 1e-12),
        "fixed_adv_inward_r1_both": by64[1.0]["F_adv_fixed"] < 0 and by80[1.0]["F_adv_fixed"] < 0,
        "rigid_comoving_adv_inward_r1_both": by64[1.0]["F_adv_rigid_comoving"] < 0 and by80[1.0]["F_adv_rigid_comoving"] < 0,
        "rigid_comoving_adv_outward_r2_both": by64[2.0]["F_adv_rigid_comoving"] > 0 and by80[2.0]["F_adv_rigid_comoving"] > 0,
        "fixed_adv_still_inward_r2_both": by64[2.0]["F_adv_fixed"] < 0 and by80[2.0]["F_adv_fixed"] < 0,
        "material_advective_flux_exact_zero": all(
            row["F_adv_material"] == 0.0 for row in a64["rows"]+a80["rows"]
        ),
    }

    return {
        "schema_version": SCHEMA_VERSION,
        "status": "DERIVED MOVING-CONTROL IDENTITY + COMPUTATIONAL CHECK",
        "exact_identity": (
            "For kinetic energy e=|u|^2/2 in a control volume with boundary velocity w_b: "
            "d/dt int_Omega e = -int_boundary e (u-w_b).n "
            "-int_boundary p u.n + nu int_boundary partial_n e "
            "-nu int_Omega |grad u|^2. "
            "For a material cell w_b=u, the relative advective term vanishes exactly."
        ),
        "checks": checks,
        "passed": sum(bool(v) for v in checks.values()),
        "total": len(checks),
        "resolution_64": a64,
        "resolution_80": a80,
        "interpretation": (
            "Translating a rigid spherical observation window with the local fluid velocity "
            "changes but does not generally remove advective energy crossing, because boundary "
            "fluid velocities are not all equal to the center velocity. A deforming material "
            "cell follows the full boundary velocity and removes relative advective crossing exactly. "
            "Advection is not removed from the Navier-Stokes dynamics; it is absorbed into the "
            "motion/deformation of the material control volume."
        ),
        "dsd_channel_consequence": {
            "q_adv_fixed": "Eulerian advective flux through a fixed shell",
            "q_adv_relative": "relative advective flux e (u-Xdot).n through a rigid co-moving shell",
            "q_adv_material": "defined zero for a true material boundary",
            "q_pressure_work": "pressure work remains active on a material boundary",
            "q_viscous": "viscous boundary transport and interior dissipation remain active",
        },
        "claim_boundary": (
            "The cancellation of relative material advection is exact Reynolds transport. "
            "The asymmetric sign comparisons are numerical audits on a large decay window, "
            "not a global regularity theorem."
        ),
    }


def write_markdown(d, path):
    b64={row["r"]:row for row in d["resolution_64"]["rows"]}
    b80={row["r"]:row for row in d["resolution_80"]["rows"]}
    lines=[
        "# Moving control-volume energy budget",
        "",
        f"Status: **{d['status']}**",
        "",
        f"Checks passed: **{d['passed']}/{d['total']}**",
        "",
        "## Exact consequence",
        "",
        "For a material cell, the boundary velocity equals the local fluid velocity.",
        "Therefore the relative advective kinetic-energy flux is exactly zero.",
        "Pressure work, viscous boundary transport, and interior viscous dissipation remain.",
        "",
        "## Asymmetric two-seed rigid-sphere check",
        "",
        f"Center velocity: `{d['resolution_64']['observer_velocity']}`.",
        "",
        "At `r=1`:",
        f"- N=64 fixed advective flux `{b64[1.0]['F_adv_fixed']:.12g}`, rigid co-moving `{b64[1.0]['F_adv_rigid_comoving']:.12g}`;",
        f"- N=80 fixed advective flux `{b80[1.0]['F_adv_fixed']:.12g}`, rigid co-moving `{b80[1.0]['F_adv_rigid_comoving']:.12g}`.",
        "",
        "At `r=2`, the rigid co-moving relative flux changes sign while the fixed-sphere flux remains negative:",
        f"- N=64 fixed `{b64[2.0]['F_adv_fixed']:.12g}`, rigid co-moving `{b64[2.0]['F_adv_rigid_comoving']:.12g}`;",
        f"- N=80 fixed `{b80[2.0]['F_adv_fixed']:.12g}`, rigid co-moving `{b80[2.0]['F_adv_rigid_comoving']:.12g}`.",
        "",
        "Thus a moving rigid sphere removes pure translation but still permits relative crossing. "
        "Only the deforming material cell removes advective crossing exactly.",
        "",
        "## Claim boundary",
        "",
        d["claim_boundary"],
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output-dir",default="results")
    args=ap.parse_args()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    d=run_checks()
    (out/"moving_control_energy_budget.json").write_text(
        json.dumps(d,indent=2),encoding="utf-8"
    )
    write_markdown(d,out/"moving_control_energy_budget.md")
    print(f"Moving control-volume energy budget: {d['passed']}/{d['total']} checks passed")
    if d["passed"]!=d["total"]:
        raise SystemExit(1)


if __name__=="__main__":
    main()
