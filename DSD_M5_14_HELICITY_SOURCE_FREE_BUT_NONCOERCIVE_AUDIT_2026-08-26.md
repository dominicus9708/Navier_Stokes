# DSD M5-14 — Helicity: Source-Free but Noncoercive Critical Audit

Date: 2026-08-26

Status: **DERIVED SOURCE-FREE SCALE-CRITICAL PRELIMIT IDENTITY / HELICITY FAILS AS A LYAPUNOV FUNCTIONAL BECAUSE VISCOUS HELICITY DISSIPATION IS SIGN-INDEFINITE / GLOBAL HELICITY FINITENESS IS NOT AUTOMATIC ON A `1/r` W1 LIMIT / GLOBAL REGULARITY UNPROVED.**

## 1. Why helicity is the next audit

M5-13 gives a positive scale-critical prelimit quantity `dot H^{1/2}`, but its evolution retains the projected nonlinear Lamb source.

To test the opposite possibility, use helicity

\[
\mathcal H_c(U)
:=\int_{\mathbb R^3}U\cdot\Omega\,dY,
\qquad \Omega=\nabla\times U.
\]

This is exactly invariant under the 3D Navier--Stokes scaling whenever the integral is well defined.

## 2. Exact evolution on smooth finite prelimit states

For smooth decaying incompressible flow, pressure contributes nothing and the Euler nonlinearity conserves helicity. In Leray variables the similarity generator also cancels because helicity is scale critical.

Therefore

\[
\boxed{
\frac{d}{ds}\mathcal H_c(U)
=-2\nu\int \Omega\cdot(\nabla\times\Omega)\,dY.
}
\]

Thus helicity satisfies the source-free requirement that the `dot H^{1/2}` norm fails to satisfy.

## 3. The sign problem

The quantity

\[
\int \Omega\cdot(\nabla\times\Omega)
\]

has no fixed sign in general.

Hence helicity is not a positive Lyapunov functional and its viscous term is not a nonnegative dissipation functional.

M5-11 requires both

\[
\mathcal D\ge0
\]

and

\[
\mathcal D=0\Rightarrow U=0.
\]

Helicity does not provide either property on the full 3D phase space.

## 4. Helical Fourier decomposition

Use the curl eigenbasis

\[
i k\times h_\pm(k)=\pm |k|h_\pm(k),
\]

and write

\[
\widehat U(k)=u_+(k)h_+(k)+u_-(k)h_-(k).
\]

Then, up to normalization conventions,

\[
\boxed{
\|U\|_{\dot H^{1/2}}^2
=\int |k|\bigl(|u_+|^2+|u_-|^2\bigr)\,dk,
}
\]

whereas

\[
\boxed{
\mathcal H_c
=\int |k|\bigl(|u_+|^2-|u_-|^2\bigr)\,dk.
}
\]

Thus `dot H^{1/2}` is the positive sum of the two helical sectors, while helicity is their signed difference.

Likewise the viscous helicity term is the signed difference of the corresponding `|k|^3` weights.

## 5. Domain audit

The exact identity above is safe on each smooth finite prelimit state. A W1 omega-limit with a persistent `1/r` cross-radius corridor need not have finite global helicity or finite global `dot H^{1/2}` norm; logarithmic endpoint divergence is compatible with the critical scaling.

Therefore M5-14 is a **prelimit structural ledger** unless an additional critical-tightness hypothesis is supplied.

Do not infer a finite helicity value for the full W1 limit solely from finite-energy prelimit convergence.

## 6. DSD interpretation

The two most natural critical quadratic prelimit ledgers fail in complementary ways:

\[
\boxed{
\dot H^{1/2}:\quad
\text{positive/coercive}
+\text{pressure-free}
-\text{nonlinear-source-free},
}
\]

\[
\boxed{
\text{helicity}:\quad
\text{pressure-free}
+\text{nonlinear-source-free}
-\text{positive/coercive}.
}
\]

The missing property is therefore not merely a new critical norm. It is a mechanism preventing cancellation/mixing between the two helical sectors while retaining nonlinear source cancellation, together with enough critical tightness to remain meaningful on the limit.

## 7. External structural anchor

In a helical-decimated Navier--Stokes model where one helicity sign is projected out, helicity becomes sign-definite and equivalent to the `H^{1/2}` critical norm; global regularity for that decimated model is known (Biferale--Titi, 2013).

This does **not** imply regularity for the full Navier--Stokes equations, because the full dynamics contain both helical sectors and their interactions.

## 8. Updated M5 target

A successful strict critical Lyapunov construction would have to combine:

1. positivity/coercivity comparable to a critical norm;
2. exact pressure cancellation;
3. exact or sign-controlled nonlinear transfer;
4. positive viscous dissipation;
5. critical tightness sufficient to survive the prelimit-to-W1 passage.

No such functional is derived here for the full 3D Navier--Stokes system.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
