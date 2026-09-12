# DSD M19-177 — Constant audit reduces the hard derivative and background norms to existing Z/P/H/tail data, while the mean-to-instantaneous occupation distortion remains the main new quantitative constant

**Date:** 2026-09-13  
**Status:** ACTIVE M19 CALCULATION / CONSTANT-DEPENDENCY AUDIT / MAIN NONCONSTRUCTIVE CONSTANT ISOLATED / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-176 removed the arbitrary normalization constant `g_-` by using a Cesaro vorticity-mean metric.

The dimension-one criterion now depends on

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

plus universal Lieb--Thirring/HLS/Calderon--Zygmund constants.

The present module determines which of these are reducible to already retained PDE resources and which remain genuinely new quantitative information.

## 2. Universal harmonic-analysis constants

The constants in

- Sobolev;
- Lieb--Thirring/density estimates;
- Hardy--Littlewood--Sobolev;
- Calderon--Zygmund/Riesz transforms

are universal and, in principle, explicit.

They are not solution-dependent proof branches.

Their sharp numerical optimization may matter for the final `N=2` inequality, but they do not represent new Navier--Stokes structural hypotheses.

## 3. Hard derivative ceiling from the linearized vorticity identity

For one hard perturbation,

\[
\frac12 Z'
+
\nu P
+
\frac14 Z
=
\mathcal C_U[W],
\]

where

\[
Z=\|\eta\|_2^2,
\qquad
P=\|\nabla\eta\|_2^2.
\]

### Local strain term

Use

\[
\left|
\int\eta\cdot S_U\eta
\right|
\le
\|S_U\|_3\|\eta\|_3^2.
\]

The 3D Gagliardo--Nirenberg estimate gives

\[
\|\eta\|_3^2
\le
C
Z^{1/2}P^{1/2}.
\]

Hence

\[
\boxed{
|C_{strain}|
\le
\frac{\nu}{8}P
+
C\nu^{-1}\|S_U\|_3^2Z.
}
\]

### Nonlocal term

Using the `grad Omega` form from M19-091/160 and the simple exponents

\[
\nabla\Omega\in L^3,
\qquad
W\in L^6,
\qquad
\nabla W\in L^2,
\]

we obtain

\[
\boxed{
|C_{nl}|
\le
C\|\nabla\Omega\|_3 Z.
}
\]

Thus

\[
\boxed{
\mathcal C_U[W]
\le
\frac{\nu}{8}P
+
B_3(s)Z,
}
\]

with

\[
\boxed{
B_3(s)
:=
C\nu^{-1}\|S_U(s)\|_3^2
+
C\|\nabla\Omega(s)\|_3.
}
\]

## 4. Mean derivative ratio

For a complete bounded hard mode, average the exact energy identity. The time derivative disappears in the Cesaro mean:

\[
\nu\langle P\rangle
+
\frac14\langle Z\rangle
=
\langle\mathcal C_U[W]\rangle.
\]

Using the preceding upper bound,

\[
\nu\langle P\rangle
+
\frac14\langle Z\rangle
\le
\frac\nu8\langle P\rangle
+
B_+\langle Z\rangle,
\]

where

\[
B_+
:=
\sup_sB_3(s).
\]

Therefore

\[
\frac{7\nu}{8}\langle P\rangle
\le
\left(
B_+-\frac14
\right)_+
\langle Z\rangle.
\]

Hence one may take

\[
\boxed{
\Lambda_P^+
\le
\frac{8}{7\nu}
\left(
B_+-\frac14
\right)_+
}
\]

or the coarser always-positive bound

\[
\boxed{
\Lambda_P^+
\lesssim
\nu^{-1}B_+.
}
\]

Thus `Lambda_P^+` is not an independent hard-bundle constant.

It descends to background `L3` strain and vorticity-gradient norms.

## 5. M_{5/2} from background Z and P

For a divergence-free whole-space background,

\[
\|\nabla U\|_2
\simeq
\|\Omega\|_2.
\]

Also

\[
\|\nabla U\|_6
\lesssim
\|\nabla^2U\|_2
\lesssim
\|\nabla\Omega\|_2.
\]

Let

\[
Z_{bg}:=\|\Omega\|_2^2,
\qquad
P_{bg}:=\|\nabla\Omega\|_2^2.
\]

Interpolate from `L2` to `L6` at `p=5/2`. The interpolation parameter is

\[
\theta=\frac3{10}.
\]

Therefore

\[
\boxed{
\|S_U\|_{5/2}
\lesssim
Z_{bg}^{7/20}
P_{bg}^{3/20}.
}
\]

Hence if the retained compact recurrent corridor has

\[
Z_{bg}\le Z_+,
\qquad
P_{bg}\le P_+,
\]

then

\[
\boxed{
M_{5/2}
\lesssim
Z_+^{7/20}P_+^{3/20}.
}
\]

Thus `M_{5/2}` descends to existing background enstrophy/palinstrophy bounds.

## 6. M_3 quantities

Similarly,

\[
\|S_U\|_3
\lesssim
Z_{bg}^{1/4}P_{bg}^{1/4},
\]

so

\[
\boxed{
M_{S,3}^2
\lesssim
Z_+^{1/2}P_+^{1/2}.
}
\]

For

\[
\|\nabla\Omega\|_3,
\]

