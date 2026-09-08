# DSD M17-419 — Analytic infinite flatness of `kappa` on a regular loop forces globally harmonic vorticity and vanishes by `L2`

Date: 2026-09-08  
Canonical ID: **M17-419**

Status: **ACTIVE ANALYTIC-FLATNESS CLOSURE / GLOBAL HARMONIC CONTINUATION / MINIMAL-LOOP TERMINAL CONTRADICTION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-418

Under the retained compact minimal-loop geometry, M17-418 closes every finite record-matched transverse/mixed coefficient jet order.

Thus the only coefficient-flat survivor would have

\[
\boxed{
D^\alpha\kappa(x_*,t_*)=0
\quad\text{for every multi-index }\alpha
}
\]

at a regular loop point `x_*` with

\[
\Omega(x_*,t_*)\neq0.
\]

The present module shows that this infinite-flat analytic survivor is impossible.

## 2. Spatial analyticity

At every retained finite regular time `t_*`, the smooth Navier--Stokes velocity and vorticity are spatially real analytic.

Hence

\[
\Omega(\cdot,t_*)
\]

and

\[
\Delta\Omega(\cdot,t_*)
\]

are real analytic on all of `R^3`.

On the nonzero-vorticity neighborhood of the regular loop point, exact CE-H gives

\[
\Delta\Omega=\kappa\Omega
\]

and therefore

\[
\kappa
=
\frac{\Delta\Omega\cdot\Omega}{|\Omega|^2},
\]

so `kappa` is real analytic there as well.

## 3. Infinite flatness implies local coefficient vanishing

A real-analytic function equals its convergent Taylor series near the expansion point.

If every derivative of `kappa` vanishes at `x_*`, then its Taylor series is identically zero.

Therefore there exists a ball

\[
B_\varepsilon(x_*)
\]

contained in the regular nonzero-vorticity neighborhood such that

\[
\boxed{
\kappa(x,t_*)=0
\qquad
(x\in B_\varepsilon(x_*)).
}
\]

## 4. Exact CE-H gives local harmonic vorticity

On that open ball,

\[
\Delta\Omega
=
\kappa\Omega
=0.
\]

Thus

\[
\boxed{
\Delta\Omega(\cdot,t_*)=0
\quad\text{on a nonempty open subset of }\mathbb R^3.
}
\]

## 5. Analytic identity theorem globalizes harmonicity

Each component of

\[
\Delta\Omega(\cdot,t_*)
\]

is a real-analytic scalar function on the connected domain `R^3`.

A real-analytic function that vanishes on a nonempty open set vanishes identically on the connected domain.

Hence

\[
\boxed{
\Delta\Omega(\cdot,t_*)\equiv0
\quad\text{on }\mathbb R^3.
}
\]

This step bypasses all component-boundary regularity issues: no continuation of `kappa` through the nodal set is needed. Only the globally analytic field `Delta Omega` is continued.

## 6. Global `L2` harmonic vorticity must vanish

The retained ancient/CE-H element has finite global enstrophy,

\[
\boxed{
\Omega(\cdot,t_*)\in L^2(\mathbb R^3).
}
\]

Take the Fourier transform.

From

\[
\Delta\Omega=0
\]

we have

\[
|\xi|^2\widehat\Omega(\xi)=0
\]

in the distributional, hence `L2`, sense.

Therefore `widehat Omega` is supported at the single point `xi=0`.

An `L2` function supported on a measure-zero set is zero almost everywhere.

Thus

\[
\boxed{
\Omega(\cdot,t_*)\equiv0.
}
\]

## 7. Contradiction with the retained loop

The loop branch assumes a regular material vortex loop with positive vorticity amplitude and, in the M17-361/413 route, positive material flux.

But Section 6 gives

\[
\Omega\equiv0.
\]

Therefore the infinite-flat analytic coefficient branch is impossible.

## 8. Complete finite/infinite jet dichotomy

At a retained minimal loop state, there are only two analytic possibilities:

1. `kappa` has a first nonzero finite transverse/mixed jet;
2. every jet vanishes.

M17-418 closes case 1 by an intrinsic-scale raw-`H2` packet contradiction.

M17-419 closes case 2 by analytic continuation and global `L2` harmonic rigidity.

Therefore

\[
\boxed{
\text{no analytic coefficient-flat minimal loop survives}
}
\]

under the retained loop geometry and representation-safe genealogy.

## 9. Combined minimal-loop closure

M17-416 closes every minimal-loop state with

\[
\kappa_\Gamma\neq0
\]

somewhere.

M17-417 closes regular first-order zero geometry.

M17-418 closes every finite higher-order zero.

M17-419 closes infinite analytic flatness.

Hence the full minimal-omega-limit loop branch is conditionally closed:

\[
\boxed{
\begin{aligned}
&\omega(Z)\text{ minimal}\\
&+\text{retained positive-flux/tubular/record geometry}\\
&\Longrightarrow
\text{contradiction}.
\end{aligned}
}
\]

The remaining compact-loop escape is therefore not an analytic coefficient value/jet branch.

It must lie in

\[
\boxed{
G_{nonminimal\ omega\text{-}limit}
\lor
G_{scale\text{-}map/genealogy}
\lor
G_{tubular\ reach/flux/amplitude}
\lor
G_{interface/rank/domain}.
}
\]

## 10. Relation to earlier harmonic modules

M17-349--354 studied harmonic/unbounded-line limits through a separate geometric route.

M17-419 does not supersede those modules globally.

It uses a stronger local premise specific to the present analytic loop branch: all coefficient jets vanish at one regular loop point, which creates an **open set** on which `Delta Omega=0`. Global analyticity of `Delta Omega` then forces global harmonicity immediately.

Thus there is no conflict with the earlier branch decomposition.

## 11. DSD audit

The DSD role is the final finite-order versus infinite-order degeneracy audit.

The terminal infinite-order case is removed by standard real-analytic uniqueness and Fourier `L2` rigidity.

No DSD axiom is used.

## 12. Audit verdict

**PASS — analytic infinite-flat loop survivor closed.**

Under minimal full omega-limit, robust loop geometry, and representation-safe record persistence, the compact closed-loop CE-H branch has no remaining coefficient-value or coefficient-jet survivor.

The next target is the complementary `nonminimal omega-limit` branch and the independent scale/genealogy/tubular/interface exits.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]