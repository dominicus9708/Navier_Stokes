# Base projective defect: time concentration and palinstrophy activation

Date: 2026-08-13

Status: **DERIVED COROLLARY OF EXTERNAL ANISOTROPIC CRITERION + STANDARD HARMONIC-ANALYSIS BOUND / GLOBAL REGULARITY NOT PROVED**.

This note specializes the energy-weighted projective inequality to derivative order `k=0`, where the projective defect is attached to the original vorticity and can therefore be connected directly to the external locally anisotropic vorticity criterion.

## 1. Base projective defect

Let

\[
E(t)=\|\omega(t)\|_2^2,
\qquad
J(t)=1-\operatorname{tr}(C_\omega(t)^2),
\]

and define

\[
\boxed{
D(t)=E(t)J(t).
}
\]

The covariance comparison with the optimal-axis defect `Pi` gives

\[
\frac12J\le\Pi\le\frac32J.
\]

A corollary of Evan Miller's locally anisotropic vorticity criterion therefore yields the necessary blowup condition

\[
\boxed{
D\notin L^2(0,T^*)
}
\]

for a hypothetical finite-time singularity in the smooth finite-energy whole-space track.

## 2. Base energy-weighted projective inequality

At `k=0`, the differentiated nonlinear forcing is simply

\[
F_0=S\omega.
\]

The general inequality becomes

\[
\boxed{
\dot D
+2\nu P
\left[
J_1+\Delta_0^2
\right]
\le
2\sqrt5\sqrt D\,\|S\omega\|_2,
}
\]

where

\[
P=E_1=\|\nabla\omega\|_2^2
\]

and

\[
\Delta_0=\|C_1-C_0\|_F.
\]

Dropping the nonnegative viscous term gives, wherever `D>0`,

\[
\boxed{
\frac d{dt}\sqrt D
\le
\sqrt5\|S\omega\|_2.
}
\]

The inequality extends across zero by the usual regularization `sqrt(D+epsilon)` and limiting argument.

## 3. A necessary nonlinear-source divergence

If

\[
\int_0^{T^*}\|S\omega\|_2dt<\infty,
\]

then `sqrt(D)` and therefore `D` remain bounded up to `T*`.

But

\[
0\le J\le\frac23,
\]

so

\[
D\le\frac23E.
\]

The kinetic-energy dissipation inequality gives

\[
\int_0^{T^*}E(t)dt<\infty.
\]

Hence `D in L1_t`; boundedness of `D` then implies

\[
D\in L^2(0,T^*).
\]

This satisfies the Miller-derived projective criterion and excludes finite-time blowup.

Therefore a hypothetical blowup must satisfy

\[
\boxed{
\int_0^{T^*}\|S\omega\|_2dt=\infty.
}
\]

This is recorded as a derived necessary condition, not as a novelty claim.

## 4. Standard Sobolev/Riesz estimate

The strain is a zero-order singular-integral transform of vorticity, so for `1<p<infinity`,

\[
\|S\|_p\lesssim\|\omega\|_p.
\]

Using Hölder with exponents `3` and `6`,

\[
\|S\omega\|_2
\le
\|S\|_3\|\omega\|_6
\lesssim
\|\omega\|_3\|\omega\|_6.
\]

Interpolate

\[
\|\omega\|_3
\le
\|\omega\|_2^{1/2}
\|\omega\|_6^{1/2},
\]

and use Sobolev

\[
\|\omega\|_6\lesssim\|\nabla\omega\|_2.
\]

Thus

\[
\boxed{
\|S\omega\|_2
\lesssim
E^{1/4}P^{3/4}.
}
\]

Define the base derivative ratio

\[
\boxed{
r_0=P/E.}
\]

Then

\[
\boxed{
\|S\omega\|_2
\lesssim
E\,r_0^{3/4}.
}
\]

## 5. Residual consequence

Since

\[
\int_0^{T^*}E(t)dt<\infty,
\]

a residual singularity must make the derivative ratio sufficiently active that

\[
\boxed{
\int_0^{T^*}
E(t)r_0(t)^{3/4}dt
=\infty
}
\]

is not ruled out by the upper estimate.

Strictly speaking, the divergence of the upper bound is only a **necessary possibility** for the divergence of `||S omega||_2`; the inequality does not reverse. The logically valid statement is:

- if `E r_0^(3/4)` is integrable, then `||S omega||_2` is integrable;
- therefore integrability of `E r_0^(3/4)` excludes blowup through the projective/Miller route.

Hence a hypothetical blowup must satisfy

\[
\boxed{
E r_0^{3/4}\notin L^1(0,T^*).
}
\]

## 6. Interpretation

The base pairwise cross-axis defect `D_0` cannot become non-`L2` merely through repeated harmless directional rearrangement.

A residual singularity must sustain a nonintegrable amount of strain-vorticity forcing, which in turn requires sufficiently strong activation of the palinstrophy/enstrophy ratio.

This directly connects the external `k=0` anisotropic gate to the derivative-radius hierarchy.

The next geometric target is stronger: exploit the Biot--Savart structure of `S omega` itself so that local projective alignment `J_r` depletes the near-field stretching kernel rather than bounding it only through the scalar Sobolev estimate above.

Status: **OPEN LOCAL PROJECTIVE DEPLETION OF STRETCHING**.
