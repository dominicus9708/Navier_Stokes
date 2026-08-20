"""Low-mode periodic toy search for the P_V H1 efficiency quotient.

This is a diagnostic only. It does NOT approximate the full R^3 first-hitting
variational class and is not evidence of regularity.

Convention:
- domain: [0, 2*pi)^3
- Fourier wave numbers are integer vectors
- random velocity modes are projected to k dot u_hat(k) = 0
- fields are normalized so max_x |omega(x)| = 1

The computed quotient is

    eta_VI = - int S:(M_sp + 2 M_rg) / int |Delta S|^2,

where
    (M_sp)_{kl} = partial_k S : partial_l S,
    M_rg = sum_k (partial_k S)^2.
"""

from __future__ import annotations

import argparse
import numpy as np


def random_divfree_velocity_hat(
    n: int,
    nmodes: int,
    kmax: int,
    rng: np.random.Generator,
) -> np.ndarray:
    uhat = np.zeros((n, n, n, 3), dtype=np.complex128)
    candidates = [
        (i, j, k)
        for i in range(-kmax, kmax + 1)
        for j in range(-kmax, kmax + 1)
        for k in range(-kmax, kmax + 1)
        if (i, j, k) != (0, 0, 0)
    ]
    rng.shuffle(candidates)
    used = set()
    count = 0

    for kv in candidates:
        if count >= nmodes:
            break
        neg = tuple(-x for x in kv)
        key = min(kv, neg)
        if key in used:
            continue
        used.add(key)

        kvec = np.asarray(kv, dtype=float)
        coeff = rng.normal(size=3) + 1j * rng.normal(size=3)
        coeff -= kvec * np.dot(kvec, coeff) / np.dot(kvec, kvec)
        coeff *= np.exp(-0.2 * np.dot(kvec, kvec))

        idx = tuple(x % n for x in kv)
        nidx = tuple((-x) % n for x in kv)
        uhat[idx] = coeff
        uhat[nidx] = np.conj(coeff)
        count += 1

    return uhat


def eta_vi(uhat: np.ndarray) -> float:
    n = uhat.shape[0]
    # Integer Fourier modes for the 2*pi-periodic torus.
    kk = np.fft.fftfreq(n, d=1.0 / n)

    grad_u = np.zeros((n, n, n, 3, 3), dtype=float)
    for j in range(3):
        shape = [1, 1, 1]
        shape[j] = n
        factor = 1j * kk.reshape(shape)
        grad_u[..., :, j] = np.fft.ifftn(
            uhat * factor[..., None], axes=(0, 1, 2)
        ).real

    strain = 0.5 * (grad_u + np.swapaxes(grad_u, -1, -2))
    omega = np.stack(
        [
            grad_u[..., 2, 1] - grad_u[..., 1, 2],
            grad_u[..., 0, 2] - grad_u[..., 2, 0],
            grad_u[..., 1, 0] - grad_u[..., 0, 1],
        ],
        axis=-1,
    )

    omega_max = np.linalg.norm(omega, axis=-1).max()
    if omega_max <= 1e-14:
        return float("nan")
    strain = strain / omega_max

    shat = np.fft.fftn(strain, axes=(0, 1, 2))
    grad_s = np.zeros((n, n, n, 3, 3, 3), dtype=float)
    k2 = np.zeros((n, n, n), dtype=float)

    for k in range(3):
        shape = [1, 1, 1]
        shape[k] = n
        factor = 1j * kk.reshape(shape)
        grad_s[..., k, :, :] = np.fft.ifftn(
            shat * factor[..., None, None], axes=(0, 1, 2)
        ).real
        k2 += kk.reshape(shape) ** 2

    lap_s = np.fft.ifftn(
        -k2[..., None, None] * shat, axes=(0, 1, 2)
    ).real

    m_sp = np.einsum("...kij,...lij->...kl", grad_s, grad_s)
    m_rg = np.einsum("...kij,...kjm->...im", grad_s, grad_s)

    numerator_density = -np.einsum(
        "...ij,...ij->...", strain, m_sp + 2.0 * m_rg
    )
    numerator = numerator_density.mean()
    denominator = np.square(lap_s).sum(axis=(-1, -2)).mean()

    if denominator <= 1e-18:
        return float("nan")
    return float(numerator / denominator)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=2500)
    parser.add_argument("--grid", type=int, default=10)
    parser.add_argument("--kmax", type=int, default=2)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--min-modes", type=int, default=4)
    parser.add_argument("--max-modes", type=int, default=15)
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    values = []
    best = -np.inf
    best_modes = None

    for _ in range(args.samples):
        nmodes = int(rng.integers(args.min_modes, args.max_modes + 1))
        uhat = random_divfree_velocity_hat(
            args.grid, nmodes, args.kmax, rng
        )
        value = eta_vi(uhat)
        if np.isfinite(value):
            values.append(value)
            if value > best:
                best = value
                best_modes = nmodes

    arr = np.asarray(values)
    print(f"samples={arr.size}")
    print(f"best_eta={best:.12g}")
    print(f"best_nmodes={best_modes}")
    if arr.size:
        for p in (50.0, 90.0, 99.0, 99.9):
            print(f"p{p:g}={np.percentile(arr, p):.12g}")


if __name__ == "__main__":
    main()
