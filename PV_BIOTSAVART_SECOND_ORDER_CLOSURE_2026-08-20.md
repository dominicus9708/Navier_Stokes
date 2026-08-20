# Second-Order Biot--Savart Closure Bound for Recurrent P_V — 2026-08-20

Overall status: **DIRECT SYSTEM-II CLOSURE ATTEMPT — GLOBAL REGULARITY NOT PROVED.**

This note replaces the previous strain-amplitude ceiling based on `||S||_2` and `||grad S||_infinity` by a more direct bound using the vorticity Biot--Savart kernel, its parity cancellation, first-hitting analyticity, and vorticity tightness.

## 1. Strain kernel

For divergence-free vorticity on `R^3`, the strain has the principal-value representation

\[
S(x)
=
\frac{3}{8\pi}
\operatorname{p.v.}\int
\frac{
(\hat z\times\omega(x-z))\otimes\hat z
+\hat z\otimes(\hat z\times\omega(x-z))
}{|z|^3}
\,dz,
\]

with `hat z = z/|z|`.

The Frobenius norm of the angular tensor satisfies

\[
\left|
(\hat z\times a)\otimes\hat z
+\hat z\otimes(\hat z\times a)
\right|_F
\le
\sqrt2\,|a|.
\]

Hence the kernel norm coefficient is

\[
\boxed{c_K=\frac{3\sqrt2}{8\pi}.}
\]

The angular kernel has zero spherical mean and is even under `z -> -z`.

## 2. Constant and linear Taylor terms both cancel in the near field

Fix a radius `R`. Because the principal-value kernel has zero angular mean, the constant term `omega(x)` contributes zero on the centered ball.

Because the kernel is even while the linear Taylor term `(grad omega(x))z` is odd, the entire linear term also integrates to zero on the centered ball.

Thus in `|z|<R` one may replace `omega(x-z)` by the second-order Taylor remainder.

Define the directional Hessian bound

\[
K_2
:=
\sup_x\sup_{|v|=1}
|(v\cdot\nabla)^2\omega(x)|.
\]

Taylor's theorem gives

\[
|\omega(x-z)-\omega(x)+(\nabla\omega(x))z|
\le
\frac12K_2|z|^2.
\]

Therefore

\[
\begin{aligned}
|S_{near}(x)|
&\le
c_K\frac{K_2}{2}
\int_{|z|<R}\frac{|z|^2}{|z|^3}\,dz\\
&=
\frac{3\sqrt2}{8}K_2R^2.
\end{aligned}
\]

Hence

\[
\boxed{
|S_{near}|
\le
A K_2R^2,
\qquad
A=\frac{3\sqrt2}{8}.
}
\]

## 3. Far-field L2 bound

For `|z|>R`, Cauchy--Schwarz yields

\[
|S_{far}(x)|
\le
c_K
\|\omega\|_2
\left(
\int_{|z|>R}|z|^{-6}dz
\right)^{1/2}.
\]

Since

\[
\int_{|z|>R}|z|^{-6}dz
=\frac{4\pi}{3R^3},
\]

we obtain

\[
\boxed{
|S_{far}|
\le
C\|\omega\|_2R^{-3/2},
\qquad
C=\frac{\sqrt6}{4\sqrt\pi}.
}
\]

Thus for every `R>0`,

\[
\boxed{
\|S\|_\infty
\le
A K_2R^2
+C\|\omega\|_2R^{-3/2}.
}
\]

## 4. Optimize the splitting radius

The optimal radius satisfies

\[
R^{7/2}
=
\frac{3C}{4A}
\frac{\|\omega\|_2}{K_2}.
\]

Since

\[
\frac{3C}{4A}
=\frac{\sqrt3}{2\sqrt\pi},
\]

substitution gives

\[
\boxed{
\|S\|_\infty
\le
C_{BS,2}
K_2^{3/7}
Z^{2/7},
}
\]

where

\[
Z=\|\omega\|_2^2
\]

and

\[
C_{BS,2}
=
\frac{7\sqrt2}{8}
\left(\frac{3}{4\pi}\right)^{2/7}
\approx0.8218327582.
\]

This is an explicit second-order Biot--Savart interpolation bound.

