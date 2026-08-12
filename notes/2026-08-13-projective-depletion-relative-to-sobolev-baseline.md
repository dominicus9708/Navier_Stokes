# Projective depletion relative to the generic Sobolev baseline

Date: 2026-08-13

Status: **DERIVED DYADIC BASELINE + DEPLETION RATIO / OPEN AUTOMATIC DEPLETION**.

This note identifies the generic no-extra-geometry size of the dyadic projective spectrum and shows that optimizing the resulting near/far split reproduces the standard enstrophy estimate

\[
|Q|\lesssim E^{3/4}P^{3/4}.
\]

This gives a quantitative baseline against which genuine directional/projective depletion can be measured.

## 1. Notation

Let

\[
E=\|\omega\|_2^2,
\qquad
P=\|\nabla\omega\|_2^2,
\]

and let

\[
P_j^{\rm pair}
=\iint_{A_j}
|\omega(x)\times\omega(y)|^2dxdy
\]

on the dyadic shell

\[
A_j=\{r_{j+1}<|x-y|\le r_j\}.
\]

Define

\[
\mathfrak P_j
=r_j^{-3}P_j^{\rm pair}.
\]

The dyadic geometric stretching estimate is

\[
|Q_j|
\lesssim
E^{1/2}\mathfrak P_j^{1/2}.
\]

## 2. Translation identity for the cross-axis factor

Write `y=x+h`. Since

\[
\omega(x)\times\omega(x)=0,
\]

we have

\[
\boxed{
\omega(x)\times\omega(x+h)
=
\omega(x)\times
[\omega(x+h)-\omega(x)].
}
\]

Therefore

\[
|\omega(x)\times\omega(x+h)|
\le
|\omega(x)|\,|\delta_h\omega(x)|,
\]

where

\[
\delta_h\omega(x)=\omega(x+h)-\omega(x).
\]

## 3. Generic `H^1` pairwise bound

For fixed `h`, Holder gives

\[
\int
|\omega|^2|\delta_h\omega|^2dx
\le
\|\omega\|_6^2
\|\delta_h\omega\|_3^2.
\]

Sobolev yields

\[
\|\omega\|_6
\lesssim
P^{1/2}.
\]

For the translation increment,

\[
\|\delta_h\omega\|_2
\le
|h|\|\nabla\omega\|_2
=|h|P^{1/2},
\]

while the triangle inequality and Sobolev give

\[
\|\delta_h\omega\|_6
\le2\|\omega\|_6
\lesssim P^{1/2}.
\]

Interpolate `L^3` between `L^2` and `L^6`:

\[
\|\delta_h\omega\|_3
\le
\|\delta_h\omega\|_2^{1/2}
\|\delta_h\omega\|_6^{1/2}
\lesssim
|h|^{1/2}P^{1/2}.
\]

Hence

\[
\boxed{
\int
|\omega(x)\times\omega(x+h)|^2dx
\lesssim
|h|P^2.
}
\]

## 4. Integrate over a dyadic shell

The shell in `h` has volume comparable to `r_j^3`, and `|h|\sim r_j`. Therefore

\[
P_j^{\rm pair}
\lesssim
r_j^4P^2.
\]

Thus

\[
\boxed{
\mathfrak P_j
\lesssim
r_jP^2.
}
\]

This is the generic `H^1` baseline. It uses no special vorticity-direction coherence beyond the algebraic fact that the cross product vanishes at zero separation.

## 5. Recover the standard near-field estimate

Using the dyadic stretching bound,

\[
|Q_j|
\lesssim
E^{1/2}r_j^{1/2}P.
\]

Summing over `r_j<=R`,

\[
\sum_{j\ge0}r_j^{1/2}
\lesssim R^{1/2}.
\]

Therefore

\[
\boxed{
|Q_{\rm near}|
\lesssim
E^{1/2}PR^{1/2}.
}
\]

## 6. Far-field estimate

Outside radius `R`, ignore the angular depletion and use Cauchy--Schwarz in the displacement variable:

\[
\int_{|h|>R}
\frac{|\omega(x+h)|}{|h|^3}dh
\le
\left(
\int_{|h|>R}|h|^{-6}dh
\right)^{1/2}
\|\omega\|_2.
\]

