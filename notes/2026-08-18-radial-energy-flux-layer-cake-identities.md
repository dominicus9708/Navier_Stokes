# Radial kinetic-energy flux as the exact source of critical H^(1/2) charge and enstrophy

Date: 2026-08-18

Status: **EXACT FOURIER LAYER-CAKE / FLUX IDENTITIES. NONLINEAR GROWTH OF THE H^(1/2) CRITICAL CHARGE AND ENSTROPHY IS THE ZEROTH AND FIRST RADIAL MOMENT OF KINETIC-ENERGY FLUX TO HIGH FREQUENCIES. GLOBAL REGULARITY NOT PROVED.**

## 1. High-frequency kinetic-energy tail

Define

\[
\mathcal E_{>K}(t)
=\frac12\int_{|\xi|>K}|\widehat u(\xi,t)|^2d\xi.
\]

By the layer-cake formulas

\[
|\xi|=\int_0^{|\xi|}dK,
\qquad
|\xi|^2=\int_0^{|\xi|}2K\,dK,
\]

we have exactly

\[
\boxed{
\frac12\|u\|_{\dot H^{1/2}}^2
=\int_0^\infty\mathcal E_{>K}\,dK,
}
\]

and

\[
\boxed{
\frac12\|\omega\|_2^2
=\int_0^\infty2K\,\mathcal E_{>K}\,dK.
}
\]

## 2. Define radial nonlinear energy flux

Let the sign convention be that

\[
\Pi_E(K,t)>0
\]

means net nonlinear kinetic-energy transfer from frequencies below `K` into frequencies above `K`.  The exact high-frequency energy balance is

\[
\frac{d}{dt}\mathcal E_{>K}
+\nu\int_{|\xi|>K}|\xi|^2|\widehat u|^2d\xi
=\Pi_E(K,t).
\]

This is simply the Fourier-projected kinetic-energy equation.

## 3. Critical H^(1/2) source is the zeroth radial flux moment

Differentiate the layer-cake identity and use Tonelli/Fubini on a smooth pre-singular solution.  The nonlinear contribution is

\[
\boxed{
\mathcal T_{1/2}(t)
=\int_0^\infty\Pi_E(K,t)\,dK.
}
\]

Thus nonlinear growth of the positive `H^(1/2)` charge is exactly the integrated forward/backward radial kinetic-energy flux.

The viscous part is

\[
-\nu\|u\|_{\dot H^{3/2}}^2.
\]

Hence

\[
\boxed{
\frac12\frac d{dt}\|u\|_{\dot H^{1/2}}^2
+\nu\|u\|_{\dot H^{3/2}}^2
=\int_0^\infty\Pi_E(K,t)\,dK.
}
\]

This is the radial-flux version of the helical heterochiral-source identity.

## 4. Enstrophy source is the first radial flux moment

Similarly, the nonlinear contribution to

\[
\frac12\|\omega\|_2^2
\]

is

\[
\boxed{
Q(t)
=\int_0^\infty2K\,\Pi_E(K,t)\,dK.
}
\]

Therefore vorticity stretching production is the first radial moment of kinetic-energy flux.

This identity is equivalent to the physical-space enstrophy production formula after summing all Fourier interactions.

## 5. Structural consequences

The narrow-shell calculation showed that pure angular redistribution on one exact frequency radius cannot change either `H^(1/2)` charge or enstrophy.  The present identities show the global reason:

\[
\boxed{
\text{critical/enstrophy growth requires net radial kinetic-energy transfer.}
}
\]

For a source-active compact unit-cell cascade, the final spectral mechanism must therefore carry

- heterochiral mixing, to avoid the homochiral critical-source cancellation;
- radial energy flux, to avoid same-radius moment cancellation;
- physical-space strain/vorticity correlation, to produce positive stretching;
- projective/signed organization or pay the corresponding residual/damping costs.

## 6. Blow-up critical-norm gate

Known critical-space regularity theory states that a mild solution remaining bounded in `dot H^(1/2)` cannot develop a finite-time singularity.  Therefore any hypothetical finite-time singularity in this class must drive

\[
\|u(t)\|_{\dot H^{1/2}}\to\infty
\]

at least along a sequence approaching the maximal time.

Through the exact layer-cake identity, this requires unbounded accumulation of high-frequency kinetic-energy tails in the radial measure

\[
\int_0^\infty\mathcal E_{>K}\,dK.
\]

In the DSD moving-band language, a survivor with uniformly bounded charge per band must therefore activate an unbounded number of radial critical bands simultaneously, or else allow the charge of some individual band to diverge.

The latter is already a stronger-amplitude/derivative branch.  Thus the bounded-unit-cell scenario sharpens to a **simultaneous radial-scale stack**.

## 7. Why the flux identity alone is not a contradiction

One kinetic-energy parcel can traverse many frequency boundaries, and the energy required by a natural packet decreases like `K^-1`.  Consequently the integrated kinetic-energy cost of a geometrically accelerating Zeno cascade may remain finite.

The exact flux identity therefore identifies the mandatory mechanism but does not provide a positive budget that forbids it.

Status: **CRITICAL SOURCE IDENTIFIED EXACTLY AS RADIAL ENERGY-FLUX MOMENT / BOUNDED UNIT-CELL BLOW-UP REQUIRES AN UNBOUNDED SIMULTANEOUS RADIAL STACK OR DIVERGENT PER-BAND CHARGE.**