# Strain residual to cubic affine-source transfer

Date: 2026-08-13

Status: **DERIVED WEIGHTED CUBIC STABILITY ESTIMATE / GLOBAL REGULARITY NOT PROVED**.

Let `gamma` be a probability weight.  Let `A_*` be a unit principal shape of the Gaussian strain second moment in the five-dimensional Hilbert space of trace-free symmetric matrices.  Write

\[
a(y)=\langle S(y),A_*\rangle_F,
\qquad
R(y)=S(y)-a(y)A_*.
\]

Then

\[
\int\gamma |R|_F^2=D_{S,\rm shape}.
\]

## 1. Determinant transfer

For `3 x 3` matrices,

\[
|\det X-\det Y|
\le C(|X|_F^2+|Y|_F^2)|X-Y|_F.
\]

Since `|a|<=|S|_F`, applying this with `X=S` and `Y=aA_*` gives

\[
\boxed{
\left|
\int\gamma\det S
-\det(A_*)\int\gamma a^3
\right|
\le C M_{4,S}^2 D_{S,\rm shape}^{1/2},
}
\]

where

\[
M_{4,S}=\left(\int\gamma |S|_F^4\right)^{1/4}.
\]

## 2. Amplitude variance

Let

\[
\bar a=\int\gamma a,
\qquad
\bar R=\int\gamma R.
\]

The principal-shape covariance identity gives

\[
\int\gamma a^2=E_{S,\gamma}\mu_1.
\]

Because `A_*` is orthogonal to `R`,

\[
|\bar S_\gamma|_F^2=\bar a^2+|\bar R|_F^2.
\]

Hence

\[
D_{S,\rm amp}
=\operatorname{Var}_\gamma(a)-|\bar R|_F^2.
\]

Therefore

\[
\boxed{
\operatorname{Var}_\gamma(a)
\le D_{S,\rm amp}+D_{S,\rm shape}.
}
\]

Using `|a|<=|S|_F`, the cubic moment obeys

\[
\boxed{
\left|
\int\gamma a^3-\bar a^3
\right|
\le C M_{4,S}^2
\left(D_{S,\rm amp}+D_{S,\rm shape}\right)^{1/2}.
}
\]

## 3. Combined transfer

Combining the two estimates,

\[
\boxed{
\left|
\int\gamma\det S
-\det(A_*)\bar a^3
\right|
\le C M_{4,S}^2
\left(D_{S,\rm amp}+D_{S,\rm shape}\right)^{1/2}.
}
\]

Thus if the two strain residual channels are small relative to the weighted fourth-moment scale, the actual weighted cubic strain invariant is close to that of one constant affine strain matrix `bar a A_*`.

## 4. Consequence with the Betchov-orbit gap

For normalized source-positive `A_*`, let

\[
d_*=\operatorname{dist}_F(A_*,\mathcal O_B),
\]

where `O_B` is the rotational orbit of `diag(-2,1,1)/sqrt(6)`.

The exact finite-dimensional identity derived separately is

\[
1-\eta_{\det}(A_*)
=\frac{d_*^2}{2}(3-d_*^2)^2.
\]

Therefore the low-strain-residual branch has only two source-efficient possibilities:

1. `A_*` is close to the Betchov orbit, returning to the biaxial compression-diffusion / precursor-reservoir route;
2. `A_*` remains a fixed distance from the Betchov orbit, yielding an explicit determinant/source-efficiency deficit.

If `D_S,shape + D_S,amp` itself is not small, that is already the Gaussian non-affinity residual channel.

Hence the strain sector reduces to

\[
\boxed{
\text{non-affine strain variance}
\quad\text{or}\quad
\text{Betchov-near affine compression-diffusion}
\quad\text{or}\quad
\text{strict cubic-source deficit}.
}
\]

## 5. Claim boundary

The estimate above is a weighted finite-moment stability bound.  The factor `M_{4,S}` must still be controlled on the chosen Gaussian windows.  Under first-hitting normalization the mean-free strain is BMO-controlled; a large fourth moment therefore has to be cross-typed with a large affine mean and/or strongly anisotropic Gaussian geometry rather than silently discarded.

Status: **STRAIN RESIDUAL-TO-AFFINE CUBIC TRANSFER CLOSED / FOURTH-MOMENT AND REPEATED-SATURATION COSTS REMAIN ACTIVE**.
