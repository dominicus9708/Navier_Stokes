# DSD M19-176 — A Cesaro invariant vorticity-mean metric normalizes the average hard enstrophy exactly to the hard dimension and removes the arbitrary g-minus constant

**Date:** 2026-09-13  
**Status:** ACTIVE M19 CALCULATION / CANONICAL HARD-FIBER NORMALIZATION / DIMENSION CRITERION CLEANUP / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-174--175 formulate the dimension-one criterion using the lower norm-equivalence constant

\[
g_->0
\]

between a scattering-normalized hard vector and its long-time vorticity mass.

That constant is useful for qualitative compactness, but it depends on the chosen normalization of the hard-fiber scattering metric.

The present module constructs a vorticity-mean metric on the finite hard fiber for which the average collective vorticity mass is exactly the fiber dimension.

Thus

\[
\boxed{g_-=1}
\]

in the normalized mean criterion.

The cost is that the collective Lieb--Thirring constants retain an intrinsic instantaneous metric-distortion factor.

## 2. Pulled-back vorticity observation form

Fix a typical complete orbit on a compact recurrent hard component and its initial real quotient hard fiber

\[
E_q(0).
\]

For `v,w in E_q(0)`, define the time-`t` pulled-back vorticity form

\[
\boxed{
G_t(v,w)
:=
\left\langle
\operatorname{curl}\Phi_t v,
\operatorname{curl}\Phi_t w
\right\rangle_{L^2}.
}
\]

Because the hard cocycle is finite-dimensional and uniformly controlled on the compact corridor,

\[
G_t
\]

is a bounded family of positive semidefinite Hermitian matrices on `E_q(0)`.

The retained vorticity observability excludes a nonzero hard vector whose vorticity vanishes for all times.

## 3. Cesaro average metric

Define

\[
\boxed{
\overline G_T
:=
\frac1T\int_0^T G_t\,dt.
}
\]

Since the matrix space is finite-dimensional and `overline G_T` is uniformly bounded, every sequence `T_n->infinity` has a subsequence such that

\[
\overline G_{T_n}
\to
G_\infty
\]

in matrix norm.

On the retained hard component, average vorticity observability gives

\[
\boxed{
G_\infty>0
}
\]

on the quotient hard fiber.

Thus `G_infinity` is a genuine inner product.

## 4. Time-shift invariance of the mean form

For a fixed shift `tau`, compare

\[
\frac1T\int_0^T G_{t+\tau}\,dt
\]

with

\[
\frac1T\int_0^T G_t\,dt.
\]

Their difference consists only of two boundary intervals of total length `2|tau|`, divided by `T`.

Hence

\[
\left\|
\frac1T\int_0^T G_{t+\tau}dt
-
\frac1T\int_0^T G_tdt
\right\|
\to0.
\]

Therefore the limiting mean metric is invariant under the hard cocycle in the Cesaro sense.

Equivariantly along the orbit, one may transport it as

\[
G_\infty(\sigma_\tau U)
=
(\Phi_\tau^{-1})^*
G_\infty(U)
\Phi_\tau^{-1}.
\]

## 5. Normalize the initial hard basis

Choose

\[
v_1,\ldots,v_N
\]

orthonormal in the mean metric:

\[
\boxed{
G_\infty(v_i,v_j)=\delta_{ij}.
}
\]

Transport them by the cocycle.

For each `j`, by definition of `G_infinity`,

\[
\lim_{n\to\infty}
\frac1{T_n}
\int_0^{T_n}
\|\eta_j(t)\|_2^2dt
=1.
\]

Summing over the basis gives

\[
\boxed{
\left\langle
Z_N
\right\rangle
=
\left\langle
\sum_{j=1}^N\|\eta_j\|_2^2
\right\rangle
=N.
}
\]

Thus the average collective hard enstrophy is exactly the real hard dimension.

## 6. Dimension criterion without g-minus

The recurrent mean inequality from M19-175 becomes

\[
\boxed{
\frac14N
\le
\widetilde C_{str}N^{3/5}
+
\widetilde C_aN^{d(a)}.
}
\]

