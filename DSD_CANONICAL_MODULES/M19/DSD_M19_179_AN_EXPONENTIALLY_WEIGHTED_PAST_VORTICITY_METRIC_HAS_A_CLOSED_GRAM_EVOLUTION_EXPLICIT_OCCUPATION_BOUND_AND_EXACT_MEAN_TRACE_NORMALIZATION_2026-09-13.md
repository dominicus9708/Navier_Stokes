# DSD M19-179 — An exponentially weighted past-vorticity metric has a closed Gram evolution, explicit occupation bound, and exact mean trace normalization

**Date:** 2026-09-13  
**Status:** ACTIVE M19 CALCULATION / EXPLICIT DYNAMIC HARD-FIBER METRIC / NONCONSTRUCTIVE OCCUPATION CONSTANT REPLACED / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-178 showed that a sharp sliding-window metric gives an explicit anti-spike occupation estimate but introduces endpoint/connection terms.

The present module replaces the sharp window by an exponentially weighted past memory.

This produces a closed ODE for the Gram metric and simultaneously yields:

1. an explicit instantaneous occupation ceiling;
2. an exact long-time normalization of the collective hard dimension;
3. an explicit, bounded connection correction in the hard trace identity.

This removes the main nonconstructive constant `kappa_occ` from M19-176--177.

## 2. Transported reference frame

Fix a complete compact recurrent hard orbit and choose a transported real hard frame

\[
e_1(s),\ldots,e_N(s),
\qquad
 e_j(s)=\Phi_s e_j(0).
\]

Let

\[
\eta_j(s)=\nabla\times e_j(s).
\]

In this transported frame define the instantaneous vorticity Gram matrix

\[
\boxed{
H(s)_{ij}
:=
\langle\eta_i(s),\eta_j(s)\rangle_{L^2}.
}
\]

Likewise let `D(s)` and `C(s)` denote the polarized gradient-vorticity and compensation matrices, so the exact matrix energy identity is

\[
\boxed{
\frac12H'(s)
+
\nu D(s)
+
\frac14H(s)
=
C(s).
}
\]

## 3. Exponential past-memory Gram metric

For

\[
\lambda>0,
\]

define

\[
\boxed{
G_\lambda(s)
:=
\lambda
\int_0^\infty
 e^{-\lambda r}
H(s-r)\,dr.
}
\]

The complete hard cocycle provides the past history needed to define this integral.
Compactness gives boundedness of `H`, so the integral converges.

Vorticity observability implies positive definiteness on the retained nondegenerate hard stratum.

## 4. Exact Gram evolution

Differentiate under the integral:

\[
G_\lambda'(s)
=
\lambda
\int_0^\infty
 e^{-\lambda r}
H'(s-r)dr.
\]

Set

\[
f(r)=H(s-r).
\]

Then

\[
f'(r)=-H'(s-r).
\]

Integration by parts gives

\[
\int_0^\infty
 e^{-\lambda r}H'(s-r)dr
=
H(s)
-
\lambda
\int_0^\infty e^{-\lambda r}H(s-r)dr.
\]

Therefore

\[
\boxed{
G_\lambda'
=
\lambda(H-G_\lambda).
}
\]

This is the key closure identity.

## 5. One-sided hard-vorticity growth in matrix form

M19-178 proved for every transported hard vector `v`

\[
Z_v'(s)
\le
L_+Z_v(s),
\]

with

\[
L_+
=
2(B_+-1/4)_+.
\]

Because the inequality holds for every coefficient vector in the transported hard frame, it is equivalent to the Loewner-form estimate

\[
\boxed{
H(s-r)
\ge
 e^{-L_+r}H(s),
\qquad r\ge0.
}
\]

Insert this into the exponential metric:

\[
\begin{aligned}
G_\lambda(s)
&\ge
\lambda
\int_0^\infty
 e^{-(\lambda+L_+)r}dr
\,H(s)\\
&=
\frac{\lambda}{\lambda+L_+}H(s).
\end{aligned}
\]

Hence

\[
\boxed{
H(s)
\le
\left(1+\frac{L_+}{\lambda}\right)
G_\lambda(s).
}
\]

Define

\[
\boxed{
\kappa_\lambda
:=
1+\frac{L_+}{\lambda}.
}
\]

This is an explicit instantaneous occupation ceiling.

## 6. Normalized instantaneous Gram matrix

Define

\[
\boxed{
X_\lambda(s)
:=
G_\lambda(s)^{-1/2}
H(s)
G_\lambda(s)^{-1/2}.
}
\]

Then

\[
X_\lambda(s)\ge0
\]

and the previous Loewner estimate gives

\[
\boxed{
0\le X_\lambda(s)
\le
\kappa_\lambda I.
}
\]

Thus every instantaneous vorticity occupation eigenvalue is explicitly bounded by `kappa_lambda`.

## 7. Exact mean trace normalization from log det

From

\[
G_\lambda'
=
\lambda(H-G_\lambda),
\]

we obtain

