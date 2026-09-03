# DSD M5-667 — Audit: Type-I vorticity-direction regularity criteria do not automatically close the normalized smooth CE-H hull

Date: 2026-09-03

Status: **EXTERNAL-THEOREM AUDIT / GIGA--MIURA AND RELATED VORTICITY-DIRECTION CRITERIA EXCLUDE TYPE-I BLOW-UP WHEN THE PHYSICAL VORTICITY DIRECTION IS UNIFORMLY CONTINUOUS IN SPACE, UNIFORMLY IN TIME, ON THE LARGE-VORTICITY REGION / THE M5-508 COMPACT HULL GIVES UNIFORM SMOOTHNESS OF THE NORMALIZED DIRECTION `xi(y,theta)`, BUT AFTER RETURNING TO PHYSICAL VARIABLES ITS LIPSCHITZ CONSTANT SCALES LIKE `(-s)^(-1/2)` / THEREFORE NORMALIZED `C^1` COMPACTNESS DOES NOT SUPPLY THE REQUIRED TIME-INDEPENDENT PHYSICAL MODULUS / THE EXTERNAL CRITERION IS A CONSISTENCY CHECK, NOT AN AUTOMATIC CLOSURE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. External criterion

A line of geometric regularity results (Giga--Miura and later variants) shows, under a Type-I/ODE blow-up-rate assumption, that a candidate singularity is excluded if the physical vorticity direction is uniformly continuous on the region where vorticity magnitude is large, with a modulus that is uniform as the singular time is approached.

The relevant qualitative condition is stronger than smoothness after blow-up normalization.

---

## 2. Current normalized direction control

On the CE-H compact hull, for every fixed high-vorticity threshold `a0>0`,

\[
\rho=|W|\ge a_0
\]

implies that

\[
\xi:=\frac{W}{|W|}
\]

is smooth with a uniform normalized bound

\[
\boxed{\|\nabla_y\xi\|_{L^\infty(\rho\ge a_0)}\le C_{a_0}.}
\]

Hence

\[
|\xi(y_1,\theta)-\xi(y_2,\theta)|
\le C_{a_0}|y_1-y_2|.
\]

---

## 3. Return to physical variables

With

\[
y=\frac{x}{\sqrt{-s}},
\qquad
\theta=-\log(-s),
\]

the vorticity direction is unchanged as a vector value:

\[
\xi_{phys}(x,s)=\xi\!\left(\frac{x}{\sqrt{-s}},\theta\right).
\]

Therefore

\[
\boxed{
|\xi_{phys}(x_1,s)-\xi_{phys}(x_2,s)|
\le
\frac{C_{a_0}}{\sqrt{-s}}|x_1-x_2|.
}
\]

The physical Lipschitz constant diverges at the Type-I rate.

Thus the normalized compact hull does not produce a time-independent physical modulus of continuity.

---

## 4. Why the shrinking parabolic region does not fix this

The geometric criteria examine high-vorticity points in regions whose diameter is comparable to the parabolic scale `sqrt(-s)`.

Two normalized points separated by a fixed `O(1)` distance correspond to physical points separated by `O(sqrt(-s))`.

A time-independent physical modulus would force

\[
|\xi(y_1,\theta)-\xi(y_2,\theta)|\to0
\]

for every fixed normalized separation as `s->0-`.

That is substantially stronger than the current bound; it would make a blow-up-limit direction spatially constant on the connected high-vorticity region.

The CE-H hard branch does not currently have this property.

---

## 5. Relation to existing CE-H splits

The current CE-H analysis already proves that a completely spatially flat vorticity direction cannot be the generic nonzero finite-enstrophy survivor: M5-614 forces a positive direction-Dirichlet floor, and M5-618--621 force a non-Beltrami transverse-magnitude/curvature channel.

Therefore the failure to meet the external direction-coherence criterion is consistent with the internal hard-core geometry.

---

## 6. Audit verdict

Do **not** claim

\[
\text{normalized smooth xi}
\Rightarrow
\text{Giga--Miura physical uniform continuity}.
\]

The correct implication is only

\[
\text{physical uniform continuity}
\Rightarrow
\text{flat direction in the blow-up limit},
\]

which would close a much narrower branch.

The present hard hull remains outside that automatic closure because the normalized direction may retain order-one variation on the parabolic scale.

---

## 7. External dependency note

The cited geometric regularity criterion is used only as an audit/comparison theorem here. No new internal implication depends on it.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
