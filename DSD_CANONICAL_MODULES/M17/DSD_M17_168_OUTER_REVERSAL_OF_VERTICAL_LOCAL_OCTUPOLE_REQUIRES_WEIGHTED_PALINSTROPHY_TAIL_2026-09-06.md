# DSD M17-168 — Reversing or neutralizing the vertical local-octupole sign in the global kappa-production channel requires a quantitative weighted palinstrophy tail

Date: 2026-09-06  
Canonical ID: **M17-168**

Status: **COERCIVE OUTER-CANCELLATION GATE / M17-167 REWRITES THE FULL VERTICAL KAPPA-PRODUCTION AS THE SIGN-CHANGING AXIAL l=3 MOMENT OF THE POSITIVE DENSITY `|grad W|^2`, WHILE M17-164 GIVES A LOCAL CORE `P(R0)=(3/7)R0^2 O_V+O(R0^3)`. IF THE FULL KAPPA-PRODUCTION FAILS TO RETAIN A FIXED FRACTION OF THAT LOCAL SIGN, THE OUTER REGION MUST CONTRIBUTE AN OPPOSITE AXIAL MOMENT OF COMPARABLE SIZE. BOUNDEDNESS OF THE ANGULAR KERNEL THEN FORCES `int_{|z|>R0}|grad W|^2 |z|^-4 dz >= c R0^2 |O_V|` UP TO THE LOCAL TAYLOR ERROR. IN PARTICULAR THE UNWEIGHTED OUTER PALINSTROPHY IS AT LEAST `c R0^6 |O_V|`. THUS MESOSCOPIC/GLOBAL CANCELLATION IS NO LONGER COST-FREE AT THE SPATIAL LEVEL; IT REQUIRES POSITIVE PALINSTROPHY OCCUPANCY. THIS IS NOT YET A TEMPORAL DISSIPATION CONTRADICTION BECAUSE THE SAME OUTER ARCHITECTURE MAY BE REUSED BY RECURRENT CROSSINGS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Core and outer decomposition

At a marked vertical crossing core `Y`, define

\[
P(R)
:=\int_{|z|<R}
|\nabla W(Y-z)|^2
\mathcal K_{333}(z)dz.
\]

M17-167 identifies the full kappa-production as

\[
\boxed{
\Pi_{V,\kappa}^{prod}(Y)
=\lim_{R\to\infty}P(R).
}
\]

M17-164 and M17-167 give the local expansion

\[
\boxed{
P(R_0)
=\frac37R_0^2O_V+\mathcal E_0,
\qquad
|\mathcal E_0|\le C M_4R_0^3.
}
\]

Write

\[
\Pi_{V,\kappa}^{prod}
=P(R_0)+P_{out}(R_0),
\]

where

\[
P_{out}(R_0)
:=\int_{|z|>R_0}
|\nabla W(Y-z)|^2
\mathcal K_{333}(z)dz.
\]

---

## 2. Define an outer-reversal event

Fix `0<=eta<1`.
Say that the full kappa-production fails to retain an `eta` fraction of the local orientation if

\[
\boxed{
O_V\,\Pi_{V,\kappa}^{prod}
\le
\eta\,|O_V|\,|P(R_0)|
}
\]

with the convention that `R0` is small enough that `P(R0)` has the sign of `O_V`.

A simpler sufficient case is complete sign reversal or neutralization:

\[
\boxed{
O_V\,\Pi_{V,\kappa}^{prod}\le0.
}
\]

Then the outer term must oppose the core by a comparable amount.

---

## 3. Minimum outer axial moment

Assume `R0` is chosen so that

\[
|\mathcal E_0|
\le\frac{1-\eta}{2}\frac37R_0^2|O_V|.
\]

Then a failure to retain the local sign by the amount in Section 2 forces

\[
\boxed{
|P_{out}(R_0)|
\ge
c_\eta R_0^2|O_V|,
}
\]

where `c_eta>0` is universal once `eta` is fixed.

For full sign reversal one may take a fixed numerical fraction of `3/7` after absorbing the Taylor remainder.

