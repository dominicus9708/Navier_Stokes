# Gaussian drift source as a Hermite gap-two transfer and curvature surplus

Date: 2026-08-14

Status: **DERIVED EXACT CHAOS-SELECTION RULE IN THE ISOTROPIC GAUSSIAN FRAME + CURVATURE-SURPLUS BOUND; BOUNDED-ANISOTROPY VERSION HOLDS UP TO CONDITION-NUMBER CONSTANTS**.

The previous source decomposition leaves

\[
J_{\rm drift}
=\int\gamma\,\delta\Omega\,
(r\cdot\nabla\log\gamma)
\]

as the narrowest untyped residual-source channel.  In Gaussian Hermite variables this term has a rigid degree structure: vorticity differentiation lowers Hermite degree by one, while Gaussian weighted divergence raises degree by one.  Therefore the drift source couples velocity chaoses separated by exactly two degrees.

This yields a quantitative bound by the curvature surplus above the Gaussian Poincare minimum.

No novelty claim is made without a separate literature-priority audit.

---

## 1. Isotropic Gaussian normalization

Let the observation Gaussian have covariance

\[
\Sigma=R^2I.
\]

Set

\[
z=\frac{x-a}{R},
\qquad
v(z)=\frac{r(a+Rz)}{R}.
\]

Then

\[
\nabla_zv=\nabla_xr,
\qquad
\nabla_z\cdot v=0.
\]

The self-consistent residual conditions imply

\[
\int\gamma v=0,
\qquad
\int\gamma\nabla v=0.
\]

Hence the Hermite expansion of `v` begins at degree two:

\[
\boxed{
v=\sum_{n\ge2}v_n.
}
\]

Moreover

\[
\delta\Omega=\nabla_z\times v.
\]

The Gaussian drift scalar is

\[
r\cdot\nabla_x\log\gamma_R
=-v\cdot z.
\]

Since `div v=0`,

\[
z\cdot v
=z\cdot v-\nabla\cdot v
=\delta_G v,
\]

where

\[
\delta_G=z\cdot-\nabla\cdot
\]

is the Gaussian divergence / creation operator, the adjoint of the Gaussian gradient.

Thus

\[
\boxed{
J_{\rm drift}
=-\int\gamma
(\nabla\times v)\,\delta_Gv.
}
\]

---

## 2. Hermite degree selection

For a pure degree-`n` Hermite vector field `v_n`,

\[
\nabla\times v_n
\in\mathcal H_{n-1},
\]

whereas

\[
\delta_Gv_n
\in\mathcal H_{n+1}.
\]

Orthogonality of distinct Gaussian chaoses therefore gives

\[
\boxed{
J_{\rm drift}
=-\sum_{m\ge2}
\int\gamma
(\nabla\times v_{m+2})
\,\delta_Gv_m.
}
\]

Only pairs of velocity Hermite degrees separated by exactly two can contribute.

In particular a residual velocity supported in a single Hermite degree has zero drift source.

---

## 3. Gradient variance and curvature

Let

\[
e_n=\|v_n\|_{L^2(\gamma)}^2.
\]

The residual gradient variance is

\[
\boxed{
B
=\int\gamma|\nabla v|_F^2
=\sum_{n\ge2}n e_n.
}
\]

Define the dimensionless Gaussian curvature

\[
\boxed{
C
=\int\gamma|D_z^2v|_F^2
=\sum_{n\ge2}n(n-1)e_n.
}
\]

Since `n>=2`, Gaussian Poincare at the residual-velocity level gives

\[
C\ge B.
\]

The strict surplus is

\[
\boxed{
C-B
=\sum_{n\ge2}n(n-2)e_n.
}
\]

It vanishes exactly on pure degree-two residual velocity.

In physical Gaussian coordinates,

\[
C=R^2D_g,
\qquad
D_g=\int\gamma_R|D_x^2r|_F^2.
\]

---

## 4. Bound the gap-two transfer by the curvature surplus

For a degree-`n` chaos,

\[
\|\nabla\times v_n\|_2^2
\le2n e_n.
\]

The creation operator from vector degree `m` to scalar degree `m+1` satisfies

\[
\|\delta_Gv_m\|_2^2
\le(m+1)e_m.
\]

Hence

