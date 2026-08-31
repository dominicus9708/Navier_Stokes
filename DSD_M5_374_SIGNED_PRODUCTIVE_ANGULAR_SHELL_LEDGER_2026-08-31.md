# DSD M5-374 — Signed productive angular shells and the disjoint-shell enstrophy tax

Date: 2026-08-31

Status: **THE ABSOLUTE ANGULAR SOURCE LEDGER OF M5-362 IS REFINED TO SIGNED PRODUCTIVE SHELL CONTRIBUTIONS / FIRST-HITTING GROWTH FORCES A POSITIVE SUM OF SHELL ACTIONS / DYADIC SOURCE SHELLS ARE SPATIALLY DISJOINT AT EACH CENTER AND TIME, GIVING AN ADDITIVE WEIGHTED `L2` ENSTROPHY LEDGER / NATURAL-AND-LARGER PRODUCTIVE SOURCES FORCE A QUANTITATIVE STAGE DISSIPATION TAX, BUT THAT TAX SCALES LIKE THE NATURAL LENGTH AND REMAINS SUMMABLE ALONG GEOMETRIC FIRST-HITTING LEVELS / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

M5-362 proved that first-hitting vorticity growth requires a nontrivial angular Biot--Savart source, but used the absolute majorant

\[
\int \frac{|\omega(x+y)|\sin\theta(x,x+y)}{|y|^3}\,dy.
\]

M5-373 then showed that a generic linear scale sum cannot be closed merely from a quadratic frequency-energy ledger.

The present note keeps the **sign of the actual longitudinal stretching contribution** and exploits a geometric fact not available to nested-ball arguments:

\[
\boxed{\text{dyadic physical source shells about one center are pairwise disjoint.}}
\]

This yields an exact additive shell-energy estimate and identifies what it can and cannot close.

## 2. Signed dyadic shell decomposition of longitudinal stretching

At a point with nonzero vorticity, write

\[
\xi(x,t)=\frac{\omega(x,t)}{|\omega(x,t)|},
\qquad
\gamma(x,t)=\xi^T S[\omega](x,t)\xi.
\]

Using a smooth radial dyadic partition of unity on `R^3 \ {0}`, decompose the Biot--Savart strain kernel into shell kernels `K_k` supported where

\[
R_k\lesssim |y|\lesssim 2R_k,
\qquad R_k=2^kR_0.
\]

Define

\[
S_k[\omega](x,t)
:=\int K_k(y)\omega(x+y,t)\,dy,
\]

and the **signed shell stretching contribution**

\[
\boxed{
\gamma_k(x,t)
:=\xi(x,t)^T S_k[\omega](x,t)\xi(x,t).
}
\]

In the principal-value/distributional sense,

\[
\boxed{
\gamma(x,t)=\sum_k\gamma_k(x,t).
}
\]

Define the productive part

\[
\boxed{
\gamma_k^{\rm prod}(x,t):=[\gamma_k(x,t)]_+.
}
\]

This is stricter than the absolute angular source used in M5-362: only shell contributions with the correct sign for longitudinal amplification are retained.

## 3. Productive shell action forced by a first-hitting stage

Let

\[
W(t)=\|\omega(t)\|_\infty
\]

and let

\[
W(t_{j+1})=qW(t_j),
\qquad q>1.
\]

M5-340 proved

\[
\int_{t_j}^{t_{j+1}}\|\gamma^+(t)\|_\infty dt\ge\log q.
\]

Since

\[
\left[\sum_k\gamma_k\right]_+
\le
\sum_k[\gamma_k]_+,
\]

we obtain pointwise

\[
\|\gamma^+(t)\|_\infty
\le
\sum_k\|\gamma_k^{\rm prod}(t)\|_\infty.
\]

Therefore, defining

\[
\boxed{
\mathfrak A_{j,k}^{\rm prod}
:=
\int_{t_j}^{t_{j+1}}
\|\gamma_k^{\rm prod}(t)\|_\infty dt,
}
\]

one has

\[
\boxed{
\sum_k\mathfrak A_{j,k}^{\rm prod}
\ge
\log q.
}
\]

This is the desired signed productive-event ledger.

It requires no measurable choice of a maximizing trajectory.

## 4. One-shell `L2` source estimate

For a shell at physical radius `R`, the angular kernel has magnitude bounded by

\[
C|y|^{-3}.
\]

Hence for every center `x`,

