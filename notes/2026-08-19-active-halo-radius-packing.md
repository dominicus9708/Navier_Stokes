# Active halo radius packing bounds

Date: 2026-08-19

Status: **DERIVED REMOTE-INFLUENCE / ENERGY / PALINSTROPHY PACKING GATE / GLOBAL REGULARITY NOT PROVED**.

This note continues the critical non-tightness and remote-tail analysis. The endpoint `L^3` theorem forces a global non-tight sector, but only a portion of that sector can dynamically drive the tracked first-hitting core.

---

## 1. Active halo definition

Work in dynamic first-hitting variables with

\[
\|\Omega\|_\infty=1.
\]

Fix a core ball `B_R0`. Let a remote vorticity sector lie outside normalized radius `R >> R0`.

Call the remote sector **active** at a time if its contribution to the strain in the tracked core satisfies

\[
\boxed{
\|S_{\rm halo}\|_{L^\infty(B_{R_0})}
\ge \sigma_0
}
\]

for a fixed `sigma0>0`.

---

## 2. Remote strain forces halo enstrophy occupancy

The Biot--Savart strain kernel gives

\[
\|S_{\rm halo}\|_{L^\infty(B_{R_0})}
\lesssim
R^{-3/2}E_{\Omega,\rm halo}^{1/2}.
\]

Hence activity requires

\[
\boxed{
E_{\Omega,\rm halo}
\gtrsim
\sigma_0^2R^3.
}
\]

Since `||Omega||_infty<=1`, the halo cannot obtain this lower bound from arbitrarily tiny amplitude on a tiny set. It carries order-volume enstrophy occupancy at scale `R`.

Moreover, because `|Omega|^(3/2) >= |Omega|^2` under the first-hitting cap,

\[
\int_{\rm halo}|\Omega|^{3/2}
\ge E_{\Omega,\rm halo},
\]

so

\[
\boxed{
\|\Omega\|_{L^{3/2}(\rm halo)}
\gtrsim
\sigma_0^{4/3}R^2.
}
\]

Thus an active large halo automatically supplies a large portion of the critical vorticity norm required by the endpoint `L^3` blow-up condition.

---

## 3. Physical energy-dissipation packing

Physical enstrophy and normalized enstrophy satisfy

\[
E_\omega=W^{1/2}E_\Omega,
\qquad dt=W^{-1}ds.
\]

Therefore the physical kinetic-energy dissipation is

\[
\nu\int E_\omega dt
=
\nu\int W^{-1/2}E_\Omega ds.
\]

Suppose an active halo of radius `R_j` persists for normalized duration `tau_j` inside a geometric first-hitting stage with `W comparable to W_j`. Then

\[
\boxed{
D^{\rm phys}_{j,\rm halo}
\gtrsim
\nu\sigma_0^2
W_j^{-1/2}R_j^3\tau_j.
}
\]

Since total physical energy dissipation is finite,

\[
\boxed{
\sum_j
W_j^{-1/2}R_j^3\tau_j
<\infty
}
\]

for disjoint active-stage contributions.

In particular, if `tau_j>=tau0>0` along infinitely many active stages, then

\[
\boxed{
R_j/W_j^{1/6}\to0
}
\]

along that subsequence. Thus a repeatedly active `O(1)`-duration halo cannot remain at or beyond the `W^(1/6)` normalized radius.

This recovers the earlier `W^(1/6)` terminal/far-scale threshold from a direct remote-influence argument.

---

## 4. Energy--palinstrophy interpolation gives a stronger derivative-controlled radius

Let

\[
K_U=\|U\|_2^2,
\qquad
E_\Omega=\|\Omega\|_2^2,
\qquad
P_\Omega=\|\nabla\Omega\|_2^2.
\]

Fourier Cauchy--Schwarz gives the exact interpolation

\[
\boxed{
E_\Omega^2
\le
K_U P_\Omega.
}
\]

Physical energy is nonincreasing, so if `K0` is the initial kinetic energy,

\[
K_U=W^{1/2}\|u(t)\|_2^2
\le
K_0W^{1/2}.
\]

Activity gives `E_Omega >= c sigma0^2 R^3`, hence

\[
\boxed{
P_\Omega
\gtrsim
\frac{\sigma_0^4R^6}{K_0W^{1/2}}.
}
\]

Therefore if the active-halo branch also avoids normalized palinstrophy growth,

\[
P_\Omega\le P_*
\]

uniformly, then

\[
\boxed{
R
\lesssim
(K_0P_*)^{1/6}\sigma_0^{-2/3}W^{1/12}.
}
\]

So an active, derivative-controlled halo is confined to a substantially smaller intermediate range than the energy-dissipation threshold alone:

\[
\boxed{
1\ll R\lesssim W^{1/12}
}
\]

up to fixed constants.

If `R/W^(1/12) -> infinity`, then normalized palinstrophy must diverge and the branch is routed to derivative escape `H`.

---

## 5. Passive versus active critical non-tightness

The endpoint critical theorem requires global non-tightness, but the remote strain estimate separates it into two distinct sectors.

### Passive critical halo

The global `L^3 / L^(3/2)` critical norm escapes to large normalized radii but

\[
\|S_{\rm halo}\|_{core}\to0.
\]

This sector is required by critical regularity theory but does not supply local vortex-stretching production.

### Active intermediate halo

The halo contributes order-one strain to the core. Then it must satisfy the occupancy and packing bounds above. Repeated non-derivative active coupling is confined to `R << W^(1/6)` and, under bounded normalized palinstrophy, to `R <= O(W^(1/12))`.

Thus a singular recurrent-core scenario requires both:

1. global critical non-tightness;
2. a local or intermediate-scale production mechanism.

These are not the same budget.

---

## 6. Revised core--halo theorem target

The remaining cross-scale problem is now concentrated in the intermediate active range:

\[
\boxed{
1\ll R_j\lesssim W_j^{1/12}
}
\]

for a derivative-controlled halo, with shorter/larger-radius episodes routed to the existing fast-stage or derivative branches.

A useful next theorem would show that repeated transfer of order-one strain from this intermediate halo into the tracked core requires a non-summable material/pressure or covariance-reorganization action.

Status: **ACTIVE FAR HALO BEYOND W^(1/6) NONREPEATABLE FOR O(1) DURATION; DERIVATIVE-CONTROLLED ACTIVE HALO CONFINED TO W^(1/12) INTERMEDIATE SCALE.**