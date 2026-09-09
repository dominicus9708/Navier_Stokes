# DSD M17-461 — Second-moment asymmetry equals sign-dependent mean coefficient-magnitude dispersion plus the small palinstrophy defect

Date: 2026-09-10  
Canonical ID: **M17-461**

Status: **ACTIVE EXACT MOMENT DECOMPOSITION / COEFFICIENT-SCALE DISPERSION REDUCTION / M17-459 SOURCE AUDIT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input

M17-459 gives

\[
\dot A+2J_0
=-2C_{0\sigma}+G_A+2S_A+2\Delta Q,
\]

where

\[
A=K_++K_-,
\qquad
P=K_--K_+,
\]

and

\[
\Delta Q:=Q_+-Q_-.
\]

M17-458 shows that on a surviving diffuse good-time branch, `P` is much smaller than the individual sign moments `K_+` and `K_-` in time average.

The present module identifies exactly what a non-small `Delta Q` means in that regime.

## 2. Sign-weighted mean coefficient magnitudes

Whenever `K_+>0` and `K_->0`, define

\[
\boxed{
\bar\kappa_+
:=\frac{Q_+}{K_+}
=\frac{\int\kappa_+^2\rho^2dx}
{\int\kappa_+\rho^2dx},
}
\]

\[
\boxed{
\bar\kappa_-
:=\frac{Q_-}{K_-}
=\frac{\int\kappa_-^2\rho^2dx}
{\int\kappa_-\rho^2dx}.
}
\]

These are not arbitrary spatial averages. They are the coefficient magnitudes seen by the positive and negative first-moment measures themselves.

Thus

\[
Q_+=\bar\kappa_+K_+,
\qquad
Q_-=\bar\kappa_-K_-.
\]

Since

\[
K_+=\frac{A-P}{2},
\qquad
K_-=\frac{A+P}{2},
\]

we obtain the exact identity

\[
\boxed{
\Delta Q
=\frac A2(\bar\kappa_+-\bar\kappa_-)
-\frac P2(\bar\kappa_++\bar\kappa_-).
}
\]

## 3. Canonical dispersion variable

Define

\[
\boxed{
\mathfrak M_\kappa
:=\bar\kappa_+-\bar\kappa_-.
}
\]

Then

\[
\boxed{
\Delta Q
=\frac A2\mathfrak M_\kappa
-\frac P2(\bar\kappa_++\bar\kappa_-).
}
\]

Hence on the M17-458 branch, where `P/A -> 0` in the relevant averaged sense,

\[
\boxed{
\Delta Q
=\frac A2\mathfrak M_\kappa+o(A)
}
\]

provided the normalized coefficient magnitudes remain bounded.

Therefore a persistent order-one second-moment source is equivalent, up to the already small palinstrophy defect, to a persistent sign-dependent mean coefficient-magnitude split.

## 4. Quantitative implication under coefficient compactness

Assume

\[
0<A_*\le A\le A^*<\infty,
\qquad
0\le\bar\kappa_\pm\le K_*.
\]

Then

\[
|\Delta Q|
\le
\frac{A^*}{2}|\mathfrak M_\kappa|
+K_*P.
\]

Conversely,

\[
\boxed{
|\mathfrak M_\kappa|
\ge
\frac{2}{A^*}\bigl(|\Delta Q|-K_*P\bigr)_+.
}
\]

Thus if

\[
|\Delta Q|\ge\delta_*>0
\]

while

\[
P\to0,
\]

then for sufficiently late records

\[
\boxed{
|\mathfrak M_\kappa|
\ge c_{\delta,A}>0.
}
\]

## 5. Common-magnitude shell closes the second-moment source

Suppose both signs live in one narrow magnitude shell

\[
\kappa_*,\varepsilon:
\qquad
\kappa_\pm\in
[\kappa_*-\varepsilon,\kappa_*+\varepsilon]
\]

on the weighted populations carrying `K_+` and `K_-`.

Then

\[
|\bar\kappa_+-\bar\kappa_-|
\le2\varepsilon,
\]

