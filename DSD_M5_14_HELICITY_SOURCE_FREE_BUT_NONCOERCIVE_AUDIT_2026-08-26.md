# DSD M5-14 — Helicity: Source-Free but Noncoercive Critical Audit

Date: 2026-08-26

Status: **DERIVED SOURCE-FREE SCALE-CRITICAL IDENTITY / HELICITY FAILS AS A LYAPUNOV FUNCTIONAL BECAUSE VISCOUS HELICITY DISSIPATION IS SIGN-INDEFINITE / GLOBAL REGULARITY UNPROVED.**

## 1. Why helicity is the next audit

M5-13 gives a positive scale-critical quantity `dot H^{1/2}`, but its evolution retains the projected nonlinear Lamb source.

To test the opposite possibility, use helicity

\[
\mathcal H_c(U)
:=\int_{\mathbb R^3}U\cdot\Omega\,dY,
\qquad \Omega=\nabla\times U.
\]

This is exactly invariant under the 3D Navier--Stokes scaling.

## 2. Exact evolution

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

## 5. DSD interpretation

The two most natural critical quadratic ledgers fail in complementary ways:

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

The missing property is therefore not merely a new critical norm. It is a mechanism preventing cancellation/mixing between the two helical sectors while retaining nonlinear source cancellation.

## 6. External structural anchor

In a helical-decimated Navier--Stokes model where one helicity sign is projected out, helicity becomes sign-definite and equivalent to the `H^{1/2}` critical norm; global regularity for that decimated model is known (Biferale--Titi, 2013).

This does **not** imply regularity for the full Navier--Stokes equations, because the full dynamics contain both helical sectors and their interactions.

## 7. Updated M5 target

A successful strict critical Lyapunov construction would have to combine the strengths of the previous two ledgers:

1. positivity/coercivity comparable to a critical norm such as `dot H^{1/2}`;
2. exact pressure cancellation;
3. exact or sign-controlled nonlinear transfer;
4. positive viscous dissipation.

No such functional is derived here for the full 3D Navier--Stokes system.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
