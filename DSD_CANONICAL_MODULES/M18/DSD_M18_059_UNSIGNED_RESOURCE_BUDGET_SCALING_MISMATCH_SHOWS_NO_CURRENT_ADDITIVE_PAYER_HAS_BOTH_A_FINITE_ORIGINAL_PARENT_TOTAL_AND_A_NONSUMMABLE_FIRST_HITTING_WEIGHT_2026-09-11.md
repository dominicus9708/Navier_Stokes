# M18-059 — Unsigned resource budget-scaling mismatch: no current additive payer has both a finite original-parent total and a nonsummable first-hitting weight

**Date:** 2026-09-11  
**Status:** AC UNSIGNED-PAYER NO-GO / HOMOGENEITY CLASSIFICATION / BUDGET-SCALING FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-058 shows that the apparent positive-\(R\) standard-energy gain of a second-generation record is canceled by the shrinking first-generation base scale when the event is mapped back to the original physical solution:

\[
r_jR_m=r_{j-m}.
\]

The present module asks a more general question.

Is there any **currently available unsigned additive resource** that simultaneously has

1. a finite total on the original finite-energy physical parent;
2. a nonsummable weight on the geometric first-hitting scale ladder;
3. a fixed positive normalized payment on the retained singular branch?

The answer, for the resources presently certified in the repository, is no.

## 2. General homogeneous resource exponent

Let \(Q\) be a normalized spacetime resource whose physical-parent charge under a length normalization \(r\) obeys

\[
\boxed{
Q^{phys}=r^\beta Q^{norm}.
}
\]

On the geometric first-hitting ladder

\[
r_n\asymp q^{-n/2},
\qquad q>1,
\]

a fixed normalized payment

\[
Q_n^{norm}\ge c_*>0
\]

has physical cost

\[
Q_n^{phys}\gtrsim c_*q^{-\beta n/2}.
\]

Thus the sign of \(\beta\) determines the native accumulation behavior.

## 3. Three homogeneity regimes

### A. \(\beta>0\): ancestry-cheap

Then

\[
\sum_n r_n^\beta<\infty.
\]

Hence a fixed normalized event at every stage can be paid by a finite parent total.

No contradiction follows from positive frequency alone.

### B. \(\beta=0\): scale-critical additive budget

A fixed normalized event has a fixed physical cost.

If a genuinely finite additive parent total existed, infinitely many nonreused events would immediately contradict it:

\[
\sum_n c_*=\infty.
\]

This is the ideal unsigned-payer homogeneity.

### C. \(\beta<0\): ancestry-expensive

Fixed normalized payments become more expensive at finer scales:

\[
r_n^\beta\to\infty.
\]

But a contradiction requires a finite original-parent total for that resource.

Without such a budget, the large event cost is not useful.

## 4. Derivative family

For

\[
q_k
=
\int\|D^k\Omega\|_2^2dt,
\]

exact Navier--Stokes scaling gives

\[
\boxed{
\beta_k=1-2k.
}
\]

Thus

\[
\begin{array}{c|c|c}
k&\beta_k&\text{own-scale physical weight}\\
\hline
0&+1&r\\
1&-1&r^{-1}\\
2&-3&r^{-3}\\
3&-5&r^{-5}
\end{array}
\]

This table explains the persistent mismatch between standard energy and higher derivative payers.

## 5. Spacetime enstrophy / kinetic-energy dissipation

For \(k=0\),

\[
q_0
=
\int\|\Omega\|_2^2dt
=
\int\|\nabla u\|_2^2dt
\]

in the whole-space divergence-free setting.

The original finite-energy solution supplies a finite total through the kinetic-energy identity:

\[
\boxed{
\int_0^{T_*}\|\Omega(t)\|_2^2dt<\infty.
}
\]

But

\[
\beta_0=1>0.
\]

Therefore a fixed normalized event has cost

\[
r_n c_*
\]

and

\[
\sum_nr_nc_*<\infty.
\]

This resource has the finite budget but the wrong homogeneity for fixed-cost accumulation.

## 6. Palinstrophy

For

\[
q_1
=
\int\|\nabla\Omega\|_2^2dt,
\]

