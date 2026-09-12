# DSD M19-169 — Orthogonal monodromy gives an exact total hard-space trace identity and reduces irrational elliptic exclusion to a single compensation-trace bound for dimension at most one

**Date:** 2026-09-13  
**Status:** ACTIVE M19 CALCULATION / TOTAL HARD-SPACE TRACE IDENTITY / DIMENSION-ONE REDUCTION / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-168 showed that a genuine irrational elliptic obstruction requires at least two real symmetry-quotient hard dimensions.

The present module derives a basis-independent trace identity for the **entire quotient hard space**, without requiring all vectors to have the same Floquet phase.

This converts the target

\[
\dim_{\mathbb R}E_q^{hard}\le1
\]

into one scalar upper bound on total compact-core compensation.

## 2. Quotient hard basis

Let

\[
E_q^{hard}(U)
\]

be the real finite-dimensional hard fiber after exact time/rotation symmetry quotient, with

\[
N
:=
\dim_{\mathbb R}E_q^{hard}.
\]

Choose a scattering-pullback orthonormal basis

\[
v_1,\ldots,v_N.
\]

Transport it by the linearized cocycle:

\[
W_j(s)=\Phi_s v_j,
\qquad
\eta_j(s)=\nabla\times W_j(s).
\]

Because the cocycle is an isometry in the scattering metric, the transported family remains scattering-orthonormal.

## 3. Orthogonal twisted return mixes the basis but preserves the total vorticity norm

At one relative period,

\[
\mathcal M_q^{tw}
\in O(N).
\]

Write its real matrix in the chosen basis as

\[
M=(M_{kj}).
\]

Then

\[
W_j(S)
=
Q_*
\sum_{k=1}^N
M_{kj}W_k(0).
\]

Taking curls,

\[
\eta_j(S)
=
Q_*
\sum_k
M_{kj}\eta_k(0).
\]

Therefore

\[
\begin{aligned}
\sum_j\|\eta_j(S)\|_2^2
&=
\sum_j
\left\|
\sum_kM_{kj}\eta_k(0)
\right\|_2^2\\
&=
\sum_{k,\ell}
\left(
\sum_jM_{kj}M_{\ell j}
\right)
\langle\eta_k(0),\eta_\ell(0)\rangle\\
&=
\sum_k\|\eta_k(0)\|_2^2,
\end{aligned}
\]

because

\[
MM^T=I.
\]

Thus

\[
\boxed{
\sum_j\|\eta_j(S)\|_2^2
=
\sum_j\|\eta_j(0)\|_2^2.
}
\]

This works even when the hard space contains several distinct elliptic phases.

## 4. Sum the exact vorticity identities

For each basis vector,

\[
\frac12\frac d{ds}\|\eta_j\|_2^2
+
\nu\|\nabla\eta_j\|_2^2
+
\frac14\|\eta_j\|_2^2
=
\mathcal C_U[W_j].
\]

Sum over `j=1,...,N` and integrate over one period. The total endpoint term cancels by the orthogonal-return identity.

Hence

\[
\boxed{
\mathfrak T_q
:=
\int_0^S
\sum_{j=1}^N
\mathcal C_U[W_j]ds
=
\nu\int_0^S
\sum_j\|\nabla\eta_j\|_2^2ds
+
\frac14\int_0^S
\sum_j\|\eta_j\|_2^2ds.
}
\]

This is the exact total quotient-hard compensation trace identity.

## 5. Uniform vorticity observability per normalized hard vector

On a compact fixed-rank hard stratum, scattering observability and exclusion of curl-free gauge modes give

\[
\boxed{
\int_0^S\|\eta_v(s)\|_2^2ds
\ge
 g_->0
}
\]

for every scattering-normalized quotient hard vector `v`.

Therefore

\[
\boxed{
\int_0^S
\sum_{j=1}^N\|\eta_j\|_2^2ds
\ge
Ng_-.
}
\]

## 6. Uniform hard-fiber Poincare gap

M19-158 gives

\[
\int_0^S\|\nabla\eta_v\|_2^2ds
\ge
\lambda_P
\int_0^S\|\eta_v\|_2^2ds
\]

uniformly on the compact hard stratum.

Hence

\[
\boxed{
\mathfrak T_q
\ge
\left(
\frac14+\nu\lambda_P
\right)
\int_0^S
\sum_j\|\eta_j\|_2^2ds
\ge
N g_-\Lambda_P,
}
\]

