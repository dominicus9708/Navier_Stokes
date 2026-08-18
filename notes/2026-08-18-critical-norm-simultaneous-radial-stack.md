# Bounded unit-cell cascade requires a simultaneous radial critical stack

Date: 2026-08-18

Status: **CRITICAL-SPACE LITERATURE GATE + DSD BAND CONSEQUENCE. BOUNDED PER-BAND CRITICAL CHARGE CANNOT PRODUCE A SINGULARITY BY MERELY MOVING ONE PACKET TO HIGHER FREQUENCY; A HYPOTHETICAL BLOW-UP MUST ACCUMULATE AN UNBOUNDED NUMBER OF SIMULTANEOUS RADIAL CRITICAL BANDS OR MAKE SOME INDIVIDUAL BAND CHARGE DIVERGE. GLOBAL REGULARITY NOT PROVED.**

## 1. External critical-space boundary

Kenig--Koch, `An alternative approach to regularity for the Navier-Stokes equations in critical spaces` (arXiv:0908.3349; Ann. Inst. H. Poincare Anal. Non Lineaire 28 (2011), 159--187), prove in particular that a mild 3D Navier--Stokes solution which remains bounded in `dot H^(1/2)` does not develop a finite-time singularity.

Thus a hypothetical finite maximal time requires

\[
\boxed{
\limsup_{t\uparrow T^*}
\|u(t)\|_{\dot H^{1/2}}
=\infty.
}
\]

This is imported standard critical-space theory, not a DSD result.

## 2. Positive band decomposition

For physical radial shells with critical charges

\[
\mathfrak h_k
\asymp
K_k\|P_ku\|_2^2,
\]

we have

\[
\boxed{
\sum_k\mathfrak h_k
\asymp
\|u\|_{\dot H^{1/2}}^2.
}
\]

The DSD compact natural packet bridge gives, on an active bounded-amplitude unit cell,

\[
\mathfrak h_k\gtrsim c>0
\]

unless the stronger derivative/amplitude branch is already active.

## 3. One moving band is insufficient

Suppose along a candidate singular sequence each active band satisfies a uniform upper critical charge

\[
\mathfrak h_k\le C_0
\]

and only `M(t)` bands are significantly active. Then

\[
\|u(t)\|_{\dot H^{1/2}}^2
\lesssim
C_0M(t)
+\text{small tails}.
\]

Hence bounded `M(t)` would keep the critical norm bounded and is incompatible with finite-time blow-up on this bounded-per-band branch.

Therefore

\[
\boxed{
M(t)\to\infty
}
\]

along a singular sequence, unless some individual band charge itself diverges.

The latter is the already typed stronger-amplitude / concentration branch.

## 4. Radial stack, not merely a travelling packet

The minimal bounded-amplitude compact scenario is therefore not

\[
K(t)\to\infty
\quad\text{with one order-one packet},
\]

but

\[
\boxed{
\text{an unbounded simultaneous stack of active radial scales}.
}
\]

The kinetic-energy price of geometrically separated critical bands can remain finite because

\[
E_k^{\rm kin}
\asymp
\frac{\mathfrak h_k}{K_k},
\]

and

\[
\sum_jK_j^{-1}<\infty
\]

for geometric `K_j`.  Thus finite energy does not exclude such a radial stack.

## 5. Each newly active radial band must be genuinely repopulated

The exact positive moving-band equation is

\[
\frac12E_k'+\nu D_k=\Pi_k.
\]

A band rising from half to full dangerous charge pays positive nonlinear input.  The narrow-shell and radial-flux identities further show that efficient growth requires actual radial kinetic-energy transfer, not merely angular rearrangement on one Fourier sphere.

Hence the stack must be dynamically maintained by a web of radial fluxes.

## 6. Additional structure already forced on the stack

Every source-active same-scale component must also negotiate the independent structural filters already derived:

1. pure homochiral fixed-shell source is absent, so efficient critical-source growth requires heterochiral mixing;
2. projective isotropy depletes common affine stretching;
3. projective/angular roughness is directly viscously damped in the magnitude equation;
4. signed-line/polarity variation is a magnitude-gradient/flux-reset branch;
5. a common lower-frequency strain extracts a signed coherent cone subpopulation;
6. positive stretching is either positive-middle strain or positive local Betchov mismatch;
7. avoiding common-axis extraction drives the responsible strain frequency toward the packet frequency.

Thus the bounded-amplitude blow-up motif sharpens to

\[
\boxed{
\textbf{an unbounded simultaneous radial stack of}
\atop
\textbf{heterochiral, radially transferring, projectively organized high--high cells}.
}
\]

## 7. Zeno timing remains possible

The first-hitting cap bounds the natural nonlinear turnover rate at physical frequency `K` by `O(K^2)`.  Therefore an order-one band transition needs at least `cK^-2` time on a bounded-channel track.

However for `K_j=2^jK_0`,

\[
\sum_jK_j^{-2}<\infty.
\]

Thus parabolic timing alone cannot forbid the radial stack from reaching arbitrarily high scales before a finite terminal time.

Status: **TRAVELLING SINGLE-BAND PICTURE REMOVED / MINIMAL BOUNDED-AMPLITUDE BLOW-UP REQUIRES SIMULTANEOUS MULTISCALE RADIAL STACK / PARABOLIC ZENO TIMING STILL COMPATIBLE.**