# Survival parameter and source--Hermite scale gap

Date: 2026-08-14

Status: **DERIVED ALGEBRAIC COMPRESSION OF THE SURVIVING LOW-CURVATURE BRANCH / NO GLOBAL REGULARITY CLAIM**.

This note compresses the current surviving intermediate branch into one dimensionless parameter and shows that the same parameter simultaneously measures:

1. how small the per-step physical dissipation may become;
2. how wide the gap is between the source-optimal radius and the finite-energy Hermite ceiling;
3. how small a fraction of the normalized kinetic-energy budget may be occupied by the active residual state.

## 1. Surviving pulse variables

Write the residual peak as

\[
m=W^{-1/3}\Lambda,
\qquad
\Lambda\to\infty,
\qquad
m\ll1.
\]

Let

\[
\Theta=\frac{V_\omega}{B}
\]

be the vorticity share of the residual gradient variance on the responsible source interval.

The typed residual-source estimate gives

\[
|J|\lesssim_K B\sqrt\Theta.
\]

The previous dissipation rearrangement showed that an infinitely surviving disjoint cascade requires

\[
\boxed{
\Lambda\Theta^{5/6}\to\infty.
}
\]

Define the single survival parameter

\[
\boxed{
H:=\Lambda\Theta^{5/6}.
}
\]

Thus every still-surviving low-curvature sequence has

\[
H\to\infty.
\]

## 2. Source-optimal radius

An order-one residual source contribution requires a time mass satisfying

\[
\int B\sqrt\Theta\,d\tau\gtrsim1.
\]

If the responsible state is capped by `B<=m` and has approximately fixed vorticity share `Theta`, the shortest possible responsible duration is

\[
\Delta\tau_S
\asymp
\frac1{m\sqrt\Theta}.
\]

On the bounded-affine Gaussian branch,

\[
R(\tau)\asymp_K\sqrt\tau.
\]

Hence the smallest radius capable of housing a unit source budget at the peak amplitude is

\[
\boxed{
R_S
\asymp
(m\sqrt\Theta)^{-1/2}.
}
\]

Substituting `m=W^(-1/3)Lambda`,

\[
\boxed{
R_S
\asymp
W^{1/6}\Lambda^{-1/2}\Theta^{-1/4}.
}
\]

This is the **source-optimal radius**: placing the same source mass farther backward, at larger Gaussian radius, only increases the Gaussian-volume dissipation cost.

## 3. Finite-energy Hermite ceiling

The low-curvature finite-energy Hermite ridge gives

\[
BR^5\lesssim W^{1/2}.
\]

At the peak `B=m`, the largest low-curvature radius is therefore

\[
R_H
\asymp
\left(\frac{W^{1/2}}m\right)^{1/5}.
\]

Hence

\[
\boxed{
R_H
\asymp
W^{1/6}\Lambda^{-1/5}.
}
\]

## 4. Exact scale-gap identity

The ratio between the Hermite ceiling and the source-optimal radius is

\[
\frac{R_H}{R_S}
\asymp
\Lambda^{3/10}\Theta^{1/4}.
\]

Since

\[
\Theta^{1/4}
=(\Theta^{5/6})^{3/10},
\]

we obtain the compact identity

\[
\boxed{
\frac{R_H}{R_S}
\asymp
H^{3/10}.
}
\]

Thus the very condition required for the residual branch to survive the existing dissipation lower bound,

\[
H\to\infty,
\]

is exactly the condition that opens a widening scale corridor

\[
R_S\ll R_H.
\]

## 5. Dissipation ledger in terms of H

The typed physical-dissipation lower bound is

\[
D_{\rm phys}
\gtrsim
W^{-1/2}m^{-3/2}\Theta^{-5/4}.
\]

Substituting `m=W^(-1/3)Lambda`,

\[
D_{\rm phys}
\gtrsim
\Lambda^{-3/2}\Theta^{-5/4}.
\]

But

\[
H^{-3/2}
=\Lambda^{-3/2}\Theta^{-5/4}.
\]

Therefore

\[
\boxed{
D_{\rm phys}\gtrsim H^{-3/2}.
}
\]

This makes the survival mechanism transparent: the branch escapes the finite total-dissipation budget only by forcing `H` to infinity.

## 6. Location penalty

Suppose a fixed fraction of the required source mass is supported only at radii

\[
R\ge zR_S,
\qquad z\ge1.
\]

The Gaussian volume factor grows like `R^3`, so the same rearrangement gives the strengthened cost

\[
\boxed{
D_{\rm phys}
\gtrsim
H^{-3/2}z^3.
}
\]

The largest low-curvature value permitted by the Hermite ridge is

\[
z_{\max}
\asymp
\frac{R_H}{R_S}
\asymp
H^{3/10}.
\]

Even if the source were forced all the way to the Hermite ceiling, the present estimates would give only

\[
D_{\rm phys}
\gtrsim
H^{-3/2}H^{9/10}
=
\boxed{H^{-3/5}}.
\]

This still tends to zero and therefore does not by itself contradict finite total physical dissipation.

This is a useful negative result: **the existing Hermite ceiling plus source-location penalty is still short of closure.**

## 7. Active residual kinetic-energy fraction

At the source-optimal radius,

\[
\frac{mR_S^5}{W^{1/2}}
=
\Lambda^{-3/2}\Theta^{-5/4}
=
H^{-3/2}.
\]

Hence

\[
\boxed{
\Xi_S
:=
\frac{mR_S^5}{W^{1/2}}
\asymp
H^{-3/2}.
}
\]

The same parameter that measures the minimum per-step physical dissipation also measures the fraction of the normalized kinetic-energy budget occupied by the source-optimal residual state.

At the Hermite ceiling,

\[
\Xi_H\asymp1.
\]

Therefore the surviving branch can be described as a migration through the corridor

\[
\Xi:H^{-3/2}\longrightarrow1,
\qquad
R:R_S\longrightarrow R_H.
\]

## 8. Revised target

The remaining low-curvature branch is no longer characterized merely by `Lambda -> infinity`.

Its natural control parameter is

\[
\boxed{H=\Lambda\Theta^{5/6}\to\infty.}
\]

Any successful closure must prevent at least one of the following from occurring indefinitely:

1. the active residual energy fraction falling to `H^(-3/2)`;
2. the source radius separating from the Hermite ceiling by `H^(3/10)`;
3. the nonlinear source repeatedly reorganizing through the resulting widening corridor without paying more than `H^(-3/2)` to `H^(-3/5)` physical dissipation per step.

This suggests a sharper next goal than the earlier generic `BR^4` target: prove a scale-time nonlinear packing, tightness, or saturation inequality that supplies a positive power of `H` beyond the present ledgers.

Status: **SURVIVING BRANCH COMPRESSED TO H / EXACT SOURCE--HERMITE SCALE GAP IDENTIFIED / ADDITIONAL POSITIVE H-GAIN STILL REQUIRED.**
