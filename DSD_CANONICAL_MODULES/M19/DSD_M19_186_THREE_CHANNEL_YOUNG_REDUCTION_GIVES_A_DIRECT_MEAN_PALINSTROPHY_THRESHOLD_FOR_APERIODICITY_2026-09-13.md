# M19-186 — Three-channel Young reduction gives a direct mean-palinstrophy threshold for aperiodicity

**Date:** 2026-09-13  
**Status:** ACTIVE CALCULATION / EXPLICIT SUFFICIENT THRESHOLD

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-185

A genuinely aperiodic quotient survivor requires at least three observable neutral hard channels: two quotient directions plus the nonzero time tangent.

For the clean `a=2` choice, set

\[
\Pi:=\langle P_U\rangle.
\]

M19-182 gives

\[
\mathfrak A
\le K_A Z_+^{7/20}\Pi^{3/20},
\qquad
\mathfrak B_2
\le K_B\Pi^{1/2},
\]

where `K_A,K_B` collect only the fixed functional-inequality constants of the certified corridor.

For three total channels,

\[
A_3:=3^{-2/5}\mathfrak A,
\qquad
B_3:=3^{-1/6}\mathfrak B_2.
\]

The exact sufficient condition is

\[
\sup_{x\ge0}
\left(A_3x^{3/5}+B_3x^{1/4}-\nu x\right)
<\frac14.
\]

## 2. Closed Young bound

Split

\[
\nu x=\frac\nu2x+\frac\nu2x.
\]

For `0<r<1`,

\[
\sup_{x\ge0}(cx^r-\mu x)
=(1-r)r^{r/(1-r)}c^{1/(1-r)}\mu^{-r/(1-r)}.
\]

### Local term

For `r=3/5`,

\[
\sup_x\left(A_3x^{3/5}-\frac\nu2x\right)
=\frac25\left(\frac35\right)^{3/2}
A_3^{5/2}
\left(\frac\nu2\right)^{-3/2}.
\]

Using

\[
A_3^{5/2}
\le
3^{-1}K_A^{5/2}Z_+^{7/8}\Pi^{3/8},
\]

this is

\[
\le K_1\nu^{-3/2}Z_+^{7/8}\Pi^{3/8},
\]

where

\[
K_1
:=
\frac25\left(\frac35\right)^{3/2}
2^{3/2}3^{-1}K_A^{5/2}.
\]

### Nonlocal term

For `r=1/4`,

\[
\sup_x\left(B_3x^{1/4}-\frac\nu2x\right)
=\frac34\left(\frac14\right)^{1/3}
B_3^{4/3}
\left(\frac\nu2\right)^{-1/3}.
\]

Since

\[
B_3^{4/3}
\le
3^{-2/9}K_B^{4/3}\Pi^{2/3},
\]

we get

\[
\le K_2\nu^{-1/3}\Pi^{2/3},
\]

with

\[
K_2
:=
\frac34\,2^{-1/3}3^{-2/9}K_B^{4/3}.
\]

## 3. Direct palinstrophy criterion

Therefore a fully explicit sufficient condition for quotient hard dimension `N<=1` is

\[
\boxed{
K_1\nu^{-3/2}Z_+^{7/8}\Pi^{3/8}
+
K_2\nu^{-1/3}\Pi^{2/3}
<\frac14.
}
\]

The left side is continuous and strictly increasing for `Pi>0`.

Hence there is a unique positive threshold `Pi_c` defined by

\[
\boxed{
K_1\nu^{-3/2}Z_+^{7/8}\Pi_c^{3/8}
+
K_2\nu^{-1/3}\Pi_c^{2/3}
=\frac14.
}
\]

Then

\[
\boxed{
\Pi<\Pi_c
\Longrightarrow
N\le1
\Longrightarrow
\text{relative-periodic after at most two quotient returns}.
}
\]

## 4. Relation to the exact M19-185 test

The Young split is slightly more conservative than solving the exact degree-15 maximizer equation of M19-185, but it has two advantages:

1. it depends directly on the single background mean-palinstrophy parameter `Pi`;
2. it exposes the exact scaling powers

\[
\boxed{
\Pi^{3/8}
\quad\text{and}\quad
\Pi^{2/3}.
}
\]

Thus this is the cleanest current quantitative audit form.

## 5. What remains

No existing repository theorem gives the universal upper estimate

\[
\Pi<\Pi_c
\]

for every singular recurrent survivor.

Therefore the complementary branch

\[
\boxed{\Pi\ge\Pi_c}
\]

remains a genuine high-activity compact-core frontier.

---

\[
\boxed{\text{M19-186: APERIODICITY NOW HAS A DIRECT EXPLICIT MEAN-PALINSTROPHY THRESHOLD.}}
\]
