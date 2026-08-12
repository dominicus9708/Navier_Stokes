# Optimal off-axis enstrophy: exact strain-axis identity and Riccati dissipation

Date: 2026-08-13

Status: **DERIVED FIXED-AXIS IDENTITIES + OPTIMAL-AXIS Dini INEQUALITY / COROLLARY OF EXTERNAL MILLER CRITERION / GLOBAL REGULARITY NOT PROVED**.

This note returns from the covariance defect to its most direct geometric representative:

\[
\boxed{
O(t)=\min_{|n|=1}\|n\times\omega(t)\|_2^2.
}
\]

For the principal covariance axis,

\[
O=E\Pi,
\]

so `O` is uniformly equivalent to the energy-weighted projective defect `D=EJ`.

## 1. Fixed-axis off-axis enstrophy

Fix a unit vector `n` that is constant in space and, for the moment, constant in time. Define

\[
f_n=n\times\omega,
\qquad
O_n=\|f_n\|_2^2.
\]

Because `n` is constant,

\[
\nabla f_n=n\times\nabla\omega.
\]

Taking `n x` of the vorticity equation and testing against `f_n`, the transport term vanishes after whole-space integration. Hence

\[
\boxed{
\frac12\frac d{dt}O_n
+\nu\|\nabla f_n\|_2^2
=
\int
(n\times\omega)\cdot(n\times S\omega)dx.
}
\]

Using

\[
(n\times a)\cdot(n\times b)
=a\cdot b-(n\cdot a)(n\cdot b),
\]

the source is precisely the production of vorticity lying outside the axis `n`.

## 2. Exact Fourier identity for the strain acting on a constant axis

For incompressible flow,

\[
\widehat u(\xi)
=\frac{i\,\xi\times\widehat\omega(\xi)}{|\xi|^2}
\]

up to the harmless Fourier-sign convention.

The Fourier transform of `S n` is

\[
\widehat{S n}
=\frac{i}{2}
\left[
(\xi\cdot n)\widehat u
+\xi(\widehat u\cdot n)
\right].
\]

Let

\[
e=\xi/|\xi|,
\qquad
e\cdot\widehat\omega=0.
\]

Then, after substituting the Biot--Savart relation,

\[
4|\widehat{S n}|^2
=
(e\cdot n)^2|\widehat\omega|^2
+
[(e\times\widehat\omega)\cdot n]^2.
\]

In the orthogonal frame

\[
\left
e,
\frac{\widehat\omega}{|\widehat\omega|},
\frac{e\times\widehat\omega}{|\widehat\omega|}
\right,
\]

the right-hand side equals

\[
|n\times\widehat\omega|^2.
\]

Therefore pointwise in frequency,

\[
\boxed{
4|\widehat{S n}(\xi)|^2
=|n\times\widehat\omega(\xi)|^2.
}
\]

By Plancherel,

\[
\boxed{
\|S n\|_2^2
=\frac14\|n\times\omega\|_2^2.
}
\]

More generally, because spatial derivatives commute with the Fourier multipliers,

\[
\boxed{
\|D^{(k)}(S n)\|_2^2
=\frac14\|D^{(k)}(n\times\omega)\|_2^2
}
\]

for the ordered derivative norm convention.

This identity is recorded without a novelty claim; it is an exact structural consequence of incompressibility and the strain-vorticity Fourier relation.

## 3. `H^{-1}` interpolation gives Riccati coercivity

For

\[
f_n=n\times\omega,
\]

we have pointwise in Fourier

\[
|\widehat f_n|
\le|\widehat\omega|
=|\xi|\,|\widehat u|
\]

for divergence-free velocity. Hence

\[
\boxed{
\|f_n\|_{\dot H^{-1}}
\le\|u\|_2.
}
\]

By homogeneous Sobolev duality,

\[
\|f_n\|_2^2
\le
\|f_n\|_{\dot H^{-1}}
\|\nabla f_n\|_2.
\]

Therefore

\[
\boxed{
\|\nabla f_n\|_2^2
\ge
\frac{O_n^2}{\|u\|_2^2}.
}
\]

The kinetic-energy law gives

