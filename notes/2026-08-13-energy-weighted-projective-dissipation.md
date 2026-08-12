# Energy-weighted projective defect: nonlinear source versus purely dissipative viscosity

Date: 2026-08-13

Status: **DERIVED ENERGY-WEIGHTED PROJECTIVE INEQUALITY / OPEN NONLINEAR ANALYTIC-NORM CLOSURE**.

This note replaces the coefficientwise normalized dispersion `J_k` by the energy-weighted projective defect

\[
\boxed{
D_k=E_kJ_k.
}
\]

This change removes the sign-indefinite viscous directional-mixing branch from the evolution equation: viscosity becomes a purely dissipative term involving both the next-order projective defect and the neighboring covariance mismatch.

No global regularity conclusion is claimed.

## 1. Starting identities

For derivative order `k`, recall

\[
\dot E_k
=2Q_k-2\nu E_{k+1},
\]

and

\[
\frac14\dot J_k
=\mathcal M_{N,k}
+\nu r_k\mathcal A_k,
\qquad
r_k=E_{k+1}/E_k,
\]

with

\[
\mathcal A_k
=\frac12
\left[
J_k-J_{k+1}-\Delta_k^2
\right],
\qquad
\Delta_k=\|C_{k+1}-C_k\|_F.
\]

## 2. Exact energy-weighted identity

Differentiate

\[
D_k=E_kJ_k.
\]

Then

\[
\begin{aligned}
\dot D_k
&=(2Q_k-2\nu E_{k+1})J_k
+4E_k\mathcal M_{N,k}
+4\nu E_{k+1}\mathcal A_k.
\end{aligned}
\]

Use

\[
2\mathcal A_k
=J_k-J_{k+1}-\Delta_k^2.
\]

The two viscous pieces combine exactly:

\[
-2\nu E_{k+1}J_k
+4\nu E_{k+1}\mathcal A_k
=-2\nu E_{k+1}(J_{k+1}+\Delta_k^2).
\]

Therefore

\[
\boxed{
\dot D_k
+2\nu E_{k+1}
\left[
J_{k+1}+\Delta_k^2
\right]
=
2Q_kJ_k+4E_k\mathcal M_{N,k}.
}
\]

This identity is exact for the smooth whole-space derivative covariance chain.

## 3. Consequence: viscosity is now sign-definite

Since

\[
J_{k+1}\ge0,
\qquad
\Delta_k^2\ge0,
\]

the entire viscous contribution to `D_k` is nonpositive.

Thus the previous sign-indefinite normalized V-branch was a consequence of dividing by the changing derivative energy `E_k`.

For the energy-weighted geometric defect, viscosity can only dissipate:

1. the next-order multi-axis content `E_{k+1}J_{k+1}`;
2. the neighboring derivative-covariance mismatch `E_{k+1}Delta_k^2`.

This is the first formulation in the active route in which the S/V split collapses to

\[
\boxed{
\text{nonlinear projective production}
\quad\text{versus}\quad
\text{pure projective viscous dissipation}.
}
\]

## 4. Bound the nonlinear source

Let

\[
\mathcal F_k
=
\left(
\sum_{|I|=k}\|F_I\|_2^2
\right)^{1/2}.
\]

Then

\[
L_k=\mathcal F_k/\sqrt{E_k}.
\]

By Cauchy--Schwarz,

\[
|Q_k|
\le\sqrt{E_k}\,\mathcal F_k.
\]

The projective mixing bound gives

\[
|\mathcal M_{N,k}|
\le
\sqrt{J_k(1-J_k)}L_k.
\]

Hence

\[
\begin{aligned}
2Q_kJ_k+4E_k\mathcal M_{N,k}
&\le
2\sqrt{E_k}\mathcal F_kJ_k
+4\sqrt{E_k}\mathcal F_k\sqrt{J_k(1-J_k)}\\
&=
\sqrt{D_k}\mathcal F_k
\left[
2\sqrt{J_k}+4\sqrt{1-J_k}
\right].
\end{aligned}
\]

For `0<=J<=2/3`, the bracket is maximized at `J=1/5` and equals

\[
2\sqrt5.
\]

Therefore

\[
\boxed{
\dot D_k
+2\nu E_{k+1}(J_{k+1}+\Delta_k^2)
\le
2\sqrt5\,\sqrt{D_k}\,\mathcal F_k.
}
\]

The constant is not central; the structural point is the square-root energy weighting and the sign-definite viscosity.

## 5. Factorial physical-scale weighting

Fix `ell>0` and define

\[
\widehat E_k
=\frac{\ell^{2k}E_k}{(k!)^2},
\]

