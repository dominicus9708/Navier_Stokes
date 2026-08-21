#!/usr/bin/env python3
"""Verify constants in the smooth large-core first-hitting tightrope.

This is a reproducibility audit for algebraic constants and one-dimensional
root solves. It is not a Navier-Stokes regularity proof.
"""

from __future__ import annotations

import math

PI_B = 1.4967761748
SIGMA = 0.5
C0 = math.sqrt(2.0) / 4.0
S3 = 3.0 * (math.pi / 2.0) ** (4.0 / 3.0)
K_P = (1.0 / (3.0 * math.sqrt(2.0))) * S3 ** (-3.0 / 4.0)
C_BS = (
    7.0
    * 2.0 ** (13.0 / 14.0)
    * 3.0 ** (2.0 / 7.0)
    / (16.0 * math.pi ** (2.0 / 7.0))
)
C_Z = 64.0 * math.sqrt(2.0) * math.pi / 105.0
C_DET = 4.0 / (3.0 * math.sqrt(6.0))


def bisect_root(fn, lo: float, hi: float, n: int = 160) -> float:
    flo = fn(lo)
    fhi = fn(hi)
    if flo == 0.0:
        return lo
    if fhi == 0.0:
        return hi
    if flo * fhi > 0.0:
        raise ValueError(f"root not bracketed: f(lo)={flo}, f(hi)={fhi}")
    for _ in range(n):
        mid = 0.5 * (lo + hi)
        fm = fn(mid)
        if flo * fm <= 0.0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return 0.5 * (lo + hi)


def bcoef(eps_z: float) -> float:
    return (
        C_BS
        * 4.0 ** (3.0 / 7.0)
        * (4.0 * math.pi / (3.0 * (1.0 - eps_z))) ** (2.0 / 7.0)
    )


def lmax(r: float) -> float:
    return PI_B * SIGMA * r * r


def action_residual(L: float) -> float:
    return max(0.0, math.pi / 2.0 - (0.5 + C0) * L)


def nu_lambda_tax(r: float, eps_z: float) -> float:
    """Conservative lower bound on nu * int lambda ds."""
    L = lmax(r)
    A = action_residual(L)
    if A <= 0.0:
        return 0.0
    zbar = (4.0 * math.pi / 3.0) * r**3 / (1.0 - eps_z)
    return (
        2.0
        * K_P ** (-4.0 / 3.0)
        * zbar ** (-2.0 / 3.0)
        * L ** (-1.0 / 3.0)
        * A ** (4.0 / 3.0)
    )


def h1_gap(r: float, eps_z: float) -> float:
    B = bcoef(eps_z) * r ** (6.0 / 7.0)
    production = math.sqrt(2.0) * B * lmax(r)
    tax = 0.75 * math.log(2.0) + nu_lambda_tax(r, eps_z)
    return production - tax


def l2_gap(r: float, eps_z: float) -> float:
    B = bcoef(eps_z) * r ** (6.0 / 7.0)
    production = C_DET * B * lmax(r)
    tax = 0.5 * math.log(2.0) + 2.0 * nu_lambda_tax(r, eps_z)
    return production - tax


def bcrit() -> float:
    return bisect_root(lambda b: b * (b * b + 0.5) - 71.0 / 21.0, 0.0, 4.0)


def gamma_z() -> float:
    b = bcrit()
    return ((b / C_BS) ** (7.0 / 2.0)) / C_Z


def double_sat_gap(r: float, eps_q: float) -> float:
    """theta^-4 - Gamma_Z; negative means double-saturation S-closure."""
    dmax = 0.7146986969 * (1.0 - eps_q) ** (-3.0 / 4.0) * r ** (9.0 / 4.0)
    creq_minus_c0 = math.pi / (PI_B * r * r) - 0.5 - C0
    if creq_minus_c0 <= 0.0:
        return math.inf
    theta = creq_minus_c0 / dmax
    return theta ** (-4.0) - gamma_z()


def main() -> None:
    print(f"C_BS = {C_BS:.15f}")
    print(f"C_Z = {C_Z:.15f}")
    print(f"K_P = {K_P:.15f}")
    print(f"C_det = {C_DET:.15f}")
    print(f"Bcrit = {bcrit():.15f}")
    print(f"Gamma_Z = {gamma_z():.15f}")
    print(f"Bcoef(epsZ=1/4) = {bcoef(0.25):.15f}")

    r_ds_q = bisect_root(lambda r: double_sat_gap(r, 0.25), 1.06, 1.14)
    r_ds_0 = bisect_root(lambda r: double_sat_gap(r, 0.0), 1.06, 1.18)
    r_h1_q = bisect_root(lambda r: h1_gap(r, 0.25), 1.20, 1.40)
    r_h1_0 = bisect_root(lambda r: h1_gap(r, 0.0), 1.20, 1.42)
    r_l2_q = bisect_root(lambda r: l2_gap(r, 0.25), 1.35, 1.55)
    r_l2_0 = bisect_root(lambda r: l2_gap(r, 0.0), 1.35, 1.55)

    print(f"r_DS quarter-tail = {r_ds_q:.12f}")
    print(f"r_DS zero-tail = {r_ds_0:.12f}")
    print(f"r_H1 quarter-tail = {r_h1_q:.12f}")
    print(f"r_H1 zero-tail = {r_h1_0:.12f}")
    print(f"r_L2 quarter-tail = {r_l2_q:.12f}")
    print(f"r_L2 zero-tail = {r_l2_0:.12f}")

    targets = {
        "r_DS quarter-tail": (r_ds_q, 1.0982016691),
        "r_H1 quarter-tail": (r_h1_q, 1.3030842670),
        "r_L2 quarter-tail": (r_l2_q, 1.4550244347),
        "r_L2 zero-tail": (r_l2_0, 1.4724232909),
    }
    for name, (got, want) in targets.items():
        err = abs(got - want)
        print(f"{name}: error={err:.3e}")
        if err > 5e-9:
            raise SystemExit(f"verification failed for {name}")

    print("all smooth large-core tightrope checks passed")


if __name__ == "__main__":
    main()
