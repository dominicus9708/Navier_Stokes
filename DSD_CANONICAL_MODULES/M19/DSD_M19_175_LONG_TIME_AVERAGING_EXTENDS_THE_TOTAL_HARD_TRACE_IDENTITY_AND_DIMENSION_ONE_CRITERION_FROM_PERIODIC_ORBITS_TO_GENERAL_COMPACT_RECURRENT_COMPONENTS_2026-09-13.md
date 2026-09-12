# DSD M19-175 — Long-time averaging extends the total hard trace identity and dimension-one criterion from periodic orbits to general compact recurrent components

**Date:** 2026-09-13  
**Status:** AUTHORITATIVE SCOPE CORRECTION + ACTIVE M19 CALCULATION / APERIODIC TRACE EXTENSION / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose and correction

M19-169--174 derived the total hard compensation trace using one relative period and then used the resulting dimension criterion as a target for eliminating aperiodic recurrence.

That presentation creates a scope problem if read literally:

\[
\text{periodic trace identity}
\not\Rightarrow
\text{aperiodic dimension bound}
\]

without an extension.

The present module supplies the required extension. The exact trace identity follows from **long-time averaging** on any compact recurrent hard component; periodicity is not needed.

This module is authoritative for the scope of the dimension-one criterion.

## 2. Transported hard frame on a recurrent orbit

Let `U(s)` lie on a compact recurrent critical hard component after exact rotation/time gauge handling.

Assume the real symmetry-quotient hard bundle has constant rank

\[
N
\]

on the fixed-rank stratum.

Choose at time `s=0` a scattering-pullback orthonormal basis

\[
v_1(0),\ldots,v_N(0).
\]

Transport it by the linearized cocycle:

\[
\boxed{
v_j(s):=\Phi_s(U(0))v_j(0).
}
\]

Because the scattering pullback norm is an exact cocycle isometry,

\[
\{v_j(s)\}_{j=1}^N
\]

remains scattering-orthonormal for all times for which the complete hard cocycle is defined.

Let

\[
W_j(s)
\]

be the corresponding velocity perturbations and

\[
\eta_j(s)=\nabla\times W_j(s).
\]

## 3. Collective hard quantities

Define

\[
\boxed{
Z_N(s)
:=
\sum_{j=1}^N\|\eta_j(s)\|_2^2,
}
\]

\[
\boxed{
P_N(s)
:=
\sum_{j=1}^N\|\nabla\eta_j(s)\|_2^2,
}
\]

and

\[
\boxed{
T_N(s)
:=
\sum_{j=1}^N\mathcal C_{U(s)}[W_j(s)].
}
\]

Summing the exact linearized-vorticity energy identities gives

\[
\boxed{
\frac12\frac d{ds}Z_N(s)
+
\nu P_N(s)
+
\frac14Z_N(s)
=
T_N(s).
}
\]

No periodicity has been used.

## 4. Compactness kills the long-time boundary term

On the retained compact hard corridor, scattering/vorticity norm equivalence gives uniform bounds

\[
0<Z_-N
\le
Z_N(s)
\le
Z_+N<\infty
\]

with corridor constants `Z_-,Z_+` independent of `s` on a fixed-rank stratum.

In particular,

\[
|Z_N(T)-Z_N(0)|
\le
C N.
\]

Divide the integrated energy identity by `T`:

\[
\frac{Z_N(T)-Z_N(0)}{2T}
+
\nu\frac1T\int_0^T P_N
+
\frac14\frac1T\int_0^T Z_N
=
\frac1T\int_0^T T_N.
\]

As

\[
T\to\infty,
\]

the boundary term satisfies

\[
\boxed{
\frac{Z_N(T)-Z_N(0)}{2T}
\to0.
}
\]

## 5. General recurrent mean trace identity

For any sequence along which the Cesaro averages converge, define

\[
\langle Z_N\rangle
:=
\lim_{T\to\infty}
\frac1T\int_0^T Z_N(s)ds,
\]

and similarly for `P_N,T_N`.

Then

\[
\boxed{
\langle T_N\rangle
=
\nu\langle P_N\rangle
+
\frac14\langle Z_N\rangle.
}
\]

On an invariant ergodic component, these are the usual Birkhoff means for almost every orbit/frame-compatible observable.

Thus the total compensation trace identity is valid for

\[
\boxed{
\text{periodic}
\quad\text{and}
\quad
\text{aperiodic recurrent}
}
\]

hard dynamics.

## 6. Mean Lieb--Thirring local-strain bound

M19-170 gives instantaneously

\[
|T_{strain}(s)|
\le
C_{str,0}P_N(s)^{3/5}.
\]

Average in time. Since `x->x^{3/5}` is concave,

