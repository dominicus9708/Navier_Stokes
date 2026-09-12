# DSD M19-158 — Compact hard fibers force a uniform vorticity Poincare gap and raise the unit-mode compensation threshold above one quarter

**Date:** 2026-09-13  
**Status:** ACTIVE M19 CALCULATION / POSITIVE COERCIVITY IMPROVEMENT ON THE FINITE HARD FIBER / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-157 reduced nonsymmetry kernel rigidity to positivity of the finite-dimensional period-averaged Hermitian form

\[
\overline H
=
\nu\overline D
+
\frac14\overline G
-
\overline C.
\]

The present module strengthens the positive part.

The finite observable hard fiber is compact after symmetry quotient and the unit modes have a uniform compact-core vorticity floor. Therefore normalized hard modes cannot approach a whole-space zero-gradient vorticity field.

This produces a uniform Poincare-type gap **on the hard bundle itself**, even though no global Poincare inequality exists on all of `R3`.

## 2. Normalized quotient hard sphere

Fix a compact moderate RSS or bounded-period RDSS stratum after the exact time/rotation gauges.

Let

\[
E_q(U)
\]

be the finite-dimensional symmetry-quotient hard fiber from M19-157.

Normalize with the scattering pullback metric:

\[
\|v\|_{sc,U}=1.
\]

Let

\[
W_v(s)=\Phi_s(U)v,
\qquad
\eta_v(s)=\nabla\times W_v(s).
\]

M19-131--150 give uniform observability and a compact-core activity floor for every nonsymmetry unit mode. In particular, after excluding exact curl-free gauge modes,

\[
\boxed{
\inf_{(U,v)}
\int_0^S\|\eta_v(s)\|_2^2ds
>0
}
\]

on each compact fixed-rank stratum.

## 3. Zero-gradient limit is impossible

Suppose, to the contrary, there exists a sequence of normalized hard vectors `(U_n,v_n)` with

\[
\frac{
\int_0^{S_n}\|\nabla\eta_n(s)\|_2^2ds
}{
\int_0^{S_n}\|\eta_n(s)\|_2^2ds
}
\to0.
\]

On a bounded-period compact stratum,

\[
0<S_-\le S_n\le S_+<\infty.
\]

Finite-dimensional hard-bundle compactness and the retained smooth spectator/core bounds give, after subsequence and bundle trivialization,

\[
(U_n,v_n)\to(U_*,v_*),
\]

with

\[
\|v_*\|_{sc,U_*}=1.
\]

The corresponding vorticity perturbations converge strongly on compact sets and weakly in the global energy spaces. Lower semicontinuity gives

\[
\int_0^{S_*}\|\nabla\eta_*(s)\|_2^2ds=0.
\]

Hence

\[
\nabla\eta_*(s)=0
\]

for almost every time.

Therefore each spatial component of `eta_*` is constant in `y`.

But

\[
\eta_*(s)\in L^2(\mathbb R^3),
\]

so the only spatially constant possibility is

\[
\boxed{\eta_*(s)\equiv0.}
\]

This contradicts the uniform compact-core vorticity activity floor and hard-mode observability.

## 4. Uniform hard-fiber Poincare ratio

Therefore there exists

\[
\boxed{\lambda_P>0}
\]

such that every normalized nonsymmetry hard mode satisfies

\[
\boxed{
\int_0^S\|\nabla\eta_v(s)\|_2^2ds
\ge
\lambda_P
\int_0^S\|\eta_v(s)\|_2^2ds.
}
\]

This is not a global Poincare inequality on `R3`.

It is a compact-fiber spectral gap on the finite-dimensional family of interior-realizable hard perturbations.

Permanent firewall:

\[
\boxed{
\text{hard-fiber Poincare gap}
\neq
\text{whole-space Poincare inequality}.
}
\]

## 5. Enhanced quarter-gap

For a unit Floquet mode, M19-150 gives

\[
\int_0^S\mathcal C_U[W]ds
=
\nu\int_0^S\|\nabla\eta\|_2^2ds
+
\frac14\int_0^S\|\eta\|_2^2ds.
\]

Apply the hard-fiber gap:

\[
\boxed{
\int_0^S\mathcal C_U[W]ds
\ge
\left(
\frac14+\nu\lambda_P
\right)
\int_0^S\|\eta\|_2^2ds.
}
\]

Thus any nonsymmetry unit multiplier must be supported by average compact-core compensation strictly larger than the bare quarter-gap.

Define

\[
\boxed{
\Lambda_{hard}
:=
\frac14+\nu\lambda_P
>
\frac14.
}
\]

Then the live unit-spectrum condition becomes

\[
\boxed{
\frac{
\int_0^S\mathcal C_U[W]ds
}{
\int_0^S\|\eta\|_2^2ds
}
\ge
\Lambda_{hard}.
}
\]

## 6. Finite Hermitian matrix consequence

In the notation of M19-157,

\[
\overline D
\ge
\lambda_P\overline G
\]

as quadratic forms on the normalized quotient hard fiber.

Therefore

\[
\boxed{
\overline H
\ge
\left(
\frac14+\nu\lambda_P
\right)\overline G
-
\overline C.
}
\]

A sufficient kernel-rigidity criterion is now the stronger finite matrix inequality

\[
\boxed{
\lambda_{max}
\left(
\overline G^{-1/2}\overline C\,\overline G^{-1/2}
\right)
<
\frac14+\nu\lambda_P.
}
\]

If it holds uniformly, then

\[
\boxed{K_{nsym}=0.}
\]

The same inequality excludes every nonsymmetry unit Floquet mode, not only `mu=1`, because M19-150's one-period balance holds for all `|mu|=1`.

## 7. Gain over the previous Ky-Fan criterion

Earlier Ky-Fan estimates required, schematically,

\[
\text{compensation}\ge\frac14
\]

per neutral channel.

The present compact-fiber argument raises the threshold to

\[
\boxed{
\frac14+\nu\lambda_P.
}
\]

This matters because the extra positive amount is **geometric/spectral**, not another unsigned parent-space ancestry payment.

It comes from the impossibility of a normalized interior-realizable hard vorticity mode becoming spatially constant.

## 8. Scope and failure modes

The argument requires:

1. a compact fixed-rank hard spectral bundle;
2. bounded periods on the stratum;
3. uniform scattering observability;
4. exclusion/quotient of exact curl-free gauge modes;
5. a uniform nonzero compact-core vorticity floor.

Failure of these assumptions is already typed as

- period escape `S->infinity`;
- spectral-bundle rank degeneration;
- isotropy/gauge degeneration;
- hard-mode observability failure;
- state compactness loss.

The result is therefore appropriately local to the retained moderate compact hard corridor.

## 9. Audit verdict

### Proved on the retained compact hard stratum

\[
\boxed{
\exists\lambda_P>0:
\quad
\int\|\nabla\eta\|_2^2
\ge
\lambda_P\int\|\eta\|_2^2
}
\]

for normalized nonsymmetry hard modes.

Hence every unit mode requires average compensation at least

\[
\boxed{
\Lambda_{hard}
=
\frac14+\nu\lambda_P.
}
\]

### Not proved

The present module does not yet prove that the compact-core compensation operator has spectral radius below `Lambda_hard`.

That is now the exact remaining sign/index problem.

## 10. Next target

M19-159 should separate the exact symmetry compensation block from the nonsymmetry block and compute the Schur complement of the finite period-averaged Hermitian matrix.

The goal is to show that a nonsymmetry unit mode can exist only if the **second compact-core compensation eigenchannel** reaches the enhanced threshold `Lambda_hard`, not merely the bare `1/4` level.
