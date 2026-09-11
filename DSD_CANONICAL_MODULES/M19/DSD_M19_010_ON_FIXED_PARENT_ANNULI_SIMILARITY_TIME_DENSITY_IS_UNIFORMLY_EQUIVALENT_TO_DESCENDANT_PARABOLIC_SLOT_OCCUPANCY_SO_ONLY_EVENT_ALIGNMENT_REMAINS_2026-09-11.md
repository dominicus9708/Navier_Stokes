# M19-010 — On fixed parent annuli, similarity-time density is uniformly equivalent to descendant parabolic-slot occupancy, so only event alignment remains

**Date:** 2026-09-11  
**Status:** CALCULATION / R-AC TIME-COORDINATE CONVERSION / ANNULAR DENSITY EQUIVALENCE / EVENT-ALIGNMENT FRONTIER

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-009 reduces the direct ancestry-return problem to occupation of the \(K_k^2\) descendant parabolic time slots available inside a fixed parent-time window.

The next question is whether recurrence information stated in backward similarity time can populate those affine descendant slots.

A naive concern is that logarithmic time has only order-one length on a fixed parent annulus and therefore cannot control \(K_k^2\) slots.

That concern is incorrect when density means **time measure** rather than merely a count of isolated event centers.

On any fixed parent backward annulus bounded away from the terminal time, similarity-time measure and normalized parent physical-time measure are uniformly equivalent. Consequently a positive similarity-time occupation fraction corresponds to a positive fraction of the \(K_k^2\) descendant parabolic slots.

Thus the remaining bridge is not a time-coordinate Jacobian loss. It is event/genealogy alignment.

## 2. Backward similarity coordinates

Let

\[
\theta:=-\log(T^*-t)
\]

up to an irrelevant additive normalization.

Then

\[
\boxed{
\frac{d\theta}{dt}
=\frac1{T^*-t}
}
\]

and therefore

\[
\boxed{
dt=(T^*-t)d\theta.
}
\]

Fix a parent spatial scale \(r_p\) and a backward annular time cell

\[
\boxed{
I_p
:=
\{t:
 a r_p^2
\le
T^*-t
\le
b r_p^2
\},
\qquad
0<a<b<\infty.
}
\]

This is the physical version of the fixed normalized annuli used in the certified ancestry ledgers.

## 3. Uniform measure equivalence on the annulus

For any measurable event set

\[
E\subset I_p,
\]

write its similarity-time image as \(E_\theta\).

Using

\[
a r_p^2
\le
T^*-t
\le
b r_p^2,
\]

we obtain

\[
 a r_p^2|E_\theta|
\le
|E|_t
\le
 b r_p^2|E_\theta|.
\]

Hence

\[
\boxed{
 a|E_\theta|
\le
\frac{|E|_t}{r_p^2}
\le
 b|E_\theta|.
}
\]

The same estimate holds for the entire parent annulus \(I_p\).

Therefore the physical-time occupation fraction and similarity-time occupation fraction are uniformly comparable:

\[
\boxed{
 c_{a,b}
\frac{|E_\theta|}{|I_{p,\theta}|}
\le
\frac{|E|_t}{|I_p|_t}
\le
C_{a,b}
\frac{|E_\theta|}{|I_{p,\theta}|}.
}
\]

No age factor \(K_k^{-2}\) appears in the **fraction**.

## 4. Descendant parabolic slots

Let an age-\(k\) descendant scale be

\[
 r_d
=\frac{r_p}{K_k}.
\]

Its parabolic time unit is

\[
\boxed{
r_d^2
=\frac{r_p^2}{K_k^2}.
}
\]

The number of descendant-scale temporal slots available in the parent annulus is therefore

\[
\boxed{
N_k^{slot}
\asymp
\frac{|I_p|_t}{r_d^2}
\asymp
K_k^2.
}
\]

For an event set \(E\subset I_p\), define the measure-based occupied-slot count

\[
\boxed{
N_k^{occ}(E)
:=
\frac{|E|_t}{r_d^2}.
}
\]

Then

\[
N_k^{occ}(E)
=
K_k^2\frac{|E|_t}{r_p^2}.
\]

Using Section 3,

\[
\boxed{
N_k^{occ}(E)
\asymp_{a,b}
K_k^2|E_\theta|.
}
\]

Thus an order-one similarity-time event measure produces order \(K_k^2\) descendant parabolic occupied slots.

## 5. Occupancy fraction equivalence

