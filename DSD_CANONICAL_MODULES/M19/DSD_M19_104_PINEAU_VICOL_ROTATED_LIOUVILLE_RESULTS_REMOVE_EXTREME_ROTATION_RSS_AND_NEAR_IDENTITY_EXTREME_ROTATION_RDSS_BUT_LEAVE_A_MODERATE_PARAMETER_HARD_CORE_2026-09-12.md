# DSD M19-104 — Pineau--Vicol rotated Liouville results remove extreme-rotation RSS and near-identity extreme-rotation RDSS but leave a moderate-parameter hard core

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / EXTERNAL 2026 ROTATED SELF-SIMILAR LIOUVILLE RESULTS INSERTED INTO THE M19-103 RSS/RDSS REDUCTION / SUBSTANTIAL PARAMETER REGIONS ARE REMOVED, BUT GENERAL RSS/RDSS NONEXISTENCE IS NOT ESTABLISHED / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Conditional input from M19-103

If the live extra-center theorem is proved and the quasi-compact recurrent component admits the retained center-manifold reduction, then

\[
\boxed{
\mathcal R_{critical}^{recurrent}
\Longrightarrow
\mathcal R_{RSS}
\lor
\mathcal R_{RDSS}.
}
\]

Thus the remaining recurrent critical problem becomes a rotated self-similarity problem.

---

## 2. External 2026 input

Ben Pineau and Vlad Vicol, *On rotated backwards self-similar solutions of the incompressible 3D Navier--Stokes equations*, arXiv:2607.09619 (2026), study:

1. rotated backward self-similar solutions (RSS), where similarity-time evolution is a constant-rate spatial rotation;
2. rotated discretely self-similar solutions (RDSS), where a discrete Navier--Stokes scaling step is accompanied by a spatial rotation.

Under a Type-I upper bound they prove Liouville-type nonexistence in parameter regimes that include:

- RSS when the rotation rate is sufficiently small or sufficiently large;
- RDSS under corresponding extreme-rotation conditions when the discrete scaling factor is sufficiently close to `1`.

The exact quantitative thresholds depend on the hypotheses and constants in their theorems and are not replaced here by invented universal numbers.

Their result does **not** claim nonexistence of arbitrary RSS/RDSS for every rotation rate and every scaling factor.

---

## 3. RSS parameter split

Write an RSS solution schematically as

\[
U(s)=\exp(s\alpha A)\cdot U_0,
\qquad A\in\mathfrak{so}(3).
\]

The external theorem removes the extreme-rate regimes

\[
\boxed{
|\alpha|\le\alpha_{small}
\quad\text{or}\quad
|\alpha|\ge\alpha_{large}
}
\]

on its certified Type-I application lane.

Ordinary self-similarity is the special case

\[
\alpha=0,
\]

which is also classically excluded under the standard Liouville hypotheses.

Thus a surviving RSS branch must lie in an intermediate rotation-rate window:

\[
\boxed{
\alpha_{small}<|\alpha|<\alpha_{large}
}
\]

with the understanding that the actual theorem thresholds are those of the external result.

This is a genuine narrowing, not full closure.

---

## 4. RDSS parameterization

For an RDSS orbit let

\[
U(s+S)=Q_*\cdot U(s),
\qquad
S=2\log\lambda,
\qquad
\lambda>1.
\]

Write the rotation holonomy in axis-angle form

\[
Q_*=\exp(S\alpha A).
\]

The pair

\[
(\lambda,\alpha)
\]

parametrizes the discrete scale-rotation step, modulo the usual angular winding ambiguity.

Pineau--Vicol remove an extreme-rotation region when

\[
\lambda
\]

is sufficiently close to `1` on their Type-I lane.

Therefore

\[
\boxed{
\text{near-identity scale step}
+
\text{extreme rotation}
\Longrightarrow
\text{trivial RDSS}
}
\]

under the external hypotheses.

---

## 5. What remains after the external theorem

The unresolved relative-periodic branch is contained in a moderate-parameter region of the schematic form

\[
\boxed{
\mathcal R_{RDSS}^{open}
\subset
\left\{
\lambda\text{ not in the certified near-1 exclusion window}
\right\}
\cup
\left\{
\alpha\text{ in the unresolved intermediate window}
\right\}.
}
\]

The precise logical union/intersection depends on the exact theorem version used; this module intentionally does not overstate the external parameter domain.

The central point is only:

\[
\boxed{
\text{M19-103 + Pineau--Vicol}
\text{ narrows RSS/RDSS but does not close all relative periodic orbits.}
}
\]

---

## 6. Relation to M19-097

M19-097 gives, under the separate one-slice regularity application gate,

\[
\boxed{
S\ge S_*>0,
\qquad
\lambda\ge e^{S_*/2}>1.
}
\]

This says a singular periodic survivor cannot have an arbitrarily small period on that lane.

The Pineau--Vicol RDSS theorem removes sufficiently near-identity scale steps under additional rotation hypotheses.

These two facts are compatible but do not automatically overlap enough to produce a contradiction: the lower bound `S_*` and the external near-identity exclusion threshold are different theorem-dependent constants.

Therefore one must not infer

\[
\boxed{
\text{M19-097 + near-1 RDSS exclusion}
\Rightarrow
\text{all RDSS excluded}.
}
\]

---

## 7. Updated critical theorem menu

Conditional on the extra-center theorem,

\[
\boxed{
\mathcal R_{critical}^{recurrent}
\Longrightarrow
\mathcal R_{RSS}^{moderate}
\lor
\mathcal R_{RDSS}^{moderate/open}.
}
\]

Hence the final periodic/relative-periodic hard core is now a **moderate-parameter Liouville problem**, not an unrestricted recurrence problem.

---

## 8. Highest-value next target

Two calculations are now natural:

1. exploit the radial weighted framework to show that the rotation generator is skew and hence isolate the exact symmetric part of the RSS/RDSS linearized operator;
2. seek a parameter-independent coercive quantity for the moderate rotation window, rather than repeatedly using small/large-rotation perturbation arguments.

---

## 9. Reference

- Ben Pineau and Vlad Vicol, *On rotated backwards self-similar solutions of the incompressible 3D Navier--Stokes equations*, arXiv:2607.09619, 2026.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
