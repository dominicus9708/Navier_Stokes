# DSD M19-096 — Pineau–Vicol one-slice Type-I regularity converts any surviving singular recurrent branch into a uniform late-time speed floor

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / EXTERNAL 2026 REGULARITY THEOREM USED AS A CONDITIONAL APPLICATION GATE / A TYPE-I SINGULAR SURVIVOR WITH THE REQUIRED PRESSURE-ANNULUS BOUND CAN NEVER BECOME SUFFICIENTLY SLOW AT EVEN ONE LATE SIMILARITY TIME / THIS DOES NOT EXCLUDE FAST PERIODIC OR QUASIPERIODIC RECURRENCE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. External input

Pineau--Vicol (2026), arXiv:2607.09619v2, Theorem 1.9, proves a local regularity criterion for a smooth 3D Navier--Stokes solution in a unit parabolic cylinder.

In the unit-viscosity normalization, assume

\[
|u(x,t)|\le \frac{C_u}{\sqrt{-t}+|x|}
\]

and a bounded pressure on a fixed physical annulus away from the candidate singular point.

There exist constants

\[
\delta_0=\delta_0(C_u)>0,
\qquad
s_0=s_0(C_u,C_p)
\]

such that if at one time `bar s >= s0` the similarity velocity

\[
U(y,s)=\sqrt{-t}\,u(x,t),
\qquad t=-e^{-s},
\]

satisfies

\[
\|\partial_sU(\cdot,\bar s)\|_{L^\infty(B_{e^{\bar s/2}})}\le\delta_0,
\]

then the top center is a regular point.

Their Remark 1.11 permits the weaker one-slice hypothesis

\[
\int_{B_{e^{\bar s/2}}}
|\partial_sU(y,\bar s)|
(1+|y|)e^{-|y|^2/8}dy
\le c_*\delta_0
\]

for a universal constant `c_*`.

For repository viscosity `nu>0`, use the standard viscosity normalization before applying the theorem and translate the constants back. No viscosity-independent constant is asserted here.

---

## 2. Applicability firewall

The theorem is used only on an M19 branch where both of the following have been independently certified in the original physical cylinder:

1. the required local Type-I velocity bound;
2. the required bounded pressure on a fixed physical annulus away from the candidate singular point.

The recurrent similarity construction alone does not automatically certify the pressure-annulus hypothesis.

Failure of this application gate remains a separate pressure/nonlocal/root-certification issue and must not be hidden.

---

## 3. Define the Gaussian similarity-speed functional

Set

\[
\boxed{
\mathcal V_G(s)
:=
\int_{B_{e^{s/2}}}
|\partial_sU(y,s)|
(1+|y|)e^{-|y|^2/8}dy.
}
\]

Because the Gaussian weight localizes strongly, on the retained smooth similarity corridor this is effectively an interior similarity-speed observable even though the formal ball grows like `e^{s/2}`.

---

## 4. Contrapositive speed-floor theorem

Suppose the top center is genuinely singular and the Pineau--Vicol application gate holds.

If there existed any

\[
\bar s\ge s_0
\]

such that

\[
\mathcal V_G(\bar s)\le c_*\delta_0,
\]

Theorem 1.9 and Remark 1.11 would imply regularity at the candidate singular point, contradiction.

Therefore every surviving singular branch must satisfy

\[
\boxed{
\mathcal V_G(s)>c_*\delta_0
\qquad\forall s\ge s_0.
}
\]

Write

\[
\boxed{
v_*:=c_*\delta_0>0.}
\]

Then

\[
\boxed{
\inf_{s\ge s_0}\mathcal V_G(s)\ge v_*.
}
\]

This is a genuine new quantitative restriction on any Type-I singular recurrent survivor to which the external theorem applies.

---

## 5. Immediate consequences

### Stationary self-similar branch

If

\[
\partial_sU\equiv0,
\]

then `V_G=0`, so the singular branch is excluded by the one-slice criterion whenever its hypotheses hold.

### Near-stationary recurrent visits

If recurrence ever produces a time sequence

\[
s_n\to\infty
\]

with

\[
\mathcal V_G(s_n)\to0,
\]

then the candidate singularity is excluded.

Thus surviving recurrence must be uniformly non-slow in the Gaussian interior observable.

---

## 6. What recurrence does not give

Poincare recurrence or almost-periodicity gives small displacement after a return time:

\[
U(s+T_n)-U(s)\to0
\]

in an appropriate local topology.

It does **not** imply

\[
\partial_sU(s_n)\to0.
\]

A constant-speed periodic orbit and an irrational torus flow are elementary countermodels.

Therefore

\[
\boxed{
\text{recurrence}\not\Rightarrow\text{one-slice approximate self-similarity}.
}
\]

The new theorem supplies a speed floor for survivors; it does not by itself close recurrent dynamics.

---

## 7. Relation to M19-075--095

M19-095 reduces the realizable nonnegative cocycle spectrum to a finite-dimensional interior bundle.

M19-096 adds that the base flow direction itself cannot become arbitrarily small in the Gaussian self-similar-speed observable on a surviving singular branch.

Hence the recurrent survivor, after rotational quotient, is a finite-dimensional center flow with a uniformly nonvanishing time vector field on the late-time singular component, unless the pressure/Type-I application gate fails.

This excludes equilibria in the certified application lane.

It does not exclude periodic circles or higher-dimensional recurrent tori.

---

## 8. Revised center split

On the certified Type-I/pressure lane,

\[
\boxed{
\text{late recurrent singular center}
\Longrightarrow
\begin{cases}
\text{uniformly fast one-dimensional periodic/DSS orbit},\\
\text{or finite-dimensional extra-center recurrent dynamics}.
\end{cases}
}
\]

The aperiodic case still requires the M19-090--095 center-index program.

The periodic case still requires the M19-092 DSS critical-tail program.

---

## 9. Citation boundary

The external theorem is not claimed here for arbitrary weak solutions or arbitrary recurrent similarity states. It is used exactly under its Type-I, pressure-annulus, smoothness, and one-slice hypotheses.

Reference:

- D. Pineau and V. Vicol, *On rotated backwards self-similar solutions of the incompressible 3D Navier--Stokes equations*, arXiv:2607.09619v2 (2026), Theorem 1.9 and Remark 1.11.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
