# M19-284 — Exact material-cutoff kinetic-energy law reduces the same-population lag branch to pressure exchange, viscous exchange, and bulk dissipation

**Date:** 2026-09-16  
**Status:** CALCULATION / SAME-POPULATION FINITE-LAG ENERGY LAW / MONOTONE-ENERGY NO-GO

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-283 conditionally localizes the global wedge-energy event to one fixed persistent material population \(i_E\), a different persistent population, or an interface/background defect.

On the same-population branch \(i_E=\alpha_*\), the next tempting argument is that repeated positive energy-transport events on the production-paying lineage should force cumulative growth of that lineage's energy.

This module derives the exact material kinetic-energy balance and blocks that shortcut.

## 2. Similarity Navier--Stokes equation

Use the similarity equation

\[
\boxed{
\partial_\theta U
+\frac12U
+\frac12(y\cdot\nabla)U
+(U\cdot\nabla)U
+\nabla P
=\nu\Delta U,
}
\]

with

\[
\nabla\cdot U=0.
\]

Define the similarity material velocity

\[
\boxed{B:=U+\frac12y,}
\]

so

\[
\boxed{\nabla\cdot B=\frac32.}
\]

Then

\[
\partial_\theta U+B\cdot\nabla U+\frac12U+\nabla P=\nu\Delta U.
\]

## 3. Pointwise kinetic-energy equation

Let

\[
e:=\frac12|U|^2.
\]

Taking the scalar product with \(U\) gives

\[
\partial_\theta e
+B\cdot\nabla e
+e
+\nabla\cdot(PU)
=\nu\Delta e-\nu|\nabla U|^2.
\]

Thus

\[
\boxed{
\partial_\theta e
+B\cdot\nabla e
=
-e-\nabla\cdot(PU)
+\nu\Delta e
-\nu|\nabla U|^2.
}
\]

## 4. Smooth material cutoff

Let \(\eta(\theta,y)\) be a smooth material cutoff for one selected persistent population, satisfying

\[
\boxed{D_B\eta:=\partial_\theta\eta+B\cdot\nabla\eta=0.}
\]

Define its kinetic energy

\[
\boxed{E_\eta(\theta):=\int\eta e\,dy.}
\]

Assume the cutoff decays sufficiently at infinity or is compactly supported in the active-core representation so that spatial integrations by parts are valid.

If a material cutoff with these properties cannot be retained across the lag, record

\[
\boxed{G_{material\ energy\ representation/residence}.}
\]

## 5. Exact material energy law

Using \(D_B\eta=0\),

\[
\begin{aligned}
E_\eta'
&=
\int \eta
\left(
\partial_\theta e+B\cdot\nabla e+(\nabla\cdot B)e
\right)dy.
\end{aligned}
\]

Since \(\nabla\cdot B=3/2\), the pointwise equation yields

\[
\boxed{
\begin{aligned}
E_\eta'
={}&
\frac12E_\eta
+
\int PU\cdot\nabla\eta\,dy\\
&-
\nu\int\nabla\eta\cdot\nabla e\,dy
-
\nu\int\eta|\nabla U|^2dy.
\end{aligned}
}
\]

Define

\[
\boxed{X_P[\eta]:=\int PU\cdot\nabla\eta\,dy,}
\]

\[
\boxed{X_\nu[\eta]:=-\nu\int\nabla\eta\cdot\nabla e\,dy,}
\]

and

\[
\boxed{D_U[\eta]:=\int\eta|\nabla U|^2dy\ge0.}
\]

Then

\[
\boxed{
E_\eta'
=
\frac12E_\eta
+X_P[\eta]
+X_\nu[\eta]
-\nu D_U[\eta].
}
\]

For a sharp material domain this is the corresponding pressure-work, viscous-boundary-flux, and bulk-dissipation identity.

## 6. Finite-lag identity

Integrating from \(\theta\) to \(\theta+h\) gives

