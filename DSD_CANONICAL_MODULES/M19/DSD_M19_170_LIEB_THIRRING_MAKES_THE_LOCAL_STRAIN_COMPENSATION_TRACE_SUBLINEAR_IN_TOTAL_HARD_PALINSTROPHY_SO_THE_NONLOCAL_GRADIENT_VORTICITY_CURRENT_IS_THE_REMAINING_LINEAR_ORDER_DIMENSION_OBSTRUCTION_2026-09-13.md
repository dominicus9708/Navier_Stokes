# DSD M19-170 — Lieb--Thirring makes the local strain compensation trace sublinear in total hard palinstrophy, so the nonlocal gradient-vorticity current is the remaining linear-order dimension obstruction

**Date:** 2026-09-13  
**Status:** ACTIVE M19 CALCULATION / SUBLINEAR LOCAL-STRAIN TRACE / NONLOCAL CURRENT ISOLATED / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-169 gave the exact total quotient-hard compensation identity

\[
\mathfrak T_q
=
\nu\mathfrak P_q
+
\frac14\mathfrak Z_q,
\]

where

\[
\mathfrak P_q
:=
\int_0^S\sum_j\|\nabla\eta_j\|_2^2ds,
\]

and

\[
\mathfrak Z_q
:=
\int_0^S\sum_j\|\eta_j\|_2^2ds.
\]

The same trace decomposes into local strain and nonlocal gradient-vorticity current.

The present module proves that the **local strain trace is sublinear in total hard palinstrophy** by a Lieb--Thirring density estimate.

Thus local strain alone cannot support arbitrarily many neutral hard channels at a linear rate.

## 2. Instantaneous hard-mode density

At a fixed time, choose an `L2`-orthonormalized vorticity frame for the hard subspace, up to the uniformly bounded Gram-condition number supplied by the compact hard bundle.

Write

\[
\rho_q(y)
:=
\sum_{j=1}^N|\eta_j(y)|^2.
\]

The collective traceless tensor satisfies

\[
|Q_q(y)|
\le
C\rho_q(y).
\]

## 3. Lieb--Thirring density estimate

For an orthonormal family in three dimensions, the vector-valued Lieb--Thirring/Sobolev density estimate has the form

\[
\boxed{
\int_{\mathbb R^3}
\rho_q^{5/3}dy
\le
C_{LT}
\sum_{j=1}^N
\|\nabla\eta_j\|_2^2.
}
\]

Uniform equivalence between the chosen instantaneous orthonormalization and the compact hard-bundle frame only changes the constant.

Define

\[
P_q(s)
:=
\sum_j\|\nabla\eta_j(s)\|_2^2.
\]

Then

\[
\boxed{
\|\rho_q(s)\|_{L^{5/3}}
\le
C
P_q(s)^{3/5}.
}
\]

## 4. Critical strain belongs to L^{5/2}

The retained critical tail has

\[
|S_U(y,s)|\lesssim r^{-2}.
\]

Hence

\[
|S_U|^{5/2}\lesssim r^{-5},
\]

which is integrable at spatial infinity in three dimensions:

\[
\int_R^\infty r^2r^{-5}dr<\infty.
\]

The smooth compact core is also integrable, so

\[
\boxed{
S_U(s)\in L^{5/2}(\mathbb R^3)
}
\]

uniformly on the retained compact hard corridor.

Let

\[
M_{5/2}
:=
\sup_s\|S_U(s)\|_{5/2}<\infty.
\]

## 5. Sublinear local strain trace

By M19-162,

\[
T_{strain}(s)
:=
\sum_j
\int
\eta_j\cdot S_U\eta_j
=
\int S_U:Q_q.
\]

Use Hölder with exponents `5/2` and `5/3`:

\[
\begin{aligned}
|T_{strain}(s)|
&\le
\|S_U(s)\|_{5/2}
\|Q_q(s)\|_{5/3}\\
&\le
C
\|S_U(s)\|_{5/2}
\|\rho_q(s)\|_{5/3}\\
&\le
C
M_{5/2}
P_q(s)^{3/5}.
\end{aligned}
\]

Therefore

\[
\boxed{
|T_{strain}(s)|
\le
C_S
P_q(s)^{3/5}.
}
\]

This is the key sublinear estimate.

## 6. Period-integrated form

Integrate over one bounded period `S` and use concavity/Hölder:

\[
\int_0^S
P_q(s)^{3/5}ds
\le
S^{2/5}
\left(
\int_0^S P_q(s)ds
\right)^{3/5}.
\]

Hence

