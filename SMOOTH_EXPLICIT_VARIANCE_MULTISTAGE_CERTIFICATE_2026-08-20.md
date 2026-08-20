# Smooth Explicit Variance–Multistage Certificate — 2026-08-20

Status: **SMOOTH-ONLY S-CLOSURE CERTIFICATE WITH EXPLICIT PERSISTENCE FACTOR / GLOBAL REGULARITY NOT PROVED.**

This note inserts the already-derived moving local-variance stage-length bound into the smooth multistage tightrope criterion. No ancient limit is used.

## 1. Multistage production condition

From `SMOOTH_MULTISTAGE_TIGHTROPE_CLOSURE_2026-08-20.md`, an infinite positive-middle non-H/T lane requires

\[
\boxed{X_+L_+\ge\frac12\log q.}
\]

On the Clay-data analytic derivative-tight lane,

\[
\boxed{
X_+
\le
C_XM_0
(1-\varepsilon_Q)^{-2/5}
\left(\frac{R_Q}{\rho_0}\right)^{6/5},
}
\]

with

\[
C_X\approx4.8329551123.
\]

## 2. Exact existing moving-variance stage ceiling

The dynamic local-variance gate gives, on a persistent low-turnover moving core,

\[
L_I
\le
\frac{C_{var}R_V^2}
{(1-\eta)\nu V_-}
\left(
\frac14(\log q)V_+
+F_0
+\frac12\kappa_V
\right).
\]

Here

- `R_V` is the normalized moving variance radius;
- `V_- <= V_R(s) <= V_+` is the persistent local velocity-variance range;
- `eta<1` is the fraction of viscous dissipation allowed to be absorbed by shell/material flux;
- `F_0` is the residual integrated shell-flux allowance;
- `kappa_V` bounds the endpoint variance change;
- `C_var` is the fixed weighted Poincare constant associated with the chosen cutoff.

Define the dimensionless persistence factor

\[
\boxed{
\Pi_V
:=
\frac{C_{var}}
{(1-\eta)V_-}
\left(
\frac14(\log q)V_+
+F_0
+\frac12\kappa_V
\right).
}
\]

Then

\[
\boxed{L_+\le\Pi_V\frac{R_V^2}{\nu}.}
\]

Large `Pi_V` has a typed meaning: loss of variance persistence, large shell/material turnover, or large endpoint reshaping. Thus it is not a hidden free constant on the intended non-T lane.

## 3. Direct combined S-closure criterion

Combining the previous two estimates,

\[
X_+L_+
\le
C_XM_0\Pi_V
(1-\varepsilon_Q)^{-2/5}
\left(\frac{R_Q}{\rho_0}\right)^{6/5}
\frac{R_V^2}{\nu}.
\]

Therefore the infinite smooth positive-middle non-H/T lane is S-closed whenever

\[
\boxed{
C_XM_0\Pi_V
(1-\varepsilon_Q)^{-2/5}
\left(\frac{R_Q}{\rho_0}\right)^{6/5}
\frac{R_V^2}{\nu}
<
\frac12\log q.
}
\]

## 4. Dimensionless Clay-data form

For the Clay-data analytic restart,

\[
\rho_0=\frac{\sqrt{\sigma\nu}}{c(M_0)},
\]

so

\[
\frac{R_V^2}{\nu}
=
\frac{\sigma}{c(M_0)^2}
\left(\frac{R_V}{\rho_0}\right)^2.
\]

Set

\[
r_Q=R_Q/\rho_0,
\qquad
r_V=R_V/\rho_0.
\]

Then the closure condition becomes

\[
\boxed{
 r_Q^{6/5}r_V^2
<
\frac{c(M_0)^2\log q}
{2C_XM_0\sigma\Pi_V}
(1-\varepsilon_Q)^{2/5}.
}
\]

This is dimensionless and contains only actual smooth finite-stage persistence/tightness parameters.

## 5. Convenient q=2, M0=2, sigma=1/2 specialization

For

\[
q=2,
\qquad M_0=2,
\qquad \sigma=\frac12,
\]

we obtain

\[
\boxed{
 r_Q^{6/5}r_V^2
<
0.07171049228
\frac{c(2)^2}{\Pi_V}
(1-\varepsilon_Q)^{2/5}
\quad\Longrightarrow\quad
\text{S-closed}.
}
\]

No numerical value of `c(2)` or `Pi_V` is inserted without proof. The value above isolates exactly what must be quantified next.

## 6. Interpretation

The intended smooth lane cannot simultaneously keep

1. derivative mass in a small analytic-scale radius `r_Q`;
2. moving velocity variance in a small analytic-scale radius `r_V`;
3. low shell/material turnover (`Pi_V` controlled);
4. and infinitely many geometric first-hitting stages.

If the inequality is violated because `r_Q` grows, this is derivative spatial spreading (`H_remote`).

If it is violated because `r_V` grows or `Pi_V` grows, this is moving-core spreading, turnover, or loss of persistent local variance (`T`/typed deformation).

If none of these occur and the left side is below the threshold, the positive-middle lane is S-closed directly.

Status: **THE PREVIOUSLY SCHEMATIC STAGE-LENGTH CONSTANT HAS BEEN REPLACED BY THE EXISTING EXPLICIT MOVING-VARIANCE PERSISTENCE FACTOR. THE REMAINING SMOOTH TIGHTROPE IS NOW A DIMENSIONLESS INEQUALITY IN `r_Q`, `r_V`, `epsilon_Q`, AND `Pi_V`.**