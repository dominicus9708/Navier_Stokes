# Bounded-vorticity quantitative gap from Gaussian Poincare saturation

Date: 2026-08-14

Status: **DERIVED QUANTITATIVE STRICT GAP FOR THE VORTICITY-VARIANCE CHANNEL AT FIXED POSITIVE VARIANCE; STRAIN-DOMINATED AND VANISHING-VARIANCE PULSES REMAIN OPEN**.

The terminal first-hitting normalization gives

\[
\|\Omega\|_{L^\infty}\le1.
\]

The ordinary Gaussian Poincare inequality is saturated by first Hermite-chaos / affine functions.  A nonconstant affine function cannot be globally bounded.  This incompatibility yields an explicit positive Poincare deficit whenever the Gaussian vorticity variance is bounded below by a fixed positive number.

No novelty claim is made without a separate literature-priority audit.

---

## 1. Standard Gaussian scalar lemma

Let `gamma` be the standard Gaussian probability measure on `R^n`.  Let

\[
f\in H^1(\gamma),
\qquad
\int f\,d\gamma=0,
\qquad
|f|\le M.
\]

Write the Hermite decomposition

\[
f=f_1+h,
\]

where

- `f_1=a dot z` is the first chaos;
- `h` contains Hermite degrees at least two.

Let

\[
V=\int f^2d\gamma,
\qquad
\delta=\|h\|_{L^2(\gamma)}^2.
\]

Then

\[
V=|a|^2+\delta.
\]

The Ornstein--Uhlenbeck spectral decomposition gives

\[
\int|\nabla f|^2d\gamma
\ge
|a|^2+2\delta
=V+\delta.
\]

Thus the Poincare deficit is at least `delta`.

---

## 2. Boundedness forces a positive higher-chaos component

Assume

\[
V\ge v_0>0.
\]

There are two cases.

### Case A

If

\[
\delta\ge v_0/2,
\]

then immediately

\[
\int|\nabla f|^2d\gamma
\ge V+v_0/2.
\]

### Case B

If

\[
\delta<v_0/2,
\]

then

\[
|a|^2=V-\delta\ge v_0/2.
\]

Let `Z` be a standard one-dimensional Gaussian in the direction of `a`.  Since `|f|<=M`, pointwise

\[
|h|=|f-a\cdot z|
\ge
\bigl(|a||Z|-M\bigr)_+.
\]

Therefore

\[
\delta
\ge
\mathbb E\left[
\bigl(|a||Z|-M\bigr)_+^2
\right]
\ge
\mathbb E\left[
\bigl(\sqrt{v_0/2}|Z|-M\bigr)_+^2
\right].
\]

Define

\[
\Psi_M(c)
:=
\mathbb E[(c|Z|-M)_+^2].
\]

Then

\[
\boxed{
\int|\nabla f|^2d\gamma
\ge
V+\eta_M(v_0)
}
\]

with

\[
\boxed{
\eta_M(v_0)
:=
\min\left\{
\frac{v_0}{2},
\Psi_M\left(\sqrt{v_0/2}\right)
\right\}>0.
}
\]

An explicit form is available.  If

\[
a_0=M/c,
\]

then

\[
\boxed{
\Psi_M(c)
=2c^2
\left[
(1+a_0^2)\,\overline\Phi(a_0)
-a_0\phi(a_0)
\right],
}
\]

where `phi` is the standard Gaussian density and `Phi-bar` its upper tail.

The constant can be very small when `v0` is small, but it is strictly positive for every fixed `v0>0`.

---

## 3. Apply componentwise to bounded vorticity

Let

\[
\delta\Omega
=\Omega-\bar\Omega_\gamma,
\qquad
V_\omega
=\int|\delta\Omega|^2d\gamma.
\]

Since

\[
|\Omega|\le1,
\]

every centered scalar component satisfies

\[
|\delta\Omega_i|\le2.
\]

If

\[
V_\omega\ge b>0,
\]

then at least one of the three components has variance at least `b/3`.

Apply the scalar lemma to that component with

\[
M=2,
\qquad
v_0=b/3.
\]

For the other components use the ordinary Gaussian Poincare inequality.  Summing gives

\[
\boxed{
\int|\nabla_z\delta\Omega|_F^2d\gamma
\ge
V_\omega+\eta_\omega(b),
}
\]

where

