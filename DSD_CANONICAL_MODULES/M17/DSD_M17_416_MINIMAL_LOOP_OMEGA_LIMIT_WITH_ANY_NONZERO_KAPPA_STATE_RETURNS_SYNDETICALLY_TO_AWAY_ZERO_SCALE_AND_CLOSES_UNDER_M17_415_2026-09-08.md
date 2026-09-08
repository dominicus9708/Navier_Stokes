# DSD M17-416 — A minimal loop omega-limit with any nonzero `kappa` state returns syndetically to an away-zero coefficient scale and closes under M17-415

Date: 2026-09-08  
Canonical ID: **M17-416**

Status: **ACTIVE MINIMAL-LOOP COEFFICIENT DICHOTOMY / AWAY-ZERO CONDITIONAL CLOSURE / ZERO-LOOP REDUCTION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input

M17-313 gives exact CE-H line constancy

\[
\boxed{D_\xi\kappa=0.}
\]

Hence on every connected regular vortex loop `Gamma`, the coefficient is constant along the loop at fixed time.

Write this scalar loop observable as

\[
\boxed{\kappa_\Gamma(Z).}
\]

M17-415 shows that if the full omega-limit set is minimal and contains one robust M17-413 good loop state, then the original orbit visits the good state set syndetically and the M17-405 raw-`H2` ancestor is contradicted.

The present module asks when a robust away-zero coefficient state exists on a minimal loop omega-limit.

## 2. Continuity of the loop coefficient observable

The M17-360 compact loop-state topology is assumed strong enough for the exact line laws and coefficient fields to pass to limits.

Therefore

\[
Z\mapsto\kappa_\Gamma(Z)
\]

is continuous on the compact omega-limit set.

Assume

\[
\Omega_\omega=\omega(Z)
\]

is minimal.

## 3. Nonzero at one state gives a robust away-zero open set

Suppose there exists

\[
z_*\in\Omega_\omega
\]

such that

\[
\kappa_\Gamma(z_*)\neq0.
\]

Set

\[
\kappa_*:=\frac12|\kappa_\Gamma(z_*)|>0.
\]

By continuity there exists a nonempty relative open neighborhood `U_kappa` of `z_*` such that

\[
\boxed{
|\kappa_\Gamma(z)|\ge\kappa_*
\qquad(z\in U_\kappa).
}
\]

Compactness also gives a finite upper coefficient bound

\[
|\kappa_\Gamma|\le K_*.
\]

Thus `U_kappa` is a fixed normalized away-zero coefficient corridor.

## 4. Minimality makes the away-zero visits syndetic

Apply the M17-415 compact minimality argument to `U_kappa`.

There exists a uniform return-gap bound and, after shrinking to a compactly contained open subset, a uniform positive dwell time.

Hence the original orbit, provided its entire omega-limit set is the same minimal set, returns to

\[
\kappa_*\le|\kappa_\Gamma|\le K_*
\]

with positive lower asymptotic time density.

Under the representation-safe parent-to-record dictionary, this is precisely a recurrent intrinsic coefficient-scale population with

\[
r_\kappa\asymp R_m^{-1}
\]

inside the corresponding record cells.

## 5. Add the retained loop geometry

Assume the other M17-413 loop hypotheses remain uniform on the compact branch:

- positive retained flux;
- parent-scale loop length;
- tubular reach/bounded-overlap segmentation;
- no amplitude/nodal/interface/rank/domain loss;
- record genealogy compatibility.

These are already typed exits if they fail.

Then every visit to `U_kappa` is a robust M17-413 good state.

M17-415 therefore gives nonsummable record occupancy

\[
\sum_m\alpha_m=\infty.
\]

M17-414 then forces divergence of the M17-405 ancestral raw-`H2` ledger, a contradiction.

## 6. Minimal-loop coefficient dichotomy

Consequently, on the retained compact geometric branch,

\[
\boxed{
\Omega_\omega\text{ minimal}
+
\exists z:\kappa_\Gamma(z)\neq0
\Longrightarrow
\text{contradiction}.
}
\]

Therefore every surviving minimal-loop omega-limit must satisfy

\[
\boxed{
\kappa_\Gamma(z)=0
\qquad\text{for all }z\in\Omega_\omega,
}
\]

unless one of the explicit geometry/scale/genealogy hypotheses fails.

This is substantially stronger than merely saying the recurrent mean of `kappa` is zero.

M17-360 gave only

\[
\langle\kappa\rangle=0.
\]

M17-416 shows that on the minimal-full-omega-limit branch, **any persistent nonzero coefficient excursion is fatal** under the M17-413 geometry.

## 7. Relation to sign changes

The conclusion does not depend on the sign of `kappa`.

A state with either

\[
\kappa_\Gamma>0
\]

or

\[
\kappa_\Gamma<0
\]

produces a robust away-zero neighborhood.

Thus oscillation between positive and negative coefficient values cannot evade the theorem; minimality would revisit both away-zero regions with bounded gaps.

The only coefficient-valued minimal survivor is the zero loop.

## 8. Revised loop frontier

The compact loop branch now becomes

\[
\boxed{
\begin{aligned}
H_{compact\ closed\ exact\ CEH\ loop}
\Longrightarrow{}&
G_{nonminimal\ omega\text{-}limit}\\
&\lor H_{minimal\ omega\text{-}limit,\ \kappa_\Gamma\equiv0}\\
&\lor G_{tubular\ reach/flux/amplitude/scale\text{-}map/genealogy}\\
&\lor G_{interface/rank/domain}.
\end{aligned}
}
\]

The away-zero minimal loop is no longer an independent survivor under the stated retained geometry.

## 9. Next zero-loop question

If

\[
\kappa_\Gamma\equiv0
\]

on the minimal omega-limit, the logarithmic coefficient coordinate is forbidden by M17-408.

The correct next audit is the transverse zero geometry:

\[
\nabla\kappa\neq0
\]

versus

\[
\nabla\kappa=0
\]

on the loop.

M17-409 suggests that a uniformly regular transverse zero corridor returns to the finite raw-`H2` ledger. The next module tests whether minimality plus nondegenerate transverse zero geometry again forces nonsummable loop occupancy.

## 10. DSD audit

The DSD role is a state-space branch compression:

- recurrent average zero is not the same as identically zero;
- minimality turns any open nonzero-coefficient state into syndetic occupancy;
- the exact ancestry ledger then excludes that occupancy under the retained loop geometry.

All mathematical steps are standard continuity/minimality plus exact CE-H line constancy and M17-405/413--415.

## 11. Audit verdict

**PASS — minimal away-zero loop branch conditionally closed.**

The surviving minimal loop is forced onto the exact coefficient-zero set, or else exits through explicitly named geometry/scale/genealogy failures.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]