and

\[
\bar\kappa_++\bar\kappa_-
\le2(\kappa_*+\varepsilon).
\]

Therefore

\[
\boxed{
|\Delta Q|
\le
A\varepsilon
+(\kappa_*+\varepsilon)P.
}
\]

Consequently a common narrowing coefficient shell together with the M17-458 `P -> 0` cancellation removes `Delta Q` as an order-one source-return term.

## 6. What survives: sign-dependent intrinsic-scale dispersion

The only way for `Delta Q` to remain non-small while `P` is small is therefore

\[
\boxed{
G_{\rm sign\text{-}dependent\ coefficient\ magnitude/scale\ dispersion}.
}
\]

Because the intrinsic coefficient scale is

\[
r_\kappa=|\kappa|^{-1/2},
\]

an order-one split in `bar kappa_+` and `bar kappa_-` is equivalently an order-one split in the coefficient scales preferentially occupied by the two signs.

This is a genuine geometric/dynamical distinction, not merely a different notation for the first-moment imbalance.

## 7. Relation to the M17-443--447 redistribution architecture

A sign-dependent magnitude split requires the positive and negative weighted populations to occupy separated coefficient classes.

If those populations are connected through a region with nondegenerate normalized amplitude and regular transverse geometry, the coefficient must cross intermediate levels and the transition returns to coefficient-gradient / regular-zero payer mechanisms.

If the transition is hidden in a low-amplitude bridge, M17-446 applies and the direct coefficient-gradient payer may disappear. M17-447 then shows that a robust low-amplitude separator with uniform transverse Poincare geometry is itself a palinstrophy payer.

Thus the surviving magnitude-dispersion branch is already typed:

\[
\boxed{
\begin{aligned}
G_{\mathfrak M_\kappa}
\Longrightarrow{}&
G_{\rm coefficient/zero\text{-}corridor\ payer}\\
&\lor G_{\rm low\text{-}amplitude\ bottleneck}\
&\lor G_{\rm remote\ sign\ population}\
&\lor G_{\rm spectral/high\text{-}jet/chart/genealogy\ loss}.
\end{aligned}
}
\]

No new untyped PDE source is introduced.

## 8. Interaction with M17-459 absolute-moment balance

Substituting the exact decomposition into M17-459 gives

\[
\boxed{
\dot A+2J_0
=-2C_{0\sigma}+G_A+2S_A
+A\mathfrak M_\kappa
-P(\bar\kappa_++\bar\kappa_-).
}
\]

On a near-perfect M17-458 sign-cancellation branch the final term is small. Therefore the lower-order source-return problem is reduced to

\[
\boxed{
-2C_{0\sigma}
+G_A
+2S_A
+A\mathfrak M_\kappa.
}
\]

M17-460 already classifies the first term conditionally as palinstrophy or trace/high-jet loss.

The genuinely remaining lower-order terms are therefore:

1. geometry-source return `G_A`;
2. strain-weighted absolute sign moment `S_A`;
3. sign-dependent coefficient-magnitude dispersion `mathfrak M_kappa`.

## 9. DSD audit role

DSD is used only to select a partition-independent moment descriptor and prevent the logical error `first-moment cancellation => second-moment cancellation`. The proof is elementary algebra on the exact CE-H weighted moments.

## 10. Audit verdict

**PASS — the second-moment asymmetry is no longer an untyped source.**

It is exactly the sign-dependent mean coefficient-magnitude dispersion plus a term proportional to the already small palinstrophy imbalance.

Therefore a retained diffuse survivor with nearly equal positive and negative first moments can use `Delta Q` as an order-one source only by separating the coefficient magnitudes/scales occupied by the two signs. That branch returns to the already explicit coefficient-gradient, low-amplitude bottleneck, remote-population, high-jet, chart, or genealogy exits.

The next narrow target is the remaining strain-weighted source `S_A` and geometry source `G_A`: determine whether their persistent common-sign replenishment can be reduced to the certified deformation/palinstrophy resources or whether an additional correlation descriptor is needed.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