\[
\boxed{
|\langle T_{strain}\rangle|
\le
C_{str,0}
\langle P_N\rangle^{3/5}.
}
\]

No period factor appears.

## 7. Mean optimized nonlocal bound

M19-172 gives, for every

\[
3/2<a<3,
\]

\[
|T_{nl}(s)|
\le
C_aM_a
Z_N(s)^{A(a)}
P_N(s)^{B(a)},
\]

where

\[
A(a)
=
\frac{11}{6}-\frac{5}{2a},
\]

\[
B(a)
=
\frac{3}{2a}-\frac12,
\]

and

\[
A(a)+B(a)
=d(a)
=
\frac43-rac1a<1.
\]

Generalized Holder/Jensen on normalized time averages gives

\[
\boxed{
|\langle T_{nl}\rangle|
\le
C_aM_a
\langle Z_N\rangle^{A(a)}
\langle P_N\rangle^{B(a)}.
}
\]

Again there is no bounded-period constant `S_+`.

## 8. Mean derivative ratio

On a compact smooth fixed-rank hard stratum, parabolic regularity and norm equivalence give a uniform mean derivative ceiling

\[
\boxed{
\langle P_N\rangle
\le
\Lambda_P^+
\langle Z_N\rangle.
}
\]

The lower hard-fiber Poincare gap also gives

\[
\boxed{
\langle P_N\rangle
\ge
\lambda_P
\langle Z_N\rangle.
}
\]

## 9. Aperiodic collective inequality

Combine the mean trace identity with the two collective estimates:

\[
\boxed{
\frac14\langle Z_N\rangle
\le
C_{str}\langle Z_N\rangle^{3/5}
+
C_a'\langle Z_N\rangle^{d(a)}.
}
\]

This is exactly the M19-172/M19-174 inequality with

\[
\mathfrak Z_q
\]

replaced by the invariant long-time mean

\[
\langle Z_N\rangle.
\]

It is therefore valid **before** relative periodicity has been proved.

## 10. Dimension lower bound for the recurrent hard bundle

Uniform vorticity observability per scattering-normalized vector gives

\[
\boxed{
\langle Z_N\rangle
\ge
Ng_-
}
\]

for some compact-corridor constant

\[
g_->0.
\]

Define

\[
X
:=
\frac{\langle Z_N\rangle}{g_-}.
\]

Then

\[
X\ge N.
\]

The exact same monotonicity argument as M19-174 now gives the aperiodic-valid sufficient criterion

\[
\boxed{
\widehat C_{str}2^{-2/5}
+
\widehat C_a2^{d(a)-1}
<
\frac14
\Longrightarrow
N\le1.
}
\]

## 11. Consequence for the logical order

The previous apparent circularity is removed.

The correct order is

\[
\boxed{
\text{compact recurrent hard component}
\xrightarrow{\text{long-time trace estimate}}
N\le1
\xrightarrow{\text{M19-173}}
\text{relative periodicity}.
}
\]

One does **not** assume periodicity in order to obtain the dimension-one bound.

## 12. Improvement over the periodic formula

The recurrent mean formula removes explicit factors such as

\[
S_+^{2/5},
\qquad
S_+^{1-d(a)}.
\]

Therefore the dimensionless constants relevant to aperiodic closure are actually cleaner than the preliminary bounded-period constants in M19-174.

The principal quantities are now

\[
\boxed{
\left(
g_-,
\Lambda_P^+,
M_{5/2},
M_a,
C_{LT},
C_{HLS/CZ}(a)
\right).
}
\]

## 13. Audit verdict

### Authoritative correction

M19-169--174 should not be read as requiring relative periodicity before the hard-dimension trace estimate can be used.

The long-time average identity proves the same dimension criterion directly on a general compact recurrent component.

### Proved

1. General recurrent total-hard trace identity.
2. Mean local and nonlocal collective sublinear estimates.
3. Aperiodic-valid dimension-one sufficient criterion.
4. Removal of the artificial bounded-period factors from the aperiodic criterion.

### Not proved

The strict numerical two-mode inequality is still not certified.

## 14. Next target

M19-176 should now audit the constants in the **mean** criterion, not the preliminary periodic one.

In particular:

- `g_-` and `Lambda_P^+` currently come from compact hard-bundle norm equivalence;
- `M_{5/2}` and `M_a` come from smooth critical-tail/core bounds;
- the universal Lieb--Thirring/HLS/CZ constants can in principle be made explicit.

The immediate question is whether `g_-` can be normalized away or replaced by a canonical hard-fiber metric so that the two-mode test depends only on PDE-controlled quantities rather than an arbitrary scattering-norm equivalence constant.
