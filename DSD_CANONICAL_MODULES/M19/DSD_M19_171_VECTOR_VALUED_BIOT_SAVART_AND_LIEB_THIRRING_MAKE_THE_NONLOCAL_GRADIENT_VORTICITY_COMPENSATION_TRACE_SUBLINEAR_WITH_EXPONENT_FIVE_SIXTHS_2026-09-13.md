# DSD M19-171 — Vector-valued Biot--Savart and Lieb--Thirring make the nonlocal gradient-vorticity compensation trace sublinear with exponent five sixths

**Date:** 2026-09-13  
**Status:** ACTIVE M19 CALCULATION / NONLOCAL TRACE SUBLINEARITY / UNIFORM QUOTIENT-HARD DIMENSION BOUND / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-170 proved that the local strain trace is sublinear in total hard palinstrophy:

\[
|T_{strain}(s)|
\lesssim
P_q(s)^{3/5}.
\]

The only remaining candidate for linear-order support of a large unit hard block was the nonlocal gradient-vorticity trace

\[
T_{nl}(s)
=
\sum_j
\mathcal C_{grad\Omega}[W_j].
\]

The present module estimates this term collectively.

The key result is

\[
\boxed{
|T_{nl}(s)|
\lesssim
\|\nabla\Omega(s)\|_2
Z_q(s)^{7/12}
P_q(s)^{1/4}.
}
\]

The total exponent is

\[
\frac7{12}+\frac14
=
\frac56<1.
\]

Thus the nonlocal trace is also sublinear in collective hard size.

## 2. Collective fields

Let

\[
E(y)
:=
\left(
\sum_{j=1}^N
|\eta_j(y)|^2
\right)^{1/2},
\]

\[
A(y)
:=
\left(
\sum_{j=1}^N
|W_j(y)|^2
\right)^{1/2},
\]

and

\[
B(y)
:=
\left(
\sum_{j=1}^N
|\nabla W_j(y)|^2
\right)^{1/2}.
\]

Define

\[
Z_q
:=
\sum_j\|\eta_j\|_2^2
=
\|E\|_2^2,
\]

and

\[
P_q
:=
\sum_j\|\nabla\eta_j\|_2^2.
\]

## 3. Exact structural reduction of the nonlocal term

M19-091 and M19-160 show that the constant-vorticity part cancels. Both nonlocal terms can be bounded by `grad Omega` times one velocity factor and one velocity-gradient/vorticity factor.

Using `|eta_j|<=C|grad W_j|` pointwise at the level of components,

\[
\boxed{
|T_{nl}(s)|
\le
C
\int
|\nabla\Omega|
\sum_j
|W_j|\,|\nabla W_j|\,dy.
}
\]

By Cauchy--Schwarz in the mode index,

\[
\sum_j|W_j||\nabla W_j|
\le
A(y)B(y).
\]

Therefore

\[
\boxed{
|T_{nl}(s)|
\le
C
\int
|\nabla\Omega|AB.
}
\]

## 4. Collective Lieb--Thirring interpolation for E

M19-170 gives

\[
\|E\|_{10/3}
\le
C
P_q^{3/10}.
\]

Interpolate between

\[
\|E\|_2
=Z_q^{1/2}
\]

and the `L^{10/3}` bound.

Choose

\[
p=\frac{12}{5}.
\]

Since

\[
\frac1p
=\frac5{12}
=
\left(1-\frac5{12}\right)\frac12
+
\frac5{12}\frac3{10},
\]

the interpolation parameter is

\[
\theta=\frac5{12}.
\]

Hence

\[
\boxed{
\|E\|_{12/5}
\le
C
Z_q^{7/24}
P_q^{1/8}.
}
\]

## 5. Vector-valued Biot--Savart estimates

Because

\[
W_j
=
\operatorname{curl}(-\Delta)^{-1}\eta_j,
\]

`W_j` is an order `-1` Riesz-potential transform of `eta_j`, while `grad W_j` is an order-zero Calderon--Zygmund transform.

Vector-valued Hardy--Littlewood--Sobolev and Calderon--Zygmund estimates therefore give

\[
\boxed{
\|A\|_{12}
\le
C
\|E\|_{12/5},
}
\]

because

\[
\frac1{12}
=
\frac5{12}-\frac13,
\]

and

\[
\boxed{
\|B\|_{12/5}
\le
C
\|E\|_{12/5}.
}
\]

Thus

\[
\boxed{
\|A\|_{12}
+
\|B\|_{12/5}
\le
C
Z_q^{7/24}
P_q^{1/8}.
}
\]

## 6. Nonlocal trace bound

Use Holder with

\[
2,
\quad
12,
\quad
\frac{12}{5},
\]

since

\[
\frac12+
\frac1{12}+
\frac5{12}=1.
\]

Then

\[
\begin{aligned}
|T_{nl}(s)|
&\le
C
\|\nabla\Omega\|_2
\|A\|_{12}
\|B\|_{12/5}\\
&\le
C
\|\nabla\Omega\|_2
\left(
Z_q^{7/24}P_q^{1/8}
\right)^2.
\end{aligned}
\]

Therefore

