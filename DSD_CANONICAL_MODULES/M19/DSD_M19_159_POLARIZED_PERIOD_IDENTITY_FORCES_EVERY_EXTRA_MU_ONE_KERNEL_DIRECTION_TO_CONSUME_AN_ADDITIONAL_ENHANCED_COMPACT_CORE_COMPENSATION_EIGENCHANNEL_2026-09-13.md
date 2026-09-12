# DSD M19-159 — Polarized period identity forces every extra mu=1 kernel direction to consume an additional enhanced compact-core compensation eigenchannel

**Date:** 2026-09-13  
**Status:** ACTIVE M19 CALCULATION / KERNEL-MULTIPLICITY TO COMPENSATION-EIGENVALUE REDUCTION / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-157 reduced kernel rigidity to a finite Hermitian compensation matrix.
M19-158 raised the bare quarter-gap to

\[
\Lambda_{hard}
=
\frac14+\nu\lambda_P
>
\frac14
\]

on normalized nonsymmetry hard modes.

The present module uses the **polarized** vorticity identity to turn an extra `mu=1` kernel direction into a precise multiplicity requirement on the compact-core compensation spectrum.

## 2. Polarized vorticity identity

For two linearized perturbations `W_1,W_2` with vorticities

\[
\eta_j=\nabla\times W_j,
\]

polarization of the exact M19-087 identity gives

\[
\boxed{
\frac12\frac d{ds}
\langle\eta_1,\eta_2\rangle
+
\nu\langle\nabla\eta_1,\nabla\eta_2\rangle
+
\frac14\langle\eta_1,\eta_2\rangle
=
\mathfrak C_U(W_1,W_2).
}
\]

Here `mathfrak C_U` is the Hermitian polarization of the linearized-vorticity compensation form.

## 3. Same unit multiplier removes the period boundary term

Suppose both perturbations belong to the same twisted Floquet eigenspace with unit multiplier

\[
\mu\in S^1.
\]

Then

\[
W_j(S)=\mu Q_*W_j(0),
\]

and likewise

\[
\eta_j(S)=\mu Q_*\eta_j(0).
\]

Because `Q_*` is orthogonal and `|mu|=1`,

\[
\langle\eta_1(S),\eta_2(S)\rangle
=
\langle\eta_1(0),\eta_2(0)\rangle.
\]

Integrating the polarized identity over one period therefore yields

\[
\boxed{
\int_0^S
\mathfrak C_U(W_1,W_2)ds
=
\nu\int_0^S
\langle\nabla\eta_1,\nabla\eta_2\rangle ds
+
\frac14\int_0^S
\langle\eta_1,\eta_2\rangle ds.
}
\]

Hence on **every fixed unit-multiplier eigenspace**, the period-averaged compensation form equals the positive damping form exactly.

## 4. The mu=1 eigenspace

Let

\[
E_1
:=
\ker(I-\mathcal M_S^{tw}).
\]

Split

\[
E_1
=
E_{sym}^{\mu=1}
\oplus
K_{nsym}
\]

with respect to the scattering-pullback metric.

Let

\[
d_0:=\dim E_{sym}^{\mu=1},
\qquad
k:=\dim K_{nsym}.
\]

Thus

\[
\dim E_1=d_0+k.
\]

For generic nontrivial RDSS holonomy, `d_0` includes the time/scaling phase and the rotation generator along the holonomy axis; special isotropy or DSS (`Q_*=I`) may change this count. The argument below keeps `d_0` abstract and representation-safe.

## 5. Generalized compensation operator

Define the period vorticity Gram form

\[
\overline G(v,v)
:=
\int_0^S\|\eta_v(s)\|_2^2ds
\]

and compensation form

\[
\overline C(v,v)
:=
\int_0^S\mathcal C_U[W_v(s)]ds.
\]

On the non-curl-free hard space `overline G` is positive definite.

Define the generalized Hermitian compensation operator

\[
\boxed{
K_{comp}
:=
\overline G^{-1/2}
\overline C
\overline G^{-1/2}.
}
\]

For every `v in E_1`, the exact period identity gives

\[
\frac{\overline C(v,v)}{\overline G(v,v)}
=
\frac14
+
\nu
\frac{\overline D(v,v)}{\overline G(v,v)}.
\]

## 6. Enhanced threshold on the full mu=1 hard eigenspace

The compact-hard-fiber argument of M19-158 applies to every normalized non-curl-free vector in the finite `mu=1` eigenspace after exact gauge modes with zero vorticity have been removed.

Thus, on a compact fixed-rank stratum, there exists

\[
\lambda_{P,1}>0
\]

such that

