#!/usr/bin/env python3
"""Verify constants in the smooth local Taylor-ball pure-P_V closure.

This script audits only algebraic/integral constants. It is not a regularity proof.
"""

from __future__ import annotations

import math


def main() -> None:
    theta = 0.5
    sigma_h = 0.4
    eta = 0.5
    f = 1.0
    delta = 1.0
    q = 2.0

    # Exact dimensionless Taylor-ball constants.
    c_v_lower = 157.0 * math.pi / 1890.0
    c_z_lower = 71.0 * math.pi / 105.0
    c_m2_ball = 4.0 * math.pi / 5.0

    # Ratios derived from the exact constants.
    lambda_ratio_coeff = c_m2_ball / c_v_lower
    dissipation_variance_coeff = 0.5 * c_z_lower / c_m2_ball

    assert abs(lambda_ratio_coeff - 1512.0 / 157.0) < 1e-13
    assert abs(dissipation_variance_coeff - 71.0 / 168.0) < 1e-13

    # Second-Taylor near-strain constant.
    a0 = 3.0 * math.sqrt(2.0) / 8.0
    b1_sq = (a0 + sigma_h) ** 2 + 0.5

    # Persistent Taylor-ball variance ratio.
    Lambda = (1512.0 / 157.0) * b1_sq / theta**2

    # Conservative use of c_*(2)>=1 and nu*K2,+ >= 8.
    L_var = theta / (2.0 * math.pi**2 * (1.0 - eta)) * (
        0.25 * math.log(q) * Lambda + f + 0.5 * delta
    )

    # Modest eigenframe action TV(theta_e)<=2 L.
    mu = 2.0
    L_swap = math.pi / (1.0 + 2.0 * mu)

    margin = L_swap - L_var

    expected = {
        "a0": 0.5303300858899106,
        "b1_sq": 1.3655140687119285,
        "Lambda": 52.6027330418455,
        "L_var": 0.5377803705715904,
        "L_swap": 0.6283185307179586,
        "margin": 0.0905381601463682,
    }

    actual = {
        "a0": a0,
        "b1_sq": b1_sq,
        "Lambda": Lambda,
        "L_var": L_var,
        "L_swap": L_swap,
        "margin": margin,
    }

    for key, ref in expected.items():
        assert abs(actual[key] - ref) < 5e-13, (key, actual[key], ref)

    assert margin > 0.0

    print("Smooth local Taylor-ball closure constants")
    for key, value in actual.items():
        print(f"{key} = {value:.15f}")
    print(f"V_lower coefficient = {c_v_lower:.15f}")
    print(f"Z_lower coefficient = {c_z_lower:.15f}")
    print(f"M2_ball coefficient = {c_m2_ball:.15f}")
    print(f"Lambda ratio coefficient = {lambda_ratio_coeff:.15f}")
    print(f"D/V upper coefficient = {dissipation_variance_coeff:.15f}")
    print("PASS")


if __name__ == "__main__":
    main()
