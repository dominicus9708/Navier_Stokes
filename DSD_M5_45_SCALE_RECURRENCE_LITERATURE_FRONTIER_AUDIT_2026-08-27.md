# DSD M5-45 — Scale-Recurrence Literature Frontier Audit

Date: 2026-08-27

Status: **LITERATURE-BOUNDARY AUDIT / EXISTING ASYMPTOTIC-DSS AND DSS RIGIDITY RESULTS DO NOT AUTOMATICALLY REMOVE THE W1 PUMP-TO-DEFECT CELL BECAUSE ITS STATIC `1/r` TAIL IS WEAK-`L3` AND MAY FAIL GLOBAL STRONG `L3` / LARGE BACKWARD-DSS WEAK-CRITICAL REGIME REMAINS AN OPEN FRONTIER / GLOBAL REGULARITY UNPROVED.**

## 1. Current W1-specific object

M5-44 produces a terminal-centered scale-recurrent Navier--Stokes cell with:

- complete recurrent W1 ancestry;
- a positive finite-amplitude pump event;
- a static `1/r` critical tail;
- recurrence under terminal-centered parabolic scaling;
- and a finite forward terminal horizon.

If W1 is periodic, the cell is exactly backward DSS. If W1 is aperiodic minimal, it is scale-aperiodically recurrent.

---

## 2. Asymptotically DSS nonexistence results

Chae's asymptotically discretely self-similar nonexistence theorem for 3D Navier--Stokes assumes, in the periodic-profile formulation, a profile in

\[
C^1(\mathbb R;
L^3(\mathbb R^3)\cap C^2(\mathbb R^3)).
\]

The W1 static tail behaves as

\[
|V(z,\sigma)|\sim |z|^{-1},
\]

so in general

\[
V(\sigma)\in L^{3,\infty}
\setminus L^3.
\]

Hence the strong-`L3` hypothesis is exactly the missing bridge.

---

## 3. Exact DSS branch

For exact backward DSS, Chae--Wolf remove singularities when the scaling parameter is sufficiently close to `1`.

That result does not remove arbitrary large scaling ratios. Contemporary discussions of the scale-invariant/weak-`L3` regime continue to describe the existence of general backward DSS singular solutions as a long-standing open problem.

Therefore

\[
\boxed{
\text{periodic W1}
\not\Rightarrow
\text{known DSS contradiction}
}
\]

without an additional integrability or scaling-factor restriction.

---

## 4. Aperiodic scale recurrence

The aperiodic minimal branch is weaker than exact DSS:

\[
\mathcal R_{h_n}V_*	o V_*
\]

along recurrent scaling times, but there is no exact nonzero period.

Thus exact-DSS theorems cannot be applied directly.

Likewise, periodic-profile asymptotic-DSS theorems do not automatically apply because the recurrence hull need not contain one periodic profile.

---

## 5. DSD audit conclusion

The known rigidity results remove stronger descriptions:

\[
\boxed{
\text{self-similar/DSS recurrence}
+\text{strong critical integrability or extra decay}
}
\]

but the current W1 survivor sits at

\[
\boxed{
\text{terminal scale recurrence}
+\text{static `1/r` ancestry}
+\text{large weak-`L3` endpoint}.
}
\]

The difference is not terminology; it is the logarithmic strong-`L3` defect already isolated throughout M5.

---

## 6. Consequence for proof search

It is not useful to continue by merely relabeling the W1 cell as `asymptotically DSS`.

A genuine closure must add one of the missing properties used by known Liouville/DSS theorems, for example:

1. a bounded strong-`L3` backward sequence;
2. a tail renormalization that legitimately removes the static `1/r` component;
3. a new weak-`L3` rigidity theorem for the scale-recurrent static-tail class;
4. or a same-trajectory pump-to-tail identity producing a contradiction without strong `L3`.

No such bridge is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