\[
\boxed{
|\mathfrak T_{strain}|
\le
C_S
S^{2/5}
\mathfrak P_q^{3/5}.
}
\]

On a bounded-period hard corridor `S<=S_+`, absorb the period into the constant:

\[
\boxed{
|\mathfrak T_{strain}|
\le
C_{str}\mathfrak P_q^{3/5}.
}
\]

## 7. Why this matters for dimension

M19-169 gives the exact lower identity

\[
\mathfrak T_q
=
\nu\mathfrak P_q
+
\frac14\mathfrak Z_q.
\]

The local strain contribution grows at most like

\[
\mathfrak P_q^{3/5},
\]

while the dissipative side contains

\[
\nu\mathfrak P_q.
\]

Therefore for large total hard palinstrophy, local strain cannot balance the unit-mode trace.

In particular, **local strain cannot by itself support arbitrarily many normalized hard dimensions**.

## 8. Nonlocal trace isolated

Write

\[
\mathfrak T_q
=
\mathfrak T_{strain}
+
\mathfrak T_{nl},
\]

where

\[
\mathfrak T_{nl}
:=
\int_0^S
\sum_j
\mathcal C_{grad\Omega}[W_j]ds.
\]

Then

\[
\boxed{
\nu\mathfrak P_q
+
\frac14\mathfrak Z_q
\le
C_{str}\mathfrak P_q^{3/5}
+
|\mathfrak T_{nl}|.
}
\]

Thus the only way to sustain a large-dimensional hard unit block is for the nonlocal gradient-vorticity current to contribute at linear order in the total hard mass/palinstrophy.

This isolates the remaining obstruction.

## 9. Conditional finite-dimension estimate

Suppose, on a subcorridor, the nonlocal trace satisfies

\[
\boxed{
|\mathfrak T_{nl}|
\le
b\,\mathfrak Z_q
+
C_{nl}\mathfrak P_q^\theta,
\qquad
\theta<1,
}
\]

with

\[
b<\frac14.
\]

Then

\[
\nu\mathfrak P_q
+
\left(
\frac14-b
\right)
\mathfrak Z_q
\le
C\left(
\mathfrak P_q^{3/5}
+
\mathfrak P_q^\theta
\right).
\]

Hence `mathfrak P_q` is uniformly bounded.

Using M19-158/169,

\[
\mathfrak P_q
\ge
\lambda_P\mathfrak Z_q
\ge
\lambda_Pg_-N,
\]

we obtain a uniform dimension bound

\[
\boxed{
N\le N_*<\infty.
}
\]

If the resulting numerical bound satisfies `N_*<=1`, all irrational elliptic blocks are eliminated by M19-168.

## 10. Why the condition is not yet certified

The presently available estimate on the nonlocal trace is controlled by `grad Omega` through Biot--Savart, but current corridor bounds do not yet give a coefficient strictly below `1/4` in front of the total hard `Z` mass.

Therefore the conditional dimension estimate is not yet an unconditional closure.

## 11. Main gain

The compensation problem has now been separated into two qualitatively different pieces:

\[
\boxed{
\begin{aligned}
\text{local strain trace}
&=O(\mathfrak P_q^{3/5})
\quad\text{sublinear},\\
\text{nonlocal }\nabla\Omega\text{ trace}
&=\text{only remaining candidate for linear-order support}.
\end{aligned}
}
\]

Thus the next calculation no longer needs to control the full compensation operator at once.

## 12. Audit verdict

### Proved

1. Critical strain lies in `L^{5/2}` on the retained corridor.
2. Lieb--Thirring yields the instantaneous collective density bound.
3. The total local strain compensation trace is sublinear in total hard palinstrophy with exponent `3/5`.
4. Any large-dimensional unit hard block must receive linear-order support from the nonlocal gradient-vorticity current.

### Not proved

1. A sublinear or sub-quarter bound for the nonlocal current trace.
2. `dim E_q^{hard}<=1`.
3. Kernel rigidity.

## 13. Next target

M19-171 should estimate

\[
\mathfrak T_{nl}
=
\int
\sum_j
\left[
\eta_j\cdot(\Omega\cdot\nabla)W_j
-
\eta_j\cdot(W_j\cdot\nabla)\Omega
\right]
\]

collectively rather than mode-by-mode.

The objective is to use

- the constant-vorticity cancellation from M19-091;
- vector-valued Biot--Savart/Sobolev estimates;
- collective Lieb--Thirring density bounds;

to obtain a sublinear estimate in `mathfrak P_q` or, failing that, an explicit coefficient multiplying `mathfrak Z_q` that can be compared with the quarter-gap.
