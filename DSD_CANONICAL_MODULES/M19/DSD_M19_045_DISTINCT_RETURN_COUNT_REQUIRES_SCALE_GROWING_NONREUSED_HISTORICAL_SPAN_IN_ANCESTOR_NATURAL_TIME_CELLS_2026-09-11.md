# M19-045 — Distinct return count requires scale-growing nonreused historical span in ancestor-natural-time cells

**Date:** 2026-09-11  
**Status:** CALCULATION / R-AC RETURN-COUNT TO HISTORICAL-SPAN CONVERSION / MULTI-CELL NECESSITY

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input

M19-040 reduces the quiet R-AC branch to

\[
\boxed{
N_k^{dist}\rho_k
\gtrsim
J_k^{1/2}
}
\]

on a subset carrying divergent cubic mass

\[
\sum_k J_k^{3/2}=\infty.
\]

Here \(\rho_k\) is the physical ancestor-shell radius and \(N_k^{dist}\) counts genuinely nonreused historical return episodes.

M19-039 proves that one retained same-population contact has duration

\[
\boxed{
\tau_{contact}\ge c_0\rho_k^2
}
\]

on the bounded weak-\(L^3\), shell-comparable, controlled-center, quiet-source branch.

The present module converts the count requirement into an exact historical-span requirement.

## 2. Distinct contacts need distinct natural-time support

Let

\[
I_{k,1},\dots,I_{k,N_k^{dist}}
\]

be selected nonreused contact intervals at shell radius \(\rho_k\).

By the nonreuse rule, the same physical contact cannot be counted twice merely because overlapping observation windows record it repeatedly.

After the standard bounded-overlap extraction, assume the selected intervals have overlap multiplicity at most \(Q<\infty\).

Since

\[
|I_{k,\ell}|\ge c_0\rho_k^2,
\]

we obtain for the measure of their union

\[
\boxed{
\left|
\bigcup_{\ell=1}^{N_k^{dist}}I_{k,\ell}
\right|
\ge
\frac{c_0}{Q}
N_k^{dist}\rho_k^2.
}
\]

Define the nonreused historical span/occupation measure

\[
\boxed{
L_k^{hist}
:=
\left|
\bigcup_{\ell=1}^{N_k^{dist}}I_{k,\ell}
\right|.
}
\]

Then

\[
\boxed{
L_k^{hist}
\gtrsim
N_k^{dist}\rho_k^2.
}
\]

This uses only genuine contact duration and nonreuse; no additive-energy claim is involved.

## 3. Return-count closure implies a historical-span threshold

If the sufficient R-AC return condition holds,

\[
N_k^{dist}\rho_k
\gtrsim
J_k^{1/2},
\]

then multiplying by \(\rho_k\) gives

\[
N_k^{dist}\rho_k^2
\gtrsim
J_k^{1/2}\rho_k.
\]

Hence necessarily

\[
\boxed{
L_k^{hist}
\gtrsim
J_k^{1/2}\rho_k.
}
\]

Thus the return-count theorem can be rewritten as a demand for a sufficiently long **nonreused historical occupation span** at the ancestor shell.

## 4. Natural-time-cell normalization

Normalize the historical span by one ancestor natural parabolic time:

\[
\boxed{
H_k
:=
\frac{L_k^{hist}}{\rho_k^2}.
}
\]

Then

\[
H_k\gtrsim N_k^{dist}
\]

up to the fixed bounded-overlap constants, and the closure threshold becomes

\[
\boxed{
H_k
\gtrsim
\frac{J_k^{1/2}}{\rho_k}.
}
\]

Therefore R-AC requires not merely one natural-time contact but a number of **nonreused ancestor-natural-time cells** of order

\[
\boxed{
\frac{J_k^{1/2}}{\rho_k}.
}
\]

This is the historical-span form of \(\mathcal T_{count}^{dist}\).

## 5. Fixed natural-time windows cannot carry the generic cubic-divergent branch

Suppose a selected shell family is restricted to only a fixed number of ancestor natural-time cells:

\[
H_k\le H_*<\infty.
\]

Then the return threshold can hold only when

\[
\boxed{
J_k^{1/2}
\lesssim
H_*\rho_k.
}
\]

Equivalently,

\[
\boxed{
J_k^{3/2}
\lesssim
H_*^3\rho_k^3.
}
\]

Consequently, on any standard shrinking shell family satisfying

\[
\boxed{
\sum_k\rho_k^3<\infty,
}
\]

the subset whose R-AC closure can be supplied inside only \(O(1)\) natural-time cells has finite cubic mass:

\[
\boxed{
\sum_{k:H_k\le H_*}
J_k^{3/2}<\infty
}
\]

whenever the return threshold itself is realized there.

Therefore a cubic-mass-divergent survivor cannot be closed by uniformly bounded historical depth on such a geometric shrinking-radius family.

