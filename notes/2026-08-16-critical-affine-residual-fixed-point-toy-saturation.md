# Critical affine-residual fixed-point toy saturation

Date: 2026-08-16

Status: **ADVERSARIAL SHARPNESS MODEL, NOT A NAVIER--STOKES SOLUTION. THE MODEL SIMULTANEOUSLY SATURATES THE CURRENT `R^-2` RESIDUAL-SEED, `R^2` DEFORMATION, CORE-COVARIANCE, LOG-STRAIN, AND `O(R)` HYPERBOLIC-RAMP LEDGERS. THEREFORE NO FURTHER SCALAR POWER IMPROVEMENT SHOULD BE EXPECTED WITHOUT USING WHOLE-SPACE NONLINEAR SELF-CONSISTENCY.**

## 1. Purpose

The current proof frontier pins the minimal residual source action to

\[
\mathcal B_R=R^{-2+o(1)},
\]

forces actual affine transition stretch

\[
q\gtrsim R^2,
\]

and, under a core-scale covariance ceiling, permits affine strain-energy of order one.

The question is whether these estimates are merely nonsharp upper/lower bounds or whether one can construct a consistent reduced model that saturates all of them simultaneously.

The following model shows that the scalar ledgers are genuinely critical.

It is deliberately only an affine-residual ODE/Gaussian benchmark; it is **not** claimed to solve the finite-energy whole-space Navier--Stokes equations.

## 2. Long weak residual-seeding stage

Use a normalized interval of total length `~R^2` ending at time zero.

On the long early stage

\[
-R^2\lesssim t\lesssim -R,
\]

set the residual variance/source scale to

\[
\boxed{B(t)\asymp R^{-4}.}
\]

Assume the signed residual mean source into the eventual axial direction saturates the existing covariance bound:

\[
\boxed{J(t)\asymp R^{-4}e_3.}
\]

Then the accumulated residual action is

\[
\boxed{
\mathcal B_R
=\int B(t)dt
\asymp R^{-2}.
}
\]

Before the strong affine ramp, the accumulated mean seed is

\[
\boxed{
m_{\rm seed}\asymp R^{-2}.}
\]

This exactly realizes the critical residual exponent.

## 3. Final hyperbolic axial-extension ramp

On the final ramp introduce a scalar `y(t)` satisfying

