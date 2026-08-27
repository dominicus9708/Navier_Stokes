# DSD M5-136 — Age–Radius Fuchsian Reformulation

Date: 2026-08-27

Status: **EXACT CHANGE OF VARIABLES / THE COMPLETE W1 LERAY SPACETIME IS REWRITTEN AS A DEGENERATE BOUNDARY-TO-CORE PDE ON `z=r^-2 > 0` AND GENEALOGICAL COORDINATE `eta=log r-s/2` / THE CANONICAL TAIL IS THE `z=0` BOUNDARY DATA AND THE UNIT-RADIUS RECURRENT CORE IS THE `z=1` SLICE / F AND P1 GATES ARE UNIFIED AS ONE GLOBAL EXTENSION PROBLEM / GLOBAL REGULARITY UNPROVED.**

---

## 1. Exact spacetime coordinates

For

\[
r=|Y|>0,
\qquad
\rho=\log r,
\]

define

\[
\boxed{
z:=r^{-2}=e^{-2\rho},
\qquad
\eta:=\rho-\frac s2.
}
\]

The inverse map is

\[
\boxed{
r=z^{-1/2},
\qquad
s=-\log z-2\eta.
}
\]

Thus

\[
(r,s)\in(0,\infty)\times\mathbb R
\longleftrightarrow
(z,\eta)\in(0,\infty)\times\mathbb R
\]

is one-to-one.

Define

\[
\boxed{
U(Y,s)=r^{-1}H(z,\eta,\theta),
\qquad
P(Y,s)=r^{-2}\Pi(z,\eta,\theta).
}
\]

No asymptotic expansion is assumed here.

---

## 2. Differential operators

At fixed Leray time `s`, radial logarithmic differentiation becomes

\[
\boxed{
D:=\partial_\rho|_s
=\partial_\eta-2z\partial_z.
}
\]

At fixed spatial point,

\[
\partial_s H=-\frac12\partial_\eta H.
\]

For the Leray passive operator

\[
\mathcal L_0
:=
\partial_s+\frac12+\frac12Y\cdot\nabla,
\]

a direct calculation gives

\[
\boxed{
\mathcal L_0U
=-r^{-1}z\,H_z.
}
\]

This is exact.

---

## 3. Divergence-free constraint

Write

\[
H=H_r\theta+H_\tau.
\]

Since

\[
\nabla\cdot U
=
r^{-2}
\left[
DH_r+H_r+\operatorname{div}_{S^2}H_\tau
\right],
\]

incompressibility becomes

\[
\boxed{
(\partial_\eta-2z\partial_z)H_r
+H_r
+\operatorname{div}_{S^2}H_\tau
=0.
}
\]

---

## 4. Laplacian and nonlinear term

Componentwise,

\[
\boxed{
\Delta U
=
r^{-3}
\left[
(D^2-D+\Delta_{S^2})H
\right].
}
\]

The nonlinear term has the form

\[
\boxed{
(U\cdot\nabla)U
=
r^{-3}\mathcal B_D(H),
}
\]

where

\[
\mathcal B_D(H)
:=
H_r(DH-H)
+
(H_\tau\cdot\nabla_{S^2})H.
\]

The pressure gradient is

\[
\boxed{
\nabla P
=
r^{-3}
\left[
\theta(D\Pi-2\Pi)
+\nabla_{S^2}\Pi
\right].
}
\]

---

## 5. Exact Fuchsian Leray system

Use the Leray equation

\[
\partial_sU
-\nu\Delta U
+(U\cdot\nabla)U
+\frac12U
+\frac12Y\cdot\nabla U
+\nabla P
=0.
\]

Since `r^-3 = z r^-1`, dividing the resulting equation by `z r^-1` gives

\[
\boxed{
H_z
=
-\nu(D^2-D+\Delta_{S^2})H
+\mathcal B_D(H)
+\theta(D\Pi-2\Pi)
+\nabla_{S^2}\Pi.
}
\]

Here

\[
D=\partial_\eta-2z\partial_z,
\]

so the equation is a **degenerate Fuchsian PDE in `z`**, not an ordinary first-order evolution: `D^2` contains terms `z H_z` and `z^2H_zz`.

Explicitly,

