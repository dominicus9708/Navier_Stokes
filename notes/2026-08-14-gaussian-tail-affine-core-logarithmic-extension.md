# Gaussian-tail affine-core logarithmic extension

Date: 2026-08-14

Status: **DERIVED ON THE BOUNDED-CONDITION GAUSSIAN BRANCH. AN ORDER-ONE COHERENT AFFINE ROTATION WITH GRADIENT VARIANCE `B <= C R^-2` FORCES KINETIC-ENERGY OCCUPANCY OUT TO `R sqrt(log R)`. THIS STRENGTHENS THE `W^(1/10)` CORE CEILING BY A LOGARITHMIC FACTOR. GLOBAL REGULARITY NOT PROVED.**

## 1. Setup

Let `U` be the terminal-normalized divergence-free velocity, let `gamma_Sigma` be a bounded-condition Gaussian centered at `a`, and write

\[
L=\int\gamma_\Sigma\nabla U,
\qquad
r(x)=U(x)-c-L(x-a),
\]

where the constant vector `c` is arbitrary for the moment. Let

\[
R=(\det\Sigma)^{1/6},
\]

and assume

\[
\boxed{
B
:=
\int\gamma_\Sigma|\nabla U-L|^2
\le C_0R^{-2}.
}
\]

Suppose also that the coherent antisymmetric part is nontrivial:

\[
\boxed{|\operatorname{skew}L|\ge c_0>0.}
\]

On the terminal mean-vorticity occupancy branch this follows from

\[
|\bar\Omega_\gamma|\ge c_0,
\]

because the antisymmetric part of the Gaussian mean gradient represents one half of the Gaussian mean vorticity.

All constants below may depend on the Gaussian condition-number bound, `C0`, and `c0`.

## 2. Convert weighted gradient variance to an enlarged Euclidean ball

For a bounded-condition Gaussian there are constants `c_K,C_K>0` such that on

\[
B_{\rho R}(a),
\]

we have

\[
\gamma_\Sigma(x-a)
\ge
c_KR^{-3}e^{-C_K\rho^2}.
\]

Therefore

\[
\begin{aligned}
\int_{B_{\rho R}(a)}|\nabla U-L|^2dx
&\le
c_K^{-1}R^3e^{C_K\rho^2}B\\
&\le
C_KR e^{C_K\rho^2}.
\end{aligned}
\]

Thus

\[
\boxed{
\int_{B_{\rho R}}|\nabla r|^2
\lesssim_K
R e^{C_K\rho^2}.
}
\]

## 3. Local Poincare for the non-affine velocity remainder

Let `d_rho` be the average of `r` on `B_{rho R}`. Euclidean Poincare gives

\[
\begin{aligned}
\int_{B_{\rho R}}|r-d_\rho|^2dx
&\lesssim
(\rho R)^2
\int_{B_{\rho R}}|\nabla r|^2dx\\
&\lesssim_K
\rho^2R^3e^{C_K\rho^2}.
\end{aligned}
\]

Write

\[
h=r-d_\rho.
\]

Then on the centered ball

\[
U=L(x-a)+d+h
\]

for another constant vector `d`.

Because the ball is centered at `a`, the affine odd term is orthogonal to constants:

\[
\int_{B_{\rho R}}L(x-a)\cdot d\,dx=0.
\]

Hence

\[
\|L(x-a)+d\|_{L^2(B_{\rho R})}^2
\ge
\|L(x-a)\|_2^2.
\]

Since `|skew L|>=c0`,

\[
\boxed{
\|L(x-a)\|_{L^2(B_{\rho R})}^2
\gtrsim_{c_0}
(\rho R)^5.
}
\]

## 4. Choose the largest logarithmic enlargement allowed by the Gaussian tail

The ratio between the remainder energy and the affine energy satisfies

