# DSD M5-650 — Audit correction: single-law relabeling is closed, but multi-sheet patching remains

Date: 2026-09-03

Status: **DSD AUDIT CORRECTION / M5-648--649 VALIDLY CONTRADICT EVERY CONNECTED RELABELING REGION ON WHICH ALL RELEVANT MATERIAL KAPPA LEVELS ARE GOVERNED BY ONE COMMON SCALAR ODE `D_B kappa=f(kappa,theta)`, BUT M5-627 EXPLICITLY WARNED THAT `nabla h parallel nabla kappa` ONLY GIVES THIS LAW LOCALLY ON CONNECTED REGULAR LEVEL-SET REGIONS / DISCONNECTED COMPONENTS OF THE SAME KAPPA LEVEL MAY IN PRINCIPLE CARRY DIFFERENT LOCAL RELABELING LAWS, SO THE CLAIM IN M5-649 THAT THE ENTIRE RELABELING BRANCH IS ELIMINATED IS TOO STRONG / THE CORRECT FRONTIER IS TRANSVERSE CROSS-LEVEL FORCING OR MULTI-SHEET RELABELING/PATCH-TRANSFER / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. What M5-627 actually proved

M5-627 defined

\[
h:=D_B\kappa
\]

and showed that on CE-H

\[
W\cdot\nabla\kappa=0,
\qquad
W\cdot\nabla h=0.
\]

If on a connected regular quotient region

\[
\nabla h\parallel\nabla\kappa,
\]

then `h` is constant on each connected `kappa` level surface and locally

\[
\boxed{
h=f(\kappa,\theta).
}
\]

Thus

\[
D_B\kappa=f(\kappa,\theta)
\]

holds on that connected relabeling sheet.

M5-627 explicitly retained the firewall that disconnected level components require patching and do not automatically share one global single-valued `f`.

---

## 2. What M5-648--649 validly close

On one connected single-law relabeling sheet, scalar ODE uniqueness preserves order between all material level histories governed by that same `f`.

M5-648 closes the synchronized zero-level case

\[
c_*\equiv0
\]

through finite irreversible absolute-flux consumption.

M5-649 closes the synchronized nonzero zero-mean case

\[
\langle c_*\rangle=0,
\qquad
c_*\not\equiv0
\]

through bounded reference-flux normalization and irreversible relative-flux consumption.

Therefore the following statement is valid:

\[
\boxed{
\text{one connected common-law persistent relabeling sheet}
\Longrightarrow\bot.
}
\]

---

## 3. The overreach in M5-649

M5-649 concluded

\[
R_{relabel}\Longrightarrow\bot.
\]

without retaining the connected-sheet qualification.

This is stronger than M5-627 supports.

A real-analytic scalar pair can satisfy

\[
dh\wedge d\kappa=0
\]

locally while two disconnected components of the same `kappa` value carry different local branches of `h` as a function of `kappa`.

Thus one may have a collection of relabeling sheets

\[
\mathscr S_1,\mathscr S_2,\ldots
\]

with local laws

\[
D_B\kappa=f_a(\kappa,\theta)
\quad\text{on }\mathscr S_a,
\]

without one global `f`.

No contradiction has yet been derived merely from the existence of such a patched structure.

---

## 4. Corrected quotient frontier

Let

\[
\mathcal A_\kappa
:=
\nabla\kappa\times\nabla(D_B\kappa).
\]

Then at regular points:

- `A_kappa != 0` is genuine cross-level acceleration and prevents even local scalar relabeling;
- `A_kappa = 0` gives local single-sheet relabeling, but global patching may remain multi-valued across disconnected level components.

Since every single common-law persistent sheet is now closed, the correct CE-H quotient frontier is

\[
\boxed{
E_{CEH}
\Longrightarrow
F_{cross-level}
\lor
R_{multi-sheet/patch-transfer}.
}
\]

This replaces the overstrong M5-649 statement.

---

## 5. Why multi-sheet relabeling is not a cosmetic topology issue

The M5-649 relative-flux argument compares a lower level against one persistent reference solution `c_*(theta)` using the same scalar ODE.

If another packet belongs to a different sheet with another law `f_b`, order relative to `c_*` need not be preserved by scalar uniqueness because the two trajectories solve different ODEs.

Hence the relative multiplier

\[
\kappa-c_*
\]

can change sign without crossing the reference solution of the same equation.

This is precisely a possible recharge mechanism for material flux.

Therefore multi-sheet patching is a genuine dynamical survivor, not merely a notational inconvenience.

---

## 6. Natural way to remove quotient singularities

Define smooth scalar fields

\[
a:=|W|^2,
\qquad
b:=W\cdot\Delta W.
\]

On `a>0`,

\[
\kappa=\frac ba.
\]

Define

\[
K:=a\nabla b-b\nabla a.
\]

Then

\[
\boxed{
K=a^2\nabla\kappa.
}
\]

Let

\[
H:=aD_Bb-bD_Ba.
\]

Since `b=kappa a`,

\[
\boxed{
H=a^2D_B\kappa=a^2h.
}
\]

Finally define

\[
M:=a\nabla H-2H\nabla a.
\]

Then

\[
\boxed{
M=a^3\nabla h.
}
\]

Hence the smooth quotient-free cross-level vector

\[
\boxed{
\mathfrak A
:=K\times M
=a^5\left[\nabla\kappa\times\nabla(D_B\kappa)\right]
}
\]

on `a>0`.

`mathfrak A` remains globally smooth through the nodal set because it is built polynomially from `W`, `Delta W` and their derivatives/material derivatives.

This is the natural observable for the forced branch.

---

## 7. Multi-sheet branch as a patch-transfer problem

If

\[
\mathfrak A\equiv0
\]

on a region, each connected regular component has a local relabeling law.

Since no one such persistent common-law sheet can support the complete recurrent mechanism indefinitely, a surviving patched branch must repeatedly do at least one of:

1. transfer active fixed-flux population between distinct relabeling sheets;
2. pass through a critical/nodal patch where the local level-sheet parametrization changes;
3. merge/split connected `kappa` level components.

Thus

\[
\boxed{
R_{multi-sheet}
\Longrightarrow
T_{sheet-transfer/critical-patching}.
}
\]

The next calculation should determine whether such transfer is already a fixed projective/viscous replacement event under M5-488, or whether it creates a genuinely new topological quotient event.

---

## 8. Audit classification

For final reconstruction:

- retain M5-648 in full;
- retain M5-649 as the closure of a **connected common-law** nonzero synchronized relabeling sheet;
- override only M5-649 Section 10's global statement `R_relabel -> contradiction`;
- use the corrected split

\[
F_{cross-level}\lor R_{multi-sheet/patch-transfer}.
\]

No exact material flux identities are changed.

---

## 9. Updated highest-value targets

### Q1 — multi-sheet transfer

Show that positive-frequency transfer between disconnected relabeling sheets necessarily entails one of the already priced finite-memory events:

\[
\text{viscous flux change}
\lor
\text{projective/noncoherent reorganization}
\lor
\text{coherent replacement}.
\]

### Q2 — forced branch

Use the quotient-free vector `mathfrak A` to derive an invariant positive activity or signed balance and compare it with the generalized-kappa-force tensor virial from M5-625--626.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]