\[
|J_{\rm drift}|
\le
\sum_{m\ge2}
\sqrt{2(m+2)(m+1)e_{m+2}e_m}.
\]

For `m>=2`,

\[
2(m+2)(m+1)
\le
\frac32
[(m+2)m][m].
\]

Therefore Cauchy--Schwarz over `m` yields

\[
\boxed{
|J_{\rm drift}|
\le
\sqrt{\frac32}
\sqrt{
\left(
\sum_{m\ge2}(m+2)m e_{m+2}
\right)
\left(
\sum_{m\ge2}m e_m
\right)
}
}
\]

and thus

\[
\boxed{
|J_{\rm drift}|
\le
C
\sqrt{B(C-B)}.
}
\]

Returning to physical scale,

\[
\boxed{
|J_{\rm drift}|
\le
C
\sqrt{B\left(R^2D_g-B\right)}.
}
\]

This is the main drift-to-curvature-surplus inequality.

---

## 5. Efficient drift forces strict curvature surplus

If the drift source carries a fixed efficiency fraction

\[
|J_{\rm drift}|
\ge
\eta\sqrt{V_\omega B},
\]

then

\[
\eta^2V_\omega B
\le
C B(R^2D_g-B).
\]

Thus

\[
\boxed{
R^2D_g-B
\ge
c\eta^2V_\omega.
}
\]

Writing

\[
\theta=V_\omega/B,
\]

we obtain

\[
\boxed{
D_g
\ge
\frac{B}{R^2}
\left(1+c\eta^2\theta\right).
}
\]

Therefore an efficient drift source cannot live at exact Gaussian Poincare saturation.  It requires a relative curvature surplus proportional to its vorticity share.

---

## 6. Bounded-anisotropy affine Gaussian

For a general covariance `Sigma`, whiten by the linear map

\[
z=\Sigma^{-1/2}(x-a)
\]

and transform the residual velocity by the corresponding Piola-type linear map so that divergence remains zero.

Hermite degree is preserved under the fixed linear transformation.  Spatial differentiation still lowers Gaussian chaos degree by one and Gaussian divergence raises it by one.  Vorticity components become bounded linear combinations of first derivatives, with constants controlled by the covariance condition number.

Hence on a branch with

\[
\kappa(\Sigma)\le K,
\]

the same selection rule and estimate hold up to `K`-dependent constants:

\[
\boxed{
|J_{\rm drift}|
\le
C_K
\sqrt{B\left(R_\gamma^2D_g-c_KB\right)_+}
}
\]

in an equivalent normalized formulation.

The isotropic formula above is the exact clean model; the anisotropic statement should be read with the natural quadratic forms induced by `Sigma` if exact constants are required.

---

## 7. Combined residual-source typing

The full Gaussian-mean residual source is

\[
J_{\rm str}+J_{\rm drift}.
\]

The preceding notes now give:

### Stretch-source dominance

\[
J_{\rm str}
=\int\gamma\delta S\delta\Omega
\]

forces weighted

\[
\boxed{
\text{directional stretch}
\quad\text{or}\quad
\text{axis conversion}.
}
\]

### Drift-source dominance

\[
J_{\rm drift}
\]

forces

\[
\boxed{
\text{Hermite gap-two transfer}
\quad\text{and}
\quad
\text{curvature surplus above Poincare}.
}
\]

Thus the local residual source no longer has an untyped bounded-affine escape channel.

---

## 8. Remaining issue

Typing a source channel is not yet the same as proving it cannot repeat indefinitely.

The remaining work is to convert the three typed costs

1. directional material stretch;
2. axis conversion;
3. curvature surplus / gap-two Hermite transfer;

into a common cross-checkpoint packing or rigidity contradiction.

The low-curvature corridor derived previously already restricts

\[
m=W^{-1/3}\Lambda,
\qquad
R\lesssim W^{1/6}\Lambda^{-1/5},
\qquad
\Lambda\to\infty.
\]

The present lemma implies that any pulse trying to avoid the first two geometric channels must leave the exact low-curvature boundary by an amount controlled by its vorticity share.

Status: **GAUSSIAN DRIFT SOURCE TYPED AS GAP-TWO HERMITE TRANSFER / ALL BOUNDED-AFFINE RESIDUAL SOURCE MECHANISMS NOW HAVE A GEOMETRIC OR CURVATURE WITNESS**.
