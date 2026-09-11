# M19-011 — Finite-lineage saturation reduces EVENT-ALIGN to a single-lineage cubic-mass versus return-occupancy decorrelation problem

**Date:** 2026-09-11  
**Status:** CALCULATION / R-AC EVENT-ALIGN RECOMPRESSION / FINITE-INCIDENCE PIGEONHOLE / SINGLE-LINEAGE FRONTIER

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-010 proves that on a fixed parent annulus, positive similarity-time event measure is uniformly equivalent to positive descendant parabolic-slot occupancy.

Thus the remaining R-AC issue is not the time-coordinate Jacobian. It is whether the recurrent event is carried by the material genealogy that realizes the age-shell ancestry return.

M18-045 supplies the relevant genealogy structure:

- fixed-lag comparison is exhausted by contact, paid exposure, or replacement;
- paid exposure is already a typed payer;
- repeated replacement enters finite-memory flux storage and cannot remain indefinitely quiet;
- export routes to remote/historical or escaping-critical roots;
- remote recurrence need not be one eternal material packet.

M5-488/M5-497 further reduce the quiet compact local branch to a finite family of persistent fixed-flux lineages.

The present module shows that, after these exits are removed, EVENT-ALIGN is not an infinite-label problem. It reduces to a finite incidence matrix and then to one persistent lineage carrying divergent cubic shell mass while its aligned return occupancy becomes too small.

## 2. Quiet represented branch

Work after removing the already typed alternatives

\[
G_{paid\ exposure},
\quad
G_{replacement/export},
\quad
\mathcal R_{remote},
\quad
\mathcal R_{critical},
\]

from the present R-AC subcalculation.

On the remaining compact represented branch, let

\[
\mathcal L
=\{L_1,\ldots,L_N\},
\qquad
N\le N_{max}<\infty,
\]

be the saturated persistent fixed-flux lineage family.

The calculation below is conditional on this already certified quiet-branch reduction. It does not claim that the typed exits are closed globally.

## 3. Shell-lineage incidence weights

Let

\[
w_k:=J_k^{3/2}.
\]

Then

\[
\boxed{
\sum_kw_k=\infty.
}
\]

For each age shell \(k\), define nonnegative representation fractions

\[
\boxed{
c_{ik}\in[0,1],
\qquad i=1,\ldots,N,
}
\]

with the interpretation that \(c_{ik}\) is the fraction of the retained shell witness/mass assigned to persistent lineage \(L_i\) under the chosen controlled finite-lineage representation.

On the quiet represented branch assume the residual has already been reduced below the retained threshold, so there exists

\[
\boxed{c_{rep}>0}
\]

such that

\[
\boxed{
\sum_{i=1}^Nc_{ik}
\ge c_{rep}
}
\]

for every retained shell in the family under calculation.

If this representation floor fails, that failure belongs to the residual/replacement/coherence/geometry exits and is not silently ignored.

## 4. Finite-lineage weighted pigeonhole

Multiply the representation floor by \(w_k\) and sum:

\[
\sum_i\sum_kc_{ik}w_k
\ge
c_{rep}\sum_kw_k
=\infty.
\]

Since the number \(N\) of lineages is finite, at least one lineage \(L_{i_*}\) satisfies

\[
\boxed{
\sum_kc_{i_*k}J_k^{3/2}
=\infty.
}
\]

Thus a cubic-mass-divergent age-shell family cannot continually evade every persistent lineage merely by rotating through infinitely many labels.

On the quiet finite-memory branch, one fixed lineage carries divergent **represented cubic mass** in the weighted incidence sense.

## 5. Aligned return occupancy for each lineage-shell pair

For every represented pair \((i,k)\), let

\[
\delta_{ik}\in[0,1]
\]

be the descendant parabolic-slot occupancy fraction of the **aligned ancestry-return event** carried by lineage \(L_i\) in the relevant fixed parent annulus.

By M19-010, this is uniformly comparable to the corresponding similarity-time event fraction whenever the same event has been identified.

Define the shell-level represented occupancy

\[
\boxed{
\delta_k^{rep}
:=
\sum_{i=1}^Nc_{ik}\delta_{ik}.
}
\]

This quantity measures not just recurrent activity, but recurrent activity weighted by how much of the shell witness is represented by the same lineage.

## 6. Sufficient aligned-return condition

On the plain-return branch, M19-009 gives the scaling target

\[
\delta_k
\gtrsim
J_k^{1/2}.
\]

Thus a sufficient represented-lineage condition is

\[
\boxed{
\delta_k^{rep}
\ge c_*J_k^{1/2}
}
\]

on a subset \(S\) with

\[
\sum_{k\in S}J_k^{3/2}=\infty.
\]

Then the represented event occupancy supplies the return-density lower bound required by the existing R-AC ledger, up to the previously certified comparability constants.

## 7. If shell-level alignment fails, one lineage carries the failure

Suppose instead that R-AC survives, so that on cubic-mass density

\[
\frac{\delta_k^{rep}}{J_k^{1/2}}
\to0
\]

