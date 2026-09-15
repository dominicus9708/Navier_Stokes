# M19-289 — The event-boundary current is a production–energy hysteresis circulation and vanishes under one-dimensional slaving

**Date:** 2026-09-16  
**Status:** CALCULATION / CONDITIONAL-CORRELATION GEOMETRY / HYSTERESIS-CYCLE FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-287 identifies the fixed-lag event-boundary current, and M19-288 resolves the production marker derivative into explicit Navier--Stokes channels.

The remaining question is whether a nonzero event-boundary mean is a one-way resource or merely recurrent phase circulation.

This module shows that it is a hysteresis/circulation observable in the joint production--energy-current state.

## 2. Two observed coordinates

Write

\[
\boxed{X(\theta):=\mathscr P_A(\theta)}
\]

for the M5-589 annular stretching production functional and

\[
\boxed{Y(\theta):=j_i(z_E,\theta)}
\]

for one selected localized radial energy current.

Let

\[
m=\chi(X)
\]

with \(\chi\) the smooth production-event marker from M19-288.

Up to the fixed q/time generator factor, the event-boundary current is

\[
\boxed{
C_\chi
:=
\left\langle
\chi'(X)\dot X\,Y
\right\rangle.
}
\]

## 3. Exact stationary integration-by-parts identity

Since the recurrent measure is invariant and \(\chi(X)Y\) is an integrable state observable on the controlled compact branch,

\[
\left\langle
\frac d{d\theta}\bigl(\chi(X)Y\bigr)
\right\rangle=0.
\]

Therefore

\[
\boxed{
\left\langle
\chi'(X)\dot X\,Y
\right\rangle
=
-\left\langle
\chi(X)\dot Y
\right\rangle.
}
\]

Thus the production-entry/exit current can equally be read as the energy-current evolution weighted by production occupancy.

It is not a scalar monotone drift.

## 4. One-dimensional slaving forces zero circulation

Suppose the localized energy current is a single-valued function of the production scalar:

\[
\boxed{Y=F(X)}
\]

on the recurrent component.

Choose a primitive \(H\) satisfying

\[
H'(x)=\chi'(x)F(x).
\]

Then

\[
\chi'(X)\dot X\,Y
=
\frac d{d\theta}H(X).
\]

Hence

\[
\boxed{C_\chi=0.}
\]

Therefore

\[
\boxed{
C_\chi\ne0
\Longrightarrow
\text{the energy current is not dynamically slaved to the production scalar alone.}
}
\]

A nonzero event-boundary current certifies genuinely multidimensional recurrent dynamics in the joint observable state.

## 5. Conditional-expectation refinement

Let

\[
F_*(X):=\mathbb E[Y\mid X]
\]

when the conditional expectation is defined. The single-valued part contributes no stationary circulation:

\[
\left\langle
\chi'(X)\dot X\,F_*(X)
\right\rangle=0
\]

under the same regularity/approximation assumptions.

Therefore

\[
\boxed{
C_\chi
=
\left\langle
\chi'(X)\dot X\,igl(Y-F_*(X)\bigr)
\right\rangle.
}
\]

The current is carried by the non-slaved phase component of the energy observable.

## 6. Periodic-orbit interpretation

On a periodic recurrent orbit of period \(T\),

\[
C_\chi
=
\frac1T
\int_0^T
\chi'(X)Y\dot X\,d\theta.
\]

Thus

\[
\boxed{
C_\chi
=
\frac1T
\oint
\chi'(X)Y\,dX.
}
\]

This is a line integral around the closed loop traced by \((X,Y)\) in observable space.

A nonzero value is therefore a hysteresis/circulation effect. It can persist indefinitely while \(X\) and \(Y\) remain bounded.

## 7. Aperiodic recurrent interpretation

For quasiperiodic or more general compact recurrent dynamics there need not be one closed finite-period loop, but the invariant measure can carry a stationary probability current in the \((X,Y)\) factor.

The same event-boundary observable samples that circulating probability current.

Hence

\[
\boxed{
\text{nonzero event-boundary current}
\not\Rightarrow
\text{finite exhaustion or monotone accumulation}.
}
\]

This is structurally the same difficulty exposed abstractly by M19-061--074: compact recurrent dynamics can support nontrivial translation/center factors and circulating bounded observables.

## 8. Relation to M19-271

M19-271 excludes a scalar bounded coboundary as the positive-mean payer.

M19-289 explains one way a non-coboundary mean survives without contradiction:

\[
\boxed{
\text{joint-state circulation/hysteresis}.
}
\]

The event-boundary term is therefore not a hidden monotone scalar. It is a two-observable circulation unless an additional theorem collapses the joint state to one dimension.

## 9. New dichotomy

For the event-boundary branch,

\[
\boxed{
\mathcal T_{event}^{boundary/current}
\Longrightarrow
\mathcal T_{slave}^{P\to J}
\lor
\mathcal T_{cycle}^{P,J},
}
\]

where

- \(\mathcal T_{slave}^{P\to J}\): prove the energy current is a single-valued function of production, which would force the event-boundary mean to vanish;
- \(\mathcal T_{cycle}^{P,J}\): classify/exclude a nontrivial recurrent circulation in the joint production--energy-current factor.

The first is a very strong PDE constitutive/observability theorem. The second is essentially a finite-dimensional shadow of the global recurrent-factor problem.

## 10. Strategic consequence

The finite-lag route has now been reduced far enough that its surviving hard branch reconnects with the factor/observability frontier:

\[
\boxed{
\text{production--energy hysteresis cycle}
\subset
\text{nontrivial recurrent dynamical factor}.
}
\]

Therefore another global unsigned energy budget will not close this branch.

The next useful calculation should test whether the **anchored M5-592 branch** forces one-dimensional slaving between production and energy current, or whether even exact strain-diffusion anchoring leaves an independent phase variable.

If anchoring forces slaving, the event-boundary current vanishes on that branch and only positive projective action remains. If not, the factor problem is genuine even inside the anchored subsystem.

---

\[
\boxed{\text{M19-289 COMPLETE; EVENT-CONDITIONED SIGNED CURRENT IS HYSTERESIS/CIRCULATION, NOT A ONE-WAY BOUNDED RESOURCE.}}
\]
