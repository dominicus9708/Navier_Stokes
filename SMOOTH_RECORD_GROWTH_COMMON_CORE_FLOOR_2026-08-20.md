# Smooth Record-Growth Common-Core Floor — 2026-08-20

Status: **SMOOTH-ONLY RECORD-GROWTH RADIUS FLOOR / GLOBAL REGULARITY NOT PROVED.**

This note combines the finite moving-variance stage ceiling, the running-record growth identity, the instantaneous Hardy--Biot--Savart strain bound, and derivative quantile tightness. No ancient or compact-limit object is used.

## 1. Stage-average record growth

On one geometric first-hitting stage,

\[
\int_I b(s)ds=\log q,
\qquad
b=(\log M)_s\ge0.
\]

The moving-variance persistence bound is

\[
L_I\le\Pi_V\frac{R_V^2}{\nu}.
\]

Therefore there exists an actual record-growth time `s_*` with

\[
\boxed{
 b(s_*)
\ge
\frac{\log q}{L_I}
\ge
\frac{\nu\log q}{\Pi_VR_V^2}.
}
\]

At such a time the running maximum is active, so `||Omega||_infty=1` at a record point.

## 2. Record growth forces strain

At a record point the vorticity maximum equation gives

\[
b+\nu|\nabla\Omega|^2
\le
\xi^T\Sigma\xi
\le
\|\Sigma\|_\infty.
\]

Hence simply

\[
\boxed{b\le\|\Sigma\|_\infty.}
\]

The smooth Hardy--Biot--Savart second-order estimate is

\[
\|\Sigma\|_\infty
\le
C_BK_2^{1/5}Q^{2/5},
\]

with

\[
\boxed{
C_B=\frac{15\sqrt2}{8}\pi^{-2/5}
\approx1.6774760211.
}
\]

Thus

\[
Q
\ge
C_B^{-5/2}b^{5/2}K_2^{-1/2}.
\]

Since

\[
C_B^{-5/2}
=
\pi\left(\frac{8}{15\sqrt2}\right)^{5/2}
\approx0.2743842622,
\]

we have

\[
\boxed{
Q
\ge
\pi\left(\frac{8}{15\sqrt2}\right)^{5/2}
 b^{5/2}K_2^{-1/2}.
}
\]

## 3. Insert the stage-average lower bound for b

At the selected record time,

\[
\boxed{
Q
\ge
\pi\left(\frac{8}{15\sqrt2}\right)^{5/2}
\left(
\frac{\nu\log q}{\Pi_VR_V^2}
\right)^{5/2}
K_2^{-1/2}.
}
\]

Thus a long, spatially broad core lowers the necessary instantaneous palinstrophy, while a tight persistent core forces strong palinstrophy at some actual record time.

## 4. Derivative tightness gives the opposite Q bound

Assume on the same smooth non-H lane

\[
\int_{B_{R_Q}}|\nabla\Omega|^2
\ge
(1-\varepsilon_Q)Q
\]

and

\[
K_1=\|\nabla\Omega\|_\infty.
\]

Then

\[
\boxed{
Q\le
\frac{4\pi}{3(1-\varepsilon_Q)}K_1^2R_Q^3.
}
\]

## 5. Common-core radius floor

Suppose the intended non-T/non-H lane has one common radius `R_C` containing both the moving variance core and the derivative core:

\[
R_V\le R_C,
\qquad
R_Q\le R_C.
\]

Combining the lower and upper Q estimates gives

\[
\boxed{
R_C^8
\ge
C_{RG}
\frac{(1-\varepsilon_Q)(\nu\log q)^{5/2}}
{\Pi_V^{5/2}K_1^2K_2^{1/2}},
}
\]

where

\[
\boxed{
C_{RG}
=
\frac34
\left(\frac{8}{15\sqrt2}\right)^{5/2}
\approx0.06550542754.
}
\]

This is an S-level necessary radius condition on every persistent common-core stage.

## 6. Clay-data analytic form

Use

\[
K_1\le M_0/\rho_0,
\qquad
K_2\le2M_0/\rho_0^2,
\qquad
\rho_0=\frac{\sqrt{\sigma\nu}}{c(M_0)}.
\]

Then

\[
\frac1{K_1^2K_2^{1/2}}
\ge
\frac{\rho_0^3}{\sqrt2\,M_0^{5/2}}.
\]

Writing

\[
r_C=R_C/\rho_0,
\]

we obtain

\[
\boxed{
r_C^8
\ge
C_{RG}^{an}
\frac{(1-\varepsilon_Q)(\log q)^{5/2}c(M_0)^5}
{\Pi_V^{5/2}\sigma^{5/2}M_0^{5/2}},
}
\]

with

\[
\boxed{
C_{RG}^{an}=\frac{C_{RG}}{\sqrt2}
\approx0.04631861777.
}
\]

## 7. q=2, M0=2, sigma=1/2 specialization

For the convenient values

\[
q=2,
\qquad M_0=2,
\qquad\sigma=1/2,
\]

we get

\[
\boxed{
r_C^8
\ge
0.01852760330
\frac{(1-\varepsilon_Q)c(2)^5}
{\Pi_V^{5/2}}.
}
\]

Equivalently,

\[
\boxed{
\frac{R_C}{\rho_0}
\ge
0.6074036613
(1-\varepsilon_Q)^{1/8}
 c(2)^{5/8}
\Pi_V^{-5/16}.
}
\]

The analyticity constant may always be enlarged so that `c(2)>=1`; no smaller numerical value is assumed.

For example, a quantitatively low-turnover lane with `Pi_V<=3/2` and `epsilon_Q<=0.1` must satisfy the conservative floor

\[
\boxed{
R_C/\rho_0\gtrsim0.5281.
}
\]

The exact formula, rather than this example, is the proof object.

## 8. Relation to the endpoint frequency floor

The sharpened endpoint frequency corridor independently forces, at zero tail and `M_0=2`,

\[
R_C/\rho_0\ge0.5319381377.
\]

The record-growth floor and endpoint-frequency floor are therefore of the same analytic-scale order and arise from different mechanisms:

1. endpoint Sobolev/frequency compatibility;
2. finite-stage record growth versus moving-core diffusion.

A surviving smooth external-line core must satisfy both.

Status: **FINITE-STAGE RECORD GROWTH AND DERIVATIVE TIGHTNESS FORCE AN EXPLICIT EIGHTH-POWER LOWER BOUND ON THE COMMON CORE RADIUS. THE SURVIVOR IS NOW CONFINED TO A CORE OF AT LEAST ORDER ONE-HALF OF THE ANALYTIC STRIP SCALE ON THE CONVENIENT M0=2 NORMALIZATION, UP TO THE EXPLICIT TURNOVER FACTOR.**