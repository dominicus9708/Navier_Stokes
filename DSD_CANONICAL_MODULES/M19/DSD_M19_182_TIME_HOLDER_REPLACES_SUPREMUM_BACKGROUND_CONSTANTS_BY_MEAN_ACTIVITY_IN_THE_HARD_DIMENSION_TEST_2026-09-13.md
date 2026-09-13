# M19-182 — Time Hölder replaces supremum background constants by mean activity in the hard-dimension test

**Date:** 2026-09-13  
**Status:** ACTIVE CALCULATION / COEFFICIENT SHARPENING

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Motivation

M19-181 used

\[
M_{5/2}=\sup_s\|S_U(s)\|_{5/2},
\qquad
M_a=\sup_s\|\nabla\Omega(s)\|_a.
\]

But the hard trace identity is already a long-time mean identity. Using temporal suprema throws away recurrent averaging.

## 2. Local strain coefficient

After M19-180/181 and the `lambda->infinity` occupation reduction, the instantaneous local term has the form

\[
|T_{str}(s)|
\le
C_{LT}^{3/5}
\|S_U(s)\|_{5/2}
P_h(s)^{3/5}.
\]

Use time Hölder with exponents `5/2` and `5/3`:

\[
\left\langle
\|S_U\|_{5/2}P_h^{3/5}
\right\rangle
\le
\left\langle\|S_U\|_{5/2}^{5/2}\right\rangle^{2/5}
\bar P_h^{3/5}.
\]

Define

\[
\boxed{
\mathfrak A
:=
C_{LT}^{3/5}
\left\langle\|S_U\|_{5/2}^{5/2}\right\rangle^{2/5}.
}
\]

Then

\[
\boxed{
\langle|T_{str}|\rangle
\le
\mathfrak A\,\bar P_h^{3/5}.
}
\]

## 3. Nonlocal coefficient

For `3/2<a<3`, let

\[
q(a)=\frac{3-a}{2a}.
\]

The instantaneous nonlocal trace has the form

\[
|T_{nl}(s)|
\le
C_a\|\nabla\Omega(s)\|_a
N^{p(a)}P_h(s)^{q(a)}
\]

after the occupation limit.

Use time Hölder with exponents

\[
\frac1{1-q(a)}
\quad\text{and}\quad
\frac1{q(a)}.
\]

Then

\[
\left\langle
\|\nabla\Omega\|_aP_h^{q(a)}
\right\rangle
\le
\left\langle
\|\nabla\Omega\|_a^{1/(1-q(a))}
\right\rangle^{1-q(a)}
\bar P_h^{q(a)}.
\]

Define

\[
\boxed{
\mathfrak B_a
:=
C_a
\left\langle
\|\nabla\Omega\|_a^{1/(1-q(a))}
\right\rangle^{1-q(a)}.
}
\]

Hence

\[
\boxed{
\langle|T_{nl}|\rangle
\le
\mathfrak B_a
N^{p(a)}\bar P_h^{q(a)}.
}
\]

## 4. Mean-activity dimension criterion

The M19-181 scalar test sharpens to

\[
\boxed{
\Psi_a^{mean}(x)
=
\mathfrak A\,2^{-2/5}x^{3/5}
+
\mathfrak B_a\,2^{d(a)-1}x^{q(a)}
-\nu x.
}
\]

A sufficient condition for

\[
\boxed{N\le1}
\]

is

\[
\boxed{
\sup_{x\ge0}\Psi_a^{mean}(x)<\frac14
}
\]

for at least one `a in (3/2,3)`.

## 5. Local coefficient descends to mean background palinstrophy

Calderon--Zygmund and interpolation give

\[
\|S_U\|_{5/2}
\lesssim
\|\Omega\|_{5/2}
\lesssim
\|\Omega\|_2^{7/10}
\|\Omega\|_6^{3/10}.
\]

Using Sobolev,

\[
\|\Omega\|_6\lesssim\|\nabla\Omega\|_2,
\]

so

\[
\|S_U\|_{5/2}^{5/2}
\lesssim
Z_U^{7/8}P_U^{3/8}.
\]

If `Z_U<=Z_+`, then concavity yields

\[
\boxed{
\mathfrak A
\lesssim
Z_+^{7/20}
\langle P_U\rangle^{3/20}.
}
\]

This is strictly less wasteful than the earlier `Z_+^{7/20}P_+^{3/20}` supremum bound.

## 6. No automatic smallness yet

The recurrent enstrophy identity provides finiteness and relations among the background mean quantities, but it does not currently force `mathfrak A` or `mathfrak B_a` below the dimension-one threshold.

Thus the improvement is quantitative but not yet a contradiction.

## 7. Next clean specialization

The choice

\[
\boxed{a=2}
\]

is especially useful because

\[
q(2)=\frac14,
\qquad
p(2)=\frac7{12},
\qquad
d(2)=\frac56,
\]

and `mathfrak B_2` can be reduced using only mean palinstrophy, without the higher-derivative `H` ledger.

---

\[
\boxed{\text{M19-182: THE DIMENSION TEST DEPENDS ON MEAN BACKGROUND ACTIVITY, NOT SUPREMUM ACTIVITY.}}
\]
