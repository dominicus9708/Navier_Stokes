# DSD M17-373 — Infinite strict-subscale flux evacuation forces either infinite similarity time or a finite-time nodal/interface endpoint

Date: 2026-09-08  
Canonical ID: **M17-373**

Status: **ACTIVE INFINITE-DESCENT TIME/GEOLOGY DICHOTOMY**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Same-family strict descent

Let one retained material flux family `F(theta)` start at time `theta_0` with

\[
\Phi_F(\theta_0)\ge\Phi_0>0.
\]

Suppose the same genealogy reaches a sequence of coefficient subscales

\[
r_j\downarrow0
\]

at times

\[
\theta_j\uparrow\theta_*\le+\infty.
\]

On the compact coefficient-mass/local-H2 branch, M17-371 gives

\[
\Phi_F(\theta_j)
\le C_*r_j^{5/2}.
\]

M17-372 therefore gives

\[
\boxed{
\int_{\theta_0}^{\theta_j}
\overline{\kappa_-}_{\Phi,F}d\theta
\ge
\frac52\log\frac1{r_j}-C_0.
}
\]

Hence

\[
\boxed{
\int_{\theta_0}^{\theta_*}
\overline{\kappa_-}_{\Phi,F}d\theta
=+\infty.
}
\]

## 2. Infinite-time descent is allowed as a genuine asymptotic branch

If

\[
\boxed{\theta_*=+\infty,}
\]

then the logarithmically divergent negative exposure is distributed over an infinite similarity-time interval.

This is not a contradiction. It is an explicit **secular flux-evacuation branch**.

If the material family is also recurrent and repeatedly recovers comparable flux, M17-372 additionally forces divergent positive exposure. That becomes a two-sided turnover/residence problem, but recurrence alone does not make it impossible.

## 3. Finite-time accumulation cannot remain uniformly regular and nondegenerate

Now suppose

\[
\boxed{\theta_*<\infty.}
\]

Assume for contradiction that the material family remains inside one uniformly regular nondegenerate active CE-H class on `[theta_0,theta_*]`.

Then on the family:

1. the material flow remains a smooth diffeomorphism;
2. material cross-section area Jacobians remain bounded above and below on the finite interval;
3. `W` and its spatial derivatives remain bounded;
4. the active representation has `rho=|W|>0` and finite coefficient velocity on the retained family.

Under these conditions the logarithmic flux ODE

\[
\frac d{d\theta}\log\Phi_F
=\bar\kappa_{\Phi,F}
\]

has a finite integral on every compact regular subinterval and cannot drive a positive flux continuously to zero without leaving the nondegenerate active coefficient chart.

But M17-371 gives

\[
\Phi_F(\theta_j)\to0.
\]

Therefore at least one regularity/nondegeneracy hypothesis must fail as `theta -> theta_*`.

## 4. Positive flux plus bounded material area identifies the failure as nodal or interface

Let `Sigma(theta)` be one retained oriented material cross-section for the family. On the regular positive-orientation branch,

\[
\Phi_F(\theta)
=\int_{\Sigma(\theta)}\rho\,dA.
\]

For a smooth finite-time material diffeomorphism, if the initial cross-section has positive area then

\[
0<A_*^-\le|\Sigma(\theta)|\le A_*^+<\infty
\]

as long as the cross-section remains in the same regular chart.

Since

\[
\Phi_F(\theta_j)\to0,
\]

we get

\[
\frac1{|\Sigma(\theta_j)|}
\int_{\Sigma(\theta_j)}\rho\,dA
\to0.
\]

If the surface geometry and `|grad rho|` remain uniformly bounded, a standard Lipschitz-ball argument upgrades this mean collapse to

\[
\boxed{
\sup_{\Sigma(\theta_j)}\rho\to0.
}
\]

Indeed, if `sup rho=m>0`, Lipschitz continuity produces a surface disk of radius comparable to `m/L` on which `rho>=m/2`, yielding a positive integral lower bound of order `m^3/L^2`.

Thus finite-time flux evacuation forces the retained family into the nodal set unless the cross-section itself degenerates or leaves the chart.

## 5. Exact finite-time exits

Therefore

\[
\boxed{
\begin{aligned}
&r_j\to0,
\quad \theta_j\to\theta_*<\infty,
\quad \Phi_F(\theta_j)=O(r_j^{5/2})\\
&\qquad\Longrightarrow
G_{nodal\ endpoint}
\lor G_{material\ area/geometry\ degeneration}
\lor G_{interface/rank/domain\ exit}.
\end{aligned}
}
\]

A finite-time infinite descent is not an interior regular CE-H genealogy.

## 6. Updated strict-descent classification

The compact same-family strict-subscale branch now has the time classification

\[
\boxed{
G_{strict\ subscale}^{same\ family}
\Longrightarrow
H_{infinite\text{-}time\ secular\ evacuation}
\lor
G_{finite\text{-}time\ nodal/interface\ endpoint}
\lor
G_{M_{3/2}/H2\ decompactification}.
}
\]

This removes the possibility of an infinite strict descent accumulating at a finite time while silently staying in one regular positive-amplitude CE-H chart.

## 7. DSD-theory role

The useful heuristic is the distinction between an **interior continuation** and a **boundary transition** of the structural chart. The mathematical conclusion itself uses only the exact material-flux ODE, finite-time smooth-flow geometry, positivity of the flux density, and the M17-371 flux bound.

## 8. Audit verdict

**PASS as a time/genealogy reduction.**

Finite-time infinite strict descent terminates at a typed nodal/interface/geometry boundary; otherwise the descent requires infinite similarity time.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]