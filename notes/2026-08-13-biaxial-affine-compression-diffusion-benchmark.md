# Biaxial extensional-plane affine benchmark: compression-enhanced diffusion requires a long precursor reservoir

Date: 2026-08-13

Status: **DERIVED LINEAR AFFINE MODEL LEMMA / NOT A FULL NAVIER--STOKES CLOSURE**.

The exact affine-covariance optimization identified the hard local affine geometry

\[
S=a\,\operatorname{diag}(-2,1,1),
\qquad a>0,
\]

with vorticity concentrated in the two-dimensional extensional plane.

This note solves the corresponding **constant-strain linear advection--stretch--diffusion model** and shows that the same compression which stretches plane vorticity also accelerates diffusion in the compressive normal direction.

Large amplification can survive only if the precursor vorticity already has a large normal-direction `L2` reservoir.

This is a model theorem, not a theorem for the full nonlinear Navier--Stokes equation with a variable local strain field.

---

## 1. Linear biaxial affine model

Let

\[
U_A(x)=(-2ax_1,ax_2,ax_3).
\]

Consider one vorticity component `w` lying in the extensional plane.  The linearized affine equation is

\[
\boxed{
\partial_t w
+U_A\cdot\nabla w
=a w+\nu\Delta w.
}
\]

The inviscid factor `a w` alone would amplify `w` by

\[
q=e^{at}.
\]

But the same affine map compresses the `x1` coordinate by `e^{-2at}`.

---

## 2. Exact affine coordinate transform

Set

\[
y_1=e^{2at}x_1,
\qquad
y_2=e^{-at}x_2,
\qquad
y_3=e^{-at}x_3,
\]

and

\[
\boxed{w(x,t)=e^{at}v(y,t).}
\]

A direct differentiation gives

\[
\boxed{
\partial_t v
=\nu\left(
 e^{4at}\partial_{y_1}^2v
+e^{-2at}(\partial_{y_2}^2+\partial_{y_3}^2)v
\right).
}
\]

The three diffusion operators commute because their coefficients depend only on time.

Define accumulated heat times

\[
\boxed{
\tau_1(t)
=\int_0^t e^{4as}ds
=\frac{e^{4at}-1}{4a},
}
\]

\[
\boxed{
\tau_\perp(t)
=\int_0^t e^{-2as}ds
=\frac{1-e^{-2at}}{2a}.
}
\]

Hence `v` is exactly an anisotropic heat evolution with normal heat time `tau1` and transverse heat time `tau_perp`.

---

## 3. One-dimensional normal smoothing is enough

The transverse heat semigroup is an `L-infinity` contraction.  The one-dimensional normal heat semigroup satisfies

\[
\boxed{
\|e^{\nu\tau\partial_1^2}f\|_{L^\infty_{x_1}}
\le
C(\nu\tau)^{-1/4}
\|f\|_{L^2_{x_1}}.
}
\]

Applying this pointwise in the transverse variables and using transverse `L-infinity` contraction gives

\[
\boxed{
\|v(t)\|_\infty
\le
C(\nu\tau_1(t))^{-1/4}
\|w_0\|_{L^\infty_{x_\perp}L^2_{x_1}}.
}
\]

Returning to `w`,

\[
\boxed{
\|w(t)\|_\infty
\le
C e^{at}
(\nu\tau_1(t))^{-1/4}
\|w_0\|_{L^\infty_{x_\perp}L^2_{x_1}}.
}
\]

---

## 4. Large affine stretch cancels against normal heat smoothing

Let

\[
q=e^{at}\ge1.
\]

Then

\[
\tau_1(t)=\frac{q^4-1}{4a}.
\]

Therefore

\[
\boxed{
\|w(t)\|_\infty
\le
C q
\left[
\frac{\nu(q^4-1)}{4a}
\right]^{-1/4}
\|w_0\|_{L^\infty_{x_\perp}L^2_{x_1}}.
}
\]

For large `q`,

\[
q(q^4-1)^{-1/4}\to1.
\]

Hence

