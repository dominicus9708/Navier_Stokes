# Off-axis projective source is quadratic in the off-axis sector: recovery of the critical vorticity Serrin baseline

Date: 2026-08-13

Status: **DERIVED ANISOTROPIC SOURCE BOUND / RECOVERS STANDARD CRITICAL VORTICITY REGULARITY SCALE**.

This note improves the crude source estimate

\[
\sqrt O\,\|S\omega\|_2
\]

for the optimal off-axis enstrophy by using the constant-axis decomposition and the fact that `S n` is a zero-order singular-integral transform of the off-axis vorticity.

The resulting coefficient reproduces the standard critical vorticity Serrin scaling. This is a consistency/baseline result, not a new global regularity theorem.

## 1. Axis decomposition

Fix a constant spatial unit vector `n` and write

\[
\omega=\alpha n+\beta,
\qquad
\beta\perp n.
\]

Define

\[
O=\|\beta\|_2^2,
\qquad
G=\|\nabla\beta\|_2^2.
\]

The fixed-axis balance is

\[
\frac12\dot O+\nu G
=
\int\beta\cdot S\omega dx.
\]

Because

\[
S\omega=\alpha S n+S\beta,
\]

we have the exact split

\[
\boxed{
\int\beta\cdot S\omega
=
\int\beta\cdot S\beta
+
\int\alpha\,\beta\cdot S n.
}
\]

## 2. `S n` is controlled by the off-axis vorticity in every `L^p`

The Fourier identity established previously gives

\[
4|\widehat{S n}|^2
=|n\times\widehat\omega|^2
\]

pointwise in frequency.

More generally, the Fourier symbol mapping

\[
n\times\omega
\longmapsto
S n
\]

is a homogeneous zero-order smooth matrix multiplier away from the origin. Hence standard Calderon--Zygmund/Mikhlin theory gives, for every

\[
1<p<\infty,
\]

\[
\boxed{
\|S n\|_p
\le C_p\|n\times\omega\|_p
=C_p\|\beta\|_p.
}
\]

Similarly,

\[
\|S\|_p\lesssim_p\|\omega\|_p.
\]

## 3. The `L^3` quadratic off-axis source

For the self-stretching term,

\[
\left|
\int\beta\cdot S\beta
\right|
\le
\|S\|_3\|\beta\|_3^2
\lesssim
\|\omega\|_3\|\beta\|_3^2.
\]

For the axis-conversion term,

\[
\left|
\int\alpha\,\beta\cdot S n
\right|
\le
\|\alpha\|_3\|\beta\|_3\|S n\|_3
\lesssim
\|\omega\|_3\|\beta\|_3^2.
\]

Therefore

\[
\boxed{
\left|
\int\beta\cdot S\omega
\right|
\lesssim
\|\omega\|_3\|\beta\|_3^2.
}
\]

The source is genuinely quadratic in the off-axis sector.

## 4. Interpolate the off-axis factor

In three dimensions,

\[
\|\beta\|_3^2
\le
\|\beta\|_2\|\beta\|_6
\lesssim
O^{1/2}G^{1/2}.
\]

Also

\[
\|\omega\|_3
\le
\|\omega\|_2^{1/2}
\|\omega\|_6^{1/2}
\lesssim
E^{1/4}P^{1/4},
\]

where

\[
E=\|\omega\|_2^2,
\qquad
P=\|\nabla\omega\|_2^2.
\]

Hence

\[
\boxed{
\left|
\int\beta\cdot S\omega
\right|
\lesssim
E^{1/4}P^{1/4}
O^{1/2}G^{1/2}.
}
\]

Young's inequality gives

\[
\boxed{
\dot O+\nu G
\lesssim
\nu^{-1}E^{1/2}P^{1/2}O.
}
\]

For the optimal constant axis, the same inequality holds in the upper-Dini sense.

## 5. Combine with Riccati coercivity

The `H^{-1}` estimate gives

\[
G\ge O^2/U_0,
\qquad
U_0=\|u_0\|_2^2.
\]

Therefore

\[
\boxed{
D_t^+O
+rac{\nu}{U_0}O^2
\lesssim
\nu^{-1}E^{1/2}P^{1/2}O.
}
\]

This is a logistic-type projective inequality.

It shows that, after exact axis decomposition, the aligned state `O=0` has no artificial square-root source. Any growth of the off-axis energy is proportional to the off-axis energy itself, up to the critical coefficient.

## 6. General critical `L^p_tL^q_x` vorticity family

Let

\[
q\ge3,
\qquad
r=\frac{2q}{q-1},
\]

so that

\[
\frac1q+\frac2r=1.
\]

The same two source terms satisfy

\[
\left|
\int\beta\cdot S\omega
\right|
\lesssim_q
\|\omega\|_q\|\beta\|_r^2.
\]

Interpolate `beta` between `L^2` and `L^6`. With

\[
\theta=\frac{3}{2q},
\]

we obtain

\[
\|\beta\|_r^2
\lesssim
O^{1-\theta}G^\theta.
\]

Therefore

\[
|T|
\lesssim
\|\omega\|_q
O^{1-\theta}G^\theta.
\]

Young's inequality absorbs `G` and yields

\[
\boxed{
D_t^+O+\nu G
\lesssim_{q,\nu}
\|\omega\|_q^{p}
O,
}
\]

where

\[
\boxed{
p=\frac1{1-\theta}
=\frac{2q}{2q-3}.}
\]

These exponents satisfy

\[
\boxed{
\frac2p+\frac3q=2,
}
\]

which is precisely the scale-critical vorticity Serrin relation.

Thus

\[
\omega\in L_t^pL_x^q,
\qquad
\frac2p+\frac3q=2,
\qquad q\ge3,
\]

makes the projective growth coefficient integrable and keeps `O` bounded; because `O<=E` and `E in L_t^1`, this yields `O in L_t^2` and feeds the external anisotropic regularity criterion.

This is consistent with established vorticity regularity theory and is not presented as a new criterion.

## 7. What this baseline tells the DSD-assisted route

Two independent reformulations now recover standard critical theory when no extra geometric information is used:

1. the dyadic pairwise projective shell estimate plus the generic `H^1` translation bound recovers

\[
|Q|\lesssim E^{3/4}P^{3/4};
\]

2. the optimal off-axis balance plus generic Calderon--Zygmund/Sobolev interpolation recovers the critical vorticity Serrin family.

Therefore a genuine advance must come from one of the additional structural channels rather than from the reparameterization alone:

- occupancy/sparseness;
- scale-dependent projective depletion below the generic Sobolev baseline;
- local covariance-axis regularity;
- adjoint-window localization;
- derivative-order projective coercivity;
- or a nontrivial interaction among these channels.

Status: **BASELINE RECOVERED — EXTRA GEOMETRIC GAIN STILL REQUIRED**.
