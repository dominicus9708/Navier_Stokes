# Strain BMO gap from Gaussian Poincare saturation

Date: 2026-08-14

Status: **DERIVED FIXED-POSITIVE STRAIN-VARIANCE GAP / VANISHING-VARIANCE REGIME REMAINS WEAK**.

At terminal first-hitting normalization one has `||Omega||_infty <= 1`.  Because the strain is a Calderon--Zygmund transform of vorticity, each scalar strain component has a uniform Euclidean BMO seminorm on the bounded-affine branch, after whitening with a bounded-condition Gaussian.

This note gives a direct quantitative argument showing that a BMO-bounded strain component with fixed positive Gaussian variance cannot approach the Gaussian Poincare equality family arbitrarily closely.

No novelty claim is made without a separate literature-priority audit.

---

## 1. Scalar setup

Let `gamma` be the standard Gaussian measure on `R^3`, and let

\[
f\in H^1(\gamma),
\qquad
\int f\,d\gamma=0,
\qquad
\|f\|_{BMO(R^3)}\le K.
\]

Write the Hermite decomposition

\[
f=a\cdot z+h,
\]

where `a dot z` is the first chaos and `h` contains Hermite degrees at least two.

Set

\[
V=\int f^2d\gamma,
\qquad
\delta=\int h^2d\gamma.
\]

Then

\[
V=|a|^2+\delta
\]

and the Ornstein--Uhlenbeck spectral decomposition gives

\[
\boxed{
\int|\nabla f|^2d\gamma
\ge V+\delta.
}
\]

Hence it suffices to force `delta>0` quantitatively.

---

## 2. Mean oscillation of a first-chaos function

On the centered Euclidean ball `B_R subset R^3`, the average of `a dot z` is zero and

\[
\frac1{|B_R|}\int_{B_R}|a\cdot z|dz
=\frac38|a|R.
\]

For any two functions `g,h`, their mean oscillations satisfy

\[
MO_{B_R}(g)
\le MO_{B_R}(g+h)
+2\frac1{|B_R|}\int_{B_R}|h|dz.
\]

Applying this with `g=a dot z` gives

\[
\frac38|a|R
\le K
+2\frac1{|B_R|}\int_{B_R}|h|dz.
\]

---

## 3. Convert Gaussian L2 error into local Euclidean L1 error

On `B_R`,

\[
\gamma(z)
\ge
(2\pi)^{-3/2}e^{-R^2/2}.
\]

Therefore

\[
\|h\|_{L^2(B_R,dz)}
\le
(2\pi)^{3/4}e^{R^2/4}\delta^{1/2}.
\]

Hence

\[
\frac1{|B_R|}\int_{B_R}|h|dz
\le
C_R\delta^{1/2},
\]

where

\[
C_R
=(2\pi)^{3/4}|B_R|^{-1/2}e^{R^2/4}.
\]

Thus

\[
\boxed{
\frac38|a|R
\le K+2C_R\delta^{1/2}.
}
\]

---

## 4. Fixed positive variance forces a strict gap

Assume

\[
V\ge v_0>0.
\]

If

\[
\delta\ge v_0/2,
\]

the desired gap is immediate.

Otherwise

\[
|a|^2
=V-\delta
\ge v_0/2.
\]

Choose

\[
R_*=\frac{16K}{3\sqrt{v_0/2}}
\]

when `K>0`.  Then

\[
\frac38\sqrt{v_0/2}R_*=2K.
\]

The previous inequality implies

\[
K
\le2C_{R_*}\delta^{1/2},
\]

hence

\[
\delta
\ge
\frac{K^2}{4C_{R_*}^2}.
\]

Therefore

\[
\boxed{
\int|\nabla f|^2d\gamma
\ge
V+\eta_{BMO}(K,v_0)
}
\]

with

\[
\boxed{
\eta_{BMO}(K,v_0)
=
\min\left\{
\frac{v_0}{2},
\frac{K^2}{4C_{R_*}^2}
\right\}>0.
}
\]

The explicit constant is extremely small when `v0` is small; the important point here is strict positivity for fixed positive variance.

---

## 5. Apply to the strain tensor

Let

\[
\delta S=S-\bar S_\gamma,
\qquad
V_S=\int\gamma|\delta S|_F^2.
\]

If

\[
V_S\ge b>0,
\]

at least one of the nine matrix entries has Gaussian variance at least `b/9`.

After whitening a Gaussian of bounded condition number, the BMO seminorm of that scalar entry remains bounded by a constant `K_*` depending only on the first-hitting vorticity cap, the Calderon--Zygmund operator, and the covariance condition bound.

Applying the scalar lemma to that entry and ordinary Gaussian Poincare to the others gives

\[
\boxed{
\int\gamma
|\nabla_z\delta S|_F^2
\ge
V_S+\eta_S(b,K_*)
}
\]

for some explicit

\[
\eta_S(b,K_*)>0.
\]

In physical Gaussian coordinates this becomes

\[
\boxed{
\int\gamma_\Sigma
\operatorname{tr}
\left[
(\nabla S)\Sigma(\nabla S)^T
\right]
\ge
V_S+\eta_S(b,K_*).
}
\]

Consequently

\[
\boxed{
D_S
:=\int\gamma_\Sigma|\nabla S|_F^2
\ge
\frac{V_S+\eta_S(b,K_*)}
{\lambda_{\max}(\Sigma)}.
}
\]

---

## 6. Four-channel consequence

Since

\[
\mathcal B_\gamma
=V_S+\frac12V_\omega,
\]

an order-one residual state has either

\[
V_S\ge b_0/2
\]

or

\[
V_\omega\ge b_0.
\]

The earlier bounded-vorticity lemma gives a strict Gaussian Poincare gap in the second case.  The present BMO lemma gives a strict gap in the first case.

Thus **every fixed-positive four-channel residual state has a strict Poincare deficit from equality**, although the explicit gap degenerates as the residual level tends to zero.

---

## 7. Limitation

The estimate does not give a useful power-law surplus when

\[
b=b(q)\to0.
\]

The ball radius `R_*` grows like `K/sqrt(b)` and the explicit Gaussian-to-Euclidean conversion makes the resulting `eta_S` exponentially small in `1/b`.

Therefore this closes fixed-positive strain Poincare saturation but not the intermediate pulse

\[
q^{-1/(1+6\varepsilon)}
\lesssim
\mathcal B_\gamma
\ll1.
\]

A stronger route is to use the fact that the residual is not an arbitrary BMO field: it is the gradient of a finite-energy velocity.  Hermite-degree/kinetic-energy coupling gives a much stronger scale-dependent curvature barrier, developed separately.

Status: **FIXED-POSITIVE STRAIN-POINCARE SATURATION EXCLUDED / FINITE-ENERGY HERMITE BARRIER IS THE STRONGER NEXT STEP**.
