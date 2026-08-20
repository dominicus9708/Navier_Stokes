import math
import numpy as np


def record_aligned_density(Sdiag, a, b12, b21, b31, b32):
    s1, s2, s3 = Sdiag
    G = np.array(
        [
            [a, b12, 0.0],
            [b21, -a, 0.0],
            [b31, b32, 0.0],
        ],
        dtype=float,
    )
    S = np.diag(Sdiag)
    C = G.T @ G - G @ G.T
    n_direct = 0.5 * np.sum(S * C)
    n_formula = 0.5 * (
        (s1 - s2) * b21**2
        + (s2 - s1) * b12**2
        + (s1 - s3) * b31**2
        + (s2 - s3) * b32**2
    )
    upper = 0.5 * (s2 - s1) * np.sum(G * G)
    return n_direct, n_formula, upper


def main(seed=20260820, trials=10000):
    rng = np.random.default_rng(seed)
    max_formula_error = 0.0
    max_upper_violation = -np.inf

    for _ in range(trials):
        m = 0.1 + 3.0 * rng.random()
        x = rng.random()
        Sdiag = (-2.0 * m, m * (1.0 - x), m * (1.0 + x))
        vals = rng.normal(size=5)
        n_direct, n_formula, upper = record_aligned_density(Sdiag, *vals)
        max_formula_error = max(max_formula_error, abs(n_direct - n_formula))
        max_upper_violation = max(max_upper_violation, n_direct - upper)

    c_star = math.sqrt(3.0 / (32.0 * math.sqrt(2.0) * 30.0 ** 2.5))

    print(f"trials = {trials}")
    print(f"max exact-formula residual = {max_formula_error:.6e}")
    print(f"max aligned-upper violation = {max_upper_violation:.6e}")
    print(f"record-overlap C_* = {c_star:.12f}")

    # Middle-zero endpoint x=1: (s1,s2,s3)=(-2m,0,2m).
    # The aligned pointwise positive coefficient becomes 0.5*s3*|G|^2
    # in the unique positive b12 shear direction.
    m = 1.0
    Sdiag = (-2.0, 0.0, 2.0)
    n_direct, n_formula, upper = record_aligned_density(
        Sdiag, 0.0, 1.0, 0.0, 0.0, 0.0
    )
    print(f"middle-zero unit-shear density = {n_direct:.12f}")
    print(f"middle-zero formula density    = {n_formula:.12f}")
    print(f"middle-zero aligned upper      = {upper:.12f}")


if __name__ == "__main__":
    main()
