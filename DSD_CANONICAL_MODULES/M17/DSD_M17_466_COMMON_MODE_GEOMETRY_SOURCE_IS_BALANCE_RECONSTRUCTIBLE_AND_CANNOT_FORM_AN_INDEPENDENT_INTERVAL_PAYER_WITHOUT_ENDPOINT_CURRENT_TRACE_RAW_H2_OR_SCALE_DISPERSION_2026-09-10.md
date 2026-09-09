# M17-466 — Common-mode geometry source is balance-reconstructible and cannot form an independent interval payer

**Date:** 2026-09-10  
**Status:** ACTIVE COMMON-MODE BALANCE REDUCTION / GEOMETRY PROVENANCE FIREWALL

## 1. Scope

This module continues M17-459–465 on the exact CE-H branch. It does **not** reconstruct or guess the termwise formula for the M17-339 geometry remainder \(\mathcal R_{\rm geom}\). The termwise provenance firewall from M17-463 remains in force.

The only input used here is the already-certified common-mode balance from M17-465.

Let
\[
K_\pm(t)=\int \kappa_\pm\rho^2\,dx,
\qquad
A:=K_++K_-,
\qquad
P:=K_--K_+,
\]
with
\[
J_0:=\int \rho^2\delta(\kappa)|\nabla\kappa|^2\,dx\ge0,
\]
and let \(C_{0\sigma}\), \(S_A\), \(\Delta Q\), and \(G_{\rm cm}\) denote the zero-level strain trace, strain-weighted first-moment source, second-moment sign asymmetry, and sign-even/common-mode geometry contribution defined in M17-459–465.

The exact \(A\)-balance is
\[
\boxed{
\dot A+2J_0
=
-2C_{0\sigma}
+2G_{\rm cm}
+2S_A
+2\Delta Q.
}
\]

## 2. Exact pointwise-in-time reconstruction

Rearranging gives
\[
\boxed{
2G_{\rm cm}
=
\dot A
+2J_0
+2C_{0\sigma}
-2S_A
-2\Delta Q.
}
\]

Therefore \(G_{\rm cm}\) is **termwise-provenance-unclassified** but it is not algebraically independent of the other balance channels.

This statement is exact at every time for which the balance is valid; no sign assumption on \(G_{\rm cm}\), \(C_{0\sigma}\), \(S_A\), or \(\Delta Q\) is used.

## 3. Exact interval reconstruction

For any interval \(I=[t_0,t_1]\),
\[
\boxed{
2\int_I G_{\rm cm}\,dt
=
A(t_1)-A(t_0)
+2\int_IJ_0\,dt
+2\int_IC_{0\sigma}\,dt
-2\int_IS_A\,dt
-2\int_I\Delta Q\,dt.
}
\]

Hence
\[
\boxed{
\begin{aligned}
2\left|\int_I G_{\rm cm}\,dt\right|
\le{}&
|A(t_1)-A(t_0)|
+2\int_IJ_0\,dt\\
&+2\left|\int_IC_{0\sigma}\,dt\right|
+2\left|\int_IS_A\,dt\right|
+2\left|\int_I\Delta Q\,dt\right|.
\end{aligned}
}
\]

Consequently, an order-one interval-integrated common-mode geometry contribution cannot occur while all five right-hand-side channels vanish.

Equivalently, persistent interval common-mode replenishment requires at least one of
\[
\boxed{
\Delta A,
\quad
J_0,
\quad
C_{0\sigma},
\quad
S_A,
\quad
\Delta Q
}
\]
to remain non-negligible on the same interval.

## 4. Combination with M17-460–462

The existing reductions give:

1. M17-460:
\[
C_{0\sigma}
\Longrightarrow
\text{palinstrophy/trace payment}
\ \lor\ 
\text{trace/high-jet decompactification},
\]
under the stated finite-jet trace-thickening hypotheses.

2. M17-461:
\[
\Delta Q
\Longrightarrow
\text{positive/negative coefficient-magnitude or intrinsic-scale dispersion},
\]
when the first-moment sign imbalance \(P\) is small.

3. M17-462:
\[
|S_A|
\lesssim
M_\rho E^{1/2}H_{\rm raw}^{1/2},
\]
so persistent \(S_A\) is a raw-\(H^2\) payer under the amplitude/enstrophy hypotheses of that module.

Thus the interval-integrated common-mode branch reduces to
\[
\boxed{
\begin{aligned}
G_{\rm cm}^{\rm interval}
\Longrightarrow{}&
G_{\Delta A}
\lor
G_{J_0}\\
&\lor
G_{\rm palinstrophy/trace\text{-}high\text{-}jet}\\
&\lor
G_{\rm raw\text{-}H^2}\\
&\lor
G_{\rm sign\text{-}dependent\ coefficient\text{-}scale\ dispersion}.
\end{aligned}
}
\]

## 5. What is closed

The sign-even geometry channel is no longer an **independent interval-integrated terminal payer**. Any persistent interval contribution is exactly accompanied by endpoint/current/trace/strain/scale-dispersion bookkeeping.

This closes the source-return question only at the balance-accounting level.

## 6. What is NOT closed

The following remain OPEN:

- the verified termwise formula/provenance of the M17-339 remainder \(\mathcal R_{\rm geom}\);
- local or instantaneous classification of individual geometry-remainder terms;
- whether \(\Delta A\), \(J_0\), trace/high-jet, raw-\(H^2\), or coefficient-scale dispersion yields a non-summable ancestral cost;
- parent-to-M17 genealogy/interface/domain persistence;
- ROOT-CERT and the non-CE-H root branches.

In particular this module does **not** prove a contradiction.

## 7. Audit firewall

Do not infer from this balance reconstruction that
\[
G_{\rm cm}=0,
\]
or that \(\mathcal R_{\rm geom}\) is termwise controlled by palinstrophy/raw-\(H^2\). Only its common-mode **interval total** is reconstructed by the exact balance.

Do not merge endpoint \(\Delta A\) with a spacetime bulk ledger until its certified scaling is checked separately.

## 8. Next target

Audit the ancestry scaling of every term in the \(A\)-balance. In particular determine the scaling of
\[
A,
\quad
\int J_0dt,
\quad
\int C_{0\sigma}dt,
\quad
\int S_A dt,
\quad
\int \Delta Qdt,
\quad
\int G_{\rm cm}dt,
\]
under the certified Navier–Stokes rescaling. This decides whether the M17-466 payer reduction can escape the record-scale summability firewall.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
