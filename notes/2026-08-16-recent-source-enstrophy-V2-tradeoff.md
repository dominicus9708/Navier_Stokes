# Recent pointwise stretching source obeys an enstrophy--weighted-V2 tradeoff

Date: 2026-08-16

Status: **EXACT KERNEL-HOLDER-GAGLIARDO--NIRENBERG TRADEOFF ON THE TERMINAL FIRST-HITTING PAST. AFTER CLEAN-PRECURSOR INHERITANCE AND OLD SOURCE ARE REMOVED, AN ORDER-ONE RECENT SOURCE MUST PAY ORDINARY ENSTROPHY-TIME ACTION OR A WEIGHTED SECOND-VORTICITY-DERIVATIVE ACTION. GLOBAL REGULARITY NOT PROVED.**

## 1. Recent source identity

After the clean precursor transport term and old stretching source are shown to be `o(1)`, a coherent terminal/crossing point must satisfy

\[
\boxed{
\left|
\int_0^L
P_{T-\tau,T}(S\Omega)(x_*)d\tau
\right|
\ge c_0
}
\]

for

\[
L=W^{1/3+\delta}
\]

and all sufficiently late members of the hypothetical sequence.

On the entire first-hitting past,

\[
M(\tau):=\|\Omega(T-\tau)\|_\infty\le1.
\]

Define

\[
E(\tau)=\|\Omega(T-\tau)\|_2^2,
\qquad
Z(\tau)=\|D^2\Omega(T-\tau)\|_2^2.
\]

---

## 2. L4 size of the stretching source

Calderon--Zygmund gives

\[
\|S\|_4\lesssim\|\Omega\|_4.
\]

The `L2-Linfinity` interpolation is

\[
\|\Omega\|_4
\le
M^{1/2}E^{1/4}.
\]

Therefore

\[
\boxed{
\|S\Omega\|_4
\le
\|S\|_4M
\lesssim
M^{3/2}E^{1/4}.
}
\]

---

## 3. Adjoint-kernel L4/3 ceiling

Nash smoothing for divergence-free advection gives, in three dimensions,

\[
\boxed{
\|K_\tau\|_{4/3}
\lesssim
(\nu\tau)^{-3/8}.
}
\]

Hence

\[
\begin{aligned}
c_0
&\lesssim
\nu^{-3/8}
\int_0^L
\tau^{-3/8}
M(\tau)^{3/2}
E(\tau)^{1/4}d\tau.
\end{aligned}
\]

Set

\[
\boxed{
D_L=\int_0^L E(\tau)d\tau
}
\]

and

\[
\boxed{
A_L
=\int_0^L
\tau^{-1/2}M(\tau)^2d\tau.
}
\]

Use Holder with exponents `4` and `4/3`:

\[
\int_0^L
\tau^{-3/8}M^{3/2}E^{1/4}
\le
D_L^{1/4}A_L^{3/4}.
\]

Thus

\[
\boxed{
D_LA_L^3
\gtrsim
\nu^{3/2}.
}
\]

This is an exact recent-source tradeoff between ordinary enstrophy-time occupancy and a weighted squared-maximum-vorticity action.

---

## 4. Replace the maximum-vorticity action by V2

The three-dimensional Gagliardo--Nirenberg inequality gives

\[
\|\Omega\|_\infty
\lesssim
\|\Omega\|_2^{1/4}
\|D^2\Omega\|_2^{3/4}.
\]

In terms of `E` and `Z`,

\[
\boxed{
M^2
\lesssim
E^{1/4}Z^{3/4}.
}
\]

Therefore

\[
A_L
\lesssim
\int_0^L
\tau^{-1/2}E^{1/4}Z^{3/4}d\tau.
\]

Write

\[
\tau^{-1/2}E^{1/4}Z^{3/4}
=
E^{1/4}
(\tau^{-2/3}Z)^{3/4}.
\]

Another Holder estimate gives

\[
\boxed{
A_L
\lesssim
D_L^{1/4}
Z_L^{3/4},
}
\]

where

\[
\boxed{
Z_L
:=
\int_0^L
\tau^{-2/3}Z(\tau)d\tau.
}
\]

The temporal weight is integrable at zero, so the quantity is well-defined for every smooth pre-singular solution.

---

## 5. Final enstrophy--V2 source barrier

Substitute the preceding estimate into

\[
D_LA_L^3\gtrsim\nu^{3/2}.
\]

Then

\[
D_L
(D_L^{1/4}Z_L^{3/4})^3
\gtrsim
\nu^{3/2}.
\]

Thus

\[
D_L^{7/4}Z_L^{9/4}
\gtrsim
\nu^{3/2}.
\]

Raising to the fourth power,

\[
\boxed{
D_L^7Z_L^9
\gtrsim
\nu^6.
}
\]

Equivalently,

\[
\boxed{
Z_L
\gtrsim
c\nu^{2/3}D_L^{-7/9}.
}
\]

Therefore a recent source layer with small ordinary enstrophy-time occupancy must have large weighted second-vorticity-derivative action.

---

## 6. Relation to the derivative hierarchy

The quantity `Z=||D2 Omega||_2^2` is the next ordinary derivative level above palinstrophy. It is already included in

- the first-hitting V2 bootstrap on bounded-enstrophy windows;
- the factorial higher-derivative generating hierarchy;
- the energy-weighted projective-dissipation identity;
- the endpoint derivative-radius-collapse branch.

Thus the recent pointwise stretching source introduces no new untyped `L-infinity` mechanism:

\[
\boxed{
\text{order-one recent source}
\Longrightarrow
\text{ordinary enstrophy occupancy}
\quad\lor\quad
\text{weighted V2 / higher-derivative concentration}.
}
\]

---

## 7. Simple cap-only corollary

Since `M<=1`,

\[
A_L\le2\sqrt L.
\]

The basic tradeoff gives

\[
\boxed{
D_L
\gtrsim
c\nu^{3/2}L^{-3/2}.
}
\]

This lower bound becomes small when `L=W^(1/3+delta)` and is not by itself non-summable. The important content of the stronger formula is that pushing `D_L` below its natural occupancy scale necessarily makes the weighted V2 ledger diverge.

---

## 8. Remaining wall

A hypothetical singular cascade may still try to keep `D_L` at a critically summable level while allowing `Z_L` to grow at the reciprocal critical rate.

The next proof target is therefore to intersect

\[
\boxed{D_L^7Z_L^9\gtrsim\nu^6}
\]

with the factorial derivative projective-dissipation identity and the scale-time packing of high-curvature events, seeking a nonrepeatability theorem for the weighted V2 concentration.

Overall status: **RECENT STRETCHING SOURCE ROUTED TO ORDINARY ENSTROPHY OR V2 / ONLY CRITICAL RECIPROCAL SATURATION OF THESE TWO EXISTING LEDGERS REMAINS.**
