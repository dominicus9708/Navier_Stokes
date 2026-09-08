# DSD M17-392 — Own-scale flux turnover has an `R`-weighted standard-energy variation ledger and logarithmic evacuation does not amplify the direct energy cost

Date: 2026-09-08  
Canonical ID: **M17-392**

Status: **ACTIVE FLUX-TURNOVER PHYSICALIZATION / STANDARD-ENERGY VARIATION LEDGER / LOG-EXPOSURE FIREWALL**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input

M17-389 gives the physical material-flux law on exact CE-H,

\[
\boxed{
\frac d{dt}\log\Phi
=\nu\bar\kappa_\Phi,
}
\]

where `bar kappa_Phi` is the flux-weighted coefficient on the retained material tube/family.

M17-391 gives the physical own-scale tube enstrophy bound

\[
\boxed{
E_T(t)
\gtrsim
\frac{\Phi(t)^2}{R}
}
\]

under scale-`R` tube geometry

\[
\ell\gtrsim R,
\qquad
A\lesssim R^2.
\]

The present module combines these two identities to charge **flux turnover itself** to the ordinary energy-dissipation ledger.

## 2. Own-scale coefficient ceiling

Assume on one retained scale-`R` episode

\[
\boxed{
|\bar\kappa_\Phi(t)|
\le
K_\kappa R^{-2}
}
\]

with fixed `K_kappa`.

If this fails, retain instead the typed exit

\[
G_{coefficient\ supercritical\ spike}.
\]

Let

\[
Q(t):=\Phi(t)^2.
\]

The physical flux law gives

\[
\frac{dQ}{dt}
=2\nu\bar\kappa_\Phi Q.
\]

Therefore

\[
\boxed{
|\dot Q|
\le
2\nu K_\kappa R^{-2}Q.
}
\]

## 3. Flux-square variation requires weighted time occupancy

Whenever `Q>0`, Section 2 implies

\[
Q\,dt
\ge
\frac{R^2}{2\nu K_\kappa}|dQ|.
\]

Integrating over an interval `I_R`,

\[
\boxed{
\int_{I_R}Q(t)dt
\ge
\frac{R^2}{2\nu K_\kappa}
\operatorname{Var}_{I_R}(Q),
}
\]

where

\[
\operatorname{Var}_{I_R}(Q)
:=
\int_{I_R}|dQ|
\]

is the total variation of the squared material flux.

This formula counts both evacuation and recovery.

No crossing-number interpretation is required.

## 4. Convert flux variation to standard energy

M17-391 gives on the same persistent tube geometry

\[
E_T(t)
\ge
c_T\frac{Q(t)}{R}.
\]

Hence

\[
\nu\int_{I_R}E_T(t)dt
\ge
c_T\frac{\nu}{R}
\int_{I_R}Q(t)dt.
\]

Insert Section 3:

\[
\boxed{
\nu\int_{I_R}E_T(t)dt
\ge
\frac{c_T}{2K_\kappa}
R\,
\operatorname{Var}_{I_R}(\Phi^2).
}
\]

Thus the exact structural cost of own-scale flux turnover is

\[
\boxed{
R\operatorname{Var}(\Phi^2).
}
\]

This is a certified first-generation standard-energy currency.

## 5. Bounded-overlap turnover ledger

Let `j` index physical own-scale tube episodes with bounded temporal/spatial multiplicity and the same uniform geometry/coefficient constants.

Summing Section 4 and using the finite-energy inequality gives

\[
\boxed{
\sum_j
R_j
\operatorname{Var}_{I_j}(\Phi_j^2)
<\infty.
}
\]

This is the main M17-392 turnover ledger.

It physicalizes the `unbounded coefficient/flux turnover` branch whenever the turnover remains inside a scale-comparable coefficient ceiling and persistent tube geometry.

## 6. Monotone evacuation from fixed flux is only an `O(R)` direct energy cost

Suppose on one scale-`R` episode the flux decreases monotonically from

\[
\Phi_{in}>0
\]

to

\[
0\le\Phi_{out}<\Phi_{in}.
\]

Then

\[
\operatorname{Var}(\Phi^2)
=
\Phi_{in}^2-\Phi_{out}^2.
\]

Therefore

\[
\boxed{
\nu\int_{I_R}E_Tdt
\gtrsim
R
\left(
\Phi_{in}^2-\Phi_{out}^2
\right).
}
\]

In particular, evacuation from fixed positive flux all the way to an arbitrarily tiny final flux has only the mandatory lower cost

\[
\boxed{\sim R\Phi_{in}^2.}
\]

The large logarithm in

\[
\int\kappa_-dt
\sim
\log\frac{\Phi_{in}}{\Phi_{out}}
\]

does **not** turn into a logarithmically amplified direct energy lower bound.

This is the precise energy version of the M17-389 strain-cancellation firewall.

## 7. Why the logarithm disappears

The reason is simple and exact.

As the flux decreases, the tube enstrophy lower bound

\[
E_T\gtrsim\Phi^2/R
\]

decreases quadratically with the remaining flux.

