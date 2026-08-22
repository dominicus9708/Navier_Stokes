#!/usr/bin/env python3
"""Verify exponent arithmetic in GLOBAL_REMOTE_ACTION_AMPLIFICATION_2026-08-22.md.

This script checks only algebraic scaling exponents. It is not a Navier--Stokes
regularity proof and does not supply the Gagliardo--Nirenberg or halo constants.
"""

from fractions import Fraction


def main() -> None:
    # GN: Q <= C K2^(4/7) Z^(5/7), so Z-time occupancy scales as Q_action^(7/5).
    q_to_z = Fraction(7, 5)

    # Energy packing requires C_j >= W^(1/2).
    energy_threshold = Fraction(1, 2)

    # If Q_action ~ R, solve R^(7/5) = W^(1/2).
    r_exp = energy_threshold / q_to_z
    assert r_exp == Fraction(5, 14)

    # Physical distance d = R / W^(1/2).
    physical_exp = r_exp - Fraction(1, 2)
    assert physical_exp == Fraction(-1, 7)

    # Check the bounded-window time exponent in C_j >= const R^(7/5)L0^(-9/5).
    # Q_action >= const R/L and GN-time interpolation contributes L^(-2/5).
    l_exp = -Fraction(7, 5) - Fraction(2, 5)
    assert l_exp == -Fraction(9, 5)

    print("remote normalized radius exponent:", r_exp, float(r_exp))
    print("physical near-zone exponent:", physical_exp, float(physical_exp))
    print("bounded-window L0 exponent:", l_exp, float(l_exp))
    print("PASS")


if __name__ == "__main__":
    main()
