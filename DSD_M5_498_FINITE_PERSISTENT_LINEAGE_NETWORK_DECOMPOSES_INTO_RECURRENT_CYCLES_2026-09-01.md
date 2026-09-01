# DSD M5-498 — Finite persistent lineage network decomposes into recurrent critical cycles

Date: 2026-09-01

Status: **FINITE-NETWORK REDUCTION / M5-497 REDUCES THE UNIFORMLY TIGHT QUIET LOCAL-PAYER BRANCH TO FINITELY MANY PERSISTENT MATERIAL-FLUX LINEAGES / AFTER PASSING TO THE COMMON INVARIANT HULL MEASURE, LONG-TIME AVERAGED LINEAGE-TRANSFER FLOWS SATISFY VERTEX CONSERVATION / ANY POSITIVE RECURRENT TRANSFER SUPPORT THEREFORE DECOMPOSES INTO DIRECTED CYCLES INSIDE RECURRENT STRONGLY CONNECTED COMPONENTS / POSITIVE PRODUCTION, NONCOLLINEAR DUAL-PAIR ACTIVITY, AND RATCHET ACTIVITY CAN BE RECORDED ON THIS FINITE NETWORK, BUT THEY NEED NOT LIE ON THE SAME CYCLE WITHOUT AN ADDITIONAL INTERSECTION THEOREM / THE TIGHT HARD CORE IS THUS A FINITE CONSERVATIVE CRITICAL-CYCLE SYSTEM RATHER THAN AN UNTYPED INFINITE GENEALOGY / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Saturated lineage set

M5-497 produces a finite persistent lineage family

\[
\mathcal L_{sat}
=
\{L_1,\ldots,L_N\},
\qquad
N\le N_{max}.
\]

No new fixed-flux lineage can be stored indefinitely without entering an already typed replacement/flux-loss/export/projective/mass exit.

On the quiet compact branch all recurrent local production and fixed-flux genealogy can therefore be represented within this finite set after a fixed residual threshold is absorbed.

---

## 2. Directed transfer graph

Construct a finite directed graph

\[
\boxed{
G=(V,E),
\qquad
V=\{1,\ldots,N\}.
}
\]

A directed edge

\[
i\to j
\]

is activated when a fixed material-flux amount genealogically transferred/reformed from the representation of lineage `L_i` into `L_j` during the retained stage, including fixed replacement events after lineage identification.

Let

\[
F_{ij}(\theta)\ge0
\]

denote a bounded normalized transfer-rate observable after fixed time smoothing inside one similarity chart.

The finite-memory and compactness assumptions make all retained edge observables bounded on the finite graph.

---

## 3. Lineage storage variables

Let

\[
M_i(\theta)
\]

be a bounded material-flux occupancy/storage observable for lineage `L_i`, measured at the fixed threshold used to define the saturated representation.

Its schematic balance has the form

\[
\boxed{
\frac{dM_i}{d\theta}
=
\sum_{j\ne i}F_{ji}
-
\sum_{j\ne i}F_{ij}
+D_i,
}
\]

where `D_i` contains signed diffusive flux change through the material-surface flux law.

If `D_i` produces a persistent net gain/loss not represented by a lineage transfer, that is already a flux-change/replacement exit rather than a quiet conservative network event.

Thus on the retained quiet network, the non-transfer signed remainder has zero invariant mean after the M5-489 signed-flux audit.

---

## 4. Invariant vertex balance

Average over the common invariant suspension measure.

Because `M_i` is bounded and the measure is invariant,

\[
\left\langle\frac{dM_i}{d\theta}\right\rangle=0.
\]

The quiet signed diffusive remainder also has zero mean.

Therefore

\[
\boxed{
\sum_{j\ne i}\bar F_{ji}
=
\sum_{j\ne i}\bar F_{ij},
}
\]

where

\[
\bar F_{ij}:=\langle F_{ij}\rangle\ge0.
\]

Thus the mean transfer graph is a finite nonnegative circulation.

---

## 5. Cycle decomposition theorem

A finite nonnegative directed flow satisfying conservation at every vertex decomposes into a finite nonnegative sum of directed cycle flows.

Therefore there exist directed cycles

\[
C_1,\ldots,C_m
\]

and weights

\[
a_1,\ldots,a_m>0
\]

such that

\[
\boxed{
\bar F
=
\sum_{k=1}^{m}a_k\,\mathbf 1_{C_k}
}
\]

in the standard edge-flow sense.

Hence every edge with

\[
\bar F_{ij}>0
\]

belongs to at least one recurrent directed cycle.

A one-way lineage cascade cannot carry positive invariant mean forever inside the finite saturated quiet branch.

---

## 6. Strongly connected recurrent components

Equivalently, collapse the directed graph into strongly connected components.

The condensation graph is acyclic.

Any edge between two distinct components carrying positive invariant mean would create net long-time flux from an upstream component to a downstream component without a return path, contradicting bounded invariant storage unless that flux exits the retained system.

Therefore the support of the quiet invariant mean transfer lies inside recurrent strongly connected components.

