# M19-051 — Sub-natural vortex-packet scaling shows amplitude-natural scale does not force volume filling or multiplicity

**Date:** 2026-09-11  
**Status:** CALCULATION / ANTI-PROOF FIREWALL / R-AC SUB-NATURAL PACKET GEOMETRY

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-050 identifies the amplitude-natural scale

\[
r_A
\sim
\rho J^{-1/4}
\]

for a shell packet of geometric radius \(\rho\) and cubic charge \(J\).

When \(J\ll1\),

\[
r_A\gg\rho.
\]

A tempting closure argument would say that a packet whose peak amplitude corresponds to the larger natural scale \(r_A\) must occupy a fixed fraction of the full \(r_A\)-core, thereby generating approximately

\[
(r_A/\rho)^3
\asymp
J^{-3/4}
\]

small packets or equivalent spatial filling.

The present module shows that this implication is false at the level of scale-compatible divergence-free fields.

A single smooth sub-natural vortex packet can realize all current shell scalings while occupying only an \(O(J^{3/4})\) fraction of the amplitude-natural volume.

This is a local scaling firewall, not an exact Navier--Stokes solution.

## 2. Fixed divergence-free seed

Choose a nonzero smooth compactly supported divergence-free vector field

\[
W\in C_c^\infty(B_2;\mathbb R^3),
\qquad
\nabla\cdot W=0.
\]

Let

\[
V
:=
\nabla\times(-\Delta)^{-1}W.
\]

Then

\[
\nabla\cdot V=0,
\qquad
\nabla\times V=W,
\]

with the usual decaying Biot--Savart field.

Fix a center \(x_0\), geometric packet radius \(\rho>0\), and charge parameter \(J>0\).

Define

\[
A
:=
\frac{J^{1/2}}{\rho^2}.
\]

Set

\[
\boxed{
\omega_{J,\rho}(x)
:=
A\,
W\left(\frac{x-x_0}{\rho}\right)
}
\]

and

\[
\boxed{
u_{J,\rho}(x)
:=
A\rho\,
V\left(\frac{x-x_0}{\rho}\right).
}
\]

Then

\[
\nabla\times u_{J,\rho}=\omega_{J,\rho}.
\]

## 3. Vorticity amplitude and enstrophy

The peak vorticity amplitude is

\[
\boxed{
\|\omega_{J,\rho}\|_\infty
\asymp
\frac{J^{1/2}}{\rho^2}.
}
\]

Its enstrophy is

\[
\begin{aligned}
\|\omega_{J,\rho}\|_2^2
&=A^2\rho^3\|W\|_2^2\\
&\asymp
\frac{J}{\rho^4}\rho^3.
\end{aligned}
\]

Hence

\[
\boxed{
\|\omega_{J,\rho}\|_2^2
\asymp
\frac J\rho.
}
\]

This is exactly the M19-046/047 bulk shell scaling.

## 4. Palinstrophy

Since

\[
\nabla\omega_{J,\rho}
=
A\rho^{-1}
(\nabla W)\left(\frac{x-x_0}{\rho}\right),
\]

\[
\begin{aligned}
\|\nabla\omega_{J,\rho}\|_2^2
&=A^2\rho\|\nabla W\|_2^2\\
&\asymp
\frac{J}{\rho^3}.
\end{aligned}
\]

Thus

\[
\boxed{
\|\nabla\omega_{J,\rho}\|_2^2
\asymp
\frac J{\rho^3}.
}
\]

The relative-frequency ratio is only order one:

\[
\boxed{
\rho^2
\frac{\|\nabla\omega\|_2^2}
{\|\omega\|_2^2}
\asymp1.
}
\]

Therefore this model lies on the ordinary kinetic branch of M19-047, not on the \(\Lambda_{rel}\to\infty\) branch.

## 5. Kinetic energy and critical Morrey charge

The velocity scale is

\[
A\rho
=
\frac{J^{1/2}}{\rho}.
\]

Therefore

\[
\begin{aligned}
\|u_{J,\rho}\|_2^2
&=A^2\rho^5\|V\|_2^2\\
&\asymp
J\rho.
\end{aligned}
\]

Hence the own-scale kinetic Morrey charge is

\[
\boxed{
\frac1\rho
\|u_{J,\rho}\|_2^2
\asymp
J.
}
\]

This saturates the M19-047 lower branch at the correct order.

## 6. Critical L3 / weak-L3 scaling

For the strong \(L^3\) norm,

\[
\begin{aligned}
\|u_{J,\rho}\|_3^3
&=A^3\rho^6\|V\|_3^3\\
&\asymp
\frac{J^{3/2}}{\rho^6}\rho^6.
\end{aligned}
\]

Thus

\[
\boxed{
\|u_{J,\rho}\|_3^3
\asymp
J^{3/2}.
}
\]

Likewise scale invariance gives

