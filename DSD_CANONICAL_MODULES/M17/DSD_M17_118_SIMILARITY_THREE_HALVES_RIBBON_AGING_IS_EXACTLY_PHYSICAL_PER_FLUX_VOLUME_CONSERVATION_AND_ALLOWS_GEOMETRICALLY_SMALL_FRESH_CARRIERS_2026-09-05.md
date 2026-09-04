# DSD M17-118 — Similarity three-halves ribbon aging is exactly physical per-flux-volume conservation and allows geometrically small fresh carriers

Date: 2026-09-05
Canonical ID: **M17-118**

Status: **INTERNAL SIMILARITY/PHYSICAL SCALE AUDIT / M17-116 DERIVES `d/dtheta log(ds_sim/|J_sim|)=3/2` FOR A MATERIAL DIRECTOR-AREA KERNEL LOOP. IN THE RETAINED NAVIER--STOKES SIMILARITY NORMALIZATION `B=U+y/2`, THE PHYSICAL LENGTH SCALE IS `r(theta)=e^{-theta/2}`. SINCE THE DIRECTOR-AREA CURRENT CONTAINS TWO SPATIAL DERIVATIVES, `J_phys=r^-2 J_sim`, WHILE `ds_phys=r ds_sim`. THEREFORE `ds_phys/|J_phys|=r^3 ds_sim/|J_sim|`, AND THE FACTOR `r^3=e^{-3theta/2}` EXACTLY CANCELS THE M17-116 SIMILARITY GROWTH. THE PHYSICAL PER-DIRECTOR-AREA-FLUX VOLUME OF A MATERIAL LOOP IS CONSTANT, AS EXPECTED FROM INCOMPRESSIBLE PHYSICAL TRANSPORT. CONSEQUENTLY THE NEED FOR FRESH LATE-STAGE RIBBON CARRIERS DOES NOT REQUIRE AN INFINITE PHYSICAL-VOLUME RESERVOIR: A COMPACT O(1) SIMILARITY CARRIER AT STAGE `j` CORRESPONDS TO O(`r_j^3`) PHYSICAL PER-FLUX VOLUME. GEOMETRICALLY SHRINKING FRESH CARRIERS CAN THEREFORE SERVICE INFINITE SIMILARITY-TIME TURNOVER WITH FINITE PHYSICAL VOLUME. THIS EXPLAINS WHY M17-116 IS A SAME-MATERIAL RECURRENCE OBSTRUCTION BUT NOT A PHYSICAL ENERGY/VOLUME CONTRADICTION, AND WHY THE M5 WEIGHTED RETURN-DENSITY LOWER BOUND REMAINS NECESSARY. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Retained similarity scaling

The CE-H similarity drift is

\[
B=U+\frac12y.
\]

This is the standard backward parabolic normalization with logarithmic similarity time `theta` and physical length scale

\[
\boxed{
r(\theta)=e^{-\theta/2}}
\]

up to the fixed reference normalization.

Thus

\[
x=r(\theta)y.
\]

---

## 2. Scaling of director derivatives and area current

The director `xi` is dimensionless.
Therefore one physical spatial derivative contributes one factor `r^-1` relative to a similarity derivative:

\[
\nabla_x\xi
=r^{-1}\nabla_y\xi.
\]

The director-area current is quadratic in first derivatives of `xi`:

\[
J_\xi^k
=\frac12\varepsilon^{kij}
\xi\cdot(\partial_i\xi\times\partial_j\xi).
\]

Hence

\[
\boxed{
J_{\xi,phys}
=r^{-2}J_{\xi,sim}.
}
\]

A line element scales as

\[
\boxed{
ds_{phys}=r\,ds_{sim}.}
\]

---

## 3. Per-flux volume scaling

Combine Section 2:

\[
\frac{ds_{phys}}{|J_{phys}|}
=
\frac{r\,ds_{sim}}
{r^{-2}|J_{sim}|}.
\]

Therefore

\[
\boxed{
\frac{ds_{phys}}{|J_{phys}|}
=r^3
\frac{ds_{sim}}{|J_{sim}|}.
}
\]

The quantity `ds/|J|` has the expected physical dimension of volume per dimensionless director-area flux.

---

## 4. Exact cancellation with M17-116

M17-116 gives

\[
\boxed{
\frac d{d\theta}
\log\left(
\frac{ds_{sim}}{|J_{sim}|}
\right)
=\frac32.
}
\]

But

\[
\frac d{d\theta}\log r^3
=-\frac32.
\]

Hence

\[
\boxed{
\frac d{d\theta}
\log\left(
\frac{ds_{phys}}{|J_{phys}|}
\right)
=0.
}
\]

Thus the physical per-flux volume element is materially constant.

For a closed material loop,

\[
\boxed{
\oint
\frac{ds_{phys}}{|J_{phys}|}
=\text{constant}.
}
\]

