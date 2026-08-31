# DSD M5-411 — Generic projective interface: retained material-axis action or flux replacement

Date: 2026-08-31

Status: **A GENERIC PROJECTIVE LABEL DOES NOT NEED TO REMAIN AN INDEPENDENT TERMINAL ON A FORMED ACTIVE CARRIER / IF THE SAME MATERIAL HIGH-VORTICITY CARRIER PERSISTS, AN ORDER-ONE CHANGE OF ITS VORTICITY AXIS IS GOVERNED BY THE EXACT DIRECTION EQUATION AND FORCES EITHER ORDER-ONE TILT-STRAIN ACTION OR ORDER-ONE DIRECTIONAL-DIFFUSION ACTION / IF NO SINGLE MATERIAL ACTIVE CARRIER PERSISTS, THE APPARENT AXIS CHANGE IS ACTUALLY THRESHOLD EXIT, FLUX REPLACEMENT, OR REFORMATION AND ENTERS THE M5-393--397 FINITE-MEMORY FLUX LEDGER / DIRECTION IS NEVER USED THROUGH ZERO VORTICITY / THUS THE GENERIC PROJECTIVE TERMINAL IS ABSORBED INTO LOCAL CRITICAL AXIS ACTION OR ALREADY-TYPED FLUX/REMOTE INTERFACE, WITHOUT RELYING ON THE NARROWER POSITIVE-MIDDLE ANTI-RIBBON THEOREM / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Purpose

M5-407 retained

\[
T_{interface}^{projective/export/realization}
\]

because the older projective viscous-tax theorem was proved on a coherent positive-middle anti-ribbon corridor and could not safely be applied to arbitrary direction defects.

That scope firewall remains correct.

However a more primitive split is available which does not use positive-middle geometry.

The word `projective` can describe two mathematically different events:

1. the **same material active carrier** changes its vorticity axis;
2. the active axis at the next observation belongs to **different material/flux ancestry**.

Only the first is a genuine material-axis rotation. The second is replacement/reformation.

This note separates them.

---

## 2. Active material corridor

Let a material trajectory or retained material carrier satisfy, on a time interval `J`,

\[
\boxed{
|\omega(X(a,t),t)|
\ge
\eta W(t)
>0,
\qquad t\in J,
}
\]

for a fixed `eta>0`.

Then the vorticity direction

\[
\xi
:=
\frac\omega{|\omega|}
\]

is well defined on this active material corridor.

The exact Navier--Stokes vorticity equation yields the direction equation

\[
\boxed{
D_t\xi
=
\tau
+
\frac\nu{|\omega|}
(I-\xi\otimes\xi)\Delta\omega,
}
\]

where

\[
\tau
:=(I-\xi\otimes\xi)S\xi.
\]

This identity requires no positive-middle eigenvalue hypothesis.

---

## 3. Order-one projective change

Suppose the retained material axis changes by a projective angle at least

\[
\delta_0>0
\]

over `J`.

Using the length of the path on the unit sphere/projective sphere,

\[
\delta_0
\le
\int_J|D_t\xi|dt.
\]

Hence

\[
\delta_0
\le
\int_J|\tau|dt
+
\nu\int_J
\frac{|(I-\xi\otimes\xi)\Delta\omega|}
{|\omega|}dt.
\]

Therefore at least one of the two alternatives holds:

\[
\boxed{
\int_J|\tau|dt
\ge\frac{\delta_0}{2}
}
\]

or

\[
\boxed{
\nu\int_J
\frac{|(I-\xi\otimes\xi)\Delta\omega|}
{|\omega|}dt
\ge\frac{\delta_0}{2}.
}
\]

This is an exact projective-action fork.

---

## 4. Natural first-hitting scaling

On a first-hitting carrier with natural scale

\[
r=\sqrt{\frac\nu W},
\]

write normalized time

\[
d\sigma=\frac\nu{r^2}dt.
\]

Then the tilt strain scales as

\[
\tau_{phys}
=\frac\nu{r^2}\widetilde\tau,
\]

while

\[
\omega_{phys}
=\frac\nu{r^2}\Omega
\]

and

\[
\Delta_x\omega_{phys}
=\frac\nu{r^4}\Delta_Y\Omega.
\]

Therefore both terms in the direction equation are scale critical:

\[
\int_J|\tau|dt
=
\int_{\widehat J}|\widetilde\tau|d\sigma,
\]

and

\[
\nu\int_J\frac{|\Delta\omega|}{|\omega|}dt
=
\int_{\widehat J}
\frac{|\Delta_Y\Omega|}{|\Omega|}d\sigma.
\]

Thus an order-one material-axis turn costs an order-one normalized action independent of `r`.

---

## 5. Tilt-driven projective action is local critical H

If

\[
\int_J|\tau|dt
\ge\delta_0/2,
\]

then the carrier pays a nontrivial transverse strain action.

This is not a vague geometric turnover label. It is one of the exact active strain channels in the decomposition

\[
|S|^2
=\frac32\gamma^2+2|\tau|^2+|D_\perp|^2.
\]

Therefore

