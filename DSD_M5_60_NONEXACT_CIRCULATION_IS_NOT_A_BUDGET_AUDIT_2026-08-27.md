# DSD M5-60 — Non-Exact Circulation Is Not a Budget

Date: 2026-08-27

Status: **DSD NECESSITY/SUFFICIENCY AUDIT / NON-EXACTNESS AVOIDS THE M5-58 TELESCOPING FAILURE BUT DOES NOT BY ITSELF CONTRADICT COMPACT RECURRENCE / A RECURRENT FLOW CAN CARRY A FIXED-SIGN NON-EXACT LOOP ACTION FOREVER / CLOSURE REQUIRES AN INDEPENDENT FINITE BUDGET OR A BOUNDED-BELOW STATE FUNCTIONAL THAT THE LOOP CONSUMES MONOTONICALLY / GLOBAL REGULARITY UNPROVED.**

## 1. What M5-59 achieved

M5-59 showed that a second independent observable can generate a path integral such as

\[
\mathcal C_Y[T_0,T_1]
=
\int_{T_0}^{T_1}Y(t)\,dE(t)
\]

which need not telescope as the difference of one bounded scalar state function.

This removes the exact-differential obstruction from M5-58.

It does **not** yet create a contradiction.

---

## 2. Compact recurrence controls state, not accumulated path length/action

A compact recurrent trajectory may traverse the same loop indefinitely.

The state remains in a compact set, while a path-dependent accumulated action can grow without bound.

The elementary model is uniform motion on a circle:

\[
\theta(t)=t\pmod{2\pi}.
\]

The state is periodic and compact.

But the non-exact one-form `dtheta` on the circle has

\[
\int_0^{2\pi N}d\theta
=2\pi N.
\]

Thus

\[
\boxed{
\text{compact recurrence}
+\text{positive non-exact loop circulation}
\not\Rightarrow
\text{contradiction}.
}
\]

The accumulated circulation is not itself required to be a bounded state coordinate.

---

## 3. Application to a pressure/Hodge loop

Suppose one succeeded in proving for every recurrent pump loop

\[
\oint Y\,dE
\ge c_*>0.
\]

After `N` returns this would imply

\[
\mathcal C_Y(N)
\ge Nc_*.
\]

This proves positive action density along the recurrent orbit.

However, unless there is an independent estimate

\[
\boxed{
\mathcal C_Y(N)
\le C_{global}<\infty
}
\]

or unless `C_Y` equals the monotone loss of a bounded-below state functional, the linear growth is dynamically admissible.

It is no different in principle from accumulating angular winding number on a periodic orbit.

---

## 4. The missing logical bridge

A closure argument must contain two separate statements.

### Recurrence lower bound

For a disjoint sequence of recurrent pump events `I_n`,

\[
\mathcal A(I_n)
\ge a_n>0.
\]

### Independent global upper bound

For the same action,

\[
\sum_n\mathcal A(I_n)
\le B_0<\infty.
\]

Only when

\[
\sum_n a_n=\infty
\]

are the two statements incompatible.

Therefore the true contradiction template is

\[
\boxed{
\text{recurrent lower action}
+\text{finite independent budget}
+\text{nonsummable event lower bounds}
\Rightarrow
\text{no survivor}.
}
\]

Non-exactness concerns the first term. It does not supply the second.

---

## 5. Relation to earlier M5 pruning

M5-49 already showed that ordinary physical energy/dissipation cannot be used naively as the independent budget: normalized recurrent event costs shrink with the physical scale and are summable on the Zeno ladder.

M5-47 showed the complementary critical phenomenon: scale-critical actions remain order one per normalized copy and hence can accumulate linearly/logarithmically, but the classical finite-energy theory does not provide a finite total budget for those critical actions.

M5-58 then showed that the most natural signed finite-band pressure overpay does have a bounded state primitive, but precisely for that reason it telescopes instead of accumulating.

These three facts form a trilemma:

\[
\boxed{
\begin{array}{ll}
\text{subcritical classical budget:} & \text{finite, but per-copy cost shrinks/sums;}\\
\text{critical recurrent action:} & \text{order one per copy, but no finite known budget;}\\
\text{bounded-state signed derivative:} & \text{finite primitive, but telescopes.}
\end{array}
}
\]

A successful closure must escape this trilemma.

---

## 6. What would escape the trilemma

At least one of the following would suffice in principle.

### A. Hidden finite critical budget

Find a scale-critical nonnegative quantity `B` for which suitable solutions satisfy

\[
\int_0^{T_*}B(t)dt<\infty
\]

from the classical hypotheses, while every recurrent pump copy contributes at least `c_*>0`.

### B. Bounded-below scale-breaking Lyapunov functional

Find a state functional `L` bounded below such that every recurrent return forces

\[
L(t_{n+1})
\le L(t_n)-c_*
\]

with one fixed `c_*>0`.

Compact recurrence would then be impossible.

### C. Topological/history action tied to a finite physical invariant

A non-exact loop action could close the argument if its cumulative winding/circulation were itself bounded by a conserved or finite initial-data quantity.

### D. Direct rigidity

Avoid budgets entirely by proving that the finite-band pump plus static `1/r` ancestry and pressure-Poisson/Hodge constraints admit no recurrent loop at all.

This is a structural nonexistence route rather than an accumulation route.

---

## 7. Pressure-Poisson locality does not itself supply a budget

M5-51 localized the order-one pressure payer to the core plus finitely many adjacent logarithmic shells.

This is valuable for rigidity because it removes dependence on infinitely remote cell shells.

But spatial locality is not temporal finiteness.

The same local pressure mechanism can, in principle, operate on every recurrent return.

Therefore

\[
\boxed{
\text{finite number of spatial payer shells}
\not\Rightarrow
\text{finite number of temporal payments}.
}
\]

A temporal/global budget or a direct no-loop theorem is still required.

---

## 8. DSD audit

### GREEN

M5-59 correctly identifies non-exact loop observables as the next level beyond exact entropy derivatives.

### RED

Treating nonzero loop circulation as a contradiction merely because the state orbit is compact/recurrent is invalid.

### GREEN

A contradiction requires an independent bounded quantity consumed by that circulation, or a direct recurrent-loop rigidity theorem.

### YELLOW

The finite-band core-plus-neighbor-shell pressure structure is sufficiently localized that a direct rigidity theorem is now a concrete alternative to finding a hidden finite budget.

---

## 9. Sharpened proof gate

The previous target

\[
\text{find a non-exact pressure/Hodge loop defect}
\]

is therefore necessary but insufficient.

The actual accumulation target is

\[
\boxed{
\text{find a sign-definite recurrent action whose nonsummable lower bound is controlled by an independent finite global budget.}
}
\]

The alternative is

\[
\boxed{
\text{prove directly that the localized pressure/Hodge pump loop cannot recur.}
}
\]

M5-61 will classify the scaling exponents of possible event budgets to determine which side is more plausible.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
