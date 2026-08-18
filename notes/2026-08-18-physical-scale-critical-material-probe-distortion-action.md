# Physical scale-critical material-probe distortion action

Date: 2026-08-18

Status: **PHYSICAL-SCALE REFORMULATION OF THE MATERIAL-PROBE H2 DISTORTION ROUTING. A FIXED-FACTOR LOSS OF NATURAL PROBE SHAPE AT SCALE ell COSTS A FIXED AMOUNT OF THE NS-SCALE-INVARIANT ACTION int (|grad u|_inf + ell |grad^2 u|_inf + ell^2 |grad^3 u|_inf) dt. GLOBAL REGULARITY NOT PROVED.**

## 1. Physical flux probe at scale ell

Let

\[
\psi_\ell(x)=\ell^{-1}\Psi((x-a)/\ell)
\]

and transport it by the inviscid adjoint material equation

\[
D_t\psi
:=
(\partial_t+u\cdot\nabla)\psi
=-(\nabla u)^T\psi.
\]

Its natural Euclidean norms are

\[
\|\psi_\ell\|_2\asymp\ell^{1/2},
\qquad
\|\nabla\psi_\ell\|_2\asymp\ell^{-1/2},
\qquad
\|\nabla^2\psi_\ell\|_2\asymp\ell^{-3/2}.
\]

Define the dimensionless shape monitor

\[
\boxed{
\mathfrak M_\ell
=\ell^{-1/2}\|\psi\|_2
+\ell^{1/2}\|\nabla\psi\|_2
+\ell^{3/2}\|\nabla^2\psi\|_2.
}
\]

For a fixed physical scale `ell` on one reset/distortion episode, the weights are constant in time.

## 2. Differential estimate

Differentiating the material adjoint equation gives the standard hierarchy

\[
\frac d{dt}\|\psi\|_2
\lesssim
\|\nabla u\|_\infty\|\psi\|_2,
\]

\[
\frac d{dt}\|\nabla\psi\|_2
\lesssim
\|\nabla u\|_\infty\|\nabla\psi\|_2
+\|\nabla^2u\|_\infty\|\psi\|_2,
\]

and

\[
\frac d{dt}\|\nabla^2\psi\|_2
\lesssim
\|\nabla u\|_\infty\|\nabla^2\psi\|_2
+\|\nabla^2u\|_\infty\|\nabla\psi\|_2
+\|\nabla^3u\|_\infty\|\psi\|_2.
\]

After multiplying by the natural powers of `ell` and absorbing the components into `M_ell`, 

\[
\boxed{
\frac d{dt}\mathfrak M_\ell
\lesssim
\left[
\|\nabla u\|_\infty
+\ell\|\nabla^2u\|_\infty
+\ell^2\|\nabla^3u\|_\infty
\right]\mathfrak M_\ell.
}
\]

Hence

\[
\boxed{
\frac d{dt}\log\mathfrak M_\ell
\lesssim
\mathcal G_\ell(t),
}
\]

with

\[
\boxed{
\mathcal G_\ell
:=
\|\nabla u\|_\infty
+\ell\|\nabla^2u\|_\infty
+\ell^2\|\nabla^3u\|_\infty.
}
\]

## 3. Scale criticality

Under the Navier--Stokes scaling

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\qquad
\ell_\lambda=\lambda^{-1}\ell,
\]

we have

\[
\|\nabla u_\lambda\|_\infty
=\lambda^2\|\nabla u\|_\infty,
\]

\[
\ell_\lambda\|\nabla^2u_\lambda\|_\infty
=\lambda^2\ell\|\nabla^2u\|_\infty,
\]

\[
\ell_\lambda^2\|\nabla^3u_\lambda\|_\infty
=\lambda^2\ell^2\|\nabla^3u\|_\infty,
\]

while `dt_lambda=lambda^-2 dt`.  Therefore

\[
\boxed{
\mathcal A_{\rm geom}(I;\ell)
:=
\int_I\mathcal G_\ell(t)dt
}
\]

is exactly scale invariant.

## 4. Fixed-factor distortion cost

If during an episode

\[
\mathfrak M_\ell(t_1)
\ge M_0\mathfrak M_\ell(t_0),
\qquad M_0>1,
\]

then Gronwall gives

\[
\boxed{
\mathcal A_{\rm geom}(I;\ell)
\gtrsim
\log M_0.
}
\]

Thus every fixed-factor failure of the bounded-shape material-probe hypothesis pays a fixed positive amount of a scale-critical derivative/strain action.

## 5. Relation to compact natural packets

For a natural packet at physical frequency `K`, take

\[
\ell=K^{-1}.
\]

Then

\[
\boxed{
\mathcal A_{\rm geom,K}
=
\int
\left[
\|\nabla u\|_\infty
+K^{-1}\|\nabla^2u\|_\infty
+K^{-2}\|\nabla^3u\|_\infty
\right]dt.
}
\]

This remains order one under natural parabolic rescaling.  Hence high-frequency probe distortion is not cheaper merely because `K` is large.

## 6. Distinction from derivative-order ascent

The operator controlling the smooth flux reset remains `Delta` at every scale.  Repeated reset/distortion events therefore need not increase derivative **order**.  The present action is instead a physical-scale critical measurement of fixed low derivative orders.

It complements, rather than replaces, the factorial derivative-order projective ledger.

## 7. Limitation

No global a-priori finite bound is known for `A_geom` near a hypothetical singularity.  Repeated distortion can therefore force divergence of this critical action without producing a contradiction.

Status: **FIXED-FACTOR MATERIAL-PROBE DISTORTION COSTS FIXED SCALE-CRITICAL GEOMETRIC ACTION / PHYSICAL SCALE AND DERIVATIVE ORDER REMAIN DISTINCT / GLOBAL REGULARITY NOT PROVED.**