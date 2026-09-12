# DSD M19-095 — Decaying critical-tail coefficients make the linearized-vorticity background a relatively compact perturbation and certify negative essential growth

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / COMPLETES THE M19-088 CORE-DOMAIN COMPACTNESS BOOKKEEPING UNDER THE RETAINED SMOOTH SPECTATOR-TAIL BOUNDS / LINEARIZED VORTICITY COCYCLE IS QUASI-COMPACT WITH ESSENTIAL GROWTH AT MOST THE BARE QUARTER-GAP / ZERO CENTER IS FINITE-DIMENSIONAL / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Objective

M19-088 reduced quasi-compactness to one functional-analytic point: prove that the background part of the linearized vorticity evolution is compact relative to the bare similarity-vorticity generator once the controlled critical-tail coefficient decay is imposed.

This module records that bookkeeping explicitly.

---

## 2. Phase space and bare generator

Work on the divergence-free vorticity Hilbert space

\[
\mathcal H_\omega=L^2_\sigma(\mathbb R^3).
\]

The bare generator is

\[
\boxed{
\mathcal L_0
=\nu\Delta-1-\frac12y\cdot\nabla.
}
\]

Its natural graph domain contains the required local `H2` regularity and the drift term `y dot grad eta` in `L2`.

The energy identity gives

\[
\boxed{
\|e^{T\mathcal L_0}\|_{\mathcal H_\omega\to\mathcal H_\omega}
\le e^{-T/4}.
}
\]

---

## 3. Linearized background operator

For `eta=curl W`, write

\[
\boxed{
\mathcal B_U\eta
=-(U\cdot\nabla)\eta
+(\eta\cdot\nabla)U
+(\Omega\cdot\nabla)W
-(W\cdot\nabla)\Omega,
}
\]

with

\[
W=\mathcal K_{BS}\eta.
\]

On the retained smooth weak-critical spectator corridor,

\[
|U(y)|\lesssim\langle y\rangle^{-1},
\]

\[
|\nabla U(y)|+|\Omega(y)|\lesssim\langle y\rangle^{-2},
\]

and

\[
|\nabla\Omega(y)|\lesssim\langle y\rangle^{-3},
\]

uniformly on the recurrent hull, together with the local smooth bounds already used in M5-563/M5-567.

---

## 4. Compactness of the transport multiplication

Consider first

\[
\eta\mapsto U\cdot\nabla\eta.
\]

Take a sequence bounded in the graph norm of `L0`.

On every fixed ball, graph-norm boundedness gives local `H2` control, hence `grad eta` is precompact in local `L2` by Rellich.

Outside a large ball,

\[
\|U\|_\infty\lesssim R^{-1}.
\]

Thus the exterior part is uniformly small.

Therefore

\[
\boxed{
\eta\mapsto U\cdot\nabla\eta
}
\]

is compact from `D(L0)` with graph norm into `L2`.

---

## 5. Compactness of the strain multiplication

For

\[
\eta\mapsto(\eta\cdot\nabla)U,
\]

the coefficient `grad U` is bounded locally and tends to zero as `r^-2`.

Local Rellich compactness plus exterior coefficient smallness yields

\[
\boxed{
\eta\mapsto(\eta\cdot\nabla)U
:
D(\mathcal L_0)\to L^2
\quad\text{compact}.
}
\]

---

## 6. Biot--Savart terms

The Riesz-transform identity gives

\[
\|\nabla W\|_2\lesssim\|\eta\|_2,
\qquad
\|W\|_6\lesssim\|\eta\|_2.
\]

For

\[
(\Omega\cdot\nabla)W,
\]

the multiplier `Omega` is locally smooth and vanishes as `r^-2`.

On the graph domain, local regularity of `eta` transfers through Biot--Savart to higher local regularity of `W`, while the exterior multiplier is uniformly small.

Hence this term is relatively compact.

For

\[
(W\cdot\nabla)\Omega,
\]

use local regularity and

\[
\|\nabla\Omega\|_{L^3(|y|>R)}\to0.
\]

Since `W in L6`, the exterior `L2` norm of the product tends uniformly to zero.

Thus

\[
\boxed{
\mathcal B_U:
D(\mathcal L_0)\to\mathcal H_\omega
\quad\text{is relatively compact}.
}
\]

The statement is uniform over the retained compact recurrent coefficient family.

---

## 7. Positive-time evolution is a compact perturbation

Let `U(theta,s)` denote the linearized vorticity evolution family.

Duhamel gives

\[
\mathcal U(\theta+T,\theta)
=e^{T\mathcal L_0}
+\int_0^T
 e^{(T-s)\mathcal L_0}
 \mathcal B_{U(\theta+s)}
 \mathcal U(\theta+s,\theta)
 ds.
\]

For every positive time separation, the analytic parabolic semigroup maps into the graph domain.

The relatively compact operator `B_U` then produces a compact `L2` image.

Approximate the time integral by excluding arbitrarily short endpoint subintervals. The middle integral is a norm limit of compact Riemann sums.

The endpoint pieces tend to zero in operator norm using the standard analytic-semigroup smoothing estimates and the relative form bounds already certified in M19-087--088.

Therefore

\[
\boxed{
\mathcal U(\theta+T,\theta)
-e^{T\mathcal L_0}
\quad\text{is compact on }\mathcal H_\omega
}
\]

for every fixed `T>0`, uniformly in the recurrent hull parameter.

---

## 8. Essential growth bound

Compact perturbations do not change the essential norm in the Calkin algebra.

Hence

\[
\boxed{
\|\mathcal U(\theta+T,\theta)\|_{ess}
\le
\|e^{T\mathcal L_0}\|
\le e^{-T/4}.
}
\]

Therefore

\[
\boxed{
\lambda_{ess}\le-\frac14<0.
}
\]

This upgrades the M19-088 quasi-compactness route to a certified result within the retained smooth critical-tail coefficient class.

---

## 9. Finite-dimensional nonnegative spectrum

Standard quasi-compact cocycle consequences now give finite multiplicity for all Lyapunov exponents above the essential bound.

In particular,

\[
\boxed{
\dim E^{\ge0}(Y)<\infty,
\qquad
\dim E^c(Y)<\infty.
}
\]

Thus the infinite-dimensional formal scattering center of M19-068 cannot be fully realized by complete interior zero-growth perturbations.

Only a finite-dimensional interior subbundle survives.

---

## 10. What this resolves and what it does not

Resolved:

\[
\boxed{
\text{formal infinite-dimensional q-center}
\longrightarrow
\text{finite-dimensional interior-realizable center}.
}
\]

Not resolved:

\[
\boxed{
E^c_{extra}=0.
}
\]

The remaining finite-dimensional extra center may still support aperiodic recurrent dynamics.

M19-090--094 identify the exact quarter-gap compensation budget that such a center must pay.

---

## 11. Updated analytic split

The weak-critical calculation now has two genuine live analytic branches:

\[
\boxed{
\mathcal T_{extra-center}:
\text{exclude finite-dimensional symmetry-transverse zero modes}
}
\]

and, after that reduction,

\[
\boxed{
\mathcal T_{DSS}^{critical}:
\text{exclude the exact nonzero log-periodic one-over-r DSS survivor}.
}
\]

These are separate tasks.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
