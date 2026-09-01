# DSD M5-458 — Determinant-one diffusion preserves 3D heat-volume smoothing

Date: 2026-09-01

Status: **THE AFFINE-PULLBACK DIFFUSION METRIC SATISFIES `det G=1`, WHICH FORCES THE TIME-INTEGRATED HEAT COVARIANCE TO HAVE DETERMINANT AT LEAST `(t-s)^3` EVEN WITHOUT A UNIFORM CONDITION-NUMBER BOUND / THUS METRIC DEGENERACY CANNOT DESTROY TOTAL THREE-DIMENSIONAL GAUSSIAN VOLUME SMOOTHING; ITS ONLY POSSIBLE LOSS IS DIRECTIONAL/DERIVATIVE SMOOTHING / GLOBAL REGULARITY REMAINS UNPROVED.**

The linear metric heat propagator from M5-457 has covariance

\[
Q(t,s):=\int_s^tG(\tau)d\tau,
\qquad G(\tau)=G(\tau)^T>0,
\qquad \det G(\tau)=1.
\]

For positive definite `3x3` matrices, Minkowski's determinant inequality gives

\[
\det(A+B)^{1/3}
\ge
\det A^{1/3}+\det B^{1/3}.
\]

Approximating the integral by Riemann sums and passing to the limit yields

\[
\boxed{
\det Q(t,s)^{1/3}
\ge
\int_s^t\det G(\tau)^{1/3}d\tau
=t-s.
}
\]

Hence

\[
\boxed{
\det Q(t,s)\ge (t-s)^3.
}
\]

The Gaussian kernel is

\[
K_{t,s}(x)
=(4\pi)^{-3/2}(\det Q)^{-1/2}
\exp\left(-\frac14x^TQ^{-1}x\right).
\]

Therefore

\[
\boxed{
\|K_{t,s}\|_\infty
\le
C(t-s)^{-3/2},
}
\]

and

\[
\boxed{
\|P_G(t,s)f\|_\infty
\le
C(t-s)^{-3/2}\|f\|_1.
}
\]

Similarly

\[
\boxed{
\|P_G(t,s)f\|_\infty
\le
C(t-s)^{-3/4}\|f\|_2.
}
\]

These bounds require only `det G=1`, not a pointwise lower eigenvalue bound.

What can still fail is derivative smoothing. For example

\[
\|\nabla K_{t,s}\|

\]

depends on `Q^{-1/2}` and therefore on the smallest eigenvalue of the integrated covariance. Thus the metric-degeneracy branch is refined to

\[
\boxed{
H_{metric\ degeneracy}
=H_{directional\ diffusion\ loss},
}
\]

rather than loss of total heat-volume smoothing.

This distinction will be used in the next audit: determine whether the dual-source/transverse-vorticity geometry forces occupation of enough independent directions to prevent persistent directional diffusion loss.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]