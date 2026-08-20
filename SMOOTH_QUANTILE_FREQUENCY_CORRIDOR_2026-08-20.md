# Smooth Quantile Frequency Corridor — 2026-08-20

Status: **S-LEVEL FIRST-HITTING ENDPOINT NECESSARY CONDITION / DIRECT CLOSURE REGION IDENTIFIED / GLOBAL REGULARITY NOT PROVED.**

This note keeps the proof entirely on actual smooth first-hitting profiles. No ancient limit or compact-limit extremizer is used.

## 1. Normalized quantities

At a finite first-hitting endpoint let

\[
\|\Omega\|_\infty=1,
\qquad
Z=\|\Omega\|_2^2,
\qquad
Q=\|\nabla\Omega\|_2^2.
\]

Using the strain-vorticity isometries,

\[
E=\|\Sigma\|_2^2=\frac12 Z,
\qquad
P=\|\nabla\Sigma\|_2^2=\frac12 Q,
\]

so the normalized derivative frequency is exactly

\[
\boxed{\lambda=\frac PE=\frac QZ.}
\]

## 2. Lower frequency from vorticity mass tightness

Assume

\[
\int_{B_{R_Z}}|\Omega|^2
\ge
(1-\varepsilon_Z)Z,
\qquad 0\le\varepsilon_Z<1.
\]

The sharp three-dimensional Sobolev inequality is

\[
S_3\|f\|_6^2\le\|\nabla f\|_2^2,
\qquad
S_3=3\left(\frac\pi2\right)^{4/3}.
\]

Apply it to `|Omega|`, using Kato's inequality. Holder on the ball gives

\[
(1-\varepsilon_Z)Z
\le
|B_{R_Z}|^{2/3}\|\Omega\|_6^2
\le
\frac{|B_{R_Z}|^{2/3}}{S_3}Q.
\]

Therefore

\[
\boxed{
\lambda\ge
c_S\frac{1-\varepsilon_Z}{R_Z^2},
}
\]

where

\[
\boxed{
c_S=
\frac{3(\pi/2)^{4/3}}{(4\pi/3)^{2/3}}
\approx2.1080877498.
}
\]

This uses only a quantile radius. No second spatial moment is required.

## 3. Record-point lower bound for Z from second derivatives

Choose a record point `y_*` and unit vector

\[
\xi=\Omega(y_*),
\qquad |\xi|=1.
\]

Let

\[
K_2=\sup_y\sup_{|v|=1}|(v\cdot\nabla)^2\Omega(y)|.
\]

For the scalar function

\[
g(y)=\xi\cdot\Omega(y),
\]

we have

\[
g(y_*)=1
\]

and, because `y_*` maximizes `|Omega|`,

\[
\nabla g(y_*)=0.
\]

Taylor's theorem yields

\[
g(y_*+h)\ge1-\frac12K_2|h|^2.
\]

Hence on

\[
|h|\le K_2^{-1/2}
\]

we have `g>=1/2`, and therefore

\[
\boxed{
Z\ge\frac\pi3K_2^{-3/2}.
}
\]

## 4. Upper Q from derivative-mass tightness

Let

\[
K_1=\|\nabla\Omega\|_\infty
\]

and assume

\[
\int_{B_{R_Q}}|\nabla\Omega|^2
\ge
(1-\varepsilon_Q)Q.
\]

Then

\[
(1-\varepsilon_Q)Q
\le
K_1^2|B_{R_Q}|,
\]

so

\[
\boxed{
Q\le
\frac{4\pi}{3(1-\varepsilon_Q)}K_1^2R_Q^3.
}
\]

## 5. Upper frequency

Combining the previous two estimates,

\[
\lambda=\frac QZ
\le
\frac{4\pi K_1^2R_Q^3}{3(1-\varepsilon_Q)}
\frac{3K_2^{3/2}}\pi.
\]

Thus

\[
\boxed{
\lambda\le
4\frac{K_1^2K_2^{3/2}R_Q^3}{1-\varepsilon_Q}.
}
\]

## 6. Smooth frequency corridor

Every first-hitting endpoint on the quantile-tight smooth lane must therefore satisfy

\[
\boxed{
 c_S\frac{1-\varepsilon_Z}{R_Z^2}
\le
\lambda
\le
4\frac{K_1^2K_2^{3/2}R_Q^3}{1-\varepsilon_Q}.
}
\]

If the left endpoint exceeds the right endpoint, the profile is impossible at that actual smooth time. This is an S-level closure, not a limit closure.

## 7. Clay-data analytic substitution

On the smooth rapidly-decaying data track, use the normalized analytic constants

\[
K_1\le\frac{M_0}{\rho_0},
\qquad
K_2\le\frac{2M_0}{\rho_0^2}.
\]

Then

\[
\boxed{
\lambda_+
\le
8\sqrt2\,
\frac{M_0^{7/2}}{1-\varepsilon_Q}
\frac{R_Q^3}{\rho_0^5}.
}
\]

The corridor is empty whenever

\[
\boxed{
\left(\frac{R_Z}{\rho_0}\right)^2
\left(\frac{R_Q}{\rho_0}\right)^3
<
\frac{c_S}{8\sqrt2\,M_0^{7/2}}
(1-\varepsilon_Z)(1-\varepsilon_Q).
}
\]

For the convenient choice `M_0=2`, the numerical coefficient is

\[
\boxed{
\frac{c_S}{8\sqrt2\,2^{7/2}}
\approx0.01646943555.
}
\]

Thus, for `M_0=2`, every smooth first-hitting endpoint satisfying

\[
\left(\frac{R_Z}{\rho_0}\right)^2
\left(\frac{R_Q}{\rho_0}\right)^3
<
0.01646943555
(1-\varepsilon_Z)(1-\varepsilon_Q)
\]

is S-closed directly.

## 8. Interpretation

The endpoint cannot simultaneously be

- too concentrated in vorticity mass;
- too concentrated in derivative mass;
- and analytically smooth with the first-hitting derivative bounds.

The obstruction is elementary: vorticity tightness forces a minimum frequency by sharp Sobolev, while record-point analyticity plus derivative tightness forces a maximum frequency.

Status: **A NONEMPTY PARAMETER REGION OF THE SMOOTH FIRST-HITTING LANE IS NOW DIRECTLY S-CLOSED BY A QUANTILE FREQUENCY CORRIDOR. THE REMAINING LANE MUST HAVE SUFFICIENTLY LARGE VORTICITY RADIUS, DERIVATIVE RADIUS, OR TAIL FRACTION.**