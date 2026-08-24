# Local-Energy Concentration Branch Bridge — 2026-08-24

## Status

**RIGOROUS CONDITIONAL BRANCH THEOREM — NOT GLOBAL CLOSURE.**

This note continues `LOCAL_ENERGY_FLUX_AMPLITUDE_GENEALOGY_GATE_2026-08-24.md`.

The aim is to attack the missing bridge

\[
\text{distinguished-scale concentration}
\stackrel{?}{\Longrightarrow}
\text{nontrivial local-energy crossing / historical amplitude}
\]

without silently assuming that the current repository certificates already imply an endpoint local kinetic-energy floor.

Throughout,

\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,
\qquad \nabla\cdot u=0,
\]

and the smooth finite-energy solution satisfies

\[
\|u(t)\|_2^2\le E_*<\infty
\]

on the pre-singular interval.

---

## 1. Endpoint local-energy certificate

For a ball centered at `x_0`, define

\[
K_R(t)=\int_{B_R(x_0)}|u(x,t)|^2dx.
\]

Assume at some time `t_*`

\[
\boxed{
K_R(t_*)\ge \kappa\nu^2R
}
\]

for some dimensionless `\kappa>0`.

The quantity

\[
\frac{K_R}{\nu^2R}
\]

is scale invariant.

The first question is whether a large absolute local velocity can evade every gradient certificate by behaving like an almost rigid drift.

Finite global energy prevents such a drift from remaining coherent out to arbitrarily large radii.

---

## 2. Finite-energy mean-drift bridge

Let

\[
\bar u_r=\frac1{|B_r|}\int_{B_r(x_0)}u(x,t_*)dx.
\]

The exact orthogonal decomposition is

\[
\int_{B_R}|u|^2
=
\int_{B_R}|u-\bar u_R|^2
+|B_R||\bar u_R|^2.
\]

Therefore one of two cases holds.

### Case A: relative fluctuation already carries half the energy

If

\[
\int_{B_R}|u-\bar u_R|^2
\ge
\frac{\kappa}{2}\nu^2R,
\]

Poincare gives

\[
\int_{B_R}|u-\bar u_R|^2
\le
C_PR^2\int_{B_R}|\nabla u|^2.
\]

Hence

\[
\boxed{
R\int_{B_R}|\nabla u|^2
\ge
c\kappa\nu^2.
}
\]

So the gradient certificate is already present at scale `R`.

### Case B: the mean drift carries half the energy

Otherwise

\[
|B_R||\bar u_R|^2
\ge
\frac{\kappa}{2}\nu^2R,
\]

and therefore

\[
\boxed{
|\bar u_R|
\ge
c_0\sqrt\kappa\frac{\nu}{R}.
}
\]

On the other hand, finite global energy implies for every `L>R`

\[
|\bar u_L|
\le
|B_L|^{-1/2}\|u(t_*)\|_2
\le
C E_*^{1/2}L^{-3/2}.
\]

Choose

\[
\boxed{
L_R
=C_0
\left(
\frac{E_*R^2}{\kappa\nu^2}
\right)^{1/3}
}
\]

with `C_0` sufficiently large. Then

\[
|\bar u_{L_R}|
\le
\frac12c_0\sqrt\kappa\frac{\nu}{R}.
\]

Thus the large mean present at `R` must decay before the radius reaches order `L_R`.

---

## 3. Dyadic telescoping forces a gradient scale

Let

\[
r_m=2^mR,
\]

and choose `N` minimal so that

\[
r_N\ge L_R.
\]

For consecutive balls,

\[
|\bar u_r-\bar u_{2r}|
\le
C r^{-3/2}
\|u-\bar u_{2r}\|_{L^2(B_{2r})}.
\]

By Poincare,

\[
|\bar u_r-\bar u_{2r}|
\le
C r^{-1/2}
\|\nabla u\|_{L^2(B_{2r})}.
\]

Define the scale-invariant gradient cost

\[
\boxed{
G(\rho)=ho\int_{B_\rho(x_0)}|\nabla u|^2dx.
}
\]

Then

\[
|\bar u_r-\bar u_{2r}|
\le
C\frac{G(2r)^{1/2}}{r}.
\]

