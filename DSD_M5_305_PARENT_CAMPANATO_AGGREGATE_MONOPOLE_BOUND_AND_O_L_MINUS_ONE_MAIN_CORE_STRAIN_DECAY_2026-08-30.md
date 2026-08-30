# DSD M5-305 — Parent-Campanato Aggregate Monopole Bound and `O(L^{-1})` Main-Core Strain Decay

Date: 2026-08-30

Parents:
- `DSD_M5_304_LOCALIZED_VORTICITY_MONOPOLE_EXACT_BOUNDARY_VELOCITY_IDENTITY_AND_ENERGY_CHARGE_2026-08-30.md`
- `DSD_M5_297_MORREY_SPARSE_CLOUD_MAIN_CORE_FAR_STRAIN_DECAY_AND_ANGULAR_CANCELLATION_SCOPE_CORRECTION_2026-08-30.md`

Status: **STRONGER MAIN-CORE DECOUPLING / USING ONE COMMON PARENT-ANNULUS VELOCITY GAUGE, THE EXACT MONOPOLE BOUNDARY IDENTITY CAN BE SUMMED BY CAUCHY–SCHWARZ OVER ALL DISJOINT COMPARABLE PACKETS / EVEN WITH ONLY GEOMETRIC `N=O(L^3)` PACKING, A PARENT RELATIVE-CAMPANATO ENERGY BOUND FORCES THE TOTAL DEGREE-`-3` MAIN-CORE STRAIN FROM THE BAND TO BE `O(L^{-1})` IN SATELLITE NATURAL UNITS / THIS REMOVES THE NEED FOR OCCUPANCY OR ANGULAR CANCELLATION IN THE MAIN-CORE FAR-STRAIN CHANNEL / GLOBAL REGULARITY UNPROVED.**

---

## 1. Setup

Consider a remote radial band at distance

\[
d=L\ell,
\qquad L\gg1,
\]

from the tracked main core.

Let `N` localized comparable packet cutoffs `chi_i` have disjoint or bounded-overlap transition supports of scale `ell` inside one fixed enlargement of the parent band.

Pure geometry gives

\[
\boxed{N\lesssim L^3.}
\]

No packet occupancy floor is assumed in this note.

---

## 2. One common Galilean gauge

Let

\[
c=(u)_{A_d^*}
\]

be one common velocity representative for the parent annulus.

For every packet, M5-304 gives

\[
M_i
=-\int\nabla\chi_i\times(u-c)dx,
\]

because

\[
\int\nabla\chi_i dx=0.
\]

Thus all packet moments can be estimated against the **same** relative velocity field `u-c`.

---

## 3. Sum of packet moments

Each fixed-shape cutoff satisfies

\[
\|\nabla\chi_i\|_2^2\lesssim\ell.
\]

By Cauchy–Schwarz in the packet index and physical space,

\[
\begin{aligned}
\sum_{i=1}^N|M_i|
&\le
\sum_i
\|\nabla\chi_i\|_2
\|u-c\|_{L^2(trans_i)}\\
&\le
\left(\sum_i\|\nabla\chi_i\|_2^2\right)^{1/2}
\left(\sum_i\|u-c\|_{L^2(trans_i)}^2\right)^{1/2}.
\end{aligned}
\]

Bounded overlap gives

\[
\sum_i\|u-c\|_{L^2(trans_i)}^2
\lesssim
\int_{A_d^*}|u-c|^2dx.
\]

Hence

\[
\boxed{
\sum_i|M_i|
\lesssim
(N\ell)^{1/2}
\left(
\int_{A_d^*}|u-c|^2dx
\right)^{1/2}.
}
\]

---

## 4. Parent Campanato input

Assume the no-`T_Campanato` corridor gives

\[
\boxed{
\int_{A_d^*}|u-c|^2dx
\le
C_C d.
}
\]

Then

\[
\boxed{
\sum_i|M_i|
\lesssim
C_C^{1/2}
(N\ell d)^{1/2}.
}
\]

