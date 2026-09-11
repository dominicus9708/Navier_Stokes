# M19-012 — Positive lineage production does not force interlineage transfer without a net node surplus, so the finite graph cannot by itself close EVENT-ALIGN

**Date:** 2026-09-11  
**Status:** CALCULATION / FINITE-NETWORK TRANSFER TEST / NODE-BALANCE NO-GO / R-AC FRONTIER SHARPENING

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-011 reduces the quiet R-AC EVENT-ALIGN problem to a finite persistent-lineage network and ultimately to one lineage carrying divergent represented cubic shell mass while its aligned ancestry-return occupancy is too small.

A natural shortcut is to use the existing positive-production lineage and finite graph currents to force activity onto the cubic-mass-bearing lineage.

The present module tests that shortcut.

The result is negative but precise:

\[
\boxed{
\text{positive production at a node}
\not\Rightarrow
\text{positive net export from that node}.
}
\]

Diffusion and similarity damping can balance production locally. Therefore the finite interaction graph alone cannot align the production mark with the cubic-mass ancestry mark unless one has a **net node surplus** or an additional cross-lineage coupling theorem.

## 2. Population moment balance

For a persistent material population \(P_i\), M18/M19 gives

\[
\boxed{
\frac1p(M_{p,i})'
=A_{p,i}-D_{p,i}-c_pM_{p,i}+B_{p,i},
}
\]

where

\[
A_{p,i}
=\int_{P_i}\sigma\rho^p,
\]

\[
D_{p,i}\ge0,
\]

and the internal boundary exchange is

\[
B_{p,i}
=\sum_j e_{ij}^{(p)}
\]

for a closed finite partition, with

\[
e_{ij}^{(p)}=-e_{ji}^{(p)}.
\]

Define the local non-transport source balance

\[
\boxed{
S_{p,i}
:=
A_{p,i}-D_{p,i}-c_pM_{p,i}.
}
\]

Then

\[
\boxed{
\frac1p(M_{p,i})'
=S_{p,i}+\sum_je_{ij}^{(p)}.
}
\]

## 3. Recurrent mean node balance

On a recurrent bounded population state,

\[
\left\langle(M_{p,i})'\right\rangle=0.
\]

Hence

\[
\boxed{
\left\langle S_{p,i}\right\rangle
+
\sum_j\left\langle e_{ij}^{(p)}\right\rangle
=0.
}
\]

Therefore mean net export is determined by the **net local surplus**

\[
\boxed{
\sum_j\bar e_{ij}^{(p)}
=-\bar S_{p,i}.
}
\]

It is not determined by the production term \(A_{p,i}\) alone.

## 4. Positive production is insufficient

Suppose

\[
\boxed{
\bar A_{p,i}>0.
}
\]

This is compatible with

\[
\boxed{
\bar D_{p,i}+c_p\bar M_{p,i}
=\bar A_{p,i},
}
\]

so that

\[
\bar S_{p,i}=0.
\]

Then the recurrent balance allows

\[
\boxed{
\sum_j\bar e_{ij}^{(p)}=0.
}
\]

In particular it allows every mean edge current incident to node \(i\) to vanish.

Thus

\[
\boxed{
\bar A_{p,i}>0
\not\Rightarrow
\text{mean interlineage transfer}.
}
\]

This is the exact obstruction to using the M5-497 positive-production mark as an automatic graph-transfer engine.

## 5. Two-node countermodel at the balance level

Consider two recurrent nodes \(1,2\) with

\[
\bar e_{12}=0.
\]

Choose positive bounded moments and diffusion rates satisfying

\[
\bar A_{p,1}
=\bar D_{p,1}+c_p\bar M_{p,1}>0,
\]

and

\[
\bar A_{p,2}
=\bar D_{p,2}+c_p\bar M_{p,2}.
\]

Then both node balances are satisfied with zero mean transfer.

Node 1 may carry the positive-production mark while node 2 carries an unrelated shell/genealogy mark.

No algebraic contradiction appears.

This is only a balance-level countermodel, not a construction of an exact Navier--Stokes solution. Its role is to prove that the currently certified node equations do not logically imply mark alignment.

