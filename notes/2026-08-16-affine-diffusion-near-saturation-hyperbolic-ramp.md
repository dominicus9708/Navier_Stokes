# Affine deformation-diffusion near saturation forces a hyperbolic strain ramp

Date: 2026-08-16

Status: **DERIVED SCALAR SATURATION RIGIDITY FOR THE AFFINE DEFORMATION--DIFFUSION PRODUCT. THE CRITICAL `q~R^2`, CORE-COVARIANCE, MINIMAL-STRAIN BRANCH CONCENTRATES ITS ACTUAL LARGE DEFORMATION ON AN `O(R)` TURNOVER-TIME RAMP WITH RICCATI/HYPERBOLIC PROFILE. GLOBAL REGULARITY NOT PROVED.**

## 1. Track a compressed covector

Fix a source time `s` and terminal time `T`. Let

\[
F(t,s)
\]

solve

\[
\partial_tF=L(t)F,
\qquad F(s,s)=I,
\qquad \operatorname{tr}L=0.
\]

Let

\[
q=\|F(T,s)\|_{op}\gg1.
\]

Because `det F=1`, the smallest singular value satisfies

\[
\sigma_{\min}(F(T,s))\le q^{-1/2}.
\]

Choose a unit vector `v` in a maximally expanded direction of `F(T,s)^(-T)` and set

\[
w(t)=F(t,s)^{-T}v,
\qquad
y(t)=|w(t)|,
\qquad
h(t)=\log y(t).
\]

Then

\[
y(s)=1,
\qquad
y(T)\ge q^{1/2}.
\]

## 2. Exact logarithmic derivative

Write

\[
L=S+A,
\qquad S^T=S,
\qquad A^T=-A.
\]

Since

\[
w'= -L^Tw=(-S+A)w,
\]

with

\[
n=w/|w|,
\]

we have exactly

\[
\boxed{
h'(t)=-n(t)^TS(t)n(t).}
\]

Hence

\[
\boxed{|h'(t)|\le\|S(t)\|_{op}.}
\]

Let

\[
\mathcal J_S=\int_s^T\|S(t)\|_{op}^2dt.
\]

Then

\[
\int_s^T h'(t)^2dt\le\mathcal J_S.
\]

## 3. Covariance in the tracked direction

The pulled-back affine heat matrix is

\[
C(T,s)
=\int_s^T F(t,s)^{-1}F(t,s)^{-T}dt.
\]

Therefore

\[
\boxed{
C_v
:=v^TC(T,s)v
=\int_s^T y(t)^2dt.
}
\]

Since

\[
y'=yh',
\]

\[
y(T)-1
=\int_s^T y(t)h'(t)dt.
\]

Cauchy--Schwarz yields the exact scalar deformation--diffusion product

\[
\boxed{
C_v
\int_s^T h'(t)^2dt
\ge
(y(T)-1)^2.
}
\]

Consequently

\[
\boxed{
C_v\mathcal J_S
\ge
(y(T)-1)^2
\gtrsim q.
}
\]

This is the one-dimensional core of the matrix two-axis diffusion lower bound.

## 4. Equality and near-equality profile

Let

\[
A=C_v=\int y^2dt,
\qquad
B_h=\int h'^2dt,
\qquad
D=y(T)-1.
\]

The Cauchy defect is

\[
AB_h-D^2\ge0.
\]

Set

\[
c=\frac{D}{A}.
\]

Then exactly

\[
\boxed{
\int_s^T|h'(t)-c\,y(t)|^2dt
=B_h-rac{D^2}{A}.
}
\]

Thus if the scalar product is near saturated,

\[
AB_h\le(1+\delta)D^2,
\]

then

\[
\boxed{
\|h'-c e^h\|_{L^2(s,T)}^2
\le
\delta\frac{D^2}{A}.
}
\]

At exact equality,

\[
\boxed{h'=c e^h,}
\]

or equivalently

\[
\boxed{y'=c y^2.}
\]

Hence

\[
\boxed{
\frac1{y(t)}
=
1-c(t-s)
}
\]

until the prescribed finite endpoint value is reached. The minimum-diffusion deformation history is therefore hyperbolic/Riccati rather than a constant-rate exponential strain.

## 5. Duration of the exact saturating ramp

For the equality profile, if

\[
Y=y(T),
\]

then

\[
A=\frac{Y-1}{c},
\qquad
B_h=c(Y-1),
\]

and the ramp duration is

\[
\boxed{
\Delta t
=T-s
=\frac{1-Y^{-1}}{c}
=A\frac{1-Y^{-1}}{Y-1}.
}
\]

For large `Y`,

\[
\boxed{
\Delta t\asymp\frac{A}{Y}.
}
\]

## 6. Evaluate the critical residual-seed saturation

The `R^-2` pinning theorem identifies the minimally escaping scale

\[
\mathcal B_R\asymp R^{-2},
\qquad
q\asymp R^2.
\]

On the core-covariance, minimal-strain branch assume the relevant covariance direction satisfies

\[
C_v\asymp R^2
\]

and

\[
\mathcal J_S\asymp1.
\]

Then

\[
Y\asymp q^{1/2}\asymp R,
\]

and the saturating coefficient is

\[
\boxed{c\asymp R^{-1}.}
\]

The actual large-deformation ramp occupies

\[
\boxed{
\Delta t_{\rm ramp}\asymp R.
}
\]

This is parametrically shorter than the `R^2` parabolic source horizon but exactly comparable to the residual turnover time already identified in the fast-rotation analysis.

The strain rate along the compressed covector grows from

\[
h'\sim R^{-1}
\]

to order one across this ramp.

## 7. Near saturation versus excess branch

If the actual deformation--diffusion product is not close to equality, then at least one of

\[
C_v
\quad\text{or}\quad
\mathcal J_S
\]

is larger than its critical value by a definite factor. These are already charged as

- Gaussian spatial/covariance escape, or
- excess affine strain-energy.

Therefore a genuinely minimal survivor must not only satisfy the exponent pinning

\[
\mathcal B_R\sim R^{-2},
\]

but also approach the Cauchy saturation geometry above.

## 8. Interaction with coherent rotation

The tracked unit covector obeys

\[
\boxed{
n'
=A n-Sn+(n^TSn)n.}
\]

Near scalar saturation also requires

\[
-n^TSn\approx\|S\|_{op}
\]

through the active ramp. Hence `n` must remain close to a most-compressive strain direction while the skew part `A` rotates material directions.

On the coherent crossing branch, the skew rotation is order one while the ramp lasts `O(R)` normalized time. Thus the minimum survivor requires a **frame-locking mechanism** between coherent rotation and the compressive eigenspace of `S` over `O(R)` rotations/turnover time.

There are two obvious ways to avoid rapid misalignment:

1. the relevant compressive eigenspace is rotationally degenerate (the axial/uniaxial geometry);
2. the strain eigenframe itself co-rotates, which requires time-dependent strain orientation/modulation.

The first connects directly to the previously derived local Betchov axial-extension mismatch. The second returns to time-modulation/high-derivative/projective channels.

This final geometric routing is not yet a theorem: a quantitative stability estimate linking Cauchy near-saturation to eigenframe locking still has to be proved.

Status: **CRITICAL SCALAR AFFINE SATURATION RIGIDIFIED TO AN `O(R)` HYPERBOLIC RAMP / NEXT TARGET = QUANTITATIVE FRAME-LOCKING: AXIAL DEGENERACY OR TIME-MODULATED STRAIN EIGENFRAME.**
