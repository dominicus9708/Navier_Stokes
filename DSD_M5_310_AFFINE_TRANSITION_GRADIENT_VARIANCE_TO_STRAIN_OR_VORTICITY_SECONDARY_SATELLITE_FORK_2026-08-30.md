# DSD M5-310 — Affine-Transition Gradient Variance to Strain Mismatch or Secondary Vorticity Satellite Fork

Date: 2026-08-30

Parent: `DSD_M5_309_AFFINE_CAMPANATO_EXCESS_FIRST_BREAK_RADIUS_AND_L_ONE_FIFTH_TRANSITION_GATE_2026-08-30.md`

Status: **AXIS/FORMATION TRANSITION-SHELL SPLIT / THE ORDER-ONE SCALE-INVARIANT GRADIENT VARIANCE FORCED AT THE AFFINE FIRST-BREAK SCALE DECOMPOSES EXACTLY INTO SYMMETRIC-STRAIN MISMATCH AND VORTICITY MISMATCH / A STRAIN-DOMINATED BREAK IS A TYPED AMBIENT/DERIVATIVE H EVENT; A VORTICITY-DOMINATED BREAK FORCES AN ACTIVE REGION WITH VORTICITY STATE SEPARATED FROM THE AFFINE CORE, PRODUCING A SECONDARY-SATELLITE/CLOUD OBJECT AT DISTANCE `O(R_br)` / GLOBAL REGULARITY UNPROVED.**

---

## 1. Transition input from M5-309

On the nonaffine-excess branch there is a radius

\[
R=R_{br}\le C L^{1/5}
\]

and a best divergence-free affine matrix `M_R` such that

\[
\boxed{
R^{-3}
\int_{B_R}
|\nabla U-M_R|^2dy
\ge\delta_*>0.
}
\]

The affine amplitude-drop and affine-direction-turn branches are already separately typed as affine/projective transition modes.

This note treats the gradient-variance branch.

---

## 2. Symmetric/skew decomposition

Write

\[
M_R=S_R+A_R,
\qquad
S_R=\operatorname{sym}M_R,
\qquad
A_R=\operatorname{skew}M_R.
\]

For the actual velocity gradient,

\[
\nabla U=S+A.
\]

Orthogonality of symmetric and skew matrices gives pointwise

\[
\boxed{
|\nabla U-M_R|^2
=|S-S_R|^2+|A-A_R|^2.
}
\]

In three dimensions, with

\[
A v=\frac12\omega\times v,
\]

one has

\[
|A-A_R|_F^2
=\frac12|\omega-\omega_R|^2,
\]

where `omega_R` is the constant vorticity vector associated with `A_R`.

Hence

\[
\boxed{
|\nabla U-M_R|^2
=|S-S_R|^2
+\frac12|\omega-\omega_R|^2.
}
\]

---

## 3. Quantitative fork

Integrating over `B_R`, the transition witness implies at least one of

\[
\boxed{
R^{-3}
\int_{B_R}|S-S_R|^2dy
\ge\frac{\delta_*}{2}
}
\]

or

\[
\boxed{
R^{-3}
\int_{B_R}|\omega-\omega_R|^2dy
\ge\delta_*
}
\]

(up to harmless fixed constants from the `1/2` factor).

Call these respectively:

\[
H_{strain-br}
\quad\text{and}\quad
S_{\omega-br}.
\]

---

## 4. Strain-dominated transition

If

\[
R^{-3}\int|S-S_R|^2\ge c_*>0,
\]

then the affine strain visible in the detached core fails to extend coherently to the transition scale.

This is a scale-invariant symmetric-gradient variance witness.

It is naturally routed to the existing derivative/ambient-strain family:

\[
\boxed{
H_{strain-br}
\to
H_{ambient/derivative}
\lor T_{shape/projective}
}
\]

according to whether the mismatch is magnitude/frequency dominated or mainly a coherent matrix-direction reorganization.

The precise final subrouting still uses the existing transverse-covariance/projective ledgers.

---

## 5. Vorticity-dominated transition

Assume instead

\[
R^{-3}
\int_{B_R}|\omega-\omega_R|^2dy
\ge c_*>0.
\]

Then the set on which the vorticity differs substantially from the affine-core vorticity cannot have vanishing measure at every fixed threshold.

For example, using the point-picked vorticity cap

