# Vorticity occupancy -> line sparseness bridge

Date: 2026-08-12

Status: **DERIVED GEOMETRIC LEMMA + EXTERNAL REGULARITY ANCHOR + OPEN DYNAMIC OCCUPANCY OBLIGATION**.

This note adds an occupancy/sparseness channel to the multiscale DSD cascade block.  It does not claim a new Navier--Stokes regularity theorem; the final regularity implication is anchored to Grujic's published geometric measure-type criterion.

## 1. Exact volume-to-line geometric lemma

Let `S` be a measurable subset of the ball `B_r(x0)`.  For a unit direction `d`, define the line occupancy through the center

\[
\rho_{\rm line}(d)
=
\frac{
|S\cap\{x_0+s d:-r<s<r\}|_1
}{2r},
\]

where `|.|_1` is one-dimensional Lebesgue measure.

Define the volume occupancy

\[
\rho_{\rm vol}
=
\frac{|S|}{|B_r|}.
\]

Then

\[
\boxed{
\inf_{d\in S^2}\rho_{\rm line}(d)
\le
\rho_{\rm vol}^{1/3}.
}
\]

### Proof

Suppose instead that every line through `x0` has occupancy greater than `delta`, i.e.

\[
|S\cap(x_0-rd,x_0+rd)|_1>2\delta r
\]

for every `d`.

For a fixed line, among subsets of `[-r,r]` of one-dimensional measure `2 delta r`, the weighted second moment

\[
\int 1_S(s)s^2ds
\]

is minimized by the centered interval `[-delta r,delta r]`.  Hence

\[
\int_{-r}^{r}
1_S(x_0+s d)s^2ds
\ge
\frac{2}{3}\delta^3r^3.
\]

Using spherical coordinates in symmetric line form,

\[
|S|
=
\frac12
\int_{S^2}
\int_{-r}^{r}
1_S(x_0+s d)|s|^2ds\,d\sigma(d),
\]

so

\[
|S|
\ge
\frac12(4\pi)\frac23\delta^3r^3
=
\frac{4\pi}{3}\delta^3r^3
=
\delta^3|B_r|.
\]

Contraposition gives the claim.

Thus

\[
\rho_{\rm vol}<\delta^3
\quad\Longrightarrow\quad
\text{there exists a direction that is linearly }\delta\text{-sparse.}
\]

## 2. Apply the lemma to intense vorticity

Let

\[
W(t)=\|\omega(t)\|_\infty
\]

and define the intense-vorticity set at a later comparison time `s` by

\[
S_s(M)
=
\{x:|\omega(x,s)|>M\}.
\]

For a threshold

\[
M=aW(t),
\qquad 0<a<1,
\]

Chebyshev gives, for every ball,

\[
|S_s(M)\cap B_r(x_0)|
\le
\frac{1}{a^2W(t)^2}
\int_{B_r(x_0)}|\omega(x,s)|^2dx.
\]

Define the critical local enstrophy channel

\[
\boxed{
\mathcal W_r(x_0,s)
=r\int_{B_r(x_0)}|\omega(x,s)|^2dx.
}
\]

It is invariant under the Navier--Stokes scaling.

## 3. Natural vorticity/analyticity scale

The vorticity version of Grujic's geometric criterion uses a scale comparable to

\[
r=bW(t)^{-1/2}
\]

for an absolute/theorem-dependent constant `b>0`.

At this scale,

\[
\begin{aligned}
\rho_{\rm vol}
&\le
\frac{
\mathcal W_r/r
}{
a^2W(t)^2(4\pi r^3/3)
}\\
&=
\frac{3}{4\pi a^2b^4}
\mathcal W_r.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathcal W_r
<
\frac{4\pi}{3}a^2b^4\delta^3
\quad\Longrightarrow\quad
\inf_d\rho_{\rm line}(d)<\delta.
}
\]

This converts a scale-critical **local enstrophy size** into the line-sparseness geometry required by the external theorem.

## 4. Global packing corollary

Using the global enstrophy at the comparison time,

\[
\|\omega(s)\|_2^2,
\]

we also have

\[
\rho_{\rm vol}
\le
\frac{3}{4\pi a^2b^3}
\frac{
\|\omega(s)\|_2^2
}{W(t)^{1/2}}.
\]

Hence the scale-invariant packing ratio

\[
\boxed{
\Pi_\omega(t,s)
=
\frac{\|\omega(s)\|_2^2}{\|\omega(t)\|_\infty^{1/2}}
}
\]

is a coarse global sufficient channel: if it is small enough (with the theorem constants), every ball at the natural scale has small enough volume occupancy, hence every point has at least one sparse direction.

This global condition is much stronger than necessary; the local `mathcal W_r` channel is the preferred DSD quantity.

## 5. External regularity anchor

Grujic's geometric measure-type theorem gives both velocity and vorticity versions.  In the vorticity version, near a hypothetical blow-up time, if at suitable later times the intense-vorticity superlevel set is linearly sparse around every spatial point at a scale no larger than the vorticity analyticity radius, the putative singular time is regular.

The present note does **not** reproduce that theorem.  It supplies only the elementary geometric and enstrophy-to-occupancy bridge needed to feed its hypothesis.

Primary source:

- Z. Grujic, *A geometric measure-type regularity criterion for solutions to the 3D Navier-Stokes equations*, arXiv:1111.0217.

## 6. Why vorticity is preferable to velocity for this geometry channel

The moving weighted-sphere proof track subtracts a coherent local translation from velocity.  Velocity superlevel sets change under such a Galilean shift.

Vorticity does not:

\[
\omega=\nabla\times u
=\nabla\times(u-c)
\]

for every spatially constant `c`.

Therefore the vorticity occupancy/sparseness channel is naturally compatible with the moving-center DSD representation.

## 7. DSD typed occupancy block

At each scale, retain

\[
\mathcal O_\omega
=
\bigl(
\mathcal W_r,
\rho_{\rm vol},
\rho_{\rm line,min},
W_\infty,
\xi,\lambda_2^+,\ldots
\bigr).
\]

Interpretation:

- `mathcal W_r`: critical amount of vorticity square in the local region;
- `rho_vol`: fraction of the region occupied by intense vorticity;
- `rho_line,min`: best sparse direction through the observation point;
- `xi`: vorticity direction where defined;
- strain/alignment channels: how the intense set is being amplified or rotated.

These must remain separate.  A small occupied volume does not say how the vorticity direction is aligned, and a coherent direction does not determine occupied volume.

## 8. Cascade consequence

The pressure-cascade locality result showed that an arbitrarily small singular scale must be sustained mainly by nearby scales.

The present result adds a terminal geometric gate:

\[
\boxed{
\text{if the intense-vorticity occupancy becomes sufficiently sparse at the natural }W^{-1/2}\text{ scale, the cascade is regularized.}
}
\]

Therefore a hypothetical singular cascade must simultaneously maintain

1. non-small moving velocity oscillation/dissipation;
2. non-small critical local enstrophy at the vorticity natural scale;
3. enough geometric occupancy to avoid a sparse direction;
4. the required nonlinear strain/vorticity alignment.

This is a stricter structural certificate than energy concentration alone.

## 9. Open dynamic obligation

What is still missing is an a-priori mechanism forcing one of the following before a singular scale is reached:

\[
\mathcal W_r\to0,
\qquad
\rho_{\rm line,min}\to0,
\qquad
\text{or a known alignment/strain regularity gate.}
\]

The global energy inequality supplies time-integrability of enstrophy but does not by itself give the required pointwise-in-time smallness at the dynamic scale.

Status: **OPEN DYNAMIC OCCUPANCY OBLIGATION**.
