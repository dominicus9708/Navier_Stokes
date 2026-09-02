# DSD M5-597 — Harmonic-eigenline return forces axial strain or magnitude-gradient charge

Date: 2026-09-03

Status: **ON THE NONDEGENERATE SAME-MARKER CE-H BRANCH, THE RETURN-CYCLE AMPLITUDE IDENTITY GIVES A QUANTITATIVE DICHOTOMY. EITHER THE MEAN AXIAL STRAIN IS AT LEAST 1/2, OR THE MEAN PARALLEL DIFFUSION `Delta rho/rho` EXCEEDS 1/2. THE LATTER FORCES POSITIVE-LAPLACIAN EVENTS, WHICH SMOOTHLY THICKEN AND, BY A LOCAL H^{-1} TEST, FORCE A FIXED MAGNITUDE-GRADIENT L2 CHARGE IN THE SAME PRODUCTION CARRIER. THUS PARALLEL DIFFUSION IS NOT A NEW FREE CHANNEL: IT REDUCES TO STRONG AXIAL STRAIN OR MAGNITUDE-GRADIENT STRUCTURE, UNLESS MARKER MIGRATION OCCURS. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Inputs

Use the M5-595 CE-H branch:

\[
\tau=0,
\qquad
\mathcal D_\xi=0,
\qquad
\Sigma\xi=\sigma\xi,
\]

on the production-paying carrier.

Use the M5-596 nondegenerate same-marker return branch:

\[
0<\rho_-\le\rho(\theta_j)\le\rho_+<\infty
\]

at recurrent finite-depth payer returns, and

\[
\boxed{
\left\langle
\sigma+rac{\Delta\rho}{\rho}-|\nabla\xi|^2
\right\rangle_{ret}=1.
}
\]

Set

\[
d:=\frac{\Delta\rho}{\rho},
\qquad
G:=|\nabla\xi|^2\ge0.
\]

Then

\[
\boxed{1=\langle\sigma\rangle+\langle d\rangle-\langle G\rangle.}
\]

## 2. Quantitative half-threshold dichotomy

Either

\[
\boxed{\langle\sigma\rangle\ge\frac12}
\]

or

\[
\langle\sigma\rangle<\frac12.
\]

In the second case,

\[
\langle d\rangle
=1-\langle\sigma\rangle+\langle G\rangle
>
\frac12.
\]

Therefore

\[
\boxed{
\text{CE-H same-marker}
\Longrightarrow
H_\sigma
\lor
H_{\Delta\rho},
}
\]

where

\[
H_\sigma:
\langle\sigma\rangle\ge\frac12,
\]

and

\[
H_{\Delta\rho}:
\left\langle\frac{\Delta\rho}{\rho}\right\rangle>\frac12.
\]

The numerical threshold \(1/2\) is not special; it is chosen to make both branches quantitative.

## 3. Strong-axial branch

On \(H_\sigma\), Jensen gives

\[
\langle\sigma^2\rangle
\ge
\langle\sigma\rangle^2
\ge
\frac14.
\]

M5-550's trace-free strain inequality with \(\tau=0\) gives

\[
|\Sigma|^2
\ge
\frac32\sigma^2.
\]

Hence along the return-cycle marker measure,

\[
\boxed{
\langle|\Sigma|^2\rangle
\ge
\frac38.
}
\]

Uniform spacetime continuity then thickens positive-strain marker events into a fixed local spacetime strain-square charge.

This is a quantitative threshold, not a contradiction.

## 4. Positive-parallel-diffusion branch has positive events

On \(H_{\Delta\rho}\), the compact hull supplies a finite upper bound

\[
|d|\le D_*.
\]

Since

\[
\langle d\rangle>\frac12,
\]

the set of return-cycle times with

\[
\boxed{d\ge\frac14}
\]

has positive lower density depending only on \(D_*\).

At those events the nondegenerate marker bound gives