Telescoping from `R` to `r_N`,

\[
|\bar u_R-\bar u_{r_N}|
\le
C\sum_{m=0}^{N-1}
\frac{G(r_{m+1})^{1/2}}{r_m}.
\]

But the choice of `L_R` gives

\[
|\bar u_R-\bar u_{r_N}|
\ge
c_1\sqrt\kappa\frac{\nu}{R}.
\]

If every dyadic scale satisfied

\[
G(r_{m+1})<\eta\kappa\nu^2,
\]

then

\[
|\bar u_R-\bar u_{r_N}|
\le
C\sqrt{\eta\kappa}\frac\nu R
\sum_{m=0}^{\infty}2^{-m}.
\]

For sufficiently small universal `\eta`, this contradicts the previous lower bound.

Therefore there exists

\[
\rho\in[R,2L_R]
\]

such that

\[
\boxed{
\rho\int_{B_\rho(x_0)}|\nabla u(x,t_*)|^2dx
\ge
c\kappa\nu^2.
}
\]

Combining Cases A and B gives the theorem

\[
\boxed{
K_R(t_*)\ge\kappa\nu^2R
\Longrightarrow
\exists\rho\in
\left[
R,
C\left(\frac{E_*R^2}{\kappa\nu^2}\right)^{1/3}
\right]
:
\rho\int_{B_\rho}|\nabla u|^2
\ge c\kappa\nu^2.
}
\]

Status: **PROVED.**

---

## 4. Shrinking-scale consequence

If a candidate singular sequence has

\[
R_j\to0
\]

and a uniform endpoint certificate

\[
K_{R_j}(t_j)\ge\kappa\nu^2R_j,
\]

then the forced gradient scales satisfy

\[
\rho_j
\le
C\left(
\frac{E_*R_j^2}{\kappa\nu^2}
\right)^{1/3}
\to0.
\]

Hence rigid drift cannot move the entire gradient cost to a fixed macroscopic scale.

It may enlarge the distinguished radius from `R_j` to order `R_j^{2/3}`, but the forced gradient scale still collapses to the candidate singular point.

Status: **PROVED.**

---

## 5. Recent-rise / persistence dichotomy

Return to the smooth cutoff local energy

\[
E_R(t)=\frac12\int|u|^2\phi_Rdx,
\]

where

\[
\phi_R=1\text{ on }B_R,
\qquad
\operatorname{supp}\phi_R\subset B_{2R}.
\]

Assume

\[
\boxed{
E_R(t_*)\ge\kappa\nu^2R.
}
\]

Fix `0<\delta<\kappa` and the backward parabolic window

\[
I_0=
\left[
 t_*-\theta\frac{R^2}{\nu},
 t_*
\right].
\]

By continuity, exactly one of the following alternatives holds.

### P. Persistence

\[
\boxed{
E_R(t)>(\kappa-\delta)\nu^2R
\quad\text{for every }t\in I_0.
}
\]

### R. Recent rise

There exists `t_-\in I_0` such that

\[
E_R(t_-)
\le
(\kappa-\delta)\nu^2R.
\]

Then

\[
\boxed{
E_R(t_*)-E_R(t_-)
\ge
\delta\nu^2R.
}
\]

This dichotomy is exact and uses no monotonicity assumption.

---

## 6. Recent rise forces a genuine crossing under a support-energy bracket

Let

\[
J=[t_-,t_*].
\]

The exact local-energy identity from the previous note is

\[
E_R(t_*)-E_R(t_-)
+D_R(J)-H_R(J)
=
\int_JF_R(t)dt,
\]

with

\[
D_R(J)
=\nu\int_J\int|\nabla u|^2\phi_Rdxdt
\ge0,
\]

and

\[
H_R(J)
=\frac\nu2\int_J\int|u|^2\Delta\phi_Rdxdt.
\]

Assume

\[
\boxed{
\sup_{t\in I_0}
\int_{B_{2R}}|u(x,t)|^2dx
\le
M_E\nu^2R.
}
\]

Since

\[
|\Delta\phi_R|\le CR^{-2}
\]

and

\[
|J|\le\theta\frac{R^2}{\nu},
\]

we have

\[
|H_R(J)|
\le
C\theta M_E\nu^2R.
\]

