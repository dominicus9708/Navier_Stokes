# DSD M19-167 — Polarized hard-mode cross tensors inherit the five-quarter gap, but scattering orthogonality does not cancel their pointwise source tuple

**Date:** 2026-09-13  
**Status:** ACTIVE M19 CALCULATION / CROSS-TENSOR AUDIT / DIRECT TENSOR-KERNEL SHORTCUT CLOSED / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-166 proved a strong `5/4` essential gap for the homogeneous anisotropy-tensor cocycle.
A natural hope is that two hard unit modes with the same Floquet multiplier might have a cross tensor whose forcing vanishes after the scattering/gauge orthogonality conditions are imposed.

If that were true, an extra kernel direction could create a homogeneous tensor unit mode and be attacked directly by the stronger tensor gap.

The present module computes the cross equation. The hoped-for forcing cancellation does not occur in general.

## 2. Two same-multiplier hard modes

Let

\[
W_1,W_2
\]

be two linearized hard perturbations with vorticities

\[
\eta_j=\nabla\times W_j,
\]

and suppose they have the same twisted Floquet multiplier

\[
\mu\in S^1.
\]

Thus

\[
W_j(S)=\mu Q_*W_j(0),
\qquad
\eta_j(S)=\mu Q_*\eta_j(0).
\]

## 3. Polarized cross tensor

Define the symmetric cross tensor

\[
\boxed{
\Gamma_{12}
:=
\frac12
\left(
\eta_1\otimes\eta_2
+
\eta_2\otimes\eta_1
\right).
}
\]

Its scalar trace is

\[
\boxed{
\rho_{12}
:=
\operatorname{tr}\Gamma_{12}
=
\eta_1\cdot\eta_2.
}
\]

Define the traceless cross anisotropy

\[
\boxed{
Q_{12}
:=
\Gamma_{12}
-
\frac{\rho_{12}}3I.
}
\]

## 4. Polarized gradient and nonlocal source tensors

Set

\[
\boxed{
\mathcal G_{12}
:=
\frac12
\sum_k
\left(
\partial_k\eta_1\otimes\partial_k\eta_2
+
\partial_k\eta_2\otimes\partial_k\eta_1
\right).
}
\]

Let

\[
F_j
:=
(\Omega\cdot\nabla)W_j
-
(W_j\cdot\nabla)\Omega.
\]

Define

\[
\boxed{
\mathcal F_{12}
:=
\frac12
\left(
F_1\otimes\eta_2
+
\eta_2\otimes F_1
+
F_2\otimes\eta_1
+
\eta_1\otimes F_2
\right).
}
\]

Take traceless parts `G_12^circ,F_12^circ` in the usual way.

## 5. Exact cross-anisotropy equation

Polarizing M19-163 gives

\[
\boxed{
\begin{aligned}
\partial_sQ_{12}
={}&
\nu\Delta Q_{12}
-
2Q_{12}
-
\frac12(y\cdot\nabla)Q_{12}
-
(U\cdot\nabla)Q_{12}\\
&+
(SQ_{12}+Q_{12}S)^\circ
+
[R,Q_{12}]\\
&-
2\nu\mathcal G_{12}^\circ
+
\frac{2\rho_{12}}3S
+
\mathcal F_{12}^\circ.
\end{aligned}
}
\]

Thus the cross tensor has the **same homogeneous 5/4 tensor operator** as the diagonal anisotropy tensor.

## 6. Same-multiplier return

Because both modes have the same unit multiplier,

\[
\Gamma_{12}(S)
=
Q_*\Gamma_{12}(0)Q_*^T,
\]

and therefore

\[
Q_{12}(S)
=
Q_*Q_{12}(0)Q_*^T.
\]

Hence the cross tensor is twisted-periodic with the background representation; the scalar phase `mu` cancels from the quadratic tensor.

## 7. Scattering orthogonality is only global/fiberwise

Choose the two hard modes scattering-orthogonal:

\[
\langle v_1,v_2\rangle_{sc}=0.
\]

This does **not** imply

\[
\eta_1(y,s)\cdot\eta_2(y,s)=0
\]

pointwise.

Therefore

\[
\boxed{
\rho_{12}(y,s)
\text{ need not vanish.}
}
\]

Likewise scattering orthogonality does not imply

\[
\mathcal G_{12}^\circ=0
\]

or

\[
\mathcal F_{12}^\circ=0.
\]

## 8. Even vorticity-Gram orthogonality is insufficient

Because the hard space is finite-dimensional, one may choose a basis with period-averaged vorticity Gram orthogonality:

\[
\int_0^S\int
\eta_1\cdot\eta_2
=0.
\]

One may also diagonalize the period gradient form on that basis.

But these are integrated relations only. They do not imply

\[
\rho_{12}S=0
\]

pointwise or after weighted pairing with a nonconstant strain field.

Similarly

\[
\int\nabla\eta_1:\nabla\eta_2=0
\]

does not imply

\[
\mathcal G_{12}^\circ=0.
\]

Thus the cross source remains genuinely nonzero in general.

## 9. Consequence for the tensor-gap strategy

The forced cross equation can be written

\[
\partial_sQ_{12}
=
\mathcal A_Q(s)Q_{12}
+
\mathcal S_{12},
\]

where

\[
\boxed{
\mathcal S_{12}
=
-2\nu\mathcal G_{12}^\circ
+
\frac{2\rho_{12}}3S
+
\mathcal F_{12}^\circ.
}
\]

There is no general reason for

\[
\mathcal S_{12}=0.
\]

Therefore an extra hard kernel direction does **not** automatically generate a homogeneous tensor unit mode.

Permanent firewall:

\[
\boxed{
\text{same Floquet phase + fiber orthogonality}
\neq
\text{zero polarized tensor forcing}.
}
\]

## 10. What remains useful

The cross tensor still obeys the stronger bare tensor gap.

Hence any persistent large cross anisotropy must be maintained by the polarized source tuple

\[
(\rho_{12}S,\mathcal G_{12}^\circ,\mathcal F_{12}^\circ).
\]

This supplies another family of orientation constraints, but it does not by itself reduce kernel multiplicity to the homogeneous tensor spectrum.

## 11. Audit verdict

### Proved

1. Exact polarized cross-tensor equation.
2. Exact `5/4` homogeneous gap for the cross tensor.
3. Same unit Floquet phase cancels from the quadratic tensor return law.
4. Scattering orthogonality, period Gram orthogonality, and gradient-form orthogonality do not cancel the pointwise polarized source tuple.

### Therefore

\[
\boxed{
\text{the direct cross-tensor-to-homogeneous-tensor shortcut is closed.}
}
\]

## 12. Next target

The kernel problem should now return to the finite-dimensional Fredholm object itself.

M19-168 should define a symmetry-reduced Evans/Fredholm determinant for the compact hard monodromy,

\[
D_U(z)
=
\det
\left(
I-z^{-1}\mathcal M_{S,q}^{tw}
\right),
\]

and separate:

- kernel crossings `D_U(1)=0`;
- irrational elliptic roots `D_U(e^{i\vartheta})=0`;
- exact symmetry factors already removed.

The aim is to obtain a finite-dimensional topological/spectral-flow invariant for the remaining unit-spectrum problem.
