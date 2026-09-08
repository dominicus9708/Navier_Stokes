# DSD M17-386 — Exact spacetime `kappa`-scale allocation and `r^3`-weighted temporal Carleson packing close single-genealogy raw-`H2` double counting but not concurrent spatial multiplicity

Date: 2026-09-08  
Canonical ID: **M17-386**

Status: **ACTIVE SPACETIME ALLOCATION THEOREM / SINGLE-GENEALOGY CARLESON PACKING / SPATIAL-MULTIPLICITY AUDIT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Inputs from M17-381 and M17-385

On exact CE-H,

\[
\Delta\Omega=\kappa\Omega,
\qquad
|\Delta\Omega|^2=\kappa^2|\Omega|^2.
\]

M17-381 assigns every nonzero raw-`H2` point to a unique dyadic intrinsic coefficient scale

\[
r_m\sim|\kappa|^{-1/2}
\]

and, at each fixed time,

\[
\boxed{\sum_m H_m(t)=H(t)},
\]

where

\[
H_m(t):=
\int_{\mathcal A_m(t)}|\Delta\Omega(x,t)|^2dx,
\qquad
H(t):=\int|\Delta\Omega(x,t)|^2dx.
\]

M17-385 shows that an order-one material deformation on an interval `I` costs global raw-`H2` spacetime charge through

\[
K_I
\lesssim
E_*^{1/8}|I|^{5/8}
\left(\int_I H(t)dt\right)^{3/8},
\]

with

\[
E_*:=\sup_{t\in I}\|\Omega(t)\|_2^2.
\]

The present module asks exactly how much of the old temporal/cross-scale double-counting debt is already removable from these two facts alone.

## 2. Snapshot allocation extends exactly to spacetime

Define the nonnegative spacetime measure

\[
d\mu(x,t):=|\Delta\Omega(x,t)|^2dxdt.
\]

For the dyadic coefficient bins of M17-381 define

\[
d\mu_m
:=
\mathbf 1_{\mathcal A_m(t)}(x)
|\Delta\Omega(x,t)|^2dxdt.
\]

At every regular spacetime point with nonzero raw-`H2` density exactly one coefficient color/scale owns that density, up to the fixed finite coloring convention.

Hence Tonelli's theorem gives, for every time interval `I`,

\[
\boxed{
\sum_m\mu_m(\mathbb R^3\times I)
=
\mu(\mathbb R^3\times I).
}
\]

Equivalently,

\[
\boxed{
\sum_m\int_I H_m(t)dt
=
\int_IH(t)dt.
}
\]

Thus **raw-`H2` spacetime ownership by intrinsic coefficient scale is exact**.

The former concern that the same raw derivative density might belong to many nested coefficient scales does not survive time integration.

## 3. Spatial cube refinement also extends to spacetime

Let `Q` range over the disjoint own-scale cubes used in M17-381 and define

\[
H_{m,Q}(t)
:=
\int_{Q\cap\mathcal A_m(t)}|\Delta\Omega|^2dx.
\]

Then

\[
\boxed{
\sum_{m,Q}\int_IH_{m,Q}(t)dt
=
\int_IH(t)dt.
}
\]

Therefore both coefficient scale and restricted-measure spatial ownership are already nonduplicating in spacetime.

What is not yet proved is that a **dynamic deformation event** attached to one cell `(m,Q)` must be paid by that same local quantity `H_{m,Q}`.

That distinction is essential below.

## 4. Critical parabolic raw-H2 charge

Under the three-dimensional Navier--Stokes parabolic scaling

\[
\Omega_\lambda(x,t)
=
\lambda^2\Omega(\lambda x,\lambda^2t),
\]

one has

\[
\int|\Delta\Omega_\lambda|^2dxdt
=
\lambda^3
\int|\Delta\Omega|^2dxdt.
\]

Therefore the scale-invariant raw-`H2` spacetime charge attached to a parabolic scale `r` is

\[
\boxed{
\mathcal P_r(I)
:=
r^3\int_IH(t)dt.
}
\]

This is the correct weight for testing nested scale-time double counting.

## 5. M17-385 becomes a fixed critical payment under normalized enstrophy control

Assume an own-scale interval satisfies

\[
|I_r|\asymp c_t r^2
\]

with viscosity absorbed into `c_t` for notational simplicity.

Suppose

\[
K_{I_r}\ge K_*>0.
\]

M17-385 gives

\[
\int_{I_r}H(t)dt
\gtrsim
K_*^{8/3}
E_*^{-1/3}
r^{-10/3}.
\]

Multiplying by `r^3`,

\[
\boxed{
\mathcal P_r(I_r)
\gtrsim
K_*^{8/3}
(rE_*)^{-1/3}.
}
\]

Hence on a scale-critical enstrophy-compact branch

\[
\boxed{rE_*\le M_E<\infty}
\]

every order-one own-scale deformation episode has a fixed positive critical raw-`H2` cost

\[
\boxed{
\mathcal P_r(I_r)
\ge c(K_*,M_E)>0.
}
\]

This statement is scale invariant.

## 6. Temporal Carleson packing along one genealogy

Fix one material/genealogical chain contained in a parent time interval `I_R^*`.

Let its active dyadic scales be

\[
r_m=2^{-m}R.
\]

At scale `r_m`, let

\[
\{I_{m,j}\}_j
\]

be own-scale time intervals with bounded same-scale overlap

\[
\sum_j\mathbf 1_{I_{m,j}}(t)
\le N_0.
\]

Such a family may be obtained from an arbitrary interval family by the standard one-dimensional Vitali selection/finite coloring, with only fixed enlargement constants.