## 6. Divergent cubic mass forces scale-growing historical depth, conditionally on geometric radius summability

Under

\[
\sum_kJ_k^{3/2}=\infty
\]

and

\[
\sum_k\rho_k^3<\infty,
\]

for every fixed \(H_*<\infty\), the shells satisfying both

\[
H_k\le H_*
\]

and the return closure inequality carry only finite cubic mass.

Hence any successful closure on a cubic-divergent family must use shells for which

\[
\boxed{
H_k\to\infty
}

in cubic-mass density, more precisely at the quantitative scale

\[
\boxed{
H_k
\gtrsim
J_k^{1/2}/\rho_k.
}
\]

This is stronger than merely saying that infinitely many returns are needed.

It states how many natural-time cells of historical support must be genuinely available.

## 7. Relation to M18-055

M18-055 proves that one fixed second-generation record annulus has only order-one capacity for independent fixed-thickness events.

M19-045 is the physical-time counterpart:

\[
\boxed{
\text{one fixed ancestor-natural-time cell}
\Rightarrow
N_k^{dist}=O(1).
}
\]

Therefore the scale-growing factor required by

\[
J_k^{1/2}/\rho_k
\]

cannot be manufactured inside one record cell.

It must come from **many genuinely different parent-time cells**.

This is exactly where the fixed-parent bounded-overlap and cross-generation synchronization problem becomes decisive.

## 8. Radial variation interpretation

M19-040 also gives, modulo typed source/diffusion/exchange terms,

\[
\int|C_{rad}|dt
\gtrsim
N_k^{dist}m_{*,k}.
\]

M19-039 bounds the instantaneous crossing rate on the quiet branch by the natural-time scale

\[
|C_{rad}|
\lesssim
\rho_k^{-2}M_{i,\rho_k}.
\]

Thus the same calculation says that each order-one exit/re-entry excursion consumes order \(\rho_k^2\) of physical time.

The radial current therefore controls **spacing/capacity**, not a lower bound on how many returns occur.

The missing theorem remains historical recurrence/nonreuse, not local radial kinematics.

## 9. Sharpened R-AC frontier

Define

\[
\boxed{
\mathcal T_{span}^{hist}:
L_k^{hist}
\gtrsim
J_k^{1/2}\rho_k
}
\]

or equivalently

\[
\boxed{
\mathcal T_{cells}^{hist}:
H_k
=\frac{L_k^{hist}}{\rho_k^2}
\gtrsim
\frac{J_k^{1/2}}{\rho_k}.
}
\]

Then, on the M19-039 retained branch,

\[
\boxed{
\mathcal T_{count}^{dist}
\Longrightarrow
\mathcal T_{span}^{hist}.
}
\]

Conversely, historical span alone does not imply distinct returns; one could spend the whole span in one long contact.

Thus the exact remaining theorem must combine

1. enough historical span, and
2. enough completed nonreused exit/re-entry or distinct-population episodes inside that span.

## 10. New two-factor formulation

The R-AC requirement may now be written as

\[
\boxed{
\underbrace{H_k}_{\text{available nonreused natural-time cells}}
\times
\underbrace{\vartheta_k}_{\text{fraction realized as distinct returns}}
\gtrsim
\frac{J_k^{1/2}}{\rho_k},
}
\]

where

\[
0\le\vartheta_k\le1
\]

is an effective distinct-return occupancy fraction.

This separates two mechanisms that were previously mixed:

- historical depth / span;
- actual return occupancy inside that history.

A failure of the first is a record-placement / ancestry-depth defect.
A failure of the second is a material-return incidence defect.

Both are R-AC, but they now have different quantitative signatures.

## 11. What is not proved

M19-045 does not prove a lower bound on \(L_k^{hist}\), \(H_k\), or \(\vartheta_k\).

It does not prove \(\sum\rho_k^3<\infty\) for every possible R-AC realization; section 5--6 is conditional on the standard geometric shrinking-radius family where that summability is certified.

It does not prove the distinct-return theorem.

It only converts the required count into an exact historical-span / occupancy threshold and shows that bounded historical depth is insufficient on the geometric shrinking-radius corridor.

## 12. Next calculation

The next target should compare the required historical cell depth

\[
H_k
\gtrsim
J_k^{1/2}/\rho_k
\]

with the actual first-hitting age clock.

The first-hitting genealogy already supplies an explicit geometric relation between age, physical radius, and backward historical time.

The key question is:

\[
\boxed{
\text{Does the available backward first-hitting age provide enough natural-time cells,}
}
\]

and if it does, does finite material memory / recurrence force a nonvanishing occupancy fraction \(\vartheta_k\)?

This separates **capacity** from **occupation** one final time.

---

\[
\boxed{\text{M19-045 COMPLETE; DISTINCT RETURN COUNT IS NOW A SCALE-GROWING HISTORICAL-SPAN PLUS OCCUPANCY PROBLEM.}}
\]