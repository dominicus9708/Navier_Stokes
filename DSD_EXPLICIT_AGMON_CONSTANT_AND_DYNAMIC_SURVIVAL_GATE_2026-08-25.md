# DSD Explicit Agmon Constant and Dynamic Survival Gate

Date: 2026-08-25

Status: **EXPLICIT WHOLE-SPACE AGMON CONSTANT DERIVED BY FOURIER SPLITTING / `C_*` REMOVED AS A FREE CONSTANT / DYNAMIC ENSTROPHY SURVIVAL FLOOR REDUCED TO FIRST-HITTING ANALYTIC-TIGHTNESS PARAMETERS / GLOBAL REGULARITY UNPROVED.**

## 1. Goal

The corrected active-core two-sided hyperpalinstrophy window gives the necessary dynamic first-hitting enstrophy floor

\[
Z_{D,+}
\ge
0.6168041085\,
 d_L^{3/25}
 C_*^{-24/25}
 \nu^{24/25}
 K_{3,+}^{-9/25}
 \left(\frac{\mu_-}{\mu_+}\right)^{7/5},
\]

where

\[
C_*=C_NC_A,
\qquad
C_N=\frac4{\sqrt6},
\]

and `C_A` is any admissible constant in the whole-space three-dimensional Agmon inequality

\[
\|F\|_\infty
\le
C_A
\|F\|_2^{1/4}
\|\Delta F\|_2^{3/4}.
\]

This note derives an explicit admissible `C_A` directly, so it need not remain symbolic.

---

## 2. Fourier convention

Use the unitary Fourier transform on `R^3`:

\[
\widehat F(\xi)
=(2\pi)^{-3/2}
\int_{\mathbb R^3}e^{-ix\cdot\xi}F(x)dx.
\]

Then Plancherel gives

\[
\|\widehat F\|_2=\|F\|_2,
\qquad
\||\xi|^2\widehat F\|_2
=\|\Delta F\|_2.
\]

For vector/tensor fields, use the Euclidean/Frobenius norm inside the Fourier integral. The same scalar Cauchy-Schwarz estimates apply component-free.

Let

\[
A:=\|F\|_2,
\qquad
B:=\|\Delta F\|_2.
\]

---

## 3. Low-frequency part

For any `R>0`,

\[
\int_{|\xi|\le R}|\widehat F(\xi)|d\xi
\le
\left(\frac{4\pi}{3}R^3\right)^{1/2}A.
\]

Define

\[
a:=\left(\frac{4\pi}{3}\right)^{1/2}.
\]

Then the low-frequency contribution is at most

\[
aAR^{3/2}.
\]

---

## 4. High-frequency part

For `|xi|>R`, insert `|xi|^-2 |xi|^2` and apply Cauchy-Schwarz:

\[
\begin{aligned}
\int_{|\xi|>R}|\widehat F|d\xi
&\le
\left(
\int_{|\xi|>R}|\xi|^{-4}d\xi
\right)^{1/2}
B\\
&=
\left(4\pi\int_R^\infty r^{-2}dr\right)^{1/2}B\\
&=
(4\pi)^{1/2}R^{-1/2}B.
\end{aligned}
\]

Define

\[
b:=(4\pi)^{1/2}.
\]

Thus

\[
\|F\|_\infty
\le
(2\pi)^{-3/2}
\left(
aAR^{3/2}
+bBR^{-1/2}
\right).
\]

---

## 5. Optimize the split radius

Set

\[
g(R)=aAR^{3/2}+bBR^{-1/2}.
\]

The critical point obeys

\[
\frac32aAR^{1/2}
-
\frac12bBR^{-3/2}=0,
\]

hence

\[
\boxed{
R^2=\frac{bB}{3aA}.
}
\]

At this radius the high-frequency contribution is three times the low-frequency contribution, so

\[
g(R_*)
=4aAR_*^{3/2}.
\]

Therefore

\[
\|F\|_\infty
\le
(2\pi)^{-3/2}
4a^{1/4}b^{3/4}3^{-3/4}
A^{1/4}B^{3/4}.
\]

The constant simplifies to

\[
\boxed{
C_A^{FS}
=
\frac{2\sqrt2}{\pi\,3^{7/8}}.
}
\]

Numerically,

\[
\boxed{C_A^{FS}\approx0.3442817667.}
\]

Thus the admissible explicit Agmon inequality is

\[
\boxed{
\|F\|_\infty
\le
\frac{2\sqrt2}{\pi\,3^{7/8}}
\|F\|_2^{1/4}
\|\Delta F\|_2^{3/4}.
}
\]

This constant is not claimed sharp; it is an explicit safe constant obtained from the stated Fourier split.

Status: **PROVED.**

---

## 6. Explicit nonlinear H1 constant

The recurrent H1 note uses

