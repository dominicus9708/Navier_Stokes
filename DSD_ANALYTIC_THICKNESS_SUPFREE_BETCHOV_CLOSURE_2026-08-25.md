# DSD Analytic-Thickness Sup-Free Betchov Closure

Date: 2026-08-25

Status: **GLOBAL LERAY VORTICITY AMPLITUDE BOUNDED BY `Z^(2/7)` FROM HESSIAN THICKNESS / Z-WEIGHTED TYPE-I AMPLITUDE EXPLICITLY CONTROLLED / NEW HESSIAN-ENSTROPHY BETCHOV CLOSURE CERTIFICATE DERIVED / NUMERIC CLOSURE DEPENDS ON SURVIVING `K2_L,Z_+` CONSTANTS / GLOBAL REGULARITY UNPROVED.**

## 1. Input

On the pure recurrent no-`H` analytic corridor, the standard Leray vorticity `W(Y,s)` has a uniform second-derivative bound

\[
\boxed{
\|\nabla_Y^2W(\cdot,s)\|_\infty
\le K_{2,L}<\infty
}
\]

for all sufficiently late recurrent times.

This follows from the stage-wide first-hitting analyticity corridor and the two-sided first-hitting/Leray clock comparison; the change between a natural stage normalization and standard Leray coordinates is bounded by fixed powers of the bounded clock factor.

Set

\[
M(s):=\|W(s)\|_\infty,
\qquad
Z(s):=\|W(s)\|_2^2.
\]

---

## 2. Taylor thickness at a global maximum

Choose a maximum point `Y0` and a unit vector

\[
\xi:=\frac{W(Y_0,s)}{M(s)}.
\]

Define the scalar directed vorticity

\[
f(Y):=\xi\cdot W(Y,s).
\]

At `Y0`,

\[
f(Y_0)=M.
\]

Because `Y0` maximizes `|W|`,

\[
\nabla|W|^2(Y_0)=0.
\]

Hence

\[
\boxed{
\nabla f(Y_0)=0.
}
\]

The Hessian ceiling gives

\[
f(Y)
\ge
M-rac{K_{2,L}}2|Y-Y_0|^2.
\]

Therefore

\[
|W(Y)|
\ge
\left(M-rac{K_{2,L}}2|Y-Y_0|^2\right)_+.
\]

Status: **PROVED.**

---

## 3. Integrate the full Taylor paraboloid

Let

\[
R_M:=\sqrt{\frac{2M}{K_{2,L}}}.
\]

Then

\[
\begin{aligned}
Z
&\ge
4\pi
\int_0^{R_M}
\left(M-rac{K_{2,L}}2r^2\right)^2r^2dr.
\end{aligned}
\]

Set

\[
r=R_M\rho.
\]

Since

\[
M-rac{K_{2,L}}2R_M^2\rho^2
=M(1-\rho^2),
\]

we obtain

\[
Z
\ge
4\pi M^2R_M^3
\int_0^1(1-\rho^2)^2\rho^2d\rho.
\]

The elementary integral is

\[
\int_0^1(1-\rho^2)^2\rho^2d\rho
=
\frac8{105}.
\]

Also

\[
R_M^3
=
2^{3/2}M^{3/2}K_{2,L}^{-3/2}.
\]

Hence

\[
\boxed{
Z
\ge
C_T
K_{2,L}^{-3/2}M^{7/2},
}
\]

where

\[
\boxed{
C_T
:=
\frac{64\sqrt2\pi}{105}
\approx2.7080429337.
}
\]

This generalizes the repository's endpoint lower-enstrophy formula from the normalized case `M=1` to arbitrary recurrent Leray amplitude `M`.

Status: **PROVED EXACTLY.**

---

## 4. Invert the thickness inequality

The preceding estimate gives

\[
M^{7/2}
\le
C_T^{-1}K_{2,L}^{3/2}Z.
\]

Therefore

\[
\boxed{
M
\le
C_T^{-2/7}
K_{2,L}^{3/7}
Z^{2/7}.
}
\]

Numerically,

\[
\boxed{
C_T^{-2/7}
\approx0.7522879923.
}
\]

Thus the global Type-I amplitude is controlled by instantaneous enstrophy on the analytic corridor.

Status: **PROVED.**

---

## 5. Bound the Z-weighted recurrent amplitude

Multiply by `Z`:

\[
MZ
\le
C_T^{-2/7}K_{2,L}^{3/7}Z^{9/7}.
\]

On the bounded-enstrophy branch

\[
Z\le Z_+,
\]

so

\[
Z^{9/7}=Z\,Z^{2/7}
\le
Z\,Z_+^{2/7}.
\]

Averaging gives

\[
\langle MZ\rangle
\le
C_T^{-2/7}K_{2,L}^{3/7}Z_+^{2/7}
\langle Z\rangle.
\]

Hence the exact sup-free amplitude from the previous note satisfies

\[
\boxed{
\overline M_Z
\le
M_{AZ}
:=
C_T^{-2/7}
K_{2,L}^{3/7}Z_+^{2/7}.
}
\]

