# DSD M5-34 — Threshold Pressure-Tail Remainder

Date: 2026-08-27

Status: **DERIVED DIRECT HALF-ABSORPTION OF THE THRESHOLD PRESSURE FLUX / THE ONLY REMAINDER IS A SCALE-CRITICAL HIGH-AMPLITUDE PRESSURE-TAIL DENSITY / GLOBAL REGULARITY UNPROVED.**

## 1. Setup

For a smooth finite-energy normalized state `V`, let

\[
a=|V|,
\qquad
\Sigma_\lambda=\{a=\lambda\}.
\]

The nonsmooth threshold ledger of M5-31 is

\[
\partial_tE_\lambda
+\nu D_\lambda^{surf}
=J_P(\lambda),
\]

where

\[
J_P(\lambda)
=
\int_{\Sigma_\lambda}
\Pi\,V\cdot n_\lambda\,dS,
\]

and

\[
D_\lambda^{surf}
=
\int_{a>\lambda}|\nabla V|^2dz
+
\lambda\int_{\Sigma_\lambda}|\nabla a|dS.
\]

At the level surface `|V|=lambda`,

\[
|V\cdot n_\lambda|\le\lambda.
\]

## 2. Pressure superlevel tail

Define

\[
\boxed{
Q_P(\lambda)
:=
\int_{a>\lambda}|\Pi|^2dz.
}
\]

By coarea, for regular levels,

\[
\boxed{
-Q_P'(\lambda)
=
\int_{\Sigma_\lambda}
\frac{|\Pi|^2}{|\nabla a|}\,dS.
}
\]

## 3. Surface Cauchy--Schwarz

First,

\[
|J_P(\lambda)|
\le
\lambda
\int_{\Sigma_\lambda}|\Pi|dS.
\]

Insert the factors `|grad a|^{1/2}` and `|grad a|^{-1/2}`:

\[
\left(
\int_{\Sigma_\lambda}|\Pi|dS
\right)^2
\le
\left(
\int_{\Sigma_\lambda}
\frac{|\Pi|^2}{|\nabla a|}dS
\right)
\left(
\int_{\Sigma_\lambda}|\nabla a|dS
\right).
\]

Therefore

\[
|J_P(\lambda)|^2
\le
\lambda^2
[-Q_P'(\lambda)]
\left(
\int_{\Sigma_\lambda}|\nabla a|dS
\right).
\]

Since

\[
D_\lambda^{surf}
\ge
\lambda
\int_{\Sigma_\lambda}|\nabla a|dS,
\]

we obtain

\[
\boxed{
|J_P(\lambda)|^2
\le
\lambda
D_\lambda^{surf}
[-Q_P'(\lambda)].
}
\]

## 4. Direct viscous half-absorption

Young's inequality gives

\[
\boxed{
|J_P(\lambda)|
\le
\frac\nu2D_\lambda^{surf}
+
\frac1{2\nu}
\lambda[-Q_P'(\lambda)].
}
\]

Thus at every regular threshold, half of the viscous coefficient can be used unconditionally. The only remaining payer is the pressure-tail density

\[
\boxed{
\mathcal R_P(\lambda)
:=
\lambda[-Q_P'(\lambda)]\ge0.
}
\]

The threshold gain therefore satisfies

\[
\boxed{
G(\lambda)
=J_P(\lambda)-\nu D_\lambda^{surf}
\le
-\frac\nu2D_\lambda^{surf}
+
\frac1{2\nu}\mathcal R_P(\lambda).
}
\]

## 5. Integration over all amplitude levels

Integrating the remainder,

\[
\int_0^\infty
\lambda[-Q_P'(\lambda)]d\lambda
=
\int_0^\infty Q_P(\lambda)d\lambda,
\]

assuming the standard boundary decay.

Layer cake then gives

\[
\boxed{
\int_0^\infty Q_P(\lambda)d\lambda
=
\int |V|\,|\Pi|^2dz.
}
\]

Consequently the global `p=3` pressure work obeys the estimate

\[
\boxed{
|F_P|
\le
\frac\nu2D_3
+
\frac1{2\nu}
\int |V|\,|\Pi|^2dz.
}
\]

## 6. Consequence on a positive-residue W1 endpoint

The exact invariant endpoint identity is

\[
\langle F_P\rangle
=
\nu\langle D_3\rangle
+
\frac{\mathscr R_3}{6}.
\]

Combining with the preceding upper estimate gives the necessary pressure-tail floor

\[
\boxed{
\left\langle
\int |V|\,|\Pi|^2dz
\right\rangle
\ge
\nu^2\langle D_3\rangle
+
\frac{\nu\mathscr R_3}{3}.
}
\]

Thus a positive critical defect requires a quantitatively large scale-critical weighted pressure tail.

## 7. Scaling audit

Under the physical Navier--Stokes scaling

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\qquad
p_\lambda=\lambda^2p(\lambda x,\lambda^2t),
\]

both

\[
D_3
\]

and

\[
\int |u|\,|p|^2dx
\]

scale like `lambda^2`; after multiplication by `dt` they are critical.

Hence the remainder is not subcritical bookkeeping. It is a genuine endpoint quantity.

## 8. DSD reduction

The M5 formation source is now routed as

\[
\boxed{
\text{threshold--Hodge commutator work}
\Longrightarrow
\text{viscous half-absorption}
+
\text{weighted pressure-tail remainder}.
}
\]

This remainder is not an independent source: it is the part of the pressure field large enough on high-amplitude states to prevent complete viscous absorption.

## 9. What remains

To close this route one would need a standard-mathematics estimate forcing

\[
\int |V|\,|\Pi|^2
<
\nu^2D_3
\]

with sufficient strictness, or a time-integrability/tightness theorem for the weighted pressure tail that contradicts the W1 floor.

No such unconditional estimate is proved here.

Thus M5 is not closed, but the direct commutator absorption problem has been reduced to one positive scale-critical pressure-tail quantity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