\[
\boxed{y'=R^{-1}y^2,}
\]

with

\[
y(t_0)=1,
\qquad
y(T)=R.
\]

The required duration is

\[
\boxed{
T-t_0
=R(1-R^{-1})
\asymp R.
}
\]

Define the incompressible affine transition

\[
\boxed{
F(t,t_0)
=\operatorname{diag}
\left(y^{-1},y^{-1},y^2\right).
}
\]

Then

\[
\det F=1
\]

and the endpoint stretch is

\[
\boxed{
q=\|F(T,t_0)\|=R^2.
}
\]

The affine strain is

\[
\boxed{
S(t)
=\operatorname{diag}
(-h',-h',2h'),
\qquad
h'=\frac{y'}y=\frac yR.
}
\]

Thus it is the ideal axial-extension shape with extensional axis `e3`.

## 4. Strain ledgers are simultaneously critical

The accumulated operator-norm strain is

\[
\int\|S\|_{op}dt
=2\int h'dt
=2\log R.
\]

Hence

\[
\boxed{
A_R\asymp2\log R.
}
\]

But the strain-energy is only order one:

\[
\begin{aligned}
\mathcal J_S
&=\int\|S\|_{op}^2dt\\
&=4\int h'^2dt\\
&=4R^{-1}(R-1).
\end{aligned}
\]

Therefore

\[
\boxed{
\mathcal J_S\to4.
}
\]

This shows explicitly how a logarithmically diverging L1 strain action can coexist with bounded L2 strain-energy: the rate accelerates hyperbolically across an `O(R)` interval.

## 5. Affine heat covariance remains at the core scale

During the long early stage the affine map is the identity, so a source injected there accumulates an isotropic heat covariance contribution of order

\[
R^2I.
\]

During the final ramp, the two transverse inverse-stretch factors are `y`, so

\[
\int_{t_0}^{T}y^2dt
=R(R-1)
\asymp R^2.
\]

The axial inverse factor is `y^-2`, giving only a smaller ramp contribution.

Consequently, after including the long early diffusion stage,

\[
\boxed{
\lambda_{\max}C\asymp R^2,
}
\]

and the covariance condition remains at the coherent parabolic scale rather than escaping by a power of `R`.

Thus

\[
\boxed{
\lambda_{\max}(\Sigma)\mathcal J_S
\asymp\nu R^2
\asymp\nu q,
}
\]

which saturates the deformation--diffusion product.

## 6. Seed times are amplified to an order-one mean

The long early-stage seed satisfies

\[
m_{\rm seed}\asymp R^{-2}e_3.
\]

The final affine transition acts on the axial direction by the factor

\[
R^2.
\]

Therefore

\[
\boxed{
F(T,t_0)m_{\rm seed}\asymp e_3.
}
\]

Equivalently,

\[
\boxed{
\mathcal B_R\,q\asymp1.
}
\]

Thus the endpoint order-one coherent mean is compatible with the exact critical seed--amplification balance.

## 7. Terminal residual scale can remain critical

If the residual variance is kept at

\[
B\asymp R^{-4}
\]

through the benchmark, then

\[
\boxed{
B R^4\asymp1,
}
\]

which is precisely the Reynolds-one residual crossing scale.

Thus the same reduced model can simultaneously represent

- a critical Reynolds-one residual variance,
- `R^-2` accumulated residual seed,
- `R^2` affine amplification,
- order-one affine strain-energy,
- logarithmic strain action,
- and an `O(R)` turnover-time hyperbolic ramp.

No current scalar exponent contradicts this configuration.

## 8. Why this is not a finite-energy Navier--Stokes solution

The final affine shape is

\[
S_{\rm ax}
=\operatorname{diag}(-a,-a,2a)
\]

up to a harmless factor-two convention relative to the earlier

\[
(-a/2,-a/2,a)
\]

normalization.

With coherent axial vorticity, the local Betchov mismatch has a fixed positive sign:

\[
\boxed{
\omega\cdot S\omega+4\det S>0
}
\]

on the aligned axial-extension core.

The exact local divergence identity therefore requires this mismatch to be supplied/removed by

\[
\boxed{
\text{boundary cubic flux}
\quad\lor\quad
\text{shape/coherence breakdown}.
}
\]

In a finite-energy whole-space flow, the pure affine field itself is impossible globally. Any Navier--Stokes realization of the toy benchmark must therefore build a surrounding compensating vorticity/strain reservoir, shell flux, palinstrophy, or positive-middle-strain region.

This missing exterior self-consistency is precisely what the scalar affine toy suppresses.

## 9. Consequence for the proof strategy

The benchmark demonstrates that trying to improve any of

\[
R^{-2},
\qquad R^2,
\qquad R,
\qquad \log R,
\qquad O(1)\text{ affine strain-energy}
\]

by another scalar interpolation is unlikely to close the problem: these values are mutually compatible and nearly saturate the exact deformation--diffusion inequalities.

The next theorem must distinguish a genuine whole-space Navier--Stokes field from this reduced critical fixed point.

A precise target is:

> **Critical affine-residual fixed-point exclusion.** A finite-energy whole-space smooth Navier--Stokes solution cannot realize an asymptotically axial critical episode with `B-action~R^-2`, affine stretch `~R^2`, core-scale affine covariance, and `O(1)` affine strain-energy over an `O(R)` hyperbolic ramp without paying a scale-orthogonal exterior Betchov/positive-middle-strain/palinstrophy cost that prevents indefinite repetition.

No proof of this exclusion theorem is currently available.

Status: **CURRENT SCALAR LEDGERS SHOWN SHARP BY AN ADVERSARIAL CRITICAL MODEL / THE TRUE REMAINING INFORMATION IS WHOLE-SPACE NONLINEAR SELF-CONSISTENCY AND EXTERIOR COMPENSATION, NOT ANOTHER POWER COUNT.**