Thus

\[
\boxed{
\text{quiet positive-frequency transfer}
\Longrightarrow
\text{recurrent finite SCC/cycle}.
}
\]

---

## 7. Attach the production observable

M5-497 gives at least one persistent lineage `L_prod` with

\[
\boxed{
\langle Q_{prod}\rangle>0.
}
\]

Record this as a positive vertex observable

\[
q_i:=\langle Q_i\rangle.
\]

At least one vertex has

\[
q_i>0.
\]

If that lineage participates in positive mean transfer, it belongs to one of the recurrent SCCs carrying cycle flow.

If it has no positive mean transfer edges, then it is a persistent self-contained producer and constitutes a one-vertex recurrent production component.

Both cases are finite recurrent endpoints.

---

## 8. Attach the dual-pair observable

For each unordered pair define a bounded dual mark

\[
d_{ij}(\theta)
\]

that records the fixed noncollinearity/flux event of M5-490.

The common invariant hull construction can retain

\[
\sum_{i<j}\langle d_{ij}\rangle>0.
\]

Since the pair set is finite, at least one pair satisfies

\[
\boxed{
\langle d_{ab}\rangle>0.
}
\]

This recovers the persistent recurrent dual pair inside the finite network language.

It need not correspond to a directed material-transfer edge; dual interaction and material replacement are different observables.

---

## 9. Attach the ratchet observable

Likewise let

\[
r_i(\theta)\ge0
\]

record the lineage-associated projective/directional ratchet activity when the active material carrier can be genealogically assigned to `L_i`.

On the quiet saturated branch, replacement events have already been routed, so the positive-density retained-material ratchet measure can be represented by the finite lineage family.

Hence

\[
\boxed{
\sum_i\langle r_i\rangle>0.
}
\]

and therefore at least one lineage `L_rat` has

\[
\boxed{
\langle r_{rat}\rangle>0.
}
\]

---

## 10. Common-measure firewall

The production, dual, and ratchet observables are all recorded on one common invariant hull measure.

Thus simultaneously

\[
\sum_i q_i>0,
\]

\[
\sum_{i<j}\langle d_{ij}\rangle>0,
\]

and

\[
\sum_i\langle r_i\rangle>0.
\]

However this does **not** imply

\[
L_{prod}=L_{rat}
\]

or that the positive dual pair contains either one.

Nor does positivity of the three means force their event-time sets to intersect.

Different recurrent SCCs or cycles can carry different functions under a non-ergodic invariant measure.

Any theorem requiring all marks on one cycle needs an additional coupling argument.

---

## 11. Ergodic-component audit

Under ergodic decomposition, each global mean is an average of component means.

There is at least one ergodic component carrying positive production, at least one carrying positive dual activity, and at least one carrying positive ratchet activity.

They need not be the same component.

A single component carrying all three would be stronger and valuable, but cannot be selected from positivity alone.

This prevents an artificial closure by silently merging independent positive-density statements.

---

## 12. Signed cocycle condition on a cycle

Suppose a bounded lineage potential

\[
\Phi_i
\]

could be found such that every active transfer edge satisfies

\[
\Phi_j-\Phi_i
\ge c_{ij}>0.
\]

Summing around any directed recurrent cycle would give

\[
0
=
\sum_{i\to j\in C}(\Phi_j-\Phi_i)
\ge
\sum_{i\to j\in C}c_{ij}>0,
\]

a contradiction.

Therefore any strict one-sign transfer potential would close the corresponding recurrent cycle immediately.

The fact that the network survives means every presently known candidate quantity either

1. has sign-changing transfer increments;
2. is not bounded on the relevant branch; or
3. fails to assign consistently to lineage vertices.

---

## 13. Current tight hard core

The uniformly tight quiet branch has been reduced to

\[
\boxed{
\text{finite recurrent critical lineage network}
}
\]

with

\[
\boxed{
\begin{aligned}
&N\le N_{max},\\
&\text{mean transfer circulation decomposed into cycles},\\
&\text{positive production on at least one recurrent vertex/component},\\
&\text{positive dual activity on at least one recurrent pair/component},\\
&\text{positive ratchet activity on at least one recurrent vertex/component},\\
&\text{zero mean signed material-flux drift on persistent cycles}.
\end{aligned}
}
\]

The endpoint is finite but still dynamically nontrivial.

---

## 14. Highest-value next targets

Two distinct tasks remain.

### C1 — component coupling

Prove that the positive-production, dual-pair, and ratchet observables must occur in one common recurrent SCC/ergodic component.

This would produce a single finite critical cycle carrying all required mechanisms.

### C2 — cycle potential

Construct a bounded signed quantity tied to material-flux lineage identity whose net change is strictly positive on at least one unavoidable edge class and nonnegative on the others.

Any such potential contradicts cycle recurrence.

If C1 fails, the failure means the survivor decomposes into dynamically distinct recurrent components whose coupling occurs only through the nonlocal velocity/strain field. That becomes a new remote-interaction structure to audit.

---

## 15. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
