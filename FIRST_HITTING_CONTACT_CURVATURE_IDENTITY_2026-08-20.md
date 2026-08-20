# First-Hitting Maximum Contact-Curvature Identity — 2026-08-20

Overall status: **EXACT MAXIMUM-POINT DYNAMIC IDENTITY (A.E. REGULAR TIMES) — GLOBAL REGULARITY NOT PROVED.**

This note connects the active `||Omega||_infty=1` contact geometry directly to derivative cost in the dynamic first-hitting normalization.

---

## 1. Normalized vorticity equation

With

\[
W=\|\omega\|_\infty,
\qquad
\lambda=W^{1/2},
\qquad
\frac{ds}{dt}=W,
\]

\[
U=\lambda^{-1}u,
\qquad
\Omega=\lambda^{-2}\omega,
\qquad
\|\Omega(s)\|_\infty=1,
\]

and

\[
a=\frac{W'}{2W^2},
\]

the normalized vorticity equation is

\[
\partial_s\Omega
=S_U\Omega
-(U-c)\cdot\nabla\Omega
+\nu\Delta\Omega
-a(2\Omega+y\cdot\nabla\Omega).
\]

The exact drift convention is immaterial for the maximum projection because all first-order transport terms vanish when projected onto the gradient of `|Omega|` at a spatial maximum.

---

## 2. Maximum-point projection

At an a.e. regular time choose a maximum point `y_*(s)` with

\[
|\Omega(y_*,s)|=1.
\]

At that point

\[
\nabla |\Omega|^2=0.
\]

Since the normalized supremum is identically one, the envelope derivative of the maximum vanishes at a.e. differentiability time:

\[
\frac{d}{ds}\frac12\|\Omega(s)\|_\infty^2=0.
\]

Dotting the vorticity equation with `Omega` at `y_*` gives

\[
0
=\Omega\cdot S_U\Omega
+\nu\Omega\cdot\Delta\Omega
-2a.
\]

Define

\[
\Gamma=\xi^TS_U\xi,
\qquad
\xi=\Omega/|\Omega|.
\]

At the maximum `|Omega|=1`, hence

\[
\boxed{
\Gamma-2a
=-\nu\,\Omega\cdot\Delta\Omega.
}
\]

---

## 3. Contact curvature lower bound

At a maximum of `|Omega|^2`,

\[
\Delta\frac{|\Omega|^2}{2}\le0.
\]

But

\[
\Delta\frac{|\Omega|^2}{2}
=\Omega\cdot\Delta\Omega+|\nabla\Omega|^2.
\]

Therefore

\[
-\Omega\cdot\Delta\Omega
\ge
|\nabla\Omega|^2.
\]

Combining with the exact maximum projection yields

\[
\boxed{
\Gamma-2a
\ge
\nu|\nabla\Omega|^2.
}
\]

Since the magnitude has zero gradient at a smooth nonzero maximum, writing `Omega=rho xi` gives

\[
\nabla\rho=0,
\]

and therefore

\[
|\nabla\Omega|^2=|\nabla\xi|^2.
\]

Hence also

\[
\boxed{
\Gamma-2a
\ge
\nu|\nabla\xi|^2.
}
\]

This recovers and sharpens the previously used first-hitting maximum inequality.

---

## 4. Interpretation

The minimum stretching needed merely to keep pace with the dynamic normalization is

\[
2a.
\]

Any excess stretching

\[
\Gamma-2a
\]

is exactly the viscous contact-curvature quantity

\[
-\nu\Omega\cdot\Delta\Omega
\]

and is bounded below by the pointwise palinstrophy density at the maximum.

Thus a contact point cannot obtain arbitrarily large stretching above the scale-growth rate for free:

\[
\boxed{
\Gamma\gg2a
\Longrightarrow
|\nabla\Omega|^2\gg1/\nu.
}
\]

This routes a strong contact-stretching excess directly toward the derivative channel `H`.

---

## 5. Flat-contact alternative

On a non-H branch the contact derivative is controlled. Therefore any maximum-point stretching responsible for repeated first-hitting growth must remain close, in the quantified sense above, to the normalization floor `2a`, unless another derivative packet appears.

The remaining contact-dominated alternative is consequently a relatively flat maximum-vorticity contact set or a contact point with bounded curvature, coupled to the projective strain geometry rather than a sharply concentrated vorticity spike.

This narrows the KKT contact branch:

\[
\boxed{
\text{contact-dominated threshold}
\Longrightarrow
H
\quad\text{or}\quad
\text{flat/controlled-curvature contact geometry}.
}
\]

---

## 6. Regularity caveat

The identity is intended at times where the supremum is differentiable and a smooth maximizing point can be selected, which is sufficient for the first-hitting a.e. ledger. A completely nonsmooth maximum-set formulation should be written using Dini derivatives/subdifferentials and is a separate technical task.

Status: **AT A REGULAR FIRST-HITTING MAXIMUM, THE EXCESS STRETCHING OVER 2a IS EXACTLY A VISCOUS CONTACT-CURVATURE TERM AND DOMINATES THE POINTWISE GRADIENT COST. STRONG EXCESS STRETCHING THEREFORE ROUTES DIRECTLY TO H. GLOBAL REGULARITY REMAINS UNPROVED.**