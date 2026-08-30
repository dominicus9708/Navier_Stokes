# DSD M5-304 — Localized Vorticity Monopole: Exact Boundary-Velocity Identity and Energy Charge

Date: 2026-08-30

Parent: `DSD_M5_303_MONOPOLE_NEUTRAL_SATELLITE_CLOUD_SUBCRITICAL_NEXT_MULTIPOLE_SUMMABILITY_2026-08-30.md`

Status: **EXACT FORMATION IDENTITY / THE LOCALIZED VORTICITY MONOPOLE `M=∫chi omega` IS NOT AN INDEPENDENT BULK CHARGE: IT EQUALS A CUTOFF-BOUNDARY VELOCITY MOMENT `-∫grad chi × u` / THE IDENTITY IS GALILEAN INVARIANT AFTER SUBTRACTING ANY CONSTANT VELOCITY / A NONDEGENERATE `|M|~ell` FORCES A NATURAL-SIZE RELATIVE KINETIC ENERGY IN THE TRANSITION REGION / CRITICAL `M!=0` CLOUDS ARE THEREFORE AUTOMATICALLY CHARGED TO BOUNDARY/CAMPANATO ENERGY / GLOBAL REGULARITY UNPROVED.**

---

## 1. Exact identity

Let

\[
\omega=\nabla\times u
\]

and let `chi` be a smooth compactly supported scalar cutoff.

Define

\[
\boxed{
M:=\int_{\mathbb R^3}\chi\omega\,dx.
}
\]

Use

\[
\nabla\times(\chi u)
=\nabla\chi\times u+\chi\nabla\times u.
\]

The integral of the curl of the compactly supported field `chi u` vanishes, so

\[
\boxed{
M
=-\int\nabla\chi\times u\,dx.
}
\]

This is exact.

---

## 2. Galilean invariance

For any constant vector `c`,

\[
\int\nabla\chi\times c\,dx
=\left(\int\nabla\chi\,dx\right)\times c
=0.
\]

Therefore

\[
\boxed{
M
=-\int\nabla\chi\times(u-c)\,dx
}
\]

for every constant `c`.

Thus the localized vorticity monopole depends only on **relative velocity across the cutoff transition**, not on a Galilean drift.

A natural choice is the transition-region mean or another local coherent velocity representative.

---

## 3. Natural-scale estimate

Take a fixed-shape packet cutoff of scale `ell`.

Then

\[
|\nabla\chi|\lesssim\ell^{-1}
\]

on a transition region of volume `O(ell^3)`.

Hence

\[
\boxed{
\|\nabla\chi\|_2
\lesssim\ell^{1/2}.
}
\]

By Cauchy–Schwarz,

\[
\boxed{
|M|
\le
C\ell^{1/2}
\|u-c\|_{L^2(transition)}.
}
\]

Equivalently,

\[
\boxed{
\|u-c\|_{L^2(transition)}^2
\ge
c\frac{|M|^2}{\ell}.
}
\]

---

## 4. Critical nonzero monopole costs natural kinetic energy

If

\[
\boxed{|M|\ge m_*\ell}
\]

with fixed `m_*>0`, then

\[
\boxed{
\|u-c\|_{L^2(transition)}^2
\ge
c m_*^2\ell.
}
\]

Thus a critical-size nonzero vorticity monopole automatically carries the same natural relative kinetic-energy scale used in the occupied-packet Morrey capacity.

This removes a possible loophole in which a large leading far-strain moment might have negligible kinetic occupation.

---

## 5. Formation interpretation

The branch variable `M` has a clearer meaning than in M5-294:

\[
\boxed{
M\neq0
\iff
\text{the cutoff boundary sees a nonzero relative velocity circulation/moment}.
}
\]

It is not a conserved point charge of vorticity.

It measures how much of the globally compensating vorticity/velocity structure has been cut away by the packet localization.

Therefore a critical `M!=0` satellite is necessarily linked to its exterior environment through the cutoff transition.

---

