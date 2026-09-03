# DSD M5-661 — Closed rank-one silent fold barriers are excluded by material-volume expansion

Date: 2026-09-03

Status: **INTERNAL TOPOLOGICAL/MATERIAL CLOSURE OF THE CLOSED-FOLD SUBBRANCH / ON A HIGH-AMPLITUDE RANK-ONE SILENT KAPPA FOLD, `W` IS NONZERO AND TANGENT TO THE FOLD WHILE M5-660 SHOWS THE FOLD MOVES WITH MATERIAL NORMAL VELOCITY / A CLOSED EMBEDDED FOLD COMPONENT THEREFORE CARRIES A NOWHERE-ZERO TANGENT VECTOR FIELD (HENCE IS TOROIDAL IF CONNECTED AND ORIENTABLE) AND BOUNDS A MATERIAL VOLUME / BECAUSE `div B=3/2`, THAT ENCLOSED VOLUME GROWS EXACTLY AS `exp(3 theta/2)`, SO A CLOSED RANK-ONE SILENT BARRIER CANNOT REMAIN IN A FIXED BOUNDED RECURRENT SIMILARITY CORE FOR ALL FUTURE TIME / THE SILENT SURVIVOR MUST EITHER REACH THE HIGH-AMPLITUDE COMPONENT BOUNDARY OR PASS THROUGH HIGHER KAPPA-CRITICAL DEGENERACY/TOPOLOGY-CHANGE EVENTS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Geometry inherited from M5-659--660

On a rank-one silent fold,

\[
\rho>a_0,
\qquad
\nabla\kappa=0,
\qquad
\nabla h=0,
\]

and

\[
\nabla^2\kappa
=
\lambda n\otimes n,
\qquad
\lambda\ne0.
\]

M5-659 gives

\[
W\cdot n=0,
\]

and M5-660 gives

\[
V_\Sigma\cdot n=B\cdot n.
\]

Thus the fold is tangent to the vorticity field and moves with material normal velocity.

---

## 2. A closed high-amplitude fold has no vorticity zeros

Because

\[
\rho=|W|>a_0>0
\]

on the high-amplitude fold,

\[
\boxed{W|_\Sigma\ne0.}
\]

Since `W` is tangent to `Sigma`, it is a nowhere-vanishing tangent vector field on the fold.

For a connected closed orientable surface embedded in `R^3`, Poincare-Hopf therefore requires

\[
\chi(\Sigma)=0.
\]

Hence a connected closed fold component must have genus one:

\[
\boxed{\Sigma\simeq\mathbb T^2.}
\]

This torus conclusion is descriptive; the volume argument below is the actual obstruction.

---

## 3. Closed material-normal barrier bounds a material region

Let `Sigma(theta)` be a closed embedded silent fold component and let `Omega(theta)` denote its bounded interior.

Since the normal velocity of `Sigma` equals the normal component of `B`, no material trajectory crosses the boundary in the normal direction.

Tangential reparametrization of the boundary does not change the enclosed set.

Therefore `Omega(theta)` is transported as a material region for the similarity material velocity `B`.

---

## 4. Exact volume law

The similarity material velocity satisfies

\[
\boxed{\nabla\cdot B=\frac32.}
\]

Hence Reynolds transport gives

\[
\frac d{d\theta}|\Omega(\theta)|
=
\int_{\Omega(\theta)}\nabla\cdot B\,dy
=
\frac32|\Omega(\theta)|.
\]

Thus

\[
\boxed{
|\Omega(\theta)|
=
|\Omega(\theta_0)|
\exp\left[\frac32(\theta-\theta_0)\right].
}
\]

If the enclosed volume is positive at one time, it grows exponentially in forward similarity time.

---

## 5. Contradiction with a bounded recurrent core

The M5-543 finite active core and subsequent localization place every retained persistent high-amplitude structure inside a fixed normalized bounded storage radius.

A closed silent fold that remains a recurrent barrier in this core would therefore enclose a uniformly bounded volume.

But the exact material-volume law forces that volume to grow without bound.

Hence

\[
\boxed{
\text{a positive-volume closed rank-one silent fold cannot persist recurrently in the bounded similarity core.}
}
\]

This is a genuine closure of the closed-fold subbranch.

---

## 6. How a closed fold could cease to be covered by the argument

The argument can fail only if the fold ceases to be a smooth rank-one silent closed barrier.

That requires at least one of:

1. generalized-force rotation/non-silent dynamics;
2. critical-force creation (`grad h !=0`);
3. rank-zero or higher-order kappa-critical degeneracy;
4. topological reconnection/termination through such a degeneracy;
5. departure of the relevant fold segment from the chosen high-amplitude component.

These are not counted as silent closed-fold recurrence.

---

## 7. Boundary-attached survivor

Inside one bounded amplitude component

\[
C_L\subset\{\rho>a_0\},
\]

a rank-one critical surface may intersect the component boundary

\[
\partial C_L\subset\{\rho=a_0\}
\]

instead of forming a closed component entirely inside `C_L`.

Such a surface does not by itself enclose a material volume using only its high-amplitude portion.

Therefore it remains as a genuine branch:

\[
\boxed{
K_{fold}^{boundary-attached}.
}
\]

The full analytic critical surface can continue into lower-amplitude regions outside the retained component.

---

## 8. Higher-degeneracy survivor

If

\[
\operatorname{rank}\nabla^2\kappa=0
\]

or the rank-one fold develops singular strata, the smooth moving-surface argument of M5-660 does not apply directly.

These events form

\[
\boxed{
K_{higher}^{degenerate}.
}

They are the natural locations where silent sheet topology can be created, destroyed, or reconnected.

---

## 9. Updated silent multi-sheet frontier

Combining M5-658--661,

\[
\boxed{
T_{high-amplitude\ cross-sheet}
\Longrightarrow
C_{rot}^{force}
\lor
C_{crit}^{force}
\lor
K_{fold}^{boundary-attached}
\lor
K_{higher}^{degenerate}.
}
\]

The purely closed smooth rank-one silent barrier has been removed.

---

## 10. Next target

The two remaining genuinely silent branches are now geometrically explicit:

1. a rank-one fold that exits the fixed high-amplitude component through `rho=a0`;
2. a higher-order degenerate critical stratum where fold topology changes.

For the first branch, the M5-651--652 amplitude-superlevel boundary deficit is naturally colocated with the fold endpoint.

For the second, analyticity and finite vanishing-order arguments should determine whether topology change requires a fixed higher-jet event.

These should be treated separately rather than by a generic `multi-sheet` label.

---

## 11. Firewall

The volume contradiction applies only to a closed embedded fold component that remains a smooth differential-silent rank-one material-normal barrier.

It does not exclude open/boundary-attached folds or higher-degeneracy topology-change events.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]