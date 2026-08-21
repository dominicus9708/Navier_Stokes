#!/usr/bin/env python3
"""Reproduce constants in the smooth ball-variance / pure-P_V closure.

This is a numerical audit of already-derived exact formulas. It is not a
Navier--Stokes proof by itself.
"""

from __future__ import annotations

import math


Q = 2.0
ETA = 0.5
LAMBDA_V = 2.0
DELTA_V = 1.0
F_V = 1.0

C0 = math.sqrt(2.0) / 4.0
C_COMPAT = 0.7146986968675707


def pi_ball() -> float:
    return (
        (4.0 / math.pi**2)
        / (1.0 - ETA)
        * (0.25 * math.log(Q) * LAMBDA_V + F_V + 0.5 * DELTA_V)
    )


def cv_compatible(r: float, eps_q: float) -> float:
    return C0 + C_COMPAT * (1.0 - eps_q) ** (-0.75) * r ** (9.0 / 4.0)


def swap_threshold(r: float, eps_q: float) -> float:
    cv = cv_compatible(r, eps_q)
    return 2.0 * math.pi / (r * r * (1.0 + 2.0 * cv))


def bisect_root(eps_q: float, target: float, lo: float, hi: float) -> float:
    flo = swap_threshold(lo, eps_q) - target
    fhi = swap_threshold(hi, eps_q) - target
    if flo * fhi > 0:
        raise RuntimeError("root not bracketed")
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        fm = swap_threshold(mid, eps_q) - target
        if flo * fm > 0:
            lo, flo = mid, fm
        else:
            hi, fhi = mid, fm
    return 0.5 * (lo + hi)


def main() -> None:
    pib = pi_ball()
    r0 = bisect_root(0.0, pib, 0.8, 1.3)
    rq = bisect_root(0.25, pib, 0.8, 1.3)

    expected_pi = 1.4967761747987849
    expected_r0 = 1.0990824374
    expected_rq = 1.0606056034

    print(f"Pi_B = {pib:.12f}")
    print(f"r_swap(eps=0) = {r0:.12f}")
    print(f"r_swap(eps=1/4) = {rq:.12f}")
    print(f"C_V(1, eps=0) = {cv_compatible(1.0, 0.0):.12f}")
    print(f"C_V(1, eps=1/4) = {cv_compatible(1.0, 0.25):.12f}")

    assert abs(pib - expected_pi) < 1e-12
    assert abs(r0 - expected_r0) < 2e-9
    assert abs(rq - expected_rq) < 2e-9
    assert swap_threshold(1.0, 0.25) > pib
    assert swap_threshold(1.2, 0.25) < pib

    print("PASS")


if __name__ == "__main__":
    main()
