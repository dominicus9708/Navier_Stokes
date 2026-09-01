# DSD M5-515 — Ergodic relative-angle dichotomy: rigid dual frame or same-pair ratchet

Date: 2026-09-01

Status: **PAIR-LEVEL COUPLING / M5-514 SELECTS ONE ERGODIC COMPACT COMPONENT CARRYING POSITIVE PRODUCTION, POSITIVE RATCHET ACTIVITY, AND BOUNDED-GAP DUAL REFORMATION / BY FINITENESS ONE PERSISTENT DUAL PAIR HAS POSITIVE EVENT MEASURE / ON THE COHERENT PERSISTENT-LINEAGE CORRIDOR ITS RELATIVE-ANGLE OBSERVABLE `c_ab=xi_a·xi_b` IS A BOUNDED ABSOLUTELY CONTINUOUS FLOW OBSERVABLE WITH EXACT DERIVATIVE FROM M5-491 / ERGODICITY IMPLIES THAT EITHER `c_ab` IS CONSTANT ON THE COMPONENT, IN WHICH CASE THE PAIR HAS A FIXED NONCOLLINEAR ANGLE AND DEFINES A MOVING `SO(3)` FRAME, OR `mean |c_ab'|>0`, WHICH FORCES POSITIVE TRANSVERSE-STRAIN/DIRECTIONAL-DIFFUSION ACTION ON THAT SAME PAIR / THUS THE NONRIGID BRANCH COUPLES DUAL, RATCHET, AND PRODUCTION AT PAIR LEVEL; ONLY THE RIGID MOVING-FRAME BRANCH ESCAPES / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. One common ergodic component

M5-514 selects an ergodic invariant component `mu_*` on the global smooth compact hard core such that

\[
\boxed{
\langle Q\rangle_{\mu_*}>0,
\qquad
\langle a_{rat}\rangle_{\mu_*}>0,
\qquad
\langle d_{dual}\rangle_{\mu_*}\ge\delta_{dual}>0.
}
\]

The persistent lineage family is finite.

Therefore at least one persistent pair

\[
(a,b)
\]

has positive dual-event measure on `mu_*`.

At those dual events there is a fixed noncollinearity threshold

\[
\boxed{
|\xi_a\times\xi_b|
\ge s_0>0.
}
\]

Equivalently,

\[
|\xi_a\cdot\xi_b|
\le
c_0:=\sqrt{1-s_0^2}<1.
\]

---

## 2. Coherent persistent-pair corridor

M5-490--491 track the two persistent material-flux lineages through their direction equations.

On the retained coherent carrier corridor, define

\[
\boxed{
c_{ab}(\theta)
:=
\xi_a(\theta)\cdot\xi_b(\theta).
}
\]

The directions are unit vectors, so

\[
-1\le c_{ab}\le1.
\]

M5-491 gives the exact derivative

\[
\boxed{
\frac{dc_{ab}}{d\theta}
=
R_{strain}^{ab}
+
R_{diff}^{ab},
}
\]

where

\[
R_{strain}^{ab}
=
\tau_a\cdot\xi_b
+
\xi_a\cdot\tau_b,
\]

and

\[
R_{diff}^{ab}
=
\mathcal D_a\cdot\xi_b
+
\xi_a\cdot\mathcal D_b.
\]

Here

\[
\tau_i
=(I-\xi_i\otimes\xi_i)\Sigma_i\xi_i
\]

is transverse strain tilt and

\[
\mathcal D_i
=
\rho_i^{-1}(I-\xi_i\otimes\xi_i)\Delta W_i
\]

is projected directional diffusion along lineage `i`.

If a lineage loses coherent nonzero carrier identity so that its direction cannot be continued, that event is already a reformation/replacement/coherence-loss channel and is outside the quiet coherent-pair subbranch considered below.

---

## 3. Ergodic lemma for a bounded differentiable observable

