# DSD M17-434 — Sign-preserving own-scale kappa with positive flux has an `R^-2 log R` maximal residence before exponential flux excursion defeats the cubic raw-H2 ancestry weight

Date: 2026-09-08  
Canonical ID: **M17-434**

Status: **ACTIVE FLUX-LAW / SIGN-RESIDENCE THRESHOLD / M17-389--405--413 CONNECTION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Setup

Work in one parent-normalized record cell with descendant own scale

\[
\boxed{r=R^{-1},\qquad R\gg1.}
\]

Assume on a connected regular exact CE-H material loop/tube interval `I=[t_0,t_1]`:

1. own-scale coefficient magnitude
   \[
   c_\kappa R^2
   \le
   |\kappa(t)|
   \le
   C_\kappa R^2;
   \]
2. `kappa` is sign-preserving on `I`;
3. the tube has the M17-413 own-scale area and segment geometry needed for the flux/raw-`H2` packet bridge;
4. retained positive flux
   \[
   \Phi(t)\ge\Phi_*>0
   \qquad(t\in I);
   \]
5. the packet is representation-safe for the M17-405 record genealogy.

Let

\[
\tau:=|I|.
\]

## 2. Exact flux excursion

M17-389 gives in physical variables

\[
\boxed{
\frac d{dt}\log\Phi
=\nu\kappa.
}
\]

The same statement in the normalized record variables carries the corresponding normalized viscosity constant. We keep `nu` explicit.

Since `kappa` is sign-preserving and

\[
|\kappa|\ge c_\kappa R^2,
\]

we have

\[
\left|
\log\frac{\Phi(t_1)}{\Phi(t_0)}
\right|
\ge
\nu c_\kappa R^2\tau.
\]

Therefore one endpoint has

\[
\boxed{
\Phi_{max}
\ge
\Phi_*\exp(\nu c_\kappa R^2\tau).
}
\]

This conclusion is independent of the sign of `kappa`: positive `kappa` amplifies forward flux, while negative `kappa` requires an exponentially larger initial flux in order to retain the fixed lower floor at the end.

## 3. One own-time near the flux maximum

Assume

\[
\tau\ge c_tR^{-2}
\]

so that at least one own-time block is available.

Because

\[
|\kappa|\le C_\kappa R^2,
\]

on a terminal or initial subinterval of duration

\[
\delta t=c_0R^{-2}
\]

adjacent to the endpoint carrying `Phi_max`, choosing `c_0` fixed sufficiently small gives

\[
\boxed{
\Phi(t)
\ge
c_\Phi\Phi_{max}
}
\]

throughout that own-time subinterval, with `c_Phi>0` independent of `R`.

## 4. Flux excursion gives one amplified normalized raw-H2 packet

M17-413 gives for one own-scale segment over one own-time

\[
\boxed{
h_{seg}^{norm}\gtrsim c\Phi^2.}
\]

Using the subinterval from Section 3,

\[
\boxed{
h_{seg}^{norm}
\gtrsim
c\Phi_*^2
\exp(2\nu c_\kappa R^2\tau).
}
\]

No spatial `R` multiplicity and no full parent-time multiplicity are needed for this estimate; it is one amplified packet.

## 5. Apply the M17-405 cubic ancestry weight

The corresponding ancestral contribution is at least

\[
\boxed{
\mathcal A_R
\gtrsim
R^{-3}\Phi_*^2
\exp(2\nu c_\kappa R^2\tau).
}
\]

Thus the cubic discount can absorb only logarithmically many own-time units of sign-preserving own-scale coefficient residence.

Set

\[
N_{own}:=R^2\tau.
\]

Then

\[
\boxed{
\mathcal A_R
\gtrsim
R^{-3}\Phi_*^2e^{2\nu c_\kappa N_{own}}.
}
\]

## 6. Critical residence threshold

The borderline at which the exponential flux excursion reaches the cubic ancestry factor is

\[
2\nu c_\kappa N_{own}
\sim
3\log R.
\]

Hence

\[
\boxed{
N_{own}^{crit}
=
\frac{3}{2\nu c_\kappa}\log R
}
\]

or, in parent-normalized time,

\[
\boxed{
\tau_{crit}
=
\frac{3}{2\nu c_\kappa}
R^{-2}\log R.
}
\]

If for infinitely many representation-safe geometric records

\[
\tau_m
\ge
\left(
\frac{3}{2\nu c_\kappa}+\varepsilon
\right)
R_m^{-2}\log R_m,
\]

then

\[
\mathcal A_{R_m}
\gtrsim
R_m^{2\nu c_\kappa\varepsilon}
\]

and the M17-405 finite ancestral raw-`H2` ledger is violated.

At the exact borderline, the per-record lower contribution is order one; infinitely many bounded-overlap records are already incompatible with a finite ancestral sum.

Therefore a surviving sequence must remain strictly below the critical series threshold or lose one of the retained hypotheses.

## 7. Consequence for full parent-time persistence

A parent interval of order-one duration contains

\[
O(R^2)
\]

own-time units.

M17-434 shows that one sign-preserving own-scale coefficient phase can occupy at most `O(log R)` own-time units before the flux excursion itself defeats the cubic ancestry discount.

Thus a full parent-time retained own-scale branch cannot remain in one sign phase.

It must repeatedly encounter at least one of:

\[
\boxed{
G_{kappa\ zero/sign\ transition},
}

\[
\boxed{
G_{coefficient\ scale\ exit},
}

\[
\boxed{
G_{positive\ flux\ floor\ loss},
}

or geometry/genealogy/interface/CE-H/domain loss.

## 8. Important distinction from M17-379

M17-379 obtains logarithmic own-scale residence as an evacuation exposure lower bound.

M17-434 obtains logarithmic own-scale residence as an **upper threshold for one sign-preserving own-scale coefficient phase under a positive flux floor**.

The two logarithms arise from different mechanisms but now meet at the same own-time scale.

This does not yet close the proof because rapid sign/scale transitions may fragment the parent interval.

## 9. DSD role

DSD is used only to compare the exponential flux currency with the cubic ancestral raw-`H2` discount and to type the required transition exits.

The proof is the exact flux ODE plus the M17-413 packet lower bound and M17-405 ancestry scaling.

## 10. Audit verdict

**PASS as a sign-residence threshold theorem.**

Positive-flux own-scale CE-H cannot remain sign-preserving for more than logarithmically many own-time units across an infinite representation-safe record sequence without defeating the raw-`H2` ancestor.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
