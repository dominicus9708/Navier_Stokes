# Divergence-free projective coherence is quantitatively incompatible with sharp Sobolev saturation

Date: 2026-08-18

Status: **DERIVED COEFFICIENT-GAP LEMMA USING THE BIANCHI--EGNELL QUANTITATIVE STABILITY THEOREM. IF VORTICITY AND ITS FIRST-DERIVATIVE VECTOR CONTENT ARE BOTH COHERENT ABOUT ONE FIXED PROJECTIVE AXIS, DIVERGENCE-FREE FORCES THE VORTICITY MAGNITUDE TO BE NEARLY INVARIANT ALONG THAT AXIS. SUCH A MAGNITUDE IS A FIXED POSITIVE DISTANCE FROM THE AUBIN--TALENTI SOBOLEV EXTREMAL MANIFOLD, SO THE SCALAR SOBOLEV STEP IN THE VORTEX-STRETCHING SOURCE HAS A UNIFORM STRICT COEFFICIENT DEFICIT. THE ESCAPE IS DERIVATIVE PROJECTIVE / COVARIANCE-MISMATCH CONCENTRATION. GLOBAL REGULARITY NOT PROVED.**

## 1. Projective decomposition around one axis

Fix a unit vector `e` and decompose the divergence-free vorticity as

\[
\boxed{
\omega=a e+b,
\qquad
b\cdot e=0.
}
\]

Choose coordinates with `e=e_3`.  Since

\[
\nabla\cdot\omega=0,
\]

we have exactly

\[
\boxed{
\partial_3 a=-\nabla_\perp\cdot b.
}
\]

Let

\[
\rho=|\omega|.
\]

The Kato pointwise inequality gives

\[
|\partial_3\rho|
\le
|\partial_3\omega|.
\]

Moreover

\[
\|\partial_3 a\|_2
\le
\|\nabla_\perp b\|_2
\le
\|\nabla b\|_2,
\]

and

\[
\|\partial_3b\|_2\le\|\nabla b\|_2.
\]

Hence

\[
\boxed{
\|\partial_e\rho\|_2
\le
\|\partial_e\omega\|_2
\le
\sqrt2\,\|\nabla b\|_2.
}
\]

Thus zeroth-order projective coherence plus small first-derivative transverse content makes the scalar magnitude nearly invariant along the preferred vorticity axis.

## 2. Directional derivative of every Sobolev extremal

In three dimensions the sharp homogeneous Sobolev inequality is

\[
S\|f\|_6^2\le\|\nabla f\|_2^2.
\]

Its nonzero extremals form the Aubin--Talenti manifold `M`, obtained from one radial profile by translation, isotropic dilation, multiplication, and sign.

For every `phi in M` and every unit direction `e`, radial symmetry gives

\[
\boxed{
\|\partial_e\phi\|_2^2
=\frac13\|\nabla\phi\|_2^2.
}
\]

## 3. Elementary positive distance from the extremal manifold

Normalize

\[
\|\nabla f\|_2=1
\]

and suppose

\[
\|\partial_e f\|_2\le\varepsilon.
\]

For any Sobolev extremal `phi`, write

\[
a=\|\nabla\phi\|_2.
\]

Then reverse triangle gives

\[
\|\nabla(f-\phi)\|_2
\ge|1-a|.
\]

Using the directional derivative,

\[
\|\nabla(f-\phi)\|_2
\ge
\|\partial_e(f-\phi)\|_2
\ge
\frac{a}{\sqrt3}-\varepsilon.
\]

Therefore

\[
\|\nabla(f-\phi)\|_2
\ge
\max\left\{|1-a|,\frac{a}{\sqrt3}-\varepsilon\right\}.
\]

For `0<=epsilon<1/sqrt3`, minimizing the right-hand side over `a>=0` yields

\[
\boxed{
\operatorname{dist}_{\dot H^1}(f,\mathcal M)
\ge
\delta_\varepsilon
:=
\frac{1-\sqrt3\,\varepsilon}{1+\sqrt3}>0.
}
\]

By homogeneity, for general nonzero `f`,

\[
\boxed{
\operatorname{dist}_{\dot H^1}(f,\mathcal M)
\ge
\delta_\varepsilon\|\nabla f\|_2
}
\]

whenever