Therefore

\[
E_R(t_*)-E_R(t_-)+D_R(J)-H_R(J)
\ge
(\delta-C\theta M_E)\nu^2R.
\]

Choose

\[
\boxed{
\theta\le\frac{\delta}{2CM_E}.
}
\]

Then

\[
\boxed{
E_R(t_*)-E_R(t_-)+D_R(J)-H_R(J)
\ge
\frac\delta2\nu^2R.
}
\]

Thus the recent-rise branch supplies the nontrivial crossing hypothesis required by the previous flux-genealogy lemma.

Status: **PROVED CONDITIONAL ON THE SUPPORT-ENERGY BRACKET.**

---

## 7. Crossing plus the flux bracket gives a historical annular ancestor

Recall

\[
a_R(t)=\|u(t)\|_{L^3(A_R)},
\]

\[
b_R(t)=\|u(t)\|_{L^3(B_{4R})},
\]

\[
T_R(t)=
\int_{|y-x_0|>4R}
\frac{|u(y,t)|^2}{|y-x_0|^4}dy,
\]

and

\[
\mathcal K_R(t)
=a_R(t)^2+b_R(t)^2+R^3T_R(t).
\]

Assume additionally

\[
\boxed{
\sup_{t\in J}\mathcal K_R(t)
\le
M_F\nu^2.
}
\]

Then the flux estimate

\[
|F_R|
\le
CR^{-1}a_R\mathcal K_R
\]

and the crossing lower bound imply

\[
\boxed{
\sup_{t\in J}
\frac{a_R(t)}\nu
\ge
c\frac{\delta}{\theta M_F}.
}
\]

Hence a recent local-energy rise on a short parabolic window cannot occur quietly: if both brackets remain controlled, a critical annular `L^3` ancestor must appear in the recent past.

Status: **PROVED CONDITIONAL ON BOTH BRACKETS.**

---

## 8. Failure of the support-energy bracket is itself a gradient route

If the support-energy bracket fails, then for some `s\in I_0`,

\[
\int_{B_{2R}}|u(x,s)|^2dx
>M_E\nu^2R
=
\frac{M_E}{2}\nu^2(2R).
\]

Applying the finite-energy mean-drift bridge at radius `2R` gives a scale `\rho(s)\to0` along any `R\to0` sequence for which

\[
\boxed{
\rho(s)\int_{B_{\rho(s)}}|\nabla u(x,s)|^2dx
\gtrsim M_E\nu^2.
}
\]

Thus support-energy bracket failure is not an untyped escape; it routes to a shrinking-scale gradient concentration certificate.

Status: **PROVED.**

---

## 9. Far-pressure bracket failure localizes to an energetic outer shell

For `m\ge2`, let

\[
A_m=
\{2^mR<|x-x_0|\le2^{m+1}R\}
\]

and define

\[
e_m(t)=
\frac{1}{\nu^2(2^mR)}
\int_{A_m}|u(x,t)|^2dx.
\]

Then

\[
R^3T_R
\le
\nu^2
\sum_{m=2}^{\infty}2^{-3m}e_m.
\]

Since

\[
\sum_{m=2}^{\infty}2^{-3m}
=\frac1{56},
\]

if

\[
R^3T_R>M\nu^2,
\]

then necessarily

\[
\boxed{
\sup_{m\ge2}e_m>56M.
}
\]

Therefore some outer dyadic annulus satisfies

\[
\int_{A_m}|u|^2
>56M\nu^2(2^mR).
\]

With `S=2^{m+1}R`,

\[
\int_{B_S}|u|^2
>28M\nu^2S.
\]

The finite-energy mean-drift bridge then yields a gradient-concentration scale at or beyond that energetic shell.

Thus a large far-pressure tail is also a spatial energy/gradient certificate rather than a completely independent failure mode.

Status: **PROVED.**

---

## 10. Persistence forces a critical parabolic `L^3` slab

On branch P,

\[
E_R(t)>(\kappa-\delta)\nu^2R
\qquad(t\in I_0).
\]

Since `\phi_R\le1` and is supported in `B_{2R}`,

\[
\int_{B_{2R}}|u(x,t)|^2dx
\ge
2(\kappa-\delta)\nu^2R.
\]

