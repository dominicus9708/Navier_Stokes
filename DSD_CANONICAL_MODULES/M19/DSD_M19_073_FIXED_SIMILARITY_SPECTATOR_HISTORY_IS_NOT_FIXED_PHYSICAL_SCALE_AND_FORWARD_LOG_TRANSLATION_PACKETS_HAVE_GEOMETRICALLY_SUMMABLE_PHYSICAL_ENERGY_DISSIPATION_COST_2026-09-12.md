# M19-073 — Fixed similarity spectator history is not fixed physical scale, and forward log-translation packets have geometrically summable physical energy/dissipation cost

**Date:** 2026-09-12  
**Status:** CALCULATION / SCATTERING GENEALOGY / FIXED-SPECTATOR PHYSICAL-SCALING FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-072 reduced global scattering noncompactness to translation escape in the log-radius variable \(q\).  Since

\[
q=\log R_{spec}-\theta/2
\]

at one fixed spectator radius, it is tempting to reinterpret a translated packet as repeated activity at one fixed boundary and then charge infinitely many events to one finite physical-time budget.

That inference is false because \(R_{spec}\) is fixed only in **similarity coordinates**.  The corresponding physical sphere shrinks toward the singular point as similarity time advances.

This module computes the exact scale conversion.  Forward-separated spectator events have geometrically decreasing physical energy and dissipation costs, so infinitely many such events remain compatible with finite physical budgets.

## 2. Similarity-to-physical variables

Let

\[
\tau:=T_*-t,
\qquad
\theta:=-\log\tau
\]

up to an irrelevant additive normalization.

Use the standard backward similarity scaling

\[
\boxed{
 y=\frac{x-x_*}{\sqrt\tau},
\qquad
 u(x,t)=\tau^{-1/2}U(y,\theta).
}
\]

Then

\[
\boxed{dt=\tau\,d\theta}
\]

in absolute value along forward physical time.

## 3. A fixed similarity sphere shrinks physically

The sphere

\[
|y|=R_{spec}
\]

corresponds to physical radius

\[
\boxed{
 r_{phys}(\theta)
=R_{spec}\sqrt\tau
=R_{spec}e^{-\theta/2}.
}
\]

Therefore

\[
\boxed{
\text{fixed similarity boundary}
\neq
\text{fixed physical boundary}.
}
\]

A shift by \(\Delta\theta=2n\) changes the physical observation scale by

\[
\boxed{
 r_{phys}(\theta+2n)
=e^{-n}r_{phys}(\theta).
}
\]

## 4. Relation to the scattering coordinate

At fixed \(R_{spec}\),

\[
q=\log R_{spec}-\frac\theta2.
\]

Hence forward similarity-time translation by \(2n\) acts as

\[
\boxed{q\mapsto q-n.}
\]

Thus the physically relevant forward translation-escape sequence is a packet shifted toward **negative** \(q\) as \(\theta\to+\infty\).

The sign is important: shifts toward positive \(q\) correspond to going backward along the complete ancient history.

## 5. Physical kinetic energy of one fixed-similarity shell

At fixed similarity annulus \(\mathcal A_{R_{spec}}\),

\[
|u|^2=\tau^{-1}|U|^2,
\qquad
 dx=\tau^{3/2}dy.
\]

Therefore the physical kinetic energy carried by that similarity shell is

\[
\boxed{
E_{phys}^{shell}(t)
=
\tau^{1/2}
\int_{\mathcal A_{R_{spec}}}|U(y,\theta)|^2dy.
}
\]

If the normalized critical shell energy is order one on recurrent events, then

\[
\boxed{E_{phys}^{shell}\asymp e^{-\theta/2}.}
\]

Thus later recurrent similarity events become cheaper in the parent physical energy.

## 6. Physical dissipation over one O(1) similarity-time event

Spatial derivatives scale as

\[
\nabla_xu
=\tau^{-1}\nabla_yU.
\]

Hence

\[
\int_{shell}|\nabla_xu|^2dx
=
\tau^{-1/2}
\int_{\mathcal A_{R_{spec}}}|\nabla_yU|^2dy.
\]

Multiplying by

\[
dt=\tau d\theta,
\]

gives

\[
\boxed{
\nu\int_{event}\int_{shell}|\nabla_xu|^2dxdt
=
\nu\int_{event}
\tau^{1/2}
\left(
\int_{\mathcal A_{R_{spec}}}|\nabla_yU|^2dy
\right)d\theta.
}
\]

