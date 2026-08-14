# Critical Reynolds one-power obstruction: the missing 1/R gain is genuinely dynamic

Date: 2026-08-14

Status: **STATIC IMPROVEMENT RULED OUT BY AN EXPLICIT DIVERGENCE-FREE SECOND-HERMITE MODEL / DYNAMIC GAIN STILL OPEN**.

## 1. The missing gain is exactly a local Reynolds-number bound

For a Gaussian residual velocity `r` at radius `R`, the current local estimate is

\[
\|r\|_{L^3(B_{CR})}\lesssim R^2\sqrt B,
\]

where

\[
B=\mathcal B_{\gamma,R}
\]

is the Gaussian residual-gradient variance.

Define

\[
\boxed{\mathcal R_G:=R^2\sqrt B.}
\]

Then

\[
BR^4=\mathcal R_G^2.
\]

Thus the previously identified missing gain

\[
BR^5\lesssim W^{1/2}
\quad\Longrightarrow\quad
BR^4\lesssim C
\]

is exactly the problem of proving a uniform bound on the Gaussian local Reynolds number `mathcal R_G`.

The nonlinear turnover time associated with residual gradient size `sqrt(B)` is

\[
t_{\rm nl}\sim B^{-1/2},
\]

while the parabolic time at radius `R` is

\[
t_{\rm diff}\sim R^2.
\]

Hence

\[
\boxed{
\frac{t_{\rm diff}}{t_{\rm nl}}
\sim R^2\sqrt B
=\mathcal R_G.
}
\]

So the missing one spatial power is not an algebraic bookkeeping artifact: it measures how many nonlinear turnover times can fit inside one diffusion time.

## 2. Explicit centered second-Hermite model

Let the centered isotropic Gaussian have covariance `R^2 I`. Consider

\[
\boxed{
r_R(x)
=\frac aR
\left(
 x_1x_2,
 -\frac12(x_2^2-R^2),
 0
\right).
}
\]

This field is divergence free:

\[
\nabla\cdot r_R=0.
\]

Its vorticity is

\[
\boxed{
\nabla\times r_R
=(0,0,-a x_1/R).
}
\]

The Gaussian mean of `r_R` vanishes and the Gaussian mean of its gradient vanishes. It is therefore a pure second-Hermite residual velocity state in the centered affine-free frame.

The gradient is

\[
\nabla r_R
=\frac aR
\begin{pmatrix}
 x_2 & x_1 & 0\\
 0 & -x_2 & 0\\
 0&0&0
\end{pmatrix}.
\]

Taking the Gaussian expectation gives

\[
\boxed{B=3a^2.}
\]

The Hessian is constant and satisfies

\[
\boxed{D_g=3a^2/R^2.}
\]

Therefore

\[
\boxed{R^2D_g=B.}
\]

This exactly saturates the ordinary Gaussian Poincare curvature level: the curvature surplus is zero.

The Gaussian residual-velocity energy is

\[
\int\gamma_R|r_R|^2dx
=\frac32a^2R^2
=\frac12R^2B.
\]

Consequently an unweighted core of volume `R^3` carries kinetic-energy scaling

\[
\boxed{E_{\rm core}\sim BR^5.}
\]

There is no extra `1/R` factor.

## 3. Finite-energy localization

The polynomial model itself is not globally finite-energy in Lebesgue measure. However multiply it by a smooth cutoff which equals one on a fixed multiple of `B_R` and vanishes outside a larger fixed multiple, followed if necessary by the standard divergence-free correction in the cutoff annulus.

For fixed cutoff ratio, the core Gaussian identities are changed only by fixed/exponentially small tail errors, while the global kinetic energy still scales like

\[
E\sim BR^5.
\]

The vorticity in the core is `O(a)` at radius `R`, so choosing `a` bounded is compatible with the normalized first-hitting vorticity scale in the observation region.

Thus no universal static estimate of the form

\[
BR^4\lesssim F(E,\|\omega\|_\infty,\text{bounded Gaussian condition number})
\]

can be obtained merely by repeating the existing finite-energy / divergence-free / first-hitting constraints with the same scaling.

## 4. Consequence for the proof route

The missing `1/R` must come from genuinely dynamical information, for example

- nonlinear creation/transfer over time;
- scale-time heat contraction;
- higher-chaos production forced by self-interaction;
- shell/spectral flux;
- a rigidity theorem;
- or a regularity gate using geometry/derivative chains.

Static Gaussian energy improvement is not a viable branch.

Status: **STATIC ONE-POWER GAIN ELIMINATED AS A TARGET; ACTIVE TARGET = DYNAMIC CONTROL OF `mathcal R_G=R^2 sqrt(B)`**.
