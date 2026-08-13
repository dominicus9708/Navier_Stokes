# Gaussian residual variance as an exact anisotropic semigroup square function

Date: 2026-08-13

Status: **EXACT GAUSSIAN VARIANCE / CURVATURE IDENTITY / DERIVATIVE-HIERARCHY BRIDGE**.

The self-consistent Gaussian residual state is

\[
\mathcal B_\Sigma
=P_\Sigma(|g|^2)-|P_\Sigma g|^2,
\qquad
g=\nabla U,
\]

where `P_Sigma` denotes convolution with the centered Gaussian of covariance `Sigma`.

This variance admits an exact positive semigroup representation across all internal Gaussian subscales.  Consequently every nonzero four-channel residual has a curvature witness.

---

## 1. Gaussian covariance semigroup

For a positive definite covariance matrix `Sigma`, let

\[
P_\Sigma f(x)
=\int\gamma_\Sigma(y)f(x+y)dy.
\]

Covariances add:

\[
P_{\Sigma_1}P_{\Sigma_2}=P_{\Sigma_1+\Sigma_2}.
\]

The generator of the one-parameter path `P_{t Sigma}` is

\[
\mathcal A_\Sigma
=\frac12\Sigma:D^2.
\]

---

## 2. Interpolation identity

Fix `g` with values in a finite-dimensional Hilbert space and define

\[
H(t)
=P_{t\Sigma}
\left(
|P_{(1-t)\Sigma}g|^2
\right),
\qquad 0\le t\le1.
\]

Then

\[
H(0)=|P_\Sigma g|^2,
\qquad
H(1)=P_\Sigma|g|^2.
\]

Let

\[
v_t=P_{(1-t)\Sigma}g.
\]

Since

\[
\partial_t v_t=-\mathcal A_\Sigma v_t,
\]

and

\[
\mathcal A_\Sigma|v|^2
-2\langle v,\mathcal A_\Sigma v\rangle
=
\operatorname{tr}
\left[(\nabla v)\Sigma(\nabla v)^T\right],
\]

we obtain

\[
\boxed{
H'(t)
=P_{t\Sigma}
\operatorname{tr}
\left[
(\nabla v_t)\Sigma(\nabla v_t)^T
\right].
}
\]

Integrating from zero to one gives

\[
\boxed{
P_\Sigma|g|^2-|P_\Sigma g|^2
=
\int_0^1
P_{t\Sigma}
\left[
\left|\nabla P_{(1-t)\Sigma}g\,\Sigma^{1/2}\right|_F^2
\right]dt.
}
\]

This is exact.

---

## 3. Apply to the affine residual

For

\[
g=\nabla U,
\qquad
L_\Sigma=P_\Sigma(\nabla U),
\]

the Gaussian least-squares residual-gradient variance is

\[
\mathcal B_\Sigma
=P_\Sigma|\nabla U|^2-|L_\Sigma|^2.
\]

Therefore

\[
\boxed{
\mathcal B_\Sigma
=
\int_0^1
P_{t\Sigma}
\left[
\left|
\nabla^2P_{(1-t)\Sigma}U\,\Sigma^{1/2}
\right|_F^2
\right]dt.
}
\]

Combined with the exact four-channel identity,

\[
\mathcal B_\Sigma
=D_{S,\rm shape}
+D_{S,\rm amp}
+\frac12D_{\omega,\rm proj}
+\frac12D_{\omega,\rm line},
\]

this shows that every active residual branch has an exact multiscale curvature representation.

---

## 4. Curvature witness

Let

\[
\lambda_{\max}(\Sigma)=R_\Sigma^2.
\]

Since

\[
\left|
A\Sigma^{1/2}
\right|_F^2
\le
\lambda_{\max}(\Sigma)|A|_F^2,
\]

we have

\[
\int_0^1
P_{t\Sigma}
\left|
\nabla^2P_{(1-t)\Sigma}U
\right|_F^2dt
\ge
\frac{\mathcal B_\Sigma}{\lambda_{\max}(\Sigma)}.
\]

Hence if

\[
\mathcal B_\Sigma\ge b_0>0,
\]

there exists `t_* in (0,1)` such that

\[
\boxed{
P_{t_*\Sigma}
\left|
\nabla^2P_{(1-t_*)\Sigma}U
\right|_F^2
\ge
\frac{b_0}{\lambda_{\max}(\Sigma)}.
}
\]

For a well-conditioned Gaussian of width `R`, this is schematically

\[
\boxed{
|\nabla^2U_{\rm smoothed}|^2
\gtrsim
\frac{b_0}{R^2}
}
\]

at some internal subscale.

---

## 5. Single Fourier-mode audit

For a complex scalar Fourier mode

\[
g(x)=e^{ik\cdot x}
\]

set

\[
a=k^T\Sigma k.
\]

Then

\[
P_\Sigma|g|^2-|P_\Sigma g|^2
=1-e^{-a}.
\]

The square-function side is

\[
\int_0^1
 a e^{-(1-t)a}dt
=1-e^{-a}.
\]

Thus the formula has the correct normalization exactly.

---

## 6. DSD interpretation

At one observation resolution `Sigma`, the unresolved state is not an opaque residual.  It is the positive accumulation of derivative activity across all unresolved internal Gaussian resolutions.

Thus the scale graph becomes

\[
\boxed{
\text{four-channel residual at scale }\Sigma
\Longrightarrow
\text{curvature witness at some subscale}
\Longrightarrow
\text{higher-derivative channel}.
}
\]

This is an exact bridge between static aggregation and the derivative hierarchy.

---

## 7. Limitation

The identity gives a scale-critical curvature witness.  It does not by itself provide a supercritical exponent or a globally summable derivative budget.  A persistent residual can still move its curvature witness between subscales.

The next target is therefore a packing/rigidity statement for these witnesses across successive first-hitting windows or a strict contraction of the residual state under the Gaussian semigroup.

Status: **RESIDUAL-TO-CURVATURE BRIDGE CLOSED / CURVATURE-WITNESS PACKING REMAINS OPEN**.
