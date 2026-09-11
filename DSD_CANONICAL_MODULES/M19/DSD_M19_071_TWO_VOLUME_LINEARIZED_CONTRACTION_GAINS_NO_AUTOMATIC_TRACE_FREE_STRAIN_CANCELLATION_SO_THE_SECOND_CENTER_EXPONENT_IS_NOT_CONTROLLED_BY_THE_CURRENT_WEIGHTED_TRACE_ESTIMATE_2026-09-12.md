# M19-071 — Two-volume linearized contraction gains no automatic trace-free strain cancellation, so the second center exponent is not controlled by the current weighted trace estimate

**Date:** 2026-09-12  
**Status:** CALCULATION / LINEAR-COCYCLE CENTER SPECTRUM / EXTERIOR-SQUARE FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-070 reformulated the final interior realizability issue as a center-spectrum problem for the linearized cocycle over the recurrent similarity hull.

Because time translation provides one zero exponent, a standard route to one-dimensional center simplicity would be to prove contraction of every two-dimensional perturbation volume:

\[
\lambda_1+\lambda_2<0.
\]

If \(\lambda_1=0\) is the time tangent, this would force \(\lambda_2<0\).

This module derives the two-volume trace identity in the M19-063 weighted geometry and tests whether incompressibility / trace-free strain yields a cancellation unavailable in the one-vector estimate.

It does not.  Global Hilbert-space orthogonality of two perturbations does not turn their pointwise quadratic tensor into the identity, so \(\operatorname{tr}S=0\) gives no automatic cancellation.  The current exterior-square bound is essentially twice the one-vector bound.

## 2. Linearized cocycle in the weighted Hilbert space

Let

\[
H_w:=L^2_\sigma(wdy),
\qquad
w=(1+\kappa|y|^2)^{-a/2}
\]

with the pressure-compatible coercive parameters of M19-063.

Along one recurrent background \(V(\theta)\), let

\[
\partial_\theta W
=\mathcal L_{V(\theta)}W
\]

be the linearized divergence-free equation.

For two linearly independent solutions \(W_1,W_2\), define their Hilbert-space parallelogram area

\[
\boxed{
\mathcal A_2
:=
\|W_1\wedge W_2\|_{\wedge^2H_w}.
}
\]

## 3. Exact two-volume logarithmic derivative

At each time choose a weighted-orthonormal basis \(e_1,e_2\) of the evolving two-dimensional subspace.  The standard exterior-power identity gives

\[
\boxed{
\frac d{d\theta}\log\mathcal A_2
=
\sum_{j=1}^2
\operatorname{Re}
\langle\mathcal L_{V(\theta)}e_j,e_j\rangle_w.
}
\]

Thus two-volume growth is controlled by the trace of the generator on the instantaneous perturbation plane.

## 4. Bare weighted similarity part

M19-063 gives, for each normalized \(e_j\),

\[
\operatorname{Re}
\langle\mathcal L_{lin}e_j,e_j\rangle_w
\le
-\nu\|\nabla e_j\|_{L^2(w)}^2
-c_{gap}.
\]

Summing,

\[
\boxed{
\sum_{j=1}^2
\operatorname{Re}
\langle\mathcal L_{lin}e_j,e_j\rangle_w
\le
-\nu\sum_{j=1}^2\|\nabla e_j\|_{L^2(w)}^2
-2c_{gap}.
}
\]

So the bare operator contributes twice the one-vector zero-order gap.

## 5. Strain trace on the perturbation plane

The linearized deformation term is

\[
-(e_j\cdot\nabla)V.
\]

Only the symmetric strain \(S_V\) contributes to its real quadratic form:

\[
\operatorname{Re}
\langle-(e_j\cdot\nabla)V,e_j\rangle_w
=
-\int e_j^TS_Ve_j\,wdy.
\]

Summing over \(j=1,2\),

\[
\boxed{
I_{str}^{(2)}
=
-\int
S_V:
\left(
 e_1\otimes e_1+e_2\otimes e_2
\right)wdy.
}
\]

Define the pointwise positive semidefinite tensor

\[
Q_2(y)
:=e_1(y)\otimes e_1(y)+e_2(y)\otimes e_2(y).
\]

Then

\[
I_{str}^{(2)}=-\int S_V:Q_2\,wdy.
\]

## 6. Why incompressibility does not cancel the strain trace

Incompressibility gives

\[
\boxed{\operatorname{tr}S_V=0.}
\]

If \(Q_2(y)\) were pointwise a scalar multiple of the identity, then

\[
S_V:Q_2=0.
\]

But weighted orthonormality only states

\[
\int e_i\cdot e_j\,wdy=\delta_{ij}.
\]

It does **not** imply any pointwise relation such as