Numerically,

\[
\boxed{
M_{AZ}
\le
0.7522879923\,
K_{2,L}^{3/7}Z_+^{2/7}.
}
\]

This can be substantially smaller than the coarse first-hitting supremum `K_I` when enstrophy and analytic curvature are moderate.

Status: **PROVED.**

---

## 6. Insert into the exact recurrent Betchov window

The sup-free Betchov window is

\[
\nu\bar\lambda
+\frac14-\frac{\overline M_Z}{2}
\le
C_BZ_+^{1/2}\bar\lambda^{3/4},
\]

where

\[
C_B=\frac8{\pi3^{9/4}}.
\]

Using `overline M_Z<=M_AZ`, every recurrent survivor must satisfy the weaker but explicit necessary inequality

\[
\boxed{
\nu\bar\lambda
+\frac14-\frac{M_{AZ}}2
\le
C_BZ_+^{1/2}\bar\lambda^{3/4}.
}
\]

Thus the analytic Hessian thickness replaces the coarse temporal Type-I supremum in the scalar compatibility test.

---

## 7. New empty-window closure certificate

The quartic minimum calculation gives a sufficient contradiction if

\[
M_{AZ}
+
\frac{32}{729\pi^4}
\frac{Z_+^2}{\nu^3}
<
\frac12.
\]

Therefore a completely explicit analytic-thickness Betchov certificate is

\[
\boxed{
C_T^{-2/7}
K_{2,L}^{3/7}Z_+^{2/7}
+
\frac{32}{729\pi^4}
\frac{Z_+^2}{\nu^3}
<
\frac12
\quad\Longrightarrow\quad
\text{no nonzero recurrent survivor}.
}
\]

Using the numerical Taylor constant,

\[
\boxed{
0.7522879923
K_{2,L}^{3/7}Z_+^{2/7}
+
\frac{32}{729\pi^4}
\frac{Z_+^2}{\nu^3}
<0.5
}
\]

is sufficient.

Status: **PROVED CONDITIONAL CLOSURE CERTIFICATE.**

---

## 8. Frequency-floor version

Let

\[
 c_{core}>0
\]

be a proven active-core lower bound for

\[
\bar\lambda.
\]

Define

\[
x_0:=c_{core}^{1/4},
\qquad
x_*:=\frac{3C_BZ_+^{1/2}}{4\nu}.
\]

If

\[
x_0\ge x_*
\]

and

\[
\boxed{
\nu c_{core}
+\frac14-rac{M_{AZ}}2
>
C_BZ_+^{1/2}c_{core}^{3/4},
}
\]

then the allowed Betchov frequency window lies entirely below the active-core floor, and recurrence is impossible.

Status: **PROVED CONDITIONAL CLOSURE CERTIFICATE.**

---

## 9. Why the exponent `2/7` is natural

At a maximum, first derivatives of the directed vorticity vanish. Therefore a second-derivative ceiling produces a ball radius

\[
R_M\sim(M/K_2)^{1/2}.
\]

The vorticity-squared mass in that ball scales as

\[
M^2R_M^3
\sim
K_2^{-3/2}M^{7/2}.
\]

Inverting gives

\[
M\sim K_2^{3/7}Z^{2/7}.
\]

Thus the `2/7` exponent is the exact three-dimensional Hessian-thickness exponent, not an interpolation artifact.

---

## 10. DSD audit

This calculation couples three previously separate formed channels:

- pointwise recurrent amplitude `M`;
- analytic curvature `K2_L`;
- global normalized enstrophy `Z`.

The maximum-point formation condition `grad |W|^2=0` is used explicitly; a generic point would only give the weaker first-derivative thickness exponent.

No tail `L3` assumption is used.

---

## 11. Remaining quantitative question

The new condition may or may not hold for the current broad no-`H` analytic constants. The repository has finite bounds for `K2_L` and `Z_+`, but they were designed as qualitative compactness constants rather than optimized numerical values.

Thus the next high-value calculation is no longer another structural branch split. It is to **tighten the surviving analytic Hessian and enstrophy ceilings** and evaluate the explicit scalar

\[
\boxed{
\mathcal B_{AZ}
:=
0.7522879923
K_{2,L}^{3/7}Z_+^{2/7}
+
\frac{32}{729\pi^4}
\frac{Z_+^2}{\nu^3}.
}
\]

If

\[
\mathcal B_{AZ}<1/2,
\]

the recurrent pure core closes.

If not, the excess identifies quantitatively whether the survivor is being protected by analytic curvature `K2_L` or global enstrophy capacity `Z_+`.

---

## 12. Verdict

### PROVED

- exact maximum-point Hessian thickness for arbitrary Leray amplitude;
- `M <= const K2^(3/7) Z^(2/7)`;
- explicit upper bound on the true recurrent `Z`-weighted Type-I amplitude;
- new Hessian-enstrophy Betchov closure criterion.

### OPEN

- whether current optimized corridor constants satisfy the new criterion;
- universal recurrent-core elimination when they do not;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