\[
\|\partial_e f\|_2
\le
\varepsilon\|\nabla f\|_2.
\]

## 4. Bianchi--Egnell stability gives a strict Sobolev coefficient

Bianchi and Egnell proved the quantitative stability estimate

\[
\boxed{
\|\nabla f\|_2^2-S\|f\|_6^2
\ge
\alpha_{BE}
\operatorname{dist}_{\dot H^1}(f,\mathcal M)^2
}
\]

for some universal `alpha_BE>0` in dimension three.

Reference: G. Bianchi and H. Egnell, *A note on the Sobolev inequality*, Journal of Functional Analysis 100 (1991), 18--24, DOI 10.1016/0022-1236(91)90099-Q.

Consequently, under the directional-invariance hypothesis,

\[
\boxed{
S\|f\|_6^2
\le
\left(1-\alpha_{BE}\delta_\varepsilon^2\right)
\|\nabla f\|_2^2.
}
\]

Set

\[
\theta_\varepsilon
=\alpha_{BE}\delta_\varepsilon^2>0.
\]

Then

\[
\boxed{
\|f\|_6
\le
S^{-1/2}(1-\theta_\varepsilon)^{1/2}
\|\nabla f\|_2.
}
\]

## 5. Apply to the vorticity magnitude

Take

\[
f=\rho=|\omega|.
\]

If

\[
\frac{\sqrt2\|\nabla b\|_2}{\|\nabla\rho\|_2}
\le\varepsilon<1/\sqrt3,
\]

then

\[
\boxed{
\|\omega\|_6
=\|\rho\|_6
\le
S^{-1/2}(1-\theta_\varepsilon)^{1/2}
P_{\rm mag}^{1/2}.
}
\]

The standard source estimate

\[
|Q|
\le C_R\|\omega\|_3^3
\le
C_R E^{3/4}\|\omega\|_6^{3/2}
\]

therefore sharpens to

\[
\boxed{
|Q|
\le
C_*\,
(1-\theta_\varepsilon)^{3/4}
E^{3/4}P_{\rm mag}^{3/4}.
}
\]

This is a **uniform coefficient deficit** relative to the generic scalar-Sobolev source estimate.

## 6. Escape = derivative projective mismatch

The hypothesis can fail because

\[
\|\nabla b\|_2
\not\ll
\|\nabla\rho\|_2.
\]

If the zeroth-order covariance `C_0` is close to `e outer e` while a fixed fraction of first-derivative energy lies transverse to `e`, then the derivative covariance `C_1` is not close to `C_0` and/or has a nontrivial first-derivative projective defect.

This is exactly the channel charged by the positive viscous terms in the energy-weighted projective identity:

\[
\nu E_1J_1
\]

and

\[
\nu E_1\|C_1-C_0\|_F^2.
\]

Thus the coherent source-saturation branch has the trichotomy

\[
\boxed{
\text{derivative-axis coherence}
\Rightarrow
\text{strict Sobolev source deficit},
}
\]

or

\[
\boxed{
\text{derivative projective / covariance mismatch cost}.
}
\]

Angular palinstrophy remains an additional direct damping branch if the zeroth-order direction field itself is not coherent.

## 7. Why this matters

The previous compact endgame repeatedly encountered critical inequalities with the correct exponents but no strict margin.  The present result gives a genuine coefficient-level incompatibility between two simultaneous saturation requirements:

1. projective/divergence-free coherence of a cheap dangerous packet;
2. near saturation of the scalar Sobolev step needed for maximal nonlinear source efficiency.

A cheap coherent tube cannot also behave like an Aubin--Talenti Sobolev bubble unless derivative-projective concentration appears.

## 8. Limitation

A strict coefficient smaller than the generic Sobolev constant does not by itself imply that viscosity dominates vortex stretching for arbitrary viscosity/data.  The remaining Calderon--Zygmund/source constants and other nonlocal strain components still matter.

Therefore this is a simultaneous-saturation gap, not a global regularity proof.

Status: **DIVERGENCE-FREE COHERENCE + DERIVATIVE-AXIS COHERENCE => UNIFORM BIANCHI--EGNELL SOBOLEV DEFICIT / ESCAPE = DERIVATIVE PROJECTIVE MISMATCH / GLOBAL REGULARITY NOT PROVED.**