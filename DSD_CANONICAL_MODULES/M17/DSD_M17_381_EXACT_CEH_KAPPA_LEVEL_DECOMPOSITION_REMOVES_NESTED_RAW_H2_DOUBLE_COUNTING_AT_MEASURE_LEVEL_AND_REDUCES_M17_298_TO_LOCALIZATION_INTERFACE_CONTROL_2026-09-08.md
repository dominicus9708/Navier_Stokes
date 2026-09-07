# DSD M17-381 — Exact CE-H `kappa`-level decomposition removes nested raw-`H2` double counting at measure level and reduces M17-298 to localization/interface control

Date: 2026-09-08  
Canonical ID: **M17-381**

Status: **ACTIVE CROSS-SCALE ALLOCATION ADVANCE / M17-298 MEASURE-LEVEL DEBT CLOSED ON EXACT CE-H**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. The M17-298 allocation problem

The unresolved M17-298 step required distributing shell raw-`H2` charge among intrinsic scales without counting the same raw derivative charge repeatedly on nested spatial dilations.

A variable-radius Vitali cover was insufficient because a large covering dilation may contain many smaller-scale packets whose raw `H2` charge is then counted again.

The present module uses an exact feature special to CE-H rather than another spatial cover.

## 2. Exact CE-H pointwise identity

On exact CE-H,

\[
\boxed{\Delta W=\kappa W.}
\]

Writing

\[
\rho=|W|,
\]

we have pointwise

\[
\boxed{|\Delta W|^2=\kappa^2\rho^2.}
\]

Thus every point with nonzero raw-`H2` density already carries an intrinsic coefficient scale

\[
\boxed{r_\kappa:=|\kappa|^{-1/2}.}
\]

No packet radius has yet been chosen.

## 3. Hard dyadic coefficient bins

For dyadic scales

\[
r_m=2^{-m}
\]

define disjoint bins

\[
\mathcal A_m
:=
\left\{
 c_0r_m^{-2}\le|\kappa|<C_0r_m^{-2}
\right\}
\]

with constants arranged to give a disjoint partition after a finite shift/coloring.

Define

\[
E_m:=\int_{\mathcal A_m}\rho^2dy,
\]

\[
H_m:=\int_{\mathcal A_m}|\Delta W|^2dy
=\int_{\mathcal A_m}\kappa^2\rho^2dy.
\]

Then on every bin

\[
 c_0^2r_m^{-4}E_m
\le H_m
\le C_0^2r_m^{-4}E_m.
\]

Hence

\[
\boxed{
 c\le r_m^4\frac{H_m}{E_m}\le C
}
\]

whenever `E_m>0`.

This is exactly the scale-comparability ratio required by the late M17 packet analysis, obtained **without selecting packets**.

## 4. Exact nonoverlapping allocation

Because the coefficient bins are disjoint,

\[
\boxed{
\sum_mH_m
=
\int_{\kappa\ne0}|\Delta W|^2dy.
}
\]

At `kappa=0`, exact CE-H gives

\[
\Delta W=0,
\]

so the omitted zero set carries no raw-`H2` density.

Therefore

\[
\boxed{
\sum_mH_m=H_{raw}.
}
\]

Similarly

\[
\boxed{
\sum_mE_m\le E.
}
\]

No nested spatial packet can cause cross-scale double counting because a point belongs to only one coefficient-scale class at a time.

This closes the **measure-level cross-scale allocation ambiguity** that blocked M17-298 on exact CE-H.

## 5. Spatial cube refinement without cross-scale duplication

For each coefficient scale `r_m`, tile space by disjoint cubes `Q` of side comparable to `r_m`.

Define

\[
E_{m,Q}
:=
\int_{Q\cap\mathcal A_m}\rho^2dy,
\]

\[
H_{m,Q}
:=
\int_{Q\cap\mathcal A_m}\kappa^2\rho^2dy.
\]

Then for every nonempty cell

\[
\boxed{
 c\le r_m^4\frac{H_{m,Q}}{E_{m,Q}}\le C.
}
\]

