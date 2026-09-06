# DSD M17-222 — Tempered whole-shell H2/L2 spectral concentration extracts a finite remote derivative-subscale packet

Date: 2026-09-06  
Canonical ID: **M17-222**

Status: **WHOLE-SHELL PACKET EXTRACTION / ON AN M17-207 GLOBALLY TEMPERED DYADIC SHELL, THE ENSTROPHY OF A FIXED ENLARGED NEIGHBORHOOD IS COMPARABLE TO THE CORE SHELL ENSTROPHY. IF THE CORE SHELL HAS `H2/L2` SPECTRAL RATIO `Lambda_R -> infinity`, A SMOOTH SHELL CUTOFF EQUAL TO ONE ON THE CORE PRODUCES A COMPACT FIELD `F_R` WITH THE SAME DIVERGENT `H2/L2` RATIO. A FIXED UNIT-SCALE PARTITION OF UNITY THEN CANNOT DILUTE THIS RATIO OVER ARBITRARILY MANY CELLS: THE RECONSTRUCTION IDENTITY FOR `Delta F_R`, TOGETHER WITH `||grad F_R||_2^2 <= ||F_R||_2 ||Delta F_R||_2`, SHOWS THAT THE SUM OF LOCALIZED `H2` MASSES IS A FIXED FRACTION OF THE GLOBAL `H2` MASS ONCE THE RATIO IS LARGE. HENCE ONE BOUNDED-SIZE CELL HAS DIVERGENT LOCAL `H2/L2`, AND ITS LAPLACIAN AND FIRST/SECOND-DERIVATIVE CORRELATION LENGTHS TEND TO ZERO. THUS THE TEMPERED WHOLE-SHELL SPECTRAL EXIT HAS A FINITE REMOTE DERIVATIVE-SUBSCALE WITNESS; DIFFUSE SPATIAL FRAGMENTATION IS NOT A TERMINAL ESCAPE AT THIS LEVEL. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Tempered core and enlarged shell

Let `C_R` be a core remote dyadic shell and `C_R^*` a fixed finite enlargement by neighboring dyadic shells.

Set

\[
E_R:=\int_{C_R}|W|^2dy,
\qquad
H_R:=\int_{C_R}|\Delta W|^2dy.
\]

Assume

\[
\boxed{
\Lambda_R^2:=\frac{H_R}{E_R}\to\infty.
}
\]

On an M17-207 globally tempered shell, every fixed finite neighbor sum is controlled by the core mass. Therefore

\[
\boxed{
E_R^*:=\int_{C_R^*}|W|^2dy
\le C_*E_R.
}
\]

No derivative comparability between neighboring shells is assumed.

---

## 2. Compact shell cutoff preserves spectral divergence

Choose a smooth radial cutoff `psi_R` satisfying

\[
0\le\psi_R\le1,
\qquad
\psi_R\equiv1\text{ on }C_R,
\qquad
\operatorname{supp}\psi_R\subset C_R^*.
\]

Define

\[
\boxed{F_R:=\psi_RW.}
\]

Since `psi_R=1` on the core shell, all cutoff derivatives vanish there and

\[
\Delta F_R=\Delta W
\qquad\text{on }C_R.
\]

Hence

\[
\boxed{
\|\Delta F_R\|_2^2
\ge H_R.
}
\]

Also

\[
\boxed{
\|F_R\|_2^2
\le E_R^*
\le C_*E_R.
}
\]

Therefore

\[
\boxed{
\frac{\|\Delta F_R\|_2^2}{\|F_R\|_2^2}
\ge
\frac1{C_*}\Lambda_R^2
\to\infty.
}
\]

Thus the whole-shell spectral concentration is converted into a compactly supported field without any carrier-localization assumption.

---

## 3. Fixed bounded-scale partition of unity

Choose a smooth partition of unity on `R^3`

\[
\boxed{
\sum_{m\in\mathbb Z^3}\chi_m^2\equiv1
}
\]

