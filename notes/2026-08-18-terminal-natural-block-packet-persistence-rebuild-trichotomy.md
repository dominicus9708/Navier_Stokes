# Terminal natural block: packet persistence versus I/V rebuild

Date: 2026-08-18

Status: **STRUCTURAL TERMINAL-BLOCK TRICHOTOMY ON THE COMPACT PACKET LANE. LARGE MULTIPLICITY WITH SMALL TERMINAL CRITICAL-STRAIN/V2 REBUILD COST MUST BE CARRIED MOSTLY BY PACKETS THAT PERSIST THROUGH THE FINAL NATURAL PARABOLIC BLOCK. GLOBAL REGULARITY NOT PROVED.**

## 1. Natural terminal block

Let

\[
W=K^2,
\qquad
\ell=K^{-1},
\qquad
I_T=[T-cK^{-2},T]
\]

for a fixed sufficiently small `c>0`.

At `T`, assume `N` bounded-overlap thick dangerous packet cores of physical volume `~K^-3` and vorticity magnitude `~K^2`.

Follow the final dangerous material labels backward through `I_T`.

## 2. Persistence/rebuild partition

Fix a lower dangerous threshold `theta W` with `0<theta<1`.

A final label is called persistent if its vorticity magnitude stays above the lower threshold for a fixed fraction of `I_T`. Otherwise it has a subinterval on which it must rebuild a fixed-factor portion of its terminal amplitude.

The rebuild labels are split by the exact Cauchy decomposition over the responsible subinterval into I-lane and V-lane labels.

Let the corresponding effective packet-volume counts be

\[
N_P,
\qquad N_I,
\qquad N_V,
\]

with

\[
N_P+N_I+N_V\gtrsim N.
\]

The constants absorb the threshold and lane fractions.

## 3. Persistent packets pay kinetic-energy dissipation

For persistent labels, the vorticity-square density is `~K^4` on volume `~N_P K^-3` for time `~K^-2`. Therefore

\[
\boxed{
\nu\int_{I_T}\|\omega(t)\|_2^2dt
\gtrsim
c_\nu\frac{N_P}{K}.
}
\]

## 4. I-lane rebuild pays critical strain

A fixed-factor material vorticity rebuild has

\[
\int |e^TSe|dt\gtrsim c_0
\]

on each I-lane label.

In terminal-normalized variables the block has `O(1)` duration and each natural packet has `O(1)` volume. Integrating over the I-lane labels and using volume preservation gives

\[
\int ds\int_{A_I(s)}|S|d x
\gtrsim N_I.
\]

At each time `|A_I(s)|~N_I`; Holder and then Cauchy in the `O(1)` time block yield

\[
\boxed{
\int_{I_T}\|S(t)\|_{L^3_x}^2dt
\gtrsim
c N_I^{2/3}.
}
\]

The `L_t^2L_x^3` strain action is Navier--Stokes scale invariant, so the normalized and physical statements have the same size.

## 5. V-lane rebuild pays V2

Assume the relevant material deformation condition number is bounded by `M`. A fixed-factor V-lane rewrite over an `O(1)` normalized block satisfies, by Cauchy in time and integration over labels,

\[
\boxed{
\int_{I_T}^{norm}\|\Delta\Omega(s)\|_2^2ds
\gtrsim
c_{\nu,M}N_V.
}
\]

If the condition number is unbounded, the episode is already in the deformation branch.

## 6. Consequence

A terminal multiplicity `N->infinity` cannot simultaneously have

- negligible persistent-packet dissipation;
- bounded terminal critical strain rebuild;
- bounded terminal V2 rebuild;
- bounded material condition number,

unless almost all of the multiplicity is carried by packets that were already present through the last natural block and `N/K` is small.

Thus the minimal surviving compact lane is sharpened to

\[
\boxed{
N=o(K)
\quad+\quad
\text{predominantly persistent high-vorticity packet population}.
}
\]

## 7. Limitation

Persistence over one natural block does not imply persistence over the full deep-checkpoint interval. Packets may be rebuilt intermittently at earlier times. The next target is a lifetime/genealogy packing theorem that combines repeated natural-block persistence with the aggregate deep I/V costs.

Status: **TERMINAL NEW-PACKET MULTIPLICITY TYPED / MINIMAL COMPACT SURVIVOR = SUBMAXIMAL, PREDOMINANTLY PERSISTENT PACKET POPULATION.**