\[
\boxed{
\Delta\rho
=d\rho
\ge
\frac14\rho_-
=:c_\Delta>0.
}
\]

## 5. Smooth thickening of the positive Laplacian

The all-order compact-hull bounds give a uniform bound on \(\nabla\Delta\rho\) in the active carrier.

Therefore there is a fixed radius \(r_\Delta>0\) such that on

\[
B_{r_\Delta}(Y(\theta)),
\]

\[
\boxed{
\Delta\rho\ge\frac12c_\Delta>0.
}
\]

Thus positive parallel diffusion is not confined to a single point.

## 6. Positive Laplacian forces magnitude-gradient L2 charge

Let \(B=B_{r_\Delta}\) and choose the positive Dirichlet test function \(\varphi\) solving

\[
-\Delta\varphi=1
\quad\text{in }B,
\qquad
\varphi=0
\quad\text{on }\partial B.
\]

Since \(\varphi>0\) inside \(B\),

\[
\int_B\varphi\Delta\rho\,dy
\ge
\frac12c_\Delta
\int_B\varphi\,dy.
\]

Integration by parts, with \(\varphi=0\) on the boundary, gives

\[
\int_B\varphi\Delta\rho
=-
\int_B\nabla\varphi\cdot\nabla\rho.
\]

Hence by Cauchy-Schwarz,

\[
\|\nabla\rho\|_{L^2(B)}
\ge
\frac{
(c_\Delta/2)\int_B\varphi
}{
\|\nabla\varphi\|_2
}
=:c_{mag}>0.
\]

Therefore

\[
\boxed{
\int_B|\nabla\rho|^2dy
\ge
c_{mag}^2>0.
}
\]

This is a fixed same-carrier magnitude-gradient charge.

## 7. Connection to M5-588

M5-588's M branch was characterized by positive magnitude-gradient charge

\[
P_{mag}=\int|\nabla\rho|^2.
\]

The present calculation shows that CE-H parallel-diffusion recurrence, if it is needed strongly enough to keep the marker amplitude recurrent, **automatically regenerates the M-type magnitude-gradient structure locally in the production payer carrier**.

Thus

\[
\boxed{
H_{\Delta\rho}
\Longrightarrow
M_{local}^{mag}.
}
\]

## 8. Marker-migration alternative remains separate

If the active representative changes between returns, M5-596 does not allow the amplitude telescoping used above.

That branch remains

\[
\boxed{
H_{migration}^{surface-current/palinstrophy}.
}
\]

It is not silently included in the same-marker conclusion.

## 9. Updated CE-H reduction

The harmonic-eigenline branch now satisfies

\[
\boxed{
\text{CE-H}
\Longrightarrow
H_{migration}
\lor
H_\sigma
\lor
M_{local}^{mag}.
}
\]

Thus the only same-marker CE-H survivor without migration is forced to pay either

1. a fixed strong axial-strain-square charge, or
2. a fixed local magnitude-gradient charge.

Neither is yet contradictory, but the supposedly free parallel diffusion channel has disappeared.

## 10. Next target

The remaining branches now all carry explicit positive local charges on the same production-linked recurrent subsystem:

- CP-E: positive net transverse derivative remainder;
- CP-S: positive transverse strain-square;
- CE-T: equal positive transverse strain/tension;
- CE-H: strong axial strain or magnitude gradient;
- marker migration: surface-current/palinstrophy charge.

The next high-value step is to place all of these charges in one finite event-level budget and ask whether a single bounded-enstrophy recurrent carrier can pay every branch without forcing a replacement/export event.

Status: **PARALLEL DIFFUSION HAS BEEN REDUCED TO ALREADY TYPED POSITIVE STRUCTURAL CHARGES. THE HARD CORE IS NOW A FINITE MENU OF SAME-EVENT PAYER MECHANISMS RATHER THAN AN UNCONTROLLED VECTOR/SCALAR DYNAMICS SPLIT. GLOBAL REGULARITY REMAINS UNPROVED.**