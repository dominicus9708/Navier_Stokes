import argparse
import math
import numpy as np


def project_div_free(U, K):
    k2 = np.sum(K * K, axis=0)
    denom = np.where(k2 == 0.0, 1.0, k2)
    dot = np.sum(U * K, axis=0)
    out = U.copy()
    for i in range(3):
        out[i] = out[i] - K[i] * dot / denom
    out[:, k2 == 0.0] = 0.0
    return out


def build_field(N=20, cutoff=3, seed=42):
    rng = np.random.default_rng(seed)
    u0 = rng.normal(size=(3, N, N, N))
    U = np.fft.fftn(u0, axes=(1, 2, 3))

    kvals = np.fft.fftfreq(N) * N
    K = np.stack(np.meshgrid(kvals, kvals, kvals, indexing="ij"))
    mask = np.max(np.abs(K), axis=0) <= cutoff
    U *= mask
    U = project_div_free(U, K)

    grad_u_hat = np.empty((3, 3, N, N, N), dtype=complex)
    for i in range(3):
        for j in range(3):
            grad_u_hat[i, j] = 1j * K[j] * U[i]

    grad_u = np.fft.ifftn(grad_u_hat, axes=(2, 3, 4)).real
    S = 0.5 * (grad_u + np.swapaxes(grad_u, 0, 1))

    omega = np.stack(
        [
            grad_u[2, 1] - grad_u[1, 2],
            grad_u[0, 2] - grad_u[2, 0],
            grad_u[1, 0] - grad_u[0, 1],
        ]
    )

    S_hat = np.fft.fftn(S, axes=(2, 3, 4))
    omega_hat = np.fft.fftn(omega, axes=(1, 2, 3))

    dS = np.empty((3, 3, 3, N, N, N))
    domega = np.empty((3, 3, N, N, N))
    hess_omega = np.empty((3, 3, 3, N, N, N))

    for k in range(3):
        dS[k] = np.fft.ifftn(1j * K[k] * S_hat, axes=(2, 3, 4)).real
        domega[k] = np.fft.ifftn(
            1j * K[k] * omega_hat, axes=(1, 2, 3)
        ).real
        for ell in range(3):
            hess_omega[k, ell] = np.fft.ifftn(
                -K[k] * K[ell] * omega_hat, axes=(1, 2, 3)
            ).real

    lap_omega = sum(hess_omega[k, k] for k in range(3))
    return S, omega, dS, domega, hess_omega, lap_omega


def mean_integral(x):
    # The common periodic-volume factor cancels in all residual checks.
    return np.mean(x)


def compute_identities(S, omega, dS, domega, hess_omega, lap_omega):
    S_mat = np.moveaxis(S, (0, 1), (-2, -1))
    omega_vec = np.moveaxis(omega, 0, -1)

    I1 = 0.0
    I2 = 0.0
    A = 0.0
    B = 0.0
    C = 0.0

    for k in range(3):
        for ell in range(3):
            I1 += mean_integral(
                S[k, ell] * np.sum(dS[k] * dS[ell], axis=(0, 1))
            )

        Gk = np.moveaxis(dS[k], (0, 1), (-2, -1))
        I2 += mean_integral(
            np.trace(S_mat @ (Gk @ Gk), axis1=-2, axis2=-1)
        )

        eta_k = np.moveaxis(domega[k], 0, -1)
        A += mean_integral(
            np.einsum("...i,...ij,...j->...", eta_k, S_mat, eta_k)
        )
        B += mean_integral(
            np.einsum("...i,...ij,...j->...", eta_k, Gk, omega_vec)
        )

        for ell in range(3):
            C += mean_integral(
                S[k, ell] * np.sum(domega[k] * domega[ell], axis=0)
            )

    N_strain = -I1 - 2.0 * I2
    N_vort = 0.5 * (A - C)

    direct_density = np.zeros(S.shape[2:])
    for a in range(3):
        for b in range(3):
            first = np.sum(omega * hess_omega[a, b], axis=0)
            second = omega[a] * lap_omega[b]
            direct_density += S[a, b] * (first - second)
    N_hess = 0.5 * mean_integral(direct_density)

    return {
        "I1": I1,
        "I2": I2,
        "A": A,
        "B": B,
        "C": C,
        "N_strain": N_strain,
        "N_vort": N_vort,
        "N_hess": N_hess,
    }


def sharp_tensor_ratio():
    # Equality example for |K| <= sqrt(3)|S||omega|.
    S = np.diag([-1.0, -1.0, 2.0]) / math.sqrt(6.0)
    omega = np.array([0.0, 0.0, 1.0])
    K = np.empty((3, 3, 3))
    Somega = S @ omega
    for a in range(3):
        for b in range(3):
            for i in range(3):
                K[a, b, i] = (
                    omega[i] * S[a, b]
                    - (1.0 if a == b else 0.0) * Somega[i]
                )
    return np.linalg.norm(K) / (np.linalg.norm(S) * np.linalg.norm(omega))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=20)
    parser.add_argument("--cutoff", type=int, default=3)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    data = build_field(args.N, args.cutoff, args.seed)
    vals = compute_identities(*data)

    print(f"B residual                         = {vals['B']:.6e}")
    print(
        "strain-vorticity identity residual = "
        f"{vals['N_strain'] - vals['N_vort']:.6e}"
    )
    print(
        "vorticity-Hessian identity residual = "
        f"{vals['N_vort'] - vals['N_hess']:.6e}"
    )
    print(
        "sharp local tensor ratio            = "
        f"{sharp_tensor_ratio():.12f}"
    )
    print(f"sqrt(3)                             = {math.sqrt(3.0):.12f}")
    print(
        "new explicit radius coefficient C1  = "
        f"{2.0 * math.sqrt(6.0) / 9.0:.12f}"
    )
    print(
        "first-hitting radius factor          = "
        f"{math.sqrt(3.0 * math.sqrt(6.0) / 4.0):.12f}"
    )


if __name__ == "__main__":
    main()
