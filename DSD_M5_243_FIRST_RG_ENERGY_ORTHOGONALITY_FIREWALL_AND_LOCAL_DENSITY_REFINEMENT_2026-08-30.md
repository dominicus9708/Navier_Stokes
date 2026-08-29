# DSD M5-243 — First-RG Energy Orthogonality Firewall and Local-Density Refinement

Date: 2026-08-30

Parent: `DSD_M5_242_GENERAL_MINIMAL_TAIL_FIRST_RG_ENERGY_CHARGE_AND_ORTHOGONAL_SPLIT_2026-08-30.md`

Status: **ORTHOGONALITY FIREWALL + STRONGER LOCAL REFINEMENT / ONE SCALAR CELL CONDITION `A(T)=0` IS ONLY CODIMENSION ONE AND DOES NOT FORCE THE RESIDUAL INTO A ROTATIONAL OR PROJECTIVE TANGENT / THE FIRST RG ENERGY CORRELATION HAS A CANONICAL LOG-RADIAL DENSITY `a_T(y)` / THE RESIDUAL-ACTIVE HULL CAN BE REFINED INTO A LOCALLY ENERGY-VISIBLE BRANCH OR A GENUINELY POINTWISE-IN-LOG-RADIUS ENERGY-TRANSVERSE BRANCH `a_T(y)=0` / EVEN THE LATTER IS NOT YET ROTATIONAL / GLOBAL REGULARITY UNPROVED.**

---

## 1. Input from M5-242

On the residual-gap branch,

\[
\mathbf F(T)\ge\varepsilon_{glob}>0
\qquad\forall T\in\mathcal T.
\]

M5-242 defines a first RG energy charge on one normalized cell,

\[
\mathfrak A(T)=\langle T,F_T\rangle_{cell}.
\]

The first split was

\[
\mathfrak A\not\equiv0
\quad\lor\quad
\mathfrak A\equiv0.
\]

The second alternative is now audited more carefully.

---

## 2. Scalar orthogonality does not imply symmetry motion

A single condition

\[
\boxed{\langle T,F_T\rangle=0}
\]

places `F_T` in a codimension-one hyperplane relative to `T` in the chosen dual pairing.

The rotational tangent space is at most three dimensional:

\[
\mathscr T_{rot}(T)
=\operatorname{span}\{\mathcal R_1T,\mathcal R_2T,\mathcal R_3T\}.
\]

The dilation tangent adds at most one more direction.

There is no functional-analytic reason for the infinite-dimensional orthogonal hyperplane to equal this finite-dimensional symmetry tangent space.

The finite-dimensional model

\[
T=(1,0,0),\qquad F=(0,1,1)
\]

already shows that orthogonality to the state does not identify a distinguished group tangent.

Hence

\[
\boxed{
\langle T,F_T\rangle=0
\not\Rightarrow
F_T\text{ is rotational/projective/dilation tangent}.
}
\]

This shortcut is RED.

---

## 3. Normalized residual coefficient

Write the critical tail and its stationary residual as

\[
T(r\theta)=r^{-1}\Phi(y,\theta),
\qquad y=\log r,
\]

and

\[
F_T(r\theta)=r^{-3}\mathcal R_T(y,\theta).
\]

The normalized residual profile `mathcal R_T` is bounded in the retained local `H^{-1}`/smooth punctured topology on the compact tail hull.

Under tail dilation, both normalized profiles translate:

\[
\Phi_{D_\tau T}(y,\theta)
=\Phi_T(y-\tau/2,\theta),
\]

\[
\mathcal R_{D_\tau T}(y,\theta)
=\mathcal R_T(y-\tau/2,\theta).
\]

---

## 4. Local first-RG energy density

Define the spherical correlation density

\[
\boxed{
 a_T(y)
 :=
 \left\langle
 \Phi(y,\cdot),
 \mathcal R_T(y,\cdot)
 \right\rangle_{S^2},
}
\]

with the pairing interpreted through the available smooth punctured realization or the corresponding `H^1/H^-1` spherical-cell duality.

This is a scalar function of log radius.

Its covariance is exact:

\[
\boxed{
 a_{D_\tau T}(y)
 =a_T(y-\tau/2).
}
\]

Thus `a_T` is itself a continuous factor observable of the minimal translation hull.

---

## 5. Relation to finite annular energy charges

For a log interval

\[
I=[y_0,y_1],
\]

the physical unweighted pairing obeys

\[
\int_{e^{y_0}<r<e^{y_1}}
T\cdot F_T\,dx
=
\int_{y_0}^{y_1}
e^{-y}a_T(y)\,dy.
\]