\[
|\omega|\le C_\omega
\]

on the relevant satellite cylinder, Chebyshev in reverse gives a threshold `eta_*>0` and a set `E_R subset B_R` with

\[
\boxed{
|E_R|\ge c_E R^3
}
\]

and

\[
\boxed{
|\omega(y)-\omega_R|\ge\eta_*
\qquad(y\in E_R)
}
\]

for constants depending only on the variance floor and vorticity cap.

Thus the transition is not a single negligible defect point; it occupies a positive volume fraction in the normalized ball, unless the variance is concentrated into a smaller high-amplitude set, which would itself strengthen the H/point-picking alternative.

---

## 6. Secondary active point

Choose `y_1 in E_R`.

Then the vorticity state at `y_1` differs by a fixed amount from the affine-core vorticity `omega_R`.

If `|omega_R|` is order one, either:

1. `|omega(y_1)|` remains order one but its direction/amplitude differs by `eta_*`; or
2. `|omega(y_1)|` is larger, in which case one may point-pick a still more active natural scale.

In either case the transition shell contains a secondary active vorticity state.

This defines

\[
\boxed{S_{secondary}.}
\]

---

## 7. Spatial separation

The transition radius obeys

\[
R_{br}=O(L^{1/5}).
\]

If `R_br -> infinity`, secondary active states can be selected at distances comparable to a dyadic portion of `R_br` from the original satellite center whenever the variance is genuinely annular rather than concentrated at the center.

This produces a multi-satellite geometry on a scale far smaller than the main-core separation `L`:

\[
\boxed{
1\ll R_{secondary}\lesssim L^{1/5}\ll L.
}
\]

If instead the variance remains concentrated near the original center at bounded radius, then the fixed-radius detached limit was not truly affine there, contradicting the assumed affine-limit branch after choosing the reference radius sufficiently large.

Thus a genuine affine-to-nonaffine transition can be localized away from the fixed affine core.

---

## 8. Formation interpretation

The affine shield cannot end silently.

It must terminate by a change in one of the structural attributes:

\[
\boxed{
\text{strain field}
\quad\lor\quad
\text{vorticity field}.
}
\]

The first is an H/projective object.

The second creates a new active object whose relation to the original satellite must be tracked.

This converts the ancestry problem into an **intermediate-scale interaction problem**.

---

## 9. Relation to the satellite-cloud machinery

The secondary satellite lies at separation at most `O(L^{1/5})` in the original satellite natural units.

Therefore its interaction with the original satellite is much stronger than the interaction of the original satellite with the main core.

The M5-298 local interaction density and M5-294 multipole tensor can now be applied to this secondary structure.

Possible outcomes include:

\[
\boxed{
H_{sat-local}
\lor C_{cancel}
\lor T_{relative/material}
\lor A_{nested-detached}.
}
\]

This is the next recursive frontier.

---

## 10. Firewall: positive variance is not automatically a higher vorticity maximum

The vorticity mismatch may be mainly directional or may reduce the local amplitude relative to `omega_R`.

Therefore one must not claim

\[
S_{\omega-br}
\Rightarrow
|\omega|> |\omega_R|.
\]

The valid conclusion is a fixed state-space separation in vorticity, not necessarily amplitude escalation.

---

## 11. Updated affine ancestry route

Combining M5-309 and M5-310:

\[
\boxed{
\begin{aligned}
A_{affine}
\Longrightarrow{}&
T_{affine-amplitude}\\
&\lor T_{affine-axis}\\
&\lor H_{strain-br}\\
&\lor S_{secondary}.
\end{aligned}
}
\]

All nontrivial transitions occur no later than radius `O(L^{1/5})`.

The exact affine fixed point is therefore replaced, in finite-energy/Morrey ancestry, by a finite-power hierarchy of transition structures.

---

## 12. Audit verdict

### PROVED / EXACT

- symmetric/skew variance decomposition;
- gradient-variance witness forces strain or vorticity variance.

### DERIVED UNDER VORTICITY CAP

- vorticity-variance branch contains a positive-measure state-separated region.

### ROUTED

- strain mismatch -> H/projective;
- vorticity mismatch -> secondary active satellite/cloud structure.

### OPEN

- closure of the secondary-satellite hierarchy;
- dynamic turnover of the transition shell;
- critical `1/R` endpoint;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]