# DSD M17-436 — Normalized kappa transition speed is not an independent exit but a union of coefficient, strain, amplitude, and direction high-jet decompactifications

Date: 2026-09-08  
Canonical ID: **M17-436**

Status: **ACTIVE TRANSITION-SPEED CLASSIFICATION / M17-339--398--435 CONNECTION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M17-435 closes rapid sign fragmentation through regular zero corridors under the normalized transition-speed bound

\[
r^4|D_t\kappa|\le S_*.
\]

The present module asks whether failure of this bound is a genuinely new PDE mechanism.

It is not.

The exact M17-339 constitutive law expresses `D_t kappa` entirely through already typed spatial coefficient, strain, amplitude, and direction geometry jets.

## 2. Exact physical CE-H coefficient law

M17-339 gives

\[
\boxed{
D_t\kappa
=
L_\rho\kappa
+
L_\rho\sigma
+
\mathcal R_{geom},
}
\]

with

\[
L_\rho f
=
\rho^{-2}\nabla\cdot(\rho^2\nabla f)
=
\Delta f
+2\nabla\log\rho\cdot\nabla f.
\]

The geometric remainder is

\[
\begin{aligned}
\mathcal R_{geom}
={}&-
\frac{2}{\rho}
\Sigma:\nabla^2\rho
+2\Sigma_{ij}\partial_i\xi\cdot\partial_j\xi\\
&+(\nabla\times\Omega)\cdot\nabla\log\rho.
\end{aligned}
\]

There is no physical `-kappa` relaxation term.

## 3. Own-scale normalized descriptors

At spatial scale `r`, define the dimensionless quantities

\[
K_1:=r^3|\nabla\kappa|,
\qquad
K_2:=r^4|\Delta\kappa|,
\]

\[
S_0:=r^2|\Sigma|,
\qquad
S_1:=r^3|\nabla\sigma|,
\qquad
S_2:=r^4|\Delta\sigma|,
\]

\[
A_1:=r|\nabla\log\rho|,
\qquad
A_2:=r^2|\nabla^2\log\rho|,
\]

\[
X_1:=r|\nabla\xi|,
\qquad
C_1:=r^3|\nabla\times\Omega|.
\]

These are the natural own-scale normalized jets for the terms in M17-339.

## 4. Weighted coefficient diffusion

Using

\[
L_\rho\kappa
=
\Delta\kappa
+2\nabla\log\rho\cdot\nabla\kappa,
\]

we obtain

\[
\boxed{
r^4|L_\rho\kappa|
\le
K_2+2A_1K_1.
}
\]

Therefore coefficient diffusion can produce unbounded normalized transition speed only if a coefficient second jet, coefficient first jet, or amplitude logarithmic gradient decompactifies.

## 5. Weighted strain diffusion

Likewise

\[
L_\rho\sigma
=
\Delta\sigma
+2\nabla\log\rho\cdot\nabla\sigma,
\]

so

\[
\boxed{
r^4|L_\rho\sigma|
\le
S_2+2A_1S_1.
}
\]

Thus the strain contribution is bounded on any own-scale state class with bounded normalized second strain jet, first strain jet, and amplitude logarithmic gradient.

M17-361/398 already identify the first strain-gradient level with palinstrophy-order structure. The second strain jet is raw-`H2` derivative order under the standard Riesz/Fourier relation, but pointwise decompactification still requires a spacetime occupancy theorem before it becomes an ancestral contradiction.

## 6. Geometric remainder in normalized variables

Use

\[
\frac{\nabla^2\rho}{\rho}
=
\nabla^2\log\rho
+
\nabla\log\rho\otimes\nabla\log\rho.
\]

Then

\[
r^4
\left|
\frac{2}{\rho}
\Sigma:\nabla^2\rho
\right|
\lesssim
S_0(A_2+A_1^2).
\]

Also

\[
\boxed{
r^4
|2\Sigma_{ij}\partial_i\xi\cdot\partial_j\xi|
\lesssim
S_0X_1^2,
}
\]

and

\[
\boxed{
r^4
|(\nabla\times\Omega)\cdot\nabla\log\rho|
\lesssim
C_1A_1.
}
\]

Therefore

\[
\boxed{
r^4|\mathcal R_{geom}|
\lesssim
S_0(A_2+A_1^2+X_1^2)
+C_1A_1.
}
\]

## 7. Master transition-speed bound

Combining Sections 4--6,

\[
\boxed{
\begin{aligned}
r^4|D_t\kappa|
\lesssim{}&
K_2+A_1K_1
+S_2+A_1S_1\\
&+S_0(A_2+A_1^2+X_1^2)
+C_1A_1.
\end{aligned}
}
\]

Consequently, if all normalized descriptors on the right remain uniformly bounded on a retained own-scale state class, then

\[
\boxed{r^4|D_t\kappa|\le S_*<\infty.}
\]

Thus the transition-speed hypothesis of M17-435 is automatic under normalized finite-jet compactness of the constitutive data.

## 8. Exact decompactification split

Therefore

\[
\boxed{
r^4|D_t\kappa|\to\infty}
\]

implies at least one of

\[
\boxed{G_{coefficient\ first/second\ jet\ decompactification}},
\]

\[
\boxed{G_{strain\ first/second\ jet\ decompactification}},
\]

\[
\boxed{G_{amplitude\ log\text{-}gradient/Hessian\ decompactification}},
\]

\[
\boxed{G_{direction\ gradient\ decompactification}},
\]

or

\[
\boxed{G_{vorticity\ gradient/curl\ decompactification}}.
\]

It is not a sixth independent transition mechanism.

## 9. Relation to existing canonical branches

The descriptors route naturally to earlier modules:

- `K_1,K_2`: coefficient intrinsic-scale / finite-jet mismatch, M17-393/418;
- `A_1,A_2`: amplitude/frequency/doubling or nodal decompactification, M17-383--384 and M17-429--431;
- `S_1`: strain-gradient payer, M17-361/398, hence palinstrophy-order;
- `S_2`: raw-`H2`-order strain high jet under Riesz/Fourier control;
- `X_1,C_1`: direction/vorticity-gradient geometry, part of the M17-398 bulk palinstrophy architecture when integrated with compact amplitude weights.

Pointwise blow-up of one descriptor is not by itself an integral contradiction; it is a typed decompactification exit that must acquire duration/multiplicity before applying M17-307 or M17-405.

## 10. Consequence for M17-435

On any retained zero-transition branch whose normalized coefficient, strain, amplitude, and direction jets remain compact, M17-436 supplies the bounded transition-speed hypothesis automatically.

Therefore M17-435 closes the **regular compact finite-jet sign-fragmentation branch**.

A surviving rapid-transition sequence must leave that compact normalized state class through one of the explicit spatial/high-jet exits in Section 8.

## 11. DSD role

DSD is used only to type an apparent temporal failure back into the actual constitutive spatial variables and prevent `fast transition` from being counted as an independent mystery.

The mathematics is the exact M17-339 coefficient equation and scale-homogeneous dimensional normalization.

## 12. Audit verdict

**PASS as a transition-speed decompactification classification.**

The late zero-transition frontier is reduced from an untyped temporal-speed exit to existing coefficient/strain/amplitude/direction high-jet decompactifications.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