\[
|\gamma_R(x,t)|
\le
C\int_{R\lesssim|y|\lesssim2R}
\frac{|\omega(x+y,t)|}{|y|^3}dy.
\]

Cauchy--Schwarz gives

\[
|\gamma_R(x,t)|
\le
C
\left(
\int_{A_R(x)}|\omega(z,t)|^2dz
\right)^{1/2}
\left(
\int_{A_R}|y|^{-6}dy
\right)^{1/2}.
\]

Since

\[
\int_{A_R}|y|^{-6}dy\asymp R^{-3},
\]

we obtain

\[
\boxed{
R^3|\gamma_R(x,t)|^2
\lesssim
\int_{A_R(x)}|\omega(z,t)|^2dz.
}
\]

The same holds with `gamma_R` replaced by its positive productive part.

## 5. Disjoint-shell square ledger

For a fixed center `x` and time `t`, the dyadic shells

\[
A_{R_k}(x)
\]

are pairwise disjoint up to uniformly bounded overlap from the smooth partition.

Therefore

\[
\boxed{
\sum_k
R_k^3
|\gamma_k^{\rm prod}(x,t)|^2
\lesssim
\|\omega(t)\|_2^2.
}
\]

This is a genuine additive shell-energy statement.

It does **not** have the nested-ball double-counting defect identified in M5-372.

This is the principal new quantitative result of the checkpoint.

## 6. Natural-and-larger scales admit an `ell1` bound

Fix a minimum retained source radius `R_*` and sum only shells with

\[
R_k\ge R_*.
\]

Weighted Cauchy--Schwarz gives

\[
\begin{aligned}
\sum_{R_k\ge R_*}\gamma_k^{\rm prod}(x,t)
&\le
\left(
\sum_{R_k\ge R_*}R_k^3|\gamma_k^{\rm prod}(x,t)|^2
\right)^{1/2}
\left(
\sum_{R_k\ge R_*}R_k^{-3}
\right)^{1/2}\\
&\lesssim
R_*^{-3/2}\|\omega(t)\|_2.
\end{aligned}
\]

Thus

\[
\boxed{
\sum_{R_k\ge R_*}
\|\gamma_k^{\rm prod}(t)\|_\infty
\lesssim
R_*^{-3/2}\|\omega(t)\|_2.
}
\]

This avoids the bare `ell2 -> ell1` obstruction of M5-373 because the Biot--Savart shell geometry supplies the positive weight `R_k^3`.

The cost is that the estimate degenerates as `R_* -> 0`.

That degeneracy is exactly the sub-natural/high-derivative route already separated in M5-362 and M5-372.

## 7. First-hitting stage tax on the non-sub-natural branch

Assume the productive contribution needed for a given first-hitting stage is carried, up to a fixed fraction, by source radii

\[
R_k\ge c_0r_j,
\]

where

\[
r_j=\sqrt{\frac{\nu}{W(t_j)}}
\]

is the physical viscous-vorticity scale and `c0>0` is fixed.

Then Sections 3 and 6 imply

\[
\log q
\lesssim
r_j^{-3/2}
\int_{I_j}\|\omega(t)\|_2dt
\]

up to the retained source fraction and universal constants.

By Cauchy--Schwarz in time,

\[
(\log q)^2
\lesssim
r_j^{-3}|I_j|
\int_{I_j}\|\omega(t)\|_2^2dt.
\]

Define the normalized stage duration

\[
\boxed{
\Theta_j
:=
W(t_j)|I_j|
=
\frac{\nu|I_j|}{r_j^2}.
}
\]

Then

\[
|I_j|=\frac{\Theta_jr_j^2}{\nu},
\]

so

\[
\boxed{
\nu\int_{I_j}\|\omega(t)\|_2^2dt
\gtrsim
\frac{\nu^2r_j}{\Theta_j}(\log q)^2.
}
\]

This is a finite-energy **productive angular stage tax**.

It is obtained directly from signed stretching plus disjoint physical shells.

## 8. Comparison with the Leray--Hopf budget

For whole-space divergence-free flow,

\[
\|\nabla u\|_2^2=\|\omega\|_2^2,
\]

and Leray--Hopf gives

\[
\nu\int_0^T\|\omega(t)\|_2^2dt
\le
\frac12\|u_0\|_2^2.
\]

The first-hitting intervals `I_j` are time-disjoint, so their physical dissipation taxes may be summed without temporal double counting:

