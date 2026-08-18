# Sharp Sobolev-gap constant audit against the deepest first-hitting checkpoint

Date: 2026-08-19

Status: **CONSTANT-LEVEL AUDIT. THE COHERENCE-INDUCED SOBOLEV DEFICIT IS REAL, BUT BY ITSELF IT REDUCES TO A SMALL-DATA/LOW-EARLIER-VORTICITY CONDITION RATHER THAN AN ARBITRARY-LARGE-DATA CONTRADICTION. GLOBAL REGULARITY NOT PROVED.**

## 1. Source bound without Calderon-Zygmund constants

Let

\[
E=\|\omega\|_2^2,
\qquad
P=\|\nabla\omega\|_2^2,
\qquad
\rho=|\omega|.
\]

The enstrophy source is

\[
Q=\int \omega\cdot S\omega.
\]

For divergence-free velocity on R3,

\[
\boxed{
\|S\|_2=\frac1{\sqrt2}\|\omega\|_2.
}
\]

Hence

\[
Q
\le
\|S\|_2\|\omega\|_4^2
\le
\frac1{\sqrt2}E^{1/2}
\left(\|\omega\|_2^{1/2}\|\omega\|_6^{3/2}\right).
\]

Suppose the coherence/Sobolev incompatibility yields a strict deficit

\[
\boxed{
S_3\|\rho\|_6^2
\le
(1-\theta)\|\nabla\rho\|_2^2,
\qquad 0<\theta<1.
}
\]

Since

\[
\|\nabla\rho\|_2\le\|\nabla\omega\|_2=P^{1/2},
\]

we obtain

\[
\boxed{
Q
\le
\frac1{\sqrt2}
\left(\frac{1-\theta}{S_3}\right)^{3/4}
E^{3/4}P^{3/4}.
}
\]

This avoids inserting a non-sharp Riesz-transform constant.

## 2. Source-active lower bound for enstrophy

At a right-sided enstrophy minimum or any time with

\[
E'\ge0,
\]

the enstrophy identity gives

\[
\nu P\le Q.
\]

Combining with the preceding source bound,

\[
P
\le
\frac1{4\nu^4}
\left(\frac{1-\theta}{S_3}\right)^3
E^3.
\]

On the other hand Fourier Cauchy-Schwarz gives exactly

\[
\boxed{
E^2\le\|u\|_2^2P.
}
\]

Therefore every source-active minimum obeys

\[
\boxed{
E
\ge
\frac{4\nu^4S_3^3}
{(1-\theta)^3\|u\|_2^2}.
}
\]

In terminal first-hitting normalized variables,

\[
\|U\|_2^2=\sqrt W\,\|u_{\rm phys}\|_2^2,
\]

so

\[
\boxed{
E_{\rm norm,min}
\ge
\frac{4\nu^4S_3^3}
{(1-\theta)^3\sqrt W\,\|u_0\|_2^2}.
}
\]

The strict Sobolev deficit increases the lower constant by the factor `(1-theta)^-3`.

## 3. Sharp logistic ceiling under a pointwise cap

Under the pointwise vorticity cap

\[
\|\omega\|_\infty\le M,
\]

we have

\[
\|\omega\|_4^2
\le
M\|\omega\|_2.
\]

Thus

\[
Q\le\frac1{\sqrt2}ME.
\]

Using again

\[
P\ge\frac{E^2}{\|u\|_2^2},
\]

the enstrophy equation gives the logistic inequality

\[
\boxed{
E'
\le
\sqrt2\,M E
-\frac{2\nu}{\|u\|_2^2}E^2.
}
\]

The carrying scale is

\[
\boxed{
E_{\rm eq}
=\frac{M\|u\|_2^2}{\sqrt2\,\nu}.
}
\]

At an earlier first-hitting threshold `M_-`, after the cap has persisted for the required natural interval, the clean checkpoint ceiling is therefore at this scale up to the persistence constant.

## 4. Compare at the deepest allowable checkpoint

If terminal vorticity is `W` and the previous physical threshold is `M_-`, the terminal-normalized upper scale is

\[
E_{-,\rm norm}
\lesssim
\frac{M_-\|u_0\|_2^2}{\sqrt2\,\nu\sqrt W}.
\]

The source-active lower scale is

\[
E_{\rm norm,min}
\ge
\frac{4\nu^4S_3^3}
{(1-\theta)^3\sqrt W\,\|u_0\|_2^2}.
\]

A coefficient contradiction would require

\[
\boxed{
M_-
<
\frac{4\sqrt2\,\nu^5S_3^3}
{(1-\theta)^3\|u_0\|_2^4}
}
\]

(up to the clean-checkpoint persistence constant).

This is a small-data / sufficiently-low-earlier-vorticity condition.  It is not available uniformly for arbitrary large smooth initial data.

## 5. Interpretation

The Bianchi-Egnell/coherence gap is mathematically useful because it creates a strict source coefficient deficit.  However, the deepest first-hitting logistic ceiling has exactly the same `W^-1/2` scaling as the source-active interpolation lower bound.

Therefore the final comparison is a constant comparison, and the initial kinetic-energy scale remains in the constant.  The deficit does not create a new power of `W`.

This explains why the argument does not automatically solve the large-data problem.

## 6. Correct role of the Sobolev gap

Retain the gap as a rigidity/channel-routing tool:

- a cheap projectively coherent cell cannot simultaneously saturate the generic Sobolev source estimate;
- to restore source efficiency it must enter derivative-projective mismatch, long coherent extension/L3, magnitude/angular gradient, or another already priced lane;
- repeated switching among those lanes is charged by the projective hysteresis identity.

Do not treat the coefficient gap alone as a global-regularity closure.

Status: **STRICT COEFFICIENT GAP VALID / LARGE-DATA CLOSURE FAILS AT THE SAME CRITICAL W^-1/2 SCALING / GAP RETAINED AS RIGIDITY, NOT AS A STANDALONE CONTRADICTION.**