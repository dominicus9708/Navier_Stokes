# M19-294 — Centered material energy requires a quantitative velocity spectral gap above 1/(2ν), not mere Poincaré positivity

**Date:** 2026-09-16  
**Status:** CALCULATION / SPECTRAL-GAP AUDIT / PRODUCTION-TO-DISSIPATION SIGN FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-293 replaces frame-dependent material kinetic energy by the Galilean-centered quantity

\[
K_\eta
=
\frac12\int\eta|U-\bar U_\eta|^2dy.
\]

The closed-core conditional balance of M19-292 then suggests testing whether the production event forces positivity of the centered dissipation surplus

\[
\nu D_U[\eta]-\frac12K_\eta.
\]

This module identifies the exact spectral threshold and audits the repository's existing Poincaré results against it.

## 2. Exact velocity spectral ratio

Define

\[
\boxed{
\Lambda_\eta
:=
\frac{D_U[\eta]}{K_\eta}
}
\]

whenever \(K_\eta>0\), where

\[
D_U[\eta]
=
\int\eta|\nabla U|^2dy.
\]

Then

\[
\boxed{
\nu D_U-\frac12K_\eta
=
K_\eta\left(\nu\Lambda_\eta-\frac12\right).
}
\]

Therefore the exact positivity condition is

\[
\boxed{
\Lambda_\eta>\frac1{2\nu}.
}
\]

A merely positive lower bound \(\Lambda_\eta\ge\lambda_0>0\) is insufficient unless it crosses this numerical threshold.

## 3. Standard Poincaré formulation

Suppose the material population satisfies the ordinary mean-zero Poincaré inequality

\[
\int\eta|U-\bar U_\eta|^2dy
\le
C_P\int\eta|\nabla U|^2dy.
\]

Then

\[
K_\eta
\le
\frac{C_P}{2}D_U,
\]

so

\[
\boxed{
\Lambda_\eta\ge\frac{2}{C_P}.
}
\]

A sufficient sign condition is therefore

\[
\boxed{C_P<4\nu.}
\]

This is a quantitative spectral condition, not simply finiteness of \(C_P\).

## 4. Existing M19-158 gap is not this gap

M19-158 proves a uniform Poincaré ratio for **vorticity perturbations in the finite-dimensional nonsymmetry hard fiber**:

\[
\int_0^S\|\nabla\eta_v\|_2^2ds
\ge
\lambda_P
\int_0^S\|\eta_v\|_2^2ds.
\]

That theorem concerns:

- linearized hard spectral modes;
- vorticity perturbations;
- a time-period/Floquet average;
- a finite-dimensional symmetry-quotient bundle.

M19-294 instead requires:

- the nonlinear base velocity itself;
- one material population/core;
- mean-centered kinetic energy;
- a pointwise or production-conditioned material spectral ratio.

Thus

\[
\boxed{
\text{M19-158 hard-fiber gap}
\not\Rightarrow
\Lambda_\eta>1/(2\nu).
}
\]

## 5. Existing M17-448/449 transverse gap is also distinct

M17-448--449 study a Poincaré constant on transverse vortex-carrier cross-sections and show that collapse of that gap corresponds to bi-Lipschitz geometry decompactification.

This is valuable geometry information, but it acts on transverse scalar fields/sections, not on the full three-dimensional mean-centered velocity population.

Even if a population is uniformly bi-Lipschitz to a bounded reference domain, one obtains only

\[
C_P\le C_*<\infty.
\]

To sign the M19-293 surplus one still needs the stronger numerical inequality

\[
C_*<4\nu.
\]

No existing M17 transverse compactness theorem supplies that threshold automatically.

## 6. Scaling/geometric firewall

For a family of geometrically similar domains with linear size \(L\), the ordinary Poincaré constant scales like

\[
C_P\sim L^2,
\]

so

\[
\Lambda_\eta\sim L^{-2}.
\]

Hence bounded but sufficiently large normalized geometry can satisfy a perfectly valid positive Poincaré inequality while still having

\[
\nu\Lambda_\eta\le\frac12.
\]

Therefore

\[
\boxed{
\text{compact/nondegenerate population geometry}
\not\Rightarrow
\text{positive centered dissipation surplus}.
}
\]

A diameter/spectral normalization theorem stronger than mere compactness is required.

## 7. Production does not algebraically determine the velocity gap

The M5-589 production marker is built from

\[
\int_{\mathcal A_*}W\cdot\Sigma W\,dy
\]

and its palinstrophy companion. These are curl/gradient-level observables.

The ratio \(\Lambda_\eta=D_U/K_\eta\) compares the velocity gradient with the centered velocity itself and is therefore sensitive to the remaining low-frequency spatial distribution inside the material population.

Galilean centering removes the exact constant mode, but it does not remove arbitrarily long-wavelength or large-diameter mean-zero velocity structure.

Thus no purely algebraic implication

\[
\boxed{
\text{positive annular vorticity production}
\Rightarrow
\Lambda_\eta>\frac1{2\nu}
}
\]

is currently certified.

## 8. Correct new gate

The dynamic-core spectral route is therefore

\[
\boxed{
\mathcal T_{vel}^{spectral}:
\text{on the production-linked persistent material core, prove }
\Lambda_\eta>\frac1{2\nu}
\text{ on the required conditioned event set.}
}
\]

Failure of this theorem can occur through

\[
\boxed{
G_{velocity\ low\text{-}frequency/large\text{-}geometry}
\lor
G_{population\ spectral\ decompactification}
\lor
G_{material\ representation}.
}
\]

## 9. Consequence for the current lag route

If \(\mathcal T_{vel}^{spectral}\) were proved uniformly, then the closed-core conditioned identity would give a sign-controlled dissipation surplus. It would still have to be compared with the event-boundary/hysteresis recurrence to obtain a nonreplenishable budget.

Without the spectral theorem, the lag route cannot convert positive vorticity production into positive centered kinetic dissipation surplus.

## 10. Next target

Audit whether the fixed finite-depth production annulus plus the persistent production-paying lineage supplies enough **observability of the centered velocity population** to control its low-frequency mode and prove a quantitative spectral gap.

This is a localized observability problem, not another ordinary Poincaré estimate.

---

\[
\boxed{\text{M19-294 COMPLETE; THE NEEDED MATERIAL VELOCITY GAP IS QUANTITATIVE AND IS NOT PROVIDED BY THE EXISTING VORTICITY OR TRANSVERSE POINCARÉ RESULTS.}}
\]