\[
\boxed{
\|u_{J,\rho}\|_{L^{3,\infty}}
\asymp
J^{1/2}.
}
\]

Hence small \(J\) packets are entirely compatible with a bounded weak-\(L^3\) corridor, while their cubic charges can still satisfy

\[
\sum_kJ_k^{3/2}=\infty
\]

across infinitely many scales.

## 7. Amplitude-natural scale and filling fraction

The peak amplitude defines the first-hitting natural scale

\[
r_A
\sim
\|\omega\|_\infty^{-1/2}
\sim
\rho J^{-1/4}.
\]

Thus

\[
\frac{\rho}{r_A}
\asymp
J^{1/4}.
\]

The packet occupies volume order \(\rho^3\), whereas the amplitude-natural ball has volume order \(r_A^3\).

Therefore the filling fraction is

\[
\boxed{
\varphi
:=
\frac{\rho^3}{r_A^3}
\asymp
J^{3/4}.
}
\]

For \(J\to0\),

\[
\varphi\to0.
\]

Yet Sections 3--6 show no scaling inconsistency.

Therefore

\[
\boxed{
\text{peak-amplitude natural scale }r_A
\not\Rightarrow
\text{order-one volume filling at }r_A.
}
\]

## 8. No free multiplicity

Geometrically, one \(r_A\)-ball could contain order

\[
(r_A/\rho)^3
\asymp
J^{-3/4}
\]

pairwise disjoint \(\rho\)-packets.

But the existence of one packet does not force those available slots to be occupied.

In particular the missing M19-050 center factor would be repaired at the Morrey-charge level if one could force roughly

\[
N\gtrsim J^{-1/4}
\]

comparable packets, because

\[
N J^{5/4}\gtrsim J.
\]

The toy packet proves that no such multiplicity follows from amplitude, enstrophy, palinstrophy, kinetic Morrey, or bounded weak-\(L^3\) scaling alone.

Thus

\[
\boxed{
\text{geometric capacity}
\neq
\text{dynamical occupancy}.
}
\]

This is the spatial analogue of the M18-055 temporal multiplicity firewall.

## 9. Flux scale also shrinks

A transverse vorticity flux through a \(\rho^2\)-sized cross-section has characteristic size

\[
\Phi_{packet}
\sim
\|\omega\|_\infty\rho^2
\sim
J^{1/2}.
\]

Therefore these small-\(J\) packets do not each carry the fixed order-one flux threshold used by the finite-memory population theorem M18-087.

Consequently one cannot use the fixed-flux storage bound to forbid arbitrarily many such sub-natural weak packets without an additional flux aggregation theorem.

This is another firewall against importing a result outside its amplitude class.

## 10. What the anti-model does and does not show

The construction is a smooth divergence-free **snapshot scaling model**.

It is not asserted to solve Navier--Stokes, to satisfy the first-hitting dynamics, or to recur in time.

It proves only that the currently retained local scale relations do not force natural-core filling, packet multiplicity, or fixed-flux material storage.

Therefore any successful M19 proof must use genuine dynamics/recurrence/pressure/nonlocal coupling rather than local dimensional packing alone.

## 11. Updated frontier

M19-050's proximity branch yields

\[
\mathcal M_k^{com}\gtrsim J_k^{5/4}
\]

and leaves a \(J^{1/4}\) center-coherence loss.

M19-051 shows this loss cannot be repaired for free by declaring the amplitude-natural core filled with comparable packets.

Hence the retained hard branch is now

\[
\boxed{
\text{terminal small-}J\text{ sub-natural packets}
+\text{cubic nonsummability}
+\text{insufficient common-center coherence}.
}
\]

The missing ingredient must be dynamical, not volumetric.

## 12. Highest-value next target

The next calculation should use the **Navier--Stokes evolution of a sub-natural packet**, rather than static geometry.

For a packet of radius \(\rho\) and velocity scale

\[
U\sim J^{1/2}/\rho,
\]

the advective turnover time is

\[
\tau_{adv}
\sim
\frac\rho U
\sim
\frac{\rho^2}{J^{1/2}},
\]

which is exactly the Type-I remaining-time scale found in M19-046.

The viscous diffusion time is

\[
\tau_{diff}
\sim
\frac{\rho^2}{\nu}.
\]

Thus for small dimensionless \(J\), advection is slower than diffusion relative to the packet scale.

The next module should calculate the packet-scale Reynolds number

\[
Re_{packet}
\sim
\frac{U\rho}{\nu}
\sim
J^{1/2}/\nu
\]

in the repository normalization and test whether the \(J_k\to0\) cubic-divergent sector is actually a **viscosity-dominated sub-natural regime** incompatible with persistent first-hitting recurrence, or whether stretching/nonlocal strain can maintain it.

---

\[
\boxed{\text{M19-051 COMPLETE; LOCAL FILLING/MULTIPLICITY CANNOT REMOVE THE J^{1/4} GAP.}}
\]