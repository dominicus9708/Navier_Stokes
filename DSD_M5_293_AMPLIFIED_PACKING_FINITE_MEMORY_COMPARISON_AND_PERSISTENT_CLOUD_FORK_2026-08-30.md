# DSD M5-293 — Amplified Satellite Packing vs Finite Memory: Persistent-Cloud Fork

Date: 2026-08-30

Parent: `DSD_M5_292_SATELLITE_PACKING_PERSISTENCE_MIXED_NORM_THRESHOLD_2026-08-30.md`

Status: **FINITE-MEMORY COMPARISON / A LARGE GLOBAL SATELLITE PACKING DOES NOT AUTOMATICALLY VIOLATE THE LOCAL COHERENT MULTIFLUX CAP / TEMPORAL REPLACEMENT AMPLIFICATION ROUTES TO EXISTING POSITIVE-FREQUENCY EXITS, BUT A LARGE SPATIALLY SEPARATED PERSISTENT CLOUD REMAINS A DISTINCT COLLECTIVE FRONTIER / GLOBAL REGULARITY UNPROVED.**

---

## 1. Two different meanings of multiplicity

M5-292 introduced

\[
N(\sigma)
\]

as the number of comparable natural satellite packets inside an outer ball

\[
B_d,
\qquad d=L\ell.
\]

The existing finite-memory theorem instead bounds the number

\[
N_{max}<\infty
\]

of coherent same-sign fixed-flux material populations stored inside **one bounded natural-scale recurrent core**.

These are not the same multiplicity.

The outer satellite ball contains on the order of

\[
\boxed{L^3}
\]

disjoint natural cells of diameter comparable to `ell`.

Hence it is perfectly compatible with the local finite-memory theorem to have

\[
N(\sigma)\asymp L^3
\]

provided the packets occupy spatially different natural cells.

Therefore

\[
\boxed{
N\to\infty
\not\Rightarrow
N>N_{max}\text{ in one coherent core}.
}
\]

---

## 2. Direct finite-memory closure is invalid

The tempting argument

\[
\text{amplified mixed norm}
\Rightarrow
N\to\infty
\Rightarrow
\text{finite-memory contradiction}
\]

is false.

The finite-memory theorem is local/material.  The mixed-norm packing count is global over the larger outer observation region.

At most one obtains a cellwise statement: if the outer region is partitioned into `O(L^3)` natural cells and each cell stores at most `N_max` coherent populations, then

\[
N\lesssim N_{max}L^3.
\]

This only changes the constant in the already-known geometric packing ceiling

\[
N\lesssim L^3.
\]

It does not improve the asymptotic power of `L`.

---

## 3. Formation split: spatial occupancy vs temporal replacement

The ensemble descriptor from M5-292 must be refined.

A large value of

\[
\mathcal P_{s,l}
=
\int N(\sigma)^{l/s}d\sigma
\]

can be produced in two fundamentally different ways.

### A. Persistent spatial cloud

Many packets occupy many different natural cells and remain substantially the same material/coherent populations over the observation interval.

Then `N(sigma)` is large while the replacement count may be small.

### B. Temporal churn / replacement

A bounded collection of cells repeatedly loses and gains coherent populations.

Then the large space-time packing descriptor is paid by a large number of material replacement events.

These two mechanisms must not be merged.

---

## 4. Temporal churn enters the existing finite-memory theorem

Suppose a fixed positive fraction of the packing/persistence mass is produced by replacement events in bounded natural cells.

The existing finite-memory theorem gives:

\[
\boxed{
\text{positive-density coherent replacement}
\Longrightarrow
X_{visc,+freq}
\lor
X_{proj,+freq}
\lor
X_{export,+freq}
\lor
X_{H,+freq}.
}
\]

Thus the replacement-generated part of the amplified mixed norm is not a new terminal branch.

It routes to the existing positive-frequency dynamic exits.

Symbolically,

\[
\boxed{
\mathscr P_{amp}^{churn}
\Longrightarrow
T_{dynamic,+freq}
\lor H_{+freq}
\lor X_{export,+freq}.
}
\]

No new contradiction is claimed; the existing ledgers and constant comparisons remain necessary.

---

## 5. Persistent cloud is not controlled by finite memory

Now suppose the large packing descriptor is realized by `N` spatially separated packets that persist without fixed-fraction replacement.

Then the finite-memory rule inside each natural cell may never be activated.

For example, one coherent packet per natural cell is consistent with

\[
N(\sigma)\asymp cL^3
\]

and with the local bound `1 <= N_max` in every cell.

Thus

\[
\boxed{
\mathscr P_{amp}^{persistent-cloud}
}
\]

is a genuine remaining collective geometry.

---

## 6. Mixed-norm size of a persistent cloud

