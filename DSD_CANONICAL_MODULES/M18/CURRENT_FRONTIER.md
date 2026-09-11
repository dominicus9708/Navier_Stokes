# M18 Current Frontier

**Date:** 2026-09-11  
**Current tip:** **M18-023**  
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

Coefficient-level smoothing instead gives

\[
B_\phi
=\int\phi(\kappa)\rho^2|\nabla\kappa|^2dx,
\]

and bulk integration by parts removes \(\nabla D_t\kappa\) exactly. Writing

\[
h=D_t\kappa,
\qquad
h=L_\rho\kappa+L_\rho\sigma+\mathcal R_{\rm geom},
\]

the exact identity is

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

### M18-023

Choose an adapted squared cutoff

\[
\phi=\chi^2,
\]

with a fixed fractional transition collar inside the retained coefficient tube. Then the coefficient-cutoff current satisfies

\[
\boxed{
|\mathcal C_\phi|
\le
\varepsilon\int\phi\rho^2|D_t\kappa|^2dx
+
C_{\chi,\varepsilon}\Gamma_{\mathcal K}\delta_0B_{\widetilde\phi},
}
\]

where

\[
\boxed{
\Gamma_{\mathcal K}
:=
\operatorname*{ess\,sup}_{\mathcal K}
\frac{|\nabla\kappa|^2}{\delta_0^3}
}
\]

is scale invariant and \(B_{\widetilde\phi}\) is a slightly larger first-coefficient-jet observable.

Thus, under normalized collar-gradient compactness and a fixed fractional collar, the cutoff current is absorbed into the favorable bulk rate term plus the inherited first-coefficient-jet resource. It is not an independent local branch.

Failure is typed as normalized collar-gradient concentration, which is a representation-safe refinement of the existing coefficient-gradient decompactification branch. Pointwise concentration still requires a thickness theorem before it becomes an integrated payer.

## 4. Current unresolved local channels

The compact regular-tube robust-flux-loss branch is currently reduced to

\[
\boxed{
\begin{aligned}
G_{\rm robust\ flux\ loss}
\Longrightarrow{}&
G_{\rm spacetime\ palinstrophy}^{R^{-1}}\\
&\lor G_{\rm first\ coefficient\ jet/D3}^{R^{-5}}\\
&\lor G_{\rm second\ coefficient\ jet/D4}^{R^{-7}}\\
&\lor G_{\rm normalized\ collar\ gradient\ concentration}\\
&\lor G_{\rm strain/geometry\ source\ square}\\
&\lor G_{\rm strain/normal\text{-}stretch\ decompactification}\\
&\lor G_{\rm level\text{-}width/critical/tube/domain/genealogy\ loss}.
\end{aligned}
}
\]

The coefficient-cutoff-current branch has been removed under the explicit M18-023 adapted-cutoff compactness hypotheses.

## 5. Next target

M18-024 should audit the remaining source square

\[
\boxed{
R_\phi
=
\int\phi\rho^2
|L_\rho\sigma+\mathcal R_{\rm geom}|^2dx.
}
\]

The first step must preserve the M17-463 provenance firewall: test whether the **combined source** has an exact lower-order cancellation, divergence, or projection identity before estimating its individual terms. If no such structure exists, only then split it into separately typed strain and geometry channels.
