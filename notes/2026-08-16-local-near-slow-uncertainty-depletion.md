# Local near-slow uncertainty depletion on the fast-rotation branch

Date: 2026-08-16

Status: **DERIVED FOR SPATIALLY TIGHT TURNOVER-SCALE PACKETS. A NEAR-SLOW INPUT CONFINED TO THE COHERENT TURNOVER CORE CANNOT SUPPLY AN ORDER-ONE SECULAR RESIDUAL MEAN SOURCE OVER `R^2` TIME. GLOBAL REGULARITY NOT PROVED.**

## 1. Fast-rotation turnover variables

On the residual mean-creation branch, use normalized radius `R -> infinity` with

\[
B\sim R^{-2},
\]

so the residual gradient RMS is `R^-1` and the residual velocity amplitude is order one.

Use turnover variables

\[
y=Rz,
\qquad
t=R\theta.
\]

For a residual gradient component write

\[
\nabla_y r(y,t)
=R^{-1}G(z,\theta).
\]

On a spatially tight bounded branch, after a fixed smooth cutoff in `z`,

\[
\boxed{
\|G\|_{L^2_z}\le C
}
\]

on the relevant turnover-scale packet. Dyadic frequency escape away from `|xi| asymp 1` is separately routed to low-frequency spatial nontightness or high-Hermite/derivative concentration.

## 2. Near-slow spectral slab

Let the coherent rotation axis be `e`, and write

\[
\xi_\parallel=\xi\cdot e.
\]

On the fixed turnover dyadic annulus

\[
c\le|\xi|\le C,
\]

define

\[
\mathcal S_\delta
=\{\xi:|\xi_\parallel|\le\delta\}.
\]

Its frequency volume satisfies

\[
|\mathcal S_\delta|\lesssim\delta.
\]

For a spatially cutoff packet `G`,

\[
\|\widehat G\|_\infty
\le\|G\|_1
\le C\|G\|_2
\]

because the cutoff support has fixed turnover volume.

Therefore Plancherel gives

\[
\begin{aligned}
\|P_{\mathcal S_\delta}G\|_2^2
&=\int_{\mathcal S_\delta}|\widehat G(\xi)|^2d\xi\\
&\le
|\mathcal S_\delta|\,\|\widehat G\|_\infty^2\\
&\lesssim
\delta\|G\|_2^2.
\end{aligned}
\]

Hence

\[
\boxed{
\|P_{\rm slow,\delta}G\|_2
\lesssim
\delta^{1/2}\|G\|_2.
}
\]

This is a simple local uncertainty estimate: an `L2` packet confined to a fixed physical turnover region cannot also place order-one mass in a vanishing-width axial-frequency slab.

## 3. Secular fast-rotation width

In turnover variables, the Coriolis frequency is multiplied by `R`.

A near-slow input has inertial frequency

\[
|\omega(\xi)|\lesssim |\xi_\parallel|/|\xi|.
\]

To remain phase coherent for `O(R)` turnover blocks, the relevant near-slow width must satisfy

\[
\boxed{
\delta\lesssim R^{-1}.
}
\]

Therefore the spatially tight near-slow component obeys

\[
\boxed{
\|P_{\rm slow}G\|_2
\lesssim R^{-1/2}.
}
\]

## 4. Consequence for the Gaussian residual mean source

The residual covariance/mean source is quadratic in residual gradients. In original normalized variables it carries the scale factor

\[
R^{-2}.
\]

For a local bilinear interaction with one near-slow factor and one bounded turnover-scale factor,

\[
\begin{aligned}
|J_{\rm slow}|
&\lesssim
R^{-2}
\|P_{\rm slow}G_1\|_2
\|G_2\|_2\\
&\lesssim
R^{-5/2}.
\end{aligned}
\]

The mean-creation interval has length `O(R^2)` in the original normalized time. Hence

\[
\boxed{
\int_{I_R}|J_{\rm slow}|dt
\lesssim
R^2R^{-5/2}
=R^{-1/2}	o0.
}
\]

Thus a spatially tight near-slow input packet cannot supply an order-one secular residual mean-vorticity source.

## 5. Remaining routes

For near-slow concentration to remain source-active, at least one assumption of the local uncertainty estimate must fail:

1. **spatial nontightness:** the packet extends over a turnover distance tending to infinity, so its `L1/L2` localization constant is no longer uniform;
2. **low-frequency escape:** `|xi|` collapses toward zero, corresponding to a larger physical scale;
3. **high-frequency escape:** `|xi|` leaves the turnover band, activating high-Hermite/derivative concentration;
4. **localization commutator/shell forcing:** cutoff or Gaussian-tail terms carry an order-one fraction of the source.

All four are already typed channels in the proof tree.

## 6. Relation to the helical null-resonance result

The earlier helical calculation left `near-slow input concentration` as the principal exact-resonance remainder after the fast-fast slow-output null form.

The present estimate removes the **spatially tight, turnover-band** realization of that remainder.

It does not yet close general near-resonant uniformly fast interactions, because the Gaussian localized output is not literally a single global `k_parallel=0` Fourier mode. Nor does it close source carried by spatial tails or shell commutators.

## 7. Claim boundary

The result is a local harmonic-analysis depletion estimate, not a global rotating-Navier--Stokes regularity theorem. It depends on the bounded turnover-scale `L2` packet and explicit routing of cutoff/frequency escapes.

Status: **TIGHT NEAR-SLOW INPUT SOURCE DEPLETED BY A `R^-1/2` UNCERTAINTY GAIN / SURVIVORS ROUTED TO SPATIAL ESCAPE, FREQUENCY ESCAPE, OR LOCALIZATION COMMUTATOR / GLOBAL REGULARITY NOT PROVED.**