After rescaling the annulus to a fixed normalized cell at radius `R=e^{y_0}`, the common `R^{-1}` shell factor is removed and the remaining coefficient is a fixed smooth positive weight applied to a translated segment of `a_T`.

Therefore every first-order renormalized shell-energy charge is a finite-window linear functional of `a_T`.

The single `mathfrak A(T)` in M5-242 corresponds to one such chosen window.

---

## 6. Why one-cell zero is weak

Suppose, schematically for a unit log-window of length `L`,

\[
\mathfrak A(D_{2s}T)
=
\int_s^{s+L}w(y-s)a_T(y)\,dy
=0
\qquad\forall s,
\]

for one fixed positive weight `w`.

This convolution identity does not imply

\[
a_T(y)=0.
\]

For special weights it may allow nonzero periodic zero-mean densities, and in general one convolution kernel may have a nontrivial Fourier null set.

Hence

\[
\boxed{
\mathfrak A\equiv0
\not\Rightarrow
a_T\equiv0.
}
\]

This is a second RED shortcut.

---

## 7. Refined first-order fork

Use a countable separating family of compact log windows and smooth positive test weights

\[
\{w_m\}_{m\ge1}
\]

which is dense in the relevant test-function space.

Define the corresponding first-order energy observables

\[
\boxed{
\mathfrak A_m(T)
:=
\int w_m(y)a_T(y)\,dy.
}
\]

There are now two exact possibilities.

### E-local: locally energy-visible residual

For some `m`,

\[
\mathfrak A_m
\not\equiv0
\quad\text{on }\mathcal T.
\]

Then continuity and minimal recurrence give a positive-density family of phases on which

\[
\boxed{
|\mathfrak A_m(T)|\ge a_m^*>0.
}
\]

Thus the first RG residual is visible in a fixed localized renormalized-energy observable.

### E-trans: genuinely local energy-transverse residual

For every separating test window,

\[
\mathfrak A_m(T)=0
\qquad\forall T\in\mathcal T.
\]

Density of the tests then gives

\[
\boxed{
 a_T(y)=0
\quad\text{for every }y
}
\]

in the distributional/continuous sense retained on the hull.

Equivalently,

\[
\boxed{
\left\langle
\Phi(y),\mathcal R_T(y)
\right\rangle_{S^2}
=0
\quad\forall y.
}
\]

This is the correct strong first-order transverse branch.

---

## 8. Even local energy transversality is not rotationality

At each `y`, the condition

\[
\langle\Phi(y),\mathcal R_T(y)\rangle_{S^2}=0
\]

still defines an infinite-dimensional orthogonal complement in the spherical function space.

The rotational tangent span remains finite dimensional.

Thus even the stronger branch does not imply

\[
\mathcal R_T
\in\mathscr T_{rot}.
\]

A new PDE relation, not energy orthogonality alone, is necessary.

---

## 9. PDE meaning of the transverse condition

Since

\[
\mathcal R_T
=\nu\mathcal L_{cyl}\Phi
-\mathcal B_{cyl}(\Phi,\Phi)
-\nabla_{cyl}\Pi
\]

schematically, the transverse condition becomes a local spherical balance

\[
\boxed{
\left\langle
\Phi,
\nu\mathcal L_{cyl}\Phi
-\mathcal B_{cyl}(\Phi,\Phi)
-\nabla_{cyl}\Pi
\right\rangle_{S^2}
=0
\quad\forall y.
}
\]

This is a nontrivial PDE constraint: at each scale the viscous, nonlinear, pressure, and radial-transfer contributions must cancel in the velocity-energy direction.

The next audit should derive this identity explicitly and determine what positive quantity remains after all exact spherical integrations by parts.

---

## 10. DSD verdict

### CLOSED

- energy-orthogonal residual `=>` rotational tangent;
- one cell charge zero `=>` pointwise/local energy orthogonality.

### REFINED BRANCH

The first RG energy split is now

\[
\boxed{
R_{gap}
\Longrightarrow
E_{local}
\lor
E_{trans},
}
\]

where `E_trans` means

\[
\boxed{
\langle\Phi(y),\mathcal R_T(y)\rangle_{S^2}=0
\quad\forall y,
\qquad
\mathcal R_T\ne0.
}
\]

### NEXT TARGET

Compute the exact spherical/log-cylinder energy identity for `a_T(y)` and test whether `a_T\equiv0` forces a derivative/flux/pressure correlation already covered by the DSD ledgers.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]