# DSD M17-423 — Cross-section ribbonization requires logarithmic strain deformation but remains compatible with the weighted standard-energy ledger

Date: 2026-09-08  
Canonical ID: **M17-423**

Status: **ACTIVE SHAPE-DECOMPACTIFICATION AUDIT / LOG-STRAIN LOWER BOUND / ENERGY FIREWALL**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-422

On a retained positive-flux tube with

\[
\Phi\ge\Phi_*>0,
\qquad
|\Omega|\le M_\rho,
\]

every material cross-section satisfies

\[
A\ge A_*:=\frac{\Phi_*}{M_\rho}>0.
\]

If a doubly-critical self-clearance `d` collapses while the tube remains centered in normal coordinates, one transverse width must satisfy

\[
b\lesssim d.
\]

Area retention then forces a second transverse scale

\[
a\gtrsim\frac{A_*}{d}.
\]

Hence the cross-section aspect ratio obeys

\[
\boxed{
\chi:=\frac{a}{b}
\gtrsim
\frac{A_*}{d^2}.
}
\]

This is the ribbonization branch.

## 2. Material deformation gradient

Let `F(t,t_0)` be the material deformation gradient along the tube:

\[
\partial_tF=(\nabla u)F,
\qquad
F(t_0,t_0)=I.
\]

For any material tangent vector `v`,

\[
\frac d{dt}|Fv|^2
=2(Fv)\cdot\Sigma(Fv),
\]

where

\[
\Sigma=\frac12(\nabla u+\nabla u^T).
\]

Therefore

\[
-\|\Sigma\|_\infty
\le
\frac d{dt}\log|Fv|
\le
\|\Sigma\|_\infty.
\]

Set

\[
K_I:=\int_I\|\Sigma(t)\|_\infty dt.
\]

Then every singular value `s_i(F)` satisfies

\[
e^{-K_I}\le s_i(F)\le e^{K_I}.
\]

Consequently the condition number obeys

\[
\boxed{
\operatorname{cond}(F)
\le e^{2K_I}.
}
\]

## 3. Aspect-ratio growth requires strain

Let a material cross-section have initial aspect ratio `chi_0` and later aspect ratio `chi_1`.

Up to the fixed compact shape constants used to compare the physical patch with its principal axes,

\[
\chi_1
\lesssim
\chi_0\operatorname{cond}(F).
\]

Thus

\[
\boxed{
K_I
\ge
\frac12\log\frac{\chi_1}{C\chi_0}.
}
\]

For the M17-422 self-clearance geometry,

\[
\chi_1\gtrsim\frac{A_*}{d^2}.
\]

If `chi_0` is uniformly bounded on entry to the retained tube class,

\[
\boxed{
K_I
\gtrsim
\log\frac1d-C_*.
}
\]

Thus tube ribbonization has an unavoidable logarithmic strain-deformation cost.

## 4. Exact limitation of the lower bound

The lower bound is only logarithmic in the inverse clearance.

At a geometric own-scale sequence

\[
d_j\sim r_j\to0,
\]

we obtain only

\[
K_j\gtrsim\log\frac1{r_j}.
\]

M17-388 supplies the standard-energy deformation ledger

\[
\boxed{
\sum_j r_jK_j^2<\infty
}
\]

for bounded-overlap physical own-scale cells.

But for geometric scales `r_j ~ 2^{-j}`,

\[
\sum_jr_j\log^2\frac1{r_j}
<\infty.
\]

Therefore one-way ribbonization through geometric scales is fully compatible with the M17-388 ledger.

## 5. Record-factor form

Writing the inverse geometric record factor as

\[
r_j\sim R_j^{-1},
\]

the lower bound is

\[
K_j\gtrsim\log R_j,
\]

while the energy weight becomes schematically

\[
R_j^{-1}\log^2R_j.
\]

For geometrically growing `R_j`, this is summable.

Hence the ribbonization branch does **not** defeat a first-order inverse-scale energy discount.

## 6. No-go firewall

The inference

\[
\chi_j\to\infty
\Longrightarrow
\sum_jr_jK_j^2=\infty
\]

is false without an additional multiplicity, repeated return, or super-geometric aspect-ratio hypothesis.

The safe statement is

\[
\boxed{
G_{ribbonization}
\Longrightarrow
G_{logarithmic\ strain\ deformation}
}
\]

but

\[
\boxed{
G_{logarithmic\ strain\ deformation}
\not\Rightarrow
\text{standard-energy contradiction}
}
\]

on geometric scales.

## 7. Repeated ribbonization would be stronger

If the same material tube is forced to return repeatedly from aspect ratio `chi >> 1` to a uniformly round/shape-compact class and then ribbonize again, total variation of `log chi` accumulates.

For `N_j` full shape cycles at scale `r_j`,

\[
K_j\gtrsim N_j\log\frac1{r_j}
\]

up to fixed constants.

Then M17-388 would require

\[
\sum_j
r_jN_j^2\log^2\frac1{r_j}
<\infty.
\]

A contradiction needs `N_j` large enough to beat the geometric weight.

No such repeated shape-return theorem is currently certified.

## 8. Stronger geometric conclusion when the parent cell stays bounded

M17-422 already shows that if the entire cross-section remains inside a uniformly bounded parent cell and its centered normal-chart representation remains valid, then fixed positive area prevents `d -> 0` outright.

Thus M17-423 concerns only the explicit **decompactifying** branch where cross-section diameter/eccentricity or chart geometry is allowed to escape.

It does not reopen the retained compact loop branch closed by M17-420.

## 9. Revised geometry frontier

Combining M17-421--423:

\[
\boxed{
\begin{aligned}
G_{tubular\ reach\ loss}
\Longrightarrow{}&
G_{C^2\ curvature\ decompactification}
\\
&\lor G_{flux/amplitude\ loss}
\\
&\lor G_{normal\ chart/topology\ loss}
\\
&\lor G_{cross\text{-}section\ spatial/shape\ decompactification}.
\end{aligned}
}
\]

The last branch pays at least logarithmic strain but is not closed by the standard-energy ledger alone.

## 10. Next target

The more promising next question is whether **spatial diameter escape** of a positive-flux cross-section is compatible with the first-generation ancient spatial tightness/localization already available in the repository.

If not, shape decompactification can be returned to a spatial-escape contradiction rather than a strain-energy contradiction.

This is the target of M17-424.

## 11. DSD audit

DSD only separates shape-state escape from energetic deformation cost.

The mathematical argument is the standard material deformation-gradient estimate plus the M17-388 weighted energy ledger.

## 12. Audit verdict

**PASS-NO-GO.**

Ribbonization necessarily costs logarithmic strain, but geometric-scale logarithmic strain remains summable in the certified standard-energy ledger. A stronger return/multiplicity or spatial-tightness input is required.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
