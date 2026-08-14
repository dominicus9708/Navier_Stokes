# Exact co-affine Gaussian Markov closure of the pure affine+heat propagator

Date: 2026-08-14

Status: **PURE TIME-DEPENDENT AFFINE TRANSPORT/STRETCHING PLUS VISCOSITY IS EXACTLY REDUCED TO A TIME-DEPENDENT ANISOTROPIC GAUSSIAN MARKOV PROPAGATOR. HERMITE DEGREE IS PRESERVED. THE PREVIOUSLY SUSPECTED PURE AFFINE/Gaussian DEGREE-MIXING COMMUTATOR IS NOT AN INDEPENDENT OBSTRUCTION. GLOBAL REGULARITY NOT PROVED.**

## 1. Co-affine Cauchy coordinates

Let the Gaussian affine mean velocity gradient be `L(t)` and let

\[
F'(t)=L(t)F(t),
\qquad
F(t_0)=I.
\]

Because the velocity is incompressible,

\[
\operatorname{tr}L=0,
\]

so

\[
\det F(t)=1.
\]

Use the affine coordinates

\[
x=a(t)+F(t)z.
\]

For vorticity, use the Cauchy-transformed variable

\[
\widetilde\Omega(z,t)
=F(t)^{-1}\Omega(x,t).
\]

The pure affine transport and affine stretching terms cancel exactly in this variable.

## 2. Diffusion becomes time-dependent anisotropic heat

Spatial gradients transform by

\[
\nabla_x=F^{-T}\nabla_z.
\]

Therefore the Laplacian becomes

\[
\Delta_x
=
\nabla_z\cdot
\bigl(G(t)\nabla_z\bigr),
\qquad
G(t)=F(t)^{-1}F(t)^{-T}.
\]

Thus the homogeneous pure affine+viscous equation is

\[
\boxed{
\partial_t\widetilde\Omega
=
\nu\nabla_z\cdot(G(t)\nabla_z\widetilde\Omega).
}
\]

On the bounded-affine branch, the condition number of `F` is uniformly bounded, so `G(t)` is uniformly elliptic up to the same bounded-condition constants.

## 3. Exact Gaussian covariance

Since `G(t)` depends only on time, the propagator from `s` to `t` is convolution by a centered Gaussian with covariance

\[
\boxed{
C_{s,t}
=2\nu\int_s^tG(\tau)d\tau.
}
\]

These covariances add exactly:

\[
C_{s,t}=C_{s,r}+C_{r,t}.
\]

Hence the time-dependent anisotropic heat flow is still an exact Gaussian convolution Markov family.

Equivalently, if a Gaussian tracking covariance is transported in the co-affine frame by

\[
\widetilde\Sigma'(t)=2\nu G(t),
\]

then in physical coordinates

\[
\Sigma(t)=F(t)\widetilde\Sigma(t)F(t)^T
\]

satisfies

\[
\boxed{
\Sigma'
=L\Sigma+\Sigma L^T+2\nu I.
}
\]

This is precisely the covariance evolution naturally matched to the affine heat kernel.

## 4. General matrix Gaussian conditional expectation

Suppose

\[
\Sigma_p=\Sigma_c+C,
\qquad C\succ0.
\]

Let

\[
X=Y+Z,
\]

where

\[
Y\sim N(0,\Sigma_c),
\qquad
Z\sim N(0,C),
\]

are independent. Then

\[
X\sim N(0,\Sigma_p).
\]

The heat propagator is the Gaussian conditional expectation

\[
Tf(Y)=E[f(X)\mid Y].
\]

After whitening parent and child variables, the cross-correlation matrix is

\[
\mathcal R
=\Sigma_p^{-1/2}\Sigma_c^{1/2}
\]

(up to an irrelevant orthogonal choice of square roots).

Gaussian second quantization implies that on the `n`-th homogeneous Wiener/Hermite chaos, `T` acts by the symmetric tensor power of this correlation operator. Consequently

\[
\boxed{
\|T|_{\mathcal H_n}\|_{2\to2}
\le
\|\mathcal R\|^n.
}
\]

Writing

\[
q
:=
\lambda_{\max}
\bigl(
\Sigma_p^{-1/2}\Sigma_c\Sigma_p^{-1/2}
\bigr)
<1,
\]

we have

\[
\|\mathcal R\|^2=q.
\]

