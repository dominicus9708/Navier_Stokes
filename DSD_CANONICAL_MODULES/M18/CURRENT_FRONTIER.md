# M18 Current Frontier

**Date:** 2026-09-11  
**Current tip:** **M18-025**  
**Status:** AUTHORITATIVE DSD ANALYSIS FRONTIER

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Phase boundary

M17 is retained as the calculation/derivation chain through M17-469. M18 is the subsequent DSD analysis/audit line. Historical M17-470--485 remain legacy aliases according to `M18_TRANSITION_AND_RENUMBERING_MAP.md`.

## 2. General-viscosity correction firewall

The repository problem setting keeps \(\nu>0\). Therefore the exact CE-H coefficient law used from M18-024 onward is

\[
\boxed{
D_t\kappa
=\nu L_\rho\kappa
+L_\rho\sigma
+\mathcal R_{\rm geom}.
}
\]

The M17-339 / M18-022 / M18-023 formulas without the factor \(\nu\) in front of \(L_\rho\kappa\) are to be read as \(\nu=1\) specializations. M18-024 is authoritative for the repository-wide general-\(\nu\) setting.

## 3. Migrated frontier

M18-001--019 are the canonical aliases of the historical post-M17-469 analysis modules through legacy M17-485.

## 4. New M18 results

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

A robust two-threshold flux-loss event plus uniform equicontinuity in coefficient time

\[
\vartheta=\int\delta(t)dt
\]

forces positive active duration. Temporal thinning therefore implies a scale-invariant temporal flux-shape jet or an explicit margin/J/tube/window/genealogy loss.

### M18-022

Coefficient-level smoothing before time differentiation removes the pointwise \(\partial_nD_t\kappa\) / D5 hazard. Bulk integration by parts yields a rate-dissipation identity. For general \(\nu\), use the corrected M18-024 form below.

### M18-023

For an adapted squared cutoff \(\phi=\chi^2\), the coefficient-cutoff current is absorbed into the favorable coefficient-rate term plus a collar-gradient remainder. The scale-invariant collar parameter is

\[
\boxed{
\Gamma_{\mathcal K}
:=
\operatorname*{ess\,sup}_{\mathcal K}
\frac{|\nabla\kappa|^2}{\delta_0^3}.
}
\]

If \(\Gamma_{\mathcal K}\) is bounded on a fixed fractional collar, the cutoff current is not an independent local branch.

### M18-024

The viscosity audit restores the exact general-\(\nu\) coefficient law and gives the corrected bulk identity

\[
\boxed{
\begin{aligned}
\dot B_\phi
&+\nu\int\phi\rho^2|L_\rho\kappa|^2dx
+\nu^{-1}\int\phi\rho^2|D_t\kappa|^2dx\\
={}&
2\int\phi(\sigma+\nu\kappa-a_n)\rho^2|\nabla\kappa|^2dx\\
&-\int\phi'(D_t\kappa)\rho^2|\nabla\kappa|^2dx\\
&+\nu^{-1}R_\phi.
\end{aligned}
}
\]

The combined source

\[
R_\phi
=\int\phi\rho^2|L_\rho\sigma+\mathcal R_{\rm geom}|^2dx
\]

has an exact material-Laplacian commutator representation and satisfies

\[
\boxed{
R_\phi
\lesssim
P^{5/4}J_3^{3/4},
}
\]

where

\[
P=\|\nabla\Omega\|_2^2,
\qquad
J_3=\|D^3\Omega\|_2^2.
\]

Thus, on finite normalized intervals with a uniform snapshot palinstrophy ceiling, the opaque strain/geometry source-square branch is controlled by the existing D3 spacetime resource.

### M18-025

Whole-space Navier--Stokes gives the scale-correct one-sided palinstrophy growth inequality

\[
\boxed{
P'(t)\le C\nu^{-1/3}P(t)^{5/3}.
}
\]

A crossing from \(p/2\) to \(p\) therefore requires

\[
\boxed{
\Delta t\gtrsim\nu^{1/3}p^{-2/3},
}
\]

and pays

\[
\boxed{
\int Pdt\gtrsim\nu^{1/3}p^{1/3}.
}
\]

For endpoint height \(p_m\) and backward same-branch window \(\tau_m\),

\[
\boxed{
q_m^P
\gtrsim
\min\left\{p_m\tau_m,\nu^{1/3}p_m^{1/3}\right\}.
}
\]

The exact ancestry contradiction test is therefore

\[
\boxed{
\sum_mR_m^{-1}
\min\left\{p_m\tau_m,\nu^{1/3}p_m^{1/3}\right\}
=\infty.
}
\]

No such divergence is claimed yet.

## 5. Current unresolved local channels

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
&\lor G_{\rm high\ snapshot\ palinstrophy/time\ concentration}\\
&\lor G_{\rm strain/normal\text{-}stretch\ decompactification}\\
&\lor G_{\rm level\text{-}width/critical/tube/domain/genealogy\ loss}.
\end{aligned}
}
\]

The independent cutoff-current and opaque strain/geometry-source-square branches have been removed under the explicit M18-023--024 hypotheses.

## 6. Next target

M18-026 should audit

\[
\boxed{
\Gamma_{\mathcal K}
=
\operatorname*{ess\,sup}_{\mathcal K}
\frac{|\nabla\kappa|^2}{\delta_0^3}
\to\infty.
}
\]

The first question is whether normalized collar-gradient concentration can be thickened spatially into the existing weighted first-coefficient-jet ledger, or whether rapid concentration necessarily returns to the M18-018--019 critical-level / second-coefficient-jet branch.
