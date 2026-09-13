# M19-224 — The formal L2 adjoint of the linearized similarity Navier–Stokes operator has a critical r^-2 scattering resonance

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / PHYSICAL PDE-ADJOINT NORMAL FORM

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-219--223 reduce a zero-q bounded-period kernel candidate to a constant-scattering-label invariant hard section and exhaust two obvious pairings: background cross-enstrophy is sign-indefinite, while the hard metric dual is tautologically parallel.

The next object must therefore come from the actual PDE adjoint rather than from the intrinsic hard metric.

This module derives the formal unweighted L2 adjoint of the linearized similarity Navier--Stokes operator and identifies its critical far-field homogeneity.

## 2. Primal linearized similarity equation

Along a smooth retained similarity background U, let W be a divergence-free linearized perturbation with pressure Q:

\[
\boxed{
\partial_s W
=
\nu\Delta W
-\frac12(y\cdot\nabla)W
-\frac12W
-(U\cdot\nabla)W
-(W\cdot\nabla)U
-\nabla Q,
\qquad \nabla\cdot W=0.
}
\]

Set

\[
b(y,s):=\frac y2+U(y,s),
\qquad M:=\nabla U.
\]

Then the spatial velocity operator is

\[
L_UW
=
\nu\Delta W
-b\cdot\nabla W
-\frac12W
-MW
\]

modulo the pressure projection.

Since div U=0,

\[
\nabla\cdot b=\frac32.
\]

## 3. Formal L2 adjoint

For smooth compactly supported divergence-free test fields Psi, integration by parts gives

\[
(-b\cdot\nabla)^*
=b\cdot\nabla+\nabla\cdot b.
\]

Therefore

\[
\boxed{
L_U^*\Psi
=
\nu\Delta\Psi
+b\cdot\nabla\Psi
+\Psi
-M^T\Psi
}
\]

on the solenoidal subspace, with an adjoint pressure multiplier Pi used to enforce divergence-free evolution.

The backward adjoint equation preserving the primal-adjoint pairing is

\[
\boxed{
-\partial_s\Psi
=
\nu\Delta\Psi
+\frac12(y\cdot\nabla)\Psi
+\Psi
+(U\cdot\nabla)\Psi
-(\nabla U)^T\Psi
+\nabla\Pi,
\qquad \nabla\cdot\Psi=0.
}
\]

The sign of Pi is gauge/convention dependent and does not affect the leading critical homogeneity below.

## 4. Bare adjoint similarity transport

Discarding the r^-2-lower-order viscous/background terms, the leading adjoint equation is

\[
\boxed{
\partial_s\Psi
+\frac12(y\cdot\nabla)\Psi
+\Psi
=0.
}
\]

Take

\[
\Psi_0(y,s)
=r^{-a}C(q,\omega),
\qquad
q=\log r-\frac s2.
\]

Then

\[
\partial_s\Psi_0
=-\frac12r^{-a}C_q,
\]

and

\[
\frac12y\cdot\nabla\Psi_0
=
\frac12r^{-a}(-aC+C_q).
\]

Hence

\[
\left(
\partial_s+rac12y\cdot\nabla+1
\right)\Psi_0
=
\left(1-\frac a2\right)r^{-a}C.
\]

Therefore the unique zero coefficient is

\[
\boxed{a=2.}
\]

Thus the adjoint critical scattering sector is

\[
\boxed{
\Psi_0(y,s)
=
\frac1{r^2}C\left(\log r-\frac s2,\omega\right).
}
\]

This is the exact dual homogeneity to the primal critical sector W~r^-1 B.

## 5. First adjoint correction is nonresonant

For the critical adjoint field Psi_0~r^-2 C,

\[
\Delta\Psi_0=O(r^{-4}),
\qquad
(U\cdot\nabla)\Psi_0=O(r^{-4}),
\qquad
(\nabla U)^T\Psi_0=O(r^{-4})
\]

because U=O(r^-1) and grad U=O(r^-2) on the retained critical tail.

An adjoint correction of the form

\[
\Psi_1=r^{-4}D(q,\omega)
\]

obeys

\[
\left(
\partial_s+rac12y\cdot\nabla+1
\right)\Psi_1
=-r^{-4}D.
\]

Thus, just as the primal r^-3 correction is nonresonant, the first adjoint r^-4 correction is nonresonant.

The only leading adjoint resonance in this even inverse-power ladder is r^-2.

## 6. Divergence-free constraint for the adjoint critical datum

Write

\[
C=C_r\omega+C_T,
\qquad C_T\cdot\omega=0.
\]

For a general r^-a vector field with q dependence,

\[
\nabla\cdot\bigl(r^{-a}C(q,\omega)\bigr)
=
r^{-a-1}
\left[
\partial_qC_r+(2-a)C_r+\operatorname{div}_{S^2}C_T
\right].
\]

At the adjoint critical exponent a=2,

\[
\boxed{
\partial_qC_r+\operatorname{div}_{S^2}C_T=0.
}
\]

For the zero-q sector,

\[
\boxed{
\operatorname{div}_{S^2}C_T=0.
}
\]

Hence

\[
\boxed{
C(\omega)
=C_r(\omega)\omega
+\omega\times\nabla_{S^2}\chi(\omega),
}
\]

with arbitrary radial scalar C_r and toroidal scalar chi (modulo the usual constant gauge for chi).

Unlike the primal r^-1 divergence constraint, the zero-q adjoint condition does not tie C_r to a poloidal tangential component.

## 7. Why this matters

The primal q=0 datum has the M19-041 Hodge form

\[
B
=
B_r\omega
-\nabla_{S^2}\Delta_{S^2}^{-1}B_r
+\omega\times\nabla_{S^2}\psi.
\]

The adjoint critical datum has independent radial and toroidal channels.

Therefore the physical PDE adjoint has exactly the right angular degrees of freedom to test both independent primal q=0 channels.

This is stronger than M19-223's abstract metric dual statement: it identifies the far-field homogeneity and Hodge structure that a genuinely physical adjoint witness must carry.

## 8. Certified / not certified

### Certified

1. The formal L2 adjoint differential operator on smooth solenoidal fields.
2. The adjoint critical similarity exponent a=2.
3. The same log-characteristic q=log r-s/2 appears in the adjoint resonant sector.
4. The first adjoint correction r^-4 is nonresonant.
5. For q=0, the adjoint leading tangential field is purely surface-divergence-free/toroidal, while the radial scalar is free.

### Not certified

1. Existence of a global smooth complete adjoint solution with prescribed nonzero r^-2 datum C.
2. Relative-periodic realization of such an adjoint solution.
3. Identification of the M19-223 hard metric covector with a physical adjoint PDE state.
4. Zero-q kernel exclusion.
5. Global regularity.

## 9. Next target

Derive the exact primal-adjoint Green identity on a ball B_R. Because W~r^-1 and Psi~r^-2, the similarity-drift boundary term is scale invariant and should converge to a finite sphere pairing between B and C, while diffusion/background/pressure terms are two powers smaller.

If a relative-periodic adjoint witness exists with nonzero B-C pairing, period integration may directly contradict the existence of the zero-q kernel.
