# M19-034 — Joint space-time incidence of one child packet carries a K^-3 parent penalty, so marginal occupancies cannot be naively multiplied

**Date:** 2026-09-11  
**Status:** CALCULATION / R-AC JOINT-INCIDENCE FIREWALL / EXACT PARABOLIC SCALING

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Parent and child scales

Let one ancestry parent have physical length scale

\[
\rho>0.
\]

Let a child first-hitting packet have natural scale

\[
r=\frac{\rho}{K},
\qquad
K\gg1.
\]

The natural parabolic times are

\[
T_{parent}=\frac{\rho^2}{\nu},
\qquad
T_{child}=\frac{r^2}{\nu}.
\]

Therefore

\[
\boxed{
\frac{T_{child}}{T_{parent}}=K^{-2}.
}
\]

## 2. Spatial critical fraction

A first-hitting packet has the physical kinetic-variance scale

\[
\mathcal E_{child}
\asymp
\nu^2r.
\]

The critical Morrey kinetic scale of the parent is

\[
\mathcal E_{parent}^{crit}
\asymp
\nu^2\rho.
\]

Thus one child contributes the spatial critical fraction

\[
\boxed{
\frac{\mathcal E_{child}}
{\mathcal E_{parent}^{crit}}
\asymp
\frac r\rho
=K^{-1}.
}
\]

This is the M19-033 eccentricity penalty.

## 3. Temporal parent fraction

If the child remains active for one natural child duration

\[
\tau\asymp\frac{r^2}{\nu},
\]

then relative to one parent parabolic time

\[
\boxed{
\frac{\tau}{T_{parent}}
\asymp K^{-2}.
}
\]

This is the same parabolic age penalty underlying the earlier R-AC return-weight calculation.

## 4. Joint space-time fraction

If one asks for the fraction of **parent critical kinetic activity integrated through parent time** supplied by the same child event, the two factors multiply:

\[
\boxed{
K^{-1}\times K^{-2}=K^{-3}.
}
\]

Equivalently, the child spacetime kinetic-variance charge is

\[
\mathcal Q_{child}
\asymp
(\nu^2r)
\left(\frac{r^2}{\nu}\right)
=
\nu r^3.
\]

The corresponding parent critical spacetime normalization is

\[
\mathcal Q_{parent}^{crit}
\asymp
(\nu^2\rho)
\left(\frac{\rho^2}{\nu}\right)
=
\nu\rho^3.
\]

Hence exactly

\[
\boxed{
\frac{\mathcal Q_{child}}
{\mathcal Q_{parent}^{crit}}
\asymp
\left(\frac r\rho\right)^3
=K^{-3}.
}
\]

## 5. Consequence for packet multiplicity

If all child events have comparable natural scale and natural duration, then an order-one joint parent occupancy requires schematically

\[
\boxed{
N_{joint}\gtrsim K^3.
}
\]

This should be compared with the separate marginal thresholds:

\[
N_{space}\gtrsim K
\]

for one-time critical radial-shell occupancy, and

\[
N_{time}\gtrsim K^2
\]

for filling one parent-time window by natural child-time slots.

The joint threshold is their product in the sense

\[
K\cdot K^2=K^3.
\]

## 6. Geometric opportunity is still not a contradiction

One parent parabolic cylinder can geometrically contain order

\[
K^3
\]

child spatial cells and order

\[
K^2
\]

child time cells, hence order

\[
K^5
\]

child parabolic cells in raw space-time capacity.

Thus the requirement

\[
N_{joint}\gtrsim K^3
\]

is not forbidden by packing:

\[
K^3\ll K^5.
\]

Again the issue is actual dynamical incidence, not geometric capacity.

## 7. Why a naive joint payer does not improve R-AC

M19-033 suggested combining spatial shell occupancy and temporal ancestry return.

The exact calculation shows that simply multiplying their normalized fractions makes the ancestry penalty **stronger**, not weaker:

\[
K^{-1}
\quad\text{and}\quad
K^{-2}
\quad\Longrightarrow\quad
K^{-3}.
\]

Therefore the route

\[
\text{spatial payer}
\times
\text{temporal payer}
\to
\text{better ancestry budget}
\]

is false.

The joint quantity can be useful only if a new theorem supplies a correspondingly large multiplicity or residence enhancement.

## 8. Marginal lower bounds do not imply joint alignment

Even if one separately knows

\[
\text{many spatial packets at some times}
\]

and

\[
\text{long ancestral return at other times},
\]

it does not follow that the same material/lineage events realize both.

Thus

\[
\boxed{
\text{spatial occupancy lower bound}
+
\text{temporal return lower bound}
\not\Rightarrow
\text{joint incidence lower bound}.
}
\]

This is the exact correlation firewall.

## 9. Correct R-AC theorem target

The useful missing theorem is therefore not merely a lower bound on a product scalar.

It must assert that the **same cubic-mass-bearing lineage events** carry enough of both:

1. radial-shell spatial occupancy;
2. ancestral physical return duration.

Symbolically,

\[
\boxed{
\mathcal T_{AC}^{corr}:
\text{cubic-mass-bearing lineage}
\Rightarrow
\text{jointly aligned space-time incidence}
\lor
\text{typed replacement/export/deformation exit}.
}
\]

Without such event alignment, the two marginal ledgers cannot be multiplied legitimately.

## 10. Relation to the previously exposed R-AC endpoint

M19-012 exposed

\[
\mathcal T_{AC}
=
\text{lineage-shell incidence / aligned occupancy / node-surplus correlation theorem}.
\]

M19-034 does not create a new independent theorem. It sharpens the same frontier:

\[
\boxed{
\mathcal T_{AC}
\text{ is fundamentally a correlation theorem, not a missing scaling estimate.}
}
\]

The scaling estimates are now explicit and unfavorable:

\[
K^{-1},
\qquad
K^{-2},
\qquad
K^{-3}.
\]

## 11. Next calculation

Further algebraic multiplication of unsigned occupancies is unlikely to help.

The next useful move is either:

1. derive a **signed/material correlation identity** tying spatial packet creation to ancestral return of the same lineage; or
2. return to R-critical and search for a rigidity theorem that closes the aperiodic scattering factor independently of ancestry.

Since M18 already found no unsigned budget with favorable scaling, the second route may now have greater leverage unless a new material identity is found.

---

\[
\boxed{\text{M19-034 COMPLETE; THE R-AC FRONTIER IS A TRUE EVENT-CORRELATION THEOREM.}}
\]
