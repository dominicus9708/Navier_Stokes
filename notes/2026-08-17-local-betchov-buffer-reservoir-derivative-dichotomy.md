# Local Betchov buffer: strain-reservoir or derivative dichotomy

Date: 2026-08-17

Status: **DERIVED LOCALIZATION IMPROVEMENT. THE EARLIER CUTOFF BETCHOV BOUND USED WHOLE-SPACE ENSTROPHY/PALINSTROPHY AND THEREFORE ALLOWED A REMOTE RESERVOIR TO ARTIFICIALLY WEAKEN THE ESTIMATE. USING THE TRANSLATION FREEDOM OF THE BETCHOV FLUX AND LOCAL POINCARE--SOBOLEV, COMPENSATION IS FORCED INTO THE SAME `O(L)` BUFFER ANNULUS: EITHER LOCAL GRADIENT ENERGY `>=cL^3` OR LOCAL SECOND-GRADIENT ENERGY `>=cL`. GLOBAL REGULARITY NOT PROVED.**

## 1. Translation freedom of the exact Betchov flux

Let

\[
A=\nabla u.
\]

For any constant vector `c`, the shifted field

\[
v=u-c
\]

has the same gradient `A` and remains divergence free.

The exact Betchov flux construction applied to `v` therefore satisfies

\[
\boxed{
\nabla\cdot\mathcal F_A(v)
=\operatorname{tr}(A^3).
}
\]

Thus the local divergence identity may be written with `u-c` rather than `u`:

\[
\boxed{
\omega\cdot S\omega+4\det S
=\frac43\nabla\cdot\mathcal F_A(u-c).
}
\]

This removes an irrelevant common translational velocity from the boundary-flux estimate.

## 2. Cutoff and local annulus

Let `chi_L` equal one on `B_L`, vanish outside `B_{2L}`, and satisfy

\[
|\nabla\chi_L|\lesssim L^{-1}.
\]

Let a slightly enlarged buffer annulus be

\[
A_L^*
=\{x:L/2<|x-x_*|<4L\}.
\]

Choose `c` to be the average of `u` on a fixed Lipschitz annular domain comparable to `A_L^*`.

Then

\[
\left|
\int\nabla\chi_L\cdot\mathcal F_A(u-c)dx
\right|
\lesssim
L^{-1}
\int_{A_L^*}|u-c||A|^2dx.
\]

Define the local buffer quantities

\[
\boxed{
e_L:=\int_{A_L^*}|A|^2dx,}
\]

\[
\boxed{p_L:=\int_{A_L^*}|\nabla A|^2dx.}
\]

## 3. Local Poincare--Sobolev

Scale-invariant Poincare--Sobolev on the annulus gives

\[
\boxed{
\|u-c\|_{L^6(A_L^*)}
\lesssim
e_L^{1/2}.
}
\]

For the gradient field `A`, local Sobolev with a cutoff gives

\[
\boxed{
\|A\|_{L^6(A_L^*)}
\lesssim
p_L^{1/2}+L^{-1}e_L^{1/2}.
}
\]

Interpolation between `L^2` and `L^6` gives

\[
\|A\|_{L^{12/5}}
\lesssim
\|A\|_2^{3/4}\|A\|_6^{1/4}.
\]

Therefore

\[
\|A\|_{12/5}^2
\lesssim
 e_L^{3/4}
\left(
p_L^{1/2}+L^{-1}e_L^{1/2}
\right)^{1/2}.
\]

Using Holder with exponents `6,12/5,12/5`,

\[
\begin{aligned}
\left|
\int\nabla\chi_L\cdot\mathcal F_A dx
\right|
&\lesssim
L^{-1}
\|u-c\|_6
\|A\|_{12/5}^2\\
&\lesssim
L^{-1}e_L^{5/4}
\left(
p_L^{1/2}+L^{-1}e_L^{1/2}
\right)^{1/2}.
\end{aligned}
\]

Using `sqrt(a+b)<=sqrt(a)+sqrt(b)` yields the explicit local form

\[
\boxed{
\left|
\int\nabla\chi_L\cdot\mathcal F_A dx
\right|
\lesssim
L^{-1}e_L^{5/4}p_L^{1/4}
+
L^{-3/2}e_L^{3/2}.
}
\]

No whole-space `E` appears.

## 4. Apply to a positive coherent mismatch

Suppose the inner coherent region has the lower bound

\[
\boxed{
\int\chi_L
(\omega\cdot S\omega+4\det S)dx
\ge c_0L^3.
}
\]

The exact divergence identity and Section 3 give

\[
L^3
\lesssim
L^{-1}e_L^{5/4}p_L^{1/4}
+
L^{-3/2}e_L^{3/2}.
\]

Introduce dimensionless buffer densities

\[
z=\frac{e_L}{L^3},
\qquad
w=\frac{p_L}{L}.
\]

Then

\[
\boxed{
1
\lesssim
z^{5/4}w^{1/4}+z^{3/2}.
}
\]

Consequently there is a universal `c>0` such that

\[
\boxed{
z\ge c
\quad\lor\quad
w\ge c.}
\]

Equivalently,

\[
\boxed{
 e_L\gtrsim L^3
\quad\lor\quad
 p_L\gtrsim L.
}
\]

## 5. Insert the logarithmically enlarged coherent radius

On the late coherent low-variance branch, the previous Gaussian-tail argument gives

\[
L=L_R
\asymp
R\sqrt{\log R}.
\]

Hence any surviving aligned `lambda_2<=0` Betchov mismatch must force, in the same physical buffer scale,

\[
\boxed{
 e_{L_R}
\gtrsim
R^3(\log R)^{3/2}
}
\]

or

\[
\boxed{
 p_{L_R}
\gtrsim
R\sqrt{\log R}.
}
\]

The former is a local annular strain/gradient-energy reservoir; the latter is a local Hessian/palinstrophy concentration.

## 6. Why this improves the previous global estimate

The earlier bound

\[
L^3
\lesssim
L^{-1}E^{5/4}P^{1/4}
\]

used whole-space norms. A huge enstrophy reservoir arbitrarily far from the coherent core could make the right-hand side large even though it played no role in the actual cutoff boundary flux.

The present estimate removes that artificial dilution. Compensation must be visible in an `O(L)` neighborhood of the cutoff surface itself.

Thus the old branch

\[
\text{remote external enstrophy reservoir}
\]

is replaced by the genuinely local alternatives

\[
\boxed{
\text{buffer strain-energy reservoir}
\quad\lor\quad
\text{buffer derivative concentration}.
}
\]

## 7. Remaining problem

The derivative alternative is already typed by the high-frequency/palinstrophy machinery.

The new final reservoir question is therefore sharper:

> Can a geometrically shrinking sequence of critical coherent cores repeatedly build an `O(L_j^3)` strain-energy reservoir in their logarithmically enlarged buffer annuli, with moving centers and nested times, without violating the existing Gaussian scale partition, Bessel packing, or a new scale-local energy packing theorem?

That is narrower than the previous whole-space reservoir recursion problem.

Status: **REMOTE RESERVOIR LOOPHOLE REMOVED FROM LOCAL BETCHOV FLUX / COMPENSATION LOCALIZED TO `e_L >= cL^3` OR `p_L >= cL` / BUFFER-ENERGY CROSS-SCALE PACKING IS THE NEW TARGET / GLOBAL REGULARITY NOT PROVED.**