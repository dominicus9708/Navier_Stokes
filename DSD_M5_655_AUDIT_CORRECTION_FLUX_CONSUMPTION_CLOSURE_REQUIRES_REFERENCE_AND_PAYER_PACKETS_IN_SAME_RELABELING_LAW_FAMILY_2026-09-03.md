# DSD M5-655 — Audit correction: the flux-consumption closures require the reference and payer packets to share one relabeling-law family

Date: 2026-09-03

Status: **DSD AUDIT CORRECTION / M5-648--649 USE ORDER OR SIGN PRESERVATION FROM ONE SCALAR ODE `D_B kappa=f(kappa,theta)`; THE STRONGLY-NEGATIVE PACKET USED IN M5-648 AND THE VORTICITY-MAXIMUM PACKET USED IN M5-649 ARE GUARANTEED GLOBALLY BUT HAVE NOT YET BEEN PROVED TO BELONG TO THE SAME CONNECTED RELABELING-LAW FAMILY AS THE PERSISTENT REFERENCE LINEAGE / IF THEY LIE ON ANOTHER DISCONNECTED SHEET WITH A DIFFERENT LOCAL LAW, THE MONOTONE ABSOLUTE/RELATIVE FLUX ARGUMENT CANNOT BE APPLIED ACROSS SHEETS / THEREFORE M5-648--649 CLOSE A COMMON-LAW CORRIDOR THAT CONTAINS BOTH THE PERSISTENT REFERENCE AND THE RECURRENT DISSIPATIVE/HIGH-AMPLITUDE PACKET POPULATION, NOT AN ARBITRARY ISOLATED PERSISTENT SHEET BY ITSELF / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. The common ingredient in M5-648 and M5-649

Both finite-resource arguments rely on scalar ODE uniqueness.

### M5-648

On the zero reference branch,

\[
D_B\kappa=f(\kappa,\theta),
\qquad
f(0,\theta)=0,
\]

so a material label with `kappa<0` remains negative and its absolute material flux is monotone decreasing.

### M5-649

For a nonzero synchronized reference solution `c_*(theta)`, a lower material level governed by the **same** scalar ODE satisfies

\[
\kappa(\theta)<c_*(\theta)
\]

for all future times, so the relative flux normalized by the persistent reference is monotone decreasing.

Thus both proofs require the packet being charged to solve the same local relabeling ODE as the reference trajectory.

---

## 2. What is known globally

M5-640--641 force, at every recurrent state, a coherent strongly-negative `kappa` packet carrying fixed enstrophy and fixed transverse flux.

M5-634 forces the global vorticity maximum to satisfy

\[
\kappa_{max}\le0.
\]

These are global state statements.

They do **not** yet identify the connected `kappa`-quotient sheet on which those packets lie.

M5-650 retained precisely the possibility that disconnected sheets carry different local functions

\[
h=f_a(\kappa,\theta).
\]

Therefore a global strongly-negative/max packet may belong to a different `a` from the persistent reference lineage.

---

## 3. Why cross-sheet order comparison is invalid

Suppose the reference solves

\[
\dot c=f_a(c,\theta)
\]

while another packet solves

\[
\dot k=f_b(k,\theta),
\qquad
b\ne a.
\]

Even if initially

\[
k<c,
\]

scalar uniqueness does not prevent crossing because these are different ODEs.

Likewise, a negative `k` value need not remain negative unless the law on sheet `b` has the zero solution as an invariant trajectory.

Therefore neither

\[
\text{absolute monotonicity}
\]

nor

\[
\text{reference-relative monotonicity}
\]

can be transported across different local relabeling laws without a new argument.

---

## 4. Correct scope of M5-648

M5-648 remains valid under the condition

\[
\boxed{
\text{the recurrent strongly-negative packet population belongs to the same zero-anchored relabeling-law family as the persistent reference.}
}
\]

On that common-law corridor the finite base transverse resource gives the contradiction exactly as written.

Without this same-family condition, M5-648 only identifies what would happen **if** the strongly-negative packet enters that sheet family.

---

## 5. Correct scope of M5-649

M5-649 remains valid under the condition

\[
\boxed{
\text{during positive reference phases, a fixed-flux high-amplitude/max packet belongs to the same common-law family as the persistent reference.}
}
\]

Then order preservation makes the relative multiplier strictly negative and the finite relative-flux resource is consumed.

If the maximum lies on another sheet, M5-649 cannot compare its `kappa` history against `c_*` through one scalar ODE.

---

## 6. Corrected relabeling frontier

The correct split is therefore

\[
\boxed{
R_{relabel}
\Longrightarrow
C_{same-law}^{closed}
\lor
R_{cross-sheet\ payer}.
}
\]

The first branch is eliminated by M5-648--649.

The surviving branch is

\[
\boxed{
R_{cross-sheet\ payer}:
\text{persistent reference flux is recurrent on one sheet family while the negative/high-amplitude payer population is repeatedly supplied by other sheet families.}
}
\]

This is more precise than the generic `multi-sheet` label of M5-650.

---

## 7. Relation to M5-653 toy oscillator

The M5-653 abstract oscillator demonstrates exactly why cross-sheet recharge can evade a one-law finite-resource argument.

Different branches of `h(kappa)` permit negative flux loss and positive recharge without one order-preserving scalar comparison.

Thus the M5-653 firewall remains relevant and is not bypassed by M5-648--649.

---

## 8. What must be proved next

A genuine closure of the relabeling side now requires one of the following:

### A. Same-sheet attribution theorem

Show that a persistent productive reference lineage necessarily contains or generates the M5-640 strongly-negative / M5-634 high-amplitude payer packet inside its own connected relabeling-law family.

Then M5-648--649 close it.

### B. Cross-sheet transfer tax

Show that repeatedly obtaining the payer packet from another relabeling sheet necessarily incurs a fixed event already priced by

\[
\text{viscous flux transfer},
\quad
\text{generalized-kappa-force creation/rotation},
\quad
\text{or finite-memory material replacement}.
\]

Then positive-frequency cross-sheet payer supply can be attacked directly.

---

## 9. Audit classification

For final reconstruction:

- M5-648 and M5-649 are retained as valid **conditional closures** of same-common-law corridors;
- M5-650's warning about disconnected sheets is strengthened by the present correction;
- do not state that one isolated persistent relabeling sheet is impossible unless its required payer population is shown to remain in the same scalar-law family.

This correction does not alter M5-647's finite-transversal lemma or any exact material-flux identity.

---

## 10. Updated master target

The relabeling problem is now reduced to one explicit coupling question:

\[
\boxed{
\text{Can a persistent fixed-flux reference sheet indefinitely outsource all negative/high-amplitude viscous payment to distinct relabeling sheets without paying a fixed cross-sheet transfer tax?}
}
\]

This is the next highest-value calculation.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]