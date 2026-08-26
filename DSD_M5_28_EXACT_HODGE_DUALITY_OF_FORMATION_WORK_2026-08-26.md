# DSD M5-28 — Exact Hodge Duality of Formation Work

Date: 2026-08-26

Status: **EXACT IDENTITY / THE PRESSURE-COUPLED GRADIENT FORMATION WORK AND THE SOLENOIDAL PROJECTED-LAMB TRANSFER ARE THE SAME HIGH-AMPLITUDE FORMATION ACTION WRITTEN IN TWO HODGE REPRESENTATIONS / P AND Q MUST NOT BE DOUBLE-COUNTED AS INDEPENDENT COSTS / FIRST HITTING HAS A FIXED ACTUAL SOLENOIDAL NONLINEAR-TRANSFER FLOOR / GLOBAL REGULARITY UNPROVED.**

## 1. Input

In normalized threshold variables define

\[
\mathcal G(V)
=\frac12\int(|V|-1)_+^2dz,
\]

\[
W
=\nabla_V\mathcal G_{density}
=\left(1-\frac1{|V|}\right)_+V,
\]

and

\[
Z:=\mathbb PW.
\]

M5-23 gives the pressure representation

\[
\boxed{
\mathcal G'
+\nu\mathcal D_{exc}
=
\int \Pi\,\operatorname{div}W\,dz.
}
\]

M5-26 shows that at a fixed positive first hitting both the gradient and solenoidal Hodge channels are nontrivial.

## 2. Time derivative only sees the solenoidal part of `W`

Because `V` is divergence free for all time,

\[
\nabla\cdot V_\sigma=0.
\]

The Hodge-gradient part `mathbb Q W` is therefore orthogonal to `V_sigma` in `L2`:

\[
\langle V_\sigma,\mathbb QW\rangle=0.
\]

Since

\[
W=\mathbb PW+\mathbb QW=Z+\mathbb QW,
\]

we obtain the exact identity

\[
\boxed{
\mathcal G'
=\langle V_\sigma,W\rangle
=\langle V_\sigma,Z\rangle.
}
\]

Thus the same convex amplitude variation can be read entirely in the solenoidal tangent space.

## 3. Projected Navier--Stokes representation

Apply the Leray projector to the normalized Navier--Stokes equation:

\[
V_\sigma
+\mathbb P((V\cdot\nabla)V)
=\nu\Delta V.
\]

Pressure disappears exactly.

Pair with `Z`:

\[
\mathcal G'
+\langle \mathbb P((V\cdot\nabla)V),Z\rangle
=\nu\langle\Delta V,Z\rangle.
\]

Since `Delta V` is divergence free,

\[
\langle\Delta V,\mathbb QW\rangle=0.
\]

Therefore

\[
\langle\Delta V,Z\rangle
=\langle\Delta V,W\rangle.
\]

The M5-23 diffusion computation gives

\[
\langle\Delta V,W\rangle
=-\mathcal D_{exc}.
\]

Hence

\[
\boxed{
\mathcal G'
+\nu\mathcal D_{exc}
=-\langle \mathbb P((V\cdot\nabla)V),Z\rangle.
}
\]

## 4. Lamb-force form

For incompressible flow,

\[
(V\cdot\nabla)V
=\Omega\times V
+\nabla(|V|^2/2).
\]

After the Leray projection,

\[
\mathbb P((V\cdot\nabla)V)
=\mathbb P(\Omega\times V).
\]

Define

\[
L_s:=\mathbb P(\Omega\times V).
\]

Then

\[
\boxed{
\mathcal G'
+\nu\mathcal D_{exc}
=-\langle L_s,Z\rangle.
}
\]

This is a pressure-free exact representation of the high-amplitude formation ledger.

## 5. Exact equality with the pressure/Hodge representation

Compare the projected identity with the pressure representation from M5-23:

\[
\mathcal G'
+\nu\mathcal D_{exc}
=
\int \Pi\,\operatorname{div}W.
\]

Therefore

\[
\boxed{
\int \Pi\,\operatorname{div}W\,dz
=
-\langle
\mathbb P(\Omega\times V),
\mathbb PW
\rangle.
}
\]

This is the exact M5-28 Hodge duality.

The left-hand side uses

- pressure;
- the Hodge-gradient component of the amplitude truncation;
- direction compression through `div W`.

The right-hand side uses

- the solenoidal Lamb force;
- the solenoidal component of the same high-amplitude excess.

They are not two independent energy sources. They are the same scalar formation work written in complementary Hodge coordinates.

## 6. First-hitting nonlinear-transfer floor

At the first fixed positive hitting of `G=g0`, M5-23 gives

\[
\mathcal G'\ge0
\]

and

\[
\mathcal D_{exc}
\ge d_{exc}>0.
\]

Therefore

\[
\int \Pi\,\operatorname{div}W
\ge
\nu d_{exc}.
\]

By the exact duality,

\[
\boxed{
-\langle
\mathbb P(\Omega\times V),
\mathbb PW
\rangle
\ge
\nu d_{exc}
=:c_{NL}>0.
}
\]

Thus every first creation of a fixed positive high-amplitude excess has a fixed **actual Navier--Stokes solenoidal nonlinear-transfer floor**.

This is stronger than merely knowing that `mathbb P W` contains critical frequency content.

## 7. DSD correction: do not double-count P and Q

M5-23 and M5-26 might superficially suggest a two-cost picture:

\[
\text{Q pressure source}
+
\text{P solenoidal transfer}.
\]

M5-28 shows this would double-count the same formation action.

The correct typed statement is

\[
\boxed{
\text{one formation work}
\begin{cases}
\text{Q representation: }\int\Pi\,\operatorname{div}W,\\
\text{P representation: }-\langle L_s,\mathbb PW\rangle.
\end{cases}
}
\]

The simultaneous nontriviality of both Hodge sectors is geometric; the scalar work they mediate is one and the same.

## 8. Relation to the earlier Lamb/Hodge analysis

Earlier W1 calculations found that Bernoulli work and vorticity transport are two manifestations of the solenoidal Lamb force.

M5-28 localizes that principle to the exact physical high-amplitude formation cell:

\[
|u|\sim L,
\qquad
|x-X_*|\sim L^{-1},
\qquad
|k|\sim L.
\]

At this cell the pressure-amplitude description and the projected-Lamb description are exactly dual.

Thus pressure is again not an independent final obstruction once the Hodge decomposition is handled correctly.

## 9. What remains open

The nonlinear-transfer floor

\[
-\langle L_s,Z\rangle\ge c_{NL}>0
\]

still does not give a contradiction.

The remaining problem is to constrain how this fixed transfer can be realized inside the solenoidal critical component `Z`.

M5-27 gives the polarization split:

\[
\text{two-helicity mixed}
\quad\lor\quad
\text{nearly homochiral / direction-twist}.
\]

The next audit should test the exact transfer

\[
\langle L_s,Z\rangle
\]

against those two polarization branches rather than treating pressure and helical transfer as separate mechanisms.

This is the M5-29 target.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
