# DSD M5-467 — Ancient zoom-out coefficient-dilation firewall

Date: 2026-09-01

Status: **FINITE-INTERVAL METRIC WEAK-CRITICAL STABILITY DOES NOT BY ITSELF TRANSFER ALBRITTON--BARKER THEOREM 4.1 / THEIR ANCIENT LIOUVILLE ARGUMENT PARABOLICALLY ZOOMS OUT ALONG `t_k -> -INFINITY`, WHILE THE METRIC COEFFICIENT HISTORY IS RESCALED TO `C(|t_k|t),G(|t_k|t)` AND LOSES THE EQUICONTINUITY USED IN M5-460 / THE ANCIENT METRIC LANE THEREFORE HAS A DISTINCT COEFFICIENT-DILATION/HOMOGENIZATION GAP / GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Standard ancient zoom-out

Albritton--Barker Theorem 4.1 rescales a standard ancient Navier--Stokes solution along `t_k -> -infinity` by

\[
v^{(k)}(x,t)
=\lambda_k v(\lambda_kx,\lambda_k^2t),
\qquad
\lambda_k:=\sqrt{|t_k|}.
\]

The standard Navier--Stokes coefficients are invariant under this rescaling.

## 2. Metric coefficient transformation

For the M5-451 metric system, the same parabolic scaling produces

\[
\boxed{
C_k(t)=C(\lambda_k^2t),
\qquad
G_k(t)=G(\lambda_k^2t).
}
\]

Even if

\[
\|C'\|+\|G'\|\le M
\]

on the original ancient history,

\[
\boxed{
\|C_k'\|+\|G_k'\|
\le
\lambda_k^2M,
}
\]

so the equi-Lipschitz compactness of M5-460 is destroyed by zoom-out.

Thus one cannot simply combine finite-interval coefficient stability with the standard ancient rescaling.

## 3. What compactness remains

Uniform ellipticity still gives weak-* compactness

\[
G_k\stackrel{*}{\rightharpoonup}\bar G
\quad\text{in }L^\infty_{loc,t}
\]

after subsequences. Also

\[
Q_k(t,s)
:=\int_s^tG_k(\tau)d\tau
\]

has uniformly Lipschitz primitives and therefore converges locally uniformly after subselection.

This is enough for convergence of the **linear heat covariances**.

However the instantaneous metric curl inverse depends on

\[
C_k(t)=G_k(t)^{-1}
\]

nonlinearly. Weak-* convergence of `G_k` does not imply strong convergence of `C_k` or convergence to `bar G^{-1}`.

Thus the nonlinear velocity-vorticity law can retain unresolved fast coefficient oscillation even if the heat propagator homogenizes.

## 4. Correct ancient metric gap

The `W1_metric` Liouville program therefore needs at least one of:

1. **coefficient stabilization:** show `C(t)` approaches a constant or a compact slowly varying orbit at ancient times;
2. **homogenization:** prove that rapidly varying determinant-one coefficient histories have an effective metric system compatible with the nonlinear div-curl law;
3. **zoom-out-free rigidity:** prove the ancient Liouville theorem by a method based on time translation/recurrence rather than parabolic dilation.

None is presently established.

## 5. Why this matters

Without this firewall one could incorrectly state:

\[
\text{metric weak-}L^3
+\text{finite-interval stability}
\Longrightarrow
\text{Albritton--Barker Liouville}.
\]

That implication is not yet justified.

The finite-interval stability program M5-461--466 remains useful, but the ancient coefficient-dilation problem is a separate hard theorem.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]