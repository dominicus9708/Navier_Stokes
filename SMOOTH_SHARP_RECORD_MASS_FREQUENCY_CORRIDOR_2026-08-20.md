# Smooth Sharp Record-Mass Frequency Corridor — 2026-08-20

Status: **SHARPENED S-LEVEL FIRST-HITTING ENDPOINT GATE / GLOBAL REGULARITY NOT PROVED.**

This note improves the record-point mass lower bound in `SMOOTH_QUANTILE_FREQUENCY_CORRIDOR_2026-08-20.md` by integrating the full positive quadratic Taylor lower envelope instead of only a half-amplitude ball.

## 1. Record-point scalar projection

At an actual smooth first-hitting endpoint choose `y_*` with

\[
|\Omega(y_*)|=1,
\qquad
\xi=\Omega(y_*).
\]

Set

\[
g(y)=\xi\cdot\Omega(y).
\]

Then

\[
g(y_*)=1,
\qquad
\nabla g(y_*)=0.
\]

Let

\[
K_2=
\sup_y\sup_{|v|=1}
|(v\cdot\nabla)^2\Omega(y)|.
\]

Along every radial segment from `y_*`, Taylor's theorem gives

\[
\boxed{
g(y_*+h)\ge1-\frac12K_2|h|^2.}
\]

The right side remains nonnegative for

\[
|h|\le\sqrt{2/K_2}.
\]

## 2. Integrate the full positive quadratic envelope

Because `|Omega|^2 >= g^2` wherever `g>=0`, write

\[
r=K_2^{-1/2}s.
\]

Then

\[
\begin{aligned}
Z=\|\Omega\|_2^2
&\ge
4\pi K_2^{-3/2}
\int_0^{\sqrt2}
 s^2\left(1-\frac{s^2}{2}\right)^2ds.
\end{aligned}
\]

The integral is exact:

\[
\int_0^{\sqrt2}
 s^2\left(1-\frac{s^2}{2}\right)^2ds
=
\frac{16\sqrt2}{105}.
\]

Therefore

\[
\boxed{
Z
\ge
C_ZK_2^{-3/2},
\qquad
C_Z=\frac{64\sqrt2\pi}{105}
\approx2.7080429337.
}
\]

This improves the previous `pi/3` coefficient by a factor about `2.586`.

## 3. Combine with derivative quantile tightness

If

\[
\int_{B_{R_Q}}|\nabla\Omega|^2
\ge
(1-\varepsilon_Q)Q
\]

and

\[
K_1=\|\nabla\Omega\|_\infty,
\]

then

\[
Q\le
\frac{4\pi}{3(1-\varepsilon_Q)}K_1^2R_Q^3.
\]

Since `lambda=Q/Z`, the sharpened upper bound is

\[
\boxed{
\lambda
\le
\frac{35}{16\sqrt2}
\frac{K_1^2K_2^{3/2}R_Q^3}
{1-\varepsilon_Q}.
}
\]

Indeed

\[
\frac{(4\pi/3)}{64\sqrt2\pi/105}
=
\frac{35}{16\sqrt2}.
\]

## 4. Sharpened Clay-data substitution

With

\[
K_1\le M_0/\rho_0,
\qquad
K_2\le2M_0/\rho_0^2,
\]

we obtain the particularly clean coefficient

\[
\boxed{
\lambda_+
\le
\frac{35}{8}
\frac{M_0^{7/2}}{1-\varepsilon_Q}
\frac{R_Q^3}{\rho_0^5}.
}
\]

The lower frequency from vorticity quantile tightness remains

\[
\lambda_-
=
 c_S\frac{1-\varepsilon_Z}{R_Z^2},
\qquad
c_S\approx2.1080877498.
\]

Hence the smooth endpoint corridor is empty whenever

\[
\boxed{
\left(\frac{R_Z}{\rho_0}\right)^2
\left(\frac{R_Q}{\rho_0}\right)^3
<
\frac{8c_S}{35M_0^{7/2}}
(1-\varepsilon_Z)(1-\varepsilon_Q).
}
\]

## 5. M0=2 numerical closure region

For `M_0=2`,

\[
\boxed{
\frac{8c_S}{35\,2^{7/2}}
\approx0.04258980409.
}
\]

Therefore

\[
\boxed{
\left(\frac{R_Z}{\rho_0}\right)^2
\left(\frac{R_Q}{\rho_0}\right)^3
<
0.04258980409
(1-\varepsilon_Z)(1-\varepsilon_Q)
\Longrightarrow
\text{S-closed endpoint}.
}
\]

If a common non-T/non-H core radius `R_C` controls both quantile radii,

\[
R_Z\le R_C,
\qquad
R_Q\le R_C,
\]

then every surviving endpoint must satisfy

\[
\boxed{
\frac{R_C}{\rho_0}
\ge
\left[
0.04258980409
(1-\varepsilon_Z)(1-\varepsilon_Q)
\right]^{1/5}.
}
\]

At zero tail fractions this gives the explicit analytic-scale floor

\[
\boxed{
R_C\ge0.5319381377\,\rho_0.
}
\]

Thus the smooth survivor cannot live in a sub-half-analytic-radius common core.

## 6. Significance

The endpoint S-closed region is now more than an order of magnitude larger in radius than the earlier very-small-core leakage gate. This does not close all smooth profiles, but it pushes every non-H/T survivor to a common core radius comparable to the analytic strip itself.

Status: **THE FULL POSITIVE QUADRATIC RECORD ENVELOPE IMPROVES THE ENDPOINT FREQUENCY CEILING AND FORCES A ZERO-TAIL COMMON-CORE SURVIVOR TO HAVE RADIUS AT LEAST `0.531938 rho_0` ON THE `M_0=2` TRACK.**