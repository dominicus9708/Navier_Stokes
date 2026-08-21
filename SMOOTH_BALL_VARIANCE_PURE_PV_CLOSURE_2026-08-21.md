# Smooth Ball-Variance Pure-P_V Closure — 2026-08-21

Status: **FIRST DIRECT S-CLOSURE OF AN EXPLICIT PURE SMOOTH P_V SUBCORRIDOR / GLOBAL REGULARITY NOT PROVED.**

This note audits the last numerical input in the anti-ribbon closure. It also corrects one scope point: the Payne–Weinberger constant `4/pi^2` is not inserted into an arbitrary weighted-cutoff Poincare inequality. Instead, on the smooth rapidly-decaying track, the moving-cutoff variance identity is passed to the sharp Euclidean-ball limit. The resulting ball mean admits the Payne–Weinberger bound legitimately.

## 1. Smooth moving-ball variance identity

Work on one finite smooth dynamic first-hitting stage

\[
M_j\to qM_j,\qquad q>1.
\]

For a Euclidean ball `B_R` in the normalized coordinates, let

\[
\bar U_R(s)=|B_R|^{-1}\int_{B_R}U(y,s)\,dy,
\]

\[
V_R(s)=\int_{B_R}|U-\bar U_R|^2dy,
\qquad
D_R(s)=\int_{B_R}|\nabla U|^2dy.
\]

Because the solution is smooth, the already-derived moving-cutoff variance identity may be approximated by smooth radial cutoffs converging to `1_{B_R}`. All cutoff-gradient terms converge to ordinary boundary/material/pressure/scale-drift fluxes. Thus the exact typed ball identity is

\[
\boxed{
\frac12V_R'+\nu D_R
=\frac a2V_R+\mathcal F_R^{\partial B}.
}
\]

Here `F_R^{partial B}` is the total boundary flux. No new forcing term is introduced.

## 2. Legitimate ball Poincare constant

The ball is convex with diameter `2R`. Payne–Weinberger gives

\[
\boxed{
V_R
\le
\frac{4R^2}{\pi^2}D_R.
}
\]

This is the proper place where `4/pi^2` is used.

## 3. Pure-corridor thresholds

Define the following dimensionless stage descriptors:

\[
\Lambda_V=\frac{V_+}{V_-},
\qquad
\delta_V=\frac{\kappa_V}{V_-},
\qquad
f_V=\frac{F_0}{V_-},
\]

where

\[
0<V_-\le V_R(s)\le V_+,
\qquad
|V_R(s_1)-V_R(s_0)|\le\kappa_V,
\]

and the integrated boundary flux obeys

\[
\left|\int_I\mathcal F_R^{\partial B}ds\right|
\le
\eta\nu\int_I D_Rds+F_0,
\qquad 0\le\eta<1.
\]

The **pure low-turnover corridor** is defined by

\[
\boxed{
\Lambda_V\le2,
\qquad
\delta_V\le1,
\qquad
f_V\le1,
\qquad
\eta\le\frac12.
}
\]

This is a branch definition, not a hidden assumption. Failure of any one inequality is routed to a typed complement:

- `Lambda_V>2`: order-one variance excursion / shape turnover;
- `delta_V>1`: order-one endpoint variance reshaping;
- `f_V>1`: order-one net boundary/material/pressure flux;
- `eta>1/2`: boundary flux absorbs more than half of the viscous interior cost.

All four complements therefore leave the intended pure P_V lane and enter the existing T/residual bookkeeping.

## 4. Exact stage-length ceiling on the pure corridor

Integrating the ball variance identity and using the ball Poincare inequality gives

\[
L_j
\le
\Pi_B\frac{R_V^2}{\nu},
\]

with

\[
\boxed{
\Pi_B
=\frac{4/\pi^2}{1-\eta}
\left[
\frac14(\log q)\Lambda_V
+f_V
+\frac12\delta_V
\right].
}
\]

For

\[
q=2,
\qquad
\Lambda_V\le2,
\qquad
\delta_V\le1,
\qquad
f_V\le1,
\qquad
\eta\le\frac12,
\]

we obtain

\[
\boxed{
\Pi_B
\le
\frac{8}{\pi^2}
\left(
\frac12\log2+\frac32
\right)
\approx1.4967761748.
}
\]

## 5. Remove the unknown analyticity normalization from the comparison

The standard analyticity theorem supplies a constant `c(2)>0`. Replace it, if necessary, by

\[
\boxed{c_*(2)=\max\{c(2),1\}.}
\]

Using the larger constant only weakens the guaranteed analyticity radius and therefore remains valid. Hence

\[
c_*(2)\ge1
\]

