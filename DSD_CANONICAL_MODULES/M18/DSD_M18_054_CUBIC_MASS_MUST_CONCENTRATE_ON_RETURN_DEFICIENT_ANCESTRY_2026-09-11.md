# DSD M18-054 — Cubic mass must concentrate on return-deficient ancestry

Date: 2026-09-11

Status: **R-AC SHARPENING. ON THE BOUNDED-Z RECURRENT NON-L3 CORRIDOR, THE EXISTING FINITE WEIGHTED-RETURN LEDGER AND DIVERGENT CUBIC ANNULAR MASS FORCE ANY SURVIVING BRANCH TO CONCENTRATE ITS DIVERGENT CUBIC MASS ON SHELLS WITH ARBITRARILY SMALL RETURN-TO-CUBIC RATIO. THUS FAILURE OF THE SUFFICIENT POINTWISE RETURN BOUND IS NOT AN UNSTRUCTURED ESCAPE: RETURN DEFICIENCY MUST OCCUR ON A CUBIC-MASS-DOMINANT SUBSEQUENCE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Existing inputs

On the audited bounded-normalized-enstrophy recurrent non-`L3` corridor, the repository has the divergent annular cubic ledger

\[
\boxed{
\sum_k J_k^{3/2}=\infty.
}
\]

The weighted physical return density is

\[
\boxed{
\mathfrak R_k
:=
\frac1{\rho_k}
\sum_{\ell=1}^{M_k}\tau_{k,\ell}.
}
\]

Under the already stated shell-amplitude retention, comparability, and bounded-overlap hypotheses, the physical dissipation ledger gives

\[
\boxed{
\sum_k J_k\mathfrak R_k<\infty.
}
\]

The earlier sufficient closure target was

\[
\mathfrak R_k\gtrsim J_k^{1/2}
\]

on a subset carrying divergent cubic mass.

The present module asks what must happen if this sufficient lower bound fails strongly enough for the branch to survive.

---

## 2. Normalize the return deficiency

For every `k` with `J_k>0`, define

\[
\boxed{
a_k:=\frac{\mathfrak R_k}{J_k^{1/2}}.}
\]

Then

\[
J_k\mathfrak R_k
=
a_kJ_k^{3/2}.
\]

Therefore the finite return ledger is exactly

\[
\boxed{
\sum_k a_kJ_k^{3/2}<\infty.
}
\]

This should be compared with

\[
\sum_kJ_k^{3/2}=\infty.
\]

Thus `a_k` is the exact dimensionless deficiency factor relative to the cubic-closure threshold.

---

## 3. Every fixed nondegenerate-return subset has finite cubic mass

Fix any

\[
\varepsilon>0
\]

and define

\[
G_\varepsilon
:=
\{k:a_k\ge\varepsilon\}.
\]

On this set,

\[
a_kJ_k^{3/2}
\ge
\varepsilon J_k^{3/2}.
\]

Hence

\[
\varepsilon
\sum_{k\in G_\varepsilon}J_k^{3/2}
\le
\sum_k a_kJ_k^{3/2}
<\infty.
\]

Therefore

\[
\boxed{
\sum_{k\in G_\varepsilon}J_k^{3/2}<\infty
\qquad\forall\varepsilon>0.
}
\]

So no fixed positive return ratio can carry an infinite amount of the cubic mass.

---

## 4. The return-deficient complement carries all divergent cubic mass

Define

\[
B_\varepsilon
:=
\{k:a_k<\varepsilon\}.
\]

Since the full cubic sum diverges while the complement `G_epsilon` has finite cubic mass,

\[
\boxed{
\sum_{k\in B_\varepsilon}J_k^{3/2}=\infty
\qquad\forall\varepsilon>0.
}
\]

Equivalently,

\[
\boxed{
\text{for every }\varepsilon>0,
\text{ the shells with }
\mathfrak R_k<\varepsilon J_k^{1/2}
\text{ still carry divergent cubic mass.}
}
\]

This is substantially stronger than merely saying that the pointwise return lower bound can fail.

---

## 5. Cubic-mass weighted average return ratio tends to zero

Let

\[
S_N:=\sum_{k\le N}J_k^{3/2}.
\]

Then

