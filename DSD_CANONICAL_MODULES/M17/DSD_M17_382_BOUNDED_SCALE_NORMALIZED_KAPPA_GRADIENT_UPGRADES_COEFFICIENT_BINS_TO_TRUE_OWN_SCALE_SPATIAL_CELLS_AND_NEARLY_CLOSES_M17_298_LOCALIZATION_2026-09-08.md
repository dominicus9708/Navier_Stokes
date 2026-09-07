# DSD M17-382 — Bounded scale-normalized `kappa` gradient upgrades coefficient bins to true own-scale spatial cells and nearly closes M17-298 localization

Date: 2026-09-08  
Canonical ID: **M17-382**

Status: **ACTIVE SPATIAL-THICKNESS THEOREM / M17-298 LOCALIZATION ADVANCE**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-381

On exact CE-H,

\[
\Delta W=\kappa W,
\qquad
|\Delta W|^2=\kappa^2|W|^2.
\]

M17-381 partitions raw `H2` exactly by intrinsic coefficient scales

\[
r\sim|\kappa|^{-1/2}
\]

and obtains measure-level scale comparability

\[
\boxed{r^4H_r\asymp E_r.}
\]

The remaining question is whether a coefficient-scale measure set contains spatial pieces of diameter comparable to `r` rather than being arbitrarily filamentary at that scale.

## 2. Core and enlarged coefficient bins

Fix constants

\[
0<\alpha<\beta<\infty.
\]

Define a core bin

\[
\mathcal C_r
:=
\left\{
\alpha r^{-2}\le|\kappa|\le\beta r^{-2}
\right\},
\]

and an enlarged bin

\[
\widetilde{\mathcal C}_r
:=
\left\{
\frac\alpha2 r^{-2}\le|\kappa|\le2\beta r^{-2}
\right\}.
\]

The logarithmic separation between the core and enlarged boundaries is fixed independently of `r`.

## 3. Scale-normalized gradient bound gives an own-scale ball

Assume on the relevant region

\[
\boxed{
r^3|\nabla\kappa|\le G_*<\infty.}
\]

Let `x_0 in C_r`. For `|x-x_0|<=c_*r`, the mean-value estimate gives

\[
|\kappa(x)-\kappa(x_0)|
\le
G_*r^{-3}(c_*r)
=c_*G_*r^{-2}.
\]

Choose

\[
0<c_*\le
\frac{1}{G_*}
\min\left\{
\frac\alpha2,\beta
\right\}.
\]

Then the change in `|kappa|` is smaller than the fixed margin from the core bin to the enlarged bin, and hence

\[
\boxed{
B_{c_*r}(x_0)
\subset
\widetilde{\mathcal C}_r.
}
\]

Therefore every core coefficient point has a genuine spatial neighborhood of its own intrinsic scale on the normalized-gradient compact branch.

## 4. True ballwise scale comparability

On

\[
B:=B_{c_*r}(x_0)
\]

we have

\[
|\kappa|\asymp r^{-2}.
\]

Thus for every measurable subball `B' subset B`,

\[
\boxed{
\int_{B'}|\Delta W|^2dy
\asymp
r^{-4}
\int_{B'}|W|^2dy.
}
\]

Equivalently,

\[
\boxed{
r^4\frac{H(B')}{E(B')}\asymp1}
\]

whenever `E(B')>0`.

This is no longer merely a coefficient-level restricted measure identity: it holds for the **actual uncut field on an actual own-scale spatial ball**.

## 5. Finite shifted dyadic systems remove bin-boundary loss

A point whose `|kappa|` lies near the boundary of one dyadic core bin may fail to belong to its core even though it belongs to the enlarged bin.

Use a finite number of shifted dyadic partitions in the variable

\[
\log_2|\kappa|.
\]

For example, finitely many shifts of the unit dyadic lattice can be chosen so that every nonzero coefficient value lies in the core of at least one shifted bin with a fixed margin to that system's boundary.

Therefore the nonzero raw-`H2` density can be decomposed into finitely many colors such that every colored point has an own-scale ball from Section 3.

The finite coloring changes constants only and introduces no cross-scale divergence.

## 6. Spatial covering at each coefficient scale

For one color and one scale `r`, choose a maximal disjoint family of balls

\[
B_{c_*r/5}(x_i)
\]

centered on the colored core set.

The fivefold balls cover that core set, while

\[
B_{c_*r}(x_i)
\subset\widetilde{\mathcal C}_r.
\]

Thus the raw-`H2` charge at that coefficient scale is allocated to bounded-overlap actual own-scale spatial balls.

Across different scales, coefficient colors/bins have only fixed overlap in `|kappa|`, so the raw-`H2` charge still has bounded cross-scale multiplicity.

This removes the old nested-spatial-cover double-counting mechanism.

## 7. Remaining inner/mid/outer mass-retention issue

Late packet modules such as M17-251 use nested inner/mid/outer regions, not merely one ball.

On every Section-6 ball the coefficient scale is already correct. The remaining question is only whether enough `L2` mass survives from the outer ball into the chosen middle/inner ball.

Hence there is an exact dichotomy:

1. **mass retention:**
   \[
   E_{mid}\ge cE_{out},
   \]
   giving
   \[
   r^4H_{mid}/E_{out}\asymp1
   \]
   and a genuine M17-251 scale-comparable packet;
2. **mass descent/nodal concentration:** the outer mass repeatedly evacuates the own-scale core, which is exactly the strict-subscale/nodal channel already identified by M17-251/302/366.

Thus failure of inner mass retention is no longer counted as a cross-scale allocation failure.

## 8. Exact remaining M17-298 exits

Combining M17-381 and the present theorem, the CE-H cross-scale allocation branch becomes

\[
\boxed{
\begin{aligned}
G_{M17\text{-}298}
\Longrightarrow{}&
H_{true\ scale\text{-}comparable\ spatial\ packets}\\
&\lor G_{scale\text{-}normalized\ |\nabla\kappa|\ decompactification}\\
&\lor G_{strict\ subscale/nodal\ mass\ descent}\\
&\lor G_{coefficient/interface/domain\ degeneration}.
\end{aligned}
}
\]

The original **raw-`H2` cross-scale ownership/double-counting debt is therefore closed on the exact CE-H branch under bounded normalized coefficient gradient.**

## 9. Relation to M17-234/235

The new noncompact exit

\[
r^3|\nabla\kappa|\to\infty
\]

is not an unknown object. Earlier M17-234/235 already identified scale-normalized coefficient-gradient activity as a critical multiplier-gradient branch.

Therefore the failure of spatial thickness returns to an existing coefficient-gradient payer rather than opening a new arbitrary gap.

## 10. DSD-theory role

The DSD heuristic is only that a scale descriptor should be tested for spatial realization. The realization theorem itself is the mean-value inequality for a smooth coefficient plus a standard Vitali covering.

## 11. Audit verdict

**PASS — major localization advance.**

On the coefficient-gradient compact CE-H branch, dyadic coefficient-scale allocation now upgrades to actual bounded-overlap own-scale spatial balls. The remaining failures are already typed gradient, nodal descent, or interface branches.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]