\[
Q_2(y)=c(y)I.
\]

Therefore

\[
\boxed{
\operatorname{tr}S_V=0
\not\Rightarrow
I_{str}^{(2)}=0.
}
\]

The hoped-for two-plane trace cancellation is absent.

## 7. Global orthogonality allows local alignment with the same growing strain sector

Two globally orthogonal perturbations can be supported predominantly in different spatial regions.  At one region, \(e_1\) may align with a locally expanding direction of the variational quadratic form; at another disjoint region, \(e_2\) may align with a similarly expanding direction.

Hence global orthogonality does not force the perturbation plane to sample complementary pointwise eigenvectors of the same \(3\times3\) strain matrix.

This gives a simple structural anti-model to any argument of the form

\[
\boxed{
\text{two perturbations} + \operatorname{tr}S=0
\Longrightarrow
\text{strain cancellation}.
}
\]

Such cancellation would require additional coherent pointwise frame information not present in the Hilbert-space exterior product.

## 8. Existing nonlinear estimates simply double

Using the same transport, pressure, and strain estimates as M19-064 for each orthonormal \(e_j\), one obtains schematically

\[
\boxed{
\frac d{d\theta}\log\mathcal A_2
\le
-2c_{gap}
+2\Lambda_{NL}(\theta)
-
\frac\nu2
\sum_{j=1}^2\|\nabla e_j\|_{L^2(w)}^2.
}
\]

Dropping the nonnegative gradient term,

\[
\boxed{
\lambda_1+\lambda_2
\le
-2c_{gap}
+2\overline\Lambda_{NL}.
}
\]

This has exactly the same threshold

\[
\overline\Lambda_{NL}<c_{gap}
\]

as the one-vector contraction theorem.

Thus the current two-volume estimate does not reach a new parameter regime.

## 9. Why an orthogonality-improved gradient bound is not automatic

In a confining compact-resolvent setting, orthogonality of multiple modes can force the sum of gradient energies to increase with dimension and produce volume contraction even when the top mode is neutral.

The present polynomial \(A_2\) weight decays only like

\[
w(y)\sim |y|^{-a},
\qquad a<3,
\]

and has infinite total weighted volume.  The simple weighted energy setup does not provide a discrete Poincare eigenvalue ladder whose second eigenvalue automatically improves the two-plane estimate.

Such a spectral discreteness theorem would be an additional result, not a consequence of M19-063.

## 10. Consequence for center simplicity

The exterior-square route remains viable only if one adds structure beyond unsigned Hilbert-space estimates, for example:

- coherent pointwise alignment of perturbation planes with the strain eigenframe;
- a compact-resolvent quotient operator with a genuine second spectral gap;
- a PDE-specific symplectic/geometric cancellation;
- direct classification of bounded entire linearized solutions.

Without such input,

\[
\boxed{
\text{two-volume contraction does not prove that the time tangent is the unique center mode.}
}

## 11. Certified / not certified

### Certified

1. Exact Hilbert-space two-volume logarithmic derivative formula.
2. Bare \(A_2\) similarity gap contributes \(-2c_{gap}\).
3. The strain contribution is the contraction of trace-free \(S_V\) with the pointwise perturbation tensor \(Q_2\).
4. Global orthogonality does not make \(Q_2\) pointwise isotropic.
5. Therefore incompressibility gives no automatic two-mode strain cancellation.
6. The current two-volume estimate has the same mean-gap threshold as the one-vector estimate.

### Not certified

1. Absence of a more refined exterior-power cancellation.
2. Compact-resolvent spectral discreteness in a different quotient geometry.
3. One-dimensionality of the center cocycle.
4. Global weak-critical factor rigidity.
5. Global 3D Navier--Stokes regularity.

## 12. Next target

M19-072 should test whether the **actual scattering topology** supplies the missing compactness absent from the polynomial weighted bulk norm.

The scattering datum lives on \(\mathbb R_q\times S^2\), and the recurrent hull may have additional regularity in angular variables and locally in \(q\).  A quotient by the translation tangent could conceivably have compact embedding on a fixed \(q\)-window, producing a discrete transverse spectrum.

The calculation should separate:

1. local-window compactness, which is plausible;
2. global \(q\)-translation escape, which is exactly the critical neutral mechanism;
3. whether quotienting only the tangent derivative \(\partial_qA\), rather than all translations, leaves a compact transverse unit sphere.

If translation escape remains noncompact after tangent projection, then no compact-resolvent shortcut exists and the center theorem is genuinely global.

---

\[
\boxed{\text{M19-071 COMPLETE; THE SIMPLE TWO-VOLUME TRACE FORMULA DOES NOT CONTROL THE SECOND CENTER EXPONENT.}}
\]
