# DSD M17-380 — Dyadic coefficient scales satisfy a partition-free Carleson-type flux packing inequality controlled by critical mass and raw-`H2`

Date: 2026-09-08  
Canonical ID: **M17-380**

Status: **ACTIVE MULTISCALE FLUX-PACKING INEQUALITY / CROSS-SCALE BRIDGE**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Dyadic negative-coefficient bins at one snapshot

Let

\[
q:=\kappa_-.
\]

Choose dyadic intrinsic coefficient scales

\[
s_m=2^m r_0.
\]

Define disjoint negative-coefficient bins

\[
\mathcal A_m
:=
\left\{
 c_0s_m^{-2}\le q<C_0s_m^{-2}
\right\}
\]

with constants chosen so the bins have uniformly bounded overlap; after a finite coloring they may be taken disjoint.

On each bin retain the regular vortex-line portion whose line segment inside the bin has arclength at least

\[
\ell_m\ge c_\ell s_m.
\]

Let `Phi_m` be the total positively oriented vorticity flux of that retained family.

## 2. Scale-wise M17-370 inequality

Define

\[
M_m
:=
\int_{\mathcal A_m}q^{3/2}dy,
\]

and

\[
H_m
:=
\int_{\mathcal A_m}|\Delta W|^2dy.
\]

M17-370 gives uniformly in `m`

\[
\boxed{
\Phi_m
\lesssim
s_m^{5/2}(M_mH_m)^{1/2}.
}
\]

Equivalently,

\[
\boxed{
s_m^{-5/2}\Phi_m
\lesssim
(M_mH_m)^{1/2}.
}
\]

## 3. Sum across coefficient scales

Because the coefficient bins are disjoint up to fixed overlap,

\[
\sum_mM_m
\le C M,
\]

where

\[
M:=\int_{\cup_m\mathcal A_m}q^{3/2}dy,
\]

and likewise

\[
\sum_mH_m
\le C H,
\]

with

\[
H:=\int_{\cup_m\mathcal A_m}|\Delta W|^2dy.
\]

Summing the scale-wise inequality and applying Cauchy--Schwarz in `m`,

\[
\begin{aligned}
\sum_m s_m^{-5/2}\Phi_m
&\lesssim
\sum_m(M_mH_m)^{1/2}\\
&\le
\left(\sum_mM_m\right)^{1/2}
\left(\sum_mH_m\right)^{1/2}.
\end{aligned}
\]

Therefore

\[
\boxed{
\sum_m s_m^{-5/2}\Phi_m
\lesssim
(MH)^{1/2}.
}
\]

This is the main multiscale packing inequality.

## 4. Interpretation

The weight `s^{-5/2}` is exactly the scale exponent found in M17-370.

Thus a compact snapshot cannot carry fixed positive material flux on many increasingly small critical-coefficient scales while both

\[
M=\int\kappa_-^{3/2}
\]

and

\[
H=\int|\Delta W|^2
\]

remain bounded.

For example, if

\[
\Phi_m\ge\phi_*>0
\]

on a sequence `s_m -> 0`, then

\[
\sum_m s_m^{-5/2}\Phi_m=\infty,
\]

forcing

\[
M=\infty
\quad\text{or}\quad
H=\infty.
\]

This is a simultaneous-scale statement and is independent of how any individual flux band is subdivided.

## 5. Instantaneous negative flux-decay rate

The total negative contribution to the material-flux derivative is

\[
\mathcal D_\Phi^-
:=
\int q\,d\Phi.
\]

On bin `m`,

\[
q\asymp s_m^{-2},
\]

so

\[
\mathcal D_\Phi^-
\lesssim
\sum_m s_m^{-2}\Phi_m.
\]

Write

\[
s_m^{-2}=s_m^{1/2}s_m^{-5/2}.
\]

If all active coefficient scales lie below a fixed outer intrinsic scale

\[
s_m\le S_*,
\]

then

\[
\boxed{
\mathcal D_\Phi^-
\lesssim
S_*^{1/2}(MH)^{1/2}.
}
\]

Thus the instantaneous rate at which negative coefficient phases can remove positively oriented material flux is controlled by a product of the critical coefficient mass and raw-`H2` charge.

## 6. Relation to the M17-379 exposure cascade

M17-379 showed that logarithmic flux evacuation may be distributed over logarithmically many coefficient scales rather than one long own-scale residence.

The present result shows that at any **single snapshot** those scales cannot carry arbitrary flux independently:

\[
\boxed{
\{\Phi_m\}_m
\text{ obeys a weighted }\ell^1\text{ packing law}.
}
\]

Therefore a multi-scale temporal evacuation cascade must continually move/reallocate its flux among scales or pay growth in `M` or `H`.

## 7. Why this still does not close M17-298

The estimate is instantaneous.

To turn

\[
\mathcal D_\Phi^-
\lesssim(MH)^{1/2}
\]

into a contradiction over a long time one would need a suitable spacetime control of the right-hand side.

The critical mass `M` may be uniformly bounded on the compact branch, but no certified finite cross-generation spacetime ledger for the raw vorticity `H2` quantity `H` is presently available.

That missing temporal/cross-generation allocation is precisely analogous to the unresolved M17-298 raw-`H2` allocation barrier.

Thus the present module provides a **direct mathematical bridge to the same bottleneck**, not a solution of it.

## 8. DSD-theory role

The useful heuristic is to replace a count of many scales by an additive invariant over disjoint coefficient bins. The proof itself is only M17-370 plus Cauchy--Schwarz and disjointness of dyadic level sets.

## 9. Audit verdict

**PASS.**

The new partition-free multiscale constraint is

\[
\boxed{
\sum_m s_m^{-5/2}\Phi_m
\lesssim
\left(
\int\kappa_-^{3/2}dy
\int|\Delta W|^2dy
\right)^{1/2}.
}
\]

The remaining obstruction is temporal/cross-generation raw-`H2` allocation, not tube fragmentation or scale counting.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]