such that every `chi_m` is supported in a cube of fixed bounded diameter, the overlap multiplicity is uniformly finite, and

\[
\sup_m
\left(
\|\nabla\chi_m\|_\infty
+\|\Delta\chi_m\|_\infty
\right)
\le C_\chi.
\]

Set

\[
\boxed{f_{R,m}:=\chi_mF_R.}
\]

Then

\[
\boxed{
\sum_m\|f_{R,m}\|_2^2
=\|F_R\|_2^2.
}
\]

Only finitely many `m` intersect `supp F_R` for each fixed `R`.

---

## 4. The localized H2 masses retain a fixed fraction of the global H2 mass

Because

\[
\chi_m\Delta F_R
=\Delta(\chi_mF_R)
-2\nabla\chi_m\cdot\nabla F_R
-(\Delta\chi_m)F_R,
\]

we have

\[
\|\chi_m\Delta F_R\|_2^2
\le
3\|\Delta f_{R,m}\|_2^2
+C|\nabla\chi_m|_\infty^2\|\nabla F_R\|_{L^2(\operatorname{supp}\chi_m)}^2
+C|\Delta\chi_m|_\infty^2\|F_R\|_{L^2(\operatorname{supp}\chi_m)}^2.
\]

Summing and using finite overlap,

\[
\boxed{
\|\Delta F_R\|_2^2
\le
3\sum_m\|\Delta f_{R,m}\|_2^2
+C_1\|\nabla F_R\|_2^2
+C_2\|F_R\|_2^2.
}
\]

For compact `F_R`, Fourier interpolation gives

\[
\boxed{
\|\nabla F_R\|_2^2
\le
\|F_R\|_2\|\Delta F_R\|_2.
}
\]

Write

\[
E_F:=\|F_R\|_2^2,
\qquad
H_F:=\|\Delta F_R\|_2^2.
\]

Since

\[
H_F/E_F\to\infty,
\]

we have

\[
\frac{\|\nabla F_R\|_2^2}{H_F}
\le
\left(\frac{E_F}{H_F}\right)^{1/2}
\to0
\]

and

\[
\frac{E_F}{H_F}\to0.
\]

Consequently, for sufficiently large `R`,

\[
\boxed{
\sum_m\|\Delta f_{R,m}\|_2^2
\ge c_HH_F
}
\]

with a fixed `c_H>0` depending only on the partition.

---

## 5. Pigeonhole a finite packet with divergent local ratio

Suppose every active cell satisfied

\[
\frac{\|\Delta f_{R,m}\|_2^2}{\|f_{R,m}\|_2^2}
<L_R.
\]

Summing would give

\[
\sum_m\|\Delta f_{R,m}\|_2^2
<L_R\sum_m\|f_{R,m}\|_2^2
=L_RE_F.
\]

Therefore, using Section 4, at least one index `m(R)` satisfies

\[
\boxed{
\frac{\|\Delta f_R^{loc}\|_2^2}
{\|f_R^{loc}\|_2^2}
\ge
c_H\frac{H_F}{E_F}
}
\]

where

\[
\boxed{f_R^{loc}:=f_{R,m(R)}.}
\]

Hence

\[
\boxed{
\frac{\|\Delta f_R^{loc}\|_2^2}
{\|f_R^{loc}\|_2^2}
\to\infty.
}
\]

Each `f_R^loc` is supported in a set of fixed bounded diameter independent of `R`.

Because `F_R` is supported in `C_R^*`, the selected packet center `p_R` satisfies

\[
\boxed{|p_R|\asymp R\to\infty.}
\]

Thus the packet is finite and genuinely remote.

---

## 6. Intrinsic local derivative scale

For the selected packet define

\[
E_{loc}:=\|f_R^{loc}\|_2^2,
\qquad
H_{loc}:=\|\Delta f_R^{loc}\|_2^2.
\]

Set

\[
\boxed{
\ell_R^{loc}
:=\left(\frac{E_{loc}}{H_{loc}}\right)^{1/4}.
}
\]

