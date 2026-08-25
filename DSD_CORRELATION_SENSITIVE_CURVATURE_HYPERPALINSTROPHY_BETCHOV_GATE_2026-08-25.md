# DSD Correlation-Sensitive Curvature/Hyperpalinstrophy Betchov Gate

Date: 2026-08-25

Status: **HESSIAN-SUPREMUM LOSS REPLACED BY A MEAN HYPERPALINSTROPHY COST USING THE ANALYTIC THIRD-DERIVATIVE CEILING / NEW CORRELATION-SENSITIVE Z-WEIGHTED AMPLITUDE BOUND DERIVED / GLOBAL REGULARITY UNPROVED.**

## 1. Motivation

The previous dynamic-to-Leray audit showed that the uniform-envelope estimate

\[
\overline M_Z
\le
C_T^{-2/7}K_{2,L,+}^{3/7}Z_+^{2/7}
\]

cannot by itself beat the nontrivial first-hitting endpoint amplitude: the same Taylor thickness forcing the estimate also forces a matching lower enstrophy at a normalized maximum.

Therefore we must average before replacing the instantaneous Hessian by its global supremum.

The bounded-`Z` recurrent branch already has a finite mean hyperpalinstrophy cap

\[
\boxed{
\overline R
\le
R_{cap}
:=
\frac{C_*^8}{16}
\frac{Z_+^5}{\nu^8},
}
\]

where

\[
R=\|\Delta W\|_2^2.
\]

The no-`H` analytic corridor also supplies a finite third-derivative ceiling. Write

\[
\boxed{
K_{3,L}
:=
\sup_s\|\nabla^3W(s)\|_\infty
<\infty.
}
\]

The aim is to convert a large instantaneous vorticity Hessian into a spatially thick `R` cost and only then average.

---

## 2. Hessian spike forces hyperpalinstrophy

At a fixed Leray time define

\[
A(s):=\|\nabla^2W(s)\|_\infty.
\]

Choose one component/direction of the Hessian attaining `A` at a point `Y_0` (or approximate the supremum and pass to the limit).

Because the third derivative is bounded by `K_{3,L}`, that selected Hessian component is Lipschitz with constant at most `K_{3,L}`. Hence on

\[
|Y-Y_0|
\le
\frac{A}{2K_{3,L}},
\]

its absolute value remains at least `A/2`.

The full Hessian `L2` norm therefore obeys

\[
\begin{aligned}
\|\nabla^2W\|_2^2
&\ge
\left(\frac A2\right)^2
\frac{4\pi}{3}
\left(\frac{A}{2K_{3,L}}\right)^3\\
&=
\frac{\pi}{24}
\frac{A^5}{K_{3,L}^3}.
\end{aligned}
\]

On `R^3`, Fourier identity gives

\[
\boxed{
\|\nabla^2W\|_2^2
=\|\Delta W\|_2^2
=R.
}
\]

Thus

\[
\boxed{
A^5
\le
\frac{24}{\pi}K_{3,L}^3R.
}
\]

Equivalently,

\[
\boxed{
A^{3/7}
\le
\left(\frac{24}{\pi}\right)^{3/35}
K_{3,L}^{9/35}R^{3/35}.
}
\]

Status: **PROVED.**

---

## 3. Insert into the exact Taylor-thickness amplitude inequality

The previous exact Taylor calculation gives pointwise

\[
M
:=\|W\|_\infty
\le
C_T^{-2/7}
A^{3/7}Z^{2/7},
\]

where

\[
C_T=\frac{64\sqrt2\pi}{105}.
\]

Insert the Hessian-to-`R` estimate:

\[
\boxed{
M
\le
C_{CR}
K_{3,L}^{9/35}
R^{3/35}
Z^{2/7},
}
\]

with

\[
\boxed{
C_{CR}
:=
C_T^{-2/7}
\left(\frac{24}{\pi}\right)^{3/35}
\approx0.8955196181.
}
\]

This estimate no longer contains the instantaneous Hessian supremum as an independent factor.

---

## 4. Z-weighted recurrent average

Multiply by `Z`:

\[
MZ
\le
C_{CR}K_{3,L}^{9/35}
R^{3/35}Z^{9/7}.
\]

Since `Z<=Z_+`,

\[
Z^{9/7}
=Z\,Z^{2/7}
\le
Z\,Z_+^{2/7}.
\]

Hence

\[
\overline M_Z
:=
\frac{\langle MZ\rangle}{\langle Z\rangle}
\le
C_{CR}K_{3,L}^{9/35}Z_+^{2/7}
\frac{\langle ZR^{3/35}\rangle}{\langle Z\rangle}.
\]

Use the probability measure

\[
d\mu_Z
:=
\frac{Z(s)ds}{\langle Z\rangle}.
\]

Because `x^(3/35)` is concave,

\[
\int R^{3/35}d\mu_Z
\le
\left(\int R\,d\mu_Z\right)^{3/35}.
\]

Therefore

\[
\overline M_Z
\le
C_{CR}K_{3,L}^{9/35}Z_+^{2/7}
\left(
\frac{\langle ZR\rangle}{\langle Z\rangle}
\right)^{3/35}.
\]

Using `Z<=Z_+`,

\[
\langle ZR\rangle
\le
Z_+\langle R\rangle.
\]

Thus the correlation-sensitive estimate is

