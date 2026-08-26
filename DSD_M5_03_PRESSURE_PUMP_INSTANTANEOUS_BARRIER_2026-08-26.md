# DSD M5-03 — Pressure-Pump Instantaneous Barrier

Date: 2026-08-26

Status: **M5 SUBSTEP / INSTANTANEOUS PRESSURE-PUMP ABSORPTION IS NOT A NEW CLOSURE ROUTE / NORM-ONLY ESTIMATES REDUCE TO THE EXISTING SMALL-CRITICAL-TAIL HYPOTHESIS / PURE SNAPSHOT SIGN DOMINATION IS NOT AVAILABLE WITHOUT NEW DYNAMIC INFORMATION / GLOBAL REGULARITY UNPROVED.**

## 1. Canonical M5 setting

The live proof stack is

\[
M0\to M1\to M2\leftrightarrow M3\stackrel{M5}{\longrightarrow}M4.
\]

M4 is already proved: one uniformly small physical high-amplitude weak-\(L^3\) tail implies \(H^1\) control and continuation.

M5 must therefore force that small-tail regime from the retained finite-energy/W1 structure.

This note asks whether the strict interior amplitude pressure pump can do that by an **instantaneous** estimate.

---

## 2. Existing critical pressure estimate

For the W1 endpoint,

\[
F_P=\int P\,U\cdot\nabla|U|\,dY
\]

and the repository has the critical Lorentz estimate

\[
\boxed{
|F_P|\le C\,\|U\|_{L^{3,\infty}}\,D_3.
}
\]

The same scaling persists after finite-parent/high-amplitude localization: pressure work is bounded by a critical tail-size factor times the corresponding critical viscous cost, plus lower-order/localization errors.

Hence an estimate of the form

\[
|F_{P,\mathrm{high}}|\le \theta\nu D_{3,\mathrm{high}},
\qquad \theta<1,
\]

obtained solely through Calderon--Zygmund/Lorentz norm bounds requires the high-amplitude weak-\(L^3\) factor itself to be below a viscosity-dependent threshold.

But that is precisely the hypothesis already sufficient in M4.

Therefore

\[
\boxed{
\text{norm-only instantaneous pressure absorption}
\Longrightarrow
\text{M4 small-tail hypothesis is assumed rather than derived}.
}
\]

This route is logically circular as an M5 proof.

---

## 3. Why a universal snapshot sign inequality is not available from the current structure

The exact cubic balance is

\[
\frac{d}{dt}\int |u|^3dx+3\nu D_3=3\Pi_3,
\qquad
\Pi_3=\int p\,u\cdot\nabla|u|\,dx.
\]

No sign is built into \(\Pi_3\).

The repository's asymmetric smooth divergence-free benchmark produces numerically stable positive and negative values of \(\Pi_3\) after reflection. This remains a **computational check**, not a theorem-level analytic counterexample.

For any fixed shape for which \(\Pi_3(u)>0\), amplitude homogeneity gives

\[
D_3(Au)=A^3D_3(u),
\qquad
\Pi_3(Au)=A^4\Pi_3(u).
\]

Thus a universal pointwise-in-time inequality

\[
\Pi_3\le \nu D_3
\]

would be incompatible with such a positive-pressure shape for sufficiently large amplitude.

Because the positivity of the benchmark is presently numerical, this is retained as a **conditional/algebraic barrier**, not as a completed impossibility theorem.

---

## 4. DSD audit conclusion

The pressure pump can be split into two logically different questions.

### Snapshot question

Can one bound the pressure pump by viscosity at one time using only instantaneous critical norms?

Current answer:

\[
\boxed{
\text{not without reintroducing the small-tail hypothesis or another equally strong critical condition.}
}
\]

### History question

Can a finite-energy Navier--Stokes trajectory repeatedly rebuild the strict interior pressure-pump cell at successively larger physical amplitudes while remaining in the large weak-critical corridor?

This is not answered by the snapshot estimate.

Therefore the only non-circular pressure route left inside M5 is

\[
\boxed{
\textbf{dynamic pressure-pump nonrepeatability / history-dependent absorption}.
}
\]

Such a theorem would have to use more than Calderon--Zygmund norm size. It must exploit at least one genuinely dynamical/global ingredient, for example:

- pressure-pump lineage across successive amplitude scales;
- incompatibility of repeated inflow/outflow pressure gaps with a finite-energy ancestor history;
- a defect-aware compactness principle linking the pump history to the \(K\)-boundary coordinate;
- a scale-breaking invariant or monotone quantity not already exhausted by the energy/dissipation budgets.

---

## 5. Relation to existing pressure regularity criteria

Published pressure criteria show that sufficiently small pressure on high-velocity regions can imply regularity. Such results are consistent with the M4/M5 architecture, but they impose a pressure/tail smallness hypothesis; they do not derive it from finite energy alone.

Thus they are external anchors for the **conclusion side** of M5, not a proof of the missing implication.

---

## 6. M5 decision after this substep

M5-01: energy/dissipation gives only time-average tail decay; spikes remain possible.

M5-02: ordinary parabolic persistence is too short to contradict that average budget.

M5-03: instantaneous pressure-pump absorption is either circular (norm-only) or requires a new sign/dynamic theorem not presently available.

Therefore the next nonredundant substep should examine

\[
\boxed{
\textbf{defect-aware critical compactness / inter-scale lineage}
}
\]

rather than another instantaneous pressure inequality.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
