# Dyadic projective bound for the vortex-stretching source

Date: 2026-08-13

Status: **DERIVED FROM THE CLASSICAL VORTICITY-DIRECTION STRETCHING REPRESENTATION / OPEN AUTOMATIC SUMMABILITY**.

This note connects the physical-scale index directly to the local pairwise projective covariance channel.

External anchor: the Constantin--Fefferman vorticity-direction approach rewrites the vortex-stretching scalar using a singular kernel and a determinant/angle factor involving the vorticity directions at two points. A convenient published statement of the formula is also given in Luigi C. Berselli, *On the vorticity direction and the regularity of 3D Navier--Stokes equations*, Nonlinearity 36 (2023), 4303--4313.

The shell estimate below is an elementary consequence of that representation and Cauchy--Schwarz.

## 1. Classical geometric stretching representation

Let

\[
\xi(x)=\omega(x)/|\omega(x)|
\]

where `omega(x) != 0`.

The stretching eigenvalue admits the principal-value representation

\[
\xi(x)\cdot S(x)\xi(x)
=\frac{3}{4\pi}\,\mathrm{p.v.}
\int_{\mathbb R^3}
\frac{
(\widehat h\cdot\xi(x))
\det(\widehat h,\xi(x),\xi(x+h))
}{|h|^3}
|\omega(x+h)|dh.
\]

The determinant is bounded by the sine of the projective angle between the vorticity directions:

\[
|\det(\widehat h,\xi(x),\xi(x+h))|
\le
|\xi(x)\times\xi(x+h)|.
\]

Therefore the pointwise stretching magnitude satisfies schematically

\[
\boxed{
|\omega\cdot S\omega|(x)
\lesssim
|\omega(x)|^2
\int
\frac{|\omega(y)|\,|\xi(x)\times\xi(y)|}{|x-y|^3}dy.
}
\]

Equivalently,

\[
\boxed{
|\omega\cdot S\omega|(x)
\lesssim
|\omega(x)|
\int
\frac{|\omega(x)\times\omega(y)|}{|x-y|^3}dy.
}
\]

This form is sign-invariant under `omega -> -omega` at either point.

## 2. Dyadic physical shells

Fix an outer scale `R>0` and define

\[
r_j=2^{-j}R,
\qquad j=0,1,2,\ldots
\]

and

\[
\boxed{
A_j
=\{(x,y):r_{j+1}<|x-y|\le r_j\}.
}
\]

Define the raw shell pairwise projective content

\[
P_j
=\iint_{A_j}
|\omega(x)\times\omega(y)|^2dxdy,
\]

and its critical kernel-weighted version

\[
\boxed{
\mathfrak P_j
=r_j^{-3}P_j.
}
\]

Because `P_j` scales like `lambda^2` while `r_j^-3` scales like `lambda^3`,

\[
\mathfrak P_j
\mapsto\lambda^5\mathfrak P_j.
\]

Thus

\[
\mathfrak P_j^{1/2}
\]

has the same Navier--Stokes scaling as `||S omega||_2`.

## 3. Shell stretching estimate

Let `Q_j` be the contribution of shell `A_j` to the integrated stretching scalar

\[
Q=\int\omega\cdot S\omega dx.
\]

On `A_j`,

\[
|x-y|^{-3}\lesssim r_j^{-3}.
\]

Hence

\[
|Q_j|
\lesssim
r_j^{-3}
\iint_{A_j}
|\omega(x)|
|\omega(x)\times\omega(y)|dxdy.
\]

Cauchy--Schwarz gives

\[
\begin{aligned}
|Q_j|
&\lesssim
r_j^{-3}
P_j^{1/2}
\left(
\iint_{A_j}|\omega(x)|^2dxdy
\right)^{1/2}.
\end{aligned}
\]

For every fixed `x`, the allowed `y` shell has volume comparable to `r_j^3`. Therefore

\[
\iint_{A_j}|\omega(x)|^2dxdy
\lesssim r_j^3E,
\qquad
E=\|\omega\|_2^2.
\]

Thus

\[
\boxed{
|Q_j|
\lesssim
E^{1/2}\,
\mathfrak P_j^{1/2}.
}
\]