If a fraction `phi` of all natural cells is occupied and persists for `Theta` natural times, M5-292 gives

\[
\boxed{
M_\kappa
\sim
\Theta\phi^{l/s}L^{l-2}.
}
\]

Therefore the amplified threshold is

\[
\boxed{
g(\ell)\Theta\phi^{l/s}L^{l-2}
\gtrsim\varepsilon_0.
}
\]

This condition does not contain a replacement count.

Hence an amplified branch may be generated entirely by a persistent spatial cloud if the exponent/scaling regime allows it.

---

## 7. Weak-L3 size of the same cloud

The persistent-cloud interpretation also explains the weak-critical escalation.

For `N` disjoint natural packets of amplitude `~ell^{-1}` and volume `~ell^3`, the level set at amplitude `~ell^{-1}` has measure

\[
\sim N\ell^3.
\]

Thus the weak-`L3` quasi-norm scales as

\[
\boxed{
\|u\|_{L^{3,\infty}}
\gtrsim
\ell^{-1}(N\ell^3)^{1/3}
=N^{1/3}.
}
\]

Therefore

\[
N\to\infty
\Longrightarrow
\|u\|_{L^{3,\infty}}\to\infty,
\]

exactly as required by the Albritton–Barker contrapositive on a nontrivial ancient survivor.

This is consistency, not contradiction.

---

## 8. Axis-property question for the persistent cloud

A persistent cloud carries many vorticity axes and spatial radial directions.

The natural next collective descriptor is not merely the packet count but the signed/angular tensor sum of their far-field contributions.

Schematically, if packet `i` has vorticity content vector `Gamma_i` and direction from an observation point `n_i`, the induced far strain has leading form

\[
S_{far}
\sim
\sum_i
K(n_i)\frac{\Gamma_i}{r_i^3},
\]

where `K` is the degree-zero angular part of the Biot–Savart strain kernel.

A large persistent cloud therefore has a new fork:

\[
\boxed{
\text{noncancelling angular cloud}
\lor
\text{strong multipole/angular cancellation}.
}
\]

The first should produce ambient strain/H.

The second is a highly balanced collective geometry and requires a separate multipole/axis audit.

No lower bound is asserted here without controlling signs and angular kernel cancellation.

---

## 9. Updated amplified branch

The amplified packing lane is therefore refined to

\[
\boxed{
\mathscr P_{amplified}
\Longrightarrow
\mathscr P_{churn}
\lor
\mathscr P_{cloud}.
}
\]

The churn branch routes to existing dynamic exits:

\[
\boxed{
\mathscr P_{churn}
\Longrightarrow
T/H/export\text{ at positive frequency}.
}
\]

The cloud branch splits geometrically as

\[
\boxed{
\mathscr P_{cloud}
\Longrightarrow
H_{ambient}^{noncancel}
\lor
C_{angular/multipole}.
}
\]

The second term denotes a persistent high-multiplicity cloud whose low angular/multipole moments cancel strongly enough to avoid producing a large ambient field.

---

## 10. Relation to the Formation-Axiom decomposition

This is a direct example of why the Formation layer is useful.

The scalar mixed norm alone does not reveal **how** its mass is formed.

The same large value can be produced by

- many simultaneous structures;
- one structure persisting a long time;
- rapid replacement in a bounded set of cells;
- or combinations of these.

Those constructions have different PDE consequences.

Thus a complete descriptor must contain at least

\[
\boxed{
(\text{multiplicity},\text{persistence},\text{replacement rate},\text{angular moments}).
}
\]

---

## 11. Current merged frontier

Combining M5-291--M5-293 gives the sharpened frontier

\[
\boxed{
\text{hypothetical singularity}
\Longrightarrow
T_{dynamic}
\lor
A_{sparse/affine\ ancestry}
\lor
C_{persistent\ angular\ cloud}.
}
\]

Here

- `A_sparse/affine ancestry` merges the isolated satellite and hidden transverse affine strain obstruction;
- `C_persistent angular cloud` is the amplified branch after finite-memory churn has been removed;
- `T_dynamic` contains genuine material/pressure/projective/export exits, not mere descriptor changes.

This is a smaller and more structurally faithful tree than the former `T vs S_iso vs S_amp` classification.

---

## 12. Next target

The next highest-value calculation is the axis/multipole audit of the persistent cloud.

Goal:

1. normalize each natural packet by its signed vorticity content and radial direction;
2. derive the leading far-strain tensor at a reference point;
3. show that either the tensor sum has a quantitative lower bound, producing `H_ambient`, or the cloud must satisfy explicit low-multipole cancellation conditions;
4. determine whether those cancellation conditions force higher angular derivatives, alternating signs, material replacement, or a known pressure/turnover cost.

This is a standard Biot–Savart/multipole calculation; the Formation/Axis systems only determine the correct variables to inspect.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
