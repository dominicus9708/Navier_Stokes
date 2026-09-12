# DSD M19-088 — Vorticity Duhamel splitting gives a quasi-compactness route with negative essential growth bound

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / CORE-TAIL OPERATOR SPLITTING / NEGATIVE BARE ESSENTIAL GROWTH / LOCAL PARABOLIC COMPACTNESS + SMALL FAR-FIELD PERTURBATION / QUASI-COMPACTNESS REDUCTION / ONE FUNCTIONAL-ANALYTIC DOMAIN BOOKKEEPING OBLIGATION REMAINS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M19-087

For linearized vorticity `eta=curl W`,

\[
\partial_\theta\eta
=\mathcal L_0\eta+\mathcal B_U(\theta)\eta,
\]

where the bare similarity-vorticity operator is

\[
\boxed{
\mathcal L_0
=\nu\Delta-1-\frac12 y\cdot\nabla,
}
\]

and `B_U` contains background transport/stretching and the Biot--Savart realization of `W` from `eta`.

M19-087 gives

\[
\boxed{
\|e^{T\mathcal L_0}\|_{L^2\to L^2}
\le e^{-T/4}.
}
\]

The quarter-gap is pressure-free.

---

## 2. Structure of the background perturbation

Schematically,

\[
\mathcal B_U\eta
=-(U\cdot\nabla)\eta
+(\eta\cdot\nabla)U
+(\Omega\cdot\nabla)W
-(W\cdot\nabla)\Omega,
\]

where

\[
W=\mathcal K_{BS}\eta
\]

is recovered from vorticity by the whole-space Biot--Savart operator.

On the controlled weak-critical spectator branch,

\[
|U|\lesssim r^{-1},
\qquad
|\nabla U|+|\Omega|\lesssim r^{-2},
\qquad
|\nabla\Omega|\lesssim r^{-3}.
\]

---

## 3. Core-tail decomposition

Let `chi_R` be a smooth cutoff equal to one on `|y|<=R` and supported in `|y|<=2R`.

Split

\[
\boxed{
\mathcal B_U
=\mathcal B_{core,R}
+\mathcal B_{tail,R}.
}
\]

The core operator contains all coefficients multiplied by `chi_R`; the tail contains `(1-chi_R)`.

For fixed `R`, the coefficients in `B_core,R` are smooth and supported in a bounded region.

For large `R`, the tail coefficients obey

\[
\|U\|_{L^\infty(|y|>R)}\lesssim R^{-1},
\]

\[
\|\nabla U\|_\infty+\|\Omega\|_\infty\lesssim R^{-2},
\]

and

\[
\|\nabla\Omega\|_{L^3(|y|>R)}\to0.
\]

---

## 4. Tail perturbation is small in the energy form

The stretching term satisfies

\[
\left|\int_{|y|>R}\eta\cdot S_U\eta\right|
\lesssim R^{-2}\|\eta\|_2^2.
\]

The `Omega grad W` term satisfies, using the `L^2` boundedness of Riesz transforms,

\[
\left|\int_{|y|>R}\eta\cdot(\Omega\cdot\nabla)W\right|
\lesssim R^{-2}\|\eta\|_2^2.
\]

For the `W grad Omega` term,

\[
\|W\|_6\lesssim\|\eta\|_2
\]

and

\[
\|\nabla\Omega\|_{L^3(|y|>R)}\to0,
\]

so

\[
\left|\int_{|y|>R}\eta\cdot(W\cdot\nabla)\Omega\right|
\le o_R(1)\|\eta\|_2^2.
\]

The transport term `U dot grad eta` is skew in the unweighted global energy, but after operator localization its commutator errors are of relative size `O(R^-1)` and can be absorbed into a small fraction of the viscous form plus `o_R(1)||eta||_2^2`.

Hence, in quadratic-form language,

\[
\boxed{
|\langle\eta,\mathcal B_{tail,R}\eta\rangle|
\le
\varepsilon_R\nu\|\nabla\eta\|_2^2
+\varepsilon_R\|\eta\|_2^2,
\qquad
\varepsilon_R\to0.
}
\]

---

## 5. Core contribution becomes compact after positive time

Fix `T>0`.

The Duhamel formula is

