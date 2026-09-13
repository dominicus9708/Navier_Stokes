# M19-180 — Exponential-memory connection has nonpositive mean and removes the lambda/8 loss

**Date:** 2026-09-13  
**Status:** ACTIVE CALCULATION / POSITIVE IMPROVEMENT  
**Scope:** recurrent finite hard bundle inside the already certified smooth passive-spectator corridor

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-179

Let `H(s)` denote the instantaneous pulled-back vorticity observation Gram form on an `N`-dimensional recurrent hard fiber. For `lambda>0`, define the exponential past-memory metric

\[
G_\lambda(s)
:=\lambda\int_0^\infty e^{-\lambda r}H(s-r)\,dr.
\]

Then

\[
\boxed{G_\lambda'=\lambda(H-G_\lambda).}
\]

Define

\[
X_\lambda
:=G_\lambda^{-1/2}HG_\lambda^{-1/2}\ge0.
\]

M19-179 also gives the one-sided occupation comparison

\[
\boxed{
H\le\kappa_\lambda G_\lambda,
\qquad
\kappa_\lambda:=1+\frac{L_+}{\lambda}.
}
\]

The moving-metric connection contribution to the normalized hard trace is

\[
\boxed{
R_\lambda(s)
=\frac{\lambda}{2}
\operatorname{tr}(X_\lambda-X_\lambda^2).
}
\]

M19-179 used only the pointwise scalar bound `x-x^2<=1/4`, producing the provisional loss `lambda N/8`.

## 2. Exact determinant identity

Since

\[
\frac d{ds}\log\det G_\lambda
=\operatorname{tr}(G_\lambda^{-1}G_\lambda'),
\]

we obtain

\[
\frac d{ds}\log\det G_\lambda
=\lambda\left(\operatorname{tr}X_\lambda-N\right).
\]

On a retained compact recurrent component, `G_lambda` remains positive definite and bounded above and below on the finite hard bundle. Hence the long-time boundary contribution vanishes and

\[
\boxed{
\left\langle\operatorname{tr}X_\lambda\right\rangle=N.
}
\]

## 3. The connection term is favorable on average

For every positive semidefinite `N x N` matrix,

\[
\operatorname{tr}(X^2)
\ge\frac1N(\operatorname{tr}X)^2.
\]

Therefore Jensen gives

\[
\left\langle\operatorname{tr}X_\lambda^2\right\rangle
\ge
\frac1N
\left\langle\operatorname{tr}X_\lambda\right\rangle^2
=N.
\]

Consequently

\[
\boxed{
\langle R_\lambda\rangle
=\frac{\lambda}{2}
\left(
N-\left\langle\operatorname{tr}X_\lambda^2\right\rangle
\right)
\le0.
}
\]

Thus the pointwise estimate

\[
R_\lambda\le\frac{\lambda N}{8}
\]

is too wasteful for the recurrent averaged problem.

## 4. Improved normalized hard-trace inequality

The M19-179 moving-metric trace balance has the schematic exact form

\[
\frac12\frac d{ds}Z_\lambda
+\nu P_\lambda
+\frac14 Z_\lambda
=T_\lambda+R_\lambda,
\]

with

\[
\langle Z_\lambda\rangle=N.
\]

Averaging and using `\langle R_lambda\rangle<=0` yields the stronger inequality

\[
\boxed{
\nu\langle P_\lambda\rangle
+\frac14N
\le
\langle T_\lambda\rangle.
}
\]

The provisional M19-179 damping coefficient

\[
\frac14-\frac\lambda8
\]

is therefore replaced by the full bare quarter-gap

\[
\boxed{\frac14.}
\]

## 5. Occupation distortion can now be driven to one

The only remaining explicit memory distortion is

\[
\kappa_\lambda
=1+\frac{L_+}{\lambda}.
\]

Since there is no longer a positive averaged connection penalty growing with `lambda`, one may take a large-`lambda` limit in the sufficient dimension estimate:

\[
\boxed{
\kappa_\lambda\downarrow1
\qquad(\lambda\to\infty).
}
\]

This does **not** mean the time-dependent metric becomes pointwise constant. It means only that the occupation/Bessel constant entering the collective inequalities can be made arbitrarily close to one while the averaged connection term remains nonpositive.

## 6. Equality case

Equality

\[
\langle R_\lambda\rangle=0
\]

requires equality in both the matrix Cauchy inequality and Jensen at the relevant averaged level. In particular, the favorable correction is strict whenever the normalized instantaneous observation matrix has genuine temporal or spectral anisotropy.

Thus occupation fluctuation helps rather than hurts the averaged hard-dimension estimate.

## 7. New firewall

\[
\boxed{
\text{pointwise moving-metric connection cost}
\neq
\text{averaged recurrent connection cost}.
}
\]

The former can be positive at an instant; the latter is nonpositive after the exact determinant normalization.

## 8. Consequence for the next module

The M19-180 result removes `lambda` as an adverse optimization variable. The next calculation should redo the Lieb--Thirring/HLS trace estimate in the `G_lambda` frame, retain the explicit generalized Bessel factor `kappa_lambda`, and then pass `lambda->infinity`.

The target becomes

\[
\boxed{
\frac14N+\nu\bar P
\le
C_{str}M_{5/2}\bar P^{3/5}
+C_aM_aN^{p(a)}\bar P^{q(a)},
}
\]

up to the generalized-frame constants, where

\[
q(a)=\frac{3-a}{2a},
\qquad
p(a)=\frac{11}{6}-\frac{5}{2a},
\qquad
p(a)+q(a)=\frac43-\frac1a<1.
\]

---

\[
\boxed{\text{M19-180: THE MEMORY-CONNECTION LOSS IS REMOVED IN LONG-TIME MEAN.}}
\]
