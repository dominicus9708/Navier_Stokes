# M19-317 — Annular nonreuse alone does not close GMS: M17-307 tolerates one critical palinstrophy event per geometric record, and linear record multiplicity is the true threshold

**Date:** 2026-09-16  
**Status:** MAJOR GMS AUDIT CORRECTION / NONREUSE NECESSARY BUT NOT SUFFICIENT / LINEAR MULTIPLICITY THRESHOLD

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Correction to the immediate reading of M19-315--316

M19-315 identifies a natural `r`-weighted palinstrophy Carleson structure and M19-316 conditionally places first-hitting carriers in fixed physical parabolic annuli.

It is tempting to conclude that a fixed positive annular palinstrophy payment at every scale would contradict a finite packing budget.

That conclusion is not currently certified.

The reason is the exact cross-generation weight in M17-307.

## 2. True M17-307 ledger

For second-generation record factor `R_m`, define normalized record-cell palinstrophy

\[
p_m:=\int_I\|\nabla\Omega_m(s)\|_2^2ds.
\]

M17-307 proves

\[
\boxed{
\sum_m R_m^{-1}p_m<\infty.
}
\]

The record factors grow geometrically:

\[
R_m\asymp q^{m/2}.
\]

Therefore

\[
\sum_mR_m^{-1}<\infty.
\]

## 3. One order-one event per record is allowed

Suppose the ideal carrier-to-payer localization theorem of M19-316 is proved and gives

\[
\boxed{p_m\ge c_*>0}
\]

for one annularly localized critical palinstrophy event in every geometric record.

Then the ledger only receives

\[
\sum_m\frac{p_m}{R_m}
\ge
c_*\sum_m\frac1{R_m}.
\]

But the right side is finite.

Hence

\[
\boxed{
\text{one fixed critical palinstrophy event per geometric record}
\text{ is fully compatible with M17-307.}
}
\]

Annular nonreuse eliminates one kind of double counting but does not remove the inverse-record-scale ancestry discount.

## 4. Relation to physical critical cost

M19-314 gives

\[
Q_{j,m}^{phys}=\rho_{j,m}^{-1}p_m.
\]

Thus an order-one normalized event corresponds to critical physical cost

\[
Q_{j,m}^{phys}\gtrsim \rho_{j,m}^{-1}.
\]

The physical critical charge

\[
\rho_{j,m}Q_{j,m}^{phys}
\]

is order one.

But there is no certified finite physical budget for the sum of these critical charges across all scales approaching the singular time.

The physical palinstrophy itself may diverge at a hypothetical singularity.

Therefore the `r`-weighted Carleson identity is bookkeeping unless its parent critical charge is independently finite.

## 5. True multiplicity threshold

Suppose record `m` contains `N_m` pairwise nonreused descendant/annular payments, each with

\[
p_{m,k}\ge c_*>0.
\]

Then

\[
p_m\ge c_*N_m
\]

provided the payments are genuinely disjoint in the derivative measure.

M17-307 then forces

\[
\boxed{
\sum_m\frac{N_m}{R_m}<\infty.
}
\]

Therefore a contradiction requires

\[
\boxed{
\sum_m\frac{N_m}{R_m}=\infty.
}
\]

Since `R_m` is geometric, polynomial or logarithmic multiplicity in `m` is insufficient.

The critical order is essentially

\[
\boxed{N_m\gtrsim R_m}
\]

on a sufficiently persistent set of records.

This is exactly the threshold already implicit in M17-307, now reinterpreted as the minimal multiplicity burden for the palinstrophy-level GMS route.

## 6. Improvement over the raw-H2 route

For raw-H2, the ancestry discount is `R_m^{-3}`. A fixed order-one event therefore requires approximately cubic record multiplicity to challenge the finite ledger.

For palinstrophy, the discount is only `R_m^{-1}`.

Thus M19-313 still produces a genuine gain:

\[
\boxed{
\text{required multiplicity severity:}
\quad
R_m^3
\longrightarrow
R_m.
}
\]

The route is much less severe, but not automatically closed.

## 7. Revised hierarchy of GMS obligations

The GMS palinstrophy route now requires all of the following:

1. **physical incidence / carrier placement** — conditionally reduced by M19-316;
2. **carrier-to-payer localization** — convert nested GMS floor into a local critical palinstrophy event;
3. **bounded reuse / derivative-measure disjointness** — avoid charging one packet repeatedly;
4. **multiplicity enhancement or subcritical gain** — enough to overcome `R_m^{-1}`.

The fourth item is essential and was not removed by M19-315.

## 8. Two ways to beat the inverse-record discount

### A. Multiplicity

Prove

\[
N_m\gtrsim R_m
\]

or another law with

\[
\sum_mN_m/R_m=\infty.
\]

### B. Per-event amplification

Instead of many events, prove each selected event has normalized palinstrophy charge

\[
p_m\gtrsim a_m
\]

with

\[
\sum_m a_m/R_m=\infty.
\]

This could arise from derivative-frequency escalation, prolonged residence, or geometry that forces supercritical palinstrophy at the record scale.

## 9. Permanent firewall

\[
\boxed{
\text{annular nonreuse}
\not\Rightarrow
\text{ancestral contradiction}.
}
\]

The cross-generation discount must still be paid.

Likewise

\[
\boxed{
\text{one singular critical event per scale}
\not\Rightarrow
\text{divergent M17-307 ledger}.
}
\]

## 10. Revised GMS target

The live gate is now

\[
\boxed{
\mathcal T_{GMS}^{pal/mult}:
\text{after physical annular incidence, force either linear-in-record multiplicity or supercritical per-event palinstrophy sufficient to violate }\sum_mR_m^{-1}p_m<\infty.
}
\]

This is narrower and more accurate than a generic base-gain label.

## 11. Verdict

M19-313 reduces the analytic derivative level and M19-316 improves physical placement, but the M17-307 inverse-record discount remains decisive.

The next high-value calculation is to search the first-hitting/recurrent genealogy for a mechanism producing `N_m` of order `R_m`, or an equivalent supercritical palinstrophy amplification.

---

\[
\boxed{\text{M19-317 COMPLETE; THE PALINSTROPHY GMS ROUTE REQUIRES LINEAR RECORD MULTIPLICITY OR AN EQUIVALENT SUPERCRITICAL GAIN.}}
\]