# Frozen mean-vorticity skew coupling is unitary and heat-commuting

Date: 2026-08-14

Status: **EXACT FOR FROZEN EUCLIDEAN MEAN VORTICITY. THE LINEAR MEAN-VORTICITY/RESIDUAL COUPLING CANNOT CREATE GLOBAL RESIDUAL ENSTROPHY OR GLOBAL GAUSSIAN SCALE VARIANCE. LOCAL GAIN IS PURE SPATIAL/SCALE REDISTRIBUTION. GLOBAL REGULARITY NOT PROVED.**

## 1. Linear mean-vorticity coupling

Let `eta` be a divergence-free residual vorticity and let `r` be its Biot--Savart velocity,

\[
\nabla\times r=\eta,
\qquad
\nabla\cdot r=0.
\]

Fix a constant mean-vorticity vector `Omega0`. Define

\[
\boxed{
K_{\Omega_0}\eta
:=(\Omega_0\cdot\nabla)r.
}
\]

In Fourier variables,

\[
\widehat r(k)
=
\frac{i k\times\widehat\eta(k)}{|k|^2},
\]

so

\[
\boxed{
\widehat{K_{\Omega_0}\eta}(k)
=-\frac{\Omega_0\cdot k}{|k|^2}
\bigl(k\times\widehat\eta(k)\bigr).
}
\]

## 2. Exact skew-adjointness

For each nonzero `k`, the matrix

\[
v\mapsto k\times v
\]

is real skew-symmetric, while

\[
-(\Omega_0\cdot k)/|k|^2
\]

is real. Hence the Fourier symbol of `K_Omega0` is skew-Hermitian on the divergence-free plane.

Therefore

\[
\boxed{
K_{\Omega_0}^*=-K_{\Omega_0}
}
\]

on `L2_sigma(R3)`, and

\[
\boxed{
\frac d{dt}\|\eta\|_2^2=0
\qquad
(\partial_t\eta=K_{\Omega_0}\eta).
}
\]

The apparently large local term

\[
\delta S\,\Omega_0
\]

must therefore be kept together with

\[
\frac12\delta\Omega\times\Omega_0;
\]

their sum is the skew operator above. Separating only the symmetric piece gives a misleading impression of linear amplitude production.

## 3. Exact commutation with isotropic heat

`K_Omega0` is a Fourier multiplier depending only on `k`, and the heat semigroup has scalar multiplier

\[
e^{-\nu t|k|^2}.
\]

Hence

\[
\boxed{
[K_{\Omega_0},e^{\nu t\Delta}]=0.
}
\]

Consequently the linear frozen evolution

\[
\partial_t\eta
=K_{\Omega_0}\eta+\nu\Delta\eta
\]

has the exact propagator

\[
\boxed{
\eta(t)
=e^{tK_{\Omega_0}}
 e^{\nu t\Delta}\eta(0).
}
\]

The first factor is unitary and the second is contractive.

Thus the frozen mean-vorticity coupling does not weaken heat contraction in any global Sobolev norm:

\[
\boxed{
\|\nabla^s\eta(t)\|_2
=
\|\nabla^s e^{\nu t\Delta}\eta(0)\|_2
}
\]

for every derivative order for which the norm is finite.

## 4. Integrated Gaussian scale variance

For isotropic Gaussian/heat smoothing `P_Sigma`, define the pointwise variance

\[
B_\Sigma[\eta](a)
=P_\Sigma|\eta|^2(a)
-|P_\Sigma\eta(a)|^2.
\]

Integrating over all centers and using preservation of spatial integrals by Gaussian convolution,

\[
\boxed{
\int_{\mathbb R^3}B_\Sigma[\eta](a)da
=
\|\eta\|_2^2
-
\|P_\Sigma\eta\|_2^2.
}
\]

Because `K_Omega0` is unitary and commutes with `P_Sigma`,

\[
\|e^{tK}\eta\|_2=\|\eta\|_2,
\qquad
\|P_\Sigma e^{tK}\eta\|_2
=
\|e^{tK}P_\Sigma\eta\|_2
=
\|P_\Sigma\eta\|_2.
\]

Therefore

\[
\boxed{
\int B_\Sigma[e^{tK}\eta](a)da
=
\int B_\Sigma[\eta](a)da.
}
\]

So the skew coupling cannot create even the **globally integrated Gaussian residual variance at a fixed scale**.

## 5. Add heat

For the full frozen linear propagator,

\[
U_t=e^{tK}e^{\nu t\Delta},
\]

we obtain

\[
\int B_\Sigma[U_t\eta]da
=
\|e^{\nu t\Delta}\eta\|_2^2
-
\|P_\Sigma e^{\nu t\Delta}\eta\|_2^2.
\]

Both terms are governed entirely by heat. In particular the skew factor does not generate a hidden global variance source.

Thus

\[
\boxed{
\text{frozen mean rotation}
=
\text{unitary redistribution only},
}
\]

while

\[
\boxed{
\text{heat}
=
\text{the only linear contraction mechanism}.
}
\]

## 6. What local first-hitting concentration means

A local Gaussian window can still see its variance increase under `e^{tK}` because multiplication/localization does not commute with the nonlocal skew operator.

But the exact global identity shows that such a local increase must be balanced by loss elsewhere at the same scale. Therefore it is not creation; it is

\[
\boxed{
\text{spatial/spectral import of pre-existing residual variance}.
}
\]

This aligns with the material-center reclassification of the quadratic `Ab` term as translation/import rather than amplification.

## 7. Bounded-affine extension

In the co-affine Cauchy frame, pure affine+heat evolution is already an exact anisotropic Gaussian Markov propagator. A time-dependent mean-vorticity skew term remains.

Frozen on one short bounded-condition block, the present theorem applies after the bounded linear coordinate change. The non-frozen error consists only of

1. variation of the mean-vorticity axis/amplitude;
2. variation of the affine metric in the Biot--Savart symbol;
3. nonlinear residual terms.

These are typed respectively as axis/projective change, bounded-affine metric commutator, and genuine nonlinear source.

The frozen skew itself is removed from the production ledger.

Status: **FROZEN MEAN-VORTICITY LINEAR COUPLING CLOSED AS UNITARY HEAT-COMMUTING REDISTRIBUTION / GLOBAL FIXED-SCALE GAUSSIAN VARIANCE IS INVARIANT UNDER THE SKEW FACTOR / ANY LOCAL GAIN IS IMPORT / GLOBAL REGULARITY NOT PROVED.**
