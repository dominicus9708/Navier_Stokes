# Gaussian mean-strain Bessel packing over nested episodes

Date: 2026-08-16

Status: **DERIVED SCALE-ORTHOGONAL PACKING FOR THE AFFINE/GAUSSIAN MEAN STRAIN ITSELF, WITH ARBITRARY CENTER MOTION AND ARBITRARY TEMPORAL OVERLAP. THE RESULT REMOVES SCALE DOUBLE COUNTING BUT THE RESULTING PHYSICAL WEIGHTS CAN STILL BE SUMMABLE. GLOBAL REGULARITY NOT PROVED.**

## 1. Gaussian mean strain as an L2 probe

For physical radius `ell>0` and center `x`, let

\[
g_{\ell,x}(y)
=(2\pi\ell^2)^{-3/2}
\exp\left(-\frac{|y-x|^2}{2\ell^2}\right).
\]

Define the Gaussian mean strain

\[
\bar S_{\ell,x}(t)
=\int g_{\ell,x}(y)S(y,t)dy.
\]

Since

\[
\|g_{\ell,x}\|_2
=c_g\ell^{-3/2},
\]

define the normalized probe

\[
p_{\ell,x}
=c_g^{-1}\ell^{3/2}g_{\ell,x},
\qquad
\|p_{\ell,x}\|_2=1.
\]

Then

\[
\boxed{
\ell^{3/2}|\bar S_{\ell,x}|
\asymp
|\langle S,p_{\ell,x}\rangle|.
}
\]

The same statement applies componentwise to the symmetric matrix field `S`.

## 2. Exact Gaussian overlap bound

For two normalized Gaussian probes at scales `ell_j,ell_k` and arbitrary centers `x_j,x_k`, direct Gaussian integration gives

\[
|\langle p_j,p_k\rangle|
\le
C
\frac{(\ell_j\ell_k)^{3/2}}
{(\ell_j^2+\ell_k^2)^{3/2}}.
\]

The center-separation exponential has simply been bounded by one.

If `ell_k<=ell_j`,

\[
\boxed{
|\langle p_j,p_k\rangle|
\lesssim
\left(\frac{\ell_k}{\ell_j}\right)^{3/2}.
}
\]

Hence center motion cannot worsen the cross-scale overlap.

## 3. Geometrically separated scales are uniformly Bessel

Assume

\[
\ell_{j+1}\le\rho\ell_j,
\qquad0<\rho<1.
\]

Then

\[
|\langle p_j,p_k\rangle|
\lesssim
\rho^{3|j-k|/2}.
\]

The Gram matrix has uniformly summable rows, so the Schur test gives

\[
\boxed{
\sum_j|\langle F,p_j\rangle|^2
\le C_\rho\|F\|_2^2
}
\]

for every `F in L2`.

Applying this to each matrix component of `S(t)` yields

\[
\boxed{
\sum_j
\ell_j^3
|\bar S_{\ell_j,x_j}(t)|_F^2
\le
C_\rho\|S(t)\|_2^2.
}
\]

This remains true for arbitrary centers `x_j=x_j(t)` because the overlap estimate is uniform in the centers.

## 4. Arbitrarily nested time intervals

Let `I_j` be the physical active interval for episode `j`. At time `t`, apply the Bessel estimate only to the active subset `j` with `t in I_j`. A subset of a Bessel family has the same bound, so

\[
\boxed{
\sum_j
\mathbf1_{I_j}(t)
\ell_j^3
|\bar S_j(t)|^2
\le
C_\rho\|S(t)\|_2^2.
}
\]

Integrating in time and using Tonelli,

\[
\boxed{
\sum_j
\ell_j^3
\int_{I_j}|\bar S_j(t)|^2dt
\le
C_\rho
\int_0^{T^*}\|S(t)\|_2^2dt
<\infty.
}
\]

Since

\[
\|S\|_2^2=\frac12\|\omega\|_2^2,
\]

the right side is controlled by the finite kinetic-energy dissipation.

Thus temporal nesting does not create an overlap loophole for the Gaussian affine mean strain once scales are separated.

## 5. Consequence of the logarithmic amplifier requirement

Suppose episode `j` lies on the small-residual-seed branch and therefore requires

\[
A_j
:=\int_{I_j}|\bar S_j(t)|dt
\ge c\log R_j.
\]

By Cauchy--Schwarz,

\[
\int_{I_j}|\bar S_j|^2dt
\ge
\frac{A_j^2}{|I_j|}.
\]

Therefore the Bessel packing gives the necessary summability condition

\[
\boxed{
\sum_j
\frac{\ell_j^3(\log R_j)^2}{|I_j|}
<\infty
}
\]

for every geometrically scale-separated surviving affine-amplification subsequence.

On the parabolic critical-saturation branch,

\[
|I_j|\asymp \ell_j^2
\]

up to the already tracked slow/excess-dissipation factor. Hence

\[
\boxed{
\sum_j
\ell_j(\log R_j)^2
<\infty
}
\]

(up to that slow factor) is necessary.

This is an overlap-free global constraint on the repeated logarithmic amplifier.

## 6. Relation to residual scale packing

The residual seed now has the independent exact bridge

\[
r^3B_r(x_*)
\lesssim
\Delta\mathcal B(4r)+r^2P,
\]

and the positive dyadic increments satisfy

\[
\sum_k\Delta\mathcal B(r_k,t)=E(t).
\]

Thus both components of the seed--amplification dichotomy have scale-orthogonal versions:

\[
\boxed{
\text{residual seed}
\to
\text{positive dyadic band or derivative},
}
\]

\[
\boxed{
\text{affine amplification}
\to
\text{Gaussian mean-strain Bessel packing}.
}
\]

The previous scale-overlap problem is therefore substantially reduced.

## 7. Sharpness and remaining wall

The Bessel lower weight is `ell_j`, after using a parabolic interval of length `ell_j^2`.

For the adversarial super-separated power families already constructed in the proof audit, `ell_j` can decrease so rapidly that

\[
\sum_j\ell_j(\log R_j)^2<\infty.
\]

Therefore the Bessel packing is compatible with a hypothetical singular cascade and is not itself a contradiction.

This is nevertheless a significant structural closure: the same physical strain cannot be counted repeatedly at different scales. Any survivor must satisfy an explicit **summability-critical scale collapse** rather than exploiting an overlap loophole.

Status: **AFFINE SCALE REUSE CLOSED BY GAUSSIAN BESSEL PACKING / RESIDUAL SCALE REUSE CLOSED BY POSITIVE DYADIC VARIANCE PACKING / FINAL WALL IS NOW THE POSSIBILITY THAT ALL SCALE-ORTHOGONAL COSTS SHRINK FAST ENOUGH TO BE SUMMABLE.**
