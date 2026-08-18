# Exact equal nonlinear injection into the two helical critical sectors

Date: 2026-08-18

Status: **EXACT HELICAL BALANCE IDENTITY. THE EULER/NAVIER--STOKES NONLINEARITY INJECTS THE POSITIVE H^(1/2) CRITICAL CHARGE EQUALLY INTO THE + AND - HELICAL SECTORS. A GROWING CRITICAL STACK IS THEREFORE ASYMPTOTICALLY HELICALLY BALANCED UNLESS DIFFERENTIAL VISCOUS DISSIPATION REMOVES ONE SIGN AT COMPARABLE RATE. GLOBAL REGULARITY NOT PROVED.**

## 1. Helical projectors

For divergence-free velocity define

\[
P^\pm
=\frac12\left(I\pm \Lambda^{-1}\nabla\times\right),
\qquad
u^\pm=P^\pm u,
\]

so that

\[
\nabla\times u^\pm=\pm\Lambda u^\pm.
\]

Define the positive critical sector charges

\[
\boxed{
H_\pm=\|\Lambda^{1/2}u^\pm\|_2^2.
}
\]

Then

\[
\boxed{
H_++H_-=\|u\|_{\dot H^{1/2}}^2
}
\]

and

\[
\boxed{
H_+-H_-=\int u\cdot\omega\,dx
}
\]

is the signed helicity.

## 2. Sector balances

Project Navier--Stokes onto the two helical sectors and pair with `Lambda u^pm`.  Write the nonlinear contributions as `N_pm`.  Then

\[
\frac12\dot H_+
+\nu\|\Lambda^{3/2}u^+\|_2^2
=N_+,
\]

\[
\frac12\dot H_-
+\nu\|\Lambda^{3/2}u^-\|_2^2
=N_-.
\]

The Euler nonlinearity conserves helicity exactly.  Since the nonlinear contribution to helicity is

\[
2(N_+-N_-),
\]

we obtain

\[
\boxed{N_+=N_-=:N_h.}
\]

Hence the positive critical charge satisfies

\[
\boxed{
\frac12\frac d{dt}(H_++H_-)
+\nu(D_++D_-)
=2N_h,
}
\]

where

\[
D_\pm=\|\Lambda^{3/2}u^\pm\|_2^2.
\]

The helical imbalance satisfies

\[
\boxed{
\frac12\frac d{dt}(H_+-H_-)
+\nu(D_+-D_-)=0.
}
\]

Thus the nonlinearity cannot create helical imbalance.

## 3. Consequence for a growing critical stack

Suppose the total positive critical charge

\[
H_c=H_++H_-
\]

grows without bound along a hypothetical blow-up sequence.

Every nonlinear increment `dH_c|_NL` contributes exactly half to each sign.  Therefore a persistent strongly imbalanced state can occur only if differential viscosity removes the repeatedly injected minority-sign charge at a comparable cumulative rate.

Schematically, a survivor must choose

\[
\boxed{
\text{helical balance}
\quad\lor\quad
\text{differential viscous / derivative dissipation}.
}
\]

On a low-extra-dissipation subsequence this forces

\[
\boxed{
\frac{H_+}{H_c},\frac{H_-}{H_c}\to\frac12.
}
\]

## 4. Relation to the radial-stack wall

The previous frontier required heterochiral mixing to create positive `H^(1/2)` charge.  The present identity sharpens this:

- pure homochiral creation is impossible;
- nonlinear creation is not merely mixed-sign, but exactly equal in the two positive helical sector charges;
- persistent helical imbalance is itself a viscous derivative channel.

Therefore the scalar-minimal same-scale radial stack is **helically balanced** in addition to being projectively/signed organized in physical space.

## 5. Limitation

Helical balance is compatible with localized signed-coherent vortex packets: physical-space vorticity-direction coherence does not imply a pure helical Fourier sign.  Thus this identity removes another degree of freedom but is not by itself contradictory.

Status: **EQUAL NONLINEAR +/- HELICAL CRITICAL INJECTION / SURVIVOR = HELICALLY BALANCED OR DIFFERENTIAL VISCOUS-DERIVATIVE BRANCH / GLOBAL REGULARITY NOT PROVED.**