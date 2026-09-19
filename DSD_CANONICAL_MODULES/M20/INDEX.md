# M20 Index — Pressure-Free Vorticity Residual and Projective Dynamics

**Opened:** 2026-09-19  
**Predecessor:** M19 frozen at M19-442  
**First reserved calculation:** M20-001  
**Status:** ACTIVE FAMILY / NO M20 CALCULATION MODULE HAS YET BEEN CLAIMED AS COMPLETE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## Scope

M20 studies the pressure-free terminal vorticity residual and its projective geometry.

Primary variables:

\[
B=B_A,
\qquad
D_\omega:=\mathcal K_3C=G_z(0),
\qquad
\xi_B:=\frac{B}{|B|}
\quad (|B|>0).
\]

## Inherited M19 frontier

\[
\boxed{
C^\perp_{\rm mandatory}
\Longrightarrow
D_{\rm dip}^{\rm crit,cons}
\lor
V_{\rm norm}^{\rm curl}
\lor
V_{\rm tan}^{\rm curl}.
}
\]

M20 prioritizes the pressure-free branches, especially the tangent/projective branch.

## Planned M20-001

Working title:

TANGENT_CURL_RESIDUAL_FORCES_QUANTITATIVE_VORTICITY_DIRECTION_MOTION_ON_A_ROBUST_HIGH_VORTICITY_SET

Target relation:

\[
\boxed{
\partial_z\xi_B
=
\frac{P_{\xi_B}^{\perp}D_\omega}{|B|}.
}
\]

Audit goals:

1. isolate a robust subset where |B| has a fixed positive lower threshold;
2. convert tangent residual activity into direction-turnover action;
3. separate amplitude change from projective direction change;
4. compare turnover with strain-eigenframe and vortex-stretching geometry;
5. preserve critical-summability and pressure-harmonic firewalls.

## Stop condition

M20 should end when terminal/projective information must be propagated through a nontrivial finite-depth wedge corridor. That transition, if reached, opens M21.
