# DSD M5-534 — Remote weighted dust is quantitatively decoupled from bounded-core velocity and strain

Date: 2026-09-01

Status: **NONLOCAL DECOUPLING / THE M5-533 INFINITE-MOMENT TAIL HAS VANISHING LOCAL AMPLITUDE AND UNIFORMLY SMALL UNWEIGHTED ENSTROPHY OUTSIDE LARGE RADII / DIRECT BIOT--SAVART KERNEL ESTIMATES SHOW THAT ITS CONTRIBUTION TO VELOCITY ON A FIXED CORE BALL IS `O(R^-1/2 E_tail(R)^1/2)` AND ITS CONTRIBUTION TO STRAIN IS `O(R^-3/2 E_tail(R)^1/2)` / HENCE THE REMOTE WEIGHTED DUST CANNOT SUPPLY AN ORDER-ONE RECURRENT CORE STRETCHING OR PROJECTIVE ACTION IN THE LIMIT `R -> infinity` / THE POSITIVE PRODUCTION/DUAL/RATCHET MECHANISMS OF THE COMPACT HARD COMPONENT ARE THEREFORE CORE-SUPPORTED, WHILE THE INFINITE FIRST-MOMENT TAIL IS A SEPARATE SPECTATOR/RESERVOIR DEFECT / THIS DOES NOT YET REMOVE THE TAIL FROM THE GLOBAL ANCIENT SOLUTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Core and remote vorticity split

Fix a core radius

\[
L<\infty.
\]

For `R>2L`, split the Biot--Savart integral into

\[
U(x)
=U_{near,R}(x)+U_{far,R}(x),
\]

where

\[
U_{far,R}(x)
:=
\int_{|z|>R}K(x-z)W(z)dz
\]

and the 3D Biot--Savart kernel obeys

\[
|K(\zeta)|\le C|\zeta|^{-2}.
\]

This is a linear integral decomposition; no claim is made that the truncated far field alone solves Navier--Stokes.

---

## 2. Geometry for a bounded core point

If

\[
|x|\le L,
\qquad
|z|>R>2L,
\]

then

\[
|x-z|
\ge |z|-L
\ge\frac12|z|.
\]

Therefore all far-field kernels may be estimated by powers of `|z|` with constants depending only on the fixed ratio `R/L` once `R>2L`.

---

## 3. Far velocity estimate

By Cauchy--Schwarz,

\[
\begin{aligned}
|U_{far,R}(x)|
&\le
C
\int_{|z|>R}|z|^{-2}|W(z)|dz\\
&\le
C
\left(
\int_{|z|>R}|W|^2dz
\right)^{1/2}
\left(
\int_{|z|>R}|z|^{-4}dz
\right)^{1/2}.
\end{aligned}
\]

In three dimensions,

\[
\int_{|z|>R}|z|^{-4}dz
\asymp
\int_R^\infty r^{-2}dr
\asymp R^{-1}.
\]

Hence

\[
\boxed{
\sup_{|x|\le L}|U_{far,R}(x)|
\le
C_L
R^{-1/2}
E_{tail}(R)^{1/2},
}
\]

where

\[
E_{tail}(R)
:=
\int_{|z|>R}|W(z)|^2dz.
\]

On the M5-508 tight branch,

\[
\sup_Y E_{tail}^Y(R)\to0.
\]

Thus

\[
\boxed{
\sup_Y
\|U_{far,R}^Y\|_{L^\infty(B_L)}
\to0.
}
\]

---

## 4. Far strain estimate

The strain kernel is one derivative of Biot--Savart:

\[
|\nabla K(\zeta)|
\le C|\zeta|^{-3}.
\]

Therefore

\[
\begin{aligned}
|\nabla U_{far,R}(x)|
&\le
C
\int_{|z|>R}|z|^{-3}|W(z)|dz\\
&\le
C E_{tail}(R)^{1/2}
\left(
\int_{|z|>R}|z|^{-6}dz
\right)^{1/2}.
\end{aligned}
\]

Since

\[
\int_{|z|>R}|z|^{-6}dz
\asymp R^{-3},
\]

we obtain

\[
\boxed{
\sup_{|x|\le L}|\nabla U_{far,R}(x)|
\le
C_L
R^{-3/2}E_{tail}(R)^{1/2}.
}
\]