\[
\frac{\|h\|_2^2}
{\|L(x-a)\|_2^2}
\lesssim_K
\frac{e^{C_K\rho^2}}
{\rho^3R^2}.
\]

Choose

\[
\boxed{
\rho^2=\alpha_K\log R
}
\]

with a fixed sufficiently small `alpha_K>0`, for example so that

\[
C_K\alpha_K<1.
\]

Then

\[
e^{C_K\rho^2}
=R^{C_K\alpha_K}
=o(R^2),
\]

and therefore

\[
\frac{\|h\|_2^2}
{\|L(x-a)\|_2^2}
\to0.
\]

For sufficiently large `R`, the triangle inequality gives

\[
\|U\|_{L^2(B_{\rho R})}
\ge
\frac12
\|L(x-a)+d\|_{L^2(B_{\rho R})}.
\]

Consequently

\[
\boxed{
\|U\|_2^2
\gtrsim_K
R^5(\log R)^{5/2}.
}
\]

This is an instantaneous finite-energy cost. It does not rely on a material tube, a pointwise vorticity lower bound, or spacetime dissipation packing.

## 5. Terminal-normalized kinetic-energy consequence

The normalized kinetic energy satisfies

\[
\|U\|_2^2
=W^{1/2}\|u\|_2^2
\le
W^{1/2}\|u_0\|_2^2.
\]

Hence an order-one coherent Gaussian mean rotation with `B <= C R^-2` must satisfy

\[
\boxed{
R^5(\log R)^{5/2}
\lesssim
W^{1/2}.
}
\]

Equivalently,

\[
R
\lesssim
W^{1/10}(\log R)^{-1/2}
\]

up to constants.

This strengthens the earlier instantaneous `R <= C W^(1/10)` mean-vorticity energy ceiling.

## 6. Mean-creation scaling

On the surviving terminal mean-creation branch,

\[
R=R_m=m^{-1/2},
\qquad
m=W^{-1/3}\Lambda.
\]

Then

\[
R^5(\log R)^{5/2}
=m^{-5/2}(\log R)^{5/2}
\lesssim W^{1/2}.
\]

Taking the power `2/5`,

\[
\boxed{
 m^{-1}\log R
\lesssim W^{1/5}.
}
\]

Thus

\[
\boxed{
 m
\gtrsim W^{-1/5}\log R.
}
\]

Since `m=W^(-1/3)Lambda` and `log R` is comparable to `log W` on every polynomially separated survivor,

\[
\boxed{
\Lambda
\gtrsim
W^{2/15}\log W
}
\]

up to fixed constants and lower-order logarithmic corrections.

For an infinite disjoint first-hitting cascade, the previously established spacetime dissipation ledger may strengthen constant-multiple saturation further, but the present statement is already a single-time kinetic-energy obstruction.

## 7. Geometric interpretation

A small Gaussian gradient variance at radius `R` cannot describe an order-one affine rotation that abruptly terminates at an ordinary `O(R)` boundary. The Gaussian tail says that the same affine state remains dominant, in Euclidean `L2`, throughout an enlarged core of radius

\[
\boxed{
R_{\rm ext}
\asymp
R\sqrt{\log R}.
}
\]

Thus a finite-energy realization must choose among:

1. extending the coherent rotation into this logarithmically enlarged region;
2. placing a highly concentrated transition layer in a set whose Gaussian mass is small enough to evade `B`;
3. transferring the termination into higher-Hermite / shell / palinstrophy structure.

The first alternative pays the kinetic-energy lower bound proved above. The latter two are dynamic/derivative branches and are the next closure targets.

Status: **ORDER-ONE ROTATION + `B <= C R^-2` FORCES `R sqrt(log R)` AFFINE-CORE EXTENSION AND `R^5(log R)^(5/2)` KINETIC ENERGY / SURVIVAL THRESHOLD STRENGTHENED TO `Lambda >=~ W^(2/15) log W` / GLOBAL REGULARITY NOT PROVED.**