Then

\[
\boxed{\ell_R^{loc}\to0.}
\]

Also define

\[
\delta_R^2
:=
\frac{\|\nabla f_R^{loc}\|_2^2}{H_{loc}}.
\]

Fourier interpolation gives

\[
\|\nabla f_R^{loc}\|_2^2
\le E_{loc}^{1/2}H_{loc}^{1/2},
\]

so

\[
\boxed{
\delta_R
\le\ell_R^{loc}
\to0.
}
\]

Therefore

\[
\boxed{
\frac{\delta_R}{R}\to0.
}
\]

This is a finite remote derivative-subscale witness.

---

## 7. Fragmentation is not terminal for the whole-shell spectral branch

M17-221 retained a localization-fragmentation exit for an arbitrary carrier because a tiny carrier need not have a comparable bounded neighborhood.

M17-222 begins one level earlier with the **whole tempered shell**.
M17-207 gives the required enlarged-shell `L2` comparability, and the fixed partition argument does not care how many small carrier components exist.

Therefore

\[
\boxed{
G_{whole\text{-}shell\ H2/L2\ spectral}^{tempered}
\Longrightarrow
H_{finite\ remote\ derivative\ subscale\ packet}.
}
\]

There is no additional diffuse spatial-fragmentation terminal branch at the whole-shell level.

---

## 8. Relation to M17-210 through M17-221

M17-210 identifies the hard weighted multiplier exit as whole-shell `H2/L2` spectral concentration.

M17-211 closes the bounded-ratio lane.

M17-212--220 provide useful amplitude/director geometry inside the unbounded-ratio lane and show that fixed-fraction quiet anisotropy is inherited rather than freshly generated.

M17-221 observes that any carrier-local spectral return already has a vanishing intrinsic Laplacian scale.

M17-222 supplies the stronger canonical routing for the original whole-shell branch:

\[
\boxed{
G_{H2/L2\ spectral}^{tempered}
\Longrightarrow
H_{finite\ remote\ vorticity\ derivative\ subscale}.
}
\]

Thus the compressed frontier should use the derivative-subscale packet as the nonrecycling endpoint rather than `spectral/director recycling`.

---

## 9. What remains open

The extracted packet has

\[
|p_R|\to\infty,
\qquad
\ell_R^{loc}\to0.
\]

The next missing step is dynamical rather than spatial:

\[
\boxed{
\text{finite remote packet with }\ell_R\to0
\Longrightarrow
\text{parabolically rescaled nonzero ancient/eternal limit}
\lor
\text{turnover/forcing/interface payment}.
}
\]

At the scale `ell_R`, the similarity drift and zeroth-order stretching/reaction terms are formally lower order, suggesting a heat-equation tangent problem.

However nontrivial mass persistence on the `ell_R^2` time scale must be proved before any heat-Liouville contradiction is claimed.

---

## 10. DSD analysis

### 10.1 Spatial versus dynamical extraction

M17-222 proves a spatial finite-packet witness at one time.
It does not yet prove persistence of that packet through a parabolic time window.

### 10.2 Why multiplicity disappears here

The partition argument sums over all cells before pigeonholing.
Increasing the number of cells cannot hide the total `H2` mass because the derivative commutator costs are lower order relative to a divergent global `H2/L2` ratio.

### 10.3 Scope of temperedness

Temperedness is used only to compare the `L2` mass of the fixed enlarged shell with the core shell when creating `F_R`.
No `H2` neighbor comparability is assumed.

---

## 11. DSD audit

- The shell cutoff equals one on the spectral core, so no lower bound on cutoff commutator terms is needed.
- Fourier interpolation is applied only to compactly supported localized fields.
- The partition has fixed geometry and finite overlap; constants do not grow with the shell radius or number of active cells.
- The result extracts a packet but does not yet supply a dynamic lifetime.
- The old M5 remote-subscale result is structurally adjacent but not silently treated as the same derivative-order theorem.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
