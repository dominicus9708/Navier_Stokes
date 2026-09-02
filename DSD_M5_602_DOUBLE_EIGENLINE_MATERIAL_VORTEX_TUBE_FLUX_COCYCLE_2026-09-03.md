# DSD M5-602 — Double-eigenline material vortex-tube flux cocycle

Date: 2026-09-03

Status: **CONDITIONAL ON M5-599. THE GLOBAL DOUBLE-EIGENLINE CLASS HAS A SCALE-INVARIANT SIGNED COCYCLE. VORTEX LINES ARE MATERIAL LINES; A MATERIAL AREA ELEMENT NORMAL TO THE VORTICITY EVOLVES AT RATE `1-sigma`, WHILE THE VORTICITY MAGNITUDE EVOLVES AT RATE `sigma+kappa-1`. THEIR PRODUCT, THE INFINITESIMAL MATERIAL VORTEX-TUBE FLUX, THEREFORE SATISFIES `D_B log Phi_tube = kappa`. FOR FINITE MATERIAL CROSS-SECTIONS, `Phi' = integral kappa W·n`. THIS IS THE FIRST CE-H OBSERVABLE IN THE CURRENT FRONTIER THAT IS BOTH SCALE INVARIANT AND SIGNED. GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Inputs

On the M5-599/M5-600 branch,

\[
\Sigma W=\sigma W,
\qquad
\Delta W=\kappa W,
\]

and

\[
D_B\xi=0,
\qquad
D_B\log\rho=\sigma+\kappa-1,
\]

where

\[
W=\rho\xi,
\qquad
B=U+\frac12y.
\]

Also

\[
\nabla\cdot B=\frac32.
\]

## 2. Vortex-line tangent vectors are material

Let \(\ell\) be an infinitesimal material line element transported by \(B\).

Then

\[
D_B\ell=(\nabla B)\ell.
\]

Suppose at one time

\[
\ell=a\xi.
\]

Since

\[
\nabla B=\nabla U+\frac12I,
\]

and the antisymmetric part of \(\nabla U\) annihilates \(\xi\),

\[
(\nabla U)\xi=\Sigma\xi=\sigma\xi.
\]

Hence

\[
(\nabla B)\xi
=(\sigma+\tfrac12)\xi.
\]

Because

\[
D_B\xi=0,
\]

the transported line element remains parallel to \(\xi\):

\[
\boxed{
D_B\log a=\sigma+\frac12.
}
\]

Thus instantaneous vortex lines are transported into vortex lines; the vortex-line foliation is material on the double-eigenline branch.

## 3. Material area vector normal to a vortex line

Let

\[
q=n\,dA
\]

be an oriented material area vector.

For a flow with velocity \(B\),

\[
D_Bq
=
\bigl[(\nabla\cdot B)I-(\nabla B)^T\bigr]q.
\]

Take an infinitesimal vortex-tube cross-section with

\[
q=a_\perp\xi.
\]

Because the antisymmetric part again annihilates \(\xi\),

\[
(\nabla B)^T\xi
=(\sigma+\tfrac12)\xi.
\]

Therefore

\[
D_Bq
=
\left(
\frac32-\sigma-\frac12
\right)q
=(1-\sigma)q.
\]

Since \(D_B\xi=0\),

\[
\boxed{
D_B\log a_\perp=1-\sigma.
}
\]

## 4. Exact infinitesimal vortex-tube flux law

The infinitesimal directed vorticity flux is

\[
\phi
:=W\cdot q
=\rho a_\perp.
\]

Using

\[
D_B\log\rho
=\sigma+\kappa-1
\]

and

\[
D_B\log a_\perp
=1-\sigma,
\]

we obtain the exact cancellation of the strain and similarity-dilation terms:

\[
\boxed{
D_B\log|\phi|
=\kappa.
}
\]

Equivalently,

\[
\boxed{
D_B\phi=\kappa\phi.
}
\]

This is the local material vortex-tube flux cocycle.

## 5. Finite material cross-section

For a finite material surface \(\Sigma(\theta)\), M5-489 gave

\[
\frac d{d\theta}
\int_{\Sigma(\theta)}W\cdot n\,dA
=
\int_{\Sigma(\theta)}\Delta W\cdot n\,dA.
\]

