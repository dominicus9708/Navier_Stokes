# Vorticity-gradient left/right covariance and nonnormal palinstrophy production

Date: 2026-08-19

Status: **DERIVED EXACT GRADIENT-MATRIX IDENTITY + SCALE-RATE/PALINSTROPHY GATE / GLOBAL REGULARITY NOT PROVED**.

This note refines the derivative source in dynamic first-hitting variables.

---

## 1. Gradient-matrix equation

Let

\[
G=\nabla\Omega,
\qquad
A=\nabla U=S+W,
\]

where `S` is symmetric and `W` antisymmetric. In dynamic first-hitting variables,

\[
\partial_s\Omega+(U-c+a y)\cdot\nabla\Omega
=S\Omega+\nu\Delta\Omega-2a\Omega.
\]

Differentiating gives

\[
\boxed{
(\partial_s+(U-c+a y)\cdot\nabla)G
=SG-GS-GW+B+\nu\Delta G-3aG,
}
\]

where

\[
\boxed{
B_{ij}=(\partial_jS_{ik})\Omega_k.
}
\]

Thus the derivative source separates into:

1. left strain action `SG`;
2. right strain action `-GS`;
3. right rigid rotation `-GW`;
4. inhomogeneous strain source `B=(nabla S)Omega`;
5. diffusion;
6. scale damping `-3aG`.

---

## 2. Left and right gradient covariance

At points where

\[
p=|G|_F^2>0,
\]

define

\[
\boxed{
L_G=\frac{GG^T}{p},
\qquad
C_G=\frac{G^TG}{p}.
}
\]

Both are positive semidefinite, trace one matrices. Moreover `GG^T` and `G^TG` have the same nonzero eigenvalues, so `L_G` and `C_G` have the same spectrum. They differ only by their orientation in the left/output and right/input spaces.

Define the normalized left-right defect

\[
\boxed{
\mathfrak D_{LR}
=\|L_G-C_G\|_F^2
=\frac{\|GG^T-G^TG\|_F^2}{|G|_F^4}.
}
\]

Thus `D_LR` is precisely a normalized nonnormality of the vorticity-gradient matrix.

Since both matrices are trace-one PSD,

\[
0\le\mathfrak D_{LR}\le2.
\]

---

## 3. Exact homogeneous-strain production

The Frobenius contraction satisfies

\[
G:SG=p\,S:L_G,
\qquad
G:GS=p\,S:C_G.
\]

Hence

\[
\boxed{
G:(SG-GS)
=p\,S:(L_G-C_G).
}
\]

Therefore homogeneous strain can change palinstrophy only through left/right covariance mismatch.

If

\[
GG^T=G^TG,
\]

i.e. `G` is normal, this homogeneous strain contribution is exactly zero.

This is stronger than merely requiring a large strain magnitude.

---

## 4. Rigid rotation gives zero trace production

Because `G^TG` is symmetric and `W` is antisymmetric,

\[
\boxed{
G:GW=\operatorname{tr}(G^TGW)=0.
}
\]

Thus rigid rotation can reorient the derivative matrix but cannot directly amplify its Frobenius norm/palinstrophy.

---

## 5. Universal bound for the inhomogeneous source under first hitting

The source `B=(nabla S)Omega` satisfies pointwise

\[
|B|^2\le|\Omega|^2|\nabla S|^2.
\]

Under dynamic first-hitting normalization,

\[
\|\Omega\|_\infty=1.
\]

Axis-resolved Plancherel gives

\[
\|\nabla S\|_2^2=\frac12\|\nabla\Omega\|_2^2.
\]

Therefore

\[
\boxed{
\|B\|_2^2\le\frac12P,
\qquad
P=\|\nabla\Omega\|_2^2.
}
\]

Consequently

\[
\boxed{
\left|\int G:B\right|
\le\frac1{\sqrt2}P.
}
\]

Thus this inhomogeneous source has a universal O(1) normalized rate under the first-hitting cap.

---

## 6. Exact global palinstrophy ledger

Let

\[
H=\|\nabla G\|_2^2=\|\nabla^2\Omega\|_2^2.
\]

The drift `U-c+a y` has divergence `3a`. Combining this divergence with the pointwise scale term `-3aG` yields the global scale damping `3aP/2` in the half-palinstrophy equation.

Hence

\[
\boxed{
\frac12P'
+\frac32aP
+\nu H
=
\int p\,S:(L_G-C_G)\,dy
+\int G:B\,dy.
}
\]

Define

\[
\boxed{
\mathcal L_{LR}^2
=\frac1P\int p|S|^2\mathfrak D_{LR}\,dy.
}
\]

Then

\[
\left|\int pS:(L_G-C_G)\right|
\le P\mathcal L_{LR}.
\]

Together with the universal `B` bound,

\[
\boxed{
\frac12(\log P)'
+\frac32a
+\nu\frac HP
\le
\mathcal L_{LR}+\frac1{\sqrt2}.
}
\]

This is the main scale-rate/palinstrophy gate.

---

## 7. Recurrent-stage consequence

For a geometric scale stage `I` with

\[
\int_Ia\,ds=A_q=\frac12\log q,
\]

integrating gives

\[
\boxed{
\frac32A_q
+\nu\int_I\frac HPds
\le
\int_I\mathcal L_{LR}ds
+\frac{|I|}{\sqrt2}
+\frac12\left|\log\frac{P(s_1)}{P(s_0)}\right|.
}
\]

Thus a stage that is both short in normalized time and recurrent in palinstrophy cannot be driven solely by the bounded inhomogeneous source `B`; it must activate left/right gradient nonnormality or hyperpalinstrophy.

Conversely, very long stages can accumulate the O(1) `B` source, but the dynamic local-variance and finite-energy packing gates already make long tight/low-turnover Type-II stages expensive.

This provides a useful short-stage / long-stage complementarity.

---

## 8. Structural interpretation

The dangerous derivative survivor now requires more than interior projective angular dispersion. It must also choose between:

1. **gradient nonnormality** — `L_G` and `C_G` remain differently oriented relative to `S`;
2. **inhomogeneous strain source** — `(nabla S)Omega` acts for sufficient normalized time;
3. **hyperpalinstrophy** — diffusion/curvature scale becomes large;
4. **turnover/non-tightness** — already typed by previous local gates.

Rigid rotation alone is not a palinstrophy source.

Status: **DERIVATIVE SOURCE REFINED INTO LEFT/RIGHT NONNORMALITY + UNIVERSALLY BOUNDED INHOMOGENEOUS SOURCE + H/T; SHORT RECURRENT SCALE STEPS REQUIRE GENUINE NONNORMAL/HIGH-DERIVATIVE ACTION.**