\[
\boxed{
\overline M_Z
\le
C_{CR}
K_{3,L}^{9/35}
Z_+^{13/35}
\left(
\frac{\overline R}{\overline Z}
\right)^{3/35}.
}
\]

Status: **PROVED.**

---

## 5. Insert the recurrent mean caps

The existing active-window construction gives a positive mean enstrophy floor

\[
\boxed{
\overline Z
\ge
Z_-
:=d_*z_*>0.
}
\]

The recurrent H1/Agmon balance gives

\[
\boxed{
\overline R
\le
R_{cap}
=
\frac{C_*^8}{16}
\frac{Z_+^5}{\nu^8}.
}
\]

Consequently

\[
\boxed{
\overline M_Z
\le
M_{CR}
:=
C_{CR}
K_{3,L}^{9/35}
Z_+^{13/35}
\left(
\frac{R_{cap}}{Z_-}
\right)^{3/35}.
}
\]

Substituting `R_cap` gives

\[
\boxed{
M_{CR}
\le
C_{CR}16^{-3/35}
C_*^{24/35}
K_{3,L}^{9/35}
Z_+^{4/5}
\nu^{-24/35}
Z_-^{-3/35}.
}
\]

Numerically,

\[
\boxed{
C_{CR}16^{-3/35}
\approx0.7060977379.
}
\]

Hence

\[
\boxed{
\overline M_Z
\le
0.7060977379\,
C_*^{24/35}
K_{3,L}^{9/35}
Z_+^{4/5}
\nu^{-24/35}
Z_-^{-3/35}.
}
\]

This is the first repository amplitude ceiling in this route that uses the **mean derivative budget before taking the recurrent amplitude bound**.

---

## 6. New Betchov empty-window certificate

The exact sup-free recurrent Betchov window is empty whenever

\[
\overline M_Z
+
\frac{32}{729\pi^4}
\frac{Z_+^2}{\nu^3}
<\frac12.
\]

It is therefore sufficient that

\[
\boxed{
M_{CR}
+
\frac{32}{729\pi^4}
\frac{Z_+^2}{\nu^3}
<\frac12.
}
\]

A fully substituted sufficient condition is

\[
\boxed{
0.7060977379\,
C_*^{24/35}
K_{3,L}^{9/35}
Z_+^{4/5}
\nu^{-24/35}
Z_-^{-3/35}
+
0.000450632966\,
\frac{Z_+^2}{\nu^3}
<\frac12.
}
\]

Status: **SUFFICIENT CLOSURE CERTIFICATE DERIVED; UNIVERSAL NUMERICAL VALIDITY NOT PROVED.**

---

## 7. Why this avoids the previous exact endpoint cancellation

The previous envelope route used

\[
K_{2,L,+}^{3/7}Z_+^{2/7}
\]

with both factors replaced by independent suprema. At a first-hitting maximum the Taylor-thickness lower bound then cancels the amplitude interpolation exactly and forces the envelope to be at least the endpoint Type-I amplitude.

The present route instead uses

\[
R^{3/35}
\]

inside the time average. A large Hessian at a sparse time is allowed, but it must create a spatially thick instantaneous hyperpalinstrophy cost; the finite **mean** `R` budget then controls how often/strongly this can happen.

Thus there is no algebraic identity forcing `M_CR` to exceed every endpoint amplitude.

This is a genuine correlation-sensitive improvement, not a relabeling of the previous supremum certificate.

---

## 8. Remaining constant dependence

The new certificate depends on

\[
\boxed{
K_{3,L},\quad
Z_+,\quad
Z_-=d_*z_*,\quad
C_*=C_NC_A,\quad
\nu.
}
\]

The repository already has explicit constructions for `d_*` and `z_*` from the terminal active windows, and `C_N=4/sqrt(6)` is explicit. The remaining non-numerically-optimized inputs are chiefly

1. the Agmon constant `C_A` used in the recurrent `R` cap;
2. the analytic third-derivative ceiling `K_{3,L}`;
3. the global bounded-enstrophy ceiling `Z_+` versus the active-core mean floor `Z_-`.

Unlike the previous envelope route, these constants enter with weak exponents `9/35`, `24/35`, and `3/35` except for the principal `Z_+^(4/5)` dependence.

---

## 9. DSD audit

The finite formed channels used here are

- Leray amplitude `M`;
- enstrophy `Z`;
- Hessian amplitude `A`;
- hyperpalinstrophy `R`;
- analytic third-derivative ceiling `K3_L`;
- invariant averages `bar Z`, `bar R`, and `bar M_Z`.

The key order of operations is

\[
\boxed{
\text{local curvature spike}
\to
\text{spatial }R\text{ cost}
\to
\text{time average}
\to
\text{Betchov scalar gate}.
}
\]

Taking the Hessian supremum before averaging is explicitly avoided.

---

## 10. Updated frontier

The next numerical/theoretical audit should compare

\[
Z_+=\sup Z
\]

against the explicit active-core floor

\[
Z_-=d_*z_*,
\]

and convert the dynamic analytic third-derivative ceiling to standard Leray coordinates. If

\[
K_{3,L}
\le
\mu_+^{5/2}K_{3,+},
\]

as dictated by the same coordinate scaling, then all quantities can again be expressed in the dynamic first-hitting constants without reintroducing a Hessian supremum cancellation.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
