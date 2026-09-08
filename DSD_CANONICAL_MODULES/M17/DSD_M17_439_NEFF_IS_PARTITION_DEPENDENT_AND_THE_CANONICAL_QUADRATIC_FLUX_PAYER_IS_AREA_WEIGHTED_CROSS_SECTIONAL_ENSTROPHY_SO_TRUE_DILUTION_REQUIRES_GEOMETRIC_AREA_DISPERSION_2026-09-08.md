# DSD M17-439 — `N_eff` is partition-dependent and the canonical quadratic flux payer is area-weighted cross-sectional enstrophy, so true dilution requires geometric area dispersion

Date: 2026-09-08  
Canonical ID: **M17-439**

Status: **ACTIVE QUADRATIC-FLUX REPRESENTATION CORRECTION / M17-432--433 REFINEMENT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Correction target

Corrected M17-432 distinguishes flux-linear currencies from the flux-quadratic M17-413 raw-`H2` packet.

M17-433 introduced for a discrete band partition

\[
N_{eff}
=
\frac{(\sum_i\phi_i)^2}{\sum_i\phi_i^2}
\]

and obtained the valid lower bound

\[
\sum_i\phi_i^2
=
\frac{\Phi^2}{N_{eff}}.
\]

However `N_eff` itself depends on how one chooses the tube-band partition.

Splitting one band of flux `phi` into two bookkeeping bands of flux `phi/2` changes its contribution from

\[
\phi^2
\]

to

\[
2(\phi/2)^2=\phi^2/2,
\]

although the physical field has not changed.

Therefore arbitrary growth of `N_eff` is **not by itself a physical PDE decompactification**.

The M17-433 formula remains a valid lower bound for a fixed geometrically canonical partition, but `N_eff` must not be used as a partition-free invariant.

## 2. Cross-sectional flux and enstrophy

Let `A` be the actual union of retained transverse cross-sectional regions at one loop arclength level or one geometrically coherent family level.

Let

\[
\Phi
=
\int_A\rho\,dA
\]

be the total oriented positive vorticity flux.

Cauchy--Schwarz gives

\[
\boxed{
\Phi^2
\le
|A|
\int_A\rho^2dA.
}
\]

Therefore

\[
\boxed{
\int_A\rho^2dA
\ge
\frac{\Phi^2}{A_{tot}},
\qquad
A_{tot}:=|A|.
}
\]

This statement is independent of any subdivision of `A` into label bands.

## 3. Partition-refined lower bound is monotone, not diluting

Let

\[
A=\bigsqcup_iA_i,
\qquad
\phi_i=\int_{A_i}\rho dA.
\]

Then on each component

\[
\int_{A_i}\rho^2dA
\ge
\frac{\phi_i^2}{A_i}.
\]

Summing,

\[
\boxed{
\int_A\rho^2dA
\ge
\sum_i\frac{\phi_i^2}{A_i}.
}
\]

If one refines a region into smaller subregions, the quantity

\[
\sum_i\frac{\phi_i^2}{A_i}
\]

cannot decrease under the optimal regrouping comparison: Cauchy gives

\[
\frac{(\phi_1+\phi_2)^2}{A_1+A_2}
\le
\frac{\phi_1^2}{A_1}
+
\frac{\phi_2^2}{A_2}.
\]

Thus physical refinement does not create a genuine quadratic payer loss.

The unweighted sum `sum phi_i^2` in M17-433 can decrease under artificial refinement only because it dropped the corresponding cross-sectional area weights.

## 4. Canonical normalized quadratic flux currency

At own scale `r`, define

\[
\boxed{
\mathfrak Q_\Phi(A)
:=
r^2\int_A\rho^2dA.
}
\]

This is the natural dimensionless cross-sectional enstrophy currency.

The flux lower bound is

\[
\boxed{
\mathfrak Q_\Phi(A)
\ge
r^2\frac{\Phi^2}{A_{tot}}.
}
\]

Define the geometric area participation factor

\[
\boxed{
\mathfrak A
:=
\frac{A_{tot}}{r^2}.
}
\]

Then

\[
\boxed{
\mathfrak Q_\Phi(A)
\ge
\frac{\Phi^2}{\mathfrak A}.
}
\]

Unlike arbitrary `N_eff`, `mathfrak A` measures actual occupied cross-sectional area in own-scale units.

## 5. Raw-H2 packet conversion

Assume the participating region remains in one own-scale exact CE-H coefficient bin

\[
|\kappa|\asymp r^{-2}.
\]

For a loop segment of length `~r`,

\[
E_{seg}
\gtrsim
r\int_A\rho^2dA.
\]

Then

\[
H_{seg}(t)
=
\int_{seg}|\Delta\Omega|^2dx
\asymp
r^{-4}E_{seg}
\gtrsim
r^{-3}\int_A\rho^2dA.
\]

