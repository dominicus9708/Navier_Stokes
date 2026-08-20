# Spatial Localization of the P_V H1 Threshold — 2026-08-20

Overall status: **THE GLOBAL H1 THRESHOLD LOCALIZES WITHOUT REWRITING THE PDE — GLOBAL REGULARITY NOT PROVED.**

A key advantage of the exact covariance identity is that both the nonlinear H1 production and hyperdissipation are spatial integrals of local densities. Therefore the blowup threshold can be localized by a partition-of-unity weighted-average argument, avoiding the most delicate cutoff commutators at the first step.

---

## 1. Local production and dissipation densities

Define

\[
q(x)
=-S:(M_{sp}+2M_{rg})(x),
\]

so that

\[
\boxed{
-\langle\mathcal R_{VI},-\Delta S\rangle
=\int q(x)dx.
}
\]

Let

\[
h(x)=|\Delta S(x)|^2,
\qquad
H=\int h(x)dx.
\]

The dangerous global ratio is

\[
\eta_{VI}
=
\frac{\int q}{\int h}.
\]

The pointwise sharp algebraic estimate gives

\[
q(x)
\le
\frac4{\sqrt6}|S(x)||\nabla S(x)|^2.
\]

---

## 2. Partition-of-unity averaging

Let `chi_alpha >= 0` be any locally finite spatial partition of unity,

\[
\sum_\alpha\chi_\alpha(x)=1.
\]

Define

\[
Q_\alpha=\int\chi_\alpha q,
\qquad
H_\alpha=\int\chi_\alpha h.
\]

Then

\[
\sum_\alpha Q_\alpha=\int q,
\qquad
\sum_\alpha H_\alpha=H.
\]

For every cell with `H_alpha>0`, set

\[
\eta_\alpha=Q_\alpha/H_\alpha.
\]

Therefore

\[
\boxed{
\eta_{VI}
=
\sum_\alpha
\frac{H_\alpha}{H}\eta_\alpha.
}
\]

This is an exact convex combination.

Consequently,

\[
\boxed{
\eta_{VI}\ge\nu
\Longrightarrow
\exists\alpha:\ \eta_\alpha\ge\nu.
}
\]

No localized Navier--Stokes equation and no pressure cutoff estimate are required for this conclusion.

---

## 3. Dyadic localization about the tracked center

Choose a smooth nonnegative partition adapted to

\[
B_{R_0}(X_*)
\]

and dyadic annuli

\[
A_k
=\{2^kR_0<|x-X_*|<2^{k+1}R_0\}.
\]

If a dangerous first-hitting profile satisfies

\[
\eta_{VI}\ge\nu-o(1),
\]

then at least one of the following carries the same threshold asymptotically:

1. the bounded tracked core;
2. a bounded-number annulus around it;
3. annuli whose normalized radii tend to infinity.

Case 3 is derivative-active spatial non-tightness: a fixed fraction of the hyperdissipation/prodution threshold lives farther and farther from the tracked core. This is naturally a `T` branch (or, if the derivative magnitude itself diverges, `H`).

Thus on a genuine non-`T` branch, the H1 threshold must be realized in a uniformly bounded normalized region.

---

## 4. Secondary active derivative core interpretation

Suppose an off-center bounded cell repeatedly satisfies

\[
\eta_\alpha\ge\nu.
\]

If its center remains a bounded normalized distance from the tracked first-hitting core, it belongs to the same bounded parent profile and can be included in the compact local class.

If instead its normalized center escapes, it is a secondary derivative-active core. Repeated appearance of such cells is exactly the secondary-core/non-tightness mechanism that the Type-I compactness program labels `T`.

Hence the H1 threshold provides an intrinsic definition of a **secondary active core** independent of an arbitrary amplitude threshold.

---

## 5. Why this helps the curvature bootstrap

The curvature bootstrap previously required applying

\[
\int|S||\nabla S|^2
\lesssim
P^{5/4}H^{1/4}
\]

to the active core rather than to the whole ancient field, because the latter carries a globally necessary critical tail.

The present localization result shows that a global dangerous H1 ratio cannot be produced only by a diffuse collection of individually subcritical regions: at least one region must itself be threshold-critical.

On the non-T branch this region remains in a fixed normalized parent ball. The remaining technical step is now only to convert its weighted/localized `Q_alpha,H_alpha` bounds into the standard compactly supported Sobolev quantities for `F=chi S`. The resulting cutoff errors live in the surrounding shell and can be separately classified as shell turnover if non-negligible.

---

## 6. A useful strengthened version

For any `delta>0`, if every cell obeys

\[
Q_\alpha\le(\nu-\delta)H_\alpha,
\]

then summing gives

\[
\boxed{
-\langle\mathcal R_{VI},-\Delta S\rangle
\le(\nu-\delta)H,
}
\]

and therefore

\[
\frac12P_S'\le-\delta H.
\]

Thus strict local depletion on every cell implies strict global H1 decay. A singularity must contain threshold cells arbitrarily late.

---

## 7. Current localization target

The next exact estimate is a cutoff-comparison lemma. For a threshold cell with a cutoff `chi` equal to one on that cell, compare

\[
P_F=\|\nabla(\chi S)\|_2^2,
\qquad
H_F=\|\Delta(\chi S)\|_2^2
\]

with the weighted core quantities. The errors have the schematic form

\[
R^{-2}P_{shell}+R^{-4}E_{shell}
\]

plus cubic shell terms. If these errors are small, the curvature bootstrap yields a uniform local H2 bound. If they are not small at infinitely many stages, the surrounding shell itself becomes an active turnover/secondary-core channel.

Status: **THE P_V H1 BLOWUP THRESHOLD LOCALIZES BY AN EXACT WEIGHTED-AVERAGE ARGUMENT. ON THE NON-T BRANCH A THRESHOLD REGION MUST REMAIN AT BOUNDED NORMALIZED RADIUS, WHICH REDUCES THE GLOBAL PASSIVE-TAIL OBSTRUCTION TO A QUANTITATIVE CUTOFF-COMPARISON LEMMA. GLOBAL REGULARITY REMAINS UNPROVED.**