in the same weighted sense as the M18-054 return deficiency.

For any \(\varepsilon>0\), the shells with

\[
\delta_k^{rep}
\ge
\varepsilon J_k^{1/2}
\]

can carry only finite cubic mass on the surviving branch.

Hence the divergent mass lies in shells where

\[
\sum_i c_{ik}\delta_{ik}
<
\varepsilon J_k^{1/2}.
\]

All terms are nonnegative. Therefore, in particular, the fixed lineage \(i_*\) from Section 4 must have a cubic-mass-divergent subsequence on which its own aligned occupancy is small relative to the shell amplitude scale, unless its incidence weight itself collapses there.

More precisely, for any threshold \(\gamma>0\), split

\[
S_{i_*,\gamma}
:=
\{k:c_{i_*k}\ge\gamma\}.
\]

If for some \(\gamma>0\)

\[
\sum_{k\in S_{i_*,\gamma}}c_{i_*k}J_k^{3/2}=\infty,
\]

then on the surviving alignment-deficient subfamily,

\[
\boxed{
\delta_{i_*k}
\lesssim
\frac{\varepsilon}{\gamma}J_k^{1/2}
}
\]

in cubic-mass density.

If no fixed \(\gamma\) carries divergent mass, then the divergent represented mass of \(L_{i_*}\) is itself concentrated on shells with

\[
\boxed{c_{i_*k}\to0}
\]

in its own mass-weighted density.

Thus the failure splits into

\[
\boxed{
\text{same-lineage occupancy deficiency}
\lor
\text{same-lineage incidence dilution}.
}
\]

## 8. Incidence dilution is a real distinct mechanism

The fact that one lineage carries

\[
\sum_kc_{ik}w_k=\infty
\]

does not imply a uniform positive lower bound on \(c_{ik}\).

For example, a slowly decaying sequence of incidence fractions can still carry divergent weighted mass.

Therefore it would be invalid to replace weighted incidence divergence by

\[
c_{ik}\ge c_0>0
\]

on infinitely many shells without proof.

This is a new precision firewall.

The relevant remaining question is whether a fixed-flux persistent lineage can carry divergent cumulative shell mass only through vanishing fractional incidence while avoiding replacement/coherence/geometry exits.

## 9. EVENT-ALIGN is now a one-lineage decorrelation theorem

Combining Sections 4--8, the quiet finite-lineage R-AC survivor has been reduced to one fixed persistent lineage satisfying a weighted version of

\[
\boxed{
\text{large cumulative age-shell mass}
\quad\text{but}\quad
\text{vanishing aligned return occupancy or vanishing incidence fraction}.
}
\]

Symbolically,

\[
\boxed{
G_{EVENT\text{-}ALIGN}
\Longrightarrow
G_{lineage\ occupancy\ decorrelation}
\lor
G_{lineage\ incidence\ dilution}
}
\]

modulo the already separated exposure/replacement/export/remote/critical exits.

The infinite-label ambiguity has been removed.

## 10. Relation to positive-density production

M5-497 proves that at least one persistent lineage carries positive mean local production on the saturated finite network.

However, it does **not** prove that this production lineage is the same lineage \(L_{i_*}\) selected by divergent age-shell incidence.

Likewise the persistent dual pair and ratchet lineage may be different members of the network.

Therefore separate positivity statements cannot simply be intersected.

This is exactly the remaining correlation problem:

\[
\boxed{
\text{production/ratchet-positive lineage}
\stackrel{?}{=}
\text{cubic-mass-bearing ancestry lineage}.
}
\]

or, more weakly, whether the finite interaction network forces sufficient transfer between them.

## 11. What would close the quiet R-AC subroot

Any one of the following would suffice:

1. a uniform incidence floor on a cubic-divergent subset;
2. a positive aligned-event occupancy floor for every persistent fixed-flux lineage carrying nontrivial shell incidence;
3. a finite-network transfer theorem forcing cubic mass from a low-occupancy lineage into a positive-density production/current lineage;
4. proof that persistent incidence dilution itself forces replacement, coherence loss, export, or remote/critical escape.

No such theorem is asserted here.

## 12. M19-011 verdict

The R-AC EVENT-ALIGN problem is no longer an uncontrolled material-identity problem.

On the quiet compact branch it reduces to a finite-network, ultimately single-lineage correlation defect:

\[
\boxed{
\text{divergent represented cubic shell mass}
\text{ decorrelates from aligned ancestry-return occupancy}.
}
\]

This is the precise calculation frontier.

## 13. Next step

The next useful calculation should test whether the **finite interaction network itself** can transfer the positive-density production/current mark to the cubic-mass-bearing lineage.

If that cannot be forced from the current graph data, R-AC should be marked as requiring a genuinely new incidence/transfer theorem and M19 should move to the next upstream root rather than endlessly repackage the same deficiency.

---

\[
\boxed{\text{M19-011 COMPLETE; R-AC REDUCED TO A SINGLE-LINEAGE INCIDENCE/OCCUPANCY CORRELATION FRONTIER.}}
\]
