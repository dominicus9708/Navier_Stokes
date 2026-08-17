# Log-extended Betchov compensation trichotomy

Date: 2026-08-17

Status: **DERIVED ON THE BOUNDED-CONDITION, LATE COHERENT, ALIGNED `lambda_2<=0` BRANCH. THE LOW-GAUSSIAN-VARIANCE AFFINE CORE EXTENDS TO `R sqrt(log R)`. ON THAT ENLARGED REGION, EITHER CUBIC RESIDUAL STRAIN IS MACROSCOPIC, OR THE POSITIVE LOCAL BETCHOV MISMATCH SURVIVES. THE SURVIVING MISMATCH FORCES EITHER A LARGE EXTERNAL ENSTROPHY RESERVOIR OR PALINSTROPHY `P >= c R sqrt(log R)`. GLOBAL REGULARITY NOT PROVED.**

## 1. Late coherent aligned branch

Let `gamma_Sigma` be the bounded-condition self-consistent Gaussian with scale

\[
R=(\det\Sigma)^{1/6}.
\]

Assume at a late-ramp time

\[
|\bar\Omega|\ge c_0>0,
\qquad
B=\operatorname{Var}_\gamma(S)+\frac12\operatorname{Var}_\gamma(\Omega)
\le C_0R^{-2}.
\]

Let

\[
\bar S=E_\gamma S.
\]

Assume the mean coherent vorticity is aligned with the maximally extensional eigenvector of `bar S`, and that the middle eigenvalue obeys

\[
\bar\lambda_2\le0.
\]

On the critical late ramp, also assume the active extension rate is bounded below and above by fixed constants:

\[
0<a_0\le\bar\lambda_1\le a_1<\infty.
\]

Then the affine reference mismatch

\[
m_0
:=
\bar\Omega\cdot\bar S\bar\Omega
+4\det\bar S
\]

satisfies

\[
\boxed{m_0\ge c_*>0.}
\]

Indeed `bar lambda_2<=0` and trace-freeness imply `det bar S>=0`, while aligned maximal extension gives

\[
\bar\Omega\cdot\bar S\bar\Omega
=\bar\lambda_1|\bar\Omega|^2
\ge a_0c_0^2.
\]

## 2. Extend low quadratic variance to a logarithmic Euclidean core

Choose

\[
L_R=\rho R,
\qquad
\rho^2=\alpha\log R
\]

with fixed sufficiently small `alpha>0` depending only on the Gaussian condition bound.

The Gaussian lower bound on `B_{L_R}` gives

\[
\int_{B_{L_R}}|S-\bar S|^2dx
\lesssim
R^3e^{C\rho^2}B
\lesssim
Re^{C\rho^2},
\]

and similarly

\[
\int_{B_{L_R}}|\Omega-\bar\Omega|^2dx
\lesssim
Re^{C\rho^2}.
\]

Since

\[
|B_{L_R}|\asymp L_R^3
\asymp
R^3(\log R)^{3/2},
\]

choosing `C alpha<2` yields

\[
\boxed{
\int_{B_{L_R}}|S-\bar S|^2=o(L_R^3),
\qquad
\int_{B_{L_R}}|\Omega-\bar\Omega|^2=o(L_R^3).
}
\]

Thus the quadratic DSD residual is negligible compared with the enlarged coherent volume.

## 3. Polynomial stability leaves one cubic residual obstruction

Write

\[
\delta S=S-\bar S,
\qquad
\delta\Omega=\Omega-\bar\Omega.
\]

The vorticity-stretching polynomial obeys, using the first-hitting bound `|Omega|<=1` and bounded `bar S`,

\[
|\Omega\cdot S\Omega-
\bar\Omega\cdot\bar S\bar\Omega|
\lesssim
|\delta S|+|\delta\Omega|+|\delta\Omega|^2.
\]

For the determinant,

\[
|\det S-\det\bar S|
\lesssim
|\delta S|+|\delta S|^2+|\delta S|^3
\]

with constants depending only on the bounded affine reference.