\[
\beta_1=-1.
\]

Thus a fixed own-scale normalized event would have physical cost

\[
r_n^{-1}c_*,
\]

which is strongly nonsummable.

However the original hypothetical singular solution is not known to satisfy

\[
\int_0^{T_*}\|\nabla\Omega\|_2^2dt<\infty.
\]

Indeed such a finite total is part of what a singularity may fail to preserve.

M5-477 proves finite total palinstrophy only for the **first marked ancient element**, whose second-generation record accounting carries the inverse record weight

\[
R_m^{-1}.
\]

That ledger is summable for fixed cell payments.

Thus palinstrophy has favorable physical homogeneity but no finite original-parent budget.

## 7. Raw-H2 and D3

Similarly,

\[
q_2
=
\int\|D^2\Omega\|_2^2dt,
\qquad
\beta_2=-3,
\]

and

\[
q_3
=
\int\|D^3\Omega\|_2^2dt,
\qquad
\beta_3=-5.
\]

Their own-scale physical costs grow even faster.

But no finite original-parent total for these resources is certified for a hypothetical singular solution.

Where finite first-generation ancient totals are proved, the corresponding second-generation ancestry weights are

\[
R_m^{-3},
\qquad
R_m^{-5},
\]

and fixed normalized payments remain summable.

Thus increasing derivative order does not repair the budget-scaling mismatch.

## 8. Instantaneous kinetic energy

The kinetic energy

\[
\|u(t)\|_2^2
\]

is globally finite and nonincreasing for the original finite-energy solution.

However it is a **state quantity**, not an additive event charge.

The same kinetic-energy budget may be present at infinitely many times without being consumed anew.

Therefore repeated recurrence cannot be summed as

\[
\sum_j\|u(t_j)\|_2^2.
\]

It does not supply the missing additive scale-critical payer.

## 9. Material vorticity flux / finite label storage

The persistent vorticity flux used in the material-lineage architecture is scale critical.

But recurrence of the same label does not create a new additive flux amount.

Finite-label storage only prices

- genuinely new labels;
- replacement;
- export/reformation events.

Once a finite persistent network is saturated, ordinary recurrence is reuse rather than additive cost.

Hence material flux is scale critical but not an additive parent budget for repeated same-lineage events.

## 10. Absolute boundary work

M18-044 produces the absolute boundary-work payer

\[
\mathscr B
=
\int|F_w|ds.
\]

This is additive across disjoint event windows and can be order one in normalized units.

But the repository has no certified universal finite total of absolute moving-boundary work on the original parent.

Signed boundary flux can cancel, while the absolute action may be arbitrarily larger.

Thus boundary work has an event currency but no current finite parent budget.

## 11. Critical velocity norms

The scale-critical quantities

\[
\|u\|_{L^3},
\qquad
\|u\|_{L^{3,\infty}}
\]

have attractive homogeneity \(\beta=0\) at the snapshot level.

But they are not additive time-consumed resources.

Moreover the hard recurrent terminal branch deliberately permits or forces global \(L^3\) failure, while weak-\(L^3\) boundedness belongs to a conditional W1 corridor rather than a finite monotone total.

Thus critical norms do not currently supply the desired additive parent budget.

## 12. Return-density / genealogy charges

Physical weighted-return and residence ledgers can possess finite totals under appropriate genealogy hypotheses.

However M17-117 and M18-045/048 show that current-epoch recurrence loses ancestral weight through factors such as

\[
K_k^{-2}.
\]

The resulting fixed own-scale events are ancestry-cheap unless a separate return-density amplification theorem is proved.

This is another manifestation of the same budget-scaling mismatch.

## 13. Current resource table