\[
\boxed{
|T_{nl}(s)|
\le
C
\|\nabla\Omega(s)\|_2
Z_q(s)^{7/12}
P_q(s)^{1/4}.
}
\]

The collective degree is

\[
\boxed{
\frac7{12}+\frac14
=
\frac56<1.
}
\]

## 7. Period-integrated bound

On the compact recurrent/relative-periodic corridor, background palinstrophy is uniformly bounded:

\[
M_{bg}
:=
\sup_s\|\nabla\Omega(s)\|_2
<\infty.
\]

Integrate over a bounded period. Generalized Holder gives

\[
\int_0^S
Z_q^{7/12}P_q^{1/4}ds
\le
S^{1/6}
\mathfrak Z_q^{7/12}
\mathfrak P_q^{1/4}.
\]

Hence

\[
\boxed{
|\mathfrak T_{nl}|
\le
C_{nl}
S^{1/6}
\mathfrak Z_q^{7/12}
\mathfrak P_q^{1/4}.
}
\]

On a bounded-period corridor absorb `S^{1/6}` into the constant:

\[
\boxed{
|\mathfrak T_{nl}|
\le
C_{nl}
\mathfrak Z_q^{7/12}
\mathfrak P_q^{1/4}.
}
\]

## 8. Combine with the local strain trace

M19-170 gives

\[
|\mathfrak T_{strain}|
\le
C_{str}
\mathfrak P_q^{3/5}.
\]

The exact total-trace identity M19-169 is

\[
\nu\mathfrak P_q
+
\frac14\mathfrak Z_q
=
\mathfrak T_{strain}
+
\mathfrak T_{nl}.
\]

Therefore

\[
\boxed{
\nu\mathfrak P_q
+
\frac14\mathfrak Z_q
\le
C_{str}\mathfrak P_q^{3/5}
+
C_{nl}
\mathfrak Z_q^{7/12}
\mathfrak P_q^{1/4}.
}
\]

Both right-hand terms are sublinear under common scaling of the collective hard family.

## 9. Uniform total-hard-size bound

On a compact hard stratum, parabolic regularity and finite-dimensional bundle equivalence provide a uniform upper derivative ratio

\[
\mathfrak P_q
\le
\Lambda_P^+
\mathfrak Z_q.
\]

Insert it into the preceding inequality:

\[
\frac14\mathfrak Z_q
\le
C_1\mathfrak Z_q^{3/5}
+
C_2\mathfrak Z_q^{5/6}.
\]

Since both exponents on the right are strictly below one, this forces

\[
\boxed{
\mathfrak Z_q
\le
Z_*<\infty.
}
\]

Consequently

\[
\boxed{
\mathfrak P_q
\le
P_*<\infty.
}
\]

The constants depend on the compact corridor bounds but **not on the number of hard modes**.

## 10. Uniform quotient-hard dimension bound

M19-169 supplies

\[
\mathfrak Z_q
\ge
Ng_-.
\]

Therefore

\[
\boxed{
N
\le
\frac{Z_*}{g_-}
=:N_*<\infty.
}
\]

This is a quantitative, corridor-uniform bound on the real symmetry-quotient hard dimension obtained directly from PDE collective estimates.

It is stronger than the earlier qualitative finite-dimensionality from essential-spectrum separation.

## 11. Does this already give N<=1?

Not yet.

The constants in

\[
Z_*
\]

have not been shown small enough to imply

\[
Z_*<2g_-.
\]

Therefore

\[
\boxed{
N\le N_*
}
\]

is certified, but

\[
N\le1
\]

is not yet certified.

## 12. Main gain

The prior obstruction was that the nonlocal current might supply compensation at linear order in hard dimension.

The present calculation removes that possibility:

\[
\boxed{
\begin{aligned}
\mathfrak T_{strain}
&=O(\mathfrak P_q^{3/5}),\\
\mathfrak T_{nl}
&=O(\mathfrak Z_q^{7/12}\mathfrak P_q^{1/4}).
\end{aligned}
}
\]

Both are collective-sublinear.

Hence the entire quotient hard unit block has a **uniform PDE dimension ceiling**.

## 13. Audit verdict

### Proved on the retained bounded-period compact corridor

1. Collective nonlocal compensation trace estimate with degree `5/6`.
2. Both local and nonlocal compensation traces are sublinear in collective hard size.
3. Uniform upper bounds on total quotient-hard enstrophy/palinstrophy trace.
4. A quantitative uniform dimension ceiling `N<=N_*` independent of the unknown hard-mode multiplicity.

### Not proved

1. The stronger numerical ceiling `N<=1`.
2. Uniform kernel rigidity.
3. Long-period `S->infinity` closure.
4. Global regularity.

## 14. Next target

M19-172 should optimize the exponent choice instead of fixing `grad Omega in L2`.

Because the critical tail gives

\[
\nabla\Omega\in L^r
\qquad
\text{for every }r>1
\]

on the smooth corridor, one may use

\[
r\in(3/2,3)
\]

together with vector HLS/Lieb--Thirring to obtain a family of collective exponents approaching total degree `2/3` as `r->3/2+`.

The goal is to sharpen `Z_*` and test whether the optimized dimension ceiling can reach the decisive threshold `N<=1` on any certified subcorridor.
