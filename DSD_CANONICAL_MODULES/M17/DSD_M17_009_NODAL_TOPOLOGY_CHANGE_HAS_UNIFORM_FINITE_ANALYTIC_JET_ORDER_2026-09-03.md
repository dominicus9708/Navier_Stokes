# DSD M17-009 — Nodal topology change has a uniform finite analytic jet order

Date: 2026-09-03
Canonical ID: **M17-009**

Status: **INTERNAL ANALYTIC COMPACTNESS REDUCTION / REGULAR CODIMENSION-TWO WINDING FILAMENTS ARE MATERIAL BY M17-007, SO TOPOLOGY CHANGE REQUIRES A DEGENERATE NODAL EVENT. ON THE COMPACT SMOOTH/ANALYTIC HARD HULL, SUCH NODAL EVENTS CANNOT HAVE UNBOUNDED VANISHING ORDER: OTHERWISE A `C^infty` LIMIT WOULD HAVE ALL SPATIAL JETS OF `W` ZERO AT ONE POINT, AND SPATIAL ANALYTICITY WOULD FORCE THE LIMIT STATE TO VANISH IDENTICALLY, CONTRADICTING THE MARKED NONZERO COMPONENT. HENCE THERE IS A UNIFORM FINITE JET ORDER `m_*` AND A UNIFORM NONZERO JET FLOOR AT EVERY RELEVANT NODAL DEGENERACY / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Nodal-degenerate branch

M17-007 gives

\[
\boxed{
\text{winding topology change}
\Longrightarrow
\operatorname{rank}(\nabla u,\nabla v)<2
}
\]

at a common zero

\[
f=u+iv=0.
\]

We call such an event a degenerate nodal event.

The question is whether arbitrarily high-order flattening of the analytic field can be used to evade a finite classification.

---

## 2. Vanishing order

For a nonzero analytic vector field `W` at a zero `p`, define the spatial vanishing order

\[
\operatorname{ord}_pW
:=\min\{m\ge1:\exists |\alpha|=m,\ \partial^\alpha W(p)\neq0\}.
\]

Every nontrivial analytic state has finite order at every point.

We now show that the order is **uniformly bounded** on the compact marked hard hull inside a fixed finite core.

---

## 3. Contradiction argument for unbounded order

Assume no uniform finite bound exists.

Then there are states `W_n` in the compact hard hull and nodal points `p_n` in a fixed compact core such that

\[
\operatorname{ord}_{p_n}W_n\to\infty.
\]

By compactness, after a subsequence,

\[
W_n\to W_\infty
\]

in `C^m` on the core for every fixed finite `m`, and

\[
p_n\to p_\infty.
\]

Fix any derivative order `m`. For all sufficiently large `n`,

\[
\partial^\alpha W_n(p_n)=0
\qquad
\text{for every }|\alpha|\le m.
\]

Passing to the limit,

\[
\partial^\alpha W_\infty(p_\infty)=0
\qquad
\text{for every }|\alpha|\le m.
\]

Since `m` was arbitrary,

\[
\boxed{
\partial^\alpha W_\infty(p_\infty)=0
\quad\forall\alpha.
}
\]

Spatial analyticity then gives

\[
\boxed{W_\infty\equiv0}
\]

on the connected whole space.

But the retained marked component excludes the zero state.

Contradiction.

Therefore

\[
\boxed{
\exists m_*<\infty:
\quad
\operatorname{ord}_pW\le m_*
}
\]

for every relevant nodal point in the fixed hard core.

---

## 4. Uniform nonzero jet floor

Compactness also upgrades finite order to a quantitative lower bound.

If no uniform jet floor existed, there would be states/points with

\[
\max_{1\le m\le m_*}|\nabla^mW(p)|\to0.
\]

Taking a compact limit would give a nodal point in the limit state where all derivatives through order `m_*` vanish, contradicting the definition of the uniform order bound.

Thus there exists

\[
\boxed{c_{jet}>0}
\]

such that at every nodal point in the relevant class,

\[
\boxed{
\max_{1\le m\le m_*}|\nabla^mW(p)|\ge c_{jet}.
}
\]

At a degenerate nodal event the first-derivative rank is `< 2`; therefore if the first derivative does not already classify the event, some higher jet with order `2 <= m <= m_*` carries the fixed nonzero geometry.

---

## 5. Finite analytic nodal models

Real-analytic zero sets admit local stratification by finite jets.

The uniform pair

\[
(m_*,c_{jet})
\]

means that the hard survivor cannot evade classification by using an infinite sequence of flatter and flatter winding reconnection events.

Every topology-changing event belongs to a finite-order family such as:

1. rank-one first-derivative nodal fold;
2. quadratic nodal merger/splitting;
3. finite higher-order cusp/branch event with order `<= m_*`.

The exact list may require a finer singularity classification, but **infinite-order flat nodal turnover is removed**.

---

## 6. Positive-rate topology turnover consequence

If the recurrent rank-one branch changes winding topology with positive asymptotic time density, then by finite pigeonhole there exists at least one finite jet type `J_*` that occurs with positive density and a uniform nonzero derivative floor.

Hence

\[
\boxed{
T_{nodal}^{deg}
\Longrightarrow
\text{positive-density finite-order coherent nodal-jet events}.
}
\]

This is structurally analogous to the finite-order critical-sheet reduction in M14.

---

## 7. DSD firewall

A finite-order nodal-jet event is still an **unsigned** analytic-geometry event. M16-016 warns that positive-density unsigned charges alone do not contradict compact recurrence.

Thus M17-009 does not close the nodal-turnover branch.

The gain is that all remaining topology change is now finite-order and can be coupled to the exact vorticity/material equations without an infinite singularity hierarchy.

---

## 8. Updated rank-one frontier

\[
\boxed{
R_1^{great-circle}
\Longrightarrow
R_{nodal}^{material}
\ \lor\ 
T_{nodal}^{finite-jet}
\ \lor\ 
G_{nonaxis}^{rank1}.
}
\]

- `R_nodal^material`: regular winding filaments transported materially.
- `T_nodal^{finite-jet}`: topology-changing nodal events of uniformly bounded analytic order.
- `G_nonaxis^{rank1}`: persistent non-axisymmetric great-circle structure without nodal topology change.

The next closure step must distinguish the regular/no-swirl-like material-filament class from the genuinely non-axisymmetric class using the semilinear 2.5D system of M17-004.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
