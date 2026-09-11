# M18-087 — Fixed-flux current events cannot churn through infinitely many quiet material populations: one persistent flux population recurs or costed exits have positive density

**Date:** 2026-09-11  
**Status:** FINITE-MEMORY FLUX-LABEL COCYCLE APPLIED TO CE-H CURRENT PATCHES / POPULATION-LEVEL RECURRENCE / INFINITESIMAL-SUBTUBE FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-086 proves that every controlled M18-076 current event carries a fixed positive directed vorticity flux

\[
\Phi_\Sigma\ge\phi_*>0.
\]

The remaining apparent escape was that, even inside one persistent lineage, infinitely many different fixed-flux subpatches might take turns carrying the current while no exact material tube recurs.

M5-488 already contains the correct finite-memory state variable for this question.

Its storage units are not arbitrary infinitesimal labels. They are **distinguishable coherent fixed-flux material populations** after a fixed angular-sector partition and fixed flux threshold.

Therefore the M18-086 events fall directly under the bounded storage cocycle once the fixed threshold is chosen below \(\phi_*\).

The result is:

\[
\boxed{
\text{positive-density controlled current events}
\Longrightarrow
\text{positive-density recurrence of one persistent fixed-flux material population}
\lor
\text{positive-density costed exits}.
}
\]

This removes infinite quiet population churn.

---

## 2. Match the M18 flux floor to the M5-488 storage threshold

M18-086 gives

\[
\boxed{
\Phi_\Sigma\ge\phi_*>0.
}
\]

Choose a fixed storage threshold

\[
0<\phi_{store}<\phi_*.
\]

Use the same finite angular-sector refinement required by the M5-397/M5-488 multiflux packing theorem.

Because the Frobenius patch already has

\[
W\cdot n=\rho>0,
\]

one can shrink/refine by a fixed amount, if required by the stored-population definition, while retaining a uniform lower flux

\[
\boxed{
\Phi_{stored}\ge c\phi_*>\phi_{store}
}
\]

for one universal retained fraction \(c>0\).

Thus every controlled current event contains a valid fixed-flux storage mark.

---

## 3. Bounded fixed-flux population count

Let

\[
N_j
\]

be the number of distinguishable coherent material-flux populations stored locally at generation/block \(j\), using the fixed threshold and angular partition.

M5-488 gives

\[
\boxed{
0\le N_j\le N_{max}<\infty.
}
\]

A genuinely new fixed-flux population without a compensating exit increases the count by at least one.

If

\[
R_j\in\{0,1\}
\]

marks new fixed-flux population formation and

\[
X_j\in\{0,1\}
\]

marks a compensating viscous-flux/projective/export/mass/geometry exit, then

\[
\boxed{
N_{j+1}-N_j
\ge
R_j-N_{max}X_j.
}
\]

This is the finite-memory storage cocycle.

---

## 4. Positive-density new-population churn forces positive-density exits

Summing the cocycle and dividing by the number of blocks gives

\[
\boxed{
\overline d(R)
\le
N_{max}\overline d(X)
}
\]

in the Cesaro/limsup sense of M5-488.

Therefore

\[
\boxed{
\overline d(R)>0
\Longrightarrow
\overline d(X)>0.
}
\]

Hence a positive-density current process cannot quietly keep producing new \(\phi_*\)-size material populations forever.

If it tries, recurrent compensating exits are mandatory.

---

## 5. Quiet branch: arbitrarily long no-new-population blocks

Now restrict to the quiet branch where the compensating exits under audit have zero density or have been split off as separate root exits.

Then new fixed-flux population creation also has zero asymptotic density.

Therefore there exist arbitrarily long blocks with no new fixed-flux population creation.

Inside such blocks, every controlled current patch must be represented by descendants of the finite population set already present at the block entrance.

Because current events themselves recur with positive density, finite pigeonhole gives at least one stored population label that carries a positive fraction of the current events on arbitrarily long blocks.

Diagonal extraction yields a persistent material-flux population in the limiting recurrent hull.

---

## 6. Invariant-measure formulation

Include the finite storage labels and current-event marks in the marked generation state.

On an invariant ergodic component with

\[
\langle X\rangle=0,
\]

M5-488 gives

\[
\langle R\rangle=0.
\]

Let

\[
C_i(\theta)\in\{0,1\}
\]

mark that persistent stored population \(i\) carries the controlled M18 current event at time \(\theta\).

After saturation,

\[
\sum_{i=1}^{N_{sat}} C_i
\ge
C_{cur}
\]

on the quiet current event set, where

\[
\langle C_{cur}\rangle>0.
\]

Hence

\[
\boxed{
\exists i_*:
\langle C_{i_*}\rangle>0.
}
\]

Thus one fixed persistent fixed-flux material population carries current events at positive invariant frequency.

---

## 7. Exact replacement of the old churn branch

The M18-086 unresolved branch

\[
G_{intra\text{-}lineage\ fixed\text{-}flux\ sub\text{-}tube\ churn}
\]

was too broad.

At the coherent fixed-flux **population** level, it is exhausted by

\[
\boxed{
G_{population\ churn}
\Longrightarrow
G_{persistent\ population\ recurrence}
\lor
G_{positive\text{-}density\ costed\ exit}.
}
\]