## 6. When the graph would force transfer

If instead one could prove a strict mean surplus

\[
\boxed{
\bar S_{p,i}\ge s_*>0,
}
\]

then

\[
\sum_j\bar e_{ij}^{(p)}
\le-s_*.
\]

Thus node \(i\) would have fixed mean export in the chosen sign convention.

Likewise a strict deficit forces fixed import.

On a finite network, a collection of positive and negative node surpluses would necessarily be connected by edge current or by an explicitly separated boundary/export term.

Therefore the missing quantity is not positive production but

\[
\boxed{
\text{nonzero recurrent node surplus after local diffusion and damping are subtracted.}
}
\]

## 7. Global source balance gives no nodewise sign

Summing over the closed population network cancels internal edge currents:

\[
\sum_i\sum_je_{ij}=0.
\]

Hence

\[
\sum_i\bar S_{p,i}=0.
\]

This allows arbitrary redistribution of positive and negative node surpluses subject to zero total.

It does not identify the sign of \(\bar S_{p,i}\) at the cubic-mass-bearing lineage.

Thus global recurrent balance cannot repair the nodewise alignment problem.

## 8. Ratchet/current marks do not automatically repair the issue

The finite lineage network also contains ratchet, dual-source, and current marks.

However a positive frequency of such an event on one node does not, from the currently certified equations alone, imply

\[
\bar S_{p,i}\ne0
\]

for the amplitude-moment balance of the cubic-mass-bearing node.

Separate positive-frequency statements cannot be intersected without a joint-incidence theorem.

Hence the same firewall applies:

\[
\boxed{
\text{finite number of marked lineages}
\not\Rightarrow
\text{all marks occur on one lineage}.
}
\]

## 9. Interaction with M19-001--004

M19-001--004 proves that any actual nonzero conservative graph cycle descends to

\[
G_{strain/geometry}
\lor
G_{palinstrophy/interface}
\lor
G_{coefficient+diffusion}
\lor
G_{geometry/topology\ loss}.
\]

That result prices a cycle **if a cycle exists**.

The present module shows that positive production alone does not force such a cycle.

Therefore M19-001--004 cannot be used backward to create interlineage transfer from an isolated positive-production mark.

## 10. Precise remaining transfer theorem

To close the M19-011 decorrelation frontier through the finite graph, one needs at least one of:

1. a nodewise surplus theorem on cubic-mass-bearing lineages;
2. a joint-incidence theorem showing production/diffusion imbalance occurs on the same lineage-shell pairs;
3. a constitutive coupling forcing a lineage with large shell incidence to exchange with a positive-density active lineage;
4. proof that failure of all such couplings is itself an already typed geometry/coherence/export exit.

None is presently certified.

## 11. R-AC status after M19-012

The existing inputs now rule out several false closure routes:

\[
\boxed{
\begin{aligned}
&\text{clock telescoping shortcut},\\
&\text{standard-energy control of flux variation},\\
&\text{kinematic shortage of parabolic slots},\\
&\text{similarity-time Jacobian loss},\\
&\text{infinite-label evasion},\\
&\text{positive-production implies graph-transfer shortcut}.
\end{aligned}
}
\]

The quiet unresolved R-AC core is now

\[
\boxed{
\text{one persistent lineage carries divergent represented cubic shell mass}
\]
\[
\boxed{
\text{while aligned ancestry-return occupancy/incidence remains too small,}
}
\]

with no certified net-surplus mechanism forcing transfer from the other marked lineages.

## 12. Calculation decision

Further progress on R-AC now requires a genuinely new theorem about

\[
\boxed{
\text{lineage-shell incidence / aligned occupancy / node surplus correlation}.
}
\]

Repeating the existing budget, graph, or recurrence arguments cannot close it.

Accordingly M19 should record R-AC as an exposed theorem frontier and proceed to the next upstream root while retaining this precise target for later return.

---

\[
\boxed{\text{M19-012 COMPLETE; CURRENT R-AC TOOLCHAIN EXHAUSTED AT A SINGLE-LINEAGE CORRELATION THEOREM.}}
\]
