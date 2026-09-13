# M19-236 — The natural Rellich multiplier exposes boundary shear but leaves an R-squared dilation-action payer

**Date:** 2026-09-14  
**Status:** ACTIVE AUDIT / RELLICH IDENTITY + BOUNDARY-SHEAR SHORTCUT NO-GO

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Target

M19-235 proves that any escaping cavity unit mode must satisfy

\[
\boxed{
\liminf_{j\to\infty}
\frac1{R_j}
\int_0^{S_j}\int_{S_{R_j}}|\partial_nw_j|^2dSds
\ge\frac1{8\nu^2}.
}
\]

A natural way to close the branch would be a Rellich/Pohozaev identity giving

\[
\int_0^{S_j}\int_{S_{R_j}}|\partial_nw_j|^2=o(R_j).
\]

We test the canonical multiplier

\[
D w:=y\cdot\nabla w.
\]

## 2. Primal equation in multiplier form

Write the cavity linearized equation as

\[
\boxed{
\partial_sw
-\nu\Delta w
+\frac12Dw
+\frac12w
+(U\cdot\nabla)w
+(w\cdot\nabla)U
+\nabla\pi=0.
}
\]

Take the \(L^2(B_R)\) inner product with \(Dw\).

## 3. Vector Rellich identity for the Laplacian

For each component of a no-slip vector field,

\[
w|_{S_R}=0.
\]

The standard dilation Rellich calculation gives in three dimensions

\[
\boxed{
\int_{B_R}\Delta w\cdot Dw
=\frac12\int_{B_R}|\nabla w|^2
+\frac R2\int_{S_R}|\partial_nw|^2dS.
}
\]

Therefore the viscous term contributes

\[
\boxed{
-\frac\nu2\|\nabla w\|_2^2
-\frac{\nu R}{2}\|\partial_nw\|_{L^2(S_R)}^2.
}
\]

The boundary shear appears with exactly the expected Rellich weight \(R\).

## 4. Pressure cancels exactly

Because

\[
\nabla\cdot w=0,
\]

we have

\[
\nabla\cdot(Dw)
=D(\nabla\cdot w)+\nabla\cdot w=0.
\]

At the no-slip boundary,

\[
Dw=R\partial_nw.
\]

Moreover divergence-free no-slip implies

\[
\partial_nw\cdot n=0.
\]

Hence

\[
Dw\cdot n=0
\quad\text{on }S_R.
\]

Thus

\[
\boxed{
\int_{B_R}\nabla\pi\cdot Dw=0.
}
\]

So pressure is not the obstruction to the Rellich strategy.

## 5. Exact dilation terms

The explicit similarity-dilation term gives

\[
\boxed{
\frac12\int|Dw|^2.
}
\]

The amplitude term gives

\[
\frac12\int w\cdot Dw
=-\frac34\|w\|_2^2.
\]

Consequently the instantaneous identity is

\[
\boxed{
\begin{aligned}
\frac{\nu R}{2}
\int_{S_R}|\partial_nw|^2dS
={}&
\int_{B_R}\partial_sw\cdot Dw
+\frac12\|Dw\|_2^2\\
&-\frac\nu2\|\nabla w\|_2^2
-\frac34\|w\|_2^2
+\mathcal B_U[w],
\end{aligned}}
\]

where

\[
\mathcal B_U[w]
:=
\int (U\cdot\nabla)w\cdot Dw
+
\int (w\cdot\nabla)U\cdot Dw.
\]

## 6. Period integration does not remove the time-dilation action

The relative-periodic return and rotational invariance of \(D\) imply periodicity of ordinary quadratic norms. However

\[
\boxed{
\mathcal A_D[w]
:=
\int_0^S\int\partial_sw\cdot Dw
}
\]

is not the derivative of a scalar quadratic energy.

Indeed

\[
D^*=-D-3
\]

on the no-slip ball, and \(D+3/2\) is skew-adjoint. Hence \(\mathcal A_D\) is a genuine dilation-action/geometric-phase term. Periodicity only gives the tautological antisymmetry relation; it does not force

\[
\mathcal A_D=0.
\]

Thus the hoped-for cancellation does not occur.

## 7. The scaling is too large for an o(R) shear upper bound

From M19-232,

\[
\int_0^{S_j}\|\nabla w_j\|_2^2ds\to\frac1{4\nu}.
\]

But pointwise in the cavity,

\[
|Dw_j|\le R_j|\nabla w_j|.
\]

Therefore the only automatic bound is

\[
\boxed{
\int_0^{S_j}\|Dw_j\|_2^2ds
\le
R_j^2
\int_0^{S_j}\|\nabla w_j\|_2^2ds
=O(R_j^2).
}
\]

The Rellich identity then permits

\[
R_j
\int_0^{S_j}\int_{S_{R_j}}|\partial_nw_j|^2
=O(R_j^2),
\]

or equivalently

\[
\int_0^{S_j}\int_{S_{R_j}}|\partial_nw_j|^2
=O(R_j),
\]

which is exactly the scale required by the M19-235 lower bound.

The background terms are not the dominant problem. On the M19-234 boundary-layer branch the remote coefficients are small, and their natural estimates are lower order than the allowed \(R_j^2\) dilation currency.

## 8. Critical-tail interpretation of the surviving payer

Introduce the similarity material/dilation derivative

\[
\mathcal D_s
:=
\partial_s+\frac12D.
\]

Then the two largest Rellich terms combine as

\[
\int\partial_sw\cdot Dw
+\frac12\int|Dw|^2
=
\int(\mathcal D_sw)\cdot Dw.
\]

For a critical scattering profile

\[
w\sim r^{-1}B\left(\log r-\frac s2,\omega\right),
\]

the q-translation part is annihilated by \(\mathcal D_s\). Thus the large dilation action is not an accidental estimate defect; it is tied directly to the critical similarity conveyor already present in the scattering architecture.

This explains why a naive Rellich inequality does not automatically improve the shear scale.

## 9. NO-GO and new requirement

The calculation proves

\[
\boxed{
\text{natural dilation Rellich identity}
\neq
\text{o}(R)\text{ boundary-shear upper bound}.
}
\]

The boundary term is exposed cleanly and pressure cancels, but an \(O(R^2)\) bulk dilation-action payer remains.

To close M19-235 one now needs one of the following genuinely stronger inputs:

1. a signed estimate showing
   \[
   \mathcal A_D+\frac12\int|Dw|^2=o(R^2);
   \]
2. a boundary-layer normal form that computes the leading \(R^2\) dilation action and proves it is incompatible with a unit multiplier;
3. a transformed/self-adjoint spectral argument for the remote similarity-Stokes cavity operator;
4. a different boundary current whose bulk dual does not contain the critical dilation action.

## 10. Updated frontier

The M19-235 shear payer remains valid, but the simplest Rellich closure is exhausted:

\[
\boxed{
\mathcal T_{cav}^{BL-spec}:
\text{resolve the singular relative boundary layer by its leading similarity-Stokes spectral/transport normal form.}
}
\]

---

\[
\boxed{\text{M19-236 COMPLETE: PRESSURE-FREE RELLICH EXPOSURE IS VALID, BUT THE R-SQUARED DILATION ACTION PREVENTS A SHEAR CONTRADICTION.}}
\]
