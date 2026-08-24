# Cubic-Mass Genealogy Deficit Ledger

Date: 2026-08-25

Status: **ALGEBRAIC DEFICIT THEOREM PROVED UNDER THE EXISTING CONDITIONAL RETURN LEDGER / GLOBAL REGULARITY NOT PROVED.**

## 1. Scope

This note is restricted to the corrected branch

\[
\boxed{\text{bounded-}Z+\text{recurrent}+\text{non-}L^3},
\]

on which the repository has established

\[
\boxed{\sum_k J_k^{3/2}=\infty.}
\]

No use of this cubic nonsummability is made outside that branch.

We also import the weighted physical return density from
`ANCESTOR_RADIUS_IDENTITY_AND_WEIGHTED_RETURN_DENSITY_2026-08-25.md`:

\[
\mathfrak R_k
=
\frac1{\rho_k}\sum_{\ell=1}^{M_k}\tau_{k,\ell}.
\]

Under amplitude retention, tracked-shell comparability, and bounded time-overlap multiplicity, the Leray dissipation ledger gives

\[
\boxed{\sum_k J_k\mathfrak R_k<\infty.}
\]

That finite ledger remains conditional on exactly those hypotheses.

---

## 2. Return-deficit ratio

On active labels with \(J_k>0\), define

\[
\boxed{
\delta_k
:=
\frac{\mathfrak R_k}{J_k^{1/2}}.
}
\]

Then identically

\[
J_k\mathfrak R_k
=
\delta_kJ_k^{3/2}.
\]

Hence the conditional finite return ledger is

\[
\boxed{
\sum_k\delta_kJ_k^{3/2}<\infty.
}
\]

This must coexist with

\[
\sum_kJ_k^{3/2}=\infty.
\]

---

## 3. Cubic-mass deficit theorem

Fix any \(\varepsilon>0\), and split the active labels into

\[
\mathcal G_\varepsilon
:=
\{k:\delta_k\ge\varepsilon\},
\]

and

\[
\mathcal D_\varepsilon
:=
\{k:\delta_k<\varepsilon\}.
\]

On the good-return set,

\[
\varepsilon
\sum_{k\in\mathcal G_\varepsilon}J_k^{3/2}
\le
\sum_{k\in\mathcal G_\varepsilon}
\delta_kJ_k^{3/2}
\le
\sum_kJ_k\mathfrak R_k.
\]

Therefore

\[
\boxed{
\sum_{k\in\mathcal G_\varepsilon}J_k^{3/2}<\infty.
}
\]

But the total cubic mass diverges. Consequently

\[
\boxed{
\forall\varepsilon>0,
\qquad
\sum_{k\in\mathcal D_\varepsilon}J_k^{3/2}
=\infty.
}
\]

Equivalently,

\[
\boxed{
\forall\varepsilon>0,
\quad
\sum_{\mathfrak R_k<\varepsilon J_k^{1/2}}
J_k^{3/2}
=\infty.
}
\]

**Status: PROVED conditional only on the imported finite return-density ledger.**

---

## 4. Meaning of the theorem

The obstruction is stronger than merely saying that there are infinitely many weak-return labels.

For every fixed positive threshold \(\varepsilon\), the labels satisfying

\[
\mathfrak R_k\ge\varepsilon J_k^{1/2}
\]

carry only finite cubic mass.

Thus all divergent cubic mass must survive inside the arbitrarily genealogy-starved region

\[
\mathfrak R_k<\varepsilon J_k^{1/2}.
\]

In particular,

\[
\boxed{\liminf_{k\to\infty}\delta_k=0}
\]

along the active cubic-mass support.

A uniform lower bound

\[
\mathfrak R_k\ge cJ_k^{1/2}
\]

on a cubic-divergent tail is therefore incompatible with the finite return ledger, exactly as in the previous contradiction target.

---

## 5. Finite survivor partition

Now suppose that every sufficiently late deficit label is assigned to one of a finite number of exhaustive residual mechanisms.

For the current local genealogy frontier, use the abstract labels

- \(F\): far-field / enstrophy-energy tax,
- \(S\): high-vorticity sparsity or high-low segregation,
- \(P\): critical palinstrophy packet,
- \(N\): third-or-higher direction/vorticity derivative needle.

This section is purely combinatorial once such an exhaustive assignment has been justified.

Write

\[
\mathcal D_\varepsilon
=
\mathcal D_\varepsilon^F
\cup
\mathcal D_\varepsilon^S
\cup
\mathcal D_\varepsilon^P
\cup
\mathcal D_\varepsilon^N.
\]

Since

\[
\sum_{k\in\mathcal D_\varepsilon}J_k^{3/2}=\infty,
\]