\[
\mathcal U(\theta+T,\theta)
=e^{T\mathcal L_0}
+\int_0^T
 e^{(T-s)\mathcal L_0}
 \mathcal B_U(\theta+s)
 \mathcal U(\theta+s,\theta)
\,ds.
\]

Insert the core-tail split.

For the core term, once `T-s>0`, the parabolic semigroup gives local smoothing. Since the coefficient support is bounded, the map passes through a bounded-domain Sobolev space and then the compact embedding

\[
H^1(B_{2R})\Subset L^2(B_{2R}).
\]

Thus, after separating an arbitrarily short terminal subinterval if necessary,

\[
\boxed{
\mathcal K_{R,T}(\theta)
:=
\int_0^T
 e^{(T-s)\mathcal L_0}
 \mathcal B_{core,R}(\theta+s)
 \mathcal U(\theta+s,\theta)ds
}
\]

is compact on the retained enstrophy phase space, provided the standard uniform parabolic-domain bounds used throughout the smooth ancient corridor are imposed.

This is the remaining functional-analytic bookkeeping point that must be written in a fully theorem-ready proof.

---

## 6. Essential norm estimate

The remaining tail-Duhamel term is a small perturbation of the bare semigroup.

Thus for fixed `T` and sufficiently large `R`,

\[
\boxed{
\mathcal U(\theta+T,\theta)
=e^{T\mathcal L_0}
+\mathcal K_{R,T}(\theta)
+\mathcal E_{R,T}(\theta),
}
\]

with

\[
\mathcal K_{R,T}(\theta)\quad\text{compact}
\]

and

\[
\|\mathcal E_{R,T}(\theta)\|
\le \delta_R(T),
\qquad
\delta_R(T)\to0
\]

uniformly on the controlled recurrent hull.

Therefore the essential norm satisfies

\[
\boxed{
\|\mathcal U(\theta+T,\theta)\|_{ess}
\le
 e^{-T/4}+\delta_R(T).
}
\]

Choosing first `T>0` and then `R` sufficiently large gives an essential contraction strictly below one.

Equivalently, the essential Lyapunov growth bound is strictly negative:

\[
\boxed{
\lambda_{ess}<0.
}
\]

This is a quasi-compactness statement, conditional only on completing the standard domain/compactness bookkeeping described above.

---

## 7. Consequence for the center spectrum

For a quasi-compact linear cocycle, Lyapunov exponents at or above the essential growth bound occur with finite multiplicity.

Hence if

\[
\lambda_{ess}<0,
\]

then the zero/nonnegative Oseledets bundle is finite-dimensional:

\[
\boxed{
\dim E^{\ge0}(Y)<\infty.
}
\]

In particular,

\[
\boxed{
\dim E^c(Y)<\infty.
}
\]

This is precisely the interior realizability effect that was missing in M19-068--086.

The formal scattering linearization remains infinite-dimensional at infinity, but only a finite-dimensional part can be realized by complete zero-growth interior perturbations if the quasi-compactness bookkeeping is fully certified.

---

## 8. Relation to exact symmetry modes

M19-075--076 identified the exact symmetry-generated center directions:

\[
\partial_\theta U
\]

plus the rotational tangent space

\[
T_U(SO(3)\cdot U).
\]

Therefore, after quotienting rotations, the live center-rigidity question is no longer

\[
\text{infinite-dimensional formal tail center}
\]

but

\[
\boxed{
\text{finite-dimensional interior center}
\stackrel{?}{=}
\operatorname{span}\{\partial_\theta U\}.
}
\]

This is a major reduction, not a completed rigidity theorem.

---

## 9. New frontier

The next calculation should not return to local tail moments.

It should ask whether an additional finite-dimensional zero exponent beyond exact symmetries can survive the quarter-gap compensation identity.

A useful target is the transverse finite-dimensional center trace:

\[
\boxed{
\operatorname{tr}
\left(
\mathcal L_U\big|_{E^c_{tr}}
\right)
}
\]

or an equivalent exterior-power growth rate after the symmetry directions have been modulated out.

Unlike M19-071, the problem is now finite-dimensional and core-observable, so trace/volume arguments no longer suffer from arbitrary far-field translation of the normalized perturbations.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
