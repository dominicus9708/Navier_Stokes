# DSD M5-658 — High-amplitude cross-sheet patching requires force rotation or a kappa-critical branch set

Date: 2026-09-03

Status: **INTERNAL LOCALIZATION / M5-657 REDUCES THE PERSISTENT RELABELING SURVIVOR TO A HIGH-AMPLITUDE CONNECTED COMPONENT IN WHICH THE PERSISTENT REFERENCE AND ITS STRONGLY-NEGATIVE PAYER CANNOT BE CONTINUED THROUGH ONE COMMON SCALAR LAW / ON ANY CONNECTED REGULAR CORRIDOR WITH `rho>a0`, `grad kappa != 0`, AND `grad kappa x grad h=0`, THE LOCAL RELATION `h=f(kappa,theta)` CONTINUES UNIQUELY ALONG THE CORRIDOR, SO A CHANGE OF RELABELING SHEET MUST CROSS EITHER A FORCE-ROTATION REGION `grad kappa x grad h !=0` OR AN ACTIVE KAPPA-CRITICAL SET `grad kappa=0` / AT A CRITICAL POINT, NONZERO `grad h` IS THE M5-654 FORCE-CREATION BRANCH, WHILE `grad h=0` IS THE ONLY DIFFERENTIAL-SILENT ANALYTIC BRANCH-POINT SURVIVOR / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Setup from M5-657

Fix one persistent fixed-flux lineage `L` at one retained similarity time.

M5-657 gives a connected component

\[
C_L\subset\{\rho>a_0\}
\]

containing both:

1. the persistent carrier of `L`;
2. a coherent strongly-negative payer packet `P_L^-` with

\[
\kappa\le-\kappa_0/2.
\]

If both belong to one common relabeling-law family, M5-648--649 close the corridor.

Hence the only survivor is that the local scalar law changes somewhere inside the connected high-amplitude component.

Write

\[
\boxed{h:=D_B\kappa.}
\]

---

## 2. Regular local relabeling criterion

On an active regular set where

\[
\rho>a_0,
\qquad
\nabla\kappa\ne0,
\]

suppose

\[
\boxed{\nabla\kappa\times\nabla h=0.}
\]

Then `h` is locally constant along each connected `kappa` level surface.

By the implicit-function theorem, `kappa` is a local coordinate transverse to the level surfaces, and there exists a local scalar function

\[
\boxed{h=f(\kappa,\theta).}
\]

This is exactly the ordinary relabeling branch of M5-627.

---

## 3. Continuation along a connected regular corridor

Let `Gamma` be a continuous path inside `C_L` joining two points and suppose a tubular neighborhood of `Gamma` satisfies

\[
\nabla\kappa\ne0,
\qquad
\nabla\kappa\times\nabla h=0.
\]

Cover `Gamma` by finitely many overlapping implicit-function neighborhoods `U_j`.

On each `U_j`,

\[
h=f_j(\kappa,\theta).
\]

On a nonempty overlap `U_j cap U_{j+1}`, both expressions represent the same analytic/smooth scalar field `h` as a function of the same regular coordinate `kappa`, so they agree on the overlap interval of `kappa` values.

Therefore the scalar law continues uniquely from one patch to the next along `Gamma`.

Hence:

\[
\boxed{
\text{a connected regular corridor with zero force rotation cannot change relabeling-law family.}
}
\]

No global single-valued law over all of `C_L` is claimed; this is a pathwise continuation statement.

---

## 4. Consequence for M5-657 cross-sheet patching

Take any path in `C_L` from the persistent carrier to the strongly-negative payer.

If the two endpoints lie on genuinely different relabeling sheets, the path cannot remain entirely inside the regular zero-rotation set.

Therefore every such sheet-changing path meets at least one of

\[
\boxed{
R_{force}:\quad
\nabla\kappa\times\nabla h\ne0,
}
\]

or

\[
\boxed{
K_{crit}:\quad
\nabla\kappa=0.
}
\]

Because `rho>a0` throughout `C_L`, these are high-amplitude events; nodal degeneracy is absent.

---

## 5. Quotient-free form of the regular branch

M5-654 defines

\[
F=\rho^2\nabla\kappa.
\]

On `rho>a0`,

\[
\nabla\kappa\times\nabla h\ne0
\]

is equivalent to

\[
\boxed{
\mathcal C_\kappa
=
F\times(D_BF+L^TF)
\ne0.
}
\]

Thus the regular sheet-change branch is exactly the already identified generalized-force rotation branch.

---

## 6. Critical-point split

At an active critical point,

\[
\rho>a_0,
\qquad
\nabla\kappa=0,
\]

one has

\[
F=0.
\]

M5-654 gives

\[
\boxed{
D_BF=\rho^2\nabla h.
}
\]

Therefore:

### 6.1 Critical force creation

If

\[
\nabla h\ne0,
\]

then

\[
\boxed{F=0,\qquad D_BF\ne0,}
\]

which is the critical generalized-force creation branch.

### 6.2 Differential-silent critical branch point

The only critical patch not detected at first differential order satisfies

\[
\boxed{
\nabla\kappa=0,
\qquad
\nabla h=0.
}

Call this

\[
\boxed{K_{silent}.}
\]

Analytic pairs can genuinely have multi-valued scalar relations across such a point. A one-dimensional model is

\[
\kappa=x^2,
\qquad
h=x^3,
\]

for which the two sides give

\[
h=\pm\kappa^{3/2}.
\]

Thus `K_silent` cannot be discarded merely by first-order differential calculus.

---

## 7. Sharpened M5-657 frontier

The high-amplitude cross-sheet branch is therefore localized to

\[
\boxed{
T_{high-amplitude\ cross-sheet}
\Longrightarrow
C_{rot}^{force}
\lor
C_{crit}^{force}
\lor
K_{silent}^{analytic\ branch}.
}
\]

The first two are genuine dynamical generalized-force events.

The third is a high-amplitude analytic critical branch set at which both first gradients vanish and different local scalar-law branches may still meet.

---

## 8. Important firewall: patching is not yet material transfer

The existence of different scalar-law sheets inside one amplitude component does **not** by itself mean that vorticity or material labels physically cross from one sheet to another.

The strongly-negative payer can coexist on another sheet and couple to the persistent carrier through the global elliptic/Biot-Savart structure.

Therefore terms such as `cross-sheet transfer tax` must not be used unless an actual transport or finite-resource flux between sheet populations is proved.

The rigorous statement at this stage is only a **sheet-patching localization**.

---

## 9. Next target

The only differential-silent patching survivor is

\[
\boxed{
\rho>a_0,
\qquad
\nabla\kappa=0,
\qquad
\nabla(D_B\kappa)=0.
}
\]

The next calculation should use the CE-H elliptic relation

\[
\Delta W=\kappa W
\]

and the material compatibility equations to determine what second- and higher-order jets are required for such an analytic branch point, and whether repeated high-amplitude branch points force a quantitative Hessian/jet charge.

---

## 10. Audit classification

This document does not close the cross-sheet branch.

It removes regular silent patching and isolates the only silent possibility to an active analytic critical branch set.

No claim is made that critical points themselves are rare enough to contradict recurrence.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]