and

\[
\boxed{
\frac{\Pi_B}{c_*(2)^2}
\le1.4967761748.
}
\]

No numerical value of the external analyticity constant is needed for this subcorridor.

## 6. Anti-ribbon swap lower time

For the zero-tail common-core benchmark, the explicit projective-speed estimate is

\[
C_{V,+}(r)
\le
0.3535533906
+2.5141113904\,r^{15/4},
\qquad
r=R_C/\rho_0.
\]

The transverse anti-ribbon swap gate requires

\[
\boxed{
L_j
\ge
L_{swap}(r)
:=
\frac{\pi}{1+2C_{V,+}(r)}.
}
\]

For `M0=2`, `sigma=1/2`, the ball-variance upper time is

\[
L_j
\le
\frac12\frac{\Pi_B}{c_*(2)^2}r^2.
\]

Therefore the pure P_V anti-ribbon stage is impossible whenever

\[
\boxed{
\frac{\Pi_B}{c_*(2)^2}
<
T_{swap}(r)
:=
\frac{2\pi}{r^2[1+2C_{V,+}(r)]}.
}
\]

Using the proven pure-corridor ceiling

\[
\Pi_B/c_*(2)^2\le1.4967761748,
\]

the equality `T_swap(r)=1.4967761748` occurs at

\[
\boxed{r_{swap}^{(0)}\approx0.90344446.}
\]

Thus, in the zero-tail common-core benchmark,

\[
\boxed{
0.53193814\le r\le0.90344446
\quad\Longrightarrow\quad
\text{pure positive-middle anti-ribbon P_V stage is S-closed}.
}
\]

The lower endpoint is the previously derived smooth frequency-corridor floor. Radii below it are already S-closed by the endpoint frequency contradiction.

Consequently the entire zero-tail pure corridor is S-closed for

\[
\boxed{r<0.90344446.}
\]

## 7. Robust quarter-tail version

If

\[
\varepsilon_Z\le\frac14,
\qquad
\varepsilon_Q\le\frac14,
\]

then the nonlinear part of the projective-speed ceiling is multiplied by at most

\[
(1-\varepsilon_Z)^{-1/2}
(1-\varepsilon_Q)^{-3/4}
\le
(3/4)^{-5/4}.
\]

Hence

\[
C_{V,+}(r)
\le
0.3535533906
+2.5141113904(3/4)^{-5/4}r^{15/4}.
\]

The corresponding equality with the same pure-corridor ball-variance ceiling occurs at

\[
\boxed{r_{swap}^{(1/4)}\approx0.85601829.}
\]

The frequency-corridor floor under quarter tails is

\[
\boxed{r_{freq}^{(1/4)}\approx0.47411712.}
\]

Therefore

\[
\boxed{
0.47411712\lesssim r\lesssim0.85601829
\quad\Longrightarrow\quad
\text{quarter-tail pure positive-middle anti-ribbon P_V stage is S-closed}.
}
\]

If either tail exceeds `1/4`, that is explicitly routed to vorticity/derivative spatial non-tightness rather than retained in this pure corridor.

## 8. What has actually closed

This is the first branch in the current smooth-only mainline that can be labeled `S-closed` after all constants in the comparison have been assigned legitimate sources.

What is closed is **not** all of P_V and certainly not global regularity. The closed subcorridor is:

1. smooth rapidly-decaying first-hitting stage;
2. positive-middle thick coherent core;
3. vorticity and derivative tails at most the stated threshold;
4. moving-ball variance remains within the pure persistence thresholds;
5. anti-ribbon rescue must be supplied by the pure projective lane rather than large T/H/residual action;
6. common analytic-scale radius below the explicit swap threshold.

Any survivor must now leave this subcorridor by at least one typed route:

\[
\boxed{
R_C>r_{swap}\rho_0
\quad\lor\quad
\varepsilon_Z>1/4
\quad\lor\quad
\varepsilon_Q>1/4
\quad\lor\quad
T_{variance/boundary}
\quad\lor\quad
H/residual/pressure\text{ action}.
}
\]

Status: **THE PURE LOW-TURNOVER POSITIVE-MIDDLE P_V SUBCORRIDOR IS DIRECTLY S-CLOSED THROUGH A LEGITIMATE MOVING-BALL PAYNE–WEINBERGER ESTIMATE. WITH QUARTER-TAIL ROBUSTNESS, ANY PURE SURVIVOR MUST HAVE COMMON CORE RADIUS ABOVE ABOUT `0.856 rho0` OR LEAVE THE PURE LANE THROUGH AN ALREADY TYPED T/H/RESIDUAL CHANNEL.**