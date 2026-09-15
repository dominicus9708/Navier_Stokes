# M19-310 — The GMS analytic derivative threshold is m>9/4, but interpolated ancient derivative tails remain exactly critical at every order

**Date:** 2026-09-16  
**Status:** ACTIVE GMS REFINEMENT / FRACTIONAL DERIVATIVE THRESHOLD / ALL-ORDER CRITICAL-TAIL FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. M19-255 used m=3 as a sufficient endpoint

The corrected M19-255 argument assumes

\[
u\in L_t^\infty L_x^2,
\qquad
D^m u\in L_{x,t}^2
\]

on a finite physical spacetime region.

Gagliardo--Nirenberg gives

\[
\|u(t)\|_{L^s}
\lesssim
\|u(t)\|_2^{1-a}
\|D^m u(t)\|_2^a,
\qquad
\frac1s=\frac12-\frac{am}{3}.
\]

Choose the exponent so that the derivative factor is directly time-integrable:

\[
as=2.
\]

Then

\[
\boxed{
s=2+\frac{4m}{3}.
}
\]

M19-255 took `m=3`, hence `s=6`.

## 2. Minimal strong-Lp threshold for the logarithmic GMS kernel

The velocity part of the GMS payer is

\[
\int |u-V|^{10/3}\rho^{-5/3}dxdt.
\]

If `u in L^s`, then `|u|^{10/3}` belongs to

\[
L^{3s/10}.
\]

Its Hölder conjugate is

\[
q=\frac{3s}{3s-10}.
\]

The parabolic homogeneous dimension is five, so

\[
\rho^{-5/3}\in L_{loc}^q
\quad\Longleftrightarrow\quad
\frac53 q<5
\quad\Longleftrightarrow\quad
q<3.
\]

The inequality

\[
\frac{3s}{3s-10}<3
\]

is equivalent to

\[
\boxed{s>5.}
\]

Thus the velocity term is strongly integrable whenever

\[
2+\frac{4m}{3}>5,
\]

i.e.

\[
\boxed{m>\frac94.}
\]

## 3. Pressure has the same threshold

For canonical whole-space pressure,

\[
p=R_iR_j(u_i u_j)
\]

up to the standard time-dependent gauge.

If `u in L^s`, Calderon--Zygmund gives

\[
p\in L^{s/2}.
\]

Then

\[
|p|^{5/3}
\in
L^{3s/10},
\]

which is exactly the same exponent as the velocity contribution.

Therefore the pressure part of the weighted payer has the same requirement

\[
\boxed{s>5
\quad\Longleftrightarrow\quad
m>9/4.}
\]

Thus the analytic GMS closure does not intrinsically require three full derivatives.

## 4. Endpoint m=9/4 is genuinely logarithmic

At

\[
m=\frac94,
\]

one has

\[
s=5,
\qquad
q=3.
\]

But

\[
\rho^{-5/3}\notin L^3_{loc}
\]

in parabolic dimension five; it lies exactly at the logarithmic divergence threshold.

Therefore ordinary strong Hölder does not close the endpoint.

A Lorentz/endpoint refinement would be a separate theorem and is not assumed here.

Permanent firewall:

\[
\boxed{m=9/4\text{ is critical, not covered by the strong argument.}}
\]

## 5. Interpolate the certified ancient derivative resources

The M5-477 palinstrophy tail is Fourier-equivalent to the velocity `D2` tail:

\[
\boxed{
\int_{-\infty}^{-T}
\|D^2V\|_2^2d\tau
\lesssim T^{-1/2}.
}
\]

M17-404 gives the velocity `D3` / vorticity raw-H2 tail:

\[
\boxed{
\int_{-\infty}^{-T}
\|D^3V\|_2^2d\tau
\lesssim T^{-3/2}.
}
\]

Let

\[
m=2+\theta,
\qquad 0\le\theta\le1.
\]

Spatial homogeneous Sobolev interpolation gives pointwise in time

\[
\|D^mV\|_2
\lesssim
\|D^2V\|_2^{1-\theta}
\|D^3V\|_2^\theta.
\]

Squaring, integrating, and applying Hölder in time yields

\[
\begin{aligned}
\int_{-\infty}^{-T}\|D^mV\|_2^2d\tau
&\lesssim
\left(
\int_{-\infty}^{-T}\|D^2V\|_2^2d\tau
\right)^{1-\theta}
\\
&\qquad\cdot
\left(
\int_{-\infty}^{-T}\|D^3V\|_2^2d\tau
\right)^\theta.
\end{aligned}
\]

Therefore

\[
\boxed{
\int_{-\infty}^{-T}\|D^mV\|_2^2d\tau
\lesssim
T^{-\frac12(1-\theta)}T^{-\frac32\theta}
=
T^{-1/2-\theta}
=
T^{3/2-m}.
}
\]

This holds for every

\[
2\le m\le3.
\]

## 6. Physical restoration remains exactly critical

The spacetime `L2` norm of `D^m u` scales with physical base radius as

\[
\boxed{
Q_m^{phys}
=
r_j^{3-2m}Q_m^{norm}.
}
\]

At backward age `T`, the certified normalized tail is

\[
Q_m^{norm}\lesssim T^{3/2-m}.
\]

Hence

\[
Q_m^{phys}
\lesssim
r_j^{3-2m}T^{3/2-m}.
\]

With composite radius

\[
\rho=r_j\sqrt T,
\]

we get

\[
\boxed{
Q_m^{phys}
\lesssim
\rho^{3-2m}.
}
\]

Thus **every interpolated derivative order between 2 and 3 remains exactly parabolically critical after physical restoration**.

In particular, lowering the analytic endpoint to `m>9/4` reduces the required derivative order but does not by itself create base gain.

## 7. Sharpened GMS transfer target

The previous sufficient target `physical D3 in L2` can be weakened to

\[
\boxed{
\exists m>\frac94:
\quad
D^m u\in L^2_{x,t}
\text{ on the relevant physical neighborhood}.
}
\]

But the current ancient resources only give critical scale behavior

\[
\rho^{3-2m}.
\]

Therefore the true missing theorem is

\[
\boxed{
\mathcal T_{GMS}^{frac-subcrit}:
\text{for some }m>9/4,
\text{ obtain a representation-safe subcritical improvement over }
T^{3/2-m}
}
\]

on backward ages compatible with

\[
\rho_j=r_j\sqrt{T_j}\to0.
\]

## 8. Why this is still a gain

Although no closure is obtained, the analytic derivative demand has been lowered from order three to arbitrarily close above order `9/4`.

This narrows the gap between the certified palinstrophy level `m=2` and the regularity endpoint from one full derivative to only slightly more than one quarter derivative.

Thus future estimates need not reproduce the full raw-H2 strength of M17-404 if they can provide a genuinely subcritical fractional improvement.

## 9. Updated firewall

\[
\boxed{
\text{lower fractional derivative threshold}
\not\Rightarrow
\text{automatic base gain};
}
\]

and

\[
\boxed{
\text{interpolation of critical ancient tails remains critical at every }m\in[2,3].
}
\]

---

\[
\boxed{\text{M19-310 COMPLETE; THE ANALYTIC GMS THRESHOLD IS }m>9/4\text{, WHILE THE KNOWN ANCIENT TAIL FAMILY IS CRITICAL THROUGHOUT.}}
\]