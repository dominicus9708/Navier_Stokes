# DSD M19-172 — Optimizing the vector HLS exponent pushes the nonlocal collective degree from five sixths toward two thirds and gives an explicit hard-dimension ceiling formula

**Date:** 2026-09-13  
**Status:** ACTIVE M19 CALCULATION / OPTIMIZED COLLECTIVE NONLOCAL EXPONENT / EXPLICIT DIMENSION-CEILING FORMULA / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-171 used

\[
\nabla\Omega\in L^2
\]

and obtained

\[
|T_{nl}|
\lesssim
\|\nabla\Omega\|_2
Z_q^{7/12}P_q^{1/4},
\]

with total collective degree `5/6`.

The critical tail actually gives better flexibility:

\[
\nabla\Omega(y)=O(r^{-3}),
\]

so on the smooth retained corridor

\[
\nabla\Omega\in L^a(\mathbb R^3)
\qquad
\text{for every }a>1.
\]

The present module optimizes the vector Hardy--Littlewood--Sobolev exponents.

## 2. Choose the background exponent

Fix

\[
\boxed{
\frac32<a<3.
}
\]

We again estimate

\[
|T_{nl}|
\le
C
\int
|\nabla\Omega|AB,
\]

where

\[
A=(\sum|W_j|^2)^{1/2},
\qquad
B=(\sum|\nabla W_j|^2)^{1/2}.
\]

Choose an exponent `p` for the collective vorticity field so that

\[
B\in L^p,
\]

and the order-minus-one Biot--Savart map gives

\[
A\in L^q,
\qquad
\frac1q
=
\frac1p-rac13.
\]

Holder requires

\[
\frac1a+
\frac1p+
\frac1q=1.
\]

Therefore

\[
\frac1a+
\frac2p-
\frac13=1,
\]

hence

\[
\boxed{
\frac1p
=
\frac23-
\frac1{2a}.
}
\]

For `a in (3/2,3)`, this gives

\[
2<p<3.
\]

## 3. Interpolation parameter

The collective vorticity magnitude

\[
E=(\sum|\eta_j|^2)^{1/2}
\]

obeys

\[
\|E\|_2=Z_q^{1/2},
\]

and by Lieb--Thirring

\[
\|E\|_{10/3}
\le
C P_q^{3/10}.
\]

Write

\[
\frac1p
=
\frac{1-\theta}{2}
+
\frac{3\theta}{10}
=
\frac12-
\frac\theta5.
\]

Using the value of `1/p`,

\[
\boxed{
\theta(a)
=
\frac{5}{2a}
-
\frac56.
}
\]

For

\[
\frac32<a<3,
\]

we have

\[
0<\theta<\frac56.
\]

Thus

\[
\boxed{
\|E\|_p
\le
C
Z_q^{(1-\theta)/2}
P_q^{3\theta/10}.
}
\]

## 4. Vector Biot--Savart/HLS estimate

Vector-valued Calderon--Zygmund gives

\[
\|B\|_p
\le
C_a\|E\|_p.
\]

Vector HLS gives

\[
\|A\|_q
\le
C_a\|E\|_p.
\]

Therefore

\[
\boxed{
|T_{nl}|
\le
C_a
\|\nabla\Omega\|_a
\|E\|_p^2.
}
\]

Substitute the interpolation estimate:

\[
|T_{nl}|
\le
C_a
\|\nabla\Omega\|_a
Z_q^{1-\theta}
P_q^{3\theta/5}.
\]

## 5. Explicit exponents

Using

\[
\theta
=
\frac{5}{2a}-\frac56,
\]

we obtain

\[
\boxed{
1-\theta
=
\frac{11}{6}
-
\frac{5}{2a},
}
\]

and

\[
\boxed{
\frac{3\theta}{5}
=
\frac{3}{2a}
-
\frac12.
}
\]

Hence

\[
\boxed{
|T_{nl}|
\le
C_a
\|\nabla\Omega\|_a
Z_q^{\,11/6-5/(2a)}
P_q^{\,3/(2a)-1/2}.
}
\]

The total collective degree is

\[
\begin{aligned}
d(a)
&=
\left(
\frac{11}{6}-\frac{5}{2a}
\right)
+
\left(
\frac{3}{2a}-\frac12
\right)\\
&=
\boxed{
\frac43-
\frac1a.
}
\end{aligned}
\]

## 6. Range of the degree

At

\[
a=2,
\]

we recover

\[
 d(2)=\frac56.
\]

As

\[
a\downarrow\frac32,
\]

we obtain

\[
\boxed{
 d(a)\downarrow\frac23.
}
\]

As

\[
a\uparrow3,
\]

we return to the linear degree

\[
 d(a)\uparrow1.
\]

Thus exponents near `a=3/2` are the favorable regime.

## 7. Endpoint firewall

At the endpoint

\[
a=\frac32,
\]

we have

