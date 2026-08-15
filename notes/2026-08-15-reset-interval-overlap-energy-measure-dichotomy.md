# Reset intervals: energy-measure summability versus unbounded overlap

Date: 2026-08-15

Status: **OVERLAP CORRECTION / STOPPING-TIME DICHOTOMY DERIVED / GLOBAL REGULARITY NOT PROVED.**

This note corrects a necessary qualification in the smooth material-flux reset cost.

A lower bound for each reset interval cannot be summed blindly if the intervals overlap. The finite kinetic-energy dissipation measure may be counted multiple times.

---

## 1. Physical dissipation measure

Define the finite positive measure on every smooth interval before a hypothetical singular time `T*` by

\[
\boxed{
 d\mu(t)=\nu\|\omega(t)\|_2^2dt.
}
\]

The kinetic-energy identity gives

\[
\boxed{
\mu([0,T^*))
\le\frac12\|u_0\|_2^2<\infty.
}
\]

For a geometry-controlled fixed-fraction flux reset with parameters `(W_j,R_j)`, the previous lemma gives

\[
\boxed{
\mu(I_j)
\ge c q_j^{-1/2},
\qquad
q_j=W_j/R_j^{10},
}
\]

where `I_j` is the corresponding reset interval.

---

## 2. Disjoint family

If a selected infinite family of reset intervals is pairwise disjoint, then

\[
\sum_j\mu(I_j)
\le\mu([0,T^*)).
\]

Therefore

\[
\boxed{
\sum_j q_j^{-1/2}<\infty.
}
\]

This is the previously derived super-separated Zeno condition.

It is valid for disjoint reset episodes.

---

## 3. General overlapping family

For an arbitrary countable family define the overlap multiplicity

\[
\boxed{
N(t)=\sum_j\mathbf 1_{I_j}(t).
}
\]

Then Tonelli gives the exact counting identity

\[
\boxed{
\sum_j\mu(I_j)
=
\int_0^{T^*}N(t)d\mu(t).
}
\]

Hence the individual lower bounds imply

\[
\boxed{
 c\sum_jq_j^{-1/2}
\le
\int N(t)d\mu(t).
}
\]

Finite total energy dissipation controls the right side only if `N` is bounded, or more generally integrable against `mu` with a uniform multiplicity bound.

Therefore one must not infer unconditional summability of `q_j^{-1/2}`.

---

## 4. Bounded-overlap branch

If

\[
\boxed{
N(t)\le M<\infty
}
\]

for almost every `t` with respect to `mu`, then

\[
\int N d\mu
\le M\mu([0,T^*]),
\]

and therefore

\[
\boxed{
\sum_jq_j^{-1/2}<\infty.
}
\]

Thus every bounded-overlap geometry-controlled reset cascade is necessarily super-separated.

---

## 5. Unbounded-overlap branch

If

\[
\sum_jq_j^{-1/2}=\infty
\]

while the physical dissipation measure is finite, then necessarily

\[
\boxed{
N(t)\text{ is unbounded on arbitrarily late sets carrying }\mu\text{-mass}.
}
\]

In a finite-time singular scenario the late reset intervals have endpoints tending to `T*`. Therefore unbounded overlap is a genuine terminal multiscale stacking phenomenon rather than a fixed early-time event.

Schematic form:

\[
\boxed{
I_{j_1},I_{j_2},\ldots
\text{ stack on the same late spacetime region while their crossing scales separate.}
}
\]

This is a different branch from a sequence of temporally separated reconnections.

---

## 6. Connection to scale packing

The repository already has static Gaussian/dyadic ANOVA and scale-square-function identities. They prevent arbitrary double counting of changes in affine representatives at one fixed time.

However the present reset observables are

- material rather than concentric Eulerian windows;
- time dependent;
- signed flux quantities rather than only gradient variance.

Thus the existing scale ANOVA does **not** yet imply

\[
\int N d\mu<\infty
\]

with a universal multiplicity bound.

A new material multiscale Carleson estimate would be required to close this overlap branch.

---

## 7. Correct final Zeno trichotomy

The repeated-reset endgame is therefore more precisely

\[
\boxed{
\text{Z1: bounded-overlap super-separated resets}
}
\]

with

\[
\sum_jq_j^{-1/2}<\infty,
\]

or

\[
\boxed{
\text{Z2: unbounded-overlap multiscale reset stack},
}
\]

or

\[
\boxed{
\text{Z3: material-probe H2 distortion / derivative collapse}.
}
\]

The earlier statement `sum q_j^{-1/2}<infinity` must always be read with the disjoint or bounded-overlap qualification.

---

## 8. Next proof target

The most promising next object is a material-flux Carleson functional that controls both reset size and overlap multiplicity, schematically

\[
\boxed{
\sum_{j:I_j\subset Q}
q_j^{-1/2}
\lesssim
\mu(cQ)
+\text{derivative/deformation error}
}
\]

for a material/parabolic region `Q`.

If such an estimate held uniformly, unbounded reset stacking would reduce to the already typed derivative/deformation error.

No such estimate has yet been proved.

Status: **RESET COST SUMMABILITY CORRECTED FOR OVERLAP / FINAL HARD BRANCH IDENTIFIED AS MATERIAL MULTISCALE CARLESON PACKING OR PROBE DISTORTION.**