Since

\[
\int_{|h|>R}|h|^{-6}dh
\sim R^{-3},
\]

we obtain

\[
\boxed{
|Q_{\rm far}|
\lesssim
E^{3/2}R^{-3/2}.
}
\]

## 7. Optimize the split radius

Combine the bounds:

\[
|Q|
\lesssim
E^{1/2}PR^{1/2}
+E^{3/2}R^{-3/2}.
\]

Balancing the two terms gives

\[
R^2\sim E/P.
\]

Hence

\[
\boxed{
|Q|
\lesssim
E^{3/4}P^{3/4}.
}
\]

This is exactly the familiar scale-critical enstrophy-production estimate. Therefore the dyadic projective formalism is consistent with standard Sobolev theory when no additional geometric depletion is inserted.

## 8. Define the projective depletion ratio

The generic baseline suggests the dimensionless shell quantity

\[
\boxed{
\delta_j
=
\frac{\mathfrak P_j}{r_jP^2}
}
\]

whenever `P>0`.

Generic `H^1` control gives only

\[
\delta_j\lesssim1.
\]

Values

\[
\delta_j\ll1
\]

measure genuine projective depletion beyond the generic translation/Sobolev cancellation.

Using `delta_j`,

\[
\boxed{
|Q_{\rm near}|
\lesssim
E^{1/2}P
\sum_{r_j\le R}
r_j^{1/2}\delta_j^{1/2}.
}
\]

Define the dimensionless dyadic depletion aggregate

\[
\boxed{
\mathcal A_R
=R^{-1/2}
\sum_{r_j\le R}
r_j^{1/2}\delta_j^{1/2}.
}
\]

Then

\[
\boxed{
|Q_{\rm near}|
\lesssim
E^{1/2}PR^{1/2}\mathcal A_R.
}
\]

The generic theory only gives `A_R=O(1)`.

## 9. Improved source if the aggregate depletion is small

For a fixed value of the depletion aggregate, balancing

\[
E^{1/2}P\mathcal A_R R^{1/2}
\]

against

\[
E^{3/2}R^{-3/2}
\]

gives schematically

\[
R^2\sim\frac{E}{P\mathcal A_R}.
\]

At such a compatible scale,

\[
\boxed{
|Q|
\lesssim
E^{3/4}P^{3/4}\mathcal A_R^{3/4}.
}
\]

Because `A_R` itself depends on `R`, this is an implicit optimized majorant, not a closed universal inequality with a freely chosen scalar parameter.

The useful structural point is:

\[
\boxed{
\mathcal A_R\ll1
\Longrightarrow
\text{strict depletion relative to the standard }E^{3/4}P^{3/4}\text{ source}.
}
\]

## 10. Connect to smooth covariance data

At comparable scale,

\[
\mathfrak P_j
\lesssim
\mathcal P_{c r_j},
\]

where

\[
\mathcal P_r=\int E_r^2J_r.
\]

Thus a smooth-kernel version of the depletion ratio is

\[
\boxed{
\delta_r^{\rm smooth}
=\frac{\mathcal P_r}{rP^2}.
}
\]

This is a directly computable DSD/static-aggregation descriptor:

- numerator: scale-`r` pairwise multi-axis enstrophy content;
- denominator: generic `H^1` projective baseline at the same scale.

## 11. Residual singularity interpretation

A residual singularity must now evade two possibilities:

1. **projective depletion:** `delta_j` becomes small enough on the active shells to weaken vortex stretching;
2. **projective viscous dissipation:** if the derivative-level projective defect remains substantial, the energy-weighted covariance inequality imposes a coercive cost.

Therefore the difficult regime is one where

- the dyadic pairwise projective spectrum stays near its generic `H^1` baseline on dangerous physical scales,
- while the derivative covariance chain simultaneously supplies enough nonlinear forcing to overcome projective viscosity.

The next target is to combine `delta_j` with the intense-vorticity occupancy/sparseness channels, asking whether a shell can remain both geometrically nondepleted and spatially concentrated without triggering an existing regularity gate.

Status: **OPEN OCCUPANCY--PROJECTIVE DEPLETION INTERSECTION**.