\[
C_N=\frac4{\sqrt6}.
\]

Therefore one may choose

\[
\begin{aligned}
C_*^{FS}
&:=C_NC_A^{FS}\\
&=
\frac4{\sqrt6}
\frac{2\sqrt2}{\pi3^{7/8}}\\
&=
\boxed{
\frac8{\pi3^{11/8}}.
}
\end{aligned}
\]

Numerically,

\[
\boxed{C_*^{FS}\approx0.5622097708.}
\]

Hence the previous mean hyperpalinstrophy cap may be written explicitly as

\[
\boxed{
\overline R
\le
\frac{(C_*^{FS})^8}{16}
\frac{Z_{L,+}^5}{\nu^8}.
}
\]

---

## 7. Remove `C_*` from the dynamic survival floor

Insert `C_*^{FS}` into

\[
Z_{D,surv,-}
=
0.6168041085\,
 d_L^{3/25}
 C_*^{-24/25}
 \nu^{24/25}
 K_{3,+}^{-9/25}
 \left(\frac{\mu_-}{\mu_+}\right)^{7/5}.
\]

The numerical prefactor becomes

\[
0.6168041085
(C_*^{FS})^{-24/25}
\approx
\boxed{1.0721234726}.
\]

Therefore every recurrent survivor on the stated corridor must satisfy

\[
\boxed{
Z_{D,+}
\ge
1.0721234726\,
 d_L^{3/25}
 \nu^{24/25}
 K_{3,+}^{-9/25}
 \left(\frac{\mu_-}{\mu_+}\right)^{7/5}.
}
\]

Status: **NECESSARY DYNAMIC SURVIVAL FLOOR WITH NO FREE AGMON CONSTANT.**

---

## 8. Insert the dynamic tightness ceiling

The non-`T` tightness corridor gives

\[
\boxed{
Z_{D,+}
\le
\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}.
}
\]

Hence the recurrent branch is excluded if

\[
\boxed{
\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}
<
1.0721234726\,
 d_L^{3/25}
 \nu^{24/25}
 K_{3,+}^{-9/25}
 \left(\frac{\mu_-}{\mu_+}\right)^{7/5}.
}
\]

This is now a finite explicit first-hitting/tightness inequality.

---

## 9. Expand the active-window constants

The existing terminal analytic-window note gives

\[
\boxed{
\delta_D
=
\frac1{4(2B_++3\nu K_{2,+})},
}
\]

\[
\boxed{
\mu_-
=
\frac{L_-}{q}e^{-B_+\delta_D},
}
\]

\[
\boxed{
\mu_+
=
\frac{L_+q}{q-1}
+
\delta_De^{B_+\delta_D},
}
\]

and

\[
\boxed{
G_L
=
\log\left[
q\frac{L_+q/(q-1)}{L_-/q}
\right].
}
\]

The active-window density is

\[
\boxed{
 d_L
=
\min\left\{
1,
\frac{\delta_D}{\mu_+G_L}
\right\}.
}
\]

Thus a fully expanded sufficient contradiction is

\[
\boxed{
\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}
<
1.0721234726
\left[
\min\left\{
1,
\frac{\delta_D}{\mu_+G_L}
\right\}
\right]^{3/25}
\nu^{24/25}
K_{3,+}^{-9/25}
\left[
\frac{(L_-/q)e^{-B_+\delta_D}}
{L_+q/(q-1)+\delta_De^{B_+\delta_D}}
\right]^{7/5}.
}
\]

Every symbol on the right is now a first-hitting analytic/stage constant or viscosity.

---

## 10. What remains numerically free

The universal interpolation constant has been removed. The remaining quantities are

\[
\boxed{
q,
L_-,
L_+,
B_+,
K_{2,+},
K_{3,+},
R_Z,
\varepsilon_Z,
\nu.
}
\]

These are not all independent:

- `delta_D` depends on `B_+`, `K2,+`, and `nu`;
- `mu_-`, `mu_+` depend on the stage/analytic constants;
- `d_L` depends on the same clock variables;
- `R_Z,epsilon_Z` describe the non-turnover enstrophy tightness class.

The next useful audit is therefore not another universal functional inequality. It is a compatibility analysis among these finite first-hitting constants, especially whether the analytic corridor itself forces a relation between `K3,+`, the tightness radius `R_Z`, and the stage ceilings `L_-,L_+` strong enough to empty the survival interval.

---

## 11. DSD audit

The argument uses only standard Fourier analysis and the previously formed finite recurrent channels.

The important reduction is

\[
\boxed{
\text{unknown universal }C_A
\quad\longrightarrow\quad
C_A^{FS}
=
\frac{2\sqrt2}{\pi3^{7/8}}.
}
\]

No claim of sharpness is needed: an explicit admissible upper constant is sufficient for the recurrent hyperpalinstrophy cap.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
