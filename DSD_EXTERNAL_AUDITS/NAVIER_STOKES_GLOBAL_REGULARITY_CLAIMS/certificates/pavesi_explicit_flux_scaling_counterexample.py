"""Exact finite-mode certificate against the data-independent flux estimate
claimed in Pavesi, Theorem 6.1.

The field is a real divergence-free trigonometric polynomial on T^3 with
Fourier support at ±p, ±q, ±r, where r=p+q.  At cutoff K=1 the standard
Hermitian spectral flux is nonzero.  Amplitude scaling then rules out an
absolute data-independent quadratic-energy bound for this cubic flux.
"""

from math import sqrt

p = (1, 0, 0)
q = (0, 1, 0)
r = (1, 1, 0)

# Sparse Fourier coefficients.  Conjugate symmetry makes the field real.
u = {
    p: (0j, 0j, 1 + 0j),
    (-1, 0, 0): (0j, 0j, 1 + 0j),
    q: (1 + 0j, 0j, 0j),
    (0, -1, 0): (1 + 0j, 0j, 0j),
    r: (0j, 0j, 1j),
    (-1, -1, 0): (0j, 0j, -1j),
}


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def hdot(a, b):
    return sum(x.conjugate() * y for x, y in zip(a, b))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(c, a):
    return tuple(c * x for x in a)


def norm2(v):
    return float(hdot(v, v).real)


def leray(k, v):
    kk = sum(x * x for x in k)
    kv = dot(tuple(complex(x) for x in k), v)
    if kv == 0:
        return v
    return tuple(v_i - k_i * kv / kk for k_i, v_i in zip(k, v))


def nonlinear_rhs(k):
    """F(k) = -i P_k sum_{a+b=k} (u(a)·b)u(b)."""
    s = (0j, 0j, 0j)
    for a, ua in u.items():
        b = tuple(k_i - a_i for k_i, a_i in zip(k, a))
        if b in u:
            coeff = dot(ua, tuple(complex(x) for x in b))
            s = add(s, scale(coeff, u[b]))
    return scale(-1j, leray(k, s))


# Reality and incompressibility checks.
for k, uk in u.items():
    minus_k = tuple(-x for x in k)
    assert u[minus_k] == tuple(x.conjugate() for x in uk)
    assert dot(tuple(complex(x) for x in k), uk) == 0

K = 1.0
E = 0.5 * sum(norm2(uk) for uk in u.values())
E_hi = 0.5 * sum(norm2(uk) for k, uk in u.items() if sqrt(sum(x*x for x in k)) > K)
Pi = sum(hdot(uk, nonlinear_rhs(k)).real for k, uk in u.items() if sqrt(sum(x*x for x in k)) > K)

assert E == 3.0
assert E_hi == 1.0
assert Pi == -2.0

print("K =", K)
print("E =", E)
print("E_>K =", E_hi)
print("Pi(K) =", Pi)
print("For u -> A u, claimed |Pi| <= C*sqrt(E_>K E)/K becomes")
print("2 A^3 <= sqrt(3) C_* A^2, impossible for A > sqrt(3) C_*/2.")
