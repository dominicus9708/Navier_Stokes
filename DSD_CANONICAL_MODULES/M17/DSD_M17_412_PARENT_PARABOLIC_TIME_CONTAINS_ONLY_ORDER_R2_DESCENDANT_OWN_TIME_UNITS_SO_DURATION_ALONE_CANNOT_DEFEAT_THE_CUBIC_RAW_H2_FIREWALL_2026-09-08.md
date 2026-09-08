# DSD M17-412 — One parent parabolic record window contains only `O(R^2)` descendant own-time units, so duration alone cannot defeat the cubic raw-`H2` firewall

Date: 2026-09-08  
Canonical ID: **M17-412**

Status: **ACTIVE TEMPORAL PACKING CAPACITY / DURATION NO-GO / SPACE-TIME MULTIPLICITY THRESHOLD**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input

M17-405 gives the raw-`H2` record weight

\[
R_m^{-3}.
\]

M17-411 shows that pure spatial multiplicity would need near-saturation of the full `O(R_m^3)` three-dimensional packing capacity.

The present module asks how much multiplicity can instead come from time residence inside one parent-scale record window.

## 2. Parent versus descendant parabolic clocks

Normalize the parent spatial scale to order one.

Let the descendant own-scale radius be

\[
\boxed{r_m\asymp R_m^{-1}.}
\]

The descendant natural parabolic time scale is therefore

\[
\boxed{r_m^2\asymp R_m^{-2}.}
\]

A parent parabolic record interval of order-one duration can contain at most

\[
\boxed{N_m^{time}\lesssim R_m^2}
\]

pairwise disjoint descendant unit-own-time intervals.

Equivalently, full occupation of the entire parent time window corresponds to `O(R_m^2)` descendant own-time units.

## 3. Full temporal saturation is still below the raw-H2 threshold

Assume optimistically that one fixed spatial descendant cell survives throughout the entire parent interval and pays an order-one normalized raw-`H2` charge in every unit own-time.

Then the record contains at most

\[
H_m^{time}\lesssim C R_m^2
\]

such temporal payments.

After the M17-405 ancestry weight,

\[
\boxed{
R_m^{-3}H_m^{time}
\lesssim
C R_m^{-1}.
}
\]

For geometric records,

\[
\sum_mR_m^{-1}<\infty.
\]

Therefore

\[
\boxed{
\text{duration alone inside one parent parabolic window}
\not\Rightarrow
\text{raw-`H2` contradiction}.
}
\]

This remains true even under **complete temporal saturation** of the parent record interval.

## 4. General space-time packet product

Let

\[
N_m^{space}
\]

be the number of bounded-overlap descendant spatial cells simultaneously available at record `m`, and let

\[
T_m^{own}
\]

be the number of bounded-overlap unit own-time intervals paid by each retained spatial population, or an appropriate average count.

If each space-time packet carries an order-one normalized raw-`H2` payment, then the record charge is schematically

\[
H_m^{pack}\gtrsim c\,N_m^{space}T_m^{own}.
\]

The ancestral contradiction criterion becomes

\[
\boxed{
\sum_m
\frac{N_m^{space}T_m^{own}}{R_m^3}
=\infty.
}
\]

The temporal capacity bound gives

\[
T_m^{own}\lesssim R_m^2
\]

inside a single parent parabolic record window.

Hence even at maximum temporal saturation the criterion reduces to

\[
\boxed{
\sum_m\frac{N_m^{space}}{R_m}=\infty.
}
\]

Thus full temporal use lowers the remaining spatial requirement from cubic to approximately **record-linear** multiplicity.

## 5. Partial residence thresholds

Write

\[
T_m^{own}=R_m^{\beta_m}b_m,
\qquad 0\le\beta_m\le2,
\]

schematically.

Then the raw-`H2` contradiction requires spatial multiplicity approximately

\[
N_m^{space}\sim R_m^{3-\beta_m}
\]

up to nonsummable slowly varying factors.

Examples:

- logarithmic residence `T_m^{own}\sim\log R_m` still requires nearly cubic spatial multiplicity;
- `T_m^{own}\sim R_m` requires nearly quadratic spatial multiplicity;
- full parent-time saturation `T_m^{own}\sim R_m^2` requires nearly linear spatial multiplicity.

This gives a continuous space-time tradeoff instead of treating duration and branching as separate qualitative exits.

## 6. Relation to M17-379

M17-379 guarantees only

\[
\sum_j\tau_{m,j}^{own}\gtrsim\log R_m
\]

on the representation-safe scale-mapped branch.

This is exponentially smaller than the maximum temporal capacity `R_m^2`.

Therefore the currently certified flux-evacuation residence occupies only a negligible fraction of the duration needed to reduce the spatial multiplicity threshold substantially.

## 7. Parent-window limitation

Could one obtain more than `R_m^2` unit own-times by simply extending farther in time?

Only by leaving the chosen parent parabolic record window.

That move requires a new genealogy/record allocation statement because the additional time may belong to older record cells and cannot be charged repeatedly to the same ancestor window.

Hence

\[
T_m^{own}\gg R_m^2
\]

inside one record is not a free option; it is a distinct long-genealogy/overlap branch.

## 8. Consequence for recurrence and loops

A retained one-dimensional vortex loop of parent-scale length can potentially supply `O(R_m)` spatial own-scale segments, while full parent-time persistence can supply `O(R_m^2)` temporal repetitions.

Their product is exactly

\[
O(R_m^3),
\]

the raw-`H2` ancestry threshold.

This identifies a particularly sharp candidate mechanism:

\[
\boxed{
\text{parent-length coefficient-scale loop}
+
\text{parent-time persistence}
\Longrightarrow
\text{potential cubic saturation}.
}
\]

The next module audits whether the existing exact CE-H loop structure actually supplies the required spatial and temporal factors without double counting.

## 9. DSD audit

The DSD role is a space-time capacity audit.

The ancestry exponent `3` can be decomposed between spatial and temporal multiplicity, but one parent parabolic window supplies at most two powers through time. Therefore at least one effective power must still come from spatial multiplicity, amplitude/flux growth, or another resource.

## 10. Audit verdict

**PASS-NO-GO / TARGET SHARPENING.**

Duration alone cannot close the raw-`H2` branch. Even maximal parent-window duration leaves a record-linear spatial multiplicity requirement.

The highest-value next target is the retained positive-flux CE-H loop: exact line constancy of `kappa` may provide the missing linear spatial factor, but only if tubular reach, flux retention, and parent-window time persistence are all certified.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]