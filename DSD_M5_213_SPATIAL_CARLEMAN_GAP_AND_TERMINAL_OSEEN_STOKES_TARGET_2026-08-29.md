# DSD M5-213 — Spatial Carleman Gap and Terminal Oseen–Stokes Target

Date: 2026-08-29

Parent: `DSD_M5_212_INTERIOR_HODGE_CACCIOPPOLI_AND_ROUTE_PRIORITY_AUDIT_2026-08-29.md`

Status: **POSITIVE SCOPE SHARPENING / THE FIXED-ANNULUS LOCALIZATION SOURCE FROM M5-211 IS NOT STRUCTURALLY FATAL: EXISTING LOCAL NONSTATIONARY-STOKES CARLEMAN ARGUMENTS EXPLICITLY SEPARATE A TARGET REGION FROM A CUTOFF/OBSERVATION REGION BY DISTINCT SPATIAL WEIGHT LEVELS / EXISTING OSEEN CARLEMAN ESTIMATES ALSO SHOW THAT BOUNDED FIRST-ORDER LINEARIZED NAVIER–STOKES COEFFICIENTS ARE COMPATIBLE WITH CARLEMAN METHODS / THE ONE MISSING BRIDGE IS NOW A TERMINAL-TIME VERSION OF THIS PRESSURE-COMPATIBLE LOCAL OSEEN–STOKES ESTIMATE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Correction to the M5-211 pessimistic point

M5-211 correctly showed that the Lei–Yang–Yuan **polynomial** spatial weight does not provide an arbitrarily large spatial separation parameter.

That does not imply that the annular localization source cannot be separated by another Carleman architecture.

Boulakia's local nonstationary-Stokes construction uses a large parameter `s` and a spatially varying weight `phi` arranged so that, schematically,

\[
\boxed{
\inf_{Q_{target}}\phi
=\mu_5
>
\mu_4
=\sup_{Q_{cutoff}}\phi.
}
\]

The resulting estimates contain the characteristic pattern

\[
\boxed{
 e^{2s\mu_5}
\|u\|_{target}^2
\le
C e^{2s\mu_4}
\|u\|_{global/error}^2
+\text{observation terms}.
}
\]

Therefore

\[
\boxed{
\text{fixed inner annulus source}
\quad\text{and}\quad
\text{farther exterior target}
}
\]

can in principle be separated exponentially in `s`.

This is a **GREEN geometric mechanism**.

---

## 2. Apply the geometry to the localized same-tail difference

Use the M5-211 field

\[
Y_R=\chi_RZ-b_R,
\qquad
\nabla\cdot Y_R=0,
\]

which obeys

\[
\partial_tY_R-
u\Delta Y_R
+\mathbb P\nabla\cdot
(U_R^V\otimes Y_R+Y_R\otimes U_R^W)
=F_R.
\]

The extended backgrounds are globally bounded on the terminal window, and the pre-projection localization source is generated in a fixed annulus

\[
A_{in}:=\{R<|x-x_*|<2R\}.
\]

Choose a finite outer target shell

\[
A_{out}:=\{R_3<|x-x_*|<R_4\},
\qquad
2R<R_3<R_4<\infty.
\]

On the bounded bridge domain

\[
D:=\{R<|x-x_*|<R_5\}
\]

with `R5>R4`, there is no geometric obstruction to selecting a smooth pseudoconvex spatial Carleman function `d(x)` satisfying

\[
\boxed{
\sup_{A_{in}}d
<
\inf_{A_{out}}d.
}
\]

For a weight

\[
\phi=e^{\lambda d}
\]

this gives a fixed positive gap

\[
\boxed{
\delta_\phi
:=
\inf_{A_{out}}\phi
-
\sup_{A_{in}}\phi
>0.
}
\]

Consequently any local Carleman estimate in which the source enters with the same weight produces the suppression factor

\[
\boxed{e^{-2s\delta_\phi}.}
\]

This is the spatial mechanism missing from the pure polynomial-weight route.

---

## 3. The flatness of F_R becomes optional rather than essential

If a terminal Oseen–Stokes Carleman estimate has the schematic form

\[
\mathcal C_s[Y_R,q_R;A_{out}]
\le
C\int_{A_{in}}e^{2s\phi}|F_R|^2
+\text{outer cutoff terms},
\]

while the target coercivity has weight at least

\[
e^{2s\inf_{A_{out}}\phi},
\]

