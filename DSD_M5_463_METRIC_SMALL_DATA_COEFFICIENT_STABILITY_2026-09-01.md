# DSD M5-463 — Small critical-data stability under metric coefficient convergence

Date: 2026-09-01

Status: **UNIFORM CONVERGENCE OF THE FINITE-DIMENSIONAL METRIC COEFFICIENTS IMPLIES CONVERGENCE OF THE LINEAR METRIC STOKES PROPAGATORS AND KATO BILINEAR OPERATORS / THE SMALL CRITICAL-DATA FIXED POINT IS THEREFORE STABLE UNDER JOINT INITIAL-DATA AND COEFFICIENT PERTURBATIONS / THIS REMOVES ANOTHER PART OF THE M5-459 TRANSFER GAP, BUT LARGE WEAK-`L3` STABILITY AND TERMINAL REGULARITY REMAIN OPEN / GLOBAL REGULARITY REMAINS UNPROVED.**

Let `(C_n,G_n)` be uniformly elliptic coefficient histories on `[s,T]` with

\[
C_n=G_n^{-1},
\qquad
C_n\to C,
\qquad
G_n\to G
\]

uniformly in time.

## 1. Heat covariance convergence

Define

\[
Q_n(t,r)=\int_r^tG_n(\tau)d\tau.
\]

Then

\[
\boxed{
Q_n(t,r)\to Q(t,r)
}
\]

uniformly on compact `(t,r)` sets with `s<=r<t<=T`.

The Fourier heat multipliers

\[
e^{-\xi^TQ_n(t,r)\xi}
\]

therefore converge pointwise to the limit multiplier and share common Gaussian upper bounds from uniform ellipticity.

## 2. Metric Biot--Savart symbol convergence

M5-452 constructs `B_C` by inverting the constant-coefficient div-curl symbol. Since this inversion is smooth in `C` inside a compact ellipticity class,

\[
\boxed{
\mathcal B_{C_n(t)}(\xi)
\to
\mathcal B_{C(t)}(\xi)
}
\]

uniformly on the unit sphere together with finitely many angular derivatives.

The same holds for the order-zero symbol

\[
\mathcal B_{C_n(t)}(\xi)
[i\xi\times]C_n(s).
\]

## 3. Linear propagator stability

For smooth compactly supported data `f`, dominated convergence in Fourier space and the uniform heat/Mikhlin bounds give

\[
\boxed{
\mathcal S_{C_n}(t,s)f
\to
\mathcal S_C(t,s)f
}
\]

in every subcritical `Lq` norm for `t>s`, locally uniformly away from the initial time.

Density plus the uniform M5-461 estimates extends this to the critical Kato data classes used below.

## 4. Bilinear operator stability

The M5-462 Duhamel kernel is

\[
\mathcal K_{C_n}(t,r)
=
-\mathcal B_{C_n(t)}P_{G_n}(t,r)
\operatorname{curl}\operatorname{div}(\cdot\, C_n(r)\cdot).
\]

Its kernel converges for every `t>r` and satisfies the common bound

\[
\|\mathcal K_{C_n}(t,r)F\|_q
\le
C(t-r)^{-\frac12-\frac32(1/p-1/q)}\|F\|_p.
\]

Hence for fixed `u,v` in a Kato space `X_q`, dominated convergence in the time integral gives

\[
\boxed{
\mathcal B_{C_n}(u,v)
\to
\mathcal B_C(u,v)
\quad\text{in }X_q
}
\]

on compact time intervals, after the standard epsilon-splitting near the initial endpoint.

## 5. Fixed-point stability

Let `a_n -> a` in a critical small-data class and assume

\[
\sup_n\|a_n\|_{crit}<\varepsilon_*(\kappa)
\]

below the uniform contraction threshold from M5-462.

Let `w_n` and `w` be the corresponding metric mild solutions. Then

\[
w_n=\mathcal S_{C_n}a_n+\mathcal B_{C_n}(w_n,w_n),
\]

\[
w=\mathcal S_Ca+\mathcal B_C(w,w).
\]

Subtracting and using the uniform contraction constant yields

\[
\boxed{
\|w_n-w\|_{X_q}\to0.
}
\]

Thus the small critical-data solution map is stable under joint data/coefficient convergence.

## 6. Significance for the Liouville transfer

The M5-459 missing package is reduced further:

- explicit metric heat/Stokes estimates: DONE (M5-457/461);
- uniform critical bilinear estimates: DONE (M5-462);
- small-data critical perturbation and coefficient stability: DONE (M5-463);
- large weak-`L^{3,infinity}` solution stability: OPEN;
- terminal Besov regularity for that large-data class: OPEN;
- final ancient Liouville theorem: OPEN.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]