The similarity `3/2` expansion is exactly the coordinate representation of physical incompressible volume conservation.

---

## 5. Meaning of the compact similarity ribbon class

A compact nondegenerate ribbon class has

\[
\mathscr V_{J,sim}
=\oint\frac{ds_{sim}}{|J_{sim}|}
\asymp1.
\]

At first-hitting stage `j` with scale `r_j`, the corresponding physical per-flux volume is therefore

\[
\boxed{
\mathscr V_{J,phys}
\asymp r_j^3.
}
\]

As

\[
r_j\to0,
\]

later compact similarity carriers may be represented by material loops with progressively smaller physical per-flux volume.

---

## 6. Infinite fresh carriers need not require infinite physical volume

M17-116--117 imply that the same material loop cannot keep reappearing indefinitely in the same compact similarity ribbon class.
Eulerian recurrence needs fresh labels.

However if stage-`j` carriers occupy physical per-flux volume of order

\[
r_j^3,
\]

then a geometrically shrinking sequence can satisfy

\[
\sum_j r_j^3<\infty
\]

for geometric first-hitting scales.

Therefore the existence of infinitely many distinct fresh material carriers is compatible with a finite total physical-volume reservoir.

No contradiction follows from carrier number alone.

---

## 7. Physical dissipation scale audit

On a compact active similarity core with

\[
\rho_{sim}\ge c_\rho>0,
\]

physical vorticity has the parabolic scaling

\[
\rho_{phys}\asymp r_j^{-2}\rho_{sim}.
\]

The velocity-gradient energy density is bounded below by a fixed multiple of vorticity squared, so at the scaling level

\[
|\nabla u|^2
\gtrsim r_j^{-4}
\]

on such a retained active packet.

Multiplying by physical per-flux volume `~r_j^3` gives an instantaneous dissipation rate per unit director-area flux of order at least

\[
\boxed{r_j^{-1}.}
\]

But an `O(1)` similarity-time residence lasts only physical time of order

\[
r_j^2.
\]

Therefore its physical dissipation cost per unit flux is only of order

\[
\boxed{r_j.}
\]

A geometric sequence of such costs can be summable.

This scaling audit is consistent with M17-117/M5's weighted-return loss and does not by itself give a Leray contradiction.

---

## 8. Why amplitude/return genealogy is essential

Physical volume conservation allows indefinitely many smaller fresh carriers.
The energy ledger can still close the branch only if the recurrent structure forces enough

- amplitude,
- dwell,
- multiplicity,
- or ancestral-scale return weight

that the sum of physical costs ceases to be summable.

This is exactly the role of the M5 target

\[
\mathfrak R_k\gtrsim J_k^{1/2}
\]

on a cubic-divergent subset.

Thus M17's director-area genealogy does not replace the M5 amplitude-weighted return theorem; it supplies a more rigid carrier identity to which that theorem would have to apply.

---

## 9. DSD analysis

The same material object has opposite-looking descriptions:

\[
\boxed{
\text{similarity per-flux volume}
\sim e^{3\theta/2},
}
\]

but

\[
\boxed{
\text{physical per-flux volume}
=\text{constant}.
}
\]

The apparent expansion is entirely a scale-coordinate effect.

This prevents a false infinite-volume contradiction while preserving the valid same-similarity-class recurrence obstruction.

---

## 10. DSD audit

### Audit A — treating similarity per-flux growth as physical volume creation
Rejected.

### Audit B — concluding infinitely many fresh labels require infinite physical volume
Rejected; their physical per-flux volumes may decay like `r_j^3`.

### Audit C — concluding a uniform similarity residence time gives uniform physical energy cost
Rejected; the scale audit gives a cost of order `r_j` per current-scale event under the stated compact-amplitude assumptions.

### Audit D — claiming the scaling estimate itself proves the exact M5 return-density exponent
Rejected. It is a consistency/scaling audit, not the missing genealogy theorem.

### Audit E — proof status
The physical meaning of ribbon turnover is clarified, but the energy closure remains conditional on stronger return/amplitude genealogy.

---

## 11. Updated ribbon/M5 frontier

The ribbon branch now has the exact interpretation

\[
\boxed{
\text{same material compact similarity recurrence impossible}
}

but

\[
\boxed{
\text{Eulerian fresh-carrier recurrence physically volume-compatible}.
}
\]

To close it, one must show that the fresh-carrier cascade has **nonsummable physical weighted activity**, not merely infinitely many carriers.

The next useful direction is therefore the M17-to-M5 amplitude-retention bridge: determine whether a director-area ribbon/peak carrier with positive Rank-2 compensation necessarily retains a quantitative fraction of the annular `J_k` or vorticity-gradient mass for long enough to force the M5 weighted return lower bound.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