By Holder on `B_{2R}`,

\[
\int_{B_{2R}}|u|^3dx
\ge
|B_{2R}|^{-1/2}
\left(
\int_{B_{2R}}|u|^2dx
\right)^{3/2}.
\]

Hence

\[
\boxed{
\int_{B_{2R}}|u(x,t)|^3dx
\ge
c(\kappa-\delta)^{3/2}\nu^3
}
\]

throughout the whole backward window.

Integrating in time,

\[
\boxed{
R^{-2}
\int_{I_0}\int_{B_{2R}}|u|^3dxdt
\ge
c\theta(\kappa-\delta)^{3/2}\nu^2.
}
\]

Therefore the persistence branch is not empty bookkeeping: it carries a nonvanishing critical parabolic velocity packet.

Under any blow-up compactness scheme strong enough to pass this local `L^3` mass, the resulting local/ancient limit is nontrivial on a backward time slab.

Status: **PROVED; LIMIT CONSEQUENCE CONDITIONAL ON THE REQUIRED COMPACTNESS.**

---

## 11. Combined endpoint branch theorem

Assume the endpoint cutoff-energy certificate

\[
E_R(t_*)\ge\kappa\nu^2R.
\]

Then one obtains the following branch structure.

\[
\boxed{
\text{endpoint local-energy concentration}
\Longrightarrow
\begin{cases}
\text{persistent critical local }L^3\text{ slab},\\
\text{recent-rise crossing}\to\text{historical annular }L^3\text{ ancestor},\\
\text{support-energy bracket exit}\to\text{gradient concentration},\\
\text{far-pressure-tail exit}\to\text{outer energy}\to\text{gradient concentration},\\
\text{core/annular critical-}L^3\text{ flux-bracket exit}.
\end{cases}
}
\]

In addition, independently of the time branch,

\[
\boxed{
\text{endpoint local-energy concentration}
\Longrightarrow
\text{a shrinking-scale gradient certificate}
}
\]

by the finite-energy mean-drift bridge.

This bypasses the earlier concern that a large absolute velocity packet might evade every gradient cost through pure Galilean drift.

It does **not** yet provide its historical genealogy automatically.

---

## 12. Scope audit against the current repository front

The audited repository files currently expose local critical channels such as

\[
C_u(z_0,r),\qquad C_p(z_0,r),\qquad E_\nabla(z_0,r),
\]

and the amplitude genealogy uses gradient-shell costs

\[
J_{j,k}
=R_{j,k}^{phys}
\int_{A_{R_{j,k}^{phys}}}|\nabla u|^2dx.
\]

What has **not** been established in the audited dependency chain is the implication

\[
\boxed{
\text{existing distinguished first-hitting / gradient / Campanato certificate}
\stackrel{?}{\Longrightarrow}
E_R(t_*)\ge\kappa\nu^2R
}
\]

with a uniform positive `\kappa` at the required scale.

A lower bound for gradient energy cannot be reversed through Poincare to obtain a local velocity-energy lower bound without an additional structural input.

Therefore this note closes the local-energy branch **once an endpoint local-energy certificate is available**, but it does not silently identify that certificate with the existing first-hitting certificate.

That bridge remains a separate proof obligation.

---

## 13. Updated frontier

The previous two missing arrows are refined as follows.

The Galilean-drift concern is partially repaired:

\[
\boxed{
\text{endpoint local kinetic-energy concentration}
+\text{finite global energy}
\Longrightarrow
\text{shrinking-scale gradient concentration}.
}
\]

The recent-time genealogy is also repaired conditionally:

\[
\boxed{
\text{endpoint local-energy recent rise}
+\text{controlled support/flux brackets}
\Longrightarrow
\text{historical critical annular }L^3\text{ ancestor}.
}
\]

The sharp remaining bridge is now

\[
\boxed{
\text{current repository distinguished-scale certificate}
\stackrel{?}{\Longrightarrow}
\text{uniform endpoint local-energy certificate}
}
\]

or, alternatively, a direct route from the existing gradient/first-hitting certificate to the recent-rise/persistence genealogy without passing through endpoint kinetic energy.

Global regularity remains unproved.