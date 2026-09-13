# M19-183 — a=2 gives an explicit algebraic two-mode threshold using only mean palinstrophy

**Date:** 2026-09-13  
**Status:** ACTIVE CALCULATION / EXPLICIT CONDITIONAL DIMENSION-ONE CRITERION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Choose the clean interior exponent a=2

For

\[
a=2,
\]

M19-181/182 give

\[
q=\frac14,
\qquad
p=\frac7{12},
\qquad
d=\frac56.
\]

Thus the two-mode test becomes

\[
\Psi_2(x)
=A'x^{3/5}+B'x^{1/4}-\nu x,
\]

where

\[
A':=2^{-2/5}\mathfrak A,
\qquad
B':=2^{-1/6}\mathfrak B_2.
\]

A sufficient condition for `N<=1` is

\[
\boxed{
\sup_{x\ge0}\Psi_2(x)<\frac14.
}
\]

## 2. The nonlocal coefficient uses only mean palinstrophy

Since

\[
\|\nabla\Omega\|_2=P_U^{1/2},
\]

and

\[
\frac1{1-q}=\frac43,
\]

we have

\[
\mathfrak B_2
=C_2
\left\langle
\|\nabla\Omega\|_2^{4/3}
\right\rangle^{3/4}
=C_2
\left\langle
P_U^{2/3}
\right\rangle^{3/4}.
\]

Concavity yields

\[
\boxed{
\mathfrak B_2
\le
C_2\langle P_U\rangle^{1/2}.
}
\]

Together with M19-182,

\[
\boxed{
\mathfrak A
\lesssim
Z_+^{7/20}\langle P_U\rangle^{3/20}.
}
\]

Therefore the clean `a=2` criterion requires no higher-derivative background ledger `H`.

## 3. Exact maximizer

For `x>0`,

\[
\Psi_2'(x)
=\frac35A'x^{-2/5}
+\frac14B'x^{-3/4}
-\nu.
\]

The derivative decreases strictly from `+infinity` to `-nu`, so there is a unique maximizer `x_*>0`.

Set

\[
y:=x_*^{1/20}>0.
\]

Then

\[
x_*^{-2/5}=y^{-8},
\qquad
x_*^{-3/4}=y^{-15}.
\]

Multiplying the critical-point equation by `y^15` gives the explicit algebraic equation

\[
\boxed{
\nu y^{15}
-\frac35A'y^7
-\frac14B'
=0.
}
\]

Its positive root is unique.

## 4. Exact maximum value

At the critical point,

\[
\nu x_*
=\frac35A'x_*^{3/5}
+\frac14B'x_*^{1/4}.
\]

Therefore

\[
\Psi_2(x_*)
=\frac25A'x_*^{3/5}
+\frac34B'x_*^{1/4}.
\]

In terms of `y`,

\[
\boxed{
\Psi_2^{max}
=\frac25A'y^{12}
+\frac34B'y^5.
}
\]

Hence the exact current two-mode exclusion test is

\[
\boxed{
\frac25A'y^{12}
+\frac34B'y^5
<\frac14,
}
\]

where `y>0` is the unique root of

\[
\boxed{
\nu y^{15}
-\frac35A'y^7
-\frac14B'=0.
}
\]

## 5. Conditional theorem extracted

There exists a positive quantitative region in the background mean-activity plane such that

\[
(A',B')\text{ lies in that region}
\Longrightarrow
N\le1.
\]

In particular, because both coefficients tend to zero with the corresponding background mean activity, sufficiently low recurrent mean palinstrophy forces

\[
\boxed{N\le1}
\]

inside the certified hard corridor.

By M19-173, this implies that the recurrent hard dynamics reduces to relative-periodic behavior after at most a two-fold quotient return.

## 6. Firewall

The repository does **not** currently contain a universal upper bound forcing every singular recurrent survivor into this low-mean-palinstrophy region.

Therefore

\[
\boxed{
\text{explicit conditional threshold}
\neq
\text{unconditional dimension-one theorem}.
}
\]

## 7. Next target

The remaining question is whether the Navier--Stokes recurrent identities themselves force `(A',B')` into the admissible algebraic region, or whether a high-mean-palinstrophy hard survivor remains possible.

---

\[
\boxed{\text{M19-183: THE DIMENSION-ONE TARGET IS NOW AN EXPLICIT ALGEBRAIC MEAN-PALINSTROPHY TEST.}}
\]
