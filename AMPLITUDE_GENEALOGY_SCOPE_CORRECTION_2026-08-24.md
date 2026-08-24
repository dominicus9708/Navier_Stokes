# Amplitude-Genealogy Scope Correction — 2026-08-24

## Status

**AUDIT CORRECTION — PROVED FROM THE CURRENT REPOSITORY DEPENDENCY CHAIN.**

This note corrects a scope leak between

- `ANTI_PROOF_CORRECTED_GLOBAL_FRONTIER_2026-08-24.md`, and
- `AMPLITUDE_SENSITIVE_HISTORICAL_GENEALOGY_GATE_2026-08-24.md`.

It does **not** establish global regularity.

---

## 1. The source statement is branch-restricted

The anti-proof-corrected frontier derives the annular cubic obstruction in its bounded-`Z` branch. In that branch a non-`L^3` recurrent state necessarily satisfies

\[
\sum_k J_k^{3/2}=\infty.
\]

The logical form is therefore

\[
\boxed{
\text{bounded-}Z
+\text{ recurrent}
+\text{ non-}L^3
\Longrightarrow
\sum_k J_k^{3/2}=\infty.
}
\]

No repository step preceding the amplitude-sensitive genealogy note upgrades this implication to every surviving ancient/Morrey branch.

---

## 2. The later genealogy note dropped the hypothesis

Section 6 of `AMPLITUDE_SENSITIVE_HISTORICAL_GENEALOGY_GATE_2026-08-24.md` imports

\[
\sum_k J_k^{3/2}=\infty
\]

as a general necessary condition, without retaining the bounded-`Z` hypothesis.

Therefore every later arithmetic shell-selection conclusion in that note that uses this nonsummability inherits a missing hypothesis.

---

## 3. Corrected scope

The valid statement is

\[
\boxed{
\text{on the bounded-}Z\text{ non-}L^3\text{ recurrent branch,}
\quad
\sum_k J_k^{3/2}=\infty.
}
\]

Consequently, amplitude-sensitive shell selections based on this ledger are presently valid only on that branch.

In particular, statements of the form

\[
\text{for every }C>0,
\quad
\text{the shells with sufficiently large amplitude-weighted cost carry divergent cubic mass}
\]

must be read with the prefix

\[
\boxed{\text{bounded-}Z\text{ non-}L^3\text{ recurrent branch}.}
\]

---

## 4. What survives unchanged

The following parts of the amplitude-sensitive genealogy construction are not invalidated by this scope correction:

1. physical-shell definitions;
2. first-hitting-time bookkeeping;
3. historical-ancestor definitions;
4. the need for a Galilean/relative formulation;
5. purely algebraic implications proved after explicitly assuming cubic nonsummability.

What changes is the domain on which cubic nonsummability is currently available.

---

## 5. What is still missing on the broader branch

For an unbounded-`Z` / broader local-energy-Morrey ancient branch, one still needs one of the following:

1. an independent derivation of an analogous cubic nonsummability ledger;
2. a reduction of that branch to bounded `Z`;
3. a different Liouville/compactness obstruction that bypasses this ledger.

Until one of these is proved, the amplitude-sensitive arithmetic selection cannot be promoted to a universal surviving-tail theorem.

---

## 6. Audit labels

| Claim | Status |
|---|---|
| The cubic nonsummability statement occurs on the bounded-`Z` branch in the corrected frontier | **PROVED / repository audit** |
| The later amplitude-genealogy note omits that qualifier in its import | **PROVED / repository audit** |
| Its downstream shell-selection conclusions remain valid on bounded-`Z` after restoring the qualifier | **PROVED / logical repair** |
| The same cubic ledger holds on every unbounded-`Z` Morrey branch | **NOT DERIVED** |
| This correction closes global regularity | **FALSE** |

---

## 7. Corrected proof-tree position

The active tree is now

\[
\text{hypothetical singularity}
\Longrightarrow
\begin{cases}
\text{bounded-}Z\text{ recurrent branch}
\Rightarrow
\text{cubic nonsummability + amplitude genealogy},\\[1mm]
\text{unbounded-}Z\text{ / Morrey branch}
\Rightarrow
\text{separate compactness/Liouville gate still required}.
\end{cases}
\]

This is a narrowing of the claimed scope, not a loss of the bounded-`Z` calculation.