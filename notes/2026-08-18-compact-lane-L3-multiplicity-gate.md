# Compact-lane L3 multiplicity gate

Date: 2026-08-18

Status: **THE COMPACT/NATURAL-SCALE LANE CANNOT SURVIVE A HYPOTHETICAL FINITE-TIME SINGULARITY WHILE THE GLOBAL CRITICAL `L3` VELOCITY NORM REMAINS BOUNDED. THEREFORE A SURVIVING COMPACT LANE MUST GROW THE CRITICAL AMPLITUDE OF ITS ACTIVE PACKET OR INCREASE SPATIAL/FREQUENCY PACKET MULTIPLICITY. THE MULTIPLICITY ALTERNATIVE IS CHARGED BY GAUSSIAN/LP ENSTROPHY-PALINSTROPHY PACKING. GLOBAL REGULARITY NOT PROVED.**

## 1. Standard endpoint gate

The Escauriaza--Seregin--Sverak endpoint theorem implies that a three-dimensional Navier--Stokes solution satisfying a bounded `L_t^infinity L_x^3` velocity norm up to a finite candidate singular time is regular.

Therefore any finite-time blow-up candidate must have an unbounded `L3` sequence as the singular time is approached.

This is imported standard PDE theory, not a DSD result.

## 2. What a single compact natural packet gives

On the compact lane the active physical scale is

\[
\ell_j\asymp W_j^{-1/2},
\qquad
K_j\asymp\sqrt{W_j}.
\]

A nontrivial natural-scale dangerous core has velocity amplitude `~sqrt(W_j)` on volume `~W_j^{-3/2}`, so its scale-invariant local `L3` contribution is only order one:

\[
\boxed{
\int_{B_{c\ell_j}}|u|^3dx\gtrsim c.
}
\]

This by itself is compatible with a bounded global `L3` norm.

Hence a hypothetical singularity cannot be explained solely by one uniformly shaped order-one compact packet moving to higher and higher physical frequency.

## 3. Surviving compact-lane dichotomy

To make the global `L3` norm unbounded, at least one of the following must happen.

### A. Packet critical amplitude growth

The local critical `L3` charge of at least one active packet diverges.

This leaves the uniformly compact fixed-shape lane and enters a stronger residual/coherent/derivative concentration branch.

### B. Packet multiplicity growth

There are `N_j -> infinity` essentially disjoint or almost-orthogonal space-frequency packets, each carrying an order-one critical `L3` contribution.

For bounded-overlap Gaussian windows at one natural scale, the local residual/mean square charges satisfy Bessel/Carleson packing. The pointwise-to-band bridge gives, schematically,

\[
\boxed{
N_j
\lesssim
E_j+P_j
}
\]

in terminal-normalized units, with constants depending on the fixed compact-lane thresholds.

At source-active times with `E'>=0`, the first-hitting palinstrophy cone gives

\[
P_j\lesssim_\nu E_j,
\]

so

\[
\boxed{
N_j\lesssim_\nu E_j.
}
\]

Thus packet multiplicity is not an untyped escape: it requires global enstrophy occupancy, or else a derivative concentration when the source-active cone is not applicable.

## 4. Relation to the moving-band frontier

The compact lane therefore has the refined form

\[
\boxed{
\text{compact natural-scale danger}
\to
\begin{cases}
\text{growing critical packet amplitude},\\
\text{growing packet multiplicity / global enstrophy},\\
\text{derivative concentration}.
\end{cases}
}
\]

The second and third alternatives are already represented in the moving-band direct-stretch / commutator-transfer ledger.

The first alternative moves toward the large-critical-charge geometry and must be compared with the coherent/Betchov lane.

## 5. Limitation

Global enstrophy is not controlled uniformly near a hypothetical singular time, so `N_j <= C E_j` is not a contradiction. The value of this gate is logical/exhaustive: the compact lane cannot hide a singularity in one bounded critical packet; it must produce additional amplitude or multiplicity, both of which are tracked quantities.

Status: **BOUNDED GLOBAL L3 COMPACT LANE REMOVED BY STANDARD ENDPOINT REGULARITY / SURVIVOR REQUIRES CRITICAL AMPLITUDE OR PACKET MULTIPLICITY GROWTH / MULTIPLICITY TYPED BY ENSTROPHY-DERIVATIVE PACKING.**