at least one branch \(B(\varepsilon)\in\{F,S,P,N\}\) satisfies

\[
\boxed{
\sum_{k\in\mathcal D_\varepsilon^{B(\varepsilon)}}
J_k^{3/2}=\infty.
}
\]

Take \(\varepsilon_n=2^{-n}\). By the infinite pigeonhole principle, some fixed branch \(B_*\) occurs for infinitely many \(n\).

Because the deficit sets are nested,

\[
0<\varepsilon'<\varepsilon
\quad\Longrightarrow\quad
\mathcal D_{\varepsilon'}^{B_*}
\subset
\mathcal D_\varepsilon^{B_*},
\]

that repeated-subsequence statement upgrades to

\[
\boxed{
\forall\varepsilon>0,
\qquad
\sum_{k\in\mathcal D_\varepsilon^{B_*}}
J_k^{3/2}=\infty.
}
\]

provided the branch assignment itself is fixed label-by-label and exhaustive.

Thus finite alternation among the residual mechanisms cannot smear the divergent cubic mass so thinly that every branch becomes harmless. At least one fixed survivor must carry divergent cubic mass at arbitrarily severe return deficit.

**Status: PROVED as a finite-partition lemma; applying the specific \(F/S/P/N\) partition to every relevant ancient annular label is PROVED CONDITIONAL on the physical genealogy identification.**

---

## 6. What this removes

One can no longer argue that the unresolved genealogy may evade contradiction merely by rapidly alternating among finitely many mechanisms.

Under the branch-restricted cubic ledger and the conditional physical return ledger, there is a fixed residual mechanism \(B_*\) for which, at every return-deficit threshold,

\[
\mathfrak R_k<\varepsilon J_k^{1/2}
\]

still occurs on a set carrying divergent \(J_k^{3/2}\)-mass.

Therefore the next proof obligation may be attacked one branch at a time:

\[
\boxed{
B_*\text{ carries divergent cubic mass}
+\text{ arbitrarily small return ratio}
\stackrel{?}{\Longrightarrow}\text{ contradiction or reduction}.
}
\]

---

## 7. Strong branch-health target

For a residual branch \(B\), a sufficient closure estimate would have the form

\[
\boxed{
\mathfrak R_k
\ge
cJ_k^{1/2}\Phi_k^B,
}
\]

where \(\Phi_k^B\ge0\) is a branch-health quantity.

On the fixed branch \(B_*\) selected above,

\[
\delta_k
=\frac{\mathfrak R_k}{J_k^{1/2}}
\ge c\Phi_k^{B_*}.
\]

Hence arbitrarily small return deficit forces

\[
\Phi_k^{B_*}\to0
\]

along cubic-divergent deficit sets.

This does not yet prove any particular branch-health inequality. It converts the global closure problem into a branch-specific quantitative target.

**Status: REDUCTION TARGET / NOT YET DERIVED FOR THE PHYSICAL BRANCHES.**

---

## 8. Audit table

| Statement | Status |
|---|---|
| \(\sum J_k^{3/2}=\infty\) | PROVED only on bounded-\(Z\)+recurrent+non-\(L^3\) branch |
| \(\sum J_k\mathfrak R_k<\infty\) | PROVED CONDITIONAL on amplitude retention, tracking/comparability, bounded overlap |
| \(\sum_{\delta_k\ge\varepsilon}J_k^{3/2}<\infty\) | PROVED under the finite return ledger |
| \(\sum_{\delta_k<\varepsilon}J_k^{3/2}=\infty\) for every \(\varepsilon>0\) | PROVED under the same hypotheses |
| A finite exhaustive branch partition has one fixed branch carrying divergent cubic mass at arbitrarily small deficit thresholds | PROVED combinatorially |
| The current \(F/S/P/N\) labels are already attached rigorously to every ancient annular label | NOT DERIVED globally; conditional genealogy step |
| A branch-health lower bound \(\mathfrak R_k\gtrsim J_k^{1/2}\Phi_k^B\) is available for every branch | NOT DERIVED |
| Global regularity | UNPROVED |

---

## 9. Updated frontier

On the corrected bounded-\(Z\), recurrent, non-\(L^3\) branch, and conditional on the existing physical return-density ledger, the closure problem is reduced to the following sharper form:

\[
\boxed{
\text{there exists a fixed survivor }B_*
\text{ carrying divergent cubic mass while }
\frac{\mathfrak R_k}{J_k^{1/2}}\to0
\text{ through arbitrarily severe deficit sets.}
}
\]

The next useful calculation is therefore not another finite case split. It is to prove a quantitative return-weight lower bound for at least one of the survivor mechanisms, starting with the palinstrophy packet because it already has a local spacetime dissipation structure.