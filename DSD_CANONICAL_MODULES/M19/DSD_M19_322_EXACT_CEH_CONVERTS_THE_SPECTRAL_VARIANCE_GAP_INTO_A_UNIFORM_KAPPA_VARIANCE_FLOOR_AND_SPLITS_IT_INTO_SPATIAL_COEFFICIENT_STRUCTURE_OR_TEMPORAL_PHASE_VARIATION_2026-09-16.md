# M19-322 — Exact CE-H converts the spectral-variance gap into a uniform kappa-variance floor and splits it into spatial coefficient structure or temporal phase variation

**Date:** 2026-09-16  
**Status:** CONDITIONAL EXACT CE-H THEOREM / COEFFICIENT-VARIANCE FLOOR / SPATIAL-TEMPORAL ROUTING

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Scope

M19-321 is branch-independent and proves a uniform radial spectral-variance gap on the canonical second-generation interior packet.

The present module specializes that result to the exact CE-H compact lane.

The exact CE-H relation is assumed on the same ancient record-limit field over one fixed normalized spacetime cell:

\[
\boxed{\Delta\Omega=\kappa\Omega.}
\]

If global CE-H representation, H2 tightness, or domain/interface coherence fails, that failure remains an explicit exit and this module is not applied silently.

## 2. Record-limit charges

On a fixed normalized time interval `I`, define

\[
q_0
:=
\int_I\int_{\mathbb R^3}|\Omega|^2dxds,
\]

\[
q_1
:=
\int_I\int_{\mathbb R^3}|\nabla\Omega|^2dxds,
\]

and

\[
q_2
:=
\int_I\int_{\mathbb R^3}|\Delta\Omega|^2dxds.
\]

On the compact retained carrier these inherit the M19-319 bounds

\[
0<c_k\le q_k\le C_k<\infty,
\qquad k=0,1,2,
\]

or else the missing global passage is itself a derivative-tail/interface compactness defect.

M19-321 gives

\[
\boxed{
\mathcal V
:=
q_2-rac{q_1^2}{q_0}
\ge c_{var}>0.
}
\]

## 3. Exact CE-H moment identities

Because

\[
\Delta\Omega=\kappa\Omega,
\]

we have

\[
q_2
=
\int_I\int\kappa^2|\Omega|^2dxds.
\]

Integration by parts on the whole space gives

\[
q_1
=
-\int_I\int\Omega\cdot\Delta\Omega\,dxds
=
-\int_I\int\kappa|\Omega|^2dxds.
\]

Define the spacetime enstrophy-weighted probability measure

\[
\boxed{
 d\mathbb P_\Omega(x,s)
 :=
 \frac{|\Omega(x,s)|^2}{q_0}\,dxds.
}
\]

Then

\[
\boxed{
\mathbb E_\Omega[\kappa]
=-\frac{q_1}{q_0},
}
\]

and

\[
\boxed{
\mathbb E_\Omega[\kappa^2]
=\frac{q_2}{q_0}.
}
\]

Therefore

\[
\boxed{
\operatorname{Var}_\Omega(\kappa)
=
\frac{q_2}{q_0}
-
\left(\frac{q_1}{q_0}\right)^2
=
\frac{\mathcal V}{q_0}.
}
\]

## 4. Uniform coefficient-variance floor

Since

\[
\mathcal V\ge c_{var}
\]

and

\[
q_0\le C_0,
\]

we obtain

\[
\boxed{
\operatorname{Var}_\Omega(\kappa)
\ge
\frac{c_{var}}{C_0}
=:c_\kappa>0.
}
\]

Thus an exact CE-H canonical interior packet cannot have an almost constant coefficient `kappa` in the spacetime enstrophy-weighted sense.

The variance is quantitatively order one in normalized variables.

## 5. Consequence: constant-kappa CE-H is impossible on the carrier

If `kappa` were constant almost everywhere on the enstrophy-bearing spacetime cell, then

\[
\operatorname{Var}_\Omega(\kappa)=0,
\]

contradicting Section 4.

Hence

\[
\boxed{
\text{nontrivial compact CE-H carrier}
\Longrightarrow
\text{quantitative coefficient segregation}.
}
\]

This is stronger than the qualitative statement that a nonzero whole-space L2 eigenfunction of the Laplacian cannot live on one exact Fourier sphere.

## 6. Spatial-temporal law of total variance

For each time with

\[
E(s):=\int|\Omega(x,s)|^2dx>0,
\]

define the spatial enstrophy-weighted probability

\[
 d\pi_s(x)
 :=
 \frac{|\Omega(x,s)|^2}{E(s)}dx
\]

and the spatial weighted coefficient mean

\[
\bar\kappa(s)
:=
\int\kappa(x,s)d\pi_s(x).
\]

Define the time probability

