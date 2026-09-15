# M19-296 — Finite flux-population labels do not automatically form a disjoint material-energy partition

**Date:** 2026-09-16  
**Status:** AUDIT CORRECTION / MATERIAL-POPULATION REPRESENTATION FIREWALL / M19-283--295 SCOPE SHARPENING

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-087 proves finite-memory recurrence of one or finitely many coherent fixed-flux **material populations**. M19-283, M19-286, M19-292, and M19-295 then study a compatible finite material partition into spatial regions \(P_i\).

These are not the same statement.

The historical M18 modules themselves already distinguish them: M18-089 explicitly assumes a compatible material-population partition and records interface/realization loss as an exit.

This module makes that scope restriction canonical for the current M19 dynamic-core route.

## 2. What M18-087 certifies

The finite-memory storage theorem supplies a bounded number of distinguishable coherent material-flux population labels on the quiet recurrent branch.

A persistent population may represent:

- a coherent flux carrier family;
- a set of related sub-tubes/patches;
- a genealogical material population;
- a recurrent current-carrying class.

The theorem does not by itself say that these labels are pairwise disjoint open three-dimensional regions covering one active core.

Thus

\[
\boxed{
\text{finite persistent population labels}
\not\Rightarrow
\text{finite disjoint spatial partition}.
}
\]

## 3. Additional structure required by energy-network modules

The M19-286/M19-292 network cancellation requires regions

\[
P_1,\ldots,P_N
\]

such that:

1. interiors are pairwise disjoint;
2. their union is the retained material core;
3. each boundary/interface is sufficiently regular;
4. the regions are transported coherently by the same material field;
5. velocity/pressure/energy-gradient traces exist across shared interfaces;
6. no material is silently double-counted or omitted except an explicitly tracked background region.

This is a genuine representation theorem, not a notational convention.

## 4. Canonical partition-realization gate

Define

\[
\boxed{
\mathcal T_{pop}^{partition}:
\text{realize the finite persistent flux-population architecture as a compatible finite material spatial partition, possibly plus an explicit residual background.}
}
\]

Failure is

\[
\boxed{
G_{population\ partition/interface/representation}.
}
\]

This gate is already implicit in M18-089 and must remain explicit in M19.

## 5. Scope of M19-283--295

The current modules divide as follows.

### Single-population formulas

M19-284, M19-291, and M19-293 require only one sufficiently regular material cutoff/population representation. They remain applicable on any branch where that one carrier can be realized.

### Finite-network formulas

M19-286, M19-292, and M19-295 additionally require \(\mathcal T_{pop}^{partition}\).

Their conclusions are conditional:

\[
\boxed{
\mathcal T_{pop}^{partition}
\Longrightarrow
\text{antisymmetric exchange cancellation / closed-core conditional balance / mean-velocity graph reduction}.
}
\]

They must not be read as unconditional consequences of finite label saturation alone.

### Partial wedge carrier localization

M19-283 additionally requires pressure-gauge coherence or a gauge-invariant reformulation, as corrected by M19-290.

## 6. Why overlapping populations matter

Two genealogically distinct material-flux populations may in principle:

- overlap spatially at different internal sublabels;
- be nested;
- represent different cross-sections of a larger carrier;
- be defined through flux/genealogy rather than volume ownership.

In such cases an additive kinetic-energy decomposition

\[
E_{core}=\sum_iE_i
\]

would double-count or omit material unless a genuine partition/refinement is first constructed.

Likewise an interface current \(Q_{ij}\) is meaningful only after a shared codimension-one spatial interface is identified.

## 7. Possible realization strategy

A sufficient construction could refine the active material region into atoms of the finite population sigma-algebra/overlap pattern, then transport those atoms materially.

But this strategy must prove:

- finite number of nontrivial atoms;
- regular enough boundaries;
- preservation over the lag window;
- compatibility with the production-paying lineage and current marks;
- no uncontrolled fragmentation at nodal/CE-H/interface events.

These are not currently certified.

## 8. Updated dynamic-core branch

The gauge-invariant material-energy route should therefore be read as

\[
\boxed{
\begin{aligned}
\mathcal T_{tail}^{lag-defect/core}
\Longrightarrow{}&
\mathcal T_{single}^{material\ energy}
\\
&\land
\Big(
\mathcal T_{pop}^{partition}
\lor
G_{population\ partition/interface/representation}
\Big).
\end{aligned}
}
\]

On the partition branch, M19-292--295 apply.

On the representation-loss branch, one must either construct a different gauge-invariant aggregate observable or classify the loss as an explicit hard survivor.

## 9. Strategic consequence

The current low-frequency finite graph is useful but **conditional**. The unconditional achievement is narrower:

- ordinary winding/index has been removed as a standalone signed payer;
- the global wedge event mean is ordinary dissipation;
- a single material carrier has an exact gauge-invariant conditioned energy law;
- if a compatible partition exists, all internal energy exchange cancels and low frequency reduces to a finite mean-velocity graph.

This is the correct canonical scope.

---

\[
\boxed{\text{M19-296 COMPLETE; FINITE MATERIAL POPULATION LABELS REQUIRE AN INDEPENDENT PARTITION-REALIZATION THEOREM BEFORE CLOSED ENERGY-NETWORK CONCLUSIONS ARE UNCONDITIONAL.}}
\]
