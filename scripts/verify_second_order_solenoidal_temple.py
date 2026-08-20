import math


def temple_constants():
    q = 5.0 ** (1.0 / 3.0)
    e0 = 15.0 * q / 4.0
    e1 = 31.0 * q / 4.0
    mean_v = q / 2.0
    var_v = 11.0 / (2.0 * q)
    mu = e0 + mean_v
    lam_lb = mu - var_v / (e1 - mu)

    c2_lb = 2.0 * lam_lb ** 1.5 / (3.0 * math.sqrt(3.0))
    coeff = math.sqrt(3.0 / 2.0) / c2_lb
    radius = math.sqrt(1.0 / coeff)

    return q, e0, e1, mean_v, var_v, mu, lam_lb, c2_lb, coeff, radius


def finite_difference_ground_state(n=4000, rmax=8.0):
    try:
        import numpy as np
        import scipy.sparse as sp
        import scipy.sparse.linalg as spla
    except ImportError:
        return None

    h = rmax / (n + 1)
    r = h * np.arange(1, n + 1)

    main = 2.0 / h**2 + 2.0 / r**2 + r**4
    off = -1.0 / h**2 * np.ones(n - 1)
    operator = sp.diags([off, main, off], [-1, 0, 1], format="csr")

    value = spla.eigsh(
        operator,
        k=1,
        which="SA",
        return_eigenvectors=False,
        tol=1.0e-11,
        maxiter=100000,
    )[0]

    c2 = 2.0 * value ** 1.5 / (3.0 * math.sqrt(3.0))
    coeff = math.sqrt(3.0 / 2.0) / c2
    radius = math.sqrt(1.0 / coeff)
    return value, c2, coeff, radius


def main():
    vals = temple_constants()
    labels = [
        "q",
        "E0",
        "E1",
        "<V>",
        "Var(V)",
        "mu",
        "Temple lambda lower",
        "C2 solenoidal lower",
        "P_V radius coefficient upper",
        "first-hitting radius factor lower",
    ]

    for name, value in zip(labels, vals):
        print(f"{name:34s} = {value:.12f}")

    numeric = finite_difference_ground_state()
    if numeric is None:
        print("SciPy unavailable: skipped numerical radial eigenvalue diagnostic.")
    else:
        value, c2, coeff, radius = numeric
        print("\nFinite-difference diagnostic (not used as proof):")
        print(f"lambda_0 numeric                   = {value:.12f}")
        print(f"C2 numeric                         = {c2:.12f}")
        print(f"P_V coefficient numeric            = {coeff:.12f}")
        print(f"radius factor numeric              = {radius:.12f}")


if __name__ == "__main__":
    main()
