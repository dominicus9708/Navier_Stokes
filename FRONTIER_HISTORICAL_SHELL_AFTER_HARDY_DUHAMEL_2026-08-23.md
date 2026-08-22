# Frontier — Historical Shell after Hardy and Duhamel Reductions — 2026-08-23

Status: **ACTIVE SMOOTH-ONLY PROOF ATTEMPT — GLOBAL REGULARITY NOT PROVED.**

This file is the continuation pointer after the 2026-08-23 historical-shell calculations.

Read in order:

1. `HISTORICAL_SHELL_LOG_RADIAL_CRITICAL_LEDGER_2026-08-23.md`
2. `SOLENOIDAL_HARDY_GAP_AND_SLIDING_HISTORY_2026-08-23.md`
3. `SLIDING_HISTORY_DUHAMEL_FORGETTING_TAX_2026-08-23.md`

## Closed/reduced at the present conditional level

- A bounded-amplitude historical `1/r` tower is not critical-cost-free:

\[
\mathfrak D_{\log}^{rad}
=\int |x||\partial_ru|^2dx
\gtrsim
\|u\|_3^3
\sim\log K.
\]

- The sharp three-dimensional solenoidal Hardy--Leray gap at weight `gamma=1/2` gives the critical constant `5/3`, so the weighted energy identity retains at least a `2/5` fraction of the weighted derivative cost.

- Consequently a persistent historical tower extending to a fixed positive physical outer radius cannot remain weighted-flux quiet; it is routed toward `T`, modulo the moving-center/localization audit.

- The only quiet geometric escape is a sliding/forgetful historical window with

\[
N_j\to\infty,
\qquad
j-N_j\to\infty.
\]

- For a forgotten packet with a fixed fraction of mass in its natural frequency band `|xi|~r_m^{-1}`, linear diffusion over the remaining Type-I time can attenuate it only by an order-one factor. Strong forgetting therefore forces the scale-invariant nonlinear action

\[
\mathcal T_m^{NL}\ge c_*>0,
\]

which routes naturally to `T`.

## Sole active technical bottleneck

Construct a divergence-free spatial/phase-space localization of every historical shell and prove a quantitative trichotomy:

\[
\boxed{
\text{natural-frequency occupancy}
\ \vee\ 
\text{low-frequency escape}
\ \vee\ 
\text{high-frequency escape}.
}
\]

Required routing:

\[
\boxed{
\begin{aligned}
\text{natural band + forgetting}&\Longrightarrow T,\\
\text{low-frequency escape}&\Longrightarrow T/\text{coherent drift},\\
\text{high-frequency escape}&\Longrightarrow H.
\end{aligned}
}
\]

The localization commutators from cutoff, Leray projection, moving center, pressure, and diffusion must be explicitly retained and assigned to the existing `H/T/drift` channels.

## Current proof status

The historical-shell survivor is now reduced from a broad weak-`L3` tail to a localized phase-space routing problem. This is a substantial narrowing of the proof tree, but it is **not** yet a proof of global regularity.