This is the direct scale-by-scale bridge between the projective pair channel and vortex stretching.

## 4. Relation to the smooth local covariance spectrum

The previous smooth local covariance channel was

\[
\mathcal P_r
=\int E_r(z)^2J_r(z)dz
=\iint K_r(x-y)
|\omega(x)\times\omega(y)|^2dxdy,
\]

with

\[
K_r=\eta_r*\eta_r.
\]

For the positive Student-type kernel used in the local covariance lemma,

\[
K_r(h)
=r^{-3}K_1(h/r),
\]

and `K_1` is positive and continuous.

Consequently, on any fixed annular ratio

\[
c_1r\le|h|\le c_2r,
\]

there is a kernel-dependent constant `c>0` such that

\[
K_r(h)\ge c r^{-3}.
\]

Therefore the critical shell content is controlled by the smooth covariance spectrum at a comparable scale:

\[
\boxed{
\mathfrak P_j
\lesssim
\mathcal P_{c r_j}
}
\]

for a fixed scale-comparison constant `c` determined by the kernel convention.

Hence

\[
\boxed{
|Q_j|
\lesssim
E^{1/2}\,
\mathcal P_{c r_j}^{1/2}.
}
\]

## 5. Near-field dyadic sum

For the near field `|x-y|<=R`, formally summing the shell estimates gives

\[
\boxed{
|Q_{\rm near}|
\lesssim
E^{1/2}
\sum_{j\ge0}
\mathfrak P_j^{1/2}
\lesssim
E^{1/2}
\sum_{j\ge0}
\mathcal P_{c r_j}^{1/2}.
}
\]

This is a sufficient majorant, not an assertion that the series is automatically finite.

## 6. Why there is no automatic shell decay

The criticality is explicit:

- strain kernel on shell: `r_j^-3`;
- shell volume: `r_j^3`.

These cancel at leading order.

Therefore the estimate does not gain a geometric factor `2^{-epsilon j}` automatically. Summability must come from improved small-scale projective alignment or from a more refined cancellation argument.

This reproduces, in the covariance language, why classical vorticity-direction criteria impose scale-dependent coherence and why logarithmic/BMO refinements are relevant at the borderline.

## 7. A projective dyadic sufficient condition

If on a time interval the far-field part is controlled separately and

\[
\boxed{
\int_0^T
E(t)^{1/2}
\sum_{j\ge0}
\mathcal P_{c r_j}(t)^{1/2}
\,dt
<\infty,
}
\]

then the near-field contribution to the total enstrophy stretching is integrable in time.

This is only a **conditional geometric criterion**. No claim is made that finite-energy Navier--Stokes solutions automatically satisfy the dyadic sum.

## 8. Relation to established coherence criteria

A pointwise bound such as

\[
|\sin\angle(\xi(x),\xi(y))|
\lesssim |x-y|^{1/2}
\]

on high-vorticity regions is known to deplete vortex stretching sufficiently for regularity in the Constantin--Fefferman / Beirao da Veiga--Berselli line of results.

The current covariance channel is different in form: it records an **enstrophy-weighted average squared projective mismatch** rather than a pointwise Hölder modulus.

Therefore it must not be claimed to imply those classical hypotheses without an additional concentration/measure argument.

The useful question is whether the averaged shell spectrum can be combined with the already derived occupancy/sparseness constraints so that a large mismatch cannot hide on a small but dynamically dangerous subset.

## 9. Current open target

The new joint physical-scale / axis descriptor is

\[
\boxed{
\mathcal G_j(t)
=E(t)^{1/2}\mathcal P_{c r_j}(t)^{1/2}.
}
\]

A residual singularity must make the sum of these near-field geometric stretching channels nonintegrable, while simultaneously evading

- line-sparseness regularity,
- local covariance-axis alignment,
- direction-gradient diffusion,
- middle-strain-eigenvalue criteria,
- and the projective derivative dissipation chain.

The next target is an **occupancy-weighted dyadic projective inequality**: split each shell into intense and non-intense vorticity sectors and determine whether the dangerous part of `P_j` can be controlled by the local enstrophy/occupancy channels already present in the route.

Status: **OPEN OCCUPANCY-WEIGHTED DYADIC PROJECTIVE CLOSURE**.
