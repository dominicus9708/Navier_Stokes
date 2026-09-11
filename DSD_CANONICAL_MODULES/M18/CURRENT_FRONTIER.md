# M18 Current Frontier

**Date:** 2026-09-11  
**Current tip:** **M18-026**  
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

The M17-339 / M18-022 / M18-023 formulas without the factor \(\nu\) in front of \(L_\rho\kappa\) are \(\nu=1\) specializations. M18-024 is authoritative for the repository-wide general-\(\nu\) setting.

## 3. Migrated frontier

M18-001--019 are the canonical aliases of the historical post-M17-469 analysis modules through legacy M17-485.

## 4. New M18 results

### M18-020--021: event time thickness

Positive active-time measure converts the zero-tube flux-loss event directly into spacetime payer sets. A robust two-threshold event plus equicontinuity in coefficient time

\[
\vartheta=\int\delta(t)dt
\]

prevents arbitrary active-time thinning. Otherwise a scale-invariant temporal flux-shape jet or an explicit margin/J/tube/window/genealogy loss occurs.

### M18-022--023: bulk smoothing and cutoff absorption

Coefficient-level smoothing removes the pointwise \(\partial_nD_t\kappa\)/D5 hazard. An adapted squared cutoff \(\phi=\chi^2\) absorbs the coefficient-cutoff current into the favorable coefficient-rate term plus the scale-invariant collar-gradient parameter

\[
\boxed{
\Gamma_{\mathcal K}
=
\operatorname*{ess\,sup}_{\mathcal K}
\frac{|\nabla\kappa|^2}{\delta_0^3}.
}
\]

Thus the cutoff current is not an independent local branch when \(\Gamma_{\mathcal K}\) is bounded on a fixed fractional collar.

### M18-024: viscosity correction and source-square descent

The corrected general-\(\nu\) bulk identity is

\[
\boxed{
\begin{aligned}
\dot B_\phi
&+\nu\int\phi\rho^2|L_\rho\kappa|^2dx
+\nu^{-1}\int\phi\rho^2|D_t\kappa|^2dx\\
={}&2\int\phi(\sigma+\nu\kappa-a_n)\rho^2|\nabla\kappa|^2dx\\
&-\int\phi'(\kappa)(D_t\kappa)\rho^2|\nabla\kappa|^2dx\\
&+\nu^{-1}R_\phi.
\end{aligned}
}
\]

The combined source has an exact material-Laplacian commutator representation and satisfies

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

Thus the opaque strain/geometry-source-square branch is reduced to the existing D3 spacetime resource plus snapshot palinstrophy decompactification.

### M18-025: palinstrophy temporal thickening

Whole-space Navier--Stokes gives

\[
\boxed{
P'(t)\le C\nu^{-1/3}P(t)^{5/3}.
}
\]

A crossing from \(p/2\) to \(p\) requires

\[
\boxed{
\Delta t\gtrsim\nu^{1/3}p^{-2/3},
\qquad
\int Pdt\gtrsim\nu^{1/3}p^{1/3}.
}
\]

For endpoint height \(p_m\) and backward window \(\tau_m\),

\[
\boxed{
q_m^P
\gtrsim
\min\{p_m\tau_m,\nu^{1/3}p_m^{1/3}\}.
}
\]

The corresponding ancestry contradiction requires

\[
\sum_mR_m^{-1}q_m^P=\infty,
\]

which is not yet established.

### M18-026: anisotropic collar-gradient packet classification

For a high-gradient collar point with

\[
G=|\nabla\kappa|,
\qquad
\Gamma=G^2/\delta_0^3,
\]

the natural transverse and normal scales are

\[
\boxed{
L_0=\delta_0^{-1/2},
\qquad
\ell_n=\delta_0/G=L_0\Gamma^{-1/2}.
}
\]

Define the scale-invariant full-Hessian shape parameter

\[
\mathfrak H_2
:=
\delta_0^{-2}\operatorname*{ess\,sup}_{\mathcal C}|D^2\kappa|
\]

and weighted packet-mass parameter

\[
\boxed{
\mathfrak M_\rho
:=
\sqrt\Gamma\,\delta_0^{-1/2}
\int_{\mathcal C}\rho^2dx.
}
\]

If the anisotropic packet survives, \(\mathfrak H_2\lesssim\sqrt\Gamma\), and \(\mathfrak M_\rho\gtrsim1\), then the packet first-coefficient-jet charge satisfies

\[
\boxed{
B_{\mathcal C}
\gtrsim
\delta_0^{7/2}\sqrt\Gamma.
}
\]

Hence normalized collar-gradient concentration must produce first-jet packet growth or escape through full second-coefficient-jet concentration, weighted packet-mass depletion, or transverse/tube/domain loss.

Full-Hessian concentration is not automatically Laplacian concentration: its trace-free part corresponds to level-shape/normal-field geometry and must remain separately audited.

## 5. Current unresolved local channels

The compact regular-tube robust-flux-loss branch is reduced to

\[
\boxed{
\begin{aligned}
G_{\rm robust\ flux\ loss}
\Longrightarrow{}&
G_{\rm spacetime\ palinstrophy}^{R^{-1}}\\
&\lor G_{\rm first\ coefficient\ jet/D3}^{R^{-5}}\\
&\lor G_{\rm second\ coefficient\ jet/D4}^{R^{-7}}\\
&\lor G_{\rm first\text{-}jet\ packet\ growth}\\
&\lor G_{\rm weighted\ packet\ mass\ depletion}\\
&\lor G_{\rm trace\text{-}free\ Hessian/level\text{-}geometry\ decompactification}\\
&\lor G_{\rm high\ snapshot\ palinstrophy/time\ concentration}\\
&\lor G_{\rm strain/normal\text{-}stretch\ decompactification}\\
&\lor G_{\rm level\text{-}width/critical/tube/domain/genealogy\ loss}.
\end{aligned}
}
\]

## 6. Next target

M18-027 should audit the weighted packet-mass depletion branch

\[
\boxed{
\mathfrak M_\rho
=
\sqrt\Gamma\,\delta_0^{-1/2}
\int_{\mathcal C}\rho^2dx
\to0.
}
\]

The target is to determine whether such depletion can coexist with the retained robust level-flux witness, or whether it necessarily forces transverse-area concentration, nodal migration/amplitude depletion, or a palinstrophy/raw-H2 payment.