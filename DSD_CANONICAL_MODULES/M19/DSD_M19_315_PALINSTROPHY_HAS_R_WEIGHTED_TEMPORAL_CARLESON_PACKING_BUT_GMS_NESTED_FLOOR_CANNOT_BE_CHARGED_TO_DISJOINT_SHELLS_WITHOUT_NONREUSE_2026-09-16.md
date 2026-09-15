# M19-315 — Palinstrophy has an r-weighted temporal Carleson packing, but the GMS nested floor cannot be charged to disjoint shells without a nonreuse theorem

**Date:** 2026-09-16  
**Status:** ACTIVE GMS TRANSFER AUDIT / PALINSTROPHY CARLESON STRUCTURE / NESTED-REUSE FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Motivation

M19-313 lowers the analytic GMS derivative threshold from physical raw-H2 / `D3 u` to physical palinstrophy / `D2 u`.

M19-314 then shows that the physically restored record-cell palinstrophy has the critical scaling

\[
Q_{pal}^{phys}\sim \rho^{-1}.
\]

The natural question is whether the temporal Carleson allocation idea of M17-386 improves this critical factor.

## 2. Palinstrophy critical weight

For vorticity palinstrophy

\[
P(t):=\|\nabla\Omega(t)\|_2^2,
\]

Navier--Stokes parabolic scaling gives

\[
\int P_\lambda(t)dt
=\lambda\int P(t)dt.
\]

Hence the scale-invariant spacetime palinstrophy charge at parabolic scale `r` is

\[
\boxed{
\mathcal C_P(r,I):=
 r\int_I P(t)dt.
}
\]

This is the palinstrophy analogue of the `r^3` raw-H2 charge in M17-386.

## 3. Single-genealogy temporal Carleson packing

Fix a parent interval `I_R^*` and a single material/genealogical chain with dyadic own scales

\[
r_m=2^{-m}R.
\]

Let `I_{m,k}` be own-scale intervals satisfying bounded same-scale overlap

\[
\sum_k\mathbf 1_{I_{m,k}}(t)\le N_0.
\]

Then

\[
\begin{aligned}
\sum_{m,k}
 r_m\int_{I_{m,k}}P(t)dt
&=
\int P(t)
\left(\sum_{m,k}r_m\mathbf 1_{I_{m,k}}(t)\right)dt\\
&\le
N_0\left(\sum_mr_m\right)
\int_{I_R^*}P(t)dt.
\end{aligned}
\]

Since

\[
\sum_mr_m=2R,
\]

we obtain

\[
\boxed{
\sum_{m,k}
 r_m\int_{I_{m,k}}P(t)dt
\le
2N_0R
\int_{I_R^*}P(t)dt.
}
\]

Thus palinstrophy has a genuine `r`-weighted temporal Carleson packing along one genealogy.

## 4. Relation to the physical composite radius

For the M19-314 two-scale reconstruction

\[
\rho=r_jR,
\]

the physical record-cell cost is

\[
Q_{j,R}^{phys}=ho^{-1}p_R.
\]

Multiplication by the physical scale gives

\[
\boxed{
\rho Q_{j,R}^{phys}=p_R.
}
\]

Thus the natural scale-invariant physical palinstrophy charge is precisely the normalized record-cell palinstrophy.

No extra gain appears merely from rewriting the same quantity in Carleson form.

## 5. GMS singular floor is nested, not annular

M19-254 proves that at a genuine singular point, for every sufficiently small `r`,

\[
\boxed{
H_V(r):=r^{-5/3}F_V(r)\ge c_*>0,
}
\]

where `F_V(r)` is measured on the nested Galilean cylinder `Q_r^V`.

However, the cylinders are nested:

\[
Q_{r_{m+1}}^V\subset Q_{r_m}^V.
\]

A single central concentration may therefore pay the lower bound at many scales simultaneously.

M19-254 already records the permanent firewall

\[
\boxed{
\text{nested-scale lower bounds}
\not\Rightarrow
\text{disjoint-annulus lower bounds}.
}
\]

## 6. Why the two facts do not yet contradict each other

The Carleson estimate counts scale-weighted derivative cost assigned to an interval family.

The GMS floor does not currently assign a distinct derivative payer to each scale. Therefore one may not write

\[
H_V(r_m)\ge c_*
\quad\Longrightarrow\quad
r_mP_m\ge c
\]

for pairwise disjoint `P_m` and then sum over `m`.

That would silently assume exactly the scale-nonreuse theorem that is missing.

Hence

\[
\boxed{
\text{GMS floor}+\text{palinstrophy Carleson packing}
\not\Rightarrow
\text{contradiction without a nonreuse/incidence bridge}.
}
\]

## 7. Precise missing bridge

A useful bridge would have one of the following forms.

### A. Annular derivative nonreuse

For infinitely many dyadic scales,

\[
H_V(r_m)\ge c_*
\Longrightarrow
r_m\int_{Q_{Cr_m}^V\setminus Q_{c r_m}^V}|D^2u|^2
\ge c_1>0.
\]

Then disjoint annuli could be compared to an `r`-weighted packing.

### B. Bounded scale reuse

Every physical derivative packet may pay the GMS floor for at most `N_*` dyadic scales.

### C. First-hitting incidence

The singular floor must intersect a first-hitting/genealogical cell whose own critical palinstrophy charge is bounded below, with uniformly bounded reuse across scales.

### D. Direct weighted estimate

Prove a representation-safe inequality controlling the logarithmic GMS payer by a certified finite weighted palinstrophy measure without first assigning annular payers.

## 8. Relation to M17-386

M17-386 closes temporal double counting along one genealogy for raw-H2 but leaves concurrent spatial payer localization open.

The palinstrophy-level problem is analogous but sharper:

- temporal scale weighting is easy and uses `r` rather than `r^3`;
- the obstruction is again **dynamic/spatial incidence**, not raw measure ownership;
- a nonlocal pressure/strain field may allow one core concentration to influence several nested scales.

Thus the current GMS obstruction is best described as a scale-reuse/localization problem.

## 9. Revised gate

The M19-314 gate refines to

\[
\boxed{
\mathcal T_{GMS}^{pal/nonreuse}:
\text{convert the nested GMS floor into bounded-reuse physical palinstrophy incidence at scale }\rho.
}
\]

Only after this bridge is available can the `r`-weighted Carleson structure be used as a contradiction mechanism.

## 10. Verdict

Palinstrophy does possess the expected critical temporal Carleson packing.

But this is bookkeeping, not yet base gain. The GMS singularity floor is nested and may reuse one central concentration across infinitely many scales.

The next calculation must therefore target scale nonreuse / annular incidence rather than another weighted sum.

---

\[
\boxed{\text{M19-315 COMPLETE; THE GMS TRANSFER PROBLEM IS NOW A CRITICAL PALINSTROPHY NONREUSE/INCIDENCE PROBLEM.}}
\]