## 6. Consequence for cloud counting

Suppose critical packets have

\[
|M_i|\ge m_*\ell
\]

and pairwise disjoint transition regions.

Then each transition region costs at least

\[
c m_*^2\ell
\]

relative kinetic energy.

Under the centered Morrey bound

\[
\int_{B_{Cd}}|u-c_{appropriate}|^2\lesssim M_*d
\]

in the form available for the packet construction, the number of critical `M!=0` packets obeys

\[
\boxed{
N_{M_*}\lesssim L.
}
\]

Thus the `O(L)` capacity is not restricted to packets whose occupancy was detected first through cubic velocity mass; it also applies directly to packets carrying a fixed critical vorticity-monopole moment, modulo the precise relative-energy gauge used on the parent region.

---

## 7. Small-monopole branch

If instead

\[
|M_i|\ll\ell,
\]

then the leading `d^{-3}` far-strain coefficient is proportionally small.

The cloud should therefore be split quantitatively, not just by exact zero/nonzero:

\[
\boxed{
|M_i|/\ell
\le\varepsilon_M
\quad\lor\quad
|M_i|/\ell>\varepsilon_M.
}
\]

The first is an approximately monopole-neutral packet and approaches the subcritical M5-303 regime.

The second pays a fixed natural transition-energy charge and is countable by Morrey capacity.

---

## 8. Aggregate main-core strain refinement

For critical-moment packets at distance `d=L ell`, each contributes

\[
|S_i|\lesssim\frac{|M_i|}{d^3}.
\]

The exact boundary identity also allows a Cauchy–Schwarz aggregate estimate.

For disjoint transitions,

\[
\sum_i|M_i|
\le
C\ell^{1/2}
N^{1/2}
\left(\sum_i\|u-c_i\|_{L^2(trans_i)}^2\right)^{1/2}.
\]

Thus even before imposing a fixed monopole floor, the leading aggregate moment is controlled by boundary relative energy rather than by a free count of vorticity blobs.

The exact best global bound depends on how the constants `c_i` are reconciled with the parent Campanato gauge, so no universal closure is asserted here.

---

## 9. Dynamic connection

M5-295 derived

\[
\dot M=\mathcal S_M+\mathcal B_M.
\]

M5-304 adds that `M` itself is a boundary-relative-velocity functional.

Therefore both the **value** and the **evolution** of the critical cloud moment are boundary/interaction-sensitive.

This reinforces the routing

\[
\boxed{
C_{M\neq0,critical}
\to
C_{boundary-linked}
}
\]

rather than treating such packets as autonomous bulk vortex particles.

---

## 10. Important firewall

The estimate does not say that every nonzero `M` is a turnover event.

A coherent steady packet may sustain a nonzero boundary velocity moment indefinitely.

The result is an energy/coupling charge and a counting tool, not a dynamical contradiction.

---

## 11. Updated critical-cloud split

The critical degree-`-3` cloud becomes

\[
\boxed{
\begin{aligned}
C_{M\neq0}
\Longrightarrow{}&
C_{M/\ell\ll1}\quad\text{(near-neutral)}\\
&\lor C_{M/\ell\gtrsim1}\quad\text{(boundary-energy charged)}.
\end{aligned}
}
\]

The first is close to the subcritical multipole lane.

The second has only `O(L)` simultaneous capacity on the compatible Morrey corridor and remains linked to boundary/ancestry dynamics.

---

## 12. Audit verdict

### PROVED / EXACT

\[
\boxed{
\int\chi\omega
=-\int\nabla\chi\times(u-c)
}
\]

for any constant `c`.

### DERIVED

Critical `|M|~ell` forces natural transition-region relative kinetic energy `~ell`.

### STRUCTURAL GAIN

The critical vorticity monopole is a boundary-linked descriptor, not an independent bulk charge.

### OPEN

- dynamic closure of boundary-linked critical packets;
- reconciliation of local packet gauges in a global Campanato sum;
- ancestry/coherent restart;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]