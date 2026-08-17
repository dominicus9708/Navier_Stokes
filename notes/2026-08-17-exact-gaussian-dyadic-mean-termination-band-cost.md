# Exact Gaussian dyadic mean-termination band cost

Date: 2026-08-17

Status: **EXACT FOURIER/GAUSSIAN SCALE IDENTITY. AN ORDER-ONE GAUSSIAN MEAN OF ANY `L^2` FIELD CANNOT DISAPPEAR TOWARD LARGE OBSERVATION SCALES WITHOUT PAYING A POSITIVE DYADIC SCALE-BAND ENERGY OF ORDER `r^3 |mean|^2`. THE BANDS TELESCOPE EXACTLY. THIS TYPES THE TERMINATION OF AN AFFINE/COHERENT EXTERIOR RESERVOIR. GLOBAL REGULARITY NOT PROVED.**

## 1. Gaussian means

Let

\[
g_r(x)
=(2\pi r^2)^{-3/2}
\exp(-|x|^2/(2r^2)),
\]

so

\[
\widehat g_r(\xi)
=e^{-r^2|\xi|^2/2}.
\]

For a scalar, vector, or matrix field `f in L^2(R^3)`, define the Gaussian mean at a fixed center `x_*` by

\[
\boxed{
m_r(x_*)=(g_r*f)(x_*).}
\]

We compare two consecutive dyadic means,

\[
D_r:=m_r-m_{2r}.
\]

Its Fourier multiplier is

\[
\boxed{
w_r(\xi)
=e^{-r^2|\xi|^2/2}
-e^{-2r^2|\xi|^2}.}
\]

This is nonnegative.

## 2. Pointwise mean change is controlled by a positive band energy

At the fixed center,

\[
D_r(x_*)
=\int e^{ix_*\cdot\xi}
w_r(\xi)\widehat f(\xi)d\xi
\]

(up to the fixed Fourier normalization).

Weighted Cauchy--Schwarz with weight `w_r` gives

\[
|D_r(x_*)|^2
\le
\left(
\int w_r|\widehat f|^2d\xi
\right)
\left(
\int w_r d\xi
\right).
\]

By scaling,

\[
\int w_r d\xi
=C_gr^{-3}.
\]

Define the positive dyadic mean-termination band energy

\[
\boxed{
\mathfrak b_r(f)
:=
\int
\left(
e^{-r^2|\xi|^2/2}
-e^{-2r^2|\xi|^2}
\right)
|\widehat f(\xi)|^2d\xi.
}
\]

Then

\[
\boxed{
r^3|m_r(x_*)-m_{2r}(x_*)|^2
\le
C\mathfrak b_r(f).}
\]

This is a pointwise-to-global scale-band estimate with no derivative remainder.

## 3. Exact dyadic telescoping

Let

\[
r_k=2^kr_0.
\]

Then

\[
\begin{aligned}
w_{r_k}(\xi)
&=e^{-r_k^2|\xi|^2/2}
-e^{-2r_k^2|\xi|^2}\\
&=e^{-r_k^2|\xi|^2/2}
-e^{-r_{k+1}^2|\xi|^2/2}.
\end{aligned}
\]

Therefore

\[
\boxed{
\sum_{k=0}^{N}w_{r_k}(\xi)
=e^{-r_0^2|\xi|^2/2}
-e^{-r_{N+1}^2|\xi|^2/2}.}
\]

As `N->infinity`, the second term vanishes for every `xi !=0`, so

\[
\boxed{
\sum_{k\ge0}\mathfrak b_{r_k}(f)
=
\int e^{-r_0^2|\xi|^2/2}|\widehat f(\xi)|^2d\xi
\le
\|f\|_2^2.}
\]

Thus the mean-termination bands are exactly positive and non-double-counting along one outward dyadic scale ladder.

## 4. Total cost of terminating a nonzero mean

Since `f in L^2`,

\[
|m_r(x_*)|
\le
\|g_r\|_2\|f\|_2
\lesssim
r^{-3/2}\|f\|_2
\to0
\]

