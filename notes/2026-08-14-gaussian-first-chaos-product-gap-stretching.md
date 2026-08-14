# Gaussian first-chaos product gap for residual stretching

Date: 2026-08-14

Status: **EXACT GAUSSIAN PRODUCT LEMMA + QUANTITATIVE HIGHER-CHAOS REQUIREMENT FOR FIRST-CHAOS STRETCHING**.

## 1. Scalar Gaussian lemma

Let `gamma` be the standard centered Gaussian measure on `R^d`. Let `f,g` be centered scalar functions in Gaussian `H^1`:

\[
\int f\,d\gamma=\int g\,d\gamma=0.
\]

Write their Hermite decompositions as

\[
f=f_1+f_h,
\qquad
g=g_1+g_h,
\]

where

\[
f_1=\Pi_1f,
\qquad
g_1=\Pi_1g,
\qquad
f_h=\Pi_{\ge2}f,
\qquad
g_h=\Pi_{\ge2}g.
\]

Define the first-Poincare excess

\[
\boxed{
H(f):=\|\nabla f\|_{L^2(\gamma)}^2-\|f\|_{L^2(\gamma)}^2
=\sum_{n\ge2}(n-1)\|\Pi_nf\|_2^2
\ge0.
}
\]

Then

\[
\boxed{
\|\Pi_1(fg)\|_2
\le
C_d\left(
\|f_1\|_2\sqrt{H(g)}
+\|g_1\|_2\sqrt{H(f)}
+\sqrt{H(f)H(g)}
\right).
}
\]

### Proof

For a first-chaos basis function `z_j`, Gaussian integration by parts gives

\[
\langle fg,z_j\rangle_\gamma
=\int \partial_j(fg)d\gamma
=\int (\partial_jf)g\,d\gamma
+\int f(\partial_jg)d\gamma.
\]

For the pure first-chaos product `f_1g_1`, the right side vanishes because `partial_j f_1` and `partial_j g_1` are constants while both `f_1` and `g_1` have zero mean. Equivalently, first chaos times first chaos contains only even Hermite degrees.

For the high-chaos pieces,

\[
\|f_h\|_2^2\le H(f),
\qquad
\|\nabla f_h\|_2^2
=\sum_{n\ge2}n\|\Pi_nf\|_2^2
\le2H(f),
\]

and similarly for `g_h`. Cauchy--Schwarz applied to the three remaining pairings yields the estimate. Summing over `j` gives the stated dimensional constant.

## 2. Matrix/vector version for residual strain and vorticity

In a whitened Gaussian frame write

\[
\delta S=S-\bar S_\gamma,
\qquad
\delta\Omega=\Omega-\bar\Omega_\gamma.
\]

Define

\[
V_S=\int|\delta S|^2d\gamma,
\qquad
V_\omega=\int|\delta\Omega|^2d\gamma,
\]

and

\[
H_S
=\int|\nabla_z\delta S|^2d\gamma-V_S,
\qquad
H_\omega
=\int|\nabla_z\delta\Omega|^2d\gamma-V_\omega.
\]

Both are nonnegative by Gaussian Poincare.

The residual-vorticity stretching term is

\[
F_{\rm str}=\delta S\,\delta\Omega.
\]

Applying the scalar lemma componentwise gives

\[
\boxed{
\|\Pi_1F_{\rm str}\|_2
\le
C\left(
\sqrt{V_S H_\omega}
+\sqrt{V_\omega H_S}
+\sqrt{H_SH_\omega}
\right).
}
\]

With a combined residual size `B` comparable to `V_S+V_omega` and combined excess `H=H_S+H_omega`, this becomes

\[
\boxed{
\|\Pi_1F_{\rm str}\|_2
\le C\left(\sqrt{BH}+H\right).
}
\]

For bounded-condition anisotropic Gaussians the same estimate holds after whitening, with constants depending on the covariance condition number.

## 3. Interpretation

A first-chaos strain/vorticity state cannot replenish first-chaos vorticity through pure first-chaos stretching:

\[
\boxed{
\Pi_1[(\delta S)_1(\delta\Omega)_1]=0.
}
\]

Any first-chaos stretching production must contain at least one higher-chaos factor, and the quantitative amount is controlled by the Gaussian Poincare excess.

This is the product-level version of the second-Hermite residual-velocity parity obstruction.

## 4. Scale-normalized consequence

At physical/Gaussian radius `R`, introduce the Navier--Stokes scale-normalized quantities

\[
\mathbb B=R^4B,
\qquad
\mathbb H=R^4H.
\]

On an `O(R^2)` scale-time slab, equivalently an `O(1)` interval in scale-normalized time, the stretching contribution to first-chaos production is bounded schematically by

\[
\boxed{
\|\Pi_1F_{\rm str}^{(R)}\|_2
\lesssim
\sqrt{\mathbb B\mathbb H}+\mathbb H.
}
\]

Suppose a surviving pulse has critical residual size `mathbb B >= 1`, a vorticity fraction

\[
\Theta=V_\omega/B,
\]

and its first-chaos vorticity component is created predominantly by local stretching during one scale-time slab, while previous-checkpoint inheritance, affine amplification, transport import, and parent-pressure forcing are negligible in that subcase. Then creation of a first-chaos amplitude comparable to

\[
\sqrt{\Theta\mathbb B}
\]

forces

\[
\boxed{
\sup_{\rm slab}\mathbb H
\gtrsim c\,\Theta
}
\]

up to fixed frame/condition constants.

Equivalently,

\[
\boxed{
\sup_{\rm slab}R^4H
\gtrsim c\,\Theta.
}
\]

This is a conditional quantitative certificate for the stretching-generated subbranch.

## 5. Channel classification

The first-chaos residual pulse can therefore change through only the following typed mechanisms:

1. local stretching with a higher-chaos certificate `R^4 H \gtrsim Theta`;
2. advection/transport, which is a scale-space import rather than pointwise vorticity-amplitude creation;
3. affine/background amplification;
4. parent/remote forcing;
5. frame/covariance degeneration.

The affine and previous-checkpoint inheritance branches are already separately constrained in the repository. The active issue is packing the higher-chaos certificate or the scale-space transport import.

## 6. Limitation

The estimate does not by itself bound the advection contribution to a moving Gaussian first-chaos coefficient. Advection is intentionally typed as a transport channel rather than merged with stretching. A global proof still requires a spacetime packing/rigidity argument for the resulting higher-chaos or transport certificates.

Status: **PURE FIRST-CHAOS STRETCH SELF-FEED CLOSED; STRETCHING-GENERATED SURVIVOR FORCES CRITICAL HIGHER-CHAOS EXCESS; TRANSPORT/PACKING REMAINS OPEN**.