Using `d=L ell`,

\[
\boxed{
\sum_i|M_i|
\lesssim
C_C^{1/2}
\ell\sqrt{NL}.
}
\]

---

## 5. Aggregate leading main-core strain

For all packets in the comparable remote band,

\[
|S_i(0)|\lesssim\frac{|M_i|}{d^3}.
\]

Therefore

\[
|S_{band}^{(0)}(0)|
\lesssim
\frac1{d^3}
\sum_i|M_i|
\lesssim
C_C^{1/2}
\frac{\ell\sqrt{NL}}{(L\ell)^3}.
\]

Normalize by the satellite natural strain scale `ell^{-2}`:

\[
\boxed{
\frac{|S_{band}^{(0)}(0)|}{\ell^{-2}}
\lesssim
C_C^{1/2}
\frac{\sqrt N}{L^{5/2}}.
}
\]

---

## 6. Use only geometric packing

With

\[
N\lesssim L^3,
\]

one gets

\[
\boxed{
\frac{|S_{band}^{(0)}(0)|}{\ell^{-2}}
\lesssim
\frac{C}{L}
\to0.
}
\]

This requires neither:

- fixed packet occupancy;
- `N=O(L)` Morrey counting;
- angular tensor cancellation;
- monopole neutrality.

It uses only:

1. exact boundary representation of each localized monopole;
2. one parent relative-Campanato bound;
3. bounded-overlap packet localization;
4. geometric `O(L^3)` packing.

---

## 7. Comparison with M5-297

M5-297 obtained the stronger

\[
O(L^{-2})
\]

main-core decay for **genuinely occupied packets**, because occupancy plus Morrey reduces the count to `N=O(L)`.

M5-305 gives the more robust

\[
\boxed{O(L^{-1})}
\]

bound without an occupancy floor.

Thus:

\[
\boxed{
\begin{aligned}
\text{arbitrary localized packets + Campanato}
&\Rightarrow O(L^{-1}),\\
\text{occupied packets + Morrey}
&\Rightarrow O(L^{-2}).
\end{aligned}
}
\]

Both vanish.

---

## 8. Structural consequence

The remote satellite population cannot maintain or generate an order-one strain at the **original main core** merely through the leading Biot–Savart monopole channel while the parent Campanato corridor remains bounded.

Therefore

\[
\boxed{
H_{remote\to main}^{monopole}
\subset
T_{Campanato}
\lor\text{finite-radius/nonremote terms}.
}
\]

This is a stronger decoupling statement than the earlier angular-cancellation analysis.

---

## 9. What this does not control

The estimate is centered on the original main core and does not give a satellite-centered Campanato bound.

It therefore does not control:

- strain at one satellite from nearby neighbors;
- affine/harmonic background seen in the detached frame;
- packet-local clustering;
- dynamic replacement/return bridges.

Those remain the true remote-satellite problems.

---

## 10. Formation interpretation

Once `M_i` is recognized as a boundary-relative-velocity functional, the cloud's main-core interaction is controlled by a **quadratic parent resource**, not by the raw number of vortex objects.

The useful collective descriptor becomes

\[
\boxed{
\mathscr M_{band}
:=
\sum_i|M_i|,
}

with the capacity estimate

\[
\boxed{
\mathscr M_{band}
\lesssim
\ell\sqrt{NL}.
}
\]

The degree-`-3` kernel then converts the quadratic resource bound into `L^{-1}` decoupling.

---

## 11. Audit verdict

### PROVED UNDER PARENT-CAMPANATO / BOUNDED-OVERLAP ASSUMPTIONS

\[
\boxed{
|S_{band,main}|/\ell^{-2}\lesssim L^{-1}.
}
\]

### STRENGTHENING

No packet occupancy or angular cancellation is required for main-core far-strain decay.

### OPEN

- satellite-local ambient strain;
- detached-frame global growth/ancestry;
- dynamic turnover and return structures;
- exponent-positive extreme Type-II separation;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]