Thus infinite quiet churn among distinct fixed-flux populations is impossible.

---

## 8. What still remains inside one persistent population

A persistent coherent material-flux population can contain a continuum of infinitesimal vortex-line/tube labels.

Positive-density recurrence of the population does not imply that one infinitesimal tube label repeats with positive density.

Therefore the exact remaining distinction is now

\[
\boxed{
\text{fixed material population recurrence}
\not\Rightarrow
\text{fixed infinitesimal tube recurrence}.
}
\]

This is narrower than the previous population-churn problem.

---

## 9. Why the infinitesimal-label gap may not be needed for ensemble M18-069--070

The multi-p moment and diffusion-depletion results M18-069--070 are formulated on joint recurrent weighted measures over the whole active component.

They do not require one infinitesimal tube to recur.

Therefore, for **population-level classification**, a persistent fixed-flux population carrying positive-density current events is already compatible with the existing global alternatives

\[
G_{strain\text{-}seg}
\lor
G_{diffusive\ sheath/core}.
\]

The exact same-tube recurrence is required only for the stronger **linewise** material identity of M18-068/084.

Thus the infinitesimal-label gap should not be promoted to a new global root unless a later argument specifically requires linewise recurrence.

---

## 10. Population-level residence coordinates

For a persistent population \(P\) with material flux-label set \(\Lambda_P\), define aggregate generalized residence

\[
\boxed{
\mathcal L_m(P,\theta)
:=
\int_{\Lambda_P}
L_m(\lambda,\theta)
\,d\nu_\theta(\lambda).
}
\]

By the tube disintegration of M18-068, this is exactly the population contribution to the corresponding amplitude moment:

\[
\boxed{
\mathcal L_{p-1}(P,\theta)
=
M_p(P,\theta)
}
\]

up to the notation that the flux measure is included in the aggregate integral.

Thus compactness/decompactification of population residence can be tested without selecting a single infinitesimal tube.

This opens a population-level route for the next audit.

---

## 11. Population-level compactness split

For one persistent current-carrying population \(P_*\), and two exponents \(q>p\ge2\), either

\[
\boxed{
(M_p(P_*),M_q(P_*))
\text{ remains in a compact nondegenerate subset on a positive-density event set},
}
\]

or at least one population moment/residence decompactifies:

\[
\boxed{
M_p(P_*)\to0/\infty
\quad\lor\quad
M_q(P_*)\to0/\infty
}
\]

along the marked current subsequence.

The first branch supports a population-level recurrent amplitude measure; the second is a typed concentration/depletion/export branch.

No infinitesimal tube selection is needed to state this split.

---

## 12. Updated current-route frontier

Combining M18-084--087 gives

\[
\boxed{
\text{mandatory controlled current}
\Longrightarrow
\begin{cases}
G_{persistent\ fixed\text{-}flux\ population},\\
G_{positive\text{-}density\ costed\ exits},\\
G_{surface/label\ geometry\ loss},\\
G_{self\text{-}helicity/twist}.
\end{cases}
}
\]

Inside the persistent population branch,

\[
\boxed{
\text{population residence compactness}
\lor
\text{population residence decompactification}.
}
\]

The compact branch can be compared directly with the global/joint M18-069--070 architecture.

---

## 13. Highest-value next target

The next useful step is therefore **not** to force recurrence of one infinitesimal tube.

M18-088 should localize the M18-069 change-of-measure identities to one persistent fixed-flux material population \(P_*\).

Define

\[
M_p^{P_*}
:=
\int_{P_*}\rho^pdy
\]

or its exact tube-disintegrated equivalent.

Then audit whether recurrent nondegenerate population moments obey the same moment baseline

\[
\mathbb E_p^{P_*}[\sigma+\kappa]
\stackrel{?}{=}
1-\frac{3}{2p}
\]

or whether boundary exchange between the population and the rest of the flow introduces an extra transfer term.

This is the precise population-versus-global localization bridge.

---

## 14. Audit verdict

### Certified

1. M18-086 current patches satisfy the fixed-flux threshold used by M5-488.
2. The number of quiet distinguishable fixed-flux material populations is uniformly bounded.
3. Positive-density creation of new fixed-flux populations forces positive-density compensating exits.
4. On the quiet branch, one fixed persistent fixed-flux population carries current events with positive invariant frequency.
5. Infinite quiet population churn is therefore removed.
6. Exact infinitesimal-tube recurrence is not yet proved, but it is not required for the existing global M18-069--070 classification.
7. Aggregate population residence/moments give a more appropriate next state variable.

### Still open

- localization of multi-p moment balance to one persistent population and its boundary-transfer terms;
- population residence decompactification;
- mean conservative lineage circulation;
- self-helicity/twist and surface geometry loss;
- ancestry, remote, and critical roots;
- global 3D Navier--Stokes regularity.

## 15. Next target

M18-088 should derive the exact amplitude-moment balance for a persistent material-flux population with a material/cutoff carrier boundary and identify the exchange defect.

The key question is whether the global baseline

\[
1-\frac{3}{2p}
\]

survives at population level or is shifted by a signed boundary/current transfer term.
