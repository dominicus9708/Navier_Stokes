# System-I H-Branch Pruning by First-Hitting Analyticity — 2026-08-20

Overall status: **BRANCH PRUNING — GLOBAL REGULARITY NOT PROVED.**

This note runs in parallel with the direct System-II closure attempt. It asks what the `H` branch can still mean at first-hitting checkpoints once the already-established order-one normalized analyticity strip is used globally on the smooth rapidly-decaying initial-data track.

## 1. First-hitting analytic checkpoint

At a first-hitting time `t_j`, let

\[
W_j=\|\omega(t_j)\|_\infty,
\qquad
r_j=W_j^{-1/2},
\]

and define the normalized vorticity

\[
\Omega_j(y)=W_j^{-1}\omega(X_j+r_jy,t_j).
\]

The first-hitting property gives a backward restart time of order `W_j^-1` on which the vorticity amplitude is bounded by `W_j`.

On the smooth rapidly-decaying track, the standard vorticity analyticity theorem therefore supplies uniform constants

\[
\rho_0>0,
\qquad
M_0<\infty
\]

such that

\[
\sup_{|\operatorname{Im}y|<\rho_0}
|\Omega_j(y)|
\le M_0
\]

for all sufficiently late first-hitting checkpoints.

Cauchy estimates imply, for every fixed integer `m >= 0`,

\[
\boxed{
\|\nabla^m\Omega_j\|_\infty
\le
C_m(M_0,\rho_0)
}
\]

uniformly in `j`.

## 2. Pointwise derivative blow-up is removed from H

Therefore an `H` branch defined by pointwise normalized derivative amplification,

\[
\|\nabla^m\Omega_j\|_\infty\to\infty
\]

for any fixed `m`, cannot occur at the first-hitting checkpoint sequence on this track.

In particular,

\[
\boxed{
H_{amp}^{(m)}
:=
\{\|\nabla^m\Omega_j\|_\infty\to\infty\}
\quad\text{is empty.}
}
\]

This does not remove derivative concentration in integral norms; it only eliminates the local-amplitude interpretation of `H`.

## 3. Fixed-radius derivative mass is uniformly bounded

For every fixed normalized radius `R`,

\[
\int_{B_R}|\nabla^m\Omega_j|^2dy
\le
|B_R|\,C_m^2.
\]

Hence

\[
\boxed{
\sup_j
\|\nabla^m\Omega_j\|_{L^2(B_R)}<\infty
\qquad\text{for each fixed }R.
}
\]

Thus an `H` event cannot be caused by unbounded derivative mass on one fixed normalized core ball either.

## 4. The only remaining H mechanism is derivative spatial non-tightness

Suppose a derivative norm such as normalized palinstrophy or higher Sobolev mass fails to remain compact along the first-hitting sequence.

Because every fixed ball has a uniform bound, failure of tightness must occur at radii escaping to infinity:

\[
\boxed{
H
\Longrightarrow
\text{derivative mass escapes to }|y|\to\infty
}
\]

on the analytic first-hitting checkpoint track.

More explicitly, if

\[
P_j=\int_{\mathbb R^3}|\nabla\Omega_j|^2dy
\]

is unbounded or non-tight, then for every fixed `R` the contribution inside `B_R` is bounded, so the excess must lie in

\[
\mathbb R^3\setminus B_R.
\]

Thus `H` is reduced from

\[
\text{local high-curvature or derivative concentration}
\]

to

\[
\boxed{
\text{spatial non-tightness of derivative mass.}
}
\]

## 5. Relation to the already-closed spatial-transport branch

The earlier material-flux analysis showed that ordinary Eulerian spatial displacement is not an independent causal mechanism at a coherent crossing. It reduces to

\[
\text{translation}
\lor
\text{viscous derivative erosion}
\lor
\text{large material deformation}.
\]

The present pruning sharpens the remaining derivative side:

- local pointwise derivative explosion at first hitting is unavailable;
- bounded-radius derivative-mass explosion is unavailable;
- only remote derivative mass can remain.

Therefore the late proof tree should distinguish

\[
\boxed{H_{remote}}
\]

from the previously broader `H` label.

## 6. Remote H still needs a global closure

This pruning does **not** prove that remote derivative mass is impossible.

A remote derivative halo can in principle carry large normalized palinstrophy over a large volume even though every derivative amplitude is uniformly bounded.

The aggregate halo estimate already gives

\[
|S_{\ge R}|^2
\lesssim
R^{-1}P_{\Omega,\ge R}.
\]

Hence a remote halo that remains dynamically relevant to the core must satisfy

\[
P_{\Omega,\ge R}\gtrsim R
\]

for arbitrarily large `R`.

The next System-I target is therefore not generic high-derivative blow-up. It is the much narrower statement:

\[
\boxed{
\text{Can a first-hitting analytic field maintain }
P_{\Omega,\ge R}\gtrsim R
\text{ at }R\to\infty
\text{ on infinitely many stages without producing }T
\text{ or violating a global budget?}
}
\]

This is a spatial packing problem rather than a local regularity problem.

## 7. Updated two-system organization

The parallel strategy is now:

### System I

\[
\boxed{
H_{remote}\lor T
}
\]

with local derivative-amplitude blow-up removed at first-hitting checkpoints.

### System II

\[
\boxed{
P_V^{recurrent}
}
\]

attacked directly by the Leray recurrence tax, compatibility self-consistency inequality, and spectral/non-normality deficits.

Status: **FIRST-HITTING ANALYTICITY REMOVES LOCAL POINTWISE AND FIXED-BALL DERIVATIVE BLOW-UP FROM THE H BRANCH. SYSTEM I IS REDUCED TO REMOTE DERIVATIVE SPATIAL NON-TIGHTNESS PLUS TURNOVER. THE REMOTE PACKING PROBLEM REMAINS OPEN.**