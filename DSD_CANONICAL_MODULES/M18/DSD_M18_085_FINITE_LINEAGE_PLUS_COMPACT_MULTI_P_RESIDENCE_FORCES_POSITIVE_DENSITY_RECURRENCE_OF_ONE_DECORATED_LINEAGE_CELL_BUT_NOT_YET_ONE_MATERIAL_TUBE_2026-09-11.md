# M18-085 — Finite lineage plus compact multi-p residence forces positive-density recurrence of one decorated lineage cell, but not yet one material tube

**Date:** 2026-09-11  
**Status:** FINITE-STATE / COMPACT-RESIDENCE PIGEONHOLE / SAME-TUBE FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-084 proves that a recurrent reversible-current branch is absorbed into the existing multi-p strain-segregation / diffusive-sheath architecture **if** the same persistent material tube has

\[
0<\Phi_-\le |\Phi|\le\Phi_+<\infty
\]

and two generalized residence coordinates

\[
L_{p-1},\qquad L_{q-1}
\]

remain recurrent and nondegenerate.

The remaining realization question is whether recurrent redistribution among finitely many persistent lineages forces such a same-tube recurrence.

The present module proves the first finite-state step:

\[
\boxed{
\text{finite lineage family}
+
\text{compact residence coordinates on a positive-density event set}
\Longrightarrow
\text{one decorated lineage cell recurs with positive density}.
}
\]

But this still does not identify one exact material tube label. The intra-lineage tube-label continuum remains a genuine bridge.

---

## 2. Finite persistent lineage family

On the retained compact no-export/no-new-label branch, let

\[
\mathcal L
=\{L_1,\dots,L_N\},
\qquad N<\infty,
\]

be the persistent lineage family from the M5-497/M5-514 saturation architecture.

Suppose recurrent current/redistribution events occur on a set

\[
\mathcal T_{cur}
\]

with positive lower time density

\[
\boxed{
\underline d(\mathcal T_{cur})>0.
}
\]

At each event choose one lineage carrying the fixed current/redistribution mark.

Because the family is finite, there exists at least one lineage

\[
L_*
\]

whose marked event subset

\[
\mathcal T_*
\subset\mathcal T_{cur}
\]

has positive lower density after finite pigeonhole refinement:

\[
\boxed{
\underline d(\mathcal T_*)>0.
}
\]

---

## 3. Two residence coordinates

Fix finite exponents

\[
q>p\ge2.
\]

For the material tube/line segment participating in a marked event inside lineage \(L_*\), define

\[
R_p(\theta):=\log L_{p-1}(\theta),
\]

\[
R_q(\theta):=\log L_{q-1}(\theta).
\]

The logarithmic coordinates are convenient because loss toward zero and blowup toward infinity become ordinary decompactification.

The residence plane is

\[
\mathcal R:=\mathbb R^2.
\]

---

## 4. Compact-residence branch

Assume that on a positive-density marked subset

\[
\mathcal T_{comp}\subset\mathcal T_*
\]

there exists a fixed compact rectangle

\[
K_R
=[a_p,b_p]\times[a_q,b_q]
\subset\mathbb R^2
\]

such that

\[
\boxed{
(R_p(\theta),R_q(\theta))\in K_R
\qquad
\forall\theta\in\mathcal T_{comp},
}
\]

and

\[
\underline d(\mathcal T_{comp})>0.
\]

Equivalently, on these events,

\[
0<e^{a_p}\le L_{p-1}\le e^{b_p}<\infty,
\]

\[
0<e^{a_q}\le L_{q-1}\le e^{b_q}<\infty.
\]

---

## 5. Finite residence-cell cover

Fix any resolution

\[
\delta>0.
\]

Cover the compact rectangle \(K_R\) by finitely many half-open rectangles

\[
Q_1,\dots,Q_M
\]

of diameter at most \(\delta\).

Every event in \(\mathcal T_{comp}\) belongs to one of the finite decorated states

\[
(L_*,Q_1),\dots,(L_*,Q_M).
\]

Since the union has positive lower density and the number of cells is finite, at least one cell

\[
Q_*
\]

has positive lower-density recurrence:

\[
\boxed{
\underline d\left(
\{\theta\in\mathcal T_{comp}:
(R_p,R_q)(\theta)\in Q_*\}
\right)>0.
}
\]

Thus one fixed lineage and one fixed coarse residence state recur at positive density.

---

## 6. Arbitrarily fine decorated recurrence subsequences

Repeat the finite-cover argument for a sequence

\[
\delta_n\downarrow0.
\]

At each scale choose a recurrent cell \(Q_n\).

By compactness of \(K_R\), after passing to a nested subsequence if necessary, the closures may be chosen so that

\[
\operatorname{diam}Q_n\to0
\]

and their centers converge to some

\[
R_*=(R_{p,*},R_{q,*})\in K_R.
\]

Therefore there exists a sequence of marked event times

\[
\theta_n\to\infty
\]

on the same persistent lineage \(L_*\) such that

\[
\boxed{
(R_p(\theta_n),R_q(\theta_n))
\to
(R_{p,*},R_{q,*}).
}
\]

This is a genuine recurrent residence-state subsequence at lineage level.

No periodicity is asserted.

---

## 7. What has not been proved: same material tube

A persistent lineage \(L_*\) may contain a continuum of material tube labels or coherent subcarriers.

The event at time \(\theta_n\) may be carried by tube label

\[
\lambda_n
\]

with

\[
\lambda_n\neq\lambda_m
\quad(n\neq m).
\]

Thus convergence of the residence pair

\[
(R_p,R_q)
\]

inside one persistent lineage does not imply

\[
\boxed{
\lambda_n=\lambda_*
\text{ for infinitely many }n.
}
\]

