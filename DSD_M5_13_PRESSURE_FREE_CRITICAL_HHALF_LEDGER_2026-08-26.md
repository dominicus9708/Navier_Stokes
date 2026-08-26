# DSD M5-13 — Pressure-Free Critical H^{1/2} Ledger

Date: 2026-08-26

Status: **DERIVED CRITICAL PRESSURE-FREE PRELIMIT LEDGER / SMALL CRITICAL NORM CLOSES BY VISCOSITY / GLOBAL `dot H^{1/2}` FINITENESS IS NOT AUTOMATIC ON A `1/r` W1 OMEGA-LIMIT / GLOBAL REGULARITY UNPROVED.**

## 1. Motivation

M5-12 shows that scalar isotropic localization necessarily creates pressure work unless it collapses to ordinary kinetic energy. The next candidate class should therefore eliminate pressure by divergence-free projection rather than by scalar cancellation.

Let

\[
\Lambda=(-\Delta)^{1/2},
\qquad
\mathcal H_{1/2}(U)
:=\frac12\|\Lambda^{1/2}U\|_2^2.
\]

This is exactly scale invariant for 3D Navier--Stokes.

## 2. Exact critical ledger on smooth finite prelimit states

For every smooth finite-energy prelimit state for which the displayed critical norms are finite, the Leray equation is

\[
U_s-\nu\Delta U+(U\cdot\nabla)U
+\frac12U+\frac12Y\cdot\nabla U+\nabla P=0,
\qquad \nabla\cdot U=0.
\]

Apply the Leray projector `P` and pair with `Lambda U`.

Pressure vanishes because `Lambda U` is divergence free and the projector is orthogonal/self-adjoint on the relevant class.

The linear similarity generator also gives zero contribution at Sobolev index `1/2`, exactly because `dot H^{1/2}` is scaling critical.

Using

\[
(U\cdot\nabla)U
=\Omega\times U+\nabla(|U|^2/2),
\]

define the solenoidal Lamb force

\[
L_s:=\mathbb P(\Omega\times U).
\]

Then

\[
\boxed{
\frac{d}{ds}\mathcal H_{1/2}(U)
+\nu\|\Lambda^{3/2}U\|_2^2
=-\langle L_s,\Lambda U\rangle.
}
\]

Thus this prelimit ledger is free of both pressure work and similarity-coordinate source terms. The only source is the genuine projected nonlinear cascade.

## 3. Standard critical estimate

The critical product estimate gives

\[
\boxed{
|\langle L_s,\Lambda U\rangle|
\le
C_{FK}
\|\Lambda^{1/2}U\|_2
\|\Lambda^{3/2}U\|_2^2.
}
\]

Hence if

\[
\|\Lambda^{1/2}U\|_2<\nu/C_{FK},
\]

then

\[
\frac{d}{ds}\mathcal H_{1/2}
+c\nu\|\Lambda^{3/2}U\|_2^2\le0.
\]

This is the familiar critical-smallness mechanism behind Fujita--Kato theory.

## 4. Why this does not close M5

The W1 survivor is a **large critical** endpoint. No preceding module forces the prelimit critical Sobolev norm below the small-data threshold.

For the one-scale infrared dilation family

\[
U_R(Y)=R^{-1}\phi(Y/R),
\]

one has exactly

\[
\boxed{
\|U_R\|_{\dot H^{1/2}}
=\|\phi\|_{\dot H^{1/2}}.
}
\]

Thus `dot H^{1/2}` sees the critical dilation defect that `L^p`, `p>3`, misses, but it does not make that defect small.

## 5. Domain audit: do not automatically evaluate the global norm on the W1 limit

A genuine cross-radius `1/r` critical corridor contains order-one critical content on infinitely many logarithmic scales. Exact homogeneous `1/r` behavior is borderline for `dot H^{1/2}` and can produce logarithmic divergence.

Therefore this file must **not** assume that every positive-defect W1 omega-limit belongs globally to `dot H^{1/2}`.

The exact ledger above is safe on each smooth finite prelimit state. Passing it to a W1 omega-limit requires an additional critical-tightness or truncation argument, which is itself part of M5.

Thus

\[
\boxed{
\text{prelimit }\dot H^{1/2}\text{ ledger is exact}
\quad\not\Rightarrow\quad
\text{global finite }\dot H^{1/2}\text{ W1 limit}.
}
\]

## 6. DSD interpretation

M5-12 and M5-13 together separate two obstructions:

\[
\boxed{
\text{scalar localization}
\Rightarrow
\text{pressure source},
}
\]

whereas

\[
\boxed{
\text{critical Hodge-projected prelimit functional}
\Rightarrow
\text{pressure removed but nonlinear cascade remains}.
}
\]

Therefore pressure itself is not the final obstruction. After pressure is eliminated exactly, the large critical projected Lamb cascade remains on the prelimit track.

## 7. Updated target

Any strict critical Lyapunov route must now do more than remove pressure. It must also provide a sign or absorption mechanism for

\[
\boxed{
\langle \mathbb P(\Omega\times U),\Lambda U\rangle
}
\]

without assuming either smallness or an unproved global critical norm bound on the W1 limit.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
