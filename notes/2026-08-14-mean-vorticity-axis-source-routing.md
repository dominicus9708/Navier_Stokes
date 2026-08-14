# Mean-vorticity-axis routing of the residual stretching source

Date: 2026-08-14

Status: **DERIVED PROJECTIVE-DEFECT / MEAN-AXIS STRETCH-CONVERSION DICHOTOMY FOR AN EFFICIENT RESIDUAL STRETCH SOURCE**.

The exact residual stretching source is

\[
J_{\rm str}=\int\gamma\,\delta S\,\delta\Omega.
\]

The previous note showed that bounded accumulated affine strain cannot hide a fixed fraction of this source when the residual peak tends to zero.  The remaining geometric ambiguity is that the direction of `delta Omega` need not coincide pointwise with the total/material vorticity direction.  This note resolves the source at the Gaussian mean-vorticity level.

---

## 1. Longitudinal/transverse split

If

\[
\bar\Omega:=\int\gamma\Omega\ne0,
\]

define the mean vorticity axis

\[
\boxed{
e=\frac{\bar\Omega}{|\bar\Omega|}.
}
\]

Write

\[
\delta\Omega
=\alpha e+\beta,
\qquad
\beta\perp e.
\]

Then

\[
\boxed{
V_\omega
=V_\parallel+V_\perp,
}
\]

where

\[
V_\parallel=\int\gamma\alpha^2,
\qquad
V_\perp=\int\gamma|\beta|^2.
\]

Because the Gaussian mean has no perpendicular component,

\[
\boxed{
V_\perp
=\int\gamma|P_e^\perp\Omega|^2.
}
\]

Thus `V_perp` is directly a mean-axis projective/directional-defect quantity.

If `bar Omega=0`, then `delta Omega=Omega`, so the fluctuating-vorticity direction is already the total vorticity direction and the mean-axis reduction is unnecessary.

---

## 2. Split the stretching source

Write

\[
J_{\rm str}
=J_\parallel+J_\perp,
\]

with

\[
J_\parallel
=\int\gamma\,\alpha\,\delta S e,
\qquad
J_\perp
=\int\gamma\,\delta S\beta.
\]

Cauchy--Schwarz gives

\[
\boxed{
|J_\perp|
\le
\sqrt{V_SV_\perp}
\le
\sqrt{BV_\perp}.
}
\]

Suppose the stretching source is efficient:

\[
|J_{\rm str}|
\ge
\eta\sqrt{V_\omega B}
\]

for some fixed `eta>0`.

Fix

\[
0<\kappa<\eta^2.
\]

Then one of two branches occurs.

---

## 3. Transverse/projective branch

If

\[
\boxed{
V_\perp\ge\kappa V_\omega,
}
\]

then a fixed fraction of the vorticity fluctuation is perpendicular to the Gaussian mean axis:

\[
\boxed{
\int\gamma|P_e^\perp\Omega|^2
\ge
\kappa V_\omega.
}
\]

This is already a quantitative directional/projective defect.  No strain conversion is needed to type this branch.

---

## 4. Longitudinal mean-axis branch

If instead

\[
V_\perp<\kappa V_\omega,
\]

then

\[
|J_\perp|
<\sqrt\kappa\sqrt{V_\omega B}.
\]

Hence

\[
|J_\parallel|
\ge
(\eta-\sqrt\kappa)
\sqrt{V_\omega B}.
\]

Choose, for example,

\[
\kappa=\eta^2/4.
\]

Then

\[
\boxed{
|J_\parallel|
\ge
\frac\eta2\sqrt{V_\omega B}.
}
\]

Since

\[
|J_\parallel|^2
\le
V_\parallel
\int\gamma|\delta S e|^2
\le
V_\omega
\int\gamma|\delta S e|^2,
\]

we obtain

\[
\boxed{
\int\gamma|\delta S e|^2
\ge
\frac{\eta^2}{4}B.
}
\]

Thus an efficient source with small transverse vorticity defect forces order-`B` strain action on the **fixed Gaussian mean-vorticity axis**.

---

## 5. Split mean-axis strain into stretch and conversion

For symmetric `delta S`,

\[
\delta S e
=(e^T\delta S e)e
+(I-e\otimes e)\delta S e.
\]

Therefore

\[
\boxed{
|\delta S e|^2
=(e^T\delta S e)^2
+|(I-e\otimes e)\delta S e|^2.
}
\]

Consequently the longitudinal source forces at least one of

\[
\boxed{
\int\gamma(e^T\delta S e)^2
\ge
\frac{\eta^2}{8}B
}
\]

or

\[
\boxed{
\int\gamma|(I-e\otimes e)\delta S e|^2
\ge
\frac{\eta^2}{8}B.
}
\]

These are respectively

1. mean-vorticity-axis directional strain;
2. mean-vorticity-axis conversion/eigenframe participation.

---

## 6. Transfer to total strain modulo affine cancellation

Since

\[
S=\bar S+\delta S,
\]

for the fixed axis `e`,

\[
\int\gamma|Se|^2
\ge
\frac12\int\gamma|\delta S e|^2
-|\bar S e|^2.
\]

Thus at a longitudinal efficient-source time either

\[
\boxed{
\int\gamma|Se|^2
\gtrsim_\eta B
}
\]

or

\[
\boxed{
|\bar S|\gtrsim_\eta\sqrt B.
}
\]

The preceding affine-cancellation lemma shows that the second alternative cannot carry a fixed fraction of a vanishing residual pulse on a uniformly bounded accumulated-affine branch, because it would require

\[
\int|\bar S|ds\gtrsim m^{-1/2}\to\infty.
\]

Therefore a fixed fraction of the source survives in the total-strain mean-axis geometry.

Again,

\[
|Se|^2
=(e^TSe)^2
+|(I-e\otimes e)Se|^2,
\]

so the total-strain witness is a mean-axis stretch/compression or mean-axis conversion event.

---

## 7. Relation to total vorticity direction

In the longitudinal branch

\[
V_\perp\ll V_\omega,
\]

the total vorticity has small Gaussian mean-square component perpendicular to `e`:

\[
\int\gamma|P_e^\perp\Omega|^2
=V_\perp.
\]

Hence, except on a set controlled by this projective defect, the total vorticity direction is concentrated near the fixed axis `e` whenever its magnitude is not too small.

This gives the required bridge to the existing global-axis / projective geometry:

- if total vorticity frequently departs from `e`, pay the projective-defect channel;
- if it remains near `e`, mean-axis strain/conversion approximates the material vorticity-axis geometry.

A fully pathwise Cauchy estimate still requires controlling the low-vorticity set and tracking the mean axis in time, but there is no longer an untyped directional ambiguity.

---

## 8. Revised stretching-source exits

An efficient residual stretching source on the bounded-affine branch must now enter at least one of

\[
\boxed{
\begin{array}{ll}
\text{A.}&\text{transverse/projective vorticity defect},\\
\text{B.}&\text{mean-vorticity-axis directional strain},\\
\text{C.}&\text{mean-vorticity-axis conversion},\\
\text{D.}&\text{large accumulated affine strain}.
\end{array}
}
\]

Branch D is excluded for a fixed source fraction in the vanishing-residual bounded-affine regime by the `m^(-1/2)` cancellation cost.

The local residual source is therefore increasingly routed into the pre-existing projective / axis / Cauchy geometry rather than remaining an independent non-affine mechanism.

Status: **DIRECTIONAL AMBIGUITY OF THE STRETCH SOURCE REDUCED TO PROJECTIVE DEFECT OR MEAN-AXIS STRETCH/CONVERSION; PATHWISE TIME-TRACKING REMAINS**.