as `r->infinity`.

Hence

\[
m_{r_0}
=\sum_{k\ge0}(m_{r_k}-m_{r_{k+1}}).
\]

Weighted Cauchy--Schwarz gives

\[
|m_{r_0}|^2
\le
\left(\sum_{k\ge0}r_k^{-3}\right)
\left(\sum_{k\ge0}r_k^3|D_{r_k}|^2\right).
\]

Because

\[
\sum_{k\ge0}r_k^{-3}
\asymp r_0^{-3},
\]

we obtain

\[
\sum_{k\ge0}r_k^3|D_{r_k}|^2
\gtrsim
r_0^3|m_{r_0}|^2.
\]

Using Section 2,

\[
\boxed{
\sum_{k\ge0}\mathfrak b_{r_k}(f)
\gtrsim
r_0^3|m_{r_0}(x_*)|^2.}
\]

Thus an order-one mean at scale `r_0` must leave at least order `r_0^3` of positive scale-band `L^2` energy before its Gaussian mean can decay to zero at large scales.

## 5. Relation to the existing Gaussian variance partition

The whole-space Gaussian variance is

\[
\mathcal V_f(r)
=\int
(1-e^{-r^2|\xi|^2})|\widehat f|^2d\xi.
\]

The present band can be written exactly as

\[
\boxed{
\mathfrak b_r(f)
=
\mathcal V_f(\sqrt2r)
-
\mathcal V_f(r/\sqrt2).
}
\]

Hence mean termination is not a new unrelated ledger. It occupies a positive finite-width block of the same exact Gaussian scale partition already used for residual fluctuations.

## 6. Apply to strain and vorticity means

At a coherent critical crossing,

\[
|g_R*S(x_*)|\gtrsim1
\]

on an active affine-strain branch and

\[
|g_R*\Omega(x_*)|\gtrsim1.
\]

Applying the theorem to `f=S` or `f=Omega` gives

\[
\boxed{
\sum_{k\ge0}\mathfrak b_{2^kR}(S)
\gtrsim R^3,
}
\]

and

\[
\boxed{
\sum_{k\ge0}\mathfrak b_{2^kR}(\Omega)
\gtrsim R^3.
}
\]

Therefore a finite-energy whole-space field cannot carry an order-one Gaussian affine/coherent mean out to infinity for free. Its eventual termination is automatically recorded in the positive dyadic scale ledger.

## 7. Exterior-compensation interpretation

The local Betchov buffer dichotomy left a possible annular strain-energy reservoir. Such a reservoir can try to be approximately the continuation of the inner affine state rather than a genuinely non-affine buffer.

The present identity shows what happens next:

1. if the mean affine/coherent state changes significantly at some outward dyadic step, that change pays a positive exact scale-band cost;
2. if it does not change, the coherent affine state propagates to a larger observation scale;
3. because `S,Omega in L^2` at every smooth pre-singular time, the Gaussian means must eventually decay to zero;
4. therefore some sequence of outward scale bands must pay a total cost `>=cR^3`.

Thus `affine continuation to the exterior` is not an untyped escape. It is a delayed scale-band expenditure.

## 8. Remaining cross-time issue

This theorem is exact at one physical time and along one outward scale ladder. Different coherent episodes occur at different times, so the same physical frequency bands could in principle be repopulated later.

The existing fixed-frequency reuse theorem already says that a fixed finite frequency block cannot supply the diverging strain action on arbitrarily shrinking singular-tail intervals. The next step is to combine that temporal frequency-drift result with the present exact outward mean-termination bands.

Status: **AFFINE/COHERENT MEAN TERMINATION -> EXACT POSITIVE DYADIC BAND COST / OUTWARD AFFINE CONTINUATION NO LONGER FREE / FINAL ISSUE IS CROSS-TIME REPOPULATION OF MOVING TERMINATION BANDS / GLOBAL REGULARITY NOT PROVED.**