\[
\boxed{
\eta_\omega(b)
:=
\min\left\{
\frac b6,
\Psi_2\left(\sqrt{b/6}\right)
\right\}>0.
}
\]

This is a strict additive gap above Gaussian Poincare whenever the vorticity variance is order one in the quantitative sense `V_omega>=b`.

---

## 4. Anisotropic Gaussian covariance

Let the physical/normalized observation Gaussian have covariance `Sigma>0`.  Whiten by

\[
z=\Sigma^{-1/2}(x-a).
\]

Then

\[
\nabla_z\Omega
=(\nabla_x\Omega)\Sigma^{1/2}.
\]

Hence

\[
\boxed{
\int\gamma_\Sigma
\left|
(\nabla\Omega)\Sigma^{1/2}
\right|_F^2
\ge
V_\omega+\eta_\omega(b)
}
\]

whenever `V_omega>=b`.

Since

\[
|A\Sigma^{1/2}|_F^2
\le
\lambda_{\max}(\Sigma)|A|_F^2,
\]

we obtain

\[
\boxed{
D_\omega
:=\int\gamma_\Sigma|\nabla\Omega|_F^2
\ge
\frac{V_\omega+\eta_\omega(b)}
{\lambda_{\max}(\Sigma)}.
}
\]

This strictly improves the ordinary Gaussian Poincare coercivity on the fixed-positive vorticity-variance branch.

---

## 5. Terminal affine-heat form

On a bounded-affine terminal window,

\[
\lambda_{\max}(\Sigma(\tau))
\le
C_K\nu\tau.
\]

Therefore, whenever

\[
V_\omega(\tau)\ge b,
\]

\[
\boxed{
\nu D_\omega(\tau)
\ge
\frac{c_K}{\tau}
\left[
V_\omega(\tau)+\eta_\omega(b)
\right].
}
\]

The second term is a genuine additive strict surplus over the scale-critical Poincare value.

If the order-one vorticity-variance state persists across a scale-time range

\[
\tau\in[\tau_1,\tau_2],
\]

then the extra viscous coercivity integrates to

\[
\boxed{
\int_{\tau_1}^{\tau_2}
\frac{c_K\eta_\omega(b)}{\tau}d\tau
=
c_K\eta_\omega(b)
\log\frac{\tau_2}{\tau_1}.
}
\]

For `tau ~ R^2`, this is

\[
\boxed{
2c_K\eta_\omega(b)
\log\frac{R_2}{R_1}.
}
\]

Thus a vorticity-dominated order-one residual cannot repeatedly saturate the ordinary Gaussian Poincare bound with zero margin across a long scale ladder.

---

## 6. Relation to the four-channel residual state

Recall

\[
\mathcal B_\gamma
=V_S+\frac12V_\omega.
\]

If an order-one residual pulse has a fixed vorticity share, for example

\[
V_\omega\ge\theta\mathcal B_\gamma
\ge b>0,
\]

then the strict vorticity Poincare surplus above applies.

The route must then pay for this surplus through the remaining terms of the vorticity-variance equation:

1. affine covariance stretching;
2. non-affine residual flux;
3. movement of the active variance to a different time/scale;
4. departure from the bounded-affine covariance branch.

This converts exact Poincare saturation into a quantitatively forbidden state for the bounded-vorticity vorticity channel.

---

## 7. Limitation

This lemma does **not** close the whole non-affine mesoscopic window.

### Vanishing intermediate pulse

For

\[
V_\omega=b(q)\to0,
\]

the explicit `eta_omega(b)` also tends to zero, in fact very rapidly with the elementary tail estimate used here.  Therefore the result is strongest for fixed-positive vorticity variance and weak for the surviving `q^(-alpha)` intermediate pulse regime.

### Strain-dominated residual

If

\[
V_S\gg V_\omega,
\]

the first-hitting bound gives only BMO-type control of the strain rather than a pointwise bound.  The elementary bounded-function argument above does not apply directly.

Thus the remaining saturation problem splits into

\[
\boxed{
\text{intermediate vanishing pulse}
\quad\text{or}\quad
\text{strain-dominated order-one pulse}
\quad\text{or}\quad
\text{affine/pressure escalation}.
}
\]

Status: **FIXED-POSITIVE VORTICITY-VARIANCE POINCARE SATURATION EXCLUDED / VANISHING AND STRAIN-DOMINATED PULSES REMAIN OPEN**.
