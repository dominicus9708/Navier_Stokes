# Projective energy-weight family: interpolation between normalized and pairwise balances

Date: 2026-08-13

Status: **DERIVED ONE-PARAMETER IDENTITY / STRUCTURAL COMPARISON**.

This note explains why the active route should retain both

\[
D=EJ
\]

and

\[
K=E^2J.
\]

They are two members of a common family with different source/dissipation tradeoffs.

## 1. Define the family

For

\[
a\ge1,
\]

define

\[
\boxed{Z_a=E^aJ.}
\]

Use the base identities

\[
\dot E=2Q-2\nu P,
\]

and

\[
\frac14\dot J
=M_N+\nu(P/E)A_0,
\]

where

\[
A_0
=\frac12(J-J_1-\Delta_0^2).
\]

## 2. Exact evolution

Differentiating gives

\[
\begin{aligned}
\dot Z_a
&=2aE^{a-1}QJ
-2a\nu E^{a-1}PJ
+4E^aM_N
+4\nu E^{a-1}PA_0.
\end{aligned}
\]

Substitute the expression for `A_0`:

\[
\boxed{
\dot Z_a
+2\nu E^{a-1}P
\left[
(a-1)J+J_1+\Delta_0^2
\right]
=
2aE^{a-1}QJ+4E^aM_N.
}
\]

For every `a>=1`, viscosity is sign-definite.

## 3. Source bound

Let

\[
F=\|S\omega\|_2.
\]

Then

\[
|Q|\le E^{1/2}F,
\]

and

\[
|M_N|
\le
\sqrt{J(1-J)}\frac{F}{E^{1/2}}.
\]

Therefore

\[
\boxed{
\dot Z_a
+2\nu E^{a-1}P[(a-1)J+J_1+\Delta_0^2]
\le
E^{a-1/2}F
\left[
2aJ+4\sqrt{J(1-J)}
\right].
}
\]

The source always carries at least a `sqrt(J)` projective-depletion factor.

## 4. Endpoint `a=1`: regularity-transfer weight

For

\[
a=1,
\]

we recover

\[
Z_1=D=EJ,
\]

and

\[
\dot D
+2\nu P(J_1+\Delta_0^2)
\le
2\sqrt5\sqrt D\,F.
\]

Advantages:

- no extra positive power of `E` multiplies the square-root source after dividing by `sqrt D`;
- `D` is directly comparable to the Miller anisotropic criterion;
- the `k=0 -> 1` bridge gives `D_1 in L1 => regularity`.

Disadvantage:

- current-order projective viscous coercivity appears only after the matrix lower bound and is quadratic in `J`.

## 5. Endpoint `a=2`: pairwise geometric weight

For

\[
a=2,
\]

we get

\[
Z_2=K=E^2J.
\]

The viscous term is

\[
2\nu EP[J+J_1+\Delta_0^2].
\]

Using

\[
J+J_1+\Delta_0^2
=2[1-\operatorname{tr}(CC_1)],
\]

this is exactly the pairwise cross-gradient dissipation.

Advantages:

- the present projective defect `J` enters linearly;
- `K` has the exact pairwise representation

\[
K=\iint|\omega(x)\times\omega(y)|^2dxdy;
\]

- it is the natural object for dyadic physical-scale localization.

Disadvantage:

- the square-root equation carries an extra `E^{1/2}` in the nonlinear source.

## 6. Role separation

The active route should therefore use the endpoints for different tasks:

\[
\boxed{
D=EJ
\quad\text{for regularity transfer and derivative-order dissipation},
}
\]

\[
\boxed{
K=E^2J
\quad\text{for pairwise geometry and physical-scale localization}.
}
\]

Intermediate values `1<a<2` interpolate continuously between these tradeoffs but no specific intermediate exponent has yet produced an additional closure.

Status: **USE D AND K AS COMPLEMENTARY TYPED CHANNELS**.