\[
\boxed{
\begin{array}{l|c|c|c}
\text{resource}&\text{finite original-parent total?}&\text{event-additive?}&\text{fixed-own-scale accumulation}\\
\hline
q_0\ \text{spacetime enstrophy}&\text{yes}&\text{yes}&\text{summable }(r)\\
q_1\ \text{palinstrophy}&\text{not certified}&\text{yes}&\text{nonsummable }(r^{-1})\\
q_2\ \text{raw-H2}&\text{not certified}&\text{yes}&\text{nonsummable }(r^{-3})\\
q_3\ \text{D3}&\text{not certified}&\text{yes}&\text{nonsummable }(r^{-5})\\
\|u\|_2^2&\text{yes}&\text{no}&\text{reusable state}\\
\text{material flux}&\text{finite label storage only}&\text{new-label only}&\text{same-label reuse}\\
\text{absolute boundary work}&\text{no known finite total}&\text{yes}&\text{unbudgeted}\\
L^3/L^{3,\infty}&\text{no additive finite total}&\text{no}&\text{critical but nonconsumptive}
\end{array}
}
\]

No current row simultaneously has

\[
\boxed{
\text{finite original total}
+
\text{event additivity}
+
\beta\le0
+
\text{fixed positive recurrent payment}.
}
\]

## 14. Generic unsigned-payer no-go

Let an unsigned recurrent payer have fixed normalized size

\[
Q_n^{norm}\ge c_*>0
\]

and physical homogeneity exponent \(\beta\).

A contradiction by simple accumulation requires both

\[
\boxed{
\sum_n r_n^\beta c_*=\infty
}
\]

and a finite additive original-parent total for \(Q\).

The current resource inventory contains no certified payer satisfying both conditions.

Therefore

\[
\boxed{
\text{the present AC route cannot be completed by another fixed unsigned local charge alone.}
}
\]

## 15. How the firewall can be escaped

There are four structurally different possibilities.

### A. Quantitative payer growth

For a resource with \(\beta>0\), prove normalized payment growth strong enough that

\[
\sum_n r_n^\beta Q_n^{norm}=\infty.
\]

For standard energy, this is

\[
\sum_n r_n e_n=\infty.
\]

### B. New finite critical budget

Find an event-additive finite parent resource with

\[
\beta\le0,
\]

preferably \(\beta=0\).

No such resource is currently certified.

### C. Signed/monotone obstruction

Replace unsigned accumulation by a one-way drift of a bounded or monotone critical observable.

This avoids the need to sum positive local costs.

### D. Rigidity/Liouville incompatibility

Show that the recurrent normalized state itself cannot exist, rather than charging every recurrence event to a consumable budget.

This is the critical-tail/Liouville route.

## 16. Relation to M18-056 and M18-057

M18-056 remains valuable because it says that within a genuinely fixed record cell, higher-order payers either descend to standard energy or force derivative escalation.

M18-057 then routes the required high-derivative escalation to remote/critical decompactification.

M18-058--059 add the global parent-level correction:

- descent to a fixed \(q_0\) payment is not yet a contradiction on the chronological first-hitting ladder;
- the original energy weight \(r_n\) remains summable;
- the high-derivative escape route still informs branch classification but does not turn fixed standard-energy payment into a global proof.

Thus the lower-order descent is a **classification gain**, not a completed AC closure.

## 17. Strategic consequence

The AC problem is now narrower but more structural.

The next useful target is not another unsigned payer estimate.

Priority should shift to one of:

1. find a scale-critical signed/monotone observable on the recurrent production system;
2. quantify growth of an existing normalized payer strongly enough to beat the \(r_n\) factor;
3. derive a new finite critical parent budget;
4. use recurrent-tail rigidity/Liouville to bypass additive economics.

Among these, the most repository-native next audit is to search the existing exact signed balances for an observable whose scale exponent is zero and whose recurrence forces a one-way drift.

## 18. Audit verdict

### Certified

- standard-energy dissipation is finite but ancestry-cheap;
- higher derivative resources are ancestry-expensive but lack finite original-parent totals;
- kinetic energy and critical norms are not additive consumed event budgets;
- material flux only counts genuinely new/replaced labels;
- absolute boundary work remains unbudgeted;
- no current unsigned payer has the required combination of finite parent total, additivity, and nonsummable first-hitting homogeneity.

### Still open

- a scale-critical signed/monotone observable;
- quantitative normalized payer growth beating chronological scale shrinkage;
- a new finite critical additive budget;
- LOG-ALIGN/NONREUSE/FE-PARENT where relevant;
- remote and critical roots;
- global 3D Navier--Stokes regularity.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]