\[
\boxed{
\sum_j
\frac{\nu^2r_j}{\Theta_j}
\lesssim_{q,c_0}
\|u_0\|_2^2
}
\]

on the non-sub-natural productive branch.

This is a necessary condition for a singular first-hitting cascade.

## 9. Why this still does not contradict geometric first-hitting growth

For geometric levels

\[
W_j=q^jW_0,
\]

one has

\[
r_j\asymp q^{-j/2}.
\]

If `Theta_j` stays order one, then

\[
\sum_jr_j<\infty.
\]

Therefore the lower bound

\[
\nu\int_{I_j}\|\omega\|_2^2dt
\gtrsim
\nu^2r_j
\]

is fully compatible with a finite total kinetic-energy dissipation budget.

Thus the signed shell ledger is stronger and cleaner than a nested occupancy charge, but it does not by itself close global regularity.

## 10. A conditional temporal-concentration exclusion

The stage tax does exclude sufficiently short normalized stages.

From

\[
\sum_j\frac{r_j}{\Theta_j}<\infty
\]

it follows that a singular non-sub-natural branch cannot satisfy any asymptotic regime forcing

\[
\sum_j\frac{r_j}{\Theta_j}=\infty.
\]

Equivalently, productive first-hitting acceleration cannot make `Theta_j` too small too often without exhausting the Leray dissipation ledger.

This is a genuine restriction on the temporal-concentration escape, though not a full exclusion because many admissible sequences still make the series convergent.

## 11. DSD analysis interpretation

The productive source descriptor should now retain

\[
\boxed{
(\text{sign},\text{shell radius},\text{action},\text{source enstrophy},\text{stage duration}).
}
\]

This separates three statements that had previously been easy to conflate:

1. a shell contains misaligned vorticity;
2. that shell contributes with the correct sign to longitudinal stretching;
3. the contribution occupies enough spacetime action to amplify a first-hitting record.

Only the third is a productive event in the present sense.

## 12. Axis-property interpretation

The relative vorticity-axis geometry enters through the signed determinant factor in the Biot--Savart representation.

Therefore `sin(theta)` is only a magnitude envelope.

The productive object is not

\[
|\omega|\sin\theta,
\]

but the signed projection

\[
D(\hat y,\xi(x+y),\xi(x))|\omega(x+y)|.
\]

This sharpens the axis-property ledger by separating harmless geometric misalignment from alignment that actually produces extensional longitudinal strain.

## 13. Audit firewall

The new square ledger must not be misread as a proof that every active scale pays an independent fixed energy amount.

The exact bound is

\[
\sum_kR_k^3|\gamma_k^{\rm prod}|^2
\lesssim\|\omega\|_2^2.
\]

A fixed linear action may still be distributed among infinitely many shells with amplitudes adapted to the weight `R_k^3`.

Therefore the number of active shells is not automatically bounded by the energy budget.

That optimization is the next audit target.

## 14. Updated proof-tree consequence

On the productive-angular branch,

\[
\boxed{
\text{first-hitting growth}
\Longrightarrow
\begin{cases}
\text{sub-natural productive source} \to H_{\rm der/occ},\\
\text{natural/remote productive source} \to \text{signed shell enstrophy tax},\\
\text{core/window loss} \to T.
\end{cases}
}
\]

The generic unsigned Dini label is no longer needed here.

The main remaining question is whether **multiscale signed shell action** forces more than the summable `~ r_j` stage tax.

## 15. Audit verdict

### PROVED / STANDARD ESTIMATES

- signed dyadic shell decomposition of longitudinal strain;
- positive first-hitting stretching action forces a positive sum of productive shell actions;
- one-shell estimate `R^3 gamma_R^2 <= C int_shell |omega|^2`;
- disjoint-shell weighted square ledger;
- natural-and-larger shell `ell1` bound from weighted Cauchy--Schwarz;
- non-sub-natural first-hitting dissipation tax `nu int_I ||omega||_2^2 >= c nu^2 r_j / Theta_j`.

### NEW RESTRICTION

- a singular productive-angular cascade must satisfy the finite series condition `sum r_j/Theta_j < infinity` on the non-sub-natural branch.

### NOT DERIVED

- a fixed energy cost per active shell;
- a growing cost proportional to the number of productive scales;
- exclusion of scale-spread shell amplitudes optimized against the `R^3` weight;
- exclusion of sub-natural derivative occupancy;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
