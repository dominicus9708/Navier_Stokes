# DSD M5-296 — Occupied Satellite Morrey Capacity and Amplified Persistence Threshold

Date: 2026-08-30

Parents:
- `DSD_M5_292_FORMATION_SATELLITE_PACKING_PERSISTENCE_THRESHOLD_FOR_AMPLIFIED_TYPEII_2026-08-30.md`
- `DSD_M5_294_FORMATION_AXIS_CLOUD_BIOT_SAVART_LEADING_MULTIPOLE_AND_ANGULAR_STRAIN_ORDER_PARAMETER_2026-08-30.md`

Status: **FORMATION-CAPACITY REFINEMENT / GENUINELY OCCUPIED NATURAL SATELLITES IN A MORREY-CONTROLLED BALL HAVE MULTIPLICITY `N=O(L)`, NOT `O(L^3)` / FOR PACKET-DOMINATED AMPLIFIED MIXED NORM THIS FORCES A LARGE PERSISTENCE/TYPE-II CLOCK, AND FOR THE IMPORTANT `1<l<2` SEREGIN RANGE BOUNDED-THETA AMPLIFICATION IS IMPOSSIBLE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Why geometric packing was too weak

M5-293 used only disjoint spatial cells and therefore allowed the geometric capacity

\[
N\lesssim L^3,
\qquad L=d/\ell.
\]

That is correct as pure geometry but too weak on the no-Campanato-turnover corridor.

A genuinely occupied natural packet carries a definite kinetic mass.

The existing localized solenoidal phase-space trichotomy proves that, under a Type-I envelope and a fixed cubic occupancy floor, a retained shell packet satisfies

\[
\boxed{
\|f_\ell\|_2^2\ge e_*\ell
}
\]

for some scale-independent `e_*>0`.

The Formation distinction is therefore:

\[
\boxed{
\text{occupied packet}
\quad\lor\quad
\text{degenerate/diffuse packet}.
}
\]

Only the occupied branch is treated quantitatively in this note.

---

## 2. Morrey capacity

Assume `N` pairwise essentially disjoint occupied satellite cores of comparable natural scale `\ell` lie in a ball of radius `Cd`.

Assume the no-`T_Campanato` corridor gives

\[
\boxed{
\int_{B_{Cd}}|u|^2dx\le M_*d.
}
\]

Because the retained packet cores are disjoint and each carries at least `e_*\ell` kinetic energy,

\[
N e_*\ell
\le
\int_{B_{Cd}}|u|^2dx
\le M_*d.
\]

Hence

\[
\boxed{
N\le C_M L,
\qquad
C_M=M_*/e_*.
}
\]

This is the correct occupied-satellite capacity on the Morrey corridor.

Thus

\[
\boxed{
N=O(L),
\quad\text{not}\quad O(L^3).
}
\]

---

## 3. Relation to the amplified mixed norm

For a packet-dominated cloud, M5-292 gives the scale estimate

\[
M_\kappa^{s,l}(u,d)
\lesssim
\Theta L^{-\kappa}N^{l/s}
\]

up to fixed packet-shape/overlap constants, where

\[
\Theta=(T^*-t)|\omega_{sat}|,
\]

and Seregin's exponent is

\[
\boxed{
\kappa=l\left(\frac3s+\frac2l-1\right)
=2+l\left(\frac3s-1\right).
}
\]

Substituting `N\le C_ML`,

\[
\boxed{
M_\kappa^{s,l}(u,d)
\lesssim
C_M^{l/s}
\Theta
L^{-\mu(s,l)},
}
\]

with

\[
\boxed{
\mu(s,l)
:=\kappa-\frac ls
=2-l+\frac{2l}{s}.
}
\]

---

## 4. Persistence threshold for amplification

The amplified Type-II descriptor requires

\[
\boxed{
g(\ell)M_\kappa^{s,l}\ge\varepsilon_0.}
\]

Therefore the occupied Morrey cloud must satisfy

\[
\boxed{
\Theta
\gtrsim
\frac{\varepsilon_0}{g(\ell)}
C_M^{-l/s}
L^{\mu(s,l)}.
}
\]

This is a stronger persistence requirement than the purely geometric `N\lesssim L^3` estimate.

---

## 5. Important `1<l<2` regime

Seregin's 2026 Type-II paper explicitly uses examples with

\[
1<l<2.
\]

In this range,

\[
\mu(s,l)
=2-l+\frac{2l}{s}
>0
\]

for every `s>1`.

Since

\[
g(\ell)\to0,
\qquad
L\to\infty,
\]

one gets

\[
\boxed{
\Theta\to\infty
}
\]

on any occupied packet-dominated amplified cloud.

Therefore

\[
\boxed{
\Theta=O(1)
\quad\Longrightarrow\quad
\text{no occupied Morrey amplified cloud}
}
\]

in the `1<l<2` range.

In words: a critical-clock cloud cannot obtain Seregin-type mixed-norm amplification merely by packing many genuinely occupied natural satellites while the Morrey bound remains valid.

---

## 6. Interpretation

Recall

\[
\Theta=(T^*-t)|\omega_{sat}|.
\]

Thus `Theta -> infinity` is already a local Type-II vorticity-clock escalation.

The amplified cloud must therefore buy its large mixed norm through at least one of:

1. very long persistence in satellite natural time;
2. loss of the occupied-packet Morrey capacity;
3. a diffuse/background velocity contribution not represented by the selected packets;
4. overlap/nonseparation invalidating the disjoint packet model.

The last three are separate Formation branches and must not be hidden inside the packet count.

---

## 7. Diffuse/background firewall

The estimate

\[
M_\kappa\lesssim\Theta L^{-\kappa}N^{l/s}
\]

is a **packet-dominated** upper model.

A large background velocity field may raise the mixed norm while contributing little to the selected satellite packet count.

Therefore the valid split is

\[
\boxed{
S_{amp}
\Longrightarrow
S_{amp}^{packet}
\lor
S_{amp}^{background/diffuse}.
}
\]

The first is governed by the persistence threshold above.

The second returns to the previously typed weak-`L^3`/Campanato/derivative-frequency escalation machinery and cannot be declared closed here.

---

## 8. Consequence for cloud geometry

The Morrey capacity also changes the angular-cloud intuition.

A remote radial band cannot contain `O(L^3)` genuinely occupied natural packets on the quiet Morrey corridor.

At most

\[
O(L)
\]

can be simultaneously occupied.

This greatly weakens their aggregate far strain and will be audited separately in M5-297.

---

## 9. Audit verdict

### PROVED / CONDITIONAL ON OCCUPANCY DESCRIPTOR

If every counted packet carries the scale-invariant occupancy floor `||f_ell||_2^2 >= e_* ell` and the Morrey energy bound holds, then

\[
\boxed{N\le C_ML.}
\]

### DERIVED

For packet-dominated mixed norm,

\[
\boxed{
M_\kappa\lesssim \Theta L^{-\mu},
\qquad
\mu=2-l+2l/s,
}
\]

and amplified behavior forces

\[
\boxed{
\Theta\gtrsim g(\ell)^{-1}L^\mu.
}
\]

For `1<l<2`, this implies `Theta -> infinity`.

### NOT PROVED

- universal occupancy of every point-picked satellite;
- exclusion of diffuse/background amplified mass;
- Seregin's additional weighted `A_f/E_f/D_f` hypotheses;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]