Divide by the total number of slots:

\[
\delta_k(E)
:=
\frac{N_k^{occ}(E)}{N_k^{slot}}.
\]

Then

\[
\boxed{
\delta_k(E)
\asymp_{a,b}
\frac{|E_\theta|}{|I_{p,\theta}|}.
}
\]

Therefore if one has a uniform similarity-time density lower bound

\[
\frac{|E_\theta|}{|I_{p,\theta}|}
\ge\delta_*>0,
\]

then

\[
\boxed{
\delta_k(E)
\ge c_{a,b}\delta_*>0
}
\]

uniformly in the age ratio \(K_k\).

This exactly supplies a fixed fraction of the quadratic parabolic slot capacity.

## 6. Relation to the M19-008 ancestry threshold

M19-008 shows that plain-return closure asks for

\[
\delta_k
\gtrsim
J_k^{1/2}
\]

at the scaling level.

If the return event itself has a similarity-time occupation fraction \(\delta_*>0\) on the relevant parent annulus, then

\[
\delta_k\gtrsim\delta_*.
\]

Thus on shells where

\[
J_k^{1/2}\le C\delta_*
\]

the required ancestry-return threshold is obtained, modulo the already certified amplitude/comparability constants.

On the bounded normalized-enstrophy corridor, \(J_k\) has a uniform upper bound. Therefore a sufficiently strong uniform return-event density would in principle overcome the single-episode age penalty.

The missing issue is whether the available positive-density recurrent event is the **same event** needed for ancestry return at shell \(k\).

## 7. Event count versus event measure

The equivalence above applies to event **measure**.

It does not say that a positive density of isolated event centers with zero temporal thickness gives positive slot occupancy.

One needs either

- an event set of positive similarity-time measure;
- or discrete events with a uniform positive similarity-time thickness.

This is consistent with the earlier temporal-thickening audits.

## 8. EVENT-ALIGN firewall

The repository contains several positive-density recurrent phenomena, including local production, ratchet activity, and persistent-lineage events.

But the ancestry return density \(\mathfrak R_k\) requires a specific age-shell/material-genealogy return.

Therefore

\[
\boxed{
\text{positive-density production/ratchet event}
\not\Rightarrow
\text{positive-density ancestry return event for every shell }k.
}
\]

The two can only be identified after proving an event-alignment theorem.

This is precisely the issue previously exposed qualitatively by the M18 LOG-ALIGN / EVENT-ANNULAR firewall.

The present calculation removes the coordinate-Jacobian ambiguity: once the correct event is aligned in a fixed annulus, the time-coordinate conversion is harmless.

## 9. Sharpened R-AC endpoint

The direct return-weight root can now be written

\[
\boxed{
G_{EVENT\text{-}ALIGN}
:
\text{cubic-mass-bearing age-shell ancestry returns fail to inherit the positive similarity-time occupancy of the recurrent compact dynamics}.
}
\]

The deficiency is no longer attributed to

- geometric time scaling;
- lack of enough parabolic time slots;
- or similarity-time versus physical-time Jacobians.

Those effects are now calculated exactly.

## 10. What would close this subroot

A sufficient theorem would have the form:

> On every cubic-mass-dominant shell family, a fixed positive fraction of the existing positive-density recurrent material/production event is carried by a contact/fresh descendant whose ancestry realizes the shell return counted by \(\mathfrak R_k\).

Combined with Section 5, this would yield a fixed slot occupancy floor and hence a return-weight lower bound.

If the event cannot be aligned, the failure must be routed to replacement/export, lineage turnover, or another already typed genealogy exit.

## 11. M19-010 verdict

\[
\boxed{
\text{similarity-time positive measure}
\Longleftrightarrow_{fixed\ annulus}
\text{positive descendant parabolic-slot occupancy fraction}.
}
\]

Thus the remaining R-AC problem is an event/genealogy identification problem, not a time-coordinate scaling problem.

## 12. Next calculation

M19-011 should combine:

- the finite persistent fixed-flux lineage network;
- positive-density local production/current events;
- contact/exposure/replacement genealogy;
- and the cubic-mass shell decomposition;

to test whether a cubic-mass-bearing shell can systematically avoid all positive-density persistent-lineage events without paying replacement/export/remote action.

That is now the highest-value R-AC bridge.

---

\[
\boxed{\text{M19-010 COMPLETE; R-AC REDUCED TO EVENT--GENEALOGY ALIGNMENT.}}
\]
