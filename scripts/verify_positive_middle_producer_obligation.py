#!/usr/bin/env python3
"""Verify constants in the positive-middle determinant producer obligation.

Algebraic/scaling audit only; not a regularity proof.
"""

from __future__ import annotations

import math


def main() -> None:
    q = 2.0
    c_z = 64.0 * math.sqrt(2.0) * math.pi / 105.0

    # K2,+ = 4/rho0^2, so K2,+^(-3/2) = rho0^3/8.
    zstar_coeff = c_z / 8.0
    expected_zstar = 8.0 * math.sqrt(2.0) * math.pi / 105.0
    assert abs(zstar_coeff - expected_zstar) < 1e-14

    cumulative_coeff = zstar_coeff / 8.0
    limsup_stage_coeff = ((math.sqrt(q) - 1.0) / math.sqrt(q)) * cumulative_coeff
    expected_stage_coeff = (math.sqrt(2.0) - 1.0) * math.pi / 105.0

    assert abs(limsup_stage_coeff - expected_stage_coeff) < 1e-14

    print(f"C_Z = {c_z:.15f}")
    print(f"z_* / rho0^3 = {zstar_coeff:.15f}")
    print(f"cumulative D_+ coefficient = {cumulative_coeff:.15f}")
    print(f"q=2 limsup A_+ coefficient = {limsup_stage_coeff:.15f}")
    print("PASS")


if __name__ == "__main__":
    main()
