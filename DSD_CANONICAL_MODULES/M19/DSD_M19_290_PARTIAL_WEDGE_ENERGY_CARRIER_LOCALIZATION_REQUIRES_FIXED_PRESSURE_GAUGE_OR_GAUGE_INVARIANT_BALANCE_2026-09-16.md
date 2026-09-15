# M19-290 — Partial wedge-energy carrier localization requires a fixed pressure gauge or a gauge-invariant balance

**Date:** 2026-09-16  
**Status:** AUDIT CORRECTION / PRESSURE-GAUGE FIREWALL / M19-283 CONDITION SHARPENED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-283 conditionally localizes the whole-sphere wedge energy current to finite material-population sectors using a partition of unity \(\eta_i\).

That calculation is algebraically correct in a fixed pressure gauge, but the **individual partial energy currents are not pressure-gauge invariant**. The whole-sphere current is gauge invariant because incompressibility kills the additive pressure constant after integration over the closed sphere.

This distinction must be made canonical before a population label is selected as the energy carrier.

## 2. Pressure gauge

Navier--Stokes pressure is defined up to a spatially constant time-dependent gauge:

\[
\boxed{P\mapsto P+C(\theta).}
\]

The velocity, vorticity, strain, production functional, CE-H geometry, and all pressure gradients/Hessians are unchanged.

The physical/similarity local energy current contains

\[
J_0=(e+P)U-\nu\nabla e.
\]

Under the gauge change,

\[
\boxed{J_0\mapsto J_0+C(\theta)U.}
\]

## 3. Whole-sphere radial flux is gauge invariant

For a closed sphere \(S_R\), incompressibility gives

\[
\int_{S_R}U\cdot n\,dS
=
\int_{B_R}\nabla\cdot U\,dy
=0.
\]

Therefore the full radial energy flux satisfies

\[
\boxed{
\int_{S_R}J_0\cdot n\,dS
\text{ is gauge invariant}.
}
\]

Hence the original M19-269/M19-270 whole-sphere observable \(\Gamma_E\) is safe.

## 4. Partial population flux is gauge dependent

M19-283 defines a localized radial current schematically by

\[
j_i(R)
=
\int_{S_R}\eta_iJ_0\cdot n\,dS.
\]

Under \(P\mapsto P+C\),

\[
\boxed{
j_i(R)
\mapsto
j_i(R)
+C(\theta)
\int_{S_R}\eta_iU_r\,dS.
}
\]

In general,

\[
\int_{S_R}\eta_iU_r\,dS\ne0.
\]

Thus the statement

\[
\text{``population }i\text{ carries positive localized energy current''}
\]

is not canonical unless the pressure gauge is fixed or the localized observable is modified to be gauge invariant.

The partition sum remains safe because

\[
\sum_i\eta_i=1
\]

and the gauge shifts cancel in the whole-sphere total.

## 5. M19-283 correction

M19-283 should therefore be read as conditional on one of the following:

### A. Inherited whole-space pressure gauge

Fix the canonical pressure supplied by the original whole-space solution, e.g. the inherited Riesz/decay normalization when available, and carry that same gauge through every blow-up/ancient representation.

Then the partial currents are well defined relative to that fixed gauge.

This requires a representation-coherence statement:

\[
\boxed{\mathcal T_{pressure}^{gauge\text{-}coherence}.}
\]

### B. Gauge-invariant localized balance

Avoid assigning the pressure-containing partial sphere flux itself and instead use a closed material-population energy balance or a pressure-difference formulation in which additive constants cancel identically.

This is structurally safer.

Without A or B, carrier selection from partial \(j_i\) is not canonical.

## 6. Closed material-population energy is gauge invariant

The M19-284 smooth material-cutoff pressure term is

\[
X_P[\eta]
=
\int PU\cdot\nabla\eta\,dy.
\]

Under \(P\mapsto P+C\), the change is

\[
C\int U\cdot\nabla\eta\,dy
=-C\int\eta\nabla\cdot U\,dy
=0.
\]

Therefore

\[
\boxed{X_P[\eta]\text{ is gauge invariant}.}
\]

Likewise, for a closed material domain, the additive pressure contribution over its complete boundary vanishes by incompressibility.

Hence the M19-284 material energy equation is a safer carrier-level object than a partial open-sphere flux.

## 7. Interface edge currents

An individual pressure edge current across one shared interface can shift under an additive gauge. However the complete closed-boundary pressure work of each material population and the full network balance are gauge invariant.

Thus M19-286's antisymmetric network structure remains valid as a **complete balance**, but an isolated edge's numerical value should not be promoted to a canonical physical observable without a pressure normalization.

## 8. Consequence for M19-287--289

The event-conditioned/hysteresis formulas remain algebraically valid in any one fixed coherent gauge. However a claim that a specific partial population current supplies a gauge-independent dynamical factor requires either

\[
\boxed{\mathcal T_{pressure}^{gauge\text{-}coherence}}
\]

or a reformulation using gauge-invariant closed-population energy observables.

Therefore the current preferred dynamic route is:

\[
\boxed{
\text{production event}
\to
\text{closed material-population energy balance}
\to
\text{conditioned pressure/viscous/dissipation correlation},
}
\]

rather than treating a partial pressure-containing sphere flux as an absolute carrier label.

## 9. Strategic effect

This correction does not invalidate the global M19-269 signed wedge event. It only sharpens the carrier-localization step.

The live options are now:

1. prove coherent inheritance of a canonical whole-space pressure gauge through the ancient representation;
2. use gauge-invariant material energy balances for the finite-lag coupling;
3. retain failure of such representation as an explicit pressure/representation gate.

---

\[
\boxed{\text{M19-290 COMPLETE; WHOLE-SPHERE ENERGY FLUX IS GAUGE SAFE, BUT PARTIAL POPULATION FLUX REQUIRES GAUGE COHERENCE OR GAUGE-INVARIANT REFORMULATION.}}
\]