\[
\boxed{
\widehat D_k
=\frac{\ell^{2k}D_k}{(k!)^2}
=\widehat E_kJ_k,
}
\]

and

\[
\widehat F_k
=\frac{\ell^k\mathcal F_k}{k!}.
\]

For a fixed `ell`, multiply the preceding inequality by `ell^{2k}/(k!)^2`:

\[
\boxed{
\dot{\widehat D}_k
+
\frac{2\nu}{\ell^2}(k+1)^2
\widehat E_{k+1}
(J_{k+1}+\Delta_k^2)
\le
2\sqrt5\sqrt{\widehat D_k}\,\widehat F_k.
}
\]

Since

\[
\widehat E_{k+1}J_{k+1}=\widehat D_{k+1},
\]

the first viscous piece is a shifted weighted projective defect with the coercive factor `(k+1)^2`.

## 6. Sum over derivative order

Define

\[
\boxed{
\mathfrak D_\ell
=\sum_{k\ge0}\widehat D_k.
}
\]

Formally, whenever the sums are finite enough to justify the operation,

\[
\begin{aligned}
\dot{\mathfrak D}_\ell
&+
\frac{2\nu}{\ell^2}
\sum_{k\ge0}(k+1)^2
\widehat E_{k+1}
(J_{k+1}+\Delta_k^2)\\
&\le
2\sqrt5
\sum_{k\ge0}
\sqrt{\widehat D_k}\,\widehat F_k.
\end{aligned}
\]

Cauchy--Schwarz yields

\[
\boxed{
\dot{\mathfrak D}_\ell
+
\frac{2\nu}{\ell^2}\mathfrak Q_\ell
\le
2\sqrt5
\sqrt{\mathfrak D_\ell}
\|\widehat F\|_{\ell^2_k},
}
\]

where

\[
\boxed{
\mathfrak Q_\ell
=
\sum_{k\ge0}(k+1)^2
\widehat E_{k+1}
(J_{k+1}+\Delta_k^2).
}
\]

Thus the common S/V majorant sought previously reduces to controlling a single factorial forcing norm.

## 7. Insert the forcing generating-function bound

Let

\[
W_k=\sqrt{\widehat E_k}
=\frac{\ell^k}{k!}\|D^{(k)}\omega\|_2.
\]

The factorial nonlinear-forcing decomposition gives schematically

\[
\widehat F
\lesssim
G*W+U*Z,
\qquad
Z_k=kW_k.
\]

Young's sequence inequality gives

\[
\boxed{
\|\widehat F\|_{\ell^2}
\lesssim
\|G\|_{\ell^1}\|W\|_{\ell^2}
+
\|U\|_{\ell^1}\|Z\|_{\ell^2}.
}
\]

The second factor

\[
\|Z\|_{\ell^2}^2
=\sum_{k\ge1}k^2\widehat E_k
\]

is exactly the derivative-order quantity naturally appearing in the viscous factorial dissipation, although the projective dissipation carries the additional factors `J_k` and covariance mismatch.

This is the first common factorial framework for both nonlinear and viscous directional channels.

## 8. Remaining obstruction

The new formulation does not yet close globally because

\[
\|G\|_{\ell^1}
\quad\text{and}\quad
\|U\|_{\ell^1}
\]

are analytic-type `L^infinity` derivative aggregates of the strain/velocity.

Also the projective viscous dissipation controls

\[
k^2\widehat E_kJ_k
\]

rather than the full

\[
k^2\widehat E_k.
\]

Therefore a nearly one-axis high-derivative sector can make the full derivative generator large while the projective dissipation is small. That sector must be returned to the locally anisotropic / axis-alignment regularity gate rather than absorbed purely by this inequality.

This produces a sharper dichotomy:

\[
\boxed{
\text{high derivatives remain multi-axis}
\Rightarrow
\text{projective viscous dissipation is strong},
}
\]

whereas

\[
\boxed{
\text{high derivatives become nearly one-axis}
\Rightarrow
\text{anisotropic alignment gate becomes the relevant branch}.
}
\]

## 9. Dynamic radius

If `ell=ell(t)`, then

\[
\frac d{dt}\widehat D_k
\]

acquires

\[
2k\frac{\dot\ell}{\ell}\widehat D_k.
\]

A decreasing radius (`dot ell<0`) produces another negative derivative-order weighted term. This is the standard structural mechanism by which the `z W'(z)` commutator contribution can potentially be absorbed.

Any proof claim must derive a quantitative radius ODE and show that `ell(t)` cannot reach zero at a finite time under the lower-order constraints. That step remains open.

Status: **OPEN DYNAMIC-RADIUS / ANISOTROPIC-DICHOTOMY CLOSURE**.