In particular, for the symmetric strain,

\[
\boxed{
\sup_Y
\|\Sigma_{far,R}^Y\|_{L^\infty(B_L)}
\to0.
}
\]

---

## 5. Higher derivative version

For any fixed integer `m>=0`,

\[
|\nabla^mK(\zeta)|
\le C_m|\zeta|^{-2-m}.
\]

Thus the same argument gives

\[
\boxed{
\sup_{|x|\le L}
|\nabla^mU_{far,R}(x)|
\le
C_{m,L}
R^{-m-1/2}
E_{tail}(R)^{1/2}.
}
\]

For `m=1` this recovers the strain estimate.

Hence the remote weighted dust is asymptotically invisible to every fixed-order local velocity derivative in the bounded core.

---

## 6. Infinite first moment does not spoil the estimate

M5-531 gives

\[
\int|z||W|^2dz=\infty
\]

for invariant-almost every state.

This does not enter the estimates above.

The Biot--Savart kernels weight remote vorticity by negative powers of radius, while the moment defect weights it by a positive power.

Thus both can hold simultaneously:

\[
\boxed{
\text{infinite positive radial moment}
\quad\text{and}\quad
\text{vanishing nonlocal influence on the core}.
}
\]

This is precisely why the tail can survive unweighted compactness while remaining dynamically weak at the marked core.

---

## 7. Consequence for the production payer

M5-493--496 require order-one recurrent production in a bounded similarity region on the tight branch.

Suppose that production were attributed to increasingly remote vorticity.

M5-534 shows that its strain contribution to the fixed core ball satisfies

\[
\|\Sigma_{far,R}\|_\infty\to0.
\]

Therefore it cannot supply a fixed lower production amount

\[
Q_{core}
\ge q_0>0
\]

for sufficiently large `R`.

Hence

\[
\boxed{
\text{order-one recurrent core production}
\text{ is paid by bounded/intermediate scales, not by the infinite-moment dust at infinity.}
}
\]

This quantitatively reinforces the local-payer branch of M5-496.

---

## 8. Consequence for the projective/dual pair

The persistent dual pair and projective ratchet live on coherent material carriers of bounded normalized scale.

A far-field strain tending to zero cannot directly rotate those core directions by an order-one amount per fixed similarity block.

Therefore the positive recurrent pair/ratchet action on the compact hard component is likewise a core/intermediate-scale mechanism.

The remote dust may still affect global quantities and boundary conditions, but it is not the direct local geometric payer.

---

## 9. Spectator-tail interpretation

The hard survivor now contains two sharply separated structures.

### Active recurrent core

\[
\boxed{
\text{finite persistent lineages}
+
\text{positive production}
+
\text{dual/ratchet activity}.
}
\]

### Weighted remote reservoir

\[
\boxed{
\text{vanishing local amplitude}
+
\text{infinite first radial moment}
+
\text{negligible direct core strain influence}.
}
\]

The second is therefore a **spectator tail** relative to the local recurrent stretching mechanism.

This term is structural only; it does not mean the tail may be deleted from the PDE.

---

## 10. Firewall against truncation

Even though

\[
U_{far,R},\Sigma_{far,R}
\to0
\]

locally on the core, one may not simply truncate `W` outside `R` and claim the remaining field is another exact Navier--Stokes solution.

Spatial truncation breaks the exact divergence/Biot--Savart/pressure coupling and changes the global PDE.

Thus M5-534 proves **asymptotic local decoupling**, not an exact decomposition into two independent Navier--Stokes solutions.

---

## 11. New frontier

The global `L3` obstruction from M5-527 is now seen to be tail-driven, whereas the singularity mechanism retained by M5-493--516 is core-driven.

Hence the next high-value question is:

\[
\boxed{
\text{Can the Albritton--Barker global }L^3\text{ obstruction be localized to the active core}
}
\]

using the quantitative smallness of the remote velocity/strain/pressure influence?

Equivalently, construct a localized critical `L3`/local-energy observable in a fixed core cylinder whose far-field error tends to zero with `R`.

If such a localized ancient Liouville or epsilon-regularity bridge closes, the spectator tail can no longer shield the active recurrent core from the known critical regularity theory.

---

## 12. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