Divide by `N>0`:

\[
\boxed{
\frac14
\le
\widetilde C_{str}N^{-2/5}
+
\widetilde C_aN^{d(a)-1}.
}
\]

Therefore the exact two-mode sufficient criterion is now

\[
\boxed{
\widetilde C_{str}2^{-2/5}
+
\widetilde C_a2^{d(a)-1}
<
\frac14
\Longrightarrow
N\le1.
}
\]

No arbitrary lower observability normalization `g_-` appears.

## 7. What replaces g-minus

The collective Lieb--Thirring/HLS estimates are easiest for instantaneous `L2`-orthonormal vorticity families.
The transported `G_infinity`-orthonormal family need not be instantaneously `L2` orthonormal.

Define the instantaneous vorticity Gram matrix

\[
\boxed{
\mathsf G(t)_{ij}
:=
\langle\eta_i(t),\eta_j(t)\rangle_{L^2}.
}
\]

The relevant intrinsic distortion is

\[
\boxed{
\kappa_G
:=
\sup_t
\frac{\lambda_{max}(\mathsf G(t))}
{\max\{\lambda_{min}(\mathsf G(t)),\,\text{appropriate nonzero hard-floor}\}}.
}
\]

More invariantly, the collective density estimates depend on the uniform occupation-number bound of the instantaneous density matrix relative to the mean metric.

Compact hard-bundle regularity gives this quantity finite on a fixed nondegenerate stratum.

Thus the arbitrary scalar `g_-` is replaced by an intrinsic frame-distortion constant already hidden in the prior generic `C` constants.

## 8. Basis-invariant density-matrix formulation

Instead of choosing an instantaneous orthonormal frame, one may write the hard density operator using the mean-metric orthogonal projector

\[
P_{hard}^{G_\infty}.
\]

Its vorticity observation defines a positive finite-rank density matrix. The Lieb--Thirring inequality extends to finite-rank density matrices with a factor equal to the maximal occupation number.

Hence the prior collective estimates remain valid in the form

\[
\boxed{
\int\rho^{5/3}
\le
C_{LT}\,\kappa_{occ}^{2/3}
P_N,
}
\]

for an intrinsic occupation/distortion constant `kappa_occ` controlled on the compact stratum.

This is the representation-safe way to carry the mean normalization through the collective estimates.

## 9. Improvement to the constant audit

The dimension-one test no longer depends on

\[
g_-.
\]

The true solution-dependent quantities are now

\[
\boxed{
\kappa_{occ},
\quad
\Lambda_P^+,
\quad
M_{5/2},
\quad
M_a,
}
\]

plus universal harmonic-analysis constants.

This is a cleaner target for either analytic sharpening or a future computer-assisted compact-corridor verification.

## 10. Important scope note

The Cesaro metric may depend on the chosen ergodic component or subsequential invariant mean if the recurrent component is not uniquely ergodic.

That does not affect the dimension argument: the trace/dimension inequality is applied component-by-component.

One should not claim a single canonical metric on the entire global W1 set without additional unique-ergodicity structure.

## 11. Audit verdict

### Proved on each retained recurrent hard component

1. Existence of a positive Cesaro vorticity-mean metric on the finite hard fiber.
2. Mean-metric normalization makes
   \[
   \langle Z_N\rangle=N.
   \]
3. The dimension-one threshold can be written without the arbitrary `g_-` normalization constant.

### Not proved

1. A sufficiently small intrinsic distortion/occupation constant.
2. The strict two-mode inequality.
3. Global regularity.

## 12. Next target

M19-177 should complete the constant audit in this mean normalization.

It should distinguish:

- **universal explicit constants:** Lieb--Thirring, HLS, Calderon--Zygmund;
- **background corridor norms:** `M_{5/2}`, `M_a`;
- **hard-bundle spectral constants:** `kappa_occ`, `Lambda_P^+`.

The decisive question is which of the last two groups can be bounded directly from already certified Type-I/scattering data and which represent genuinely new quantitative information.