\[
p=3,
\qquad
q=\infty.
\]

The strong HLS estimate

\[
I_1:L^3\to L^\infty
\]

is not available in the ordinary strong form.

Therefore one must keep

\[
\boxed{a>3/2}
\]

strictly.

The constants `C_a` deteriorate as

\[
a\downarrow3/2.
\]

Hence the optimal numerical bound is not obtained by blindly taking the endpoint; it requires balancing the better power against the worsening HLS constant.

## 8. Period-integrated form

Let

\[
M_a
:=
\sup_s\|\nabla\Omega(s)\|_a.
\]

For bounded period `S<=S_+`, generalized Holder gives

\[
\boxed{
|\mathfrak T_{nl}|
\le
C_aM_a
S_+^{1-d(a)}
\mathfrak Z_q^{\,11/6-5/(2a)}
\mathfrak P_q^{\,3/(2a)-1/2}.
}
\]

Since

\[
1-d(a)
=
\frac1a-rac13>0,
\]

the period factor is harmless on a bounded-period corridor.

## 9. Combine with the hard derivative ceiling

On the compact hard stratum,

\[
\mathfrak P_q
\le
\Lambda_P^+
\mathfrak Z_q.
\]

Hence

\[
\boxed{
|\mathfrak T_{nl}|
\le
C_a'
\mathfrak Z_q^{d(a)}.
}
\]

The local strain term remains

\[
|\mathfrak T_{strain}|
\le
C_{str}
\mathfrak Z_q^{3/5}
\]

after the same derivative ceiling.

Therefore the exact trace identity gives

\[
\boxed{
\frac14\mathfrak Z_q
\le
C_{str}\mathfrak Z_q^{3/5}
+
C_a'\mathfrak Z_q^{d(a)}.
}
\]

with

\[
\frac23<d(a)<1.
\]

## 10. Explicit ceiling

Let

\[
x:=\mathfrak Z_q.
\]

If

\[
x>
(8C_{str})^{5/2},
\]

then

\[
C_{str}x^{3/5}<\frac{x}{8}.
\]

If

\[
x>
(8C_a')^{1/(1-d(a))},
\]

then

\[
C_a'x^{d(a)}<\frac{x}{8}.
\]

Both inequalities would give

\[
\frac{x}{4}
<
\frac{x}{4},
\]

a contradiction after harmless strictness adjustment.

Thus one may take schematically

\[
\boxed{
Z_*(a)
\lesssim
\max
\left\{
(8C_{str})^{5/2},
(8C_a')^{\frac1{1-d(a)}}
\right\}.
}
\]

Since

\[
\frac1{1-d(a)}
=
\boxed{
\frac{3a}{3-a}
},
\]

we obtain

\[
\boxed{
Z_*(a)
\lesssim
\max
\left\{
(8C_{str})^{5/2},
(8C_a')^{\frac{3a}{3-a}}
\right\}.
}
\]

## 11. Dimension ceiling

M19-169 gives

\[
N g_-
\le
\mathfrak Z_q.
\]

Therefore

\[
\boxed{
N
\le
N_*(a)
:=
\frac{Z_*(a)}{g_-}.
}
\]

The best certified ceiling is obtained by optimizing over

\[
\boxed{
\frac32<a<3.
}
\]

with the actual corridor constants `C_a,M_a,Lambda_P^+,g_-`.

## 12. Can the exponent optimization alone prove N<=1?

No.

The power improves toward `2/3`, but the relevant constants are not currently sharp enough or explicitly bounded tightly enough to certify

\[
Z_*(a)<2g_-.
\]

Therefore

\[
\boxed{
\text{better exponent}
\neq
\text{automatic dimension-one theorem}.
}
\]

The optimization is nevertheless useful because it identifies the correct near-endpoint functional regime for any future quantitative estimate or computer-assisted bound.

## 13. Audit verdict

### Proved

1. A one-parameter family of nonlocal collective estimates for `3/2<a<3`.
2. Exact collective degree
   \[
   d(a)=4/3-1/a.
   \]
3. The degree approaches `2/3` from above as `a->3/2+`.
4. An explicit formula for the resulting total-hard enstrophy and dimension ceiling.

### Not proved

1. A numerical ceiling `N<=1` on the full hard corridor.
2. Kernel rigidity.
3. Global regularity.

## 14. Next target

There are now two sensible branches:

1. **quantitative branch:** sharpen the compact-corridor constants and test whether `N_*(a)<=1` on any certified subcorridor;
2. **structural branch:** return to the one-dimensional residual case and derive a direct finite-iterate kernel contradiction, so that even a weaker ceiling `N<=1` would suffice.

M19-173 should pursue the second branch first: assume the quotient hard space is one-dimensional and calculate the exact real `mu=+1` / finite-iterate `mu=-1` kernel equations, their adjoint solvability conditions, and whether the q-speed/rotation observables force a contradiction.
