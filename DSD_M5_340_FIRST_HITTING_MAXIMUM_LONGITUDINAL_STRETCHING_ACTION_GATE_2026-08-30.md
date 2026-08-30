# DSD M5-340 — First-Hitting Maximum / Longitudinal Stretching Action Gate

Date: 2026-08-30

Status: **AT VORTICITY MAXIMA VISCOSITY CANNOT PRODUCE RECORD AMPLITUDE / EACH GEOMETRIC FIRST-HITTING STAGE PAYS A FIXED `L_t^1L_x^infty` LONGITUDINAL-STRETCHING ACTION / SAME-SECTOR POSITIVE-MIDDLE CORE CANNOT USE DIFFUSION AS THE RECORD-GROWTH PAYER / GLOBAL REGULARITY UNPROVED.**

## 1. Vorticity magnitude equation

On the nonzero-vorticity set, write

\[
\omega=w\xi,
\qquad w=|\omega|,
\qquad |\xi|=1,
\]

and

\[
\gamma=\xi^TS\xi.
\]

From the vorticity equation,

\[
D_t\omega=S\omega+\nu\Delta\omega,
\]

one obtains the exact scalar identity

\[
\boxed{
D_tw
=\gamma w
+\nu\left(\Delta w-w|\nabla\xi|^2\right).
}
\]

The directional-diffusion term is explicitly nonpositive apart from the scalar Laplacian of `w`.

## 2. Spatial vorticity maximum

Let

\[
W(t)=\|\omega(t)\|_\infty.
\]

At a smooth spatial maximum point of `w`,

\[
\nabla w=0,
\qquad
\Delta w\le0.
\]

Therefore

\[
\boxed{
D_tw\le\gamma w
}
\]

at such a maximizing point.

Using the standard upper-Dini derivative argument for `W(t)`,

\[
\boxed{
D^+\log W(t)
\le
\|\gamma^+(t)\|_\infty.
}
\]

## 3. First-hitting stage cost

Let `[t_j,t_{j+1}]` be a geometric first-hitting stage with

\[
W(t_{j+1})=qW(t_j),
\qquad q>1.
\]

Integrating the Dini inequality gives

\[
\boxed{
\int_{t_j}^{t_{j+1}}
\|\gamma^+(t)\|_\infty dt
\ge\log q.
}
\]

This action is Navier--Stokes scale invariant.

Thus every record-amplifying stage pays a fixed longitudinal-stretching action.

## 4. Diffusion does not replace the growth payer

At the vorticity maximum,

\[
\nu(\Delta w-w|\nabla\xi|^2)\le0.
\]

Hence the alternatives

\[
\text{record growth by stretching}
\quad\text{versus}\quad
\text{record growth by viscosity}
\]

are not symmetric.

Viscosity can reduce record growth but cannot create it.

Therefore the same-sector branch from M5-339 sharpens to

\[
\boxed{
\text{record same-sector core}
\Longrightarrow
H_{stretch}^{max}
\ \lor\
T_{core/maximum\ relocation}.
}
\]

Even if the maximizing point changes, the global `L^infty` bound above still forces the same integrated stretching action; relocation is relevant only to lineage/localization arguments.

## 5. Relation to the positive-middle sector

On the sector

\[
\lambda_2\ge\delta|S|>0,
\]

positive `gamma` means the vorticity direction has a net extensional component.

Thus the remaining same-sector dynamic core simultaneously carries

\[
\boxed{
\lambda_2^+\text{ critical action}
+\gamma^+\text{ first-hitting action}
+S_-\text{ atom-compressive action}.
}
\]

This triple action is much more structured than the known positive-middle criterion alone, but it is not yet a contradiction.

## 6. Limitation

The lower bound

\[
\int\|\gamma^+\|_\infty dt\ge\log q
\]

per stage is consistent with a hypothetical singularity; summing infinitely many first-hitting stages gives the expected BKM-type divergence.

The next issue is spatial organization: whether the maximum-stretching point, the positive-middle productive region, and the atom-compressive region can remain separated without paying turnover/gradient action.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