## 5. Insert the exact non-normality H1 ceiling

The vorticity-gradient representation gives

\[
N
=\frac12\int
S:(G^TG-GG^T),
\qquad G=\nabla\omega.
\]

Bottcher--Wenzel together with the exact whole-space isometry

\[
\|\nabla\omega\|_2^2
=2\|\nabla S\|_2^2
=2P
\]

gives

\[
\boxed{
N\le\sqrt2\,\|S\|_\infty P.
}
\]

Therefore

\[
q:=\frac NP
\le
\sqrt2\,\|S\|_\infty.
\]

Combining with the optimized Biot--Savart estimate,

\[
\boxed{
q
\le
\frac74
\left(\frac{3}{4\pi}\right)^{2/7}
K_2^{3/7}Z^{2/7}.
}
\]

## 6. Use first-hitting vorticity tightness

At first-hitting normalization,

\[
\|\Omega\|_\infty\le1.
\]

Suppose a non-turnover compact class has a vorticity tightness radius `R_Z` with

\[
\int_{B_{R_Z}}|\Omega|^2
\ge
(1-\varepsilon_Z)Z.
\]

Then

\[
(1-\varepsilon_Z)Z
\le
|B_{R_Z}|
=\frac{4\pi}{3}R_Z^3.
\]

Hence

\[
\boxed{
Z
\le
\frac{4\pi}{3(1-\varepsilon_Z)}R_Z^3.
}
\]

Substitution into the preceding `q` estimate cancels the geometric constants exactly:

\[
\boxed{
q
\le
\frac74
K_2^{3/7}
R_Z^{6/7}
(1-\varepsilon_Z)^{-2/7}.
}
\]

The exact coefficient `7/4` is a consequence of the second-order near-field cancellation and the three-dimensional ball volume.

## 7. First-hitting analyticity supplies K2

If the normalized first-hitting vorticity extends analytically to a complex strip of radius `rho_0` with

\[
\sup_{|\operatorname{Im}y|<\rho_0}|\Omega(y)|\le M_0,
\]

then one-dimensional Cauchy estimates along every real direction give

\[
\boxed{
K_2
\le
\frac{2M_0}{\rho_0^2}.
}
\]

Thus

\[
\boxed{
q
\le
\frac74
\left(\frac{2M_0}{\rho_0^2}\right)^{3/7}
R_Z^{6/7}
(1-\varepsilon_Z)^{-2/7}.
}
\]

On the smooth rapidly-decaying vorticity analyticity track, one may write symbolically

\[
M_0=M,
\qquad
\rho_0=\frac{\sqrt{\sigma\nu}}{c(M)},
\]

so

\[
\boxed{
q
\le
\frac74
\left(
\frac{2M c(M)^2}{\sigma\nu}
\right)^{3/7}
R_Z^{6/7}
(1-\varepsilon_Z)^{-2/7}.
}
\]

## 8. Direct recurrent closure criterion

The Leray H1 identity forces, at recovery/checkpoint times,

\[
q\ge q_-.
\]

Therefore the entire recurrent `P_V` branch is impossible if

\[
\boxed{
q_-
>
\frac74
K_2^{3/7}
R_Z^{6/7}
(1-\varepsilon_Z)^{-2/7}.
}
\]

This criterion is independent of the previous strain Lipschitz constant `L_+` and strain `L2` ceiling `E_+`. The remaining class inputs are now only

\[
K_2,
\qquad
R_Z,
\qquad
\varepsilon_Z,
\qquad
q_-.
\]

The two-parameter compatibility tax from `PV_TWO_PARAMETER_COHERENT_CLOSURE_2026-08-20.md` can be inserted on top of this universal non-normality ceiling to lower the right-hand side further on the positive-middle coherent subbranch.

Status: **THE RECURRENT P_V BRANCH NOW HAS A DIRECT EXPLICIT BIOT--SAVART/NON-NORMALITY CEILING `q <= (7/4) K2^(3/7) R_Z^(6/7) (1-eps_Z)^(-2/7)`. IF THE LERAY RECURRENCE FLOOR EXCEEDS THIS VALUE, SYSTEM II CLOSES. GLOBAL REGULARITY REMAINS UNPROVED.**