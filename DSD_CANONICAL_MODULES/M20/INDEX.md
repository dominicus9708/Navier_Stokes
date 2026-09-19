# M20 Index — Pressure-Free Vorticity Residual and Projective Dynamics

**Opened:** 2026-09-19  
**Predecessor:** M19 frozen at M19-442  
**Current tip:** M20-010  
**Next ID:** M20-011  
**Status:** ACTIVE FAMILY

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## Core modules

### M20-001
Global enstrophy-tangent residual is decomposed into relative-amplitude reweighting, genuine direction motion, and a provisional nodal term.

### M20-002
Genuine direction motion splits into Eulerian direction-texture transport, transverse strain-eigenframe action, or viscous projective diffusion.

### M20-003
Relative amplitude reweighting is the exact normalized-enstrophy probability current

\[
\partial_zd\pi_z=2(\lambda-\alpha)d\pi.
\]

### M20-004
The positive-volume nodal L2 branch is closed:

\[
D_\omega=0\quad\text{a.e. on }\{B=0\}.
\]

Hence the authoritative tangent split is only reweighting or genuine direction motion.

### M20-005
Transverse strain is the projective double commutator

\[
D_tQ|_S=[[S,Q],Q],
\]

with

\[
\|[S,Q]\|_F^2=2|P_\xi^\perp S\xi|^2.
\]

### M20-006
The projective strain vector satisfies an exact signed transverse-pressure compensation law:

\[
P_\xi^\perp D_ts_\perp
=
-2\gamma s_\perp
-
P_\xi^\perp(\nabla^2p)\xi
+
\nu P_\xi^\perp(\Delta S)\xi
+
P_\xi^\perp(S-\gamma I)v_\perp.
\]

### M20-007
The transverse pressure-Hessian commutator is a traceless Calderon--Zygmund channel with the same critical annular \(R^{-3}\) ancestry weight. It is not a new noncritical payer.

### M20-008
Higher projective moments do not eliminate silent reweighting. The exact blind kernel of all direction-only observables is

\[
\mathbb E[\lambda-\alpha\mid Q]=0.
\]

### M20-009
The terminal reweighting speed obeys the exact vorticity-magnitude decomposition

\[
\lambda
=
X_T-\gamma+X_D+X_\xi.
\]

### M20-010
Axial stretching yields the exact selection covariance

\[
\operatorname{Cov}(\lambda,\gamma)
=
-\operatorname{Var}(\gamma)
+
\operatorname{Cov}(X_T+X_D+X_\xi,\gamma).
\]

The natural observability state is upgraded from \(Q\) to \((Q,\gamma)\), with blind kernel

\[
\mathbb E[\lambda-\alpha\mid Q,\gamma]=0.
\]

## Current target

M20-011 should combine:

\[
C_{\lambda\gamma}
=
\operatorname{Cov}(\lambda,\gamma)
\]

and

\[
M_{\gamma S}
=
\mathbb E[\gamma\|[S,Q]\|_F^2]
\]

into one signed compensation system.

The intended question is whether simultaneous neutrality of amplitude selection and projective strain can persist without pressure-Hessian, scalar-diffusion, direction-gradient, or lineage-hysteresis compensation.

## Stop condition

M20 ends when the terminal projective information must be propagated through a genuinely finite-depth wedge corridor. That transition opens M21.
