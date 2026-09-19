# M20 Index — Pressure-Free Vorticity Residual and Projective Dynamics

**Opened:** 2026-09-19  
**Predecessor:** M19 frozen at M19-442  
**Current tip:** M20-005  
**Next ID:** M20-006  
**Status:** ACTIVE FAMILY

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## Scope

M20 studies the pressure-free terminal vorticity residual and its projective geometry.

Primary variables:

\[
B=B_A,
\qquad
D_\omega=\mathcal K_3C=G_z(0),
\qquad
\xi_B=\frac{B}{|B|}.
\]

## Modules

### M20-001
Global enstrophy-tangent curl residual is refined pointwise into:

- relative amplitude reweighting;
- true local direction motion;
- provisional nodal birth term.

It also establishes robust positive-vorticity-threshold placement for a genuine direction branch.

### M20-002
True direction motion satisfies the exact terminal direction PDE and splits into:

\[
T_{\rm texture}
\lor
S_{\rm eig}
\lor
V_{\rm proj}.
\]

This separates Eulerian advection from material projective motion.

### M20-003
Relative amplitude reweighting is the exact probability law

\[
\partial_zd\pi_z|_0
=
2(\lambda-\alpha)d\pi_B.
\]

It changes global projective covariance only through direction-correlated selection and can be projectively silent at second moment.

### M20-004
The nodal positive-volume L2 branch is closed:

\[
D_\omega=0
\quad\text{a.e. on }\{B=0\},
\]

hence

\[
Z_0=0.
\]

The authoritative tangent split is now only

\[
V_{\rm reweight}\lor V_{\rm dir}.
\]

### M20-005
Transverse strain is the projective double commutator

\[
D_tQ|_S=[[S,Q],Q],
\]

with

\[
\|[S,Q]\|_F^2=2|P_\xi^\perp S\xi|^2.
\]

Its positive Rayleigh-ascent contribution is compensated in full Navier--Stokes by pressure-Hessian, strain-diffusion, and viscous projective terms.

## Current architecture

\[
\boxed{
V_{\rm tan}^{curl}
\Longrightarrow
R_{\rm proj}
\lor
R_{\rm silent}
\lor
T_{\rm texture}
\lor
S_{\rm eig}
\lor
V_{\rm proj}.
}
\]

## Next target

M20-006 should use the coordinate-free commutator \([S,Q]\) to derive a signed compensation/covariance law for recurrent transverse strain action, rather than another unsigned critical norm.

A secondary target is higher projective moments for the second-moment-silent reweighting branch.

## Stop condition

M20 ends when the projective terminal information must be propagated through a genuinely finite-depth wedge corridor. That transition opens M21.