For an \(O(1)\)-duration similarity event with normalized Dirichlet charge bounded above and below,

\[
\boxed{
D_{phys}^{event}\asymp e^{-\theta/2}.
}
\]

## 7. Forward-separated recurrent events are geometrically summable

Take event times

\[
\theta_n=\theta_0+2nT_0,
\qquad T_0>0.
\]

Then

\[
\tau_n^{1/2}
=e^{-\theta_n/2}
=e^{-\theta_0/2}e^{-nT_0}.
\]

Therefore both the physical shell-energy scale and one-event physical dissipation satisfy

\[
\boxed{
\sum_{n=0}^\infty e^{-\theta_n/2}<\infty.
}
\]

Thus

\[
\boxed{
\text{infinitely many separated similarity-boundary events}
\not\Rightarrow
\text{infinite physical energy/dissipation}.}
\]

This is the same critical summability mechanism previously seen in M19-014, now expressed directly in the finite spectator-boundary history.

## 8. Why this does not contradict M19-069

M19-069 showed that the outward map from spectator history to scattering data is near identity in the quiet strong norm.  M19-073 shows that repeated finite-spectator events do not automatically accumulate an unsummable **physical** cost because the spectator surface itself shrinks physically.

Hence the two facts are compatible:

\[
\boxed{
\text{boundary degrees survive outward propagation}
\quad\text{and}\quad
\text{their forward physical costs can still be summable}.}
\]

## 9. Backward ancient direction is a genealogy problem, not one parent-time budget

As \(\theta\to-\infty\), fixed similarity radius corresponds to increasing physical scale in the original similarity reconstruction.

For a blowup-limit ancient solution, that direction cannot be charged naively to one finite terminal interval of the original parent solution.  It is exactly where the second-generation/ancestry orientation firewalls developed in M18 become relevant.

Therefore neither direction of the complete \(q\)-translation line admits a simple fixed-parent unsigned budget argument:

- forward \(\theta\): physical costs are geometrically summable;
- backward \(\theta\): one exits the fixed terminal parent window and enters genealogy/ancestry bookkeeping.

## 10. Consequence for the translation-escape strategy

M19-072 suggested that translated packets at one spectator boundary might be eliminated by a nonreusable physical-time budget.

M19-073 closes that shortcut:

\[
\boxed{
\text{fixed-similarity-boundary recurrence does not remove the critical scaling discount.}
}
\]

The missing rigidity must therefore compare the **shape/dynamics** of separated spectator histories, not merely add their unsigned physical energy or dissipation costs.

## 11. Certified / not certified

### Certified

1. Fixed similarity radius corresponds to physical radius \(R_{spec}e^{-\theta/2}\).
2. Forward shift \(q\mapsto q-n\) corresponds to physical scale decrease by \(e^{-n}\).
3. Physical kinetic energy of a fixed normalized spectator shell carries factor \(e^{-\theta/2}\).
4. Physical dissipation of an \(O(1)\) similarity-time spectator event carries the same factor.
5. Therefore infinitely many forward separated recurrent boundary events can have geometrically summable physical cost.

### Not certified

1. Rigidity of the spectator-boundary time history.
2. Nonexistence of a signed or relative finite-boundary invariant.
3. One-dimensionality of the recurrent center cocycle.
4. Global weak-critical scattering rigidity.
5. Global 3D Navier--Stokes regularity.

## 12. Next target

Unsigned physical budgets at the spectator boundary are now exhausted by scaling.  The next useful object must be **relative between two times/phases**, so that the common critical scaling factor cancels.

M19-074 should examine the normalized difference of two spectator profiles separated by a recurrence time \(T\):

\[
\boxed{
D_T(\theta)
:=
\left\|
R_{spec}U(R_{spec}\cdot,\theta+T)
-
R_{spec}U(R_{spec}\cdot,\theta)
\right\|_X.
}
\]

Through M19-069 this is equivalent up to \(O(R_{spec}^{-2})\) to the scattering translation difference

\[
\|A(q-T/2)-A(q)\|_X.
\]

The key question is whether recurrence plus parabolic uniqueness gives a monotonicity/three-cylinder estimate for \(D_T\), or whether quasiperiodic histories can keep \(D_T\) bounded and recurrent without contradiction.

---

\[
\boxed{\text{M19-073 COMPLETE; FIXED-SPECTATOR HISTORY RETAINS THE SAME CRITICAL PHYSICAL SUMMABILITY THAT BLOCKED EARLIER UNSIGNED ANCESTRY CLOSURE.}}
\]
