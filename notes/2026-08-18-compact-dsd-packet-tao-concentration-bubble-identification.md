# Compact DSD packet and Tao critical concentration-bubble identification

Date: 2026-08-18

Status: **LITERATURE/STRUCTURE IDENTIFICATION. THE COMPACT NATURAL-SCALE DSD PACKET IS THE SAME SCALE-CRITICAL TYPE OF HIGH-FREQUENCY CONCENTRATION BUBBLE THAT APPEARS IN TAO'S QUANTITATIVE L3 REGULARITY ARGUMENT. THIS PREVENTS US FROM MISLABELING THE GENERIC COMPACT BUBBLE WALL AS A NEW DSD CLOSURE. GLOBAL REGULARITY NOT PROVED.**

## 1. DSD compact packet

At terminal first-hitting level

\[
W=K^2,
\qquad
\ell=K^{-1},
\]

a compact natural packet has order-one normalized velocity amplitude and critical local `L3` content. In Littlewood--Paley language this corresponds schematically to

\[
\boxed{K^{-1}|P_Ku(t,x)|\gtrsim c.}
\]

This quantity is scale invariant.

## 2. Tao's quantitative critical bubble

Tao, *Quantitative bounds for critically bounded solutions to the Navier--Stokes equations* (arXiv:1908.04958), uses the scale-invariant concentration quantity

\[
N^{-1}|P_Nu(t,x)|
\]

as the main high-frequency bubble variable. A sufficiently large bubble can be propagated backward through a parabolic domain of dependence, and quantitative unique-continuation/Carleman arguments produce concentration at many separated spatial scales. Bounded global `L3` then limits how far the high-frequency bubble can persist.

Thus the DSD compact natural packet is not a new kind of critical object. It is a more structurally annotated version of the standard critical concentration bubble.

## 3. Consequence for this proof challenge

A completion cannot rely on the statement

> high-frequency critical packets must move to infinity in frequency

alone. That is already the generic critical concentration problem treated quantitatively by Tao and related work.

Any genuinely DSD-specific gain must use additional restrictions proved in this repository, for example

- exact first-hitting I/V causal routing;
- affine/residual decomposition;
- positive Gaussian scale increments;
- projective/angular derivative structure;
- coherent/Betchov local compensation on the large-R lane;
- vector-valued commutator packing.

The compact lane is therefore retained as a **generic critical-bubble lane plus DSD structural annotations**, not claimed as a solved or novel regularity mechanism.

## 4. Quantitative blow-up-rate compatibility

Tao's theorem implies that for a finite-time singularity the global critical `L3` norm must diverge at least at a triply logarithmic rate along a sequence of times. If the compact DSD realization is packet-dominated and each bounded-affine packet carries only `O(1)` local `L3^3`, this forces packet multiplicity to diverge quantitatively (up to any stronger background critical reservoir).

The resulting lower rate is extremely slow and remains compatible with the repository's terminal dissipation price `N/K`. Hence the existing quantitative critical theorem does not by itself close the DSD compact lane.

Status: **COMPACT DSD PACKET = STANDARD CRITICAL CONCENTRATION BUBBLE TYPE / DSD MUST OBTAIN A STRUCTURAL GAIN BEYOND GENERIC CRITICAL L3 STACKING.**