\[
S_N\to\infty.
\]

Define the cubic-mass weighted average

\[
\overline a_N
:=
\frac{\sum_{k\le N}a_kJ_k^{3/2}}
{\sum_{k\le N}J_k^{3/2}}.
\]

The numerator is bounded as `N->infinity`, while the denominator diverges.

Hence

\[
\boxed{
\overline a_N\to0.
}
\]

Thus the branch survives only if its ancestry return ratio vanishes **in cubic-mass density**.

This is the correct weighted statement; pointwise convergence of `a_k` for every `k` is not required.

---

## 6. Block extraction of a sharply deficient subsequence

Let

\[
\varepsilon_n\downarrow0.
\]

Because each `B_{\varepsilon_n}` has divergent cubic mass, one can choose disjoint index blocks

\[
I_n
\]

such that

\[
I_n\subset B_{\varepsilon_n}
\]

and

\[
\sum_{k\in I_n}J_k^{3/2}\ge1.
\]

Therefore along these blocks,

\[
\boxed{
\mathfrak R_k
<
\varepsilon_nJ_k^{1/2}
\qquad(k\in I_n),
}
\]

while

\[
\boxed{
\sum_n\sum_{k\in I_n}J_k^{3/2}=\infty.
}
\]

Hence any R-AC survivor contains a diagonally extractable sequence of cubic-mass-bearing blocks whose normalized return ratio tends to zero.

---

## 7. Interpretation

The old dichotomy was too coarse:

\[
\text{return bound holds}
\quad\lor\quad
\text{return bound fails}.
\]

The correct consequence of the two ledgers is

\[
\boxed{
\text{contradiction}
\quad\lor\quad
\text{divergent cubic mass is asymptotically supported on ancestry-return-deficient shells}.
}
\]

Thus R-AC has been reduced to a genuine concentration statement.

The remaining branch cannot hide most of its critical cubic mass on shells with ordinary ancestral return.

---

## 8. Relation to the age penalty

For an age-`k` shell with scale ratio

\[
K_k=q^{k/2},
\]

persistence for only a current-epoch window gives the exact loss

\[
K_k^{-2}=q^{-k}
\]

in ancestor-normalized dwell.

The present module does not assume that this current-window estimate is sharp for every actual return.

Instead it proves that if no stronger return mechanism exists, then the cubic mass must increasingly occupy precisely those shells where the realized return ratio

\[
a_k=\mathfrak R_k/J_k^{1/2}
\]

is small.

Therefore the next task is no longer to prove a uniform return bound for all shells.

It is enough to rule out a cubic-mass-divergent family with

\[
\boxed{a_k\to0\text{ in cubic-mass density}.}
\]

---

## 9. New R-AC endpoint

The ancestry-conversion root can now be sharpened from a broad return-weight deficiency to

\[
\boxed{
\mathcal R_{AC}^{def}
:
\sum J_k^{3/2}=\infty,
\qquad
\sum a_kJ_k^{3/2}<\infty,
\qquad
\overline a_N\to0.
}
\]

Equivalently, every fixed positive-return sector carries only finite cubic mass.

This is the precise sparse-return endpoint that must now be attacked.

---

## 10. Highest-value next target

The next calculation should compare `a_k` with structural age variables already present in the first-hitting genealogy.

Candidates include

- age ratio `K_k=q^{k/2}`;
- number of fresh/contact carriers;
- replacement count;
- first-hitting epoch gap;
- material radial velocity / shell-crossing action;
- local payer amplitude `J_k`.

A useful theorem would have the form

\[
\boxed{
a_k\ll1
\Longrightarrow
\text{large replacement/export/deformation action}
\lor
\text{strong age sparsity}.}
\]

Either side could then be priced by an existing root ledger.

---

## 11. Firewall

This module does not prove

\[
a_k\to0
\]

pointwise on all shells.

It proves vanishing in the measure whose mass is `J_k^{3/2}`.

It also does not prove that small return ratio is itself costly; that is the next genealogy theorem.

---

## 12. Status

\[
\boxed{
\mathcal R_{AC}\text{ SURVIVAL}
\Longrightarrow
\text{CUBIC-MASS-DOMINANT RETURN DEFICIENCY}.
}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
