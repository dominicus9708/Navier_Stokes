# M21 Current Frontier

**Date:** 2026-09-20  
**Active family:** M21  
**Current tip:** M21-007  
**Next:** M21-008  
**Predecessor:** M20 frozen at M20-013  
**Status:** ACTIVE FINITE-DEPTH WEDGE COUPLING / PHASE-TRANSITION AUDIT COMPLETE / TRANSPORT COBBOUNDARY REMOVED / PRESSURE-DIFFUSION REDUCED TO EXISTING ANALYTIC FIREWALLS / LONGITUDINAL NO-CROSSING SURVIVOR REDUCED TO MIXED-MOMENT TRANSITION OR STRONG GAMMA-K ANTI-CORRELATION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Compact finite-depth input

M21-001 gives

\[
z_{EK},z_\omega\in[a_{21},b_{21}].
\]

The two witnesses lie in one fixed finite-depth corridor, but overlap is not automatic.

## 2. Common strain budget

M21-002 gives

\[
\boxed{
\mathscr S_{\omega\Sigma}
=
\frac{\mathscr Q_\omega^2}{W}
+
W\operatorname{Var}_{\pi_z}(\Gamma)
+
\frac12\mathscr Z.
}
\]

Thus mean longitudinal stretching, longitudinal heterogeneity, and transverse projective noncommutation share one exact nonnegative strain-square budget.

## 3. Mixed-moment ODE

M21-003 defines

\[
\mathscr M=\langle E\Gamma K\rangle
\]

and derives

\[
\boxed{
\mathscr M'
+
2z\mathscr F_M'
+
9\mathscr F_M
=
3\mathscr A
-
\frac12\mathscr B
-
\mathscr C
-
\mathscr D.
}
\]

Define

\[
\boxed{
\mathscr H:=6\mathscr A-\mathscr B.
}
\]

Then

\[
\mathscr M'
+
2z\mathscr F_M'
+
9\mathscr F_M
=
\frac12\mathscr H
-
\mathscr C
-
\mathscr D.
\]

## 4. M21-004 — phase transition is not automatic

Neither \(z_\omega\) nor \(z_{EK}\) fixes the sign of \(\mathscr H\).

Therefore the existing two witnesses do not imply

\[
\exists z_*:\mathscr H(z_*)=0.
\]

On the no-crossing branch, continuity and compactness give

\[
\boxed{
|\mathscr H(z)|\ge\delta_H>0
}
\]

with one fixed sign throughout the corridor.

M21-004 converts this into a signed compensation by:

- mixed transport current;
- pressure/diffusion correlation;
- longitudinal/transverse segregation.

## 5. M21-005 — transport is a depth coboundary

Define

\[
\mathscr Y_M
=
z^{7/2}\mathscr M
+
2z^{9/2}\mathscr F_M.
\]

Then

\[
\mathscr Y_M(0)=0,
\qquad
\mathscr Y_M(\infty)=0.
\]

Thus the corridor difference \(\Delta Y_M\) is only exchange with complementary depth regions.

If no crossing persists while the corridor is enlarged, \(\Delta Y_M\) can be made arbitrarily small.

Therefore the transport-current branch is not an independent bulk payer.

The phase frontier reduces to

\[
\boxed{
T_{\rm phase}
\lor
P_{PD}
\lor
P_{\rm segregation}.
}
\]

## 6. M21-006 — pressure/diffusion returns to existing resources

The compensator

\[
R_{PD}
=
\int z^{7/2}(\mathscr C+\mathscr D)\,dz
\]

expands into:

- scalar vorticity diffusion;
- direction-gradient damping;
- transverse/longitudinal pressure-Hessian coupling;
- strain diffusion;
- viscous projective coupling.

On the compact normalized corridor:

- scalar and strain diffusion reduce to raw-\(H^2\);
- direction gradients reduce to palinstrophy;
- pressure returns to the M20-007 traceless Calderon--Zygmund critical channel;
- nodal failures remain interface geometry rather than a positive-volume bulk payer.

Hence

\[
\boxed{
P_{PD}
\Longrightarrow
P_{\rm existing\ analytic}.
}
\]

No new noncritical bulk resource is obtained.

## 7. Distinct no-crossing survivor

After M21-005--006, the structurally distinct no-crossing branch is

\[
\boxed{
R_{\Gamma K}
=
\frac72
\int
z^{5/2}
\langle E\Gamma K\rangle\,dz.
}
\]

This is signed longitudinal/transverse phase segregation.

## 8. M21-007 — longitudinal segregation sharpens

On a longitudinal no-crossing phase, if existing analytic payers do not carry the charge, then

\[
R_{\Gamma K}<0.
\]

Therefore some depth \(z_-\) satisfies

\[
\mathscr M(z_-)=\langle E\Gamma K\rangle<0.
\]

Compact ceilings upgrade a fixed negative moment to a robust positive-measure packet with simultaneously:

\[
\Gamma\le-\gamma_*<0,
\qquad
K\ge K_*>0.
\]

Thus strong compressive stretching and strong projective noncommutation coexist on a real enstrophy-weighted population.

## 9. Compare with enstrophy-production shell

At \(z_\omega\),

\[
\bar\Gamma(z_\omega)
=
\mathbb E_{\pi_{z_\omega}}\Gamma
>0.
\]

Therefore exactly one of the following occurs:

### Mixed-moment transition

If

\[
\mathscr M(z_\omega)\ge0,
\]

then continuity between \(z_-\) and \(z_\omega\) gives

\[
\boxed{
\exists z_M:
\mathscr M(z_M)=0.
}
\]

### Strong same-depth anti-correlation

If

\[
\mathscr M(z_\omega)<0,
\]

then

\[
\boxed{
\operatorname{Cov}_{\pi_{z_\omega}}(\Gamma,K)
<
-\bar\Gamma(z_\omega)\bar K(z_\omega).
}
\]

Thus projective noncommutation is concentrated in below-average stretching/compressive regions strongly enough to reverse the K-weighted stretching sign.

## 10. Current authoritative longitudinal frontier

The longitudinal no-crossing branch is now

\[
\boxed{
L_{\rm no-cross}
\Longrightarrow
P_{\rm existing\ analytic}
\lor
T_M
\lor
C_{\Gamma K}^{-}.
}
\]

Here:

- \(P_{\rm existing\ analytic}\): CZ / palinstrophy / raw-\(H^2\) / interface firewalls;
- \(T_M\): mixed moment zero crossing;
- \(C_{\Gamma K}^{-}\): strong same-depth anti-correlation at the positive enstrophy-production slice.

The transverse no-crossing phase is less constrained and remains separate.

## 11. Next target

M21-008 should study

\[
C_{\Gamma K}^{-}
\]

as a two-population geometry problem inside the compact similarity annulus.

The key question is whether robust:

- extensional enstrophy-production populations;
- compressive projective-strain populations;

force one of:

- a positive-thickness transition layer;
- a low-vorticity bottleneck;
- a projective-alignment separator \(K\approx0\);
- or a high spatial/angular derivative cost.

This is the current highest-value finite-depth coupling target.

\[
\boxed{\text{CURRENT TIP: M21-007 / NEXT: M21-008.}}
\]