Therefore the **energy** in the `n`-th Hermite chaos contracts by at most

\[
\boxed{q^n.}
\]

For `n=2`,

\[
\boxed{
E_2^{(c)}
\le q^2E_2^{(p)}.
}
\]

The isotropic formula `c^n` is the special case `Sigma_c=c Sigma_p`.

## 5. No Hermite-degree mixing from pure affine+heat evolution

The crucial consequence is structural:

\[
\boxed{
\text{pure time-dependent affine+heat propagation preserves Hermite degree.}
}
\]

Anisotropy can rotate and distort the finite-dimensional coefficient tensor inside a fixed Hermite degree, but it does not transfer degree two into degree one, degree three, etc.

Thus a moving affine frame does **not** create an independent degree-mixing source when the Gaussian covariance is chosen to solve the matching affine heat covariance equation.

The earlier concern about a generic `affine/Gaussian Hermite commutator` was therefore an artifact of comparing against a non-co-moving fixed Gaussian basis.

## 6. Consequence for the second-chaos erasure barrier

On one bounded-condition matched block with radius `R`, the degree-two coefficient vector can be represented in a continuously normalized Gaussian basis as

\[
Y_2'+\mathcal A_2(t)Y_2=F_2,
\]

where pure affine+heat evolution acts entirely inside degree two.

On a geometric matched block,

\[
\|\mathcal A_2(t)\|
\lesssim_K R^{-2}.
\]

Possible basis rotation contributes only an in-degree finite-dimensional skew part; it does not create a different Hermite degree.

Integrating gives

\[
\int F_2dt
=Y_2(t_+)-Y_2(t_-)
+
\int\mathcal A_2(t)Y_2(t)dt.
\]

Hence if a block source action `a` does not survive in the endpoint degree-two state, then

\[
|a|
\lesssim_K
R^{-2}\int|Y_2(t)|dt.
\]

Cauchy--Schwarz over a block of length comparable to `R^2` yields exactly the same estimate as in the isotropic model:

\[
\boxed{
\int|Y_2|^2dt
\gtrsim_K
R^2a^2.
}
\]

Therefore the previously derived physical dissipation price

\[
\boxed{
D_{{\rm phys},j}^{\rm erase}
\gtrsim_K
W^{-1/2}R_j^5a_j^2
}
\]

extends to the pure **time-dependent bounded-affine+heat** propagator with only bounded-condition constants.

Consequently the strict-mesoscopic packing barrier

\[
D_{\rm phys}^{\rm erase}
\gtrsim
c_{K,\rho}
\frac{W^{5\varepsilon}}{\log W}
\]

also persists for the pure bounded-affine heat lane.

## 7. What the actual remaining linear obstruction is

After the Cauchy affine transform, the residual-vorticity equation still contains the coupling of Gaussian mean vorticity to the residual velocity,

\[
\boxed{
T_{\bar\Omega}\eta
=(\bar\Omega\cdot\nabla)r.
}
\]

For frozen `barOmega` in unweighted Fourier space, using

\[
\widehat r(k)
=
\frac{i k\times\widehat\eta(k)}{|k|^2},
\]

this operator has symbol

\[
-\frac{(\bar\Omega\cdot k)}{|k|^2}(k\times\cdot),
\]

which is skew-adjoint. Hence it redistributes vorticity without creating global unweighted `L2` enstrophy.

However it is a nonlocal order-zero operator and need not preserve a localized Gaussian Hermite degree decomposition.

Thus the true remaining linear localization problem is not the affine heat kernel. It is

\[
\boxed{
\text{mean-vorticity skew redistribution versus Gaussian/Hermite localization}.
}
\]

This lane must either be shown harmless by a weighted commutator estimate or be routed into the existing projective/Cauchy geometry ledger.

Status: **PURE TIME-DEPENDENT BOUNDED-AFFINE+HEAT PROPAGATOR CLOSED EXACTLY BY CO-AFFINE GAUSSIAN MARKOV STRUCTURE / STRICT-MESOSCOPIC SECOND-CHAOS HEAT ERASURE BARRIER EXTENDS TO THIS PROPAGATOR / REMAINING LINEAR OBSTRUCTION = MEAN-VORTICITY SKEW REDISTRIBUTION / GLOBAL REGULARITY NOT PROVED.**