Integrating over one own-time `~r^2` and multiplying by the normalized raw-`H2` factor `r^3`,

\[
\boxed{
h_{seg}^{norm}
\gtrsim
r^2\int_A\rho^2dA
=
\mathfrak Q_\Phi(A).
}
\]

Hence

\[
\boxed{
h_{seg}^{norm}
\gtrsim
\frac{\Phi^2}{\mathfrak A}.
}
\]

This is the partition-safe replacement for the M17-433 `Phi^2/N_eff` lower bound.

## 6. Relation to M17-433

If a geometrically canonical partition has components satisfying

\[
A_i\le C_Ar^2,
\]

then

\[
\sum_i\frac{\phi_i^2}{A_i}
\ge
\frac1{C_Ar^2}
\sum_i\phi_i^2.
\]

Thus

\[
\mathfrak Q_\Phi
\ge
c\sum_i\phi_i^2
=
c\frac{\Phi^2}{N_{eff}}.
\]

Therefore M17-433 remains a legitimate **corollary for a fixed canonical own-scale partition**.

But the canonical primary descriptor is `mathfrak Q_Phi` or, more weakly, the actual geometric area factor `mathfrak A`, not arbitrary `N_eff`.

## 7. Corrected loop record currency

With the M17-413 parent-length spatial factor `~R` and good-time factor `alpha R^2`, one obtains

\[
H_R^{norm}
\gtrsim
c\alpha R^3\mathfrak Q_\Phi.
\]

After M17-405 ancestry,

\[
\boxed{
R^{-3}H_R^{norm}
\gtrsim
c\alpha\mathfrak Q_\Phi.
}
\]

Using only total flux and total cross-sectional area,

\[
\boxed{
R^{-3}H_R^{norm}
\gtrsim
c\alpha\frac{\Phi^2}{\mathfrak A}.
}
\]

The corresponding partition-safe closure criterion is

\[
\boxed{
\sum_m\alpha_m\mathfrak Q_{\Phi,m}
=\infty,
}
\]

or sufficiently,

\[
\boxed{
\sum_m
\alpha_m
\frac{\Phi_m^2}{\mathfrak A_m}
=\infty.
}
\]

## 8. What true quadratic dilution means

A fixed positive total flux can weaken the raw-`H2` lower bound only through an actual physical mechanism such as:

1. cross-sectional occupied area growing in own-scale units;
2. flux being dispersed across geometrically independent components whose total area grows;
3. coefficient-scale coherence or the common transverse cross-section failing;
4. amplitude/flux leaving the retained component;
5. chart/topology/genealogy loss.

Pure relabeling or arbitrary subdivision is not an escape.

Therefore the old phrase

\[
G_{quadratic\ flux\ dilution}\;(N_{eff}\to\infty)
\]

should be read canonically as

\[
\boxed{G_{cross\text{-}sectional\ area/geometric\ participation\ decompactification}}
\]

unless `N_eff` is tied to a fixed geometrically canonical own-scale partition.

## 9. Ambient capacity

Inside a bounded parent three-dimensional region, a parent-length collection of disjoint tube components has total cross-sectional area at most parent order under the retained volume/length geometry.

Thus

\[
A_{tot}\lesssim O(1)
\]

and

\[
\boxed{
\mathfrak A
\lesssim
Cr^{-2}
=CR^2.
}
\]

This is the maximal two-dimensional transverse area participation scale.

It is large enough that area dilution alone can still be summable across geometric records, so M17-439 is a representation correction, not a contradiction theorem.

## 10. Updated late-loop split

The quadratic fragmented-loop branch becomes

\[
\boxed{
\begin{aligned}
H_{positive\ flux\ loop\ family}
\Longrightarrow{}&
H_{\sum\alpha_m\mathfrak Q_{\Phi,m}=\infty}
\Rightarrow\text{contradiction}\\
&\lor G_{positive\ flux\ thinning}\\
&\lor G_{cross\text{-}sectional\ area/geometry\ dispersion}\\
&\lor G_{good\text{-}time\ occupation\ thinning}\\
&\lor G_{coefficient\ scale/tube/chart/genealogy\ loss}.
\end{aligned}
}
\]

Arbitrary label fragmentation is removed from the list of physical escapes.

## 11. DSD role

This is a representation audit in the strict sense: a bookkeeping partition was separated from an invariant physical quadratic payer.

The mathematics is Cauchy--Schwarz, weighted partition refinement, exact CE-H scaling, and the M17-413 packet conversion.

## 12. Audit verdict

**PASS as a correction/refinement of M17-433.**

`N_eff` is not a canonical invariant unless the partition is geometrically fixed. The canonical quadratic currency is area-weighted cross-sectional enstrophy, and true dilution requires actual geometric transverse-area dispersion or another retained-hypothesis loss.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