\[
\|u(t)\|_2^2\le\|u_0\|_2^2=:U_0.
\]

Thus the fixed-axis balance implies

\[
\boxed{
\frac d{dt}O_n
+\frac{2\nu}{U_0}O_n^2
\le
2\sqrt{O_n}\,\|S\omega\|_2.
}
\]

## 4. Optimize the axis at each time without differentiating the eigenvector

Define

\[
O(t)=\min_{|n|=1}O_n(t).
\]

At each time choose any minimizing axis `n_t`. The minimizer exists by compactness of the sphere.

For `h>0`,

\[
O(t+h)
\le O_{n_t}(t+h),
\qquad
O(t)=O_{n_t}(t).
\]

Therefore the upper right Dini derivative satisfies

\[
D_t^+O(t)
\le
\frac d{dt}O_{n_t}(t)
\]

whenever the fixed-axis derivative exists.

Consequently,

\[
\boxed{
D_t^+O
+\frac{2\nu}{U_0}O^2
\le
2\sqrt O\,\|S\omega\|_2.
}
\]

No time differentiability of a principal eigenvector is required.

## 5. Relation to covariance defects

If `C_omega` has principal eigenvalue `mu_1`, then

\[
O=E(1-\mu_1)=E\Pi.
\]

Since

\[
\frac12J\le\Pi\le\frac32J,
\]

we have

\[
\boxed{
\frac12D\le O\le\frac32D,
\qquad
D=EJ.
}
\]

Thus the Riccati formulation and the energy-weighted projective formulation are quantitatively equivalent at base order, but `O` is exactly the mixed-norm quantity entering the external anisotropic criterion.

## 6. Direct Miller connection

Choose a measurable minimizing axis `n(t)`. It is constant in space, so

\[
\nabla_xn=0.
\]

Evan Miller's locally anisotropic criterion therefore applies if

\[
\int_0^{T^*}\|n(t)\times\omega(t)\|_2^4dt
=
\int_0^{T^*}O(t)^2dt
<\infty.
\]

The Riccati inequality gives

\[
\frac{2\nu}{U_0}
\int_0^T O^2dt
\le
O(0)
+2\int_0^T\sqrt O\,\|S\omega\|_2dt.
\]

Therefore

\[
\boxed{
\int_0^{T^*}
\sqrt{O(t)}\,\|S\omega(t)\|_2dt
<\infty
\Longrightarrow
\int_0^{T^*}O(t)^2dt<\infty
\Longrightarrow
\text{regularity}.
}
\]

A hypothetical finite-time singularity must therefore satisfy

\[
\boxed{
\int_0^{T^*}
\sqrt{O(t)}\,\|S\omega(t)\|_2dt
=\infty.
}
\]

This is equivalent in strength, up to universal covariance constants, to the previously derived `sqrt(D_0)||S omega||_2` obstruction.

## 7. Near-one-axis interpretation of `S n`

The exact identity

\[
\|S n\|_2=\frac12\|n\times\omega\|_2
\]

shows that as vorticity approaches one constant axis in `L^2`, the strain applied to that same axis simultaneously vanishes in `L^2`.

For an exactly one-axis divergence-free vorticity field, the corresponding embedded flow has the familiar two-dimensional structural property: no strain component acts along the vorticity axis.

The identity quantifies the approach to that limit without changing the Navier--Stokes equation.

## 8. Remaining nonlinear gap

The right-hand side still contains the product

\[
\sqrt O\,\|S\omega\|_2.
\]

The Fourier identity controls `S n`, not the full nonlinear vector `S omega`. Therefore it does not by itself close the source.

The next useful decomposition is

\[
\omega=\alpha n+\beta,
\qquad
\beta=P_{n^\perp}\omega,
\]

for which

\[
\int(n\times\omega)\cdot(n\times S\omega)
=
\int\beta\cdot S\omega
=
\int\beta\cdot S\beta
+
\int\alpha\,\beta\cdot S n.
\]

The conversion term contains `S n` and is therefore directly depleted by the off-axis norm through the exact Fourier identity. The self-stretching term of `beta` remains tied to the strain generated by the full vorticity field.

Status: **OPEN OFF-AXIS SELF-STRETCHING CLOSURE**.
