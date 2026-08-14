# Quadratic-core projective dissipation barrier

Date: 2026-08-14

Status: **DERIVED FOR THE QUADRATIC-CORE CONSTANT-SHIFT / PROJECTIVE `Ab` LANE. THIS DOES NOT YET COVER THE FULL TRANSVERSE STRAIN PROJECTIVE SOURCE. GLOBAL REGULARITY NOT PROVED.**

## 1. Setup

On a responsible bounded-affine first-hitting interval let

\[
B(t)=\mathcal B_\gamma(t),
\qquad
V_\omega(t)=\Theta(t)B(t),
\]

and denote

\[
m=\sup_I B,
\qquad
\theta=\sup_I\Theta.
\]

On a surviving sequence write

\[
m=W^{-1/3}\Lambda,
\qquad
\Lambda\to\infty,
\qquad
m\ll1.
\]

For the quadratic Hermite core, the constant-shift/projective contribution to the mean-vorticity source is

\[
J_{Ab}=Ab.
\]

The previously derived projective estimate is

\[
|Ab|\lesssim \sqrt{V_\omega V_\perp}.
\]

Because

\[
V_\perp\le V_\omega,
\]

we obtain the sharper lane-specific estimate

\[
\boxed{
|J_{Ab}|
\lesssim V_\omega
=\Theta B.
}
\]

This is stronger than the generic typed source estimate

\[
|J|\lesssim B\sqrt\Theta
\]

when `Theta` is small.

## 2. Fixed endpoint action forces a larger B-mass

Assume that the `Ab` lane carries a fixed positive fraction of the endpoint residual source action. Thus for some fixed `rho>0`, independent of the first-hitting level,

\[
\rho
\lesssim
\int_I |J_{Ab}(t)|\,dt.
\]

Using the lane-specific estimate,

\[
\rho
\lesssim
\int_I\Theta(t)B(t)\,dt
\le
\theta\int_I B(t)\,dt.
\]

Therefore

\[
\boxed{
\int_I B(t)\,dt
\gtrsim
\frac{\rho}{\theta}.
}
\]

Hence a small vorticity/projective share cannot produce fixed endpoint action cheaply: the required residual-gradient mass grows like `theta^{-1}`.

## 3. Rearrangement and physical dissipation

The Gaussian-volume lower bound on the bounded-affine branch is

\[
\|\nabla U(\tau)\|_2^2
\gtrsim
\tau^{3/2}B(\tau).
\]

The bathtub/rearrangement lemma says that if

\[
0\le B\le m,
\qquad
\int B\ge A,
\]

then

\[
\int\tau^{3/2}B(\tau)\,d\tau
\gtrsim
A^{5/2}m^{-3/2}.
\]

Here

\[
A\gtrsim\rho/\theta.
\]

Consequently

\[
\int_I\|\nabla U\|_2^2dt
\gtrsim
\rho^{5/2}\theta^{-5/2}m^{-3/2}.
\]

Returning to physical variables gives

\[
\boxed{
D_{\rm phys}^{Ab}(I)
\gtrsim
W^{-1/2}m^{-3/2}\theta^{-5/2}.
}
\]

Substituting

\[
m=W^{-1/3}\Lambda
\]

cancels the `W` factor:

\[
\boxed{
D_{\rm phys}^{Ab}(I)
\gtrsim
\Lambda^{-3/2}\theta^{-5/2}
=
(\Lambda^{3/5}\theta)^{-5/2}.
}
\]

## 4. Survival condition on an infinite disjoint cascade

Consecutive first-hitting physical intervals are disjoint and the global kinetic-energy identity permits only finite total dissipation.

Therefore, if infinitely many such intervals have the `Ab` lane carrying a fixed positive fraction of the required endpoint source action, their individual lower bounds must tend to zero. A necessary condition is

\[
\boxed{
\Lambda^{3/5}\theta\to\infty.
}
\]

Equivalently, up to constants/subpower losses,

\[
\boxed{
\theta\gg\Lambda^{-3/5}.
}
\]

This is substantially stronger than the universal typed survival condition

\[
H=\Lambda\Theta^{5/6}\to\infty,
\]

which by itself only forces roughly `Theta >> Lambda^{-6/5}`.

## 5. Equivalent matched-block radius interpretation

If a single matched parabolic block of duration comparable to `R^2` carries fixed `Ab` source action, then

\[
1\lesssim m\theta R^2.
\]

Hence

\[
R
\gtrsim
(m\theta)^{-1/2}
=
W^{1/6}\Lambda^{-1/2}\theta^{-1/2}.
\]

On the low-curvature Hermite ridge we already have

\[
R\lesssim W^{1/6}\Lambda^{-1/5}.
\]

Compatibility therefore requires

\[
\boxed{
\theta\gtrsim\Lambda^{-3/5}.
}
\]

The finite-total-dissipation argument strengthens this non-strict scale compatibility to

\[
\Lambda^{3/5}\theta\to\infty
\]

on a surviving infinite sequence.

## 6. Interaction with the Hermite-curvature dichotomy

Recall

\[
\delta=\frac{K-B}{B}.
\]

On a responsible subset where `Theta` is dyadically localized, so that

\[
\Theta\asymp\theta,
\]

the existing dichotomy becomes sharper on the surviving `Ab` branch.

If

\[
\delta\ll\Theta,
\]

then the pressure-free near-Poincare vorticity argument gives

\[
\boxed{mR^4\gtrsim1.}
\]

If instead

\[
\delta\gtrsim\Theta,
\]

then the present projective survival condition gives

\[
\boxed{
\delta\Lambda^{3/5}\to\infty.
}
\]

This latter conclusion is stronger than the previously available universal rescaling

\[
\delta\Lambda^{6/5}\to\infty
\]

but only on the dyadically localized quadratic-core `Ab`-responsible branch.

## 7. Scope boundary

This note does **not** prove the same `Theta B` bound for the general transverse stretching source

\[
J_\perp
=
\int\gamma\,\delta S\,\beta.
\]

For that full source one only has

\[
|J_\perp|
\le
\sqrt{BV_\perp}.
\]

Therefore the exponent improvement proved here belongs specifically to the quadratic-core constant-shift/projective `Ab` route.

The remaining work is to obtain an analogous spacetime packing/cost for the general projective stretching route, or to force it into Cauchy material-axis change / viscous rewrite.

Status: **QUADRATIC-CORE `Ab` PROJECTIVE LANE REQUIRES `Lambda^(3/5) Theta -> infinity` ON A SURVIVING INFINITE CASCADE / FULL PROJECTIVE PACKING REMAINS OPEN / GLOBAL REGULARITY NOT PROVED.**