Nor does it imply that one fixed material tube remains nondegenerate across the entire recurrent sequence.

This is the central same-tube firewall.

---

## 8. Why finiteness of lineages is insufficient

A simple abstract countermodel is enough.

Take one lineage vertex \(L_1\) containing material labels

\[
\lambda\in[0,1].
\]

At event \(n\), choose

\[
\lambda_n=1/n.
\]

Suppose all labels have the same residence pair

\[
(R_p,R_q)=R_*.
\]

Then the decorated lineage state is perfectly recurrent while no nonzero material label repeats.

Therefore

\[
\boxed{
\text{finite lineage recurrence}
+
\text{residence recurrence}
\not\Rightarrow
\text{same material-tube recurrence}.
}
\]

An additional compactness, atomicity, flux-floor, or label-persistence theorem is necessary.

---

## 9. Complement: residence decompactification

If no compact rectangle captures a positive-density fraction of the marked events, then for every compact

\[
K\subset\mathbb R^2
\]

the residence pair leaves \(K\) on asymptotically dominant marked events.

Hence along a marked subsequence at least one of

\[
R_p\to+\infty,
\quad
R_p\to-\infty,
\quad
R_q\to+\infty,
\quad
R_q\to-\infty
\]

occurs.

Equivalently,

\[
\boxed{
L_{p-1}\to\infty
\lor
L_{p-1}\to0
\lor
L_{q-1}\to\infty
\lor
L_{q-1}\to0.
}
\]

Call this

\[
\boxed{G_{residence\ decompactification}.}
\]

This is a typed material-amplitude/line-geometry exit rather than a quiet reversible current loop.

---

## 10. Exact compactness split

The recurrent current branch now has the rigorous split

\[
\boxed{
G_{cycle}^{rev}
\Longrightarrow
G_{decorated\ lineage\ compact}
\lor
G_{residence\ decompactification}
\lor
G_{lineage/label\ realization\ loss}.
}

On the first branch, one fixed persistent lineage has arbitrarily fine recurrent multi-p residence states.

But M18-084 still requires an extra theorem to pass from

\[
G_{decorated\ lineage\ compact}
\]

to

\[
G_{same\ material\ tube\ recurrence}.
\]

---

## 11. What could close the same-tube gap

At least three mechanisms could suffice.

### A. Fixed flux-floor atomicity

If every recurrent current event contains a material sub-tube carrying flux at least

\[
\phi_*>0
\]

and the total available absolute flux is finite, only finitely many pairwise disjoint such labels can coexist.

This could convert continuum label recurrence into finite material-label recurrence, provided disjointness/nonreuse is certified.

### B. Material-label compactness plus recurrence of the full state

If tube labels live in a compact metric label space and the material evolution is invertible/continuous with a recurrent marked state, one may seek an actual recurrent label rather than only a recurrent lineage.

This requires more than the existing coarse lineage graph.

### C. Saturation theorem for fixed-current packets

A local current floor plus smooth compactness may thicken to a fixed-flux material packet. If the existing finite-label saturation theorem applies to those packets, one fixed packet label must recur after finitely many replacements.

Whether the M18-076 current floor is strong enough for this exact packet extraction is the highest-value next question.

---

## 12. Relation to M5-497/M5-514

M5-497/M5-514 already show that recurrent fixed-flux payer packets cannot proliferate indefinitely on the quiet compact branch.

However those theorems should not be imported automatically here.

The present current mark is initially an \(L^2\) surface-current / divergence-driven redistribution mark.

One must first prove

\[
\boxed{
\text{fixed recurrent surface-current mark}
\Longrightarrow
\text{fixed-flux material sub-tube mark}
}
\]

with controlled geometry and nonzero flux floor.

Only then can finite packet-label saturation be applied without circularity.

---

## 13. Strategic consequence

The reversible-current branch has been reduced from a broad dynamical possibility to one precise realization bridge:

\[
\boxed{
\text{surface-current recurrence}
\stackrel{?}{\Longrightarrow}
\text{fixed-flux sub-tube recurrence}.
}
\]

If this bridge is proved, finite-label saturation plus the decorated recurrence result can feed the branch into M18-084 and hence back into the existing covariance/sheath architecture.

If it fails, the failure must explain how a fixed current can be carried by ever-changing arbitrarily small-flux labels without triggering geometry or derivative concentration.

That failure itself is structurally informative.

---

## 14. Audit verdict

### Certified

1. Finite persistent lineages plus compact two-residence coordinates force positive-density recurrence of one fixed decorated lineage cell.
2. Arbitrarily fine residence-state recurrence subsequences exist inside that lineage.
3. This does not imply recurrence of one exact material tube label.
4. If residence coordinates fail compactness, at least one generalized residence decompactifies to zero or infinity.
5. The remaining same-tube gap can potentially be attacked by a fixed-flux sub-tube extraction from the recurrent surface-current mark.

### Still open

- fixed-current \(\to\) fixed-flux sub-tube extraction;
- exact material-label recurrence;
- residence decompactification routing;
- mean conservative lineage circulation;
- self-helicity/twist and surface geometry loss;
- ancestry, remote, and critical roots;
- global regularity.

## 15. Next target

M18-086 should test whether the M18-076 quantitative current/divergence floor, together with compact CE-H smoothness and a nondegenerate Frobenius patch, forces a subpatch carrying a fixed signed vorticity-flux amount

\[
\left|\int_{S'}\rho\,dA\right|\ge\phi_*>0
\]

or an equivalent fixed material-tube flux mark.

The proof must distinguish current magnitude from vorticity-flux magnitude; a large current on a very low-amplitude patch may fail to provide such a flux floor. That low-amplitude escape should be kept explicit rather than hidden.
