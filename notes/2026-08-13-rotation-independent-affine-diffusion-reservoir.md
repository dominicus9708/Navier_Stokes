# Rotation-independent affine stretch/diffusion bound: axis rotation cannot remove the transverse precursor reservoir

Date: 2026-08-13

Status: **DERIVED GENERAL LINEAR AFFINE LEMMA / REMOVES FAST EIGENAXIS ROTATION AS AN INDEPENDENT LINEAR ESCAPE**.

The fixed-axis biaxial benchmark suggested that fast rotation of the compressive normal might evade the one-dimensional compression-diffusion mechanism.  Rotation can indeed redistribute compression among transverse directions, so the **fixed-axis `q^2` normal-length reservoir** is not rotation-invariant.

However, a more invariant matrix argument shows that rotation cannot eliminate compression-diffusion altogether.  For any volume-preserving linear affine flow with bounded symmetric strain rate, a final stretch factor `q` forces a two-dimensional accumulated heat covariance whose area grows at least like `q`.

The resulting universal mixed-norm estimate requires a transverse precursor `L2` reservoir of order `q^(1/2)` and, under amplitude one, a transverse occupied area of order `q`.

This is a linear affine theorem, not yet a perturbative theorem for the full nonlinear Navier--Stokes equation.

---

## 1. General volume-preserving linear affine flow

Let

\[
\partial_t\omega
+(L(t)x)\cdot\nabla\omega
=L(t)\omega+\nu\Delta\omega,
\]

where

\[
\operatorname{tr}L(t)=0.
\]

The antisymmetric part of `L` is rigid rotation; only

\[
S(t)=\operatorname{sym}L(t)
\]

changes singular values.

Assume

\[
\boxed{
\|S(t)\|_{op}\le M
}
\]

on `[0,T]`.

Let

\[
\boxed{
F'=L(t)F,
\qquad F(0)=I.
}
\]

Then

\[
\det F(t)=1.
\]

Let the final largest singular value be

\[
\boxed{
q=\sigma_1(F(T))=\|F(T)\|_{op}>1.
}
\]

---

## 2. Exact affine removal

Set

\[
x=F(t)y,
\qquad
\omega(x,t)=F(t)v(y,t).
\]

Then the affine advection and vector stretching cancel exactly and

\[
\boxed{
\partial_t v
=\nu\nabla_y\cdot(A(t)\nabla_yv),
}
\]

with

\[
\boxed{
A(t)=F(t)^{-1}F(t)^{-T}.
}
\]

Because `A(t)` is spatially constant at each time, the diffusion operators commute.  The solution is an anisotropic Gaussian convolution with accumulated heat matrix

\[
\boxed{
C_T=\int_0^T A(s)ds.
}
\]

---

## 3. Backward comparison of the diffusion metric

Let

\[
\Phi(T,s)=F(T)F(s)^{-1}
\]

be the affine transition map from `s` to `T`.

The symmetric-strain bound gives the standard singular-value estimate

\[
\|\Phi(T,s)\|_{op}
\le e^{M(T-s)},
\]

and

\[
\sigma_{\min}(\Phi(T,s))
\ge e^{-M(T-s)}.
\]

For any vector `z`,

\[
F(s)^{-T}z
=\Phi(T,s)^T F(T)^{-T}z.
\]

Therefore

\[
|F(s)^{-T}z|
\ge
e^{-M(T-s)}|F(T)^{-T}z|.
\]

Equivalently in Loewner order,

\[
\boxed{
A(s)
\succeq
e^{-2M(T-s)}A(T).
}
\]

Integrating,

\[
\boxed{
C_T
\succeq
c_T A(T),
\qquad
c_T=\frac{1-e^{-2MT}}{2M}.
}
\]

---

## 4. Replace the physical duration by the final stretch

Since the largest singular value can grow at rate at most `M`,

\[
q\le e^{MT}.
\]

Hence

\[
e^{-2MT}\le q^{-2}.
\]

Therefore

\[
\boxed{
C_T
\succeq
c_q A(T),
\qquad
c_q=\frac{1-q^{-2}}{2M}.
}
\]

This bound is completely independent of how the strain eigenvectors rotate.

---

## 5. Two-dimensional heat-area lower bound

Let the singular values of `F(T)` be

\[
\sigma_1=q\ge\sigma_2\ge\sigma_3>0.
\]

Volume preservation gives

\[
\sigma_1\sigma_2\sigma_3=1.
\]

The eigenvalues of

\[
A(T)=F(T)^{-1}F(T)^{-T}
\]

in increasing order are

\[
\alpha_1=\sigma_1^{-2},
\quad
\alpha_2=\sigma_2^{-2},
\quad
\alpha_3=\sigma_3^{-2}.
\]

The product of the **two largest** is exactly

\[
\boxed{
\alpha_2\alpha_3
=(\sigma_2\sigma_3)^{-2}
=q^2.
}
\]

Let

\[
0<\mu_1\le\mu_2\le\mu_3
\]

be the eigenvalues of `C_T`.  Since

\[
C_T\succeq c_qA(T),
\]

min--max gives

\[
\mu_i\ge c_q\alpha_i.
\]

Therefore

\[
\boxed{
\mu_2\mu_3
\ge
c_q^2q^2
=\left(\frac{1-q^{-2}}{2M}\right)^2q^2.
}
\]

This is the rotation-independent transverse heat-area lower bound.

---

## 6. Two-dimensional mixed-norm heat smoothing

Diagonalize `C_T` by an orthogonal basis

\[
(e_1,e_2,e_3),
\]

with `e2,e3` corresponding to `mu2,mu3`.