Then

\[
\begin{aligned}
\sum_{m,j}
 r_m^3\int_{I_{m,j}}H(t)dt
&=
\int H(t)
\left(
\sum_{m,j}r_m^3\mathbf 1_{I_{m,j}}(t)
\right)dt\\
&\le
N_0
\left(
\sum_mr_m^3
\right)
\int_{I_R^*}H(t)dt.
\end{aligned}
\]

Since

\[
\sum_{m=0}^\infty r_m^3
=
R^3\sum_{m=0}^\infty2^{-3m}
=
\frac{R^3}{1-2^{-3}},
\]

we obtain

\[
\boxed{
\sum_{m,j}
 r_m^3\int_{I_{m,j}}H(t)dt
\le
C N_0
R^3
\int_{I_R^*}H(t)dt.
}
\]

This is the desired **single-genealogy temporal Carleson packing inequality**.

The `r^3` critical weight is precisely what makes infinitely many nested dyadic time scales summable.

## 7. Counting order-one deformation episodes

Assume additionally

\[
r_mE_{m,j,*}\le M_E
\]

for every retained episode and

\[
K_{I_{m,j}}\ge K_*.
\]

Section 5 gives

\[
r_m^3\int_{I_{m,j}}Hdt
\ge c_*:=c(K_*,M_E)>0.
\]

Therefore Section 6 implies

\[
\boxed{
N_{dist}\,c_*
\le
C N_0
R^3\int_{I_R^*}H(t)dt.
}
\]

Consequently, if the parent critical raw-`H2` charge

\[
R^3\int_{I_R^*}Hdt
\]

is finite, one genealogical chain cannot contain infinitely many distinct order-one own-scale deformation episodes satisfying the stated compactness hypotheses.

This is a genuine non-double-counting theorem.

## 8. Why this is not yet a full packet-forest Carleson theorem

The preceding argument counts **time intervals along one genealogy**.

Suppose instead that at one scale and one time there are many spatially disjoint own-scale cells

\[
Q_1,Q_2,\dots,Q_N.
\]

M17-381 gives the exact local allocation

\[
\sum_i H_{m,Q_i}(t)
\le H_m(t),
\]

but M17-385 does not prove

\[
K_{m,Q_i}
\lesssim
E_{m,Q_i}^{1/8}
\left(
\int H_{m,Q_i}
\right)^{3/8}.
\]

Its strain payer is the global/nonlocal quantity

\[
\|\Sigma\|_\infty.
\]

A single coherent large-scale strain field may deform many child cells simultaneously.

Therefore charging the same global `H(t)` independently to every concurrent cell would recreate an artificial **spatial multiplicity**.

The exact spacetime raw-`H2` ownership theorem does not by itself localize the nonlocal strain payer to the same coefficient cell.

## 9. Exact surviving split

The old phrase

\[
G_{spacetime/cross\text{-}generation\ raw\text{-}H2\ allocation}
\]

can now be sharpened.

On exact CE-H,

\[
\boxed{
\begin{aligned}
G_{dynamic\ allocation}
\Longrightarrow{}&
H_{exact\ spacetime\ coefficient\text{-}scale\ ownership}\\
&\land H_{single\text{-}genealogy\ temporal\ Carleson\ packing}\\
&\land
\Big(
G_{concurrent\ spatial\ payer\ localization}\\
&\qquad\lor
G_{parent\ critical\ raw\text{-}H2\ charge\ divergence}\\
&\qquad\lor
G_{normalized\ enstrophy\ decompactification}\\
&\qquad\lor
G_{genealogy/interface/domain\ loss}
\Big).
\end{aligned}
}
\]

Thus the raw measure itself is no longer the ambiguous object.

The remaining hard issue is to localize or quotient the **nonlocal deformation payer** across simultaneously active spatial cells, together with obtaining a certified parent critical raw-`H2` control.

## 10. Cross-generation scaling audit

The quantity

\[
r^3\int_{I_r}\|\Delta\Omega\|_2^2dt
\]

is parabolically scale invariant.

Hence the temporal packing theorem does not create the old M17-307 inverse-record-scale discount by itself.

However, no certified uniform bound of the form

\[
\sup_{P_R}
R^3
\int_{P_R}|\Delta\Omega|^2dxdt
<\infty
\]

is presently available from the standard finite-energy Navier--Stokes estimates.

Therefore scale invariance of the charge is useful for bookkeeping but is not a regularity contradiction.

## 11. DSD audit role

The DSD role is a representation and ownership audit:

- extend the exact coefficient-scale owner from snapshots to spacetime before inventing a new temporal allocation variable;
- use the scale-invariant `r^3` weight when summing nested parabolic episodes;
- do not charge one global nonlocal strain event once for every spatial child cell;
- distinguish raw-measure ownership from dynamic-payer localization.

All canonical inequalities above are standard Tonelli/Fubini, parabolic scaling, geometric-series, Vitali-overlap, and M17-385 estimates.

## 12. Audit verdict

**PASS — substantial temporal allocation advance with one precise remaining spatial obstruction.**

The exact new facts are

\[
\boxed{
\sum_m\int_IH_mdt
=
\int_IHdt
}
\]

and, along one bounded-overlap genealogy,

\[
\boxed{
\sum_{m,j}r_m^3\int_{I_{m,j}}Hdt
\lesssim
R^3\int_{I_R^*}Hdt.
}
\]

The next highest-value task is to split the nonlocal strain into near-field and far-field contributions on a persistent own-scale CE-H cell and determine whether concurrent spatial deformation can be charged locally, or whether the far field is only a coherent parent-scale deformation/enstrophy exit.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
