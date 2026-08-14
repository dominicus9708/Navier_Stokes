# Exact adjoint-kernel entropy and diffusive volume floor

Date: 2026-08-14

Status: **DERIVED FOR THE EXACT ADVECTION--DIFFUSION ADJOINT TRANSITION DENSITY, WHEN ITS SECOND MOMENT IS FINITE. INCOMPRESSIBLE DRIFT CANNOT COLLAPSE THE KERNEL BELOW DIFFUSIVE COVARIANCE VOLUME. KERNEL DEFORMATION IS THEREFORE ANISOTROPY / MULTIMODALITY / SPATIAL ESCAPE, NOT VOLUME COLLAPSE. GLOBAL REGULARITY NOT PROVED.**

## 1. Backward-age form of the exact adjoint kernel

Let

\[
\partial_t f+U\cdot\nabla f=\nu\Delta f,
\qquad \nabla\cdot U=0,
\]

and let

\[
K(x,s;x_*,T)
\]

be the backward adjoint transition density used in the exact Duhamel representation. Put

\[
\tau=T-s,
\qquad
\rho(x,\tau)=K(x,T-\tau;x_*,T).
\]

Then `rho` has unit mass and satisfies

\[
\boxed{
\partial_\tau\rho
=U(x,T-\tau)\cdot\nabla\rho
+\nu\Delta\rho.
}
\]

Equivalently, this is a forward Fokker--Planck equation with divergence-free drift `-U`.

Thus

\[
\rho\ge0,
\qquad
\int_{\mathbb R^3}\rho(x,\tau)dx=1.
\]

## 2. Incompressible transport does not change Shannon entropy

Define differential entropy

\[
\boxed{
h(\tau)=-\int\rho\log\rho\,dx.}
\]

For smooth positive `rho`, differentiation gives

\[
\begin{aligned}
h'(\tau)
&=-\int(1+\log\rho)
\left(U\cdot\nabla\rho+\nu\Delta\rho\right)dx.
\end{aligned}
\]

The transport contribution vanishes because

\[
\int U\cdot\nabla(\rho\log\rho)dx=0
\]

when `div U=0` and the kernel decays at infinity.

Integrating the diffusion term by parts yields

\[
\boxed{
h'(\tau)=\nu I(\rho_\tau),}
\]

where

\[
\boxed{
I(\rho)=\int\frac{|\nabla\rho|^2}{\rho}\,dx
}
\]

is the Fisher information.

Hence entropy growth is generated entirely by viscosity. Incompressible advection may deform the kernel, but it does not reduce its entropy.

## 3. Drift-independent entropy lower bound

The divergence-free advection--diffusion semigroup obeys the Nash ultracontractive estimate

\[
\boxed{
\|\rho(\tau)\|_\infty
\le C_\nu\tau^{-3/2}
=C(\nu\tau)^{-3/2}.
}
\]

Since `rho` is a probability density,

\[
\begin{aligned}
h(\tau)
&=-\int\rho\log\rho\\
&\ge-\log\|\rho(\tau)\|_\infty.
\end{aligned}
\]

Therefore

\[
\boxed{
h(\tau)
\ge
\frac32\log(\nu\tau)-C.}
\]

This lower bound is independent of the detailed incompressible drift.

## 4. Covariance-volume floor

Let

\[
m(\tau)=\int x\rho(x,\tau)dx
\]

and, whenever finite,

\[
\boxed{
\Sigma_K(\tau)
=
\int (x-m)\otimes(x-m)\rho(x,\tau)dx.
}
\]

Among all probability densities with a fixed covariance matrix, the Gaussian has maximal differential entropy. Hence

\[
\boxed{
 h(\tau)
\le
\frac12\log\left[(2\pi e)^3\det\Sigma_K(\tau)\right].
}
\]

Combining with the entropy lower bound,

\[
\frac12\log\left[(2\pi e)^3\det\Sigma_K\right]
\ge
\frac32\log(\nu\tau)-C.
\]

Exponentiation gives

\[
\boxed{
\det\Sigma_K(\tau)
\ge c(\nu\tau)^3.
}
\]

Define the covariance-volume radius

\[
\boxed{
R_K(\tau)
=(\det\Sigma_K(\tau))^{1/6}.
}
\]

Then

\[
\boxed{
R_K(\tau)
\ge c\sqrt{\nu\tau}.}
\]

Thus the exact nonlinear adjoint kernel cannot be compressed, in covariance volume, below the ordinary diffusive scale.

If the second moment is infinite, this is already a spatial-escape / non-tightness branch and no covariance-volume collapse is present.

## 5. What kernel deformation can still do

The determinant lower bound does **not** imply bounded condition number. A volume-preserving incompressible drift can shear a density into a highly eccentric shape while keeping entropy large.

Nor does covariance detect multiple separated lobes.

Therefore failure of Gaussian comparability is reduced to three typed possibilities:

\[
\boxed{
\text{K1. covariance anisotropy},
\qquad
\text{K2. non-Gaussian/multimodal shape},
\qquad
\text{K3. spatial non-tightness/escape}.
}
\]

There is no fourth branch in which the exact adjoint kernel simply collapses to a volume scale much smaller than `sqrt(nu tau)` in all directions.

## 6. Entropy deficit relative to the covariance Gaussian

Let `G_Sigma` be the Gaussian with the same mean and covariance as `rho`. Define

\[
\boxed{
\mathfrak D_K
:=
D_{\rm KL}(\rho\|G_\Sigma)
=
 h(G_\Sigma)-h(\rho)
\ge0.
}
\]

This is an exact non-Gaussianity channel. It vanishes if and only if the kernel is Gaussian almost everywhere.

Thus a translation-complete DSD state for the exact kernel can type its geometric loss as

\[
\boxed{
(\kappa(\Sigma_K),\ \mathfrak D_K,\ \text{tightness tail}).
}
\]

The determinant is already bounded below by diffusion and need not be kept as an independent collapse channel.

## 7. Relation to the bounded-affine Gaussian route

On the pure bounded-affine branch the exact Cauchy-frame kernel is Gaussian with bounded condition number, so

\[
\mathfrak D_K=0
\]

and the covariance chain is already exactly controlled.

For the full nonlinear flow, a failure of comparison between `K` and the matched affine Gaussian must therefore manifest through

1. large covariance anisotropy;
2. positive/non-negligible entropy deficit;
3. spatial non-tightness.

The first is naturally a deformation/strain channel; the second is a nonlinear mixing/shape channel; the third is the existing shell-import/transport channel.

Status: **EXACT ADJOINT-KERNEL VOLUME COLLAPSE EXCLUDED BY ENTROPY + NASH / REMAINING KERNEL-DEFORMATION GEOMETRY = ANISOTROPY, NON-GAUSSIANITY, OR NON-TIGHTNESS / GLOBAL REGULARITY NOT PROVED.**