The anisotropic Gaussian semigroup obeys the mixed-norm estimate

\[
\boxed{
\|e^{\nu C_T:D^2}f\|_\infty
\le
C
[\nu^2\mu_2\mu_3]^{-1/4}
\|f\|_{L^\infty_{e_1}L^2_{e_2,e_3}}.
}
\]

The remaining `e1` heat factor is only used as an `L-infinity` contraction.

Since

\[
\omega(T)=F(T)e^{\nu C_T:D^2}\omega_0,
\]

we get

\[
\begin{aligned}
\|\omega(T)\|_\infty
&\le
q\,
C[\nu^2\mu_2\mu_3]^{-1/4}
\|\omega_0\|_{L^\infty_{e_1}L^2_{e_2,e_3}}\\
&\le
C q^{1/2}
(\nu c_q)^{-1/2}
\|\omega_0\|_{L^\infty_{e_1}L^2_{e_2,e_3}}.
\end{aligned}
\]

Thus

\[
\boxed{
\|\omega(T)\|_\infty
\le
C q^{1/2}
\left[
\frac{2M}{\nu(1-q^{-2})}
\right]^{1/2}
\|\omega_0\|_{L^\infty_{e_1}L^2_{e_2,e_3}}.
}
\]

For `q>=2`, the denominator factor is uniformly order one, so schematically

\[
\boxed{
\|\omega(T)\|_\infty
\lesssim
q^{1/2}(M/\nu)^{1/2}
\|\omega_0\|_{L^\infty L^2_{\rm transverse}}.
}
\]

---

## 7. Necessary precursor reservoir for a target `q` amplification

If the final target is

\[
\|\omega(T)\|_\infty
\ge c_0q
\]

from a normalized initial state, then

\[
\boxed{
\|\omega_0\|_{L^\infty_{e_1}L^2_{e_2,e_3}}
\gtrsim
c_0 q^{1/2}
\left(
\frac{\nu(1-q^{-2})}{M}
\right)^{1/2}.
}
\]

If

\[
|\omega_0|\le1,
\]

then a transverse `L2` norm of this size requires, at some value of the remaining coordinate, an occupied transverse area of at least

\[
\boxed{
A_{\rm precursor}
\gtrsim
q\,rac\nu M
}
\]

up to constants and the target fraction `c0`.

Thus axis rotation may redistribute a one-dimensional normal reservoir into a two-dimensional transverse reservoir, but it cannot remove the precursor requirement.

---

## 8. Fixed-axis biaxial case is stronger

For the ideal fixed-axis Betchov flow

\[
F=\operatorname{diag}(q^{-2},q,q),
\]

the strongest diffusion eigenvalue is of order `q^4`, and the one-dimensional normal smoothing already cancels the full `q` stretch.

The general rotation-independent argument uses only the product of the two strongest diffusion eigenvalues and therefore yields the weaker residual factor `q^(1/2)`.

This loss is real: rapid rotation can distribute compression among two transverse material directions.

---

## 9. Explicit rapid-rotation intuition

Consider an ideal biaxial strain whose compressive normal rotates rapidly around one fixed extensional direction.  The fixed direction can continue to stretch approximately like `e^{at}`, while the two-dimensional perpendicular area contracts like `e^{-at}` and rapid rotation distributes that contraction roughly evenly.

The two transverse singular values can then behave schematically like

\[
e^{-at/2},
\qquad
e^{-at/2},
\]

rather than `(e^a t, e^{-2at})` within a fixed normal/extensional pair.

This explains why rotation weakens the one-dimensional `q^2` length requirement to a two-dimensional `q` area requirement, but does not eliminate compression-diffusion.

---

## 10. Updated escape structure

For the **linear affine model with bounded symmetric strain rate**, fast eigenaxis rotation is no longer an independent escape.

A large amplification can avoid the rotation-independent heat bound only through

1. **large affine rate** `M`, which returns to coherent local strain concentration;
2. **large precursor transverse reservoir**;
3. or, in the full Navier--Stokes equation, **non-affine nonlinear/viscous forcing** large enough that the linear affine approximation is not perturbative.

Thus the previous four-way fixed-axis list

\[
\text{rate / rotation / residual / reservoir}
\]

is sharpened, at the linear level, to

\[
\boxed{
\text{rate / residual / reservoir}.
}
\]

---

## 11. DSD interpretation

The compressive axis does not need to be tracked point-by-point to preserve the relevant diffusion information.  The matrix aggregate

\[
\boxed{
C_T=\int_0^T F^{-1}F^{-T}dt
}
\]

already sums the rotating directional history.

Its two-dimensional spectral area

\[
\boxed{\mu_2\mu_3}
\]

is the rotation-invariant descriptor that survives coarse-graining.

This is more economical than tracking the full eigendirection path when the immediate question is whether rotation can erase compression-enhanced smoothing.

---

## 12. Remaining nonlinear target

The full Navier--Stokes proof route now needs a perturbative comparison between a first-hitting dangerous window and its optimal local affine model.

A sufficient result would show that, on a window where the residual BMO/source channels remain quantitatively subordinate,

\[
\boxed{
\text{large full amplification}
\Longrightarrow
\text{large precursor transverse reservoir}
}
\]

with the affine rate already charged to local strain concentration.

If the perturbative comparison fails, that failure itself must be charged to the residual nonlinear/Cauchy-V channel.

Status: **AXIS ROTATION ELIMINATED AS AN INDEPENDENT LINEAR ESCAPE / NONLINEAR PERTURBATIVE TRANSFER REMAINS OPEN**.