Let `c` be a bounded absolutely continuous observable along an ergodic flow.

If

\[
\langle|c'|\rangle=0,
\]

then

\[
c'=0
\]

almost everywhere.

Hence `c` is constant along almost every trajectory.

Ergodicity then implies

\[
\boxed{
c=c_*
\quad\mu_*\text{-almost everywhere}.
}
\]

Conversely, if `c` is not almost-everywhere constant, then necessarily

\[
\boxed{
\langle|c'|\rangle>0.
}
\]

Apply this to `c_ab`.

---

## 4. Exact relative-angle dichotomy

We obtain

\[
\boxed{
\text{either}
\quad
c_{ab}\equiv c_*,
\quad
\text{or}
\quad
\langle|c_{ab}'|\rangle_{\mu_*}>0.
}
\]

Because the pair has positive dual-event measure with

\[
|c_{ab}|\le c_0<1,
\]

the constant case must satisfy

\[
\boxed{
|c_*|\le c_0<1.
}
\]

Thus the constant branch is not a collinear pair.

It is a **rigid noncollinear relative-angle pair**.

---

## 5. Nonrigid branch forces same-pair projective action

Suppose

\[
\kappa_{ab}
:=
\langle|c_{ab}'|\rangle_{\mu_*}
>0.
\]

From the exact derivative equation,

\[
|c_{ab}'|
\le
|\tau_a|
+|\tau_b|
+|\mathcal D_a|
+|\mathcal D_b|.
\]

Therefore

\[
\boxed{
\left\langle
|\tau_a|+|\tau_b|+|\mathcal D_a|+|\mathcal D_b|
\right\rangle
\ge
\kappa_{ab}>0.
}
\]

Thus the same persistent pair that realizes the dual-source geometry must carry positive projective control action.

This is stronger than merely knowing that some lineage somewhere on the component carries ratchet activity.

---

## 6. Squared pair-action lower bound

Let

\[
A_{ab}
:=
|\tau_a|+|\tau_b|+|\mathcal D_a|+|\mathcal D_b|.
\]

Since `mu_*` is a probability measure,

\[
\langle A_{ab}^2\rangle
\ge
\langle A_{ab}\rangle^2
\ge
\kappa_{ab}^2.
\]

Also

\[
A_{ab}^2
\le
4\left(
|\tau_a|^2+|\tau_b|^2+|\mathcal D_a|^2+|\mathcal D_b|^2
\right).
\]

Hence

\[
\boxed{
\left\langle
|\tau_a|^2+|\tau_b|^2+|\mathcal D_a|^2+|\mathcal D_b|^2
\right\rangle
\ge
\frac14\kappa_{ab}^2>0.
}
\]

At least one of the four same-pair squared channels has positive mean.

---

## 7. Thickening to local PDE charge

The persistent dual packets have fixed positive carrier amplitude and coherent radius on the retained analytic/smooth corridor.

M5-487 and M5-500 already established the relevant thickening mechanism:

- a positive transverse-strain value on an active carrier thickens to local `rho^2|tau|^2` charge;
- a positive projected-diffusion value thickens to local `|(I-xi tensor xi)Delta W|^2` charge.

Therefore the nonrigid pair branch yields, for some fixed local carrier windows,

\[
\boxed{
\left\langle
\int_{B_a}\rho_a^2|\tau_a|^2
+
\int_{B_b}\rho_b^2|\tau_b|^2
+
\int_{B_a}|(I-\xi_a\otimes\xi_a)\Delta W|^2
+
\int_{B_b}|(I-\xi_b\otimes\xi_b)\Delta W|^2
\right\rangle
>0.
}
\]

Thus dual geometry and ratchet action are coupled on the same material pair.

---

## 8. Production is already on the same component

By M5-499 and M5-514,

\[
\boxed{
\langle Q\rangle_{\mu_*}>0.
}
\]

