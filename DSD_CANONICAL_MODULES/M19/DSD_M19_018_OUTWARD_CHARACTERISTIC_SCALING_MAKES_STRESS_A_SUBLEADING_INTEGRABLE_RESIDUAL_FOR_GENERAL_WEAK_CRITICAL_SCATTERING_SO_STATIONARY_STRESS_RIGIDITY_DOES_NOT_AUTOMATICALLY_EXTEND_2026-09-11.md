# M19-018 — Outward-characteristic scaling makes stress a subleading integrable residual for general weak-critical scattering, so stationary stress rigidity does not automatically extend

**Date:** 2026-09-11  
**Status:** CALCULATION / R-CRITICAL STRESS TEST / CHARACTERISTIC RESIDUAL SCALING / STATIONARY-VERSUS-RECURRENT FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-017 shows that a nonzero ergodic weak-critical scattering datum generates a positive-log-density stack of critical Morrey annuli, but ordinary energy/dissipation counting remains geometrically summable.

The next proposed route is momentum stress.

A \(1/R\) velocity tail has

\[
U\otimes U\sim R^{-2},
\qquad
P\sim R^{-2},
\qquad
\nabla U\sim R^{-2},
\]

so the integrated physical-type stress through a sphere can be order one.

Historical stationary-tail modules exploit exactly this critical stress scale.

However the general passive recurrent tail has an additional leading dilation/time-transport channel. M5-563/567 already contains the exact calculation showing that along outward similarity characteristics the nonlinear/viscous/stress residual is multiplied by \(R^{-2}\) and is integrable.

The present module records the consequence: stationary stress rigidity cannot be transplanted unchanged to the aperiodic recurrent scattering branch.

## 2. Similarity velocity equation

In viscosity-one backward similarity variables,

\[
\boxed{
\partial_\theta U
+\frac12 y\cdot\nabla U
+\frac12U
+(U\cdot\nabla)U
+\nabla P
=\Delta U,
\qquad
\nabla\cdot U=0.
}
\]

The first three terms are the similarity transport/dilation operator.

For a critical tail \(U\sim R^{-1}\), these terms are of order \(R^{-1}\), whereas

\[
(U\cdot\nabla)U,
\quad
\nabla P,
\quad
\Delta U
\]

are of order \(R^{-3}\) pointwise.

Thus the leading critical tail is transported primarily by similarity dilation, not by a stationary elliptic balance.

## 3. Outward characteristic

Let

\[
R(\tau)=R_0e^{\tau/2}
\]

and define the critical amplitude along the outward characteristic by

\[
\boxed{
V(\xi,\tau)
:=
R(\tau)
U(R(\tau)\xi,\theta_0+\tau).
}
\]

The choice of \(R(\tau)\) exactly follows the dilation characteristic of

\[
\partial_\theta+\frac12 y\cdot\nabla.
\]

M5-563 computes the resulting equation

\[
\boxed{
\partial_\tau V
=
R_0^{-2}e^{-\tau}
\mathcal R[V,P].
}
\]

On the passive spectator branch,

\[
\|\mathcal R[V,P]\|_X
\le C_{spec}
\]

in the retained fixed-annulus norm.

## 4. The residual is integrable

Therefore

\[
\|\partial_\tau V\|_X
\le
C_{spec}R_0^{-2}e^{-\tau}.
\]

Integrating from \(\tau_1\) to infinity,

\[
\boxed{
\|V(\tau_1)-A(q)\|_X
\le
C R_0^{-2}e^{-\tau_1}.
}
\]

Thus the total future nonlinear/viscous/stress correction to the critical amplitude is finite and decays quadratically in radius.

The leading datum

\[
A(q,\omega)
\]

survives as free asymptotic scattering data subject to the divergence-free and recurrence constraints already identified.

## 5. Why an order-one integrated stress does not contradict Section 4

Pointwise stress density is of order

\[
R^{-2}.
\]

Multiplying by sphere area \(R^2\) can produce an order-one integrated stress flux.