\[
\overline D(v,v)
\ge
\lambda_{P,1}\overline G(v,v)
\qquad
\forall v\in E_1.
\]

Set

\[
\boxed{
\Lambda_1
:=
\frac14+\nu\lambda_{P,1}
>
\frac14.
}
\]

Then every nonzero `v in E_1` obeys

\[
\boxed{
\frac{\overline C(v,v)}{\overline G(v,v)}
\ge
\Lambda_1.
}
\]

## 7. Min-max multiplicity consequence

Let

\[
\kappa_1\ge\kappa_2\ge\cdots
\]

be the eigenvalues of `K_comp` on the finite hard fiber.

Because the `(d_0+k)`-dimensional subspace `E_1` has Rayleigh quotient at least `Lambda_1`, the Courant--Fischer min-max principle gives

\[
\boxed{
\kappa_{d_0+k}
\ge
\Lambda_1.
}
\]

In particular, the existence of **one** nonsymmetry kernel direction (`k>=1`) forces

\[
\boxed{
\kappa_{d_0+1}
\ge
\Lambda_1.
}
\]

This is the precise version of the earlier phrase "a second compensation channel is required."

The channel count is representation-aware: it is the first eigenchannel beyond the exact `mu=1` symmetry multiplicity `d_0`.

## 8. Stronger statement for multiple kernel directions

If

\[
\dim K_{nsym}=k,
\]

then at least `d_0+k` generalized compensation eigenvalues must satisfy

\[
\boxed{
\kappa_j\ge\Lambda_1,
\qquad
1\le j\le d_0+k.
}
\]

Equivalently,

\[
\boxed{
\#\{j:\kappa_j\ge\Lambda_1\}
\ge d_0+k.
}
\]

Thus kernel multiplicity is converted into a compact-core spectral-count requirement.

## 9. Scalar sufficient criteria

The eigenvalue-count formulation yields several sufficient kernel-exclusion tests.

### (a) Direct eigenvalue test

If

\[
\boxed{
\kappa_{d_0+1}<\Lambda_1,
}
\]

then

\[
\boxed{K_{nsym}=0.}
\]

### (b) Positive-trace test

If `K_comp^+` denotes the positive part and

\[
\boxed{
\operatorname{tr}K_{comp}^+
<
(d_0+1)\Lambda_1,
}
\]

then a nonsymmetry kernel is impossible.

### (c) Hilbert--Schmidt test

If

\[
\boxed{
\|K_{comp}^+\|_{HS}^2
<
(d_0+1)\Lambda_1^2,
}
\]

then again

\[
K_{nsym}=0.
\]

These are sufficient, not necessary, criteria.

## 10. Why this is stronger than a norm ceiling

A crude operator-norm estimate only controls

\[
\kappa_1.
\]

But the exact symmetries may already consume one or more large compensation channels.

The true nonsymmetry question is therefore not whether the **largest** compact-core amplification exceeds the threshold. It is whether the first eigenvalue **beyond the exact symmetry multiplicity** does:

\[
\boxed{
\kappa_{d_0+1}
\stackrel{?}{<}
\Lambda_1.
}
\]

This is a substantially sharper target.

## 11. Relation to background stretching

The background enstrophy identity supplies a positive average stretching channel, and exact time/rotation symmetries may naturally occupy part of the high compensation spectrum.

The present result says that a nonsymmetry kernel needs an **additional independent high-compensation direction**.

Therefore a promising next step is not another scalar upper bound on total stretching, but an upper bound on the **rank or second/next singular value** of the compact-core compensation operator after the exact symmetry block is removed.

## 12. Audit verdict

### Proved

1. The period-averaged polarized damping-minus-compensation form vanishes identically on each fixed unit-multiplier eigenspace.
2. The `mu=1` eigenspace therefore lies entirely above the enhanced compensation threshold `Lambda_1` in generalized Rayleigh quotient.
3. Every extra nonsymmetry kernel dimension consumes one additional compensation eigenchannel above that threshold.
4. Kernel rigidity follows from the finite spectral condition
   \[
   \kappa_{d_0+1}<\Lambda_1.
   \]

### Not proved

The required upper bound on `kappa_{d_0+1}` has not yet been established from the Navier--Stokes background geometry.

## 13. Next target

M19-160 should inspect the compact-core compensation operator itself and determine whether its high-eigenvalue part can be shown to have rank no larger than the exact symmetry compensation block.

The first decomposition should separate

\[
\text{local strain stretching}
\quad\text{from}\quad
\text{nonlocal vorticity-gradient commutator},
\]

and ask whether either part can support an independent `(d_0+1)`-st eigenchannel above `Lambda_1`.