interpolate between

\[
\nabla\Omega\in L^2
\]

and

\[
\nabla\Omega\in L^6
\]

using

\[
H_{bg}:=\|D^2\Omega\|_2^2.
\]

Then

\[
\boxed{
\|\nabla\Omega\|_3
\lesssim
P_{bg}^{1/4}H_{bg}^{1/4}.
}
\]

Hence

\[
\boxed{
M_{\nabla\Omega,3}
\lesssim
P_+^{1/4}H_+^{1/4}
}
\]

when a uniform compact-corridor `H_+` is retained.

Thus the hard derivative ceiling descends schematically to

\[
\boxed{
\Lambda_P^+
\lesssim
\nu^{-2}Z_+^{1/2}P_+^{1/2}
+
\nu^{-1}P_+^{1/4}H_+^{1/4}.
}
\]

## 7. M_a for 2 <= a < 3

For

\[
2\le a<3,
\]

interpolate `grad Omega` between `L2` and `L6`.

Let

\[
\frac1a
=
\frac{1-\theta_a}{2}
+
\frac{\theta_a}{6}.
\]

Then

\[
\boxed{
M_a
\lesssim
P_+^{(1-\theta_a)/2}
H_+^{\theta_a/2}.
}
\]

This range is therefore controlled by the existing compact smooth `P/H` package.

## 8. M_a in the optimized range 3/2 < a < 2

The best collective exponent in M19-172 prefers `a` near `3/2`, below the direct `L2` interpolation range.

Use a core/tail split at a fixed spectator radius `R`.

### Core

On `B_R`, finite volume gives

\[
\|\nabla\Omega\|_{L^a(B_R)}
\le
|B_R|^{1/a-1/2}
\|\nabla\Omega\|_2
\lesssim
R^{3(1/a-1/2)}P_+^{1/2}.
\]

### Tail

The critical spectator expansion gives

\[
|\nabla\Omega(y)|
\le
C_{tail}r^{-3}
\]

for `r>=R`.

Hence

\[
\int_{r>R}
|\nabla\Omega|^a
\lesssim
C_{tail}^a
\int_R^\infty
r^{2-3a}dr.
\]

For `a>1`,

\[
\boxed{
\|\nabla\Omega\|_{L^a(r>R)}^a
\lesssim
\frac{C_{tail}^a}{3a-3}
R^{3-3a}.
}
\]

Thus

\[
\boxed{
M_a
\lesssim
R^{3(1/a-1/2)}P_+^{1/2}
+
C_{tail}(3a-3)^{-1/a}R^{3/a-3}.
}
\]

Therefore the near-`3/2` optimized `M_a` is also reducible to existing compact-core palinstrophy and explicit tail-amplitude data.

## 9. Which constants remain genuinely nonconstructive

After these reductions, the main solution-dependent quantities are

\[
Z_+,
\quad
P_+,
\quad
H_+,
\quad
C_{tail},
\]

plus the mean-to-instantaneous hard-frame occupation/distortion constant

\[
\boxed{\kappa_{occ}.}
\]

The first four belong to the already retained smooth compact background/tail package, although the repository generally proves their **existence as finite bounds**, not sharp numerical values.

`kappa_occ` is different: it measures how concentrated an average-normalized hard direction can become instantaneously in the vorticity observation metric.

Current compactness proves

\[
\kappa_{occ}<\infty
\]

on a nondegenerate stratum, but no sharp analytic formula has yet been derived from `Z_+,P_+,H_+,C_tail`.

Thus

\[
\boxed{
\kappa_{occ}
\text{ is the cleanest genuinely new quantitative constant in the }N=2\text{ test}.
}
\]

## 10. Why qualitative compactness is insufficient for the two-mode inequality

The desired criterion is strict:

\[
\widetilde C_{str}2^{-2/5}
+
\widetilde C_a2^{d(a)-1}
<
\frac14.
\]

Knowing only that every factor is finite cannot establish it.

Therefore the aperiodic closure has reached a genuinely quantitative stage:

\[
\boxed{
\text{finite corridor constants}
\neq
\text{constants small enough for }N<2.
}
\]

## 11. Audit verdict

### Reduced to existing resource package

\[
\boxed{
\Lambda_P^+,
\quad
M_{5/2},
\quad
M_a
}
\]

can be bounded in terms of

\[
Z_+,P_+,H_+,C_{tail},\nu
\]

and universal harmonic-analysis constants.

### Main new quantitative obstruction

\[
\boxed{\kappa_{occ}}
\]

remains only qualitatively controlled by compact hard-bundle arguments.

### Still not numeric

Even `Z_+,P_+,H_+,C_tail` are currently mostly symbolic corridor bounds rather than sharp universal numbers.

## 12. Next target

M19-178 should attack `kappa_occ` directly.

A possible route is to use the one-sided differential inequality for the instantaneous hard-vorticity mass

\[
Z_v(s)=\|\eta_v(s)\|_2^2
\]

and recurrence/mean normalization to control how high and how narrow a vorticity burst can be.

If one can prove a uniform anti-spike estimate

\[
\boxed{
\sup_s Z_v(s)
\le
C_{spike}
\langle Z_v\rangle
}
\]

for every mean-normalized hard vector, then `kappa_occ` becomes explicit in terms of `C_spike` and the existing background norms.