The later part of a very deep logarithmic evacuation can therefore last many coefficient-exposure units while carrying very little direct flux-enstrophy mass.

The flux ODE and the tube-energy estimate combine to telescope in `Phi^2`, not in `log Phi`.

Thus

\[
\boxed{
\text{logarithmic coefficient exposure}
\not\Rightarrow
\text{logarithmic standard-energy cost}.
}
\]

## 8. Repeated evacuation/recovery cycles

Suppose one scale-`R` episode contains `N_R` full flux cycles between two fixed levels

\[
0<\Phi_-<\Phi_+.
\]

Each full down-and-up cycle contributes at least

\[
2(\Phi_+^2-\Phi_-^2)
\]

to the total variation of `Phi^2`.

Hence

\[
\operatorname{Var}_{I_R}(\Phi^2)
\ge
2N_R(\Phi_+^2-\Phi_-^2).
\]

Section 4 gives

\[
\boxed{
\nu\int_{I_R}E_Tdt
\gtrsim
R N_R
(\Phi_+^2-\Phi_-^2).
}
\]

Across geometric scales,

\[
\boxed{
\sum_jR_jN_j
(\Phi_{+,j}^2-\Phi_{-,j}^2)
<\infty.
}
\]

For fixed order-one flux swing, the power-law turnover threshold is therefore

\[
\boxed{
N_j\sim R_j^{-1}
}

for non-summability on geometric scales.

Thus mere `N_j -> infinity` is not enough.

The rate matters.

## 9. Relation to M17-379

M17-379 gives

\[
\sum_m\tau_m^{own}
\gtrsim
\log\frac1r
\]

for strict-subscale flux evacuation, with the alternative of long true own-scale residence or a logarithmic multi-scale cascade.

M17-392 shows that this logarithmic own-time/exposure requirement does not by itself force an energy contradiction.

If the flux is predominantly monotone downward, the direct standard-energy payment telescopes to the finite flux-square drop.

If the branch instead repeatedly restores order-one flux and evacuates it again, then the appropriate energy variable is no longer exposure time but

\[
\boxed{
\operatorname{Var}(\Phi^2).
}
\]

This is the correct quantity to compare with turnover count.

## 10. Cross-scale monotone cascade firewall

Consider a monotone evacuation distributed across many decreasing physical scales `R_m`, with flux-square drops

\[
\Delta Q_m
:=
Q_{m,in}-Q_{m,out}
\ge0.
\]

The M17-392 mandatory energy expression is

\[
\sum_mR_m\Delta Q_m.
\]

Since

\[
\sum_m\Delta Q_m
\le Q_{initial}
\]

for a purely monotone total evacuation and

\[
R_m\le R_0,
\]

we have

\[
\boxed{
\sum_mR_m\Delta Q_m
\le
R_0Q_{initial}<\infty.
}
\]

Therefore arbitrarily many monotone scale stages cannot make the **known mandatory flux-energy lower bound** diverge.

A contradiction requires repeated recovery/variation, supercritical flux growth, multiplicity growth, or another payer.

## 11. Combined late-CE-H standard-energy firewall

M17-388, M17-391, and M17-392 now give, on a bounded-overlap persistent physical own-scale genealogy,

\[
\boxed{
\sum_jR_j
\left[
K_j^2
+\Phi_j^2
+\operatorname{Var}_{I_j}(\Phi_j^2)
\right]
<\infty
}
\]

up to fixed geometry/coefficient constants and with the obvious convention that `Phi_j^2` denotes a retained flux floor when Section 391 is invoked.

The three currencies correspond to

1. material deformation;
2. persistent retained flux;
3. flux turnover/variation.

All are paid by the ordinary finite-energy dissipation ledger.

## 12. Remaining turnover exits

The variation theorem does not cover a turnover event if one of the following occurs:

- `|kappa| R^2 -> infinity` — coefficient-supercritical spike;
- tube cross-sectional area or length loses own-scale comparability;
- the material tube/family identity is lost;
- flux labels enter or leave through nodal/interface/rank/domain events;
- the relevant scale changes too rapidly to assign one persistent physical own-scale episode.

These remain explicit branches rather than being counted as free turnover.

## 13. DSD audit role

The DSD role is to choose the correct conserved/transported currency.

Counting sign crossings or logarithmic exposure alone obscures the direct physical cost.

The flux law shows that the natural turnover variable for energy accounting is

\[
\Phi^2
\]

and its total variation.

The canonical result uses only the physical flux ODE, a coefficient ceiling, Cauchy--Schwarz tube enstrophy, and the standard energy inequality.

## 14. Audit verdict

**PASS — unbounded turnover is quantitatively physicalized.**

On the compact own-scale branch,

\[
\boxed{
\sum_jR_j\operatorname{Var}(\Phi_j^2)<\infty.
}
\]

Therefore repeated order-one flux turnover can contradict finite energy only if its count grows at a non-summable rate, with `R^{-1}` the natural geometric power threshold for fixed flux swings.

The next target is the coefficient-supercritical / interface / rapid-scale-migration side, because ordinary logarithmic exposure and ordinary turnover are now both below or inside certified standard-energy ledgers.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
