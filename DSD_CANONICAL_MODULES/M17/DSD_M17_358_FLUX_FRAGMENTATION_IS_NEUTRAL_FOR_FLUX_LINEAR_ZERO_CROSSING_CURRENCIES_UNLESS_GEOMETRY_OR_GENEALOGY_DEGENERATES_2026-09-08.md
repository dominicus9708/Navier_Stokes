# DSD M17-358 — Flux fragmentation is neutral for flux-linear zero-crossing currencies unless geometry or genealogy degenerates

Date: 2026-09-08  
Canonical ID: **M17-358**

Status: **ACTIVE FRAGMENTATION AUDIT / M17-356--357 REFINEMENT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Fragmented flux partition

Let a retained regular material-flux family be partitioned into disjoint tube-label bands

\[
\Lambda=\bigsqcup_i\Lambda_i.
\]

Write their oriented fluxes as

\[
\phi_i:=\int_{\Lambda_i}d\Phi>0,
\]

with total retained positive flux

\[
\Phi_{tot}:=\sum_i\phi_i.
\]

M17-356 observed that if

\[
\Phi_{tot}\ge\Phi_*>0
\]

while

\[
\sup_i\phi_i\to0,
\]

then the number of tube bands must diverge.

The present question is whether that fragmentation can weaken the active critical zero-crossing currencies.

## 2. Pure-flux crossing currency is exactly additive

For each fragment define

\[
\mathcal C_i(I)
:=
\int_I\int_{\Lambda_i}
(D_t\kappa)_-\delta(\kappa)d\Phi dt.
\]

Because the tube-label sets are disjoint and the integrand is nonnegative,

\[
\boxed{
\mathcal C_{\Phi,-}^{0}(I)
=
\sum_i\mathcal C_i(I).
}
\]

Therefore repartitioning the same material flux into arbitrarily many smaller flux bands does not change the total downward crossing charge.

There is no factor depending on `min_i phi_i`.

## 3. Critical spatialized currency is likewise additive

In vortex-line coordinates M17-340 writes

\[
\mathcal Q_0(I)
=
\int_I\int
\mathcal L_{crit}(\lambda,t)
(D_t\kappa)_-\delta(\kappa)
\,d\Phi dt,
\]

where

\[
\mathcal L_{crit}
=
\int_{\Gamma_\lambda}
\rho|\nabla\kappa|^{-1/3}ds.
\]

Thus

\[
\boxed{
\mathcal Q_0(I)=\sum_i\mathcal Q_{0,i}(I).
}
\]

Again fragmentation by itself does not lower the aggregate charge.

## 4. Uniform compact-family lower bound survives arbitrary fragmentation

M17-345--346 show that on a compact fixed-segment material family,

\[
L_\rho\ge L_{min}>0,
\]

\[
D_{\Gamma,\kappa}\le D_{max}<\infty,
\]

and hence

\[
\mathcal L_{crit}
\ge
\ell_{min}
:=L_{min}^{7/6}D_{max}^{-1/6}>0.
\]

This estimate is **per material label/segment** and does not require a lower bound for the flux of the tube band containing that label.

Therefore, for every fragmented partition,

\[
\begin{aligned}
\mathcal Q_0(I)
&=\sum_i\mathcal Q_{0,i}(I)\\
&\ge
\ell_{min}
\sum_i\mathcal C_i(I).
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal Q_0(I)
\ge
\ell_{min}\mathcal C_{\Phi,-}^{0}(I)
}
\]

uniformly in the number and individual fluxes of the fragments.

## 5. Fragmentation is therefore not an independent escape on the uniform compact branch

Suppose

\[
\sup_i\phi_i\to0,
\qquad
N_{tube}\to\infty,
\]

but the following remain uniform:

1. retained total material crossing activity;
2. high-amplitude segment capture;
3. lower `L_rho`;
4. upper `D_{Gamma,kappa}`;
5. coherent material-label genealogy.

Then the M17-346 critical-spatial lower bound is unchanged.

Thus

\[
\boxed{
G_{flux\ fragmentation}
\not\Rightarrow
\text{loss of critical zero-crossing charge}
}
\]

on the uniform compact material family.

Fragmentation merely repartitions the measure.

## 6. What fragmentation can actually expose

For fragmentation to weaken the proof branch, at least one uniform per-label property must fail as the tube bands become finer.

The typed alternatives are

\[
\boxed{
G_{L_\rho\text{-}lower\ bound\ degeneration},
}

\[
\boxed{
G_{D_{\Gamma,\kappa}\text{-}upper\ bound\ degeneration},
}

\[
\boxed{
G_{transverse\ tube\ shape/chart\ degeneration},
}

\[
\boxed{
G_{material\ genealogy/interface\ replacement},
}

or loss of the retained total flux/current allocation itself.

The first two are already routed by M17-345--346 to segment collapse / threshold loss / coefficient-gradient decompactification.

Hence flux fragmentation is primarily an **interface/genealogy complexity indicator**, not a new currency-loss mechanism.

## 7. Signed current is also partition invariant

The M5-681 material distribution and current are linear in the material flux measure:

\[
F(k,t)=\int\delta(k-\kappa_\lambda)d\Phi,
\]

\[
G(k,t)=\int h_\lambda\delta(k-\kappa_\lambda)d\Phi.
\]

Under a disjoint flux partition,

\[
F=\sum_iF_i,
\qquad
G=\sum_iG_i.
\]

Thus the quantitative stationary statement

\[
\overline G(0)\le-d_{flux}<0
\]

is likewise unaffected by merely changing the granularity of the tube partition.

This prevents a bookkeeping fragmentation from masquerading as a dynamical escape.

## 8. DSD-theory role

The useful heuristic is to distinguish structural splitting from loss of the conserved/additive measure. The mathematical statement is ordinary countable additivity of the material-flux integrals plus the uniform per-label M17-346 estimate.

No DSD axiom is used as a PDE hypothesis.

## 9. Updated branch

Combining M17-356--358,

\[
\boxed{
\begin{aligned}
G_{winding/fragmented\ tail}
\Longrightarrow{}&
H_{same\ material\ closed\ loop}\\
&\lor G_{segment/coefficient\ geometry\ degeneration}\\
&\lor G_{tube\ chart/interface/genealogy\ turnover}\\
&\lor G_{loss\ of\ retained\ flux/current\ allocation}.
\end{aligned}
}
\]

Neither exact spatial reuse nor flux fragmentation remains an independent escape on the coherent uniform compact branch.

## 10. Next target

The most concrete surviving structural branch is now

\[
\boxed{G_{tube\ chart/interface/genealogy\ turnover}.}
\]

The next calculation should determine whether repeated replacement of activity-carrying material tube segments can occur with bounded total crossing current without producing a quantitative interface/turnover measure, or whether the replacement count itself is forced into an existing critical currency.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