\[
\boxed{
\|w(t)\|_\infty
\lesssim
\left(\frac a\nu\right)^{1/4}
\|w_0\|_{L^\infty_{x_\perp}L^2_{x_1}}
}
\]

uniformly in the nominal affine stretch factor `q` once `q` is large.

Thus arbitrary inviscid stretch does **not** translate into arbitrary maximum-vorticity amplification in this constant biaxial model unless the precursor normal reservoir also grows.

---

## 5. Necessary precursor reservoir for a target amplification

Suppose the initial normalized maximum is at most one and one asks for

\[
\|w(t)\|_\infty\ge c_0 q
\]

for a target factor `q>>1`.

The preceding bound forces

\[
\boxed{
\|w_0\|_{L^\infty_{x_\perp}L^2_{x_1}}
\gtrsim
q\left(\frac\nu a\right)^{1/4}.
}
\]

If `|w_0|<=1`, a linewise `L2` norm of size `M` requires a normal-direction occupied length of order at least `M^2` in the crude amplitude-one model.

Hence schematically

\[
\boxed{
L_{\rm normal}
\gtrsim
q^2\left(\frac\nu a\right)^{1/2}.
}
\]

This is the precursor-reservoir interpretation.

---

## 6. Exact Gaussian benchmark

For a one-dimensional Gaussian normal profile

\[
w_0(x_1)=\exp\left(-\frac{x_1^2}{2\sigma_0^2}\right)
\]

with no transverse dependence, the center value is explicit:

\[
\boxed{
\frac{w(0,t)}{w(0,0)}
=
\frac{q}
{\sqrt{1+\beta(q^4-1)}},
}
\]

where

\[
\boxed{
\beta=\frac\nu{2a\sigma_0^2}.
}
\]

The maximum over `q>=1` occurs, when `beta<1/2`, at

\[
\boxed{
q_*^4=\frac{1-\beta}{\beta}.
}
\]

The maximum gain is

\[
\boxed{
G_{\max}
=[4\beta(1-\beta)]^{-1/4}.
}
\]

If `beta>=1/2`, the center amplitude never increases above its initial value.

For large desired gain `G`, the small-`beta` asymptotic requires

\[
\boxed{
\sigma_0^2
\gtrsim
\frac{2\nu}{a}G^4.
}
\]

Equivalently the normal width itself must grow like `G^2`.

---

## 7. Connection to the biaxial covariance hard branch

For the Betchov-optimal strain shape, affine source is maximal when the vorticity covariance lies in the extensional plane.

But this is precisely the configuration in which the spatial normal is compressed at twice the extensional rate.  Any normal variation is therefore rapidly pushed to shorter physical scales and exposed to enhanced viscous smoothing.

Thus the hard branch has a second requirement:

\[
\boxed{
\text{extensional-plane vorticity}
+
\text{large normal precursor reservoir / weak normal variation}.
}
\]

This links the affine-covariance near-extremizer to the earlier long-tube/sheet and occupancy channels.

---

## 8. Why this is not yet a full proof

The full Navier--Stokes strain is not a prescribed constant matrix.

Residual nonlinear strain, rotation of the eigenframe, pressure, spatial variation of the affine representative, and viscous Cauchy rewriting can all modify the benchmark.

Therefore one may **not** infer from this note that the biaxial branch is excluded in the nonlinear equation.

The proof-producing target is to show that a sufficiently near-biaxial first-hitting window inherits a stable version of the normal heat-time lower bound, with the errors charged to already typed residual/BMO/deformation channels.

---

## 9. Next target

Seek a perturbative lemma of the form

\[
\boxed{
\text{biaxial affine dominance}
+\text{bounded residual BMO/affine errors}
\Longrightarrow
\text{normal compression-diffusion estimate}
}
\]

which would force either

1. failure of a large amplification step;
2. a long normal precursor reservoir;
3. or a quantitatively large residual/non-affine channel.

Status: **LINEAR BIAXIAL COMPRESSION-DIFFUSION MECHANISM CLOSED / NONLINEAR PERTURBATIVE TRANSFER OPEN**.
