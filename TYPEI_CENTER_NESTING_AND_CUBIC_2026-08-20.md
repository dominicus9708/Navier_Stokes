# Type-I Center Nesting and Cubic Interpolation — 2026-08-20

Overall status: **PARTIAL COMPACTNESS-BRIDGE CLOSURE — GLOBAL REGULARITY NOT PROVED.**

This note closes two concrete sublemmas in `TYPEI_COMPACTNESS_BRIDGE_2026-08-20.md`:

1. no-`T` natural-scale center nesting;
2. local cubic-velocity control from scale-invariant local energy and dissipation.

---

## 1. Quantitative turnover displacement

Let

\[
r_j=W_j^{-1/2},
\qquad
W_{j+1}=qW_j,
\]

and let `X_j` be the tracked core center at the `j`-th first-hitting level.

Define the dimensionless center-turnover displacement

\[
\boxed{
\mathfrak T_j
=\frac{|X_{j+1}-X_j|}{r_j}.
}
\]

A repeated event `mathfrak T_j >> 1` means that the next dangerous core is not contained in a bounded multiple of the current natural core. This is precisely a core-replacement/material-turnover event and should be included in `T_bounded`.

Therefore the **non-T center condition** is

\[
\boxed{
\sup_{j\ge j_0}\mathfrak T_j\le C_T<\infty.
}
\]

---

## 2. Geometric center nesting

Since

\[
r_{j+k}=q^{-k/2}r_j,
\]

for `m>0`,

\[
\begin{aligned}
|X_{j+m}-X_j|
&\le
\sum_{k=0}^{m-1}|X_{j+k+1}-X_{j+k}|\\
&\le
C_T\sum_{k=0}^{m-1}r_{j+k}\\
&\le
C_T r_j\sum_{k=0}^{\infty}q^{-k/2}.
\end{aligned}
\]

Hence

\[
\boxed{
|X_{j+m}-X_j|
\le
C_Xr_j,
\qquad
C_X=\frac{C_T}{1-q^{-1/2}}.
}
\]

Thus all later first-hitting cores lie inside one fixed multiple of the stage-`j` natural radius.

In particular, `X_j` is Cauchy and converges to a single physical point `X_*`, with

\[
\boxed{
|X_*-X_j|\le C_Xr_j.
}
\]

This is exactly the natural-scale spatial nesting needed for a single singular-point parabolic tower.

Therefore the center-nesting gap in the compactness bridge is closed **provided `T` is defined to include unbounded dimensionless center replacement**.

---

## 3. Parabolic nesting

On an eventual non-`H/T` branch, the rate reduction gives

\[
L_-\le L_j\le L_+,
\]

and hence

\[
\Delta t_j\asymp r_j^2.
\]

Therefore

\[
T^*-t_j
\asymp r_j^2.
\]

Together with

\[
|X_*-X_j|\lesssim r_j,
\]

this shows that the first-hitting points `(X_j,t_j)` approach `(X_*,T^*)` non-tangentially in parabolic scaling.

For every fixed `m`, the earlier stage scale satisfies

\[
r_{j-m}=q^{m/2}r_j,
\]

so after rescaling by `r_j`, the first-hitting tower covers spatial radii `R_m=q^(m/2)` and backward times comparable to `R_m^2`.

---

## 4. Local cubic interpolation

Let `v` be a divergence-free velocity in a parabolic cylinder `Q(R)=B_R x (-R^2,0)`.

For each time, the local Gagliardo--Nirenberg/Sobolev estimate gives

\[
\|v\|_{L^3(B_R)}^3
\lesssim
\|v\|_{L^2(B_R)}^{3/2}
\left(
\|\nabla v\|_{L^2(B_R)}
+R^{-1}\|v\|_{L^2(B_R)}
\right)^{3/2}.
\]

After time integration and Holder,

\[
\boxed{
C(R)
\lesssim
A(R)^{3/4}E(R)^{3/4}
+A(R)^{3/2},
}
\]

where

\[
A(R)=R^{-1}\operatorname*{ess\,sup}\int_{B_R}|v|^2,
\]

\[
C(R)=R^{-2}\int_{Q(R)}|v|^3,
\]

\[
E(R)=R^{-1}\int_{Q(R)}|\nabla v|^2.
\]

Therefore

\[
\boxed{
A(R)+E(R)\le M
\Longrightarrow
C(R)\le C(M)
}
\]

uniformly in scale.

The cubic Type-I quantity is thus **not an independent compactness gap** once the local energy and dissipation quantities are controlled.

---

## 5. Reduced compactness checklist

After this note, the expanding first-hitting ancient tower still requires three genuinely nontrivial uniform controls:

1. `A`: convert moving relative-velocity variance into a coherent scale-uniform local energy bound after fixing the drift gauge;
2. `E`: prove no-`H` plus passive remote strain gives scale-uniform local velocity-gradient/dissipation bounds over the entire tower;
3. `D`: control pressure oscillation uniformly, including the affine pressure induced by the moving frame.

`C` then follows from `A+E`, and center nesting follows directly from quantitative exclusion of `T`.

Status: **NO-T CENTER NESTING CLOSED; CUBIC VELOCITY CONTROL REDUCED TO A+E. REMAINING TYPE-I BRIDGE GAPS = DRIFT-GAUGE A, LOCAL DISSIPATION E, AND PRESSURE D.**