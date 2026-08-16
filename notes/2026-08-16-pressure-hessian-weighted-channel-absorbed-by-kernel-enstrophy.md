# Weighted pressure-Hessian channel is absorbed by kernel-weighted enstrophy

Date: 2026-08-16

Status: **DERIVED UNDER THE TERMINAL FIRST-HITTING VORTICITY CAP AND BOUNDED-CONDITION ADJOINT GAUSSIAN. THE WEIGHTED PRESSURE-HESSIAN VARIANCE USED IN THE RESIDUAL-VARIANCE EQUATION IS CONTROLLED BY THE EXISTING KERNEL-WEIGHTED ENSTROPHY ACTION. PRESSURE-HESSIAN CONCENTRATION IS NOT AN INDEPENDENT FINAL ESCAPE ON THIS BRANCH. GLOBAL REGULARITY NOT PROVED.**

## 1. Pressure Hessian from the quadratic velocity gradient

For incompressible Navier--Stokes,

\[
-\Delta P
=\partial_iU_j\,\partial_jU_i.
\]

Calderon--Zygmund gives

\[
\|\nabla^2P\|_2
\le
C\|\nabla U\otimes\nabla U\|_2
\le
C\|\nabla U\|_4^2.
\]

Because `nabla U` is a zero-order singular integral of vorticity,

\[
\|\nabla U\|_4
\le C\|\Omega\|_4.
\]

Hence

\[
\boxed{
\|\nabla^2P\|_2
\lesssim
\|\Omega\|_4^2.
}
\]

## 2. First-hitting amplitude cap

On the terminal first-hitting interval,

\[
\|\Omega\|_\infty\le1.
\]

Let

\[
E(\tau)=\|\Omega\|_2^2.
\]

Interpolation gives

\[
\|\Omega\|_4^4
\le
\|\Omega\|_\infty^2\|\Omega\|_2^2
\le E.
\]

Therefore

\[
\boxed{
\|\nabla^2P\|_2^2
\lesssim E.
}
\]

No derivative norm beyond global enstrophy is required for this estimate.

## 3. Gaussian pressure-Hessian variance

Let `gamma_tau` be the bounded-condition backward affine/adjoint Gaussian of age `tau`, and define

\[
\Pi_P(\tau)^2
=
\int\gamma_\tau
\left|
\nabla^2P-(\nabla^2P)_{\gamma_\tau}
\right|^2dx.
\]

Variance is bounded by the second moment:

\[
\Pi_P^2
\le
\int\gamma_\tau|\nabla^2P|^2dx.
\]

The bounded-condition Gaussian has heat-kernel ceiling

\[
\|\gamma_\tau\|_\infty
\lesssim_K
(\nu\tau)^{-3/2}.
\]

Thus

\[
\boxed{
\Pi_P(\tau)^2
\lesssim_{K,\nu}
\tau^{-3/2}E(\tau).
}
\]

## 4. The exact weight appearing in residual-variance dynamics

The Gaussian residual-variance inequality contains pressure through

\[
\int \tau\,\Pi_P(\tau)^2d\tau.
\]

Using the previous estimate,

\[
\boxed{
\int_0^L\tau\,\Pi_P(\tau)^2d\tau
\lesssim_{K,\nu}
\int_0^L\tau^{-1/2}E(\tau)d\tau.
}
\]

Define the already-established kernel-weighted enstrophy action

\[
\mathfrak Z_K(L)
:=
\int_0^L\tau^{-1/2}E(\tau)d\tau.
\]

Then

\[
\boxed{
\int_0^L\tau\,\Pi_P^2d\tau
\lesssim_{K,\nu}
\mathfrak Z_K(L).
}
\]

## 5. Routing consequence

Earlier kernel analysis already showed that a non-negligible `Z_K` must realize itself as either

\[
\boxed{
\text{mesoscopic ordinary enstrophy-time occupancy}
}
\]

or

\[
\boxed{
\text{terminal global enstrophy concentration}
\Rightarrow
\text{productive middle-strain escalation}.
}
\]

Therefore weighted pressure-Hessian concentration cannot be retained as a separate final branch.

The residual-variance terminal-collapse alternative sharpens from

\[
\text{V2/high-curvature}
\lor
\text{pressure-Hessian}
\lor
\text{affine deformation}
\]

to

\[
\boxed{
\text{V2/high-curvature}
\lor
\text{ordinary/kernel-weighted enstrophy concentration}
\lor
\text{affine deformation}.
}
\]

## 6. Claim boundary

The estimate uses:

1. the global first-hitting cap `||Omega||_infinity<=1`;
2. whole-space Calderon--Zygmund estimates;
3. a bounded-condition Gaussian kernel so that `||gamma_tau||_infinity <= C tau^-3/2`.

It does not prove that `Z_K` is finite uniformly along a hypothetical blowup sequence. Instead it identifies pressure-Hessian forcing with an already existing critical enstrophy channel.

Status: **WEIGHTED PRESSURE-HESSIAN VARIANCE ABSORBED BY KERNEL-WEIGHTED ENSTROPHY / NO INDEPENDENT PRESSURE FINAL BRANCH ON THE BOUNDED-CONDITION FIRST-HITTING TRACK / GLOBAL REGULARITY NOT PROVED.**