# Adjoint kernel removes the Gaussian drift source

Date: 2026-08-14

Status: **EXACT REPRESENTATION IDENTITY. THE GAUSSIAN DRIFT SOURCE IS NOT AN INDEPENDENT PHYSICAL VORTICITY-AMPLIFICATION CHANNEL; IT IS RECLASSIFIED AS A WEIGHT/TRANSPORT-MISMATCH CHANNEL. GLOBAL REGULARITY NOT PROVED.**

## 1. Vorticity equation

In terminal-normalized variables,

\[
\partial_t\Omega+U\cdot\nabla\Omega
=S\Omega+\nu\Delta\Omega,
\qquad
\nabla\cdot U=0.
\]

Fix the terminal first-hitting point `(x_*,0)` with

\[
|\Omega(x_*,0)|=1.
\]

Let `P_{s,t}` denote the evolution operator of the linear advection--diffusion equation

\[
\partial_t f+U\cdot\nabla f=\nu\Delta f.
\]

Its backward adjoint transition density from time `s<0` to `(x_*,0)` is denoted by

\[
K(x,s;x_*,0)\ge0,
\qquad
\int_{\mathbb R^3}K(x,s;x_*,0)\,dx=1.
\]

## 2. Exact Duhamel representation

Duhamel's formula gives

\[
\boxed{
\Omega(x_*,0)
=
P_{-q,0}\Omega(-q)(x_*)
+
\int_{-q}^{0}
P_{s,0}(S\Omega)(s)(x_*)\,ds.
}
\]

Equivalently,

\[
\boxed{
\Omega(x_*,0)
=
\int K(x,-q;x_*,0)\Omega(x,-q)\,dx
+
\int_{-q}^{0}\int K(x,s;x_*,0)S\Omega(x,s)\,dx\,ds.
}
\]

There is no separate transport source and no separate viscous source in this representation. They are exactly built into the Markov kernel `K`.

## 3. Fixed stretching action forced by first hitting

At the previous adaptive checkpoint,

\[
\|\Omega(-q)\|_{L^\infty}\le q^{-1}.
\]

Because `K` is a probability density,

\[
\left|
\int K(x,-q)\Omega(x,-q)\,dx
\right|
\le q^{-1}.
\]

Since the terminal magnitude equals one,

\[
\boxed{
\int_{-q}^{0}\int K(x,s)|S\Omega|(x,s)\,dx\,ds
\ge
1-q^{-1}.
}
\]

Thus terminal first hitting requires an order-one total stretching action along the exact advection--diffusion transition law.

This is a physical source statement and contains no Gaussian-window drift term.

## 4. Why the Gaussian drift appeared

For a prescribed Gaussian weight `gamma`, differentiation of

\[
\int\gamma\Omega
\]

produces a residual transport term because `gamma` is not the exact adjoint solution transported by the full velocity field.

The previously derived term

\[
J_{\rm drift}
=
\int\gamma\,\delta\Omega
(r\cdot\nabla\log\gamma)
\]

therefore measures the mismatch between

1. the self-consistent affine Gaussian observation window, and
2. the exact nonlinear advection--diffusion transition density.

It is not an additional physical vorticity-amplification mechanism beyond stretching.

## 5. Drift-independent kernel density ceiling

The divergence-free transport part is skew in `L^2`. For the scalar advection--diffusion semigroup,

\[
\frac12\frac d{dt}\|f\|_2^2
=-\nu\|\nabla f\|_2^2.
\]

Combining this with the three-dimensional Nash inequality gives the drift-independent ultracontractive estimate

\[
\boxed{
\|P_{s,t}\|_{L^1\to L^\infty}
\lesssim
(\nu(t-s))^{-3/2}.
}
\]

Consequently the transition density satisfies

\[
\boxed{
0\le K(x,s;x_*,0)
\lesssim
(\nu|s|)^{-3/2}
}
\]

with a dimensional constant independent of the detailed incompressible drift.

This retains the same volume exponent that was used in the Gaussian dissipation rearrangement.

## 6. What is and is not controlled

The Nash estimate gives an upper density ceiling but does **not** by itself give a two-sided Gaussian spatial comparison

\[
c_K\gamma_{\Sigma(s),a(s)}
\le K(\cdot,s;x_*,0)
\le C_K\gamma_{\Sigma(s),a(s)}.
\]

Such a comparison would control the shape and localization of the exact adjoint kernel. It is not obtained from incompressibility plus the present bounded-affine mean hypotheses alone, because residual nonlinear transport can mix or displace the transition density.

Therefore the former Gaussian gap-two drift lane is reclassified into the dichotomy:

### A. Gaussian-comparable adjoint kernel

If `K` remains quantitatively comparable to the bounded-condition affine Gaussian on the responsible scale-time blocks, then the Gaussian variance/source ledgers transfer up to constants, while the exact adjoint representation removes the separate drift source. The surviving source is then physical stretching and is subject to the strengthened Hermite-diagonal/projective barriers.

### B. Kernel-deformation / nonlinear-mixing branch

If such comparison fails, then the remaining escape is not a hidden vorticity source. It is a quantitative deformation/mixing of the exact advection--diffusion kernel relative to the affine Gaussian observation geometry.

This is the precise nonlinear transport branch that must be controlled to complete the bounded-affine proof route.

## 7. Revised causal map

The physical first-hitting growth has the exact causal form

\[
\boxed{
\text{previous-checkpoint inheritance}
+\text{vortex stretching along }K
=\text{terminal vorticity}.
}
\]

The previous-checkpoint inheritance is asymptotically negligible on the adaptive branch. Therefore an order-one stretching action is unavoidable.

The Gaussian drift term should henceforth be treated only as a diagnostic of the discrepancy between `K` and the moving Gaussian frame, not as an independent physical amplification channel.

Status: **GAUSSIAN DRIFT REMOVED FROM THE PHYSICAL SOURCE LEDGER BY THE EXACT ADJOINT MARKOV REPRESENTATION / REMAINING TRANSPORT ISSUE = QUANTITATIVE ADJOINT-KERNEL DEFORMATION OR MIXING / GLOBAL REGULARITY NOT PROVED.**
