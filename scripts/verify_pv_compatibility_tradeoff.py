import math
import numpy as np


def compatible_mode(k, a):
    k = np.asarray(k, dtype=float)
    a = np.asarray(a, dtype=float)
    k = k / np.linalg.norm(k)
    a = a - k * np.dot(k, a)
    a = a / np.linalg.norm(a)
    A = 0.5 * (np.outer(k, a) + np.outer(a, k))
    return k, a, A


def combined_covariance_mode(k, a):
    k, a, A = compatible_mode(k, a)
    anorm2 = np.sum(A * A)
    Csp = np.outer(k, k)
    Crg = (A @ A) / anorm2
    C = (Csp + 2.0 * Crg) / 3.0
    return C


def q_tensor(n):
    n = np.asarray(n, dtype=float)
    n = n / np.linalg.norm(n)
    return (np.eye(3) - 3.0 * np.outer(n, n)) / math.sqrt(6.0)


def projection_overlap(theta):
    # n=e1, khat in e1-e2 plane, and choose polarization a in that plane
    # perpendicular to khat to maximize |Q_n : A|.
    n = np.array([1.0, 0.0, 0.0])
    k = np.array([math.cos(theta), math.sin(theta), 0.0])
    a = np.array([-math.sin(theta), math.cos(theta), 0.0])
    _, _, A = compatible_mode(k, a)
    A /= np.linalg.norm(A)
    Q = q_tensor(n)
    return abs(np.sum(Q * A))


def theta_static(x):
    return 0.5 + 0.5 / math.sqrt(1.0 + x * x / 3.0)


def theta_nonnormal(x):
    return (3.0 + x) / (2.0 * math.sqrt(3.0 + x * x))


def coherence_gap(C):
    return (math.sqrt(C + 1.0 / 9.0) - math.sqrt(C)) ** 2


def main():
    # Single compatible Fourier mode: exact eigenvalues 2/3, 1/3, 0.
    C = combined_covariance_mode([1, 0, 0], [0, 1, 0])
    eig = np.linalg.eigvalsh(C)[::-1]
    print("single-mode combined covariance eigenvalues:", eig)
    print("lambda_max target 2/3:", 2.0 / 3.0)

    # Fourier max-mid projection gap.
    thetas = np.linspace(0.0, math.pi / 2.0, 20001)
    overlaps = np.array([projection_overlap(t) for t in thetas])
    imax = int(np.argmax(overlaps))
    print("max |P_Vk Q_n| numerical:", overlaps[imax])
    print("angle at max (deg):", thetas[imax] * 180.0 / math.pi)
    print("sqrt(3)/2 target:", math.sqrt(3.0) / 2.0)
    print("minimum distance target 1/2:", 0.5)

    # Double-saturation crossing.
    xstar = 3.0 * (math.sqrt(3.0) - 1.0) / 4.0
    thetastar = (15.0 + 6.0 * math.sqrt(3.0)) / 26.0
    print("x_star:", xstar)
    print("theta_static(x_star):", theta_static(xstar))
    print("theta_nonnormal(x_star):", theta_nonnormal(xstar))
    print("theta_star exact target:", thetastar)
    print("double-saturation fractional tax:", 1.0 - thetastar)

    # Example class-level covariance gaps.
    for Ccoh in [0.0, 0.1, 1.0, 10.0, 100.0]:
        print(f"C_coh={Ccoh:7.3f}  delta_cov={coherence_gap(Ccoh):.12g}")


if __name__ == "__main__":
    main()