\[
\boxed{
\text{retained-axis projective change through tilt}
\Longrightarrow
H_{\tau,act}^{crit}.
}
\]

The stronger older anti-ribbon theorem may convert this action to an explicit viscous frequency tax under its additional hypotheses, but that refinement is not needed for the present classification.

---

## 6. Diffusion-driven projective action is derivative/capacity H

Suppose instead

\[
\nu\int_J
\frac{|(I-\xi\otimes\xi)\Delta\omega|}
{|\omega|}dt
\ge\delta_0/2.
\]

On the active corridor

\[
|\omega|\ge\eta W,
\]

so no small denominator is hidden.

In normalized variables,

\[
\int_{\widehat J}
|\Delta_Y\Omega|d\sigma
\gtrsim
\eta\delta_0.
\]

Stage-wide analyticity bounds each fixed derivative pointwise, so the correct interpretation is not parent-scale pointwise derivative blowup.

The event is a finite critical **directional diffusion action** over space-time. If it becomes concentrated on smaller internal scales, it is frequency/capacity H; if it remains formed at the natural scale, it is a local derivative-occupancy action.

Thus

\[
\boxed{
\text{retained-axis projective change through diffusion}
\Longrightarrow
H_{dir\,diff/freq/cap}^{crit}.
}
\]

---

## 7. Crossing low vorticity is not a projective rotation

The direction `xi` is undefined where

\[
\omega=0.
\]

More generally, if the tracked material carrier leaves the active region

\[
|\omega|\ge\eta W,
\]

and later a different high-vorticity axis appears, one must not connect the two directions by a fictitious continuous projective path through the low-vorticity interval.

That event is instead

\[
\boxed{
\text{active-threshold exit/re-entry}
\lor
\text{carrier replacement/reformation}.
}
\]

This is a DSD domain firewall: an undefined direction cannot accumulate artificial angle action.

---

## 8. No retained material carrier means flux genealogy turnover

Suppose the current and later formed carriers have different active axes but there is no material high-vorticity lineage satisfying the corridor of Section 2.

Then the projective label is only observational.

At the flux level M5-393--395 distinguish old material contact from actual vorticity-flux ancestry and prove that fixed target-volume replacement creates a fixed target flux

\[
\Phi_{new}\gtrsim c\nu.
\]

M5-397 then gives finite local material-flux memory.

Therefore

\[
\boxed{
\text{axis change without retained material active ancestry}
\Longrightarrow
H_{viscous\ flux}
\lor
H_{direction/capacity}
\lor
T_{export/remote}
\lor
\text{fresh critical carrier novelty}.
}
\]

It is not an independent projective terminal.

---

## 9. Relation to the M5-410 remote source result

A reformed/new carrier is itself a natural critical atom when the thick formation hypotheses hold.

Hence repeated observational axis changes by replacement contribute either

- new M5-408 phase-space atoms;
- viscous flux loss;
- remote export;
- or interface/localization failure.

M5-410 already shows that finite reuse of a fixed natural carrier set cannot indefinitely self-source remote strain.

Thus projective replacement cannot be used to hide fresh scale-space throughput behind a purely geometric word.

---

## 10. Generic projective master split

The full projective label can now be written as

\[
\boxed{
T_{projective}^{generic}
\Longrightarrow
\begin{cases}
H_{\tau,act}^{crit}
\lor H_{dir\,diff/freq/cap}^{crit},
&\text{retained material active axis},\\[1mm]
H_{flux/direction}^{crit}
\lor S_{remote}
\lor T_{replacement/interface},
&\text{no retained active axis}.
\end{cases}
}
\]

But M5-395--410 subsequently route the replacement/remote terms into fresh critical carrier throughput or already typed H/interface action.

Therefore the projective word itself no longer needs to remain a final independent branch.

---

## 11. What remains under interface

This note does not eliminate every possible localization/pressure interface.

The following still require separate care:

- large cutoff/Bogovskii correction when a carrier description changes;
- pressure-driven velocity/energy transfer not represented by a retained vorticity-flux carrier;
- loss of the smooth active material corridor before a flux replacement object is formed;
- observational changes in a descriptor whose material support cannot be consistently assigned.

These remain under

\[
T_{realization/boundary/pressure}.
\]

The narrower label `T_projective` is no longer necessary as an independent terminal.

---

## 12. Audit verdict

### DERIVED

- exact direction-equation projective fork on any retained active material carrier;
- both tilt and directional-diffusion actions are scale critical;
- low-vorticity/zero-vorticity crossings are replacement/threshold events, not valid projective paths;
- observational axis replacement enters the existing scale-invariant flux genealogy.

### REMOVED AS INDEPENDENT TERMINAL

\[
\boxed{T_{projective}^{generic}.}
\]

### SURVIVING CONTENT

\[
H_{axis/direction}^{crit}
\lor
H_{flux/novelty}^{crit}
\lor
S_{remote}
\lor
T_{realization/boundary/pressure}.
\]

The remaining problem is now even closer to a common critical throughput ledger rather than a collection of unrelated geometric branches.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]