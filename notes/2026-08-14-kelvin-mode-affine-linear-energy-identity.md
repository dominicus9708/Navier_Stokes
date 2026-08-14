# Exact Kelvin-mode energy identity for the full affine linearized residual

Date: 2026-08-14

Status: **EXACT GLOBAL FOURIER ENERGY IDENTITY FOR THE FULL LINEARIZATION ABOUT A TIME-DEPENDENT INCOMPRESSIBLE AFFINE FLOW. MEAN ROTATION / BACKGROUND-VORTICITY SKEW COUPLING CANNOT AMPLIFY MODE ENERGY. LOCAL GAUSSIAN REDISTRIBUTION REMAINS TO BE CONTROLLED. GLOBAL REGULARITY NOT PROVED.**

## 1. Linearized residual velocity equation

After removing the Gaussian center translation, consider the linear part of the residual velocity equation about the affine field

\[
U_{\rm aff}(x,t)=L(t)x,
\qquad
\operatorname{tr}L=0.
\]

Ignoring genuinely nonlinear residual forcing, the divergence-free perturbation `r` satisfies

\[
\partial_t r
+(Lx\cdot\nabla)r
+Lr
+\nabla p
=
\nu\Delta r,
\qquad
\nabla\cdot r=0.
\]

This is the full linearized affine equation; the background-vorticity coupling that appears separately in the vorticity formulation is already contained in this velocity-pressure system.

## 2. Kelvin wavevector characteristic

Fourier transformation gives

\[
\partial_t\widehat r
-(L^Tk)\cdot\nabla_k\widehat r
+L\widehat r
+i k\widehat p
=
-\nu|k|^2\widehat r.
\]

Follow the Kelvin characteristic

\[
\boxed{
k'=-L^Tk.
}
\]

Writing

\[
v(t)=\widehat r(k(t),t),
\]

we obtain

\[
v'+Lv+i k\widehat p
=-\nu|k|^2v,
\qquad
k\cdot v=0.
\]

Differentiate the incompressibility constraint:

\[
0
=(k\cdot v)'
=-k\cdot Lv+k\cdot v'.
\]

Substituting the amplitude equation yields

\[
0
=-2k\cdot Lv-i|k|^2\widehat p.
\]

Hence

\[
i\widehat p
=-2\frac{k\cdot Lv}{|k|^2}.
\]

Therefore

\[
\boxed{
v'
=-(I-2P_k)Lv
-\nu|k|^2v,
}
\]

where

\[
P_k=\frac{k\otimes k}{|k|^2}.
\]

## 3. Exact mode-energy identity

Take the Euclidean inner product with `v`. Since

\[
v\perp k,
\]

we have

\[
v\cdot P_kLv=0.
\]

Thus

\[
\frac12\frac d{dt}|v|^2
=-v\cdot Lv
-\nu|k|^2|v|^2.
\]

Decompose

\[
L=S+A,
\qquad
S^T=S,
\qquad
A^T=-A.
\]

Because

\[
v\cdot Av=0,
\]

we get the exact identity

\[
\boxed{
\frac12\frac d{dt}|v|^2
=-v^TSv
-\nu|k|^2|v|^2.
}
\]

This is the central result.

The antisymmetric affine part, equivalently the rigid-rotation/background-vorticity skew channel, can rotate the vector amplitude but cannot increase its Fourier-mode energy.

## 4. Wavevector magnitude is also controlled only by strain

From

\[
k'=-L^Tk
\]

we obtain

\[
\frac12\frac d{dt}|k|^2
=-k^TSk,
\]

because the antisymmetric part again drops out.

Hence if the accumulated affine strain satisfies

\[
\int_s^t\|S(\tau)\|d\tau\le K,
\]

then

\[
\boxed{
e^{-K}|k(s)|
\le
|k(t)|
\le
e^K|k(s)|.
}
\]

In particular,

\[
\int_s^t|k(\tau)|^2d\tau
\ge
e^{-2K}(t-s)|k(s)|^2.
\]

## 5. Homogeneous propagator bound

Integrating the mode-energy identity gives

\[
|v(t)|
\le
\exp\left(\int_s^t\|S(\tau)\|d\tau\right)
\exp\left(-\nu\int_s^t|k(\tau)|^2d\tau\right)
|v(s)|.
\]

Therefore on the bounded accumulated-strain branch,

\[
\boxed{
|v(t)|
\le
C_K
\exp\bigl(-c_K\nu(t-s)|k(s)|^2\bigr)
|v(s)|.
}
\]

After integration over Kelvin wavevectors (the flow is volume preserving because `tr L=0`), the full affine linear propagator has the same qualitative global `L2` structure:

- at most a bounded `C_K` amplitude factor from strain;
- parabolic frequency damping comparable to heat;
- no amplification caused by the antisymmetric affine/background-vorticity channel.

## 6. Consequence for previous-checkpoint inheritance

The earlier previous-checkpoint argument used heat contraction plus bounded-affine comparison constants. The Kelvin identity now gives a direct reason why this comparison is legitimate for the **full affine linearization**, not merely the kinematic affine+heat part.

A residual mode inherited from the previous checkpoint cannot recover frequency energy that viscosity has removed merely through mean affine rotation or the background-vorticity skew coupling.

Thus the statement

\[
B_{\rm inh}=o(m)
\]

should be interpreted as robust against full bounded accumulated-strain affine linear propagation, modulo the remaining conversion from global spectral control to a moving localized Gaussian variance.

## 7. Exact remaining localization problem

The Kelvin identity is global in Fourier space. A moving Gaussian window can still see redistribution of an energy-preserving field between spatial regions and between local Hermite coefficients.

Thus the unresolved linear question is now sharply formulated as

\[
\boxed{
\text{global Kelvin-energy-preserving affine redistribution}
\quad\Longrightarrow?\quad
\text{moving Gaussian/Hermite local variance control}.
}
\]

This is not an amplitude-growth problem.

Any future estimate of this lane should exploit the exact cancellations

\[
v\cdot P_kLv=0,
\qquad
v\cdot Av=0,
\qquad
k\cdot Ak=0,
\]

rather than bound the full affine operator by its absolute norm.

Status: **FULL AFFINE LINEAR MODE AMPLIFICATION REDUCED EXACTLY TO STRAIN; MEAN ROTATION / BACKGROUND-VORTICITY SKEW IS ENERGY-PRESERVING AT EACH KELVIN MODE / REMAINING ISSUE = LOCAL GAUSSIAN REDISTRIBUTION, NOT LINEAR GROWTH / GLOBAL REGULARITY NOT PROVED.**