Moreover

\[
\boxed{
\sum_{m,Q}H_{m,Q}=H_{raw},
}
\]

and

\[
\boxed{
\sum_{m,Q}E_{m,Q}\le E.
}
\]

Thus even after localization to own-scale spatial cells, the accounting remains exact at the level of restricted measures.

## 6. What remains before importing M17-251/255 packet compactness

The set

\[
Q\cap\mathcal A_m
\]

need not contain a full ball on which the same coefficient scale persists.

Therefore one cannot yet replace it silently by a smooth scale-`r_m` packet with inner/mid/outer balls.

There are two possibilities:

1. **thick coefficient cell:** a fixed fraction of `E_{m,Q}` and `H_{m,Q}` lies in a spatially thick subset admitting an own-scale ball/cube localization;
2. **coefficient-bin porosity/interface:** the scale-`r_m` coefficient population is filamentary/porous at its own spatial scale or repeatedly crosses the bin boundary.

The second case is an explicit geometry/coefficient-interface branch, not a failure of raw-`H2` allocation.

## 7. Smooth coefficient partition and interface terms

Instead of hard bins, choose a smooth dyadic partition of unity in `log |kappa|`,

\[
\chi_m(\kappa),
\qquad
\sum_m\chi_m(\kappa)^2=1
\quad(\kappa\ne0),
\]

with

\[
\operatorname{supp}\chi_m
\subset
\{|\kappa|\asymp r_m^{-2}\}.
\]

The weighted allocation quantities

\[
E_m^\chi:=\int\chi_m^2\rho^2dy,
\]

\[
H_m^\chi:=\int\chi_m^2\kappa^2\rho^2dy
\]

still satisfy

\[
 r_m^4H_m^\chi\asymp E_m^\chi
\]

and bounded-overlap summation.

If one promotes

\[
W_m:=\chi_m(\kappa)W
\]

to an actual localized field, then

\[
\Delta W_m
=
\chi_m\Delta W
+2\nabla\chi_m\cdot\nabla W
+(\Delta\chi_m)W.
\]

The new terms are exactly coefficient-gradient/interface terms involving

\[
\nabla\kappa,
\qquad
\Delta\kappa.
\]

Thus the only cost of converting the exact measure allocation into smooth localized packets is routed to the already typed coefficient-gradient/interface channels rather than back to an unclassified cross-scale overlap.

## 8. Revised status of M17-298 on CE-H

The old statement

\[
G_{cross\text{-}scale\ raw\text{-}H2\ allocation}
\]

should now be split into

\[
\boxed{
G_{M17\text{-}298}
\Longrightarrow
H_{exact\ coefficient\text{-}scale\ measure\ allocation}
\lor
G_{coefficient\text{-}bin\ localization/interface}.
}
\]

On exact CE-H, the first branch is now proved by Sections 2--5.

Therefore the remaining open part of M17-298 is no longer **which scale owns the raw `H2` charge**. It is whether the coefficient-scale measure can be upgraded to the spatially thick smooth packet geometry required by later packet/tangent arguments without paying an already-recognized interface/gradient exit.

## 9. Relation to M17-380

M17-380 independently derived the multiscale flux packing law

\[
\sum_mr_m^{-5/2}\Phi_m
\lesssim(MH)^{1/2}.
\]

The present decomposition explains why that sum is legitimate: the dyadic coefficient scales form a nonduplicating raw-`H2` allocation on CE-H.

The two modules together provide a partition-free coefficient-scale architecture for the nodal and raw-`H2` branches.

## 10. DSD-theory role

The useful heuristic is to assign a quantity to the scale encoded by the field itself rather than to every spatial cover that happens to contain it. The proof is entirely the exact CE-H identity and dyadic measure decomposition.

## 11. Audit verdict

**PASS — substantial advance.**

On exact CE-H,

\[
\boxed{
\text{cross-scale raw-`H2` ownership is now exact at measure level.}
}
\]

The surviving M17-298 debt is a **localization/interface theorem**, not a cross-scale double-counting theorem.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]