\[
\boxed{
\begin{aligned}
E_\eta(\theta+h)-E_\eta(\theta)
=
\int_\theta^{\theta+h}
\Big[
\frac12E_\eta
+X_P+X_\nu-\nu D_U
\Big]ds.
\end{aligned}
}
\]

The left side is an ordinary finite-lag state increment whenever the marked material cutoff is part of the recurrent state.

## 7. Recurrent mean balance

On a bounded integrable recurrent marked-population branch,

\[
\boxed{
\left\langle E_\eta\circ\sigma_h-E_\eta\right\rangle=0.
}
\]

Therefore

\[
\boxed{
0
=
\frac12\langle E_\eta\rangle
+\langle X_P\rangle
+\langle X_\nu\rangle
-\nu\langle D_U\rangle.
}
\]

Equivalently,

\[
\boxed{
\nu\langle D_U\rangle
=
\frac12\langle E_\eta\rangle
+\langle X_P+X_\nu\rangle.
}
\]

Thus a recurrent material population can maintain bounded energy by balancing similarity amplification against bulk dissipation and signed pressure/viscous exchange.

No monotone-energy contradiction follows from recurrence alone.

## 8. Relation to M19-271 and M19-282

The exact same-population lag law has precisely the structure anticipated by the coboundary firewall:

\[
\boxed{
\Delta_hE_\eta
=
\text{similarity baseline}
+
\text{pressure exchange}
+
\text{viscous exchange}
-
\text{bulk dissipation}.
}
\]

The lag increment has zero invariant mean, while the RHS terms compensate.

M19-282 already showed that the unconditional positive mean of the wedge-energy event is paid by ordinary dissipation. M19-284 confirms that following the same material population does not remove this compensation: pressure/interface exchange and similarity amplification remain available.

Therefore

\[
\boxed{
\text{same persistent lineage}
+\text{positive recurrent energy event}
\not\Rightarrow
\text{monotone material-energy accumulation}.
}
\]

## 9. Exact same-population remainder taxonomy

On the controlled material branch, any attempt to convert the localized wedge event into a finite-lag material-energy contradiction must isolate at least one of

\[
\boxed{
G_{pressure\ exchange}
\lor
G_{viscous\ boundary\ exchange}
\lor
G_{bulk\ dissipation}
\lor
G_{material\ energy\ representation/residence}.
}
\]

The first three are explicit PDE channels, not untyped errors.

Bulk dissipation is unsigned and remains subject to the M5-598 physical-accumulation firewall. Pressure and viscous exchange are signed and therefore are the more promising candidates for a genuinely non-coboundary finite-lag defect, but they require an independent sign or finite-budget theorem.

## 10. Important distinction from the wedge radial current

The M19-283 localized wedge current lives on a fixed wedge-depth sphere/annulus. The material energy law follows a cutoff transported by \(B=U+y/2\).

These are not the same geometry. Their difference contains the relative sweeping of a material carrier through fixed-depth observation surfaces.

Hence one must not identify the localized \(\Gamma_{i_E}\) directly with \(X_P+X_\nu-\nu D_U\) without an additional Eulerian-to-material conversion identity.

This conversion is now the precise next gate.

## 11. Next target

Derive the exact relative-flux identity between

1. the fixed-depth wedge energy current localized by \(\eta_i\), and
2. the material-cutoff energy budget transported by \(B\).

The difference should separate into

\[
\boxed{
\text{relative sweeping/geometry}
+
\text{pressure work}
+
\text{viscous exchange}
+
\text{bulk dissipation}.
}
\]

If the relative sweeping is an exact bounded-state coboundary or cancels under invariant averaging, the remaining signed pressure/interface term becomes the highest-value candidate for \(\mathcal T_{tail}^{lag-defect/core}\).

---

\[
\boxed{\text{M19-284 COMPLETE; SAME-POPULATION FINITE-LAG ENERGY IS EXACTLY COMPENSATED BY SIMILARITY, PRESSURE, VISCOUS-EXCHANGE, AND DISSIPATION CHANNELS.}}
\]
