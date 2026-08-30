# DSD M5-297 — Morrey-Sparse Cloud Main-Core Far-Strain Decay and Angular-Cancellation Scope Correction

Date: 2026-08-30

Parents:
- `DSD_M5_294_FORMATION_AXIS_CLOUD_BIOT_SAVART_LEADING_MULTIPOLE_AND_ANGULAR_STRAIN_ORDER_PARAMETER_2026-08-30.md`
- `DSD_M5_296_OCCUPIED_SATELLITE_MORREY_CAPACITY_AND_AMPLIFIED_PERSISTENCE_THRESHOLD_2026-08-30.md`

Status: **SCOPE CORRECTION / ON THE QUIET MORREY CORRIDOR, A RADIAL BAND OF GENUINELY OCCUPIED COMPARABLE NATURAL SATELLITES HAS ONLY `N=O(L)` MEMBERS, SO ITS ABSOLUTE LEADING FAR STRAIN AT THE MAIN CORE IS ALREADY `O(L^{-2})` RELATIVE TO THE SATELLITE NATURAL STRAIN SCALE / FIVE-COMPONENT ANGULAR CANCELLATION IS NOT REQUIRED TO HIDE SUCH A MORREY-SPARSE CLOUD FROM THE MAIN CORE / ANGULAR MULTIPOLE CONSTRAINTS REMAIN RELEVANT ONLY OUTSIDE THIS SPARSE-OCCUPIED REGIME OR FOR SATELLITE-LOCAL AMBIENT STRAIN / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-294 derived, for one natural packet at distance `d=L ell`, the leading main-core strain scale

\[
\frac{|S_i(0)|}{\ell^{-2}}\lesssim L^{-3}.
\]

It then observed that `N~L^3` coherently oriented packets could create order-one aggregate strain, motivating a five-component angular cancellation tensor.

M5-296 shows that `N~L^3` genuinely occupied packets are impossible on the centered Morrey corridor.

The present note corrects the scope of the angular-cancellation branch.

---

## 2. Assumptions

Consider a radial band at distance

\[
d\simeq L\ell,
\qquad L\gg1,
\]

containing `N` pairwise essentially disjoint occupied natural satellites of comparable scale `ell`.

Assume:

1. natural vorticity cap on each packet,
   \[
   |\omega|\le C_\omega\ell^{-2};
   \]
2. packet support volume `O(ell^3)`;
3. occupied kinetic mass floor,
   \[
   \int_{core_i}|u|^2\ge e_*\ell;
   \]
4. centered Morrey energy bound on the parent ball,
   \[
   \int_{B_{Cd}}|u|^2\le M_*d.
   \]

Then M5-296 gives

\[
\boxed{N\le C_ML.}
\]

---

## 3. Absolute leading far-strain sum

For each packet,

\[
|M_i|
=\left|\int\chi_i\omega\right|
\le
C\ell
\]

from the vorticity cap and support volume.

M5-294 therefore gives

\[
|S_i(0)|\le C\frac\ell{d^3}.
\]

Without using any angular cancellation,

\[
|S_{cloud}^{(0)}(0)|
\le
\sum_{i=1}^N|S_i(0)|
\le
CN\frac\ell{d^3}.
\]

Normalize by the satellite natural strain scale `ell^{-2}`:

\[
\frac{|S_{cloud}^{(0)}(0)|}{\ell^{-2}}
\le
C\frac{N}{L^3}.
\]

Using `N<=C_ML`,

\[
\boxed{
\frac{|S_{cloud}^{(0)}(0)|}{\ell^{-2}}
\le
\frac{C}{L^2}
\to0.
}
\]

Thus the leading cloud strain is automatically small at the main core.

---

## 4. Next multipole is even smaller

If a packet has `M_i=0`, M5-294 gives next-order strain

\[
|S_i^{(1)}(0)|\lesssim\frac{\ell^2}{d^4}.
\]

Summing `N<=C_ML` packets and normalizing by `ell^{-2}` gives

\[
\boxed{
\frac{|S_{cloud}^{(1)}(0)|}{\ell^{-2}}
\lesssim
\frac{N}{L^4}
\lesssim
L^{-3}	o0.
}
\]

Higher multipoles decay faster still, provided the corresponding natural moment bounds hold.

---

## 5. Correction to the M5-294 branching emphasis

Inside the occupied Morrey-sparse regime, the implication

\[
\text{quiet main-core far strain}
\Longrightarrow
\mathfrak A_0\approx0
\]

is **not needed**.

The stronger statement is simply

\[
\boxed{
\text{occupied Morrey-sparse remote cloud}
\Longrightarrow
S_{far,main}=o(\ell^{-2}).
}
\]

No fine angular cancellation is required.

Therefore the five-component tensor-cancellation and radial-axis-alignment branches from M5-294 are relevant primarily when at least one of the following occurs:

1. Morrey capacity fails / Campanato turnover;
2. packet occupancy degenerates so the count is not charged by kinetic energy;
3. a diffuse/background field, rather than the occupied packets, dominates the far strain;
4. one studies **ambient strain at a satellite center**, where neighboring packets need not all be distance `d` away.

---

## 6. Formation interpretation

This is a useful example of why the Formation layer should distinguish

\[
\text{object multiplicity}
\quad\text{from}\quad
\text{interaction relevance}.
\]

A cloud may contain a growing number of satellites, but if its allowed count is only `O(L)` while the interaction kernel decays like `L^{-3}`, the aggregate main-core interaction vanishes.

Thus the relevant descriptor is not `N` alone but

\[
\boxed{
\mathscr I_{far}:=N/L^3.
}
\]

On the occupied Morrey corridor,

\[
\boxed{
\mathscr I_{far}\lesssim L^{-2}\to0.
}
\]

---

## 7. Consequence for the master frontier

The persistent occupied cloud is not automatically an `H_ambient` source for the original main core.

Instead it becomes a **dynamically decoupled remote population** unless:

- satellites cluster near one another and create satellite-local ambient strain;
- they undergo replacement/material/pressure turnover;
- they generate a diffuse background field not represented by the occupied cores;
- the Morrey capacity fails.

So the frontier is better written as

\[
\boxed{
C_{occupied,remote}
\Longrightarrow
C_{decoupled}
\lor H_{sat-local}
\lor T_{dynamic}
\lor T_{Campanato}
\lor H_{background/diffuse}.
}
\]

---

## 8. Relation to the old passive-tail survivor

The automatic `L^{-2}` main-core decoupling explains why earlier audits repeatedly found a persistent passive remote tail that could coexist with an active core without paying order-one local strain.

The present calculation does not revive that branch as a contradiction.

It identifies the precise kernel/capacity mechanism:

\[
\boxed{
\text{Morrey capacity }N=O(L)
+
\text{strain kernel }L^{-3}
\Longrightarrow
\text{aggregate }L^{-2}\text{ decoupling}.
}
\]

Any closure must therefore use ancestry, global critical norms, persistence/Type-II amplification, or satellite-local interactions rather than main-core far strain alone.

---

## 9. Audit verdict

### PROVED UNDER THE OCCUPIED MORREY ASSUMPTIONS

\[
\boxed{
|S_{cloud,main}|/\ell^{-2}=O(L^{-2}).
}
\]

### SCOPE CORRECTION

Five-component angular cancellation is not a necessary condition for quiet main-core strain in the occupied Morrey-sparse regime.

### STILL OPEN

- satellite-local clustering/ambient strain;
- diffuse/background amplified field;
- ancestry/coherent-restart control of decoupled satellites;
- dynamic turnover;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]