\[
\begin{aligned}
\frac d{ds}\log\det G_\lambda
&=
\operatorname{tr}(G_\lambda^{-1}G_\lambda')\\
&=
\lambda
\operatorname{tr}
\left(
G_\lambda^{-1}H-I
\right)\\
&=
\lambda
\left(
\operatorname{tr}X_\lambda-N
\right).
\end{aligned}
\]

Hence

\[
\boxed{
\frac d{ds}\log\det G_\lambda
=
\lambda
(\operatorname{tr}X_\lambda-N).
}
\]

On a compact nondegenerate hard stratum, `G_lambda` and `G_lambda^{-1}` are bounded, so `log det G_lambda` is bounded.

Therefore every Cesaro long-time average satisfies

\[
\boxed{
\left\langle
\operatorname{tr}X_\lambda
\right\rangle
=N.
}
\]

This is an **exact dimension normalization**, not merely a lower bound.

## 8. Time-dependent metric connection term

Let

\[
A_\lambda
:=
G_\lambda^{-1}.
\]

Define the dynamically normalized collective quantities

\[
Z_\lambda
:=
\operatorname{tr}(A_\lambda H)
=
\operatorname{tr}X_\lambda,
\]

\[
P_\lambda
:=
\operatorname{tr}(A_\lambda D),
\]

\[
T_\lambda
:=
\operatorname{tr}(A_\lambda C).
\]

Trace the matrix energy identity against `A_lambda`:

\[
\frac12\operatorname{tr}(A_\lambda H')
+
\nu P_\lambda
+
\frac14Z_\lambda
=
T_\lambda.
\]

Since

\[
Z_\lambda'
=
\operatorname{tr}(A_\lambda'H)
+
\operatorname{tr}(A_\lambda H'),
\]

we get

\[
\boxed{
\frac12Z_\lambda'
+
\nu P_\lambda
+
\frac14Z_\lambda
=
T_\lambda
+
R_\lambda,
}
\]

where

\[
R_\lambda
:=
\frac12\operatorname{tr}(A_\lambda'H).
\]

## 9. Exact connection formula

Differentiate the inverse metric:

\[
A_\lambda'
=
-A_\lambda G_\lambda'A_\lambda
=
-\lambda
A_\lambda(H-G_\lambda)A_\lambda.
\]

Therefore

\[
\begin{aligned}
R_\lambda
&=
-\frac\lambda2
\operatorname{tr}
\left[
A_\lambda(H-G_\lambda)A_\lambda H
\right]\\
&=
-\frac\lambda2
\operatorname{tr}
\left[
(X_\lambda-I)X_\lambda
\right].
\end{aligned}
\]

Thus

\[
\boxed{
R_\lambda
=
\frac\lambda2
\operatorname{tr}
\left(
X_\lambda-X_\lambda^2
\right).
}
\]

## 10. Universal upper bound on the connection cost

For every scalar `x>=0`,

\[
x-x^2
\le
\frac14.
\]

Hence

\[
\boxed{
R_\lambda(s)
\le
\frac{\lambda N}{8}.
}
\]

Large occupation eigenvalues `x>1` make `x-x^2` negative and therefore **help** the energy inequality rather than hurt it.

The worst positive connection cost occurs at `x=1/2`.

## 11. Long-time normalized trace identity

Average

\[
\frac12Z_\lambda'
+
\nu P_\lambda
+
\frac14Z_\lambda
=
T_\lambda+R_\lambda.
\]

On the compact hard corridor the derivative term vanishes in the Cesaro mean, and Section 7 gives

\[
\langle Z_\lambda\rangle=N.
\]

Therefore

\[
\boxed{
\nu\langle P_\lambda\rangle
+
\frac N4
=
\langle T_\lambda\rangle
+
\langle R_\lambda\rangle.
}
\]

Using the universal connection ceiling,

\[
\boxed{
\nu\langle P_\lambda\rangle
+
\left(
\frac14-rac\lambda8
\right)N
\le
\langle T_\lambda\rangle.
}
\]

Thus the time-dependent normalization costs only an explicit linear amount `lambda/8` per hard dimension.

## 12. Tradeoff

The memory parameter `lambda` controls two competing effects:

### Occupation distortion

\[
\boxed{
\kappa_\lambda
=1+\frac{L_+}{\lambda}.
}
\]

Larger `lambda` makes the instantaneous occupation closer to one.

### Connection cost

\[
\boxed{
\text{cost per dimension}
\le
\frac\lambda8.
}
\]

Smaller `lambda` makes the connection correction smaller.

Therefore the former nonconstructive constant `kappa_occ` has been replaced by an explicit one-parameter optimization problem in `lambda`.

## 13. Main gain

The earlier aperiodic dimension criterion depended on a qualitative compactness constant

\[
\kappa_{occ}<\infty.
\]

The present construction replaces it by

\[
\boxed{
\kappa_\lambda
=1+\frac{L_+}{\lambda}
}
\]

plus the explicit connection penalty

\[
\boxed{
\lambda/8.
}
\]

Both depend only on the already controlled one-sided growth constant `L_+` and the freely chosen memory parameter `lambda`.

Thus the main nonconstructive hard-frame distortion in M19-176--177 is removed.

## 14. Audit verdict

### Proved

1. Closed exponential-memory Gram evolution.
2. Explicit Loewner occupation bound.
3. Exact long-time normalization `average tr X_lambda=N`.
4. Exact connection formula and universal upper cost `lambda N/8`.
5. Reduction of the occupation problem to an explicit one-parameter tradeoff.

### Not proved

1. That the optimized trace constants cross the decisive `N=2` threshold.
2. `N<=1`.
3. Global regularity.

## 15. Next target

M19-180 should redo the collective Lieb--Thirring/HLS trace estimates in the `G_lambda`-normalized density-matrix frame.

The occupation ceiling `kappa_lambda` will enter explicitly. The target inequality should have the form

\[
\boxed{
\left(
\frac14-rac\lambda8
\right)N
\le
A(\lambda)N^{3/5}
+
B_a(\lambda)N^{d(a)}
}
\]

with

\[
A(\lambda),B_a(\lambda)
\]

explicit functions of

\[
\kappa_\lambda=1+L_+/\lambda.
\]

Then `N<=1` becomes a two-parameter optimization over `lambda` and `a` with no hidden occupation constant.