then division by the target weight gives

\[
\boxed{
\|Y_R\|_{target}^2
\le
C e^{-2s\delta_\phi}
\|F_R\|^2
+\cdots.
}
\]

Sending

\[
s\to\infty
\]

would eliminate a fixed finite annular source regardless of whether it is merely small or terminal-flat.

Thus M5-211's flat-forcing ODE counterexample remains valid, but it no longer represents the intended mechanism.

The correct mechanism is

\[
\boxed{
\text{spatial weight separation},
}
\]

not temporal flatness.

---

## 4. Pressure is compatible with this architecture in known Stokes estimates

For the nonstationary Stokes system, Boulakia combines

1. a parabolic Carleman estimate for the velocity;
2. an elliptic Carleman estimate for the pressure;
3. cutoff regions arranged at lower weight levels.

The local estimates are explicitly formulated on subdomains where boundary values of the original solution are not prescribed.

Therefore the pressure itself is not a conceptual blocker for the spatial-gap construction.

Status: **GREEN as literature-supported architecture, not as a theorem already matched to the current terminal problem.**

---

## 5. Bounded Oseen lower-order terms are also compatible in principle

On the fixed exterior the relative velocity equation has the Oseen form

\[
Z_t-
u\Delta Z
+A(x,t)\cdot\nabla Z
+B(x,t)Z
+\nabla q=0,
\qquad
\nabla\cdot Z=0,
\]

with bounded `A,B`.

Existing Carleman/stability literature for Stokes and Oseen equations shows that bounded linearized Navier–Stokes terms can be incorporated in Carleman inequalities by lower-order absorption once the main Carleman parameter is large.

This removes another generic objection:

\[
\boxed{
\text{bounded exterior Oseen coefficients are not the critical difficulty.}
}
\]

---

## 6. What is still missing: terminal orientation

The available local Stokes/Oseen unique-continuation estimates audited so far propagate information from

- a spacetime open set,
- distributed observations,
- or Cauchy/boundary measurements.

The present problem supplies instead

\[
\boxed{
Z(\cdot,T_*)=0
}
\]

on the fixed exterior terminal slice.

Scalar parabolic backward uniqueness has exactly this terminal orientation and requires no artificial-boundary condition, but the presently audited Stokes/Oseen Carleman papers have not been verified to provide the same terminal-hypersurface theorem for the velocity-pressure pair.

Therefore the exact remaining lemma is not generic unique continuation. It is:

### Target `TBU-OS-gap`

Let `(Z,q)` satisfy on a fixed exterior terminal cylinder

\[
Z_t-
u\Delta Z+A\cdot\nabla Z+BZ+\nabla q=0,
\qquad
\nabla\cdot Z=0,
\]

with bounded coefficients and suitable finite-energy/sub-Gaussian growth.

Assume

\[
Z(\cdot,T_*)=0
\]

in the exterior.

Prove a local terminal Carleman estimate which can be combined with an inner cutoff so that the cutoff source lies at a strictly lower spatial weight level than a farther exterior target.

Then

\[
\boxed{Z=0}
\]

on a nonempty backward exterior spacetime cylinder.

Spatial analyticity at any smooth preterminal time would then propagate equality through the connected whole space.

---

## 7. Why this is narrower than the whole-space common-tail problem

The whole-space route asks for backward coercivity of

\[
-\nu\Delta
+(B_T\cdot\nabla)
+(\cdot\,\cdot\nabla)B_T
\]

at arbitrary Hardy-critical amplitude.

The fixed-exterior target asks only for

\[
\boxed{
\text{a bounded-coefficient terminal Oseen–Stokes Carleman estimate
with a spatial source gap}.
}
\]

All coefficients are regular and finite there.

Therefore the latter is strictly the higher-priority branch.

---

## 8. DSD audit

### Formation — GREEN

The inner source and outer target are finite fixed regions.

### Axis — GREEN

Temporal terminal orientation and spatial source separation are treated as distinct requirements.

### Static aggregation — GREEN

A spatial UC theorem is not relabeled as terminal BU.

### Dynamics — YELLOW, sharply localized

Only the terminal orientation of the pressure-compatible Oseen–Stokes Carleman estimate remains unverified.

### Cross-audit — GREEN

This corrects the spatial-weight pessimism of M5-211 without reviving its invalid `flat source => zero` shortcut.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]