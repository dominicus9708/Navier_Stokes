# Exact kernel regression, relative score, and entropy-defect identity

Date: 2026-08-14

Status: **EXACT PDE IDENTITIES FOR THE TRUE ADJOINT KERNEL. COVARIANCE DEFORMATION BEYOND THE KERNEL-MEAN VELOCITY GRADIENT IS EXACTLY A RESIDUAL-VELOCITY / RELATIVE-SCORE COUPLING, AND THE NON-GAUSSIAN KL DEFECT SATISFIES AN EXACT PRODUCTION--DISSIPATION LAW. GLOBAL REGULARITY NOT PROVED.**

## 1. Backward-age kernel and moments

Let the exact adjoint density satisfy

\[
\partial_\tau\rho
=U(x,T-\tau)\cdot\nabla\rho+\nu\Delta\rho,
\qquad
\nabla\cdot U=0,
\]

with unit mass.

Define

\[
m=E_\rho X,
\qquad
Y=X-m,
\qquad
\Sigma=E_\rho[Y\otimes Y].
\]

Let

\[
\bar U=E_\rho U,
\qquad
L=E_\rho\nabla U.
\]

Then

\[
\operatorname{tr}L=0
\]

and

\[
\boxed{m'=-\bar U.}
\]

## 2. Exact velocity-regression matrix and covariance dynamics

Define the best linear regression matrix of velocity on position,

\[
\boxed{
M
:=
E_\rho[(U-\bar U)\otimes Y]\,\Sigma^{-1},
}
\]

when `Sigma` is positive definite.

Equivalently, `M` minimizes

\[
E_\rho|U-\bar U-A Y|^2
\]

over constant matrices `A`.

Ito/moment differentiation gives

\[
\boxed{
\Sigma'
=-M\Sigma-\Sigma M^T+2\nu I.
}
\]

Thus covariance shape is controlled by the regression affine drift rather than directly by the mean velocity gradient `L`.

## 3. Relative score to the covariance Gaussian

Let `G` be the Gaussian with the same mean `m` and covariance `Sigma` as `rho`. Define the relative score

\[
\boxed{
 s
:=
\nabla\log\frac{\rho}{G}
=
\nabla\log\rho+\Sigma^{-1}Y.
}
\]

The score has the exact orthogonality relations

\[
\boxed{
E_\rho s=0,
\qquad
E_\rho[Y\otimes s]=0.
}
\]

The second identity follows from

\[
E[Y_i\partial_j\log\rho]=-\delta_{ij}
\]

and

\[
E[Y_i(\Sigma^{-1}Y)_j]=\delta_{ij}.
\]

## 4. Regression gradient minus mean gradient

Integration by parts gives

\[
L_{ij}
=E[\partial_jU_i]
=-E[U_i\partial_j\log\rho].
\]

Using

\[
\partial_j\log\rho
=s_j-(\Sigma^{-1}Y)_j
\]

we obtain

\[
L=M-E[(U-\bar U)\otimes s].
\]

Define the kernel-mean affine residual velocity

\[
\boxed{
 r
:=
U-\bar U-LY.
}
\]

Since `E[Y tensor s]=0`, the affine part drops out and therefore

\[
\boxed{
M-L
=E_\rho[r\otimes s].
}
\]

This is the exact bridge between covariance deformation and non-Gaussian kernel geometry.

In particular,

\[
\boxed{
|M-L|_F
\le
\left(E_\rho|r|^2\right)^{1/2}
\left(I_{\rm rel}(\rho)\right)^{1/2},
}
\]

where

\[
\boxed{
I_{\rm rel}(\rho)
:=E_\rho|s|^2.
}
\]

Thus covariance anisotropy beyond the physical kernel-mean affine gradient requires both residual transport amplitude and non-Gaussian relative-score structure.

## 5. Relative Fisher identity

The ordinary Fisher information is

\[
I(\rho)=E|\nabla\log\rho|^2.
\]

Expanding the relative score and using integration by parts,

\[
\boxed{
I_{\rm rel}(\rho)
=I(\rho)-\operatorname{tr}(\Sigma^{-1}).
}
\]

This is nonnegative, with equality precisely for the covariance Gaussian.

## 6. Determinant evolution

From the covariance equation,

\[
\begin{aligned}
\frac d{d\tau}\log\det\Sigma
&=\operatorname{tr}(\Sigma^{-1}\Sigma')\\
&=-2\operatorname{tr}M
+2\nu\operatorname{tr}(\Sigma^{-1}).
\end{aligned}
\]

Since `tr L=0` and `M-L=E[r tensor s]`,

\[
\boxed{
\frac12\frac d{d\tau}\log\det\Sigma
=-E[r\cdot s]
+\nu\operatorname{tr}(\Sigma^{-1}).
}
\]

Thus incompressible coherent affine strain has zero trace and cannot directly alter covariance volume; volume change comes from diffusion plus the non-Gaussian residual-score coupling.

## 7. Exact KL entropy-defect equation

The covariance Gaussian has entropy

\[
h(G)
=\frac12\log[(2\pi e)^3\det\Sigma].
\]

Define the Gaussian entropy deficit

\[
\boxed{
\mathfrak D
:=D_{\rm KL}(\rho\|G)
=h(G)-h(\rho).
}
\]

For the incompressible adjoint kernel,

\[
h'(\rho)=\nu I(\rho).
\]

Therefore Sections 5--6 give

\[
\begin{aligned}
\mathfrak D'
&=
-E[r\cdot s]
+\nu\operatorname{tr}(\Sigma^{-1})
-\nu I(\rho)\\
&=
\boxed{
-E[r\cdot s]-\nu I_{\rm rel}.
}
\end{aligned}
\]

This is an exact production--dissipation identity for kernel non-Gaussianity.

## 8. Complete-square form

Pointwise in probability space,

\[
-r\cdot s-\nu|s|^2
=
\frac{|r|^2}{4\nu}
-\nu\left|s+\frac{r}{2\nu}\right|^2.
\]

Hence

\[
\boxed{
\mathfrak D'
=
\frac1{4\nu}E|r|^2
-
\nu E\left|s+\frac{r}{2\nu}\right|^2.
}
\]

Consequently

\[
\boxed{
\mathfrak D(\tau)
\le
\frac1{4\nu}
\int_0^\tau E_{\rho_s}|r(s)|^2ds,
}
\]

because the initial delta and its infinitesimal matched Gaussian have zero non-Gaussian defect in the limiting small-time sense.

This recovers the endpoint relative-entropy upper bound associated with the Girsanov path-action argument, but it is obtained directly from the Fokker--Planck PDE.

## 9. Integrated Fisher-price form

A less sharp Young inequality gives

\[
-r\cdot s
\le
\frac{|r|^2}{2\nu}
+\frac\nu2|s|^2.
\]

Thus

\[
\boxed{
\mathfrak D'
+\frac\nu2 I_{\rm rel}
\le
\frac1{2\nu}E|r|^2.
}
\]

Integrating,

\[
\boxed{
\mathfrak D(\tau)
+\frac\nu2\int_0^\tau I_{\rm rel}(s)ds
\le
\frac1{2\nu}
\int_0^\tau E|r(s)|^2ds.
}
\]

Therefore persistent non-Gaussianity pays either continuing residual transport action or relative-Fisher dissipation.

## 10. Revised kernel-deformation classification

The old qualitative branches

\[
\text{anisotropy},\quad
\text{non-Gaussianity},\quad
\text{transport}
\]

are now coupled by exact identities:

- covariance shape uses `M`;
- `M-L=E[r tensor s]`;
- non-Gaussianity uses `D`;
- `D'=-E[r dot s]-nu I_rel`.

Hence a kernel cannot sustain a covariance deformation unrelated to the physical mean gradient unless it simultaneously carries

\[
\boxed{
\text{residual velocity action}
\quad\text{and}\quad
\text{relative-score/Fisher structure}.
}
\]

The only remaining independent geometric escape is spatial non-tightness/infinite second moment, which is already a shell/transport branch.

Status: **KERNEL ANISOTROPY AND NON-GAUSSIANITY MERGED INTO A SINGLE RESIDUAL-TRANSPORT / RELATIVE-SCORE LEDGER / EXACT KL PRODUCTION--DISSIPATION IDENTITY DERIVED / GLOBAL REGULARITY NOT PROVED.**
