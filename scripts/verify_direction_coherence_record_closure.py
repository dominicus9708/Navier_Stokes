#!/usr/bin/env python3
"""Verify the direction-coherence / record-stretching closure constants."""

from __future__ import annotations

import math


def main() -> None:
    h = 0.4
    a0 = 3.0 * math.sqrt(2.0) / 8.0
    b1_sq = (a0 + h) ** 2 + 0.5
    lstar = 756.0 * math.log(2.0) * b1_sq / (157.0 * math.pi**2) + 3.0 / (4.0 * math.pi**2)
    delta_star = (math.log(2.0) / lstar - h) / 3.0

    assert abs(lstar - 0.5377803705715904) < 5e-13
    assert abs(delta_star - 0.2963012774299293) < 5e-13

    lower_time = math.log(2.0) / (3.0 * delta_star + h)
    assert abs(lower_time - lstar) < 5e-13

    print(f"L_*(0.4) = {lstar:.15f}")
    print(f"delta_*(0.4) = {delta_star:.15f}")
    print(f"boundary equality time = {lower_time:.15f}")
    print("PASS")


if __name__ == "__main__":
    main()