On the double-eigenline branch,

\[
\Delta W=\kappa W,
\]

so

\[
\boxed{
\Phi'(\theta)
=
\int_{\Sigma(\theta)}
\kappa W\cdot n\,dA.
}
\]

For an infinitesimal material vortex tube this reduces exactly to

\[
\phi'=\kappa\phi.
\]

For a finite tube, \(\kappa\) may vary between vortex lines, so one must retain the flux-weighted average rather than silently replacing it by one scalar value.

## 6. Vortex-line first integral and tube law

M5-600 gives

\[
W\cdot\nabla\kappa=0.
\]

Thus at each fixed time, \(\kappa\) is constant along each vortex line.

Accordingly, an infinitesimal tube based on one vortex line has a well-defined instantaneous scalar multiplier \(\kappa\), and the material flux law is geometrically consistent along the line.

## 7. Scaling audit

Vorticity flux through a surface is Navier--Stokes scale invariant.

Therefore

\[
\log|\phi|
\]

is a bounded/recurrence-compatible **critical observable** on a persistent fixed-flux lineage, unlike physical kinetic-energy costs whose generation weights were summable in M5-598.

The derivative

\[
\boxed{\kappa}
\]

is consequently a genuine candidate signed drift.

## 8. Recurrent persistent tube consequence

Suppose the same infinitesimal material vortex tube is tracked through return times \(\theta_j\) and its flux remains uniformly nondegenerate and bounded:

\[
0<\phi_-\le|\phi(\theta_j)|\le\phi_+<\infty.
\]

Then

\[
\int_{\theta_1}^{\theta_N}\kappa(Y(\theta),\theta)d\theta
=
\log\frac{|\phi(\theta_N)|}{|\phi(\theta_1)|}.
\]

The right side is uniformly bounded.

Therefore

\[
\boxed{
\langle\kappa\rangle_{tube-return}=0.
}
\]

This is an exact scale-invariant signed recurrence condition.

## 9. Combine with area recurrence

If the same tube cross-section returns to a fixed coherent similarity size so that

\[
0<a_-\le a_\perp(\theta_j)\le a_+<\infty,
\]

then

\[
\int(1-\sigma)d\theta
=
\log\frac{a_\perp(\theta_N)}{a_\perp(\theta_1)},
\]

and hence

\[
\boxed{
\langle\sigma\rangle_{tube-return}=1.
}
\]

Thus a genuinely recurrent coherent CE-H vortex tube must satisfy simultaneously

\[
\boxed{
\langle\kappa\rangle=0,
\qquad
\langle\sigma\rangle=1.
}
\]

The magnitude return equation then follows automatically from

\[
D_B\log\rho=\sigma+\kappa-1.
\]

## 10. Current gap

M5-600 gives the global enstrophy-weighted identity

\[
\int\kappa|W|^2=-P<0
\]

for every nontrivial time slice.

M5-602 gives zero **tube-return average** of \(\kappa\) on a recurrent fixed-flux material tube.

These are different measures and are not yet contradictory.

A diffuse/background vorticity population can in principle carry the negative global viscous average while the persistent active tube has zero signed drift.

Thus the next step is a measure-attribution problem:

\[
\boxed{
\text{can all of the negative }|W|^2\text{-weighted }\kappa
\text{ be carried outside the finite persistent recurrent tubes?}
}
\]

## 11. DSD audit

This note does **not** assume that a finite coherent carrier has spatially constant \(\kappa\).

The scalar law \(D_B\log\phi=\kappa\) is exact only for an infinitesimal tube/area element based on one vortex line.

For a finite cross-section the exact law is the flux-weighted integral.

Status: **CE-H NOW POSSESSES A SCALE-INVARIANT SIGNED FLUX COCYCLE. RECURRENT FIXED-FLUX TUBES FORCE ZERO MEAN VISCOUS MULTIPLIER, WHILE THE GLOBAL ENSTROPHY MEASURE FORCES A STRICTLY NEGATIVE MEAN. THE REMAINING QUESTION IS WHETHER THESE TWO MEASURES CAN REMAIN DISJOINT. GLOBAL REGULARITY REMAINS UNPROVED.**