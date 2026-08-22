#!/usr/bin/env python3
"""Verify the adaptive Taylor-ball closure constants.

Algebraic/integral audit only; not a Navier-Stokes regularity proof.
"""

from __future__ import annotations

import math


def poly(beta: float) -> float:
    return 13.0 * beta * beta - 108.0 * beta + 252.0


def l_ceiling(theta: float) -> float:
    assert 0.0 < theta <= 1.0
    beta = min(1.0, 2.0 * theta)
    a0 = 3.0 * math.sqrt(2.0) / 8.0
    b1_sq = (a0 + 0.4) ** 2 + 0.5
    return beta * theta / math.pi**2 * (
        378.0 * math.log(2.0) * b1_sq / (poly(beta) * theta**2)
        + 1.5
    )


def main() -> None:
    # Exact beta=1 constants from the fixed Taylor-ball audit.
    assert poly(1.0) == 157.0
    assert abs((math.pi / 1890.0) * poly(1.0) - 157.0 * math.pi / 1890.0) < 1e-15

    # Dense deterministic scan of the two analytic pieces.
    max_l = -1.0
    max_theta = None
    for i in range(1, 200001):
        theta = i / 200001.0
        value = l_ceiling(theta)
        if value > max_l:
            max_l = value
            max_theta = theta

    endpoint = l_ceiling(0.5)
    expected = 0.5377803705715904
    swap = math.pi / 5.0

    assert abs(endpoint - expected) < 5e-13
    assert max_l <= expected + 2e-6
    assert swap > endpoint

    # Piecewise monotonicity checks by finite differences.
    prev = l_ceiling(1e-5)
    for i in range(2, 50001):
        theta = 0.5 * i / 50001.0
        cur = l_ceiling(theta)
        assert cur + 1e-12 >= prev
        prev = cur

    prev = l_ceiling(0.5)
    for i in range(1, 50001):
        theta = 0.5 + 0.5 * i / 50000.0
        cur = l_ceiling(theta)
        assert cur <= prev + 1e-12
        prev = cur

    print(f"max scanned L = {max_l:.15f} at theta ~= {max_theta:.8f}")
    print(f"L(1/2) = {endpoint:.15f}")
    print(f"pi/5 = {swap:.15f}")
    print(f"margin = {swap-endpoint:.15f}")
    print("PASS")


if __name__ == "__main__":
    main()
