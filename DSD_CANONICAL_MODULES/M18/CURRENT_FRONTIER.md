# M18 Current Frontier

**Date:** 2026-09-11  
**Current tip:** **M18-022**  
**Status:** AUTHORITATIVE DSD ANALYSIS FRONTIER

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Phase boundary

M17 is retained as the calculation/derivation chain through M17-469. M18 is the subsequent DSD analysis/audit line. Historical M17-470--485 remain legacy aliases according to `M18_TRANSITION_AND_RENUMBERING_MAP.md`.

## 2. Migrated frontier

M18-001--019 are the canonical aliases of the historical post-M17-469 analysis modules through legacy M17-485.

## 3. New M18 results

### M18-020

Positive time measure of a zero-tube flux-loss event can be partitioned directly into spacetime payer sets without differentiating the individual payer currencies. The payer ancestry classes remain

\[
R^{-1}\quad\text{(palinstrophy)},
\qquad
R^{-5}\quad\text{(first coefficient jet/D3)},
\qquad
R^{-7}\quad\text{(second coefficient jet/D4)}.
\]

### M18-021

The exact-equality active set used operationally in M18-020 is not robust enough to generate positive time measure. A two-threshold inequality event is required.

With a strict margin and uniform equicontinuity in the invariant coefficient-time coordinate

\[
\vartheta=\int\delta(t)dt,
\]

active-time thinning is impossible. The scale-invariant differentiable temporal-shape parameter is

\[
\Theta=\delta^{-1}\left|\partial_t(F/J)\right|.
\]

Thus temporal thinning forces temporal flux-shape decompactification or an explicit margin/J/tube/window/genealogy loss.

### M18-022

The pointwise time derivative of one level flux contains \(\partial_nD_t\kappa\) and therefore appears to reach a third coefficient jet / D5-type vorticity derivative.

However, coefficient-level smoothing gives

\[
B_\phi
=\int\phi(\kappa)\rho^2|\nabla\kappa|^2dx
=\int\phi(s)F(s,t)ds,
\]

and bulk integration by parts removes \(\nabla D_t\kappa\) exactly.

Writing

\[
h=D_t\kappa,
\qquad
h=L_\rho\kappa+L_\rho\sigma+\mathcal R_{\rm geom},
\]

the exact bulk identity is

\[
\begin{aligned}
\dot B_\phi
&+\int\phi\rho^2\left(|L_\rho\kappa|^2+|h|^2\right)dx\\
={}&2\int\phi(\sigma+\nu\kappa-a_n)\rho^2|\nabla\kappa|^2dx\\
&-\int\phi'h\rho^2|\nabla\kappa|^2dx\\
&+\int\phi\rho^2|L_\rho\sigma+\mathcal R_{\rm geom}|^2dx.
\end{aligned}
\]

Therefore the pointwise D5 temporal barrier is not universal on macroscopic coefficient-width branches.

## 4. Current unresolved local channels

The compact regular-tube zero-flux branch is currently reduced to:

\[
\boxed{
\begin{aligned}
G_{\rm robust\ flux\ loss}
\Longrightarrow{}&
G_{\rm spacetime\ palinstrophy}^{R^{-1}}\\
&\lor G_{\rm first\ coefficient\ jet/D3}^{R^{-5}}\\
&\lor G_{\rm second\ coefficient\ jet/D4}^{R^{-7}}\\
&\lor G_{\rm coefficient\ cutoff\ current}\\
&\lor G_{\rm strain/geometry\ source\ square}\\
&\lor G_{\rm level\text{-}width/critical/tube/domain/genealogy\ loss}.
\end{aligned}
}
\]

## 5. Next target

M18-023 should audit the coefficient-cutoff current

\[
\mathcal C_\phi
=-\int\phi'(\kappa)(D_t\kappa)\rho^2|\nabla\kappa|^2dx
\]

using adapted cutoffs, collar decomposition, and weighted inequalities. The goal is to absorb it into the favorable bulk rate term and the existing first-coefficient-jet resource, or isolate an explicit higher-gradient collar exit.
