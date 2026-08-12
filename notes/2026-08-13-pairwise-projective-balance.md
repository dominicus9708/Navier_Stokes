# Pairwise projective balance for vorticity

Date: 2026-08-13

Status: **DERIVED EXACT PAIRWISE BALANCE / OPEN DYADIC SINGULAR-KERNEL CLOSURE**.

This note evolves the unnormalized pairwise projective content

\[
\boxed{
K(t)=E(t)^2J(t)
=
\iint_{\mathbb R^3\times\mathbb R^3}
|\omega(x,t)\times\omega(y,t)|^2\,dx\,dy.
}
\]

Unlike the scalar upper bound through `||S omega||_2`, this formulation keeps an explicit cross-axis factor at the nonlinear source level.

## 1. Notation

Let

\[
a=\omega(x,t),
\qquad
b=\omega(y,t),
\]

and

\[
c=S(x,t)a,
\qquad
d=S(y,t)b.
\]

The vorticity equation is

\[
\partial_t\omega+(u\cdot\nabla)\omega
=S\omega+\nu\Delta\omega.
\]

## 2. Transport cancellation

For the pair function

\[
R(x,y)=|a\times b|^2,
\]

the two transport operators are

\[
u(x)\cdot\nabla_xR
\qquad\text{and}\qquad
u(y)\cdot\nabla_yR.
\]

After integration in `(x,y)`, both vanish for smooth decaying divergence-free flow.

Thus the pair balance contains only stretching and viscosity.

## 3. Exact stretching source

Differentiate the cross product under the stretching dynamics:

\[
\partial_t(a\times b)
=c\times b+a\times d.
\]

Hence

\[
\boxed{
\mathcal N_K
=2\iint
(a\times b)\cdot
\left[
(c\times b)+(a\times d)
\right]dxdy.
}
\]

Using

\[
(a\times b)\cdot(c\times b)
=(a\cdot c)|b|^2-(a\cdot b)(c\cdot b),
\]

and symmetry under interchange of `x` and `y`, one recovers the covariance formula

\[
\boxed{
\mathcal N_K
=4\left[
EQ-\operatorname{tr}(NA)
\right],
}
\]

where

\[
E=\int|\omega|^2,
\quad
N=\int\omega\otimes\omega,
\quad
Q=\int\omega\cdot S\omega,
\quad
A=\int(S\omega)\otimes\omega.
\]

Thus the pairwise and covariance descriptions are exactly the same nonlinear channel at different resolutions.

## 4. Exact viscous pair dissipation

For one spatial derivative direction `m`, integration by parts in `x` gives

\[
\int
(a\times b)\cdot((\partial_m^2a)\times b)dx
=-\int
|\partial_ma\times b|^2dx.
\]

The same holds in `y`. Therefore

\[
\boxed{
\mathcal V_K
=-2\nu\iint
\sum_{m=1}^3
\left[
|\partial_ma\times b|^2
+|a\times\partial_mb|^2
\right]dxdy.
}
\]

By symmetry,

\[
\boxed{
\mathcal V_K
=-4\nu\iint
\sum_m
|\partial_m\omega(x)\times\omega(y)|^2dxdy.
}
\]

Hence viscosity is manifestly sign-definite in the pairwise projective formulation.

## 5. Exact pairwise balance

Combining the preceding steps,

\[
\boxed{
\begin{aligned}
\dot K
&+2\nu\iint\sum_m
\left[
|\partial_m\omega(x)\times\omega(y)|^2
+|\omega(x)\times\partial_m\omega(y)|^2
\right]dxdy\\
&=2\iint
(\omega(x)\times\omega(y))\cdot
\Bigl[
(S(x)\omega(x))\times\omega(y)\\
&\hspace{6.5em}
+\omega(x)\times(S(y)\omega(y))
\Bigr]dxdy.
\end{aligned}
}
\]

This is an exact whole-space identity for smooth decaying solutions.

## 6. A global projective source bound

Let

\[
\mathcal R
=\iint\sum_m
|\partial_m\omega(x)\times\omega(y)|^2dxdy.
\]

Cauchy--Schwarz gives for the first nonlinear pair term

\[
\left|
\iint
(a\times b)\cdot(c\times b)
\right|
\le
K^{1/2}
\left(
\iint|c|^2|b|^2
\right)^{1/2}.
\]

Since

\[
\iint|c|^2|b|^2
=E\|S\omega\|_2^2,
\]

and the second term is identical by symmetry,

\[
\boxed{
|\mathcal N_K|
\le
4\sqrt{KE}\,\|S\omega\|_2.
}
\]

Because

\[
K=E^2J,
\]

the factor is

\[
\sqrt{KE}=E^{3/2}\sqrt J.
\]

Thus the pairwise equation retains the same global projective depletion factor `sqrt(J)` but displays its origin explicitly as `omega(x) x omega(y)`.

## 7. Pairwise viscous coercivity

The pairwise dissipation has the covariance form

\[
\mathcal R
=EP-\operatorname{tr}(NH),
\]

where

\[
P=\int|\nabla\omega|^2,
\qquad
H=\sum_m\int(\partial_m\omega)\otimes(\partial_m\omega).
\]

Writing

\[
C=N/E,
\qquad
C_1=H/P,
\]

we get

\[
\mathcal R
=EP\left[1-\operatorname{tr}(CC_1)\right].
\]

Since `C_1` is positive semidefinite with trace one,

\[
\operatorname{tr}(CC_1)
\le\mu_1(C)=1-\Pi,
\]

so

\[
\mathcal R\ge EP\Pi.
\]

Using

\[
\Pi\ge\frac12J,
\]

we obtain

\[
\boxed{
\mathcal R
\ge
\frac12EPJ
=
\frac12P D_0,
}
\]

where

\[
D_0=EJ.
\]

Therefore

\[
\boxed{
\dot K+2\nu P D_0
\le
4E\sqrt{D_0}\,\|S\omega\|_2.
}
\]

This is weaker in some respects than the sharper covariance-coercive `D_0` inequality, but it keeps the exact pairwise geometry needed for spatial localization.

## 8. Why this formulation is useful

The nonlinear source contains an explicit factor

\[
\omega(x)\times\omega(y).
\]

Thus it vanishes identically when all vorticity vectors lie on one unoriented global axis, regardless of sign changes.

More importantly, the same cross-axis quantity appears in the local smoothed spectrum

\[
\mathcal P_r
=
\iint K_r(x-y)
|\omega(x)\times\omega(y)|^2dxdy.
\]

This makes the pairwise balance the natural parent identity for a dyadic physical-scale decomposition.

## 9. Remaining singular-kernel step

The stretching vector `S(x)omega(x)` is itself a singular integral of vorticity. Substituting the Biot--Savart/strain representation turns the nonlinear pair source into a trilinear singular integral.

Classical vorticity-direction criteria exploit geometric cancellation in precisely this stretching structure. The current task is not to reproduce those criteria under a new name, but to determine whether the local covariance/projective spectrum supplies a quantitatively useful **averaged** angular depletion condition on each dyadic shell.

A single global `J` or a single smooth scale `P_r` is insufficient because the strain kernel is borderline at small separation.

The next target is a dyadic shell bound in which each shell retains its own projective mismatch channel and can be compared against Dini/logarithmic/BMO-type summability conditions from the established literature.

Status: **OPEN DYADIC PAIRWISE STRETCHING CLOSURE**.
