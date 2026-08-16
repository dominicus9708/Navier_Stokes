# Gaussian residual mean source as a score-cross-product flux

Date: 2026-08-16

Status: **EXACT VECTOR IDENTITY. THE GAUSSIAN RESIDUAL MEAN-VORTICITY SOURCE IS AN ANTISYMMETRIC FLUX PAIRED WITH THE GAUSSIAN SCORE. THIS EXPOSES THE TRANSVERSE-DERIVATIVE GEOMETRY NEEDED FOR SOURCE-SENSITIVE AFFINE DIFFUSION. GLOBAL REGULARITY NOT PROVED.**

## 1. Residual source

In the self-consistent Gaussian affine frame write

\[
u=a'+Ly+r,
\qquad
\Omega=\bar\Omega+\delta\Omega,
\]

with

\[
\int\gamma r=0,
\qquad
\int\gamma\nabla r=0,
\qquad
\int\gamma\delta\Omega=0.
\]

Because `Omega` is divergence free and `bar Omega` is spatially constant,

\[
\boxed{\nabla\cdot\delta\Omega=0.}
\]

The mean residual vorticity source previously reduced to

\[
\boxed{
J
=
\int\gamma(\delta\Omega\cdot\nabla)r\,dy
+
\int\gamma\,\delta\Omega
(r\cdot\nabla\log\gamma)\,dy.
}
\]

Let the Gaussian score be

\[
\boxed{s(y)=\nabla\log\gamma(y).}
\]

## 2. Integrate the first term exactly by parts

For component `i`,

\[
\int\gamma\,\delta\Omega_j\partial_jr_i\,dy
=
-\int r_i\partial_j(\gamma\delta\Omega_j)\,dy.
\]

Since `div deltaOmega=0`,

\[
\partial_j(\gamma\delta\Omega_j)
=\gamma\delta\Omega\cdot s.
\]

Hence

\[
\boxed{
\int\gamma(\delta\Omega\cdot\nabla)r\,dy
=-\int\gamma\,r(\delta\Omega\cdot s)\,dy.
}
\]

Therefore

\[
\boxed{
J
=
\mathbb E_\gamma
\left[
\delta\Omega(r\cdot s)
-r(\delta\Omega\cdot s)
\right].
}
\]

Using the vector triple-product identity,

\[
s\times(\delta\Omega\times r)
=\delta\Omega(s\cdot r)-r(s\cdot\delta\Omega),
\]

we obtain the compact exact form

\[
\boxed{
J
=
\mathbb E_\gamma
\left[
s\times(\delta\Omega\times r)\right].
}
\]

## 3. Directional form

For any unit vector `e`,

\[
\boxed{
 e\cdot J
=
\mathbb E_\gamma
\left[
(e\times s)\cdot(\delta\Omega\times r)
\right].
}
\]

Thus the component of the residual source along `e` uses only the score **transverse** to `e`.

In particular, no score derivative parallel to `e` enters `e dot J` directly.

## 4. Gaussian covariance form

For a centered Gaussian

\[
\gamma=N(0,\Sigma),
\]

\[
\boxed{s=-\Sigma^{-1}y,}
\]

and

\[
\boxed{
\mathbb E_\gamma[s\otimes s]=\Sigma^{-1}.
}
\]

Therefore

\[
\boxed{
\mathbb E_\gamma|e\times s|^2
=
\operatorname{tr}(\Sigma^{-1})
-e^T\Sigma^{-1}e.
}
\]

The source direction is therefore coupled explicitly to the two inverse covariance directions transverse to the output direction.

## 5. Elementary source bound from the identity

Cauchy--Schwarz gives

\[
\boxed{
|e\cdot J|
\le
\left(
\operatorname{tr}(\Sigma^{-1})-e^T\Sigma^{-1}e
\right)^{1/2}
\left(
\mathbb E_\gamma|\delta\Omega\times r|^2
\right)^{1/2}.
}
\]

On a first-hitting window `|Omega|<=1`, `|deltaOmega|` is bounded by a universal constant. Hence

\[
\mathbb E|\delta\Omega\times r|^2
\lesssim\mathbb E|r|^2.
\]

Gaussian Poincare and the affine orthogonality of `r` give

\[
\mathbb E|r|^2
\le
\lambda_{\max}(\Sigma)
\mathbb E|\nabla r|^2
=
\lambda_{\max}(\Sigma)B.
\]

Thus

\[
\boxed{
|e\cdot J|
\lesssim
\left[
\lambda_{\max}(\Sigma)
\left(
\operatorname{tr}(\Sigma^{-1})-e^T\Sigma^{-1}e
\right)
B
\right]^{1/2}.
}
\]

This bound is intentionally not claimed to improve the existing `|J|lesssim B` estimate in every geometry; in a strongly anisotropic Gaussian the covariance factor may be large.

## 6. Why the identity matters for affine deformation

Suppose an affine transition has singular values

\[
\sigma_1\ge\sigma_2\ge\sigma_3,
\qquad
\sigma_1\sigma_2\sigma_3=1.
\]

A source component subsequently amplified along the principal output direction `e_1` is controlled by the Gaussian score in the **other two** directions.

This is the correct source-sensitive counterpart of the older affine diffusion observation: incompressible amplification in one direction is accompanied by heat smoothing in transverse/compressive directions.

However there is a hard geometric split:

1. if only `sigma1` is very large, both transverse directions are candidates for strong score/diffusion control;
2. if `sigma1` and `sigma2` are both large, only the third direction is strongly compressed and the problem becomes the old biaxial extensional-plane branch.

Thus the identity does not by itself close arbitrary affine deformation. It identifies exactly why the remaining singular-value split should be **uniaxial-like versus biaxial extension**.

## 7. Relation to the curl form of the residual forcing

The full residual vorticity forcing is

\[
 f_{\rm res}
=(\Omega\cdot\nabla)r-(r\cdot\nabla)\Omega
=\nabla\times(r\times\Omega).
\]

The score-cross-product identity is the Gaussian-mean analogue of this curl structure. Both facts say that source into a selected direction necessarily uses derivatives/flux in transverse directions.

This alignment is important for a future source-sensitive affine Duhamel estimate: the same transverse directions that appear in the curl/source are the directions in which incompressible affine extension produces enhanced heat smoothing.

## 8. Current implication

Combine the exact source geometry with the newly derived small-seed deformation barrier

\[
\mathcal B_R\le R^{-\gamma}
\Longrightarrow
q_*\gtrsim R^\gamma.
\]

The remaining small-seed problem can now be split by the second singular value of the responsible transition:

\[
\boxed{
\sigma_2\ \text{moderate}
\quad\lor\quad
\sigma_2\ \text{large}.
}
\]

The first is a source-transverse two-direction smoothing problem. The second is a biaxial compression-diffusion / long-reservoir problem.

Status: **RESIDUAL SOURCE ANTISYMMETRY EXPOSED EXACTLY / SOURCE DIRECTION COUPLED TO TRANSVERSE GAUSSIAN SCORE / SMALL-SEED DEFORMATION NOW ROUTED TO UNIAXIAL-LIKE OR BIAXIAL DIFFUSION GEOMETRY.**