\[
\boxed{
 d\nu(s)
 :=
 \frac{E(s)}{q_0}ds.
}
\]

Then

\[
d\mathbb P_\Omega=d\pi_s\,d\nu(s).
\]

The law of total variance gives exactly

\[
\boxed{
\operatorname{Var}_\Omega(\kappa)
=
\mathbb E_\nu
\left[
\operatorname{Var}_{\pi_s}(\kappa)
\right]
+
\operatorname{Var}_\nu
\left(\bar\kappa(s)\right).
}
\]

Hence at least one branch satisfies

\[
\boxed{
\mathbb E_\nu
\left[
\operatorname{Var}_{\pi_s}(\kappa)
\right]
\ge\frac{c_\kappa}{2}
}
\]

or

\[
\boxed{
\operatorname{Var}_\nu(\bar\kappa)
\ge\frac{c_\kappa}{2}.
}
\]

## 7. Spatial coefficient-variance branch

On this branch a positive weighted set of snapshots has nontrivial within-state spatial kappa variance.

If that variance remains inside one bounded active component with

\[
\rho=|\Omega|\ge a_0>0
\]

and a uniform Poincare/connectivity geometry, the M18-065 transition argument yields a quantitative coefficient-gradient event:

\[
\boxed{
\int |\nabla\kappa|^2
\ge c_{\nabla\kappa}>0
}
\]

on a positive recurrent state set, after the standard threshold/thickness extraction.

If the variance is realized only through

- separated components,
- thin necks,
- passages through `rho=0`,
- unbounded spatial radii,
- loss of CE-H domain/interface coherence,

then the branch is already routed to the corresponding component/zero/interface/remote-critical exit.

Thus spatial variance creates no new untyped survivor.

## 8. Temporal coefficient-phase branch

The spatial mean has an exact derivative-ratio interpretation.

At each time,

\[
P(s):=\|\nabla\Omega(s)\|_2^2
=
-\int\kappa|\Omega|^2dx.
\]

Therefore

\[
\boxed{
\bar\kappa(s)
=-\frac{P(s)}{E(s)}.
}
\]

Hence the temporal branch is equivalently

\[
\boxed{
\operatorname{Var}_\nu
\left(
\frac{P}{E}
\right)
\ge
\frac{c_\kappa}{2}.
}
\]

So the effective enstrophy-weighted squared frequency cannot remain temporally constant over the normalized record cell.

The packet must execute a nontrivial recurrent frequency/coefficient phase motion.

This is a phase/hysteresis quantity, not a monotone resource.

If temporal equicontinuity fails, it routes to time-jet/frequency decompactification. If it holds, the coefficient ratio has repeated finite-width transitions.

## 9. Relation to M18-062--069

M18-062 forces amplitude-growth covariance.

M18-069 splits its coefficient part into normalized diffusion depletion versus strain segregation.

M19-322 supplies an independent source of mandatory coefficient variation: the interior carrier's spatial localization and spectral uncertainty.

Thus even before invoking the multi-p amplitude tilt, the exact CE-H compact carrier must carry quantitative kappa heterogeneity in space, time, or both.

The two mechanisms are compatible and can be combined in future work.

## 10. Representation firewall

The identities of Sections 3--4 require exact global CE-H on the charge-bearing field and enough decay/tightness for whole-space integration by parts.

If only local CE-H is available while q1/q2 charge escapes through the complement, then the correct conclusion is

\[
\boxed{
\text{CE-H coefficient variance}
\lor
\text{derivative-tail / interface / representation loss}.
}
\]

Do not silently attribute escaped derivative charge to kappa.

## 11. What this does not prove

A positive kappa variance is compatible with compact recurrence.

The spatial branch may pay derivative/interface cost that remains ancestry-summable, while the temporal branch may form a bounded hysteresis loop.

Therefore

\[
\boxed{
\operatorname{Var}_\Omega(\kappa)>0
\not\Rightarrow
\text{global contradiction}.
}

The gain is a new rigidity restriction on the compact exact CE-H survivor.

## 12. Next target

The most promising next calculation is to combine

\[
\operatorname{Var}_\Omega(\kappa)\ge c_\kappa
\]

with the CE-H line constraint

\[
D_\xi\kappa=0.
\]

Since kappa is constant along each vortex line, any spatial kappa variance must be **transverse to the vorticity-line foliation**.

Thus a bounded-core spatial-variance state necessarily contains transverse coefficient separation between distinct vortex lines or active components.

Quantifying the minimum transverse interface/line-packing geometry needed to support the variance may connect directly to the mesoscopic carrier and coefficient-gradient branches of late M17.

---

\[
\boxed{\text{M19-322 COMPLETE; EXACT CE-H FORCES A UNIFORM ENSTROPHY-WEIGHTED KAPPA VARIANCE.}}
\]