where

\[
\boxed{
\Lambda_P
:=
\frac14+\nu\lambda_P.
}
\]

Thus

\[
\boxed{
N
\le
\frac{\mathfrak T_q}{g_-\Lambda_P}.
}
\]

## 7. Dimension-one sufficient criterion

If the total symmetry-quotient compensation satisfies

\[
\boxed{
\mathfrak T_q
<
2g_-\Lambda_P,
}
\]

then the integer dimension obeys

\[
\boxed{
N\le1.
}
\]

By M19-168, this immediately excludes every genuine irrational elliptic block.

Hence

\[
\boxed{
\mathfrak T_q<2g_-\Lambda_P
\Longrightarrow
\text{no irrational elliptic neutral dynamics}.
}
\]

The only remaining quotient unit spectrum is a one-dimensional finite-iterate kernel channel.

## 8. Full kernel-rigidity sufficient criterion

If the stronger trace bound

\[
\boxed{
\mathfrak T_q
<
g_-\Lambda_P
}
\]

holds, then

\[
N=0.
\]

Therefore

\[
\boxed{
E_q^{hard}=\{0\}
}
\]

and all nonsymmetry unit spectrum is absent.

This is stronger than needed for the first elliptic reduction.

## 9. Collective-tensor representation of the trace

Define the quotient hard-family tensor

\[
\Gamma_q
=
\sum_{j=1}^N
\eta_j\otimes\eta_j,
\]

with traceless part

\[
Q_q
=
\Gamma_q
-
\frac{\rho_q}{3}I.
\]

M19-162 gives

\[
\boxed{
\sum_j
\int
\eta_j\cdot S_U\eta_j
=
\int S_U:Q_q.
}
\]

The nonlocal trace is controlled by the corresponding collective current tensor `J_q` involving `grad Omega`.

Therefore

\[
\boxed{
\mathfrak T_q
=
\int_0^S\!\int
S_U:Q_q
+
\int_0^S\!\int
\nabla\Omega:\mathcal J_q
}
\]

schematically, with the exact nonlocal tensor convention inherited from M19-160--162.

Thus the dimension-one target has become a single collective orientation-trace estimate.

## 10. Why this avoids the different-phase problem

M19-159's min-max argument was sharp for a fixed multiplier eigenspace but does not automatically combine different unit phases into one positive quadratic subspace.

The present trace argument avoids that issue entirely.

Orthogonality of the **monodromy matrix on the whole hard fiber** is enough to cancel the summed endpoint term.

Therefore the estimate is valid simultaneously for

- kernel modes;
- rational elliptic blocks;
- irrational elliptic blocks;
- mixtures of several unit phases.

## 11. New strategic hierarchy

The unit-spectrum problem can now be attacked in two stages.

### Stage A — dimension reduction

Prove

\[
\boxed{
\mathfrak T_q
<
2g_-\Lambda_P.
}
\]

Then

\[
\dim E_q^{hard}\le1
\]

and all irrational elliptic blocks disappear.

### Stage B — final kernel exclusion

Prove either

\[
\mathfrak T_q<g_-\Lambda_P
\]

or separately exclude the remaining one-dimensional finite-iterate kernel.

This is weaker than demanding full strict coercivity at the outset.

## 12. Audit verdict

### Proved

1. Exact total quotient-hard compensation trace identity for arbitrary mixtures of unit phases.
2. Linear lower bound of the trace by the quotient hard dimension.
3. The scalar criterion
   \[
   \mathfrak T_q<2g_-\Lambda_P
   \]
   is sufficient to eliminate irrational elliptic blocks.
4. The stronger scalar criterion
   \[
   \mathfrak T_q<g_-\Lambda_P
   \]
   eliminates all quotient hard modes.

### Not proved

The required upper bound on `mathfrak T_q` is not yet established from the background fields.

## 13. Next target

M19-170 should estimate the collective trace directly using the exact tensor decomposition

\[
\mathfrak T_q
=
\int S_U:Q_q
+
\text{gradient-vorticity current trace},
\]

and the stronger `5/4` evolution law for `Q_q`.

The immediate goal is the weaker threshold

\[
\boxed{
\mathfrak T_q<2g_-\Lambda_P,
}
\]

because that alone removes the genuinely irrational elliptic problem and leaves only a one-dimensional finite-iterate kernel.
