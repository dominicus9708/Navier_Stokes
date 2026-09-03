# DSD M16-026 — Rank-one weighted-harmonic director collapses to a great-circle phase

Date: 2026-09-03
Canonical ID: **M16-026**

Status: **INTERNAL CONSTANT-RANK / WEIGHTED-HARMONIC REDUCTION / THE MATERIAL DIRECTOR FIELD IN CE-H SATISFIES A WEIGHTED HARMONIC-MAP EQUATION. ON ANY CONNECTED ACTIVE OPEN SET WHERE THE FULL DIFFERENTIAL `d xi` HAS RANK ONE, CONSTANT-RANK FACTORIZATION `xi = gamma(psi)` REDUCES THAT VECTOR EQUATION TO TWO SCALAR CONDITIONS: THE IMAGE CURVE `gamma` MUST BE A GEODESIC OF `S^2` (A GREAT CIRCLE), AND THE PHASE `psi` MUST SOLVE `div(rho^2 grad psi)=0`. SPATIAL ANALYTICITY THEN EXTENDS THE FIXED GREAT-CIRCLE PLANE AS A GLOBAL ONE-COMPONENT VORTICITY CONSTRAINT AT THAT TIME. THIS IS A STRONG CLASSIFICATION BUT NOT YET A COMPLETE LIOUVILLE CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Weighted harmonic-director equation

From

\[
\Delta W=\kappa W,
\qquad
W=\rho\xi,
\qquad
|\xi|=1,
\]

take the component perpendicular to `xi`.

The standard decomposition gives

\[
2\nabla\rho\cdot\nabla\xi
+\rho\left(\Delta\xi+|\nabla\xi|^2\xi\right)=0.
\]

Multiplying by `rho`,

\[
\boxed{
\nabla\cdot(\rho^2\nabla\xi)
+\rho^2|\nabla\xi|^2\xi=0.
}
\]

This is the exact CE-H weighted harmonic-director equation.

---

## 2. Full-rank dichotomy

M16-025 used transverse material vectors. For the local analytic classification it is better to consider the full spatial differential

\[
d\xi:T_y\mathbb R^3\to T_\xi S^2.
\]

Since the target tangent space is two-dimensional,

\[
\operatorname{rank}d\xi\in\{0,1,2\}.
\]

Rank zero on an active open set means `xi` is locally constant and belongs to the already audited flat-direction/geometric-depletion branch.

Thus the genuinely nonconstant alternatives are

\[
\boxed{R_2:\operatorname{rank}d\xi=2}
\]

or

\[
\boxed{R_1:\operatorname{rank}d\xi=1.}
\]

The rank-two branch carries a nonzero pullback of the sphere area 2-form, as in M16-025.

We now classify `R_1`.

---

## 3. Constant-rank factorization

On a connected open set where

\[
\operatorname{rank}d\xi=1,
\]

the constant-rank theorem gives a local scalar phase `psi` and a regular curve

\[
\gamma:I\to S^2
\]

such that

\[
\boxed{
\xi(y)=\gamma(\psi(y)).
}
\]

Reparametrize `gamma` by arclength, so

\[
|\gamma'|=1.
\]

Then

\[
\nabla\xi=\gamma'(\psi)\otimes\nabla\psi,
\]

and

\[
|\nabla\xi|^2=|\nabla\psi|^2.
\]

---

## 4. Substitute into the weighted harmonic equation

Compute

\[
\nabla\cdot(\rho^2\nabla\xi)
=
\gamma'\,\nabla\cdot(\rho^2\nabla\psi)
+\rho^2\gamma''|\nabla\psi|^2.
\]

Hence the weighted harmonic-director equation becomes

\[
\boxed{
\gamma'\,\nabla\cdot(\rho^2\nabla\psi)
+\rho^2|\nabla\psi|^2(\gamma''+\gamma)=0.
}
\]

For a unit-speed curve on the unit sphere,

\[
\gamma''=-\gamma+k_g n_g,
\]

where `k_g` is the geodesic curvature in `S^2` and `n_g` is the in-sphere normal to the curve.

Therefore

\[
\gamma''+\gamma=k_g n_g.
\]

The vectors `gamma'` and `n_g` are orthogonal, so the equation splits into

\[
\boxed{
\nabla\cdot(\rho^2\nabla\psi)=0,
}
\]

and

\[
\boxed{
\rho^2|\nabla\psi|^2k_g=0.
}
\]

On the rank-one active set,

\[
\rho>0,
\qquad
|\nabla\psi|>0.
\]

Hence

\[
\boxed{k_g=0.}
\]

Thus `gamma` is a geodesic of the round sphere: a great circle.

---

## 5. Great-circle form

There exists a fixed unit vector `n` and an orthonormal basis `e_1,e_2` of `n^perp` such that locally

\[
\boxed{
\xi
=\cos\psi\,e_1+\sin\psi\,e_2,
}
\]

with

\[
\boxed{
\nabla\cdot(\rho^2\nabla\psi)=0.
}
\]

In particular,

\[
\boxed{n\cdot\xi=0}
\]

throughout the connected rank-one active open set.

Therefore

\[
\boxed{n\cdot W=0}
\]

there.

---

## 6. Spatial analyticity extension

At a fixed ancient time, `W` is real analytic in space in the retained smooth branch.

The scalar analytic function

\[
y\mapsto n\cdot W(y)
\]

vanishes on a nonempty open set. Hence it vanishes on the connected whole space:

\[
\boxed{n\cdot W\equiv0\quad\text{on }\mathbb R^3}
\]

at that time.

Thus an open rank-one CE-H director patch forces a global one-component vorticity constraint at that time.

If the same material rank-one patch persists on a time interval, the great-circle plane is material-image data and its normal `n` is fixed for that patch; the corresponding global component constraint persists on that interval.

---

## 7. Why ordinary harmonic-map Liouville does not close the branch

For an **unweighted** stationary harmonic map

\[
\xi:\mathbb R^3\to S^2
\]

finite Dirichlet-energy Liouville results are known.

But our equation is

\[
\nabla\cdot(\rho^2\nabla\xi)
+\rho^2|\nabla\xi|^2\xi=0,
\]

with a strongly nonconstant, decaying weight `rho^2` coupled to the Navier--Stokes field itself.

Therefore the ordinary finite-energy harmonic-map Liouville theorem cannot be imported without an additional argument controlling/removing the weight.

Likewise the global constraint `n dot W = 0` is much narrower than the original CE-H class, but it is not by itself identical to a two-dimensional Navier--Stokes solution.

---

## 8. Updated geometric frontier

The same-tube transverse-director survivor has now been refined to

\[
\boxed{
R_2
\ \lor\ 
R_1^{great-circle}.
}
\]

- `R_2`: nonzero material director-area 2-form / rank-two director geometry.
- `R_1^{great-circle}`: vorticity directions lie in a fixed great-circle plane and the phase solves the weighted scalar equation

\[
\nabla\cdot(\rho^2\nabla\psi)=0.
\]

The next audit should use the **full Navier--Stokes coupling**, not an unweighted harmonic-map shortcut:

1. test whether the global one-component vorticity constraint plus CE-H eigenline equations collapses to a lower-dimensional regular class;
2. for `R_2`, combine conserved director-area flux with finite vorticity flux and material cross-section recurrence.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