---

## 4. Bound the angular moment by positive palinstrophy

The kernel obeys

\[
|\mathcal K_{333}(z)|
\le C_K|z|^{-4}.
\]

Therefore

\[
|P_{out}(R_0)|
\le
C_K
\int_{|z|>R_0}
\frac{|\nabla W(Y-z)|^2}{|z|^4}dz.
\]

Combine with Section 3:

\[
\boxed{
\int_{|z|>R_0}
\frac{|\nabla W(Y-z)|^2}{|z|^4}dz
\ge
c_*R_0^2|O_V|.
}
\]

This is the weighted palinstrophy-tail cost of outer reversal.

---

## 5. Unweighted consequence

Since on `|z|>R0`,

\[
|z|^{-4}\le R_0^{-4},
\]

we have

\[
\int_{|z|>R_0}
\frac{|\nabla W|^2}{|z|^4}dz
\le
R_0^{-4}
\int_{|z|>R_0}|\nabla W|^2dz.
\]

Thus

\[
\boxed{
\int_{|z|>R_0}|\nabla W|^2dz
\ge
c_*R_0^6|O_V|.
}
\]

This lower bound is weaker than the weighted one but makes the positive cost explicit in ordinary palinstrophy units.

---

## 6. Dyadic shell form

Let

\[
A_m(R_0)
:=\{2^mR_0<|z|<2^{m+1}R_0\}.
\]

Then

\[
\boxed{
\sum_{m\ge0}
(2^mR_0)^{-4}
\int_{A_m(R_0)}|\nabla W|^2dz
\gtrsim
R_0^2|O_V|.
}
\]

Hence the cancellation must be carried by a genuine dyadic palinstrophy-anisotropy stack around the marked core.

It cannot arise from an outer region with arbitrarily small positive palinstrophy mass.

---

## 7. Crossing-ensemble implication

M17-095--165 force a positive average of the relative-speed-weighted local octupole/production coefficient.

If a positive fraction of this crossing population avoids transferring that sign to the full kappa-production channel, then those crossings must lie in the weighted-palinstrophy-tail branch of Section 4.

Symbolically,

\[
\boxed{
\text{M5-biased crossing}
\Longrightarrow
\text{global-sign retention}
\ \lor\
P_{tail}^{weighted}.
}
\]

The exact population statement still retains the M5 label measure and relative-speed weight.

---

## 8. Why this is not yet a temporal contradiction

The lower bound in Section 4 is instantaneous and spatial.
The same outer palinstrophy architecture may be encountered repeatedly by a recurrent marked core.

Therefore one may not multiply the per-crossing spatial lower bound by the number of crossings without a packing, disjointness, or temporal turnover theorem.

This is the same DSD distinction encountered in Rank-2:

\[
\boxed{
\text{positive spatial occupancy}
\neq
\text{nonrecyclable temporal cost}.
}
\]

---

## 9. DSD audit

### Audit A — using positivity of `|grad W|^2` to assign the kernel sign
Rejected. The kernel remains sign-changing.

### Audit B — calling the weighted tail a dissipation integral
Rejected. It is an instantaneous weighted palinstrophy occupancy.

### Audit C — choosing `R0` without Taylor control
`R0` must lie inside the uniform local fourth-jet radius of the regular compact crossing hull.

### Audit D — summing the cost over crossings without overlap control
Rejected.

### Audit E — proof status
Outer reversal now pays a positive spatial palinstrophy cost, but recycling remains possible.

---

## 10. Updated vertical gate

At every quantitatively regular crossing with nonzero `O_V`, either

\[
\boxed{
\Pi_{V,\kappa}^{prod}
\text{ retains the local octupole orientation}
}
\]

or

\[
\boxed{
\int_{|z|>R_0}
|\nabla W|^2|z|^{-4}dz
\gtrsim R_0^2|O_V|.
}
\]

The next useful calculation is to determine whether the M5 crossing flux can reuse the same weighted palinstrophy tail indefinitely, or whether motion of the marked zero surface forces a nontrivial sweep/packing of these weighted neighborhoods.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