But the equation for the **critical amplitude** \(V=RU\) contains the stress/nonlinear residual after two inverse powers of radius relative to the leading dilation transport.

These statements are compatible:

- sphere-integrated momentum stress is critical as a surface quantity;
- its effect on the transported leading \(1/R\) amplitude along an outward characteristic is subleading and integrable.

Thus one cannot infer that an order-one surface stress forces the scattering amplitude to decay.

## 6. Stationary branch is exceptional

If

\[
\partial_\theta U=0
\]

and the tail is exactly stationary/self-similar, the time-translation degree of freedom is absent.

The leading scattering datum is constant in \(q\), and the remaining spatial equation can be attacked through stationary stress, Pohozaev, point-force, and Landau/Carleman identities.

Historical M5 stationary-tail modules exploit this special structure.

But for a general recurrent datum,

\[
A=A(q,\omega),
\qquad
q=\log R-\theta/2,
\]

the change in \(q\) supplies a leading transport channel.

Therefore

\[
\boxed{
\text{stationary critical-tail rigidity}
\not\Rightarrow
\text{aperiodic recurrent critical-tail rigidity}.
}
\]

A new argument must control the translation dynamics of \(A\), not simply reuse a stationary stress identity.

## 7. DSS branch is also structurally special

For a discretely self-similar state, \(A(q)\) is periodic in \(q\).

Periodic structure may allow integration over one log-period to cancel the leading translation derivative and expose a net stress identity.

However this is an additional periodicity hypothesis.

It does not apply to a general aperiodic ergodic scattering measure.

Thus the critical root naturally separates into

\[
\boxed{
\text{stationary/DSS special dynamics}
\lor
\text{aperiodic translation dynamics}.
}
\]

## 8. Mean stress alone is insufficient without a q-cocycle

Suppose one defines a sphere stress observable

\[
\mathcal F(q,A).
\]

Under the scattering translation,

\[
A(q)\mapsto A(q-s),
\]

a recurrent invariant measure can have

\[
\langle\mathcal F\rangle=0
\]

while \(\mathcal F\) fluctuates with nonzero total variation.

Conversely a nonzero invariant mean stress need not contradict recurrence unless it is the derivative of a bounded state quantity or is incompatible with the smooth unforced core.

Therefore the missing stress theorem must supply an actual **q-cocycle or source matching law**, not merely a nonzero stress magnitude.

## 9. Relation to the conditional CE-H harmonic dipole

Under M17-349's extra CE-H coefficient-compact exterior-line hypotheses, the exterior vorticity becomes harmonic.

M17-350 then reduces the weak-critical obstruction to a finite-dimensional toroidal dipole coefficient.

That conditional branch has much stronger spatial structure than the general scattering datum and may admit a direct stress/topology calculation.

The present no-go concerns the **general upstream weak-critical scattering root**.

## 10. R-critical status after the stress test

The following routes are now removed as generic closures:

\[
\boxed{
\begin{aligned}
&\text{finite energy summation across critical scales},\\
&\text{positive log-density plus energy summation},\\
&\text{global strong-}L^3\text{ recurrent scattering},\\
&\text{direct transplantation of stationary stress rigidity to aperiodic scattering}.
\end{aligned}
}
\]

The retained general root is

\[
\boxed{
\text{nonzero weak-critical scattering datum with aperiodic/ergodic log-translation dynamics}.
}
\]

## 11. Next calculation

Two directions remain mathematically distinct.

1. **q-cocycle route:** derive a bounded or finite-defect observable whose log-radius derivative sees the recurrent scattering stress/current.
2. **conditional CE-H dipole route:** under the already analyzed coefficient-compact harmonic exterior branch, calculate the toroidal dipole's material/current consequences directly.

The second is narrower but has more rigid structure and can be tested immediately without claiming closure of the full R-critical root.

---

\[
\boxed{\text{M19-018 COMPLETE; GENERAL R-CRITICAL REMAINS AN APERIODIC WEAK-SCATTERING RIGIDITY PROBLEM.}}
\]
