# Smooth Multistage Tightrope Closure — 2026-08-20

Status: **SMOOTH-ONLY MULTISTAGE NECESSARY CONDITION / NO ANCIENT LIMIT USED / GLOBAL REGULARITY NOT PROVED.**

This note sums the exact finite-stage frequency ledger over many actual first-hitting stages. The endpoint frequency corridor removes the need to classify every individual frequency-collapse event.

## 1. Exact finite-stage ledger

For each geometric first-hitting stage `I_j`, with record level changing by the fixed factor `q>1`, the smooth tightrope identity is

\[
\frac12\Delta_j\log\lambda
+\frac12\log q
+\nu\int_{I_j}\mathcal G\,ds
=
\int_{I_j}\mathcal X\,ds,
\]

where

\[
\lambda=P/E,
\qquad
\mathcal G=H/P-P/E\ge0,
\qquad
\mathcal X=N/P-A/E.
\]

On the positive-middle lane, `A>=0`, so

\[
\mathcal X\le N/P.
\]

## 2. Sum N actual smooth stages

Summing from `j=0` to `N-1`,

\[
\frac12\log\frac{\lambda_N}{\lambda_0}
+\frac N2\log q
+\nu\int_{\cup I_j}\mathcal G\,ds
=
\int_{\cup I_j}\mathcal X\,ds.
\]

Assume the first-hitting endpoint profiles remain in the smooth quantile frequency corridor

\[
0<\lambda_-\le\lambda_j\le\lambda_+<\infty.
\]

Then

\[
\frac12\log\frac{\lambda_N}{\lambda_0}
\ge
-\frac12\log\frac{\lambda_+}{\lambda_-}.
\]

Hence

\[
\boxed{
\int\mathcal X\,ds
\ge
\frac N2\log q
-\frac12\log\frac{\lambda_+}{\lambda_-}
+\nu\int\mathcal G\,ds.
}
\]

No compact or ancient object appears.

## 3. Uniform production ceiling from analyticity and derivative tightness

The instantaneous smooth Hardy--Biot--Savart ceiling is

\[
\mathcal X\le\frac NP
\le
C_PK_2^{1/5}Q^{2/5},
\qquad
C_P=\frac{15}{4}\pi^{-2/5}.
\]

Assume derivative mass is uniformly quantile-tight on the stage family:

\[
\int_{B_{R_Q}}|\nabla\Omega|^2
\ge
(1-\varepsilon_Q)Q,
\]

and `|grad Omega|<=K_1`. Then

\[
Q\le
\frac{4\pi}{3(1-\varepsilon_Q)}K_1^2R_Q^3.
\]

Therefore

\[
\boxed{
\mathcal X\le X_+
:=
C_P
\left[\frac{4\pi}{3(1-\varepsilon_Q)}\right]^{2/5}
K_2^{1/5}K_1^{4/5}R_Q^{6/5}.
}
\]

On the Clay-data analytic strip,

\[
K_1\le M_0/\rho_0,
\qquad
K_2\le2M_0/\rho_0^2,
\]

so

\[
\boxed{
X_+
\le
C_X M_0
(1-\varepsilon_Q)^{-2/5}
\left(\frac{R_Q}{\rho_0}\right)^{6/5},
}
\]

with

\[
\boxed{
C_X
=C_P2^{1/5}(4\pi/3)^{2/5}
\approx4.8329551123.
}
\]

## 4. Use the smooth bounded-core upper stage length

On the existing non-H/T bounded-radius lane, the moving-core variance argument supplies a finite upper normalized stage length

\[
|I_j|\le L_+.
\]

Let

\[
S_N=\sum_{j=0}^{N-1}|I_j|.
\]

Then

\[
S_N\le NL_+.
\]

Since `G>=0`, the summed ledger and `X<=X_+` give

\[
X_+S_N
\ge
\frac N2\log q
-\frac12\log\frac{\lambda_+}{\lambda_-}.
\]

Therefore

\[
X_+L_+
\ge
\frac12\log q
-\frac1{2N}\log\frac{\lambda_+}{\lambda_-}.
\]

Letting the number of actual smooth stages increase gives the necessary condition

\[
\boxed{
X_+L_+\ge\frac12\log q.
}
\]

This is a smooth-sequence statement. It is not an ancient-limit statement.

## 5. S-level multistage closure criterion

Consequently, an infinite positive-middle non-H/T first-hitting lane is impossible if

\[
\boxed{
X_+L_+<\frac12\log q.
}
\]

Using the analytic quantile bound,

\[
\boxed{
C_XM_0
(1-\varepsilon_Q)^{-2/5}
\left(\frac{R_Q}{\rho_0}\right)^{6/5}
L_+
<
\frac12\log q
}
\]

is an explicit S-level closure condition.

For `q=2` and `M_0=2`, this becomes

\[
\boxed{
L_+
\left(\frac{R_Q}{\rho_0}\right)^{6/5}
<
0.03585524614
(1-\varepsilon_Q)^{2/5}.
}
\]

## 6. Optional positive viscous improvement

If one also has a uniform quantile lower bound

\[
\mathcal G\ge G_->0
\]

through the stage family, then the same argument yields

\[
\boxed{
(X_+-\nu G_-)L_+
\ge
\frac12\log q.
}
\]

Hence the stronger closure criterion is

\[
\boxed{
(X_+-\nu G_-)L_+
<
\frac12\log q.
}
\]

A moment-free candidate lower bound follows by applying sharp Sobolev to `grad Omega`: if

\[
\int_{B_{R_Q}}|\nabla\Omega|^2
\ge(1-\varepsilon_Q)Q,
\]

then

\[
\frac HP
=\frac{\|\nabla^2\Omega\|_2^2}{\|\nabla\Omega\|_2^2}
\ge
c_S\frac{1-\varepsilon_Q}{R_Q^2}.
\]

Thus

\[
\mathcal G
\ge
\left[
 c_S\frac{1-\varepsilon_Q}{R_Q^2}-\lambda
\right]_+.
\]

A uniform `G_-` requires a corresponding uniform upper bound on `lambda` throughout the stages; endpoint bounds alone are not enough, so no hidden interior-frequency assumption is made here.

## 7. What remains

The remaining quantitative bottleneck on this smooth-only lane is no longer an ancient compactness constant. It is the finite-stage product

\[
\boxed{
L_+
\left(\frac{R_Q}{\rho_0}\right)^{6/5}
}
\]

plus the derivative-tail fraction.

If the existing moving-core variance upper-time estimate is sharpened from `L_+~R^2/nu` to a fully explicit constant in the same quantile radius, the multistage criterion becomes a direct numerical test.

Status: **AN INFINITE SMOOTH POSITIVE-MIDDLE NON-H/T LANE MUST PAY AT LEAST `(1/2) log q` OF CROSS-ORDER PRODUCTION PER STAGE IN THE LONG RUN. THE RESULTING S-LEVEL CLOSURE CONDITION DEPENDS ONLY ON THE SMOOTH ANALYTIC DERIVATIVE RADIUS, DERIVATIVE QUANTILE RADIUS, TAIL FRACTION, AND THE FINITE BOUNDED-CORE STAGE-LENGTH CEILING.**