\[
D^2-D
=
\partial_\eta^2-\partial_\eta
-4z\partial_{\eta z}
+4z^2\partial_{zz}
+6z\partial_z.
\]

The highest `z` derivative therefore degenerates quadratically at `z=0`.

---

## 6. Pressure equation

The pressure Poisson equation becomes

\[
\boxed{
-\left(
D^2-3D+2+\Delta_{S^2}
\right)\Pi
=
\mathcal Q_D[H],
}
\]

where `mathcal Q_D[H]` is the exact scaled quadratic strain source corresponding to

\[
\partial_iU_j\partial_jU_i=r^{-4}\mathcal Q_D[H].
\]

At `z=0`, `D` reduces to `partial_eta`, recovering the M5-133 log-cylinder pressure operator.

---

## 7. The canonical tail is the Fuchsian boundary value

As

\[
z\downarrow0,
\]

we have `r -> infinity` while holding the co-moving genealogical coordinate `eta` fixed.

The canonical-tail construction gives

\[
\boxed{
H(0,\eta,\theta)=\Phi(\eta,\theta).
}
\]

Likewise

\[
\boxed{
\Pi(0,\eta,\theta)=\Psi(\eta,\theta)
}
\]

for the realized leading critical pressure factor.

Thus the entire tail factor is boundary data at the regular-singular face `z=0`.

---

## 8. The recurrent core is an interior slice

At unit normalized radius

\[
r=1,
\qquad z=1,
\]

one has

\[
s=-2\eta.
\]

Therefore

\[
\boxed{
H(1,\eta,\theta)
=
U(\theta,-2\eta).
}
\]

The complete recurrent W1 orbit on the unit sphere is encoded as translation in `eta` of the interior slice `z=1`.

More generally, every fixed `z=z_0` slice is the W1 orbit observed at one fixed normalized radius.

---

## 9. Why M5-135 appears automatically

Expand near the Fuchsian boundary:

\[
H(z,\eta,\theta)
\sim
\Phi(\eta,\theta)
+
\sum_{n\ge1}z^nG_n(\eta,\theta).
\]

Since

\[
r^{-1}z^n=r^{-(1+2n)},
\]

this is exactly the M5-135 subleading hierarchy.

The term `H_z` contributes `nG_n z^{n-1}`, which is the origin of the nonzero `n` divisor in the recursive correction equations.

Thus finite-order nonresonance is the formal Taylor property of the Fuchsian boundary problem.

---

## 10. DSD four-chain audit

### Formation — GREEN

The variables `(z,eta)` are an exact reparameterization of the existing W1 spacetime; no new solution is constructed.

### Axis — GREEN

`z` is inverse squared normalized radius / scale-depth, while `eta` is genealogical age. Their roles are separated instead of mixing physical time and log radius.

### Static aggregation — GREEN

The tail `z=0` and core `z=1` are slices of one field `H`, not independent objects to be summed.

### Dynamics — GREEN

W1 time translation becomes translation of the `eta` coordinate on each fixed `z` slice.

### Cross-audit — GREEN

The transformation reproduces both the canonical-tail conveyor and the finite-order correction hierarchy already audited independently.

---

## 11. Major conceptual reduction

The two previously separate gates

\[
F:\text{ tail-factor realization},
\qquad
P1:\text{ same-tail strong fiber}
\]

are now parts of one boundary-to-interior question:

\[
\boxed{
\text{For a compact recurrent critical boundary state }(\Phi,\Psi)\text{ at }z=0,
\text{ how many global smooth Fuchsian extensions }(H,\Pi)\text{ reach }z=1?
}
\]

Injectivity of the tail factor means uniqueness of this extension within the W1 class.

Noninjective same-tail fibers mean multiple strong-critical extensions of the same Fuchsian boundary data.

---

## 12. New frontier

The far-field asymptotic problem is no longer the right place to seek a finite-order contradiction.

The true problem is the global Fuchsian extension from

\[
z=0
\]

to an order-one interior scale such as

\[
z=1,
\]

subject to

- incompressibility;
- pressure Poisson coupling;
- compact recurrence in `eta`;
- strong `L2 cap L3` quotient control;
- and finite-energy prelimit realizability.

This provides a common coordinate system for the remaining W1 rigidity work.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]