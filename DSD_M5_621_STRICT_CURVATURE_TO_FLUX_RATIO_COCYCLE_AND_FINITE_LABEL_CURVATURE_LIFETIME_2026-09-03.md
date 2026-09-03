# DSD M5-621 — Strict curvature-to-flux ratio cocycle and finite curvature lifetime of one material label

Date: 2026-09-03

Status: **INTERNAL STRICT COCYCLE ON CE-H / COMBINING THE MATERIAL CURVATURE LAW FROM M5-620 WITH THE MATERIAL FLUX LAW FROM M5-602 ELIMINATES BOTH STRAIN AND THE VISCOUS MULTIPLIER: FOR A MATERIAL VORTEX-TUBE ELEMENT, `D_B log[(rho |K|)/|phi|] = -3/2` EXACTLY / HENCE THE CURVATURE-AMPLITUDE TO FLUX RATIO DECAYS AS `exp(-3 theta/2)` ALONG EVERY MATERIAL FLUX LABEL / A FIXED NONDEGENERATE FLUX LABEL CAN THEREFORE CARRY AN ORDER-ONE CURVATURE-AMPLITUDE PACKET ONLY FOR A UNIFORMLY FINITE SIMILARITY-TIME WINDOW / RECURRENT CURVATURE ACTIVITY MUST MIGRATE TO NEW MATERIAL LABELS OR FALL INTO THE TRANSVERSE-MAGNITUDE CHANNEL / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Inputs

On CE-H,

\[
D_B\log\rho
=\sigma+\kappa-1,
\]

and M5-620 gives

\[
D_B\log|\mathcal K|
=-\sigma-\frac12
\]

where

\[
\mathcal K=(\xi\cdot\nabla)\xi.
\]

Therefore

\[
\boxed{
D_B\log(\rho|\mathcal K|)
=\kappa-\frac32.
}
\]

For the same infinitesimal material vortex-tube cross-section, M5-602 gives

\[
\boxed{
D_B\log|\phi|=\kappa.
}
\]

---

## 2. Exact strict ratio law

Subtract the two logarithmic equations:

\[
D_B
\left[
\log(\rho|\mathcal K|)-\log|\phi|
\right]
=-\frac32.
\]

Hence

\[
\boxed{
D_B\log
\frac{\rho|\mathcal K|}{|\phi|}
=-\frac32.
}
\]

Integrating along a material vortex-line/tube label from `theta0` to `theta`,

\[
\boxed{
\frac{\rho|\mathcal K|}{|\phi|}(\theta)
=
\frac{\rho|\mathcal K|}{|\phi|}(\theta_0)
\exp\left[-\frac32(\theta-\theta_0)\right].
}
\]

This is an exact strict cocycle with no remainder and no sign ambiguity.

---

## 3. Why this is stronger than the separate curvature and flux laws

The individual laws contain unknown recurrent coefficients:

\[
D_B\log|\mathcal K|=-\sigma-\frac12,
\]

\[
D_B\log|\phi|=\kappa.
\]

The ratio law contains neither `sigma` nor `kappa`.

Thus no recurrent strain-diffusion compensation can cancel the drift:

\[
\boxed{-3/2}
\]

is universal on the CE-H branch.

This is precisely the type of bounded-observable strict drift sought in the earlier M5-485/M5-598 cocycle program.

---

## 4. Curvature-amplitude variable is uniformly bounded above

Define

\[
Z_{curv}:=\rho|\mathcal K|.
\]

Since

\[
\rho\mathcal K
=P_\xi^\perp(\xi\cdot\nabla W),
\]

we have pointwise on the active set

\[
\boxed{
Z_{curv}\le|\nabla W|.
}
\]

The compact all-order hull has

\[
\|\nabla W\|_\infty\le M_1,
\]

so

\[
\boxed{Z_{curv}\le M_1.}
\]

Thus the numerator in the strict ratio has a uniform state-space upper bound.

---

## 5. Fixed-flux coherent label

A retained coherent material-flux population in the finite-memory genealogy has a scale-critical flux threshold

\[
0<\phi_-\le|\phi|\le\phi_+<\infty
\]

while it remains counted as the same coherent fixed-flux label.

Therefore for such a label

\[
\frac{Z_{curv}}{|\phi|}
\le
\frac{M_1}{\phi_-}.
\]

Suppose the label is curvature-active whenever

\[
Z_{curv}\ge z_*>0.
\]

At a curvature-active time,

\[
\frac{Z_{curv}}{|\phi|}
\ge
\frac{z_*}{\phi_+}.
\]

---

## 6. Uniform finite curvature-active lifetime of one material label

The strict ratio law gives

\[
\frac{z_*}{\phi_+}
\le
\frac{M_1}{\phi_-}
\exp\left[-\frac32(\theta-\theta_{birth})\right]
\]

whenever a label born/selected at `theta_birth` is still curvature-active at time `theta`.

Hence

\[
\boxed{
\theta-\theta_{birth}
\le
T_{curv}
:=
\frac23
\log
\left(
\frac{M_1\phi_+}{z_*\phi_-}
\right).
}
\]

Thus one retained nondegenerate material-flux label can support an order-one curvature-amplitude packet for only a uniformly finite amount of similarity time.

After that time it can never again cross the same curvature threshold while remaining the same fixed-flux label, because the ratio is strictly decreasing.

---

## 7. Extraction of a coherent curvature packet from the M5-619 curvature channel

M5-619's curvature alternative is

\[
\|\rho^2\mathcal K\|_2\ge b_*/2.
\]

The compact amplitude and derivative caps imply

\[
\rho|\mathcal K|\le M_1.
\]

Consequently an `L2` lower bound on `rho^2 K` cannot be carried entirely where `rho` is arbitrarily small.

After finite-core localization and smooth thickening, there exist fixed constants

\[
\rho_*>0,
\qquad
z_*>0,
\qquad
r_*>0
\]

such that every quantitatively curvature-active event contains a ball `B_{r_*}` on which

\[
\boxed{
\rho\ge\rho_*,
\qquad
Z_{curv}=\rho|\mathcal K|\ge z_*.
}
\]

Shrinking the ball if necessary, direction coherence gives a material cross-section with fixed nonzero vorticity flux, so the packet is eligible for the existing finite-memory flux genealogy.

This is the bridge needed to apply the strict ratio law to the curvature channel.

---

## 8. Consequence for recurrent curvature activity

If curvature-active events occur with positive invariant density for arbitrarily large similarity times, no finite set of persistent fixed-flux labels can pay all of them indefinitely, because each label has curvature-active lifetime at most `T_curv`.

Therefore

\[
\boxed{
\text{positive-density curvature channel}
\Longrightarrow
\text{positive-density material-label renewal/turnover}
}
\]

unless the system moves to the transverse-magnitude branch of M5-619.

The finite-memory theorem M5-488 then converts this label renewal into compensating exits.

On CE-H,

- projective reorientation is absent because `D_B xi=0`;
- remote/export branches were separately removed on the compact hard core.

Hence the remaining compensation is viscous flux change/turnover.

Thus

\[
\boxed{
\text{persistent curvature activity}
\Longrightarrow
\text{positive-density viscous-flux turnover}
}
\]

on the surviving CE-H compact branch.

---

## 9. What is and is not closed

The strict ratio law closes the possibility that **one persistent fixed-flux material label** carries recurrent order-one curvature forever.

It does not yet prohibit a finite-memory system in which curvature activity repeatedly transfers to different material labels while viscosity reduces/raises their fluxes.

That remaining scenario is now much narrower:

\[
\boxed{
\text{curvature branch}
\Rightarrow
\text{viscous label-turnover branch}.
}
\]

The other surviving geometric possibility is the transverse-magnitude branch

\[
\|\rho P_\xi^\perp\nabla\rho\|_2\ge b_*/2.
\]

---

## 10. Highest-value next target

Two branches remain after the strict curvature cocycle:

1. `T`: positive-density viscous flux turnover generated by recurring curvature packets;
2. `M_perp`: persistent transverse magnitude-gradient charge.

The next step should derive the material evolution of

\[
G:=P_\xi^\perp\nabla\log\rho
\]

and determine whether a strict ratio analogous to the curvature/flux ratio exists for the transverse-magnitude branch.

If such a strict drift exists, the entire M5-619 non-Beltrami dichotomy may reduce to viscous-flux turnover alone.

---

## 11. Firewall

The fixed active lifetime applies only while the object remains the **same finite-memory material-flux label** with flux bounded below by the retained threshold.

A lineage may leave that label class by viscous flux loss, in which case it is counted as the explicit turnover exit rather than silently continuing the same label.

No contradiction with material-volume expansion is claimed.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