Hence the nonrigid branch carries on one ergodic component

\[
\boxed{
\text{positive axial production}
+
\text{positive dual-pair activity}
+
\text{positive same-pair transverse/diffusive action}.
}
\]

This is the strongest dual--ratchet--production coupling obtained so far.

It still does not force all three to peak at the same instant.

---

## 9. The rigid branch defines a moving frame

Now suppose

\[
c_{ab}\equiv c_*,
\qquad
|c_*|<1.
\]

The two directions remain noncollinear for the entire coherent trajectory.

Define the orthonormal frame

\[
e_1=\xi_a,
\]

\[
e_2
=
\frac{\xi_b-c_*\xi_a}{\sqrt{1-c_*^2}},
\]

\[
e_3=e_1\times e_2.
\]

Then

\[
R_{ab}(\theta)
=(e_1,e_2,e_3)
\in SO(3).
\]

Since `R_ab` is an orthogonal frame,

\[
\boxed{
\mathcal A_{ab}(\theta)
:=
R_{ab}'R_{ab}^T
\in\mathfrak{so}(3).
}
\]

Thus all pair-direction motion is a common instantaneous rigid rotation of this two-lineage frame.

This does **not** imply that the entire Navier--Stokes velocity field is a rigidly rotated profile.

---

## 10. Rigid-pair firewall

The implication

\[
\boxed{
\text{two persistent directions keep a fixed angle}
\not\Longrightarrow
\text{global RSS/RDSS symmetry of }U
}
\]

is essential.

Other parts of the vorticity/velocity field may deform independently of `R_ab`.

The local frame angular velocity

\[
\mathcal A_{ab}(\theta)
\]

must not be identified with the global rotation parameter `alpha` in RSS/RDSS theorems without a separate rigidity argument.

Thus the Pineau--Vicol rotated-self-similar theorem cannot yet be applied merely from the rigid-pair branch.

---

## 11. Relation to M5-513 topology

M5-513 noted that a continuously noncollinear pair defines an `SO(3)` frame and hence permits path-homotopy information.

M5-515 supplies exactly the condition needed to make that frame global along the coherent pair trajectory in the rigid branch:

\[
|c_*|<1
\quad\text{for all time}.
\]

Thus the topological route is no longer blocked by pair collinearity on this branch.

For an exact periodic return, the frame path defines a loop in

\[
SO(3),
\]

with class in

\[
\pi_1(SO(3))\cong\mathbb Z_2.
\]

Neither class is yet contradictory.

---

## 12. Updated pair-level frontier

On the common ergodic hard-core component,

\[
\boxed{
\mathcal E_*
\Longrightarrow
\mathcal R_{pair}^{rigid}
\lor
\mathcal A_{pair}^{rel}>0,
}
\]

where

\[
\mathcal R_{pair}^{rigid}
:
\quad
\xi_a\cdot\xi_b=c_*,
\quad |c_*|<1,
\]

and

\[
\mathcal A_{pair}^{rel}>0
:
\quad
\langle|c_{ab}'|\rangle>0
\]

forces positive same-pair transverse/diffusive PDE charge.

The second branch is now a fully coupled dual--ratchet--production recurrence.

The first branch is a rigid moving-frame recurrence.

---

## 13. Highest-value next target

The rigid-pair branch is now the sharper survivor.

Write the pair-frame angular velocity as the vector `varpi_ab` satisfying

\[
\mathcal A_{ab}v
=\varpi_{ab}\times v.
\]

The next audit should compare `varpi_ab` with

1. the individual direction equations of both lineages;
2. the local symmetric strain tensors `Sigma_a`, `Sigma_b`;
3. the projected diffusion terms;
4. the finite-lineage flux-transfer cycle.

The goal is to determine whether a common rigid pair rotation can be sustained by symmetric strain alone, or whether viscosity/transfer must provide a signed torque-like remainder each cycle.

---

## 14. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