The `L^1` and `L^2` error contributions are `o(L_R^3)` by Cauchy--Schwarz and Section 2.

Therefore either

\[
\boxed{
\int_{B_{L_R}}|\delta S|^3dx
\gtrsim L_R^3,
}
\]

or the actual Betchov mismatch retains the affine positive sign in integral form:

\[
\boxed{
\int_{B_{L_R}}
(\Omega\cdot S\Omega+4\det S)dx
\gtrsim L_R^3.
}
\]

The first alternative is a macroscopic critical cubic residual-strain concentration. It is already outside the minimal bounded-residual affine branch and can be routed to the existing scale-local/high-derivative machinery.

## 4. Local Betchov mismatch at the enlarged radius

Assume the cubic residual alternative is absent. Take a cutoff `chi_{L_R}` equal to one on `B_{L_R}` and supported in `B_{2L_R}`.

The exact local Betchov divergence identity gives

\[
\int\chi_{L_R}
(\Omega\cdot S\Omega+4\det S)dx
=-\frac43\int\nabla\chi_{L_R}\cdot\mathcal F_A dx.
\]

The established global bound on the cutoff flux is

\[
\left|\int\nabla\chi_{L_R}\cdot\mathcal F_A dx\right|
\lesssim
L_R^{-1}E^{5/4}P^{1/4},
\]

where

\[
E=\|\Omega\|_2^2,
\qquad
P=\|\nabla\Omega\|_2^2.
\]

Hence

\[
L_R^3
\lesssim
L_R^{-1}E^{5/4}P^{1/4}.
\]

Equivalently,

\[
\boxed{
P
\gtrsim
\frac{L_R^{16}}{E^5}.
}
\]

## 5. Reservoir-or-palinstrophy form

If the global/nearby enstrophy is not parametrically larger than the enlarged coherent core,

\[
E\lesssim C_E L_R^3,
\]

then

\[
P
\gtrsim
c_{C_E}L_R.
\]

Since

\[
L_R\asymp R\sqrt{\log R},
\]

we obtain

\[
\boxed{
P
\gtrsim
cR\sqrt{\log R}.
}
\]

Conversely, avoiding this palinstrophy price requires

\[
\boxed{
E\gg L_R^3
\asymp
R^3(\log R)^{3/2},
}
\]

which is an explicit external-enstrophy-reservoir branch.

Thus the aligned `lambda_2<=0` critical ramp obeys the trichotomy

\[
\boxed{
\text{macroscopic cubic residual strain}
\quad\lor\quad
\text{external enstrophy reservoir}
\quad\lor\quad
P\gtrsim R\sqrt{\log R}.
}
\]

## 6. Relation to the `lambda_2>0` branch

The aligned critical ramp already has the elementary shape dichotomy

\[
\bar\lambda_2>0
\quad\lor\quad
\bar\lambda_2\le0.
\]

The first side is the productive positive-middle-strain branch and now pays a logarithmic critical `L_t^2L_x^3` action.

The second side is the present Betchov branch and is no longer a free boundary-flux escape: low Gaussian variance pushes it to one of

1. cubic residual-strain concentration;
2. a parametrically larger exterior enstrophy reservoir;
3. logarithmically strengthened palinstrophy.

## 7. Limitation

Neither large palinstrophy nor a large exterior enstrophy reservoir is presently forbidden near a hypothetical singularity. The value of the result is structural: exterior Betchov compensation cannot remain an untyped local boundary term on the critical fixed-point branch.

The remaining target is the reservoir branch. One must determine whether an exterior reservoir large enough to avoid the palinstrophy bound can be recursively transferred across the decreasing physical scales of a first-hitting cascade without generating a critical `L^3`, positive-middle-strain, or scale-local residual packing contradiction.

Status: **BETCHOV EXTERIOR COMPENSATION TYPED INTO CUBIC RESIDUAL / LARGE EXTERNAL ENSTROPHY RESERVOIR / `R sqrt(log R)` PALINSTROPHY / RESERVOIR RECURSION REMAINS OPEN / GLOBAL REGULARITY NOT PROVED.**