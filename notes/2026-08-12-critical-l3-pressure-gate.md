# Critical `L^3` pressure gate for the DSD-assisted Navier–Stokes route

Date: 2026-08-12

Status: **DERIVED INEQUALITY / ROUTE CLARIFICATION**.

This note isolates what can and cannot be obtained directly from the critical global

\[
T_3(t)=\int_{\mathbb R^3}|u(x,t)|^3\,dx=\|u(t)\|_3^3
\]

channel for a smooth rapidly decaying incompressible Navier–Stokes solution.

It does **not** prove global regularity.  Its purpose is to turn the previously numerical pressure-rate observation into a scale-consistent analytic gate and to identify the exact remaining obstruction.

## 1. Smooth `L^3` balance

For

\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,
\qquad \nabla\cdot u=0,
\]

multiply by `3|u|u` and integrate over `R^3`.

The transport term cancels by incompressibility and decay.  One obtains

\[
\frac{d}{dt}T_3(t)+D_3(t)=\Pi_3(t),
\]

where

\[
D_3(t)
=3\nu\int_{\mathbb R^3}|u|\left(|\nabla u|^2+|\nabla |u||^2\right)dx
\]

and

\[
\Pi_3(t)
=3\int_{\mathbb R^3}p\,u\cdot\nabla |u|\,dx.
\]

Thus advection does not directly change the global critical channel; the competition is between viscous dissipation and the pressure correlation.

## 2. Pure `T_3` control is ruled out by scaling

Under the Navier–Stokes scaling

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\qquad
p_\lambda(x,t)=\lambda^2p(\lambda x,\lambda^2t),
\]

we have

\[
T_3[u_\lambda](t)=T_3[u](\lambda^2t),
\]

while

\[
D_3[u_\lambda](t)=\lambda^2D_3[u](\lambda^2t),
\qquad
\Pi_3[u_\lambda](t)=\lambda^2\Pi_3[u](\lambda^2t).
\]

Therefore a universal instantaneous estimate of the form

\[
|\Pi_3(t)|\le F(T_3(t))
\]

with `F` depending only on the scale-invariant scalar `T_3` cannot be scale compatible unless the pressure correlation vanishes identically on the relevant class.

The repository already contains asymmetric smooth benchmark evidence with nonzero `Pi_3`; rigorous certification of one explicit nonzero example would promote this from a conditional scaling obstruction to a fully certified failed route.

**Route consequence:** the DSD pressure channel cannot be closed by the single global scalar `T_3` alone.  A same-scaling derivative/local channel is necessary.

## 3. Introduce the weighted derivative channel

Set

\[
w=|u|^{3/2}.
\]

Then

\[
\nabla w=\frac32|u|^{1/2}\nabla|u|
\]

where `u != 0`, with the usual weak interpretation across zeros, and hence

\[
\|\nabla w\|_2^2
=\frac94\int |u|\,|\nabla|u||^2dx.
\]

In particular, part of the viscous term satisfies

\[
3\nu\int |u|\,|\nabla|u||^2dx
=\frac{4\nu}{3}\|\nabla w\|_2^2.
\]

This derivative channel has the same `lambda^2` Navier–Stokes scaling as `Pi_3`.

## 4. Pressure estimate

Using

\[
-\Delta p=\partial_i\partial_j(u_i u_j),
\]

Calderón–Zygmund boundedness gives, for the exponent `9/4`,

\[
\|p\|_{9/4}
\le C_{CZ}\|u\otimes u\|_{9/4}
\le C_{CZ}\|u\|_{9/2}^2.
\]

Also

\[
|\Pi_3|
\le 2\int |p|\,|u|^{1/2}|\nabla w|\,dx.
\]

Hölder with exponents

\[
\frac{4}{9}+\frac{1}{18}+\frac12=1
\]

yields

\[
|\Pi_3|
\le 2\|p\|_{9/4}\|u\|_9^{1/2}\|\nabla w\|_2.
\]

Interpolate

\[
\|u\|_{9/2}
\le \|u\|_3^{1/2}\|u\|_9^{1/2}.
\]

Since

\[
\|u\|_9^{3/2}
=\||u|^{3/2}\|_6
=\|w\|_6,
\]

and the homogeneous Sobolev estimate gives

\[
\|w\|_6\le C_S\|\nabla w\|_2,
\]

we obtain the scale-consistent estimate

\[
\boxed{
|\Pi_3|
\le C_*\,\|u\|_3\,\|\nabla |u|^{3/2}\|_2^2
}
\]

for a universal constant `C_*` assembled from the Calderón–Zygmund and Sobolev constants.

## 5. Small-critical-channel closure

Combining the preceding estimate with the viscous contribution gives

\[
\frac{d}{dt}T_3
+3\nu\int |u|\,|\nabla u|^2dx
+\left(\frac{4\nu}{3}-C_*\|u\|_3\right)
\|\nabla |u|^{3/2}\|_2^2
\le0.
\]

Hence whenever

\[
C_*\|u(t)\|_3<\frac{4\nu}{3},
\]

this estimate closes dissipatively.

This is a **small-critical-channel gate**, not an arbitrary-data theorem.

## 6. DSD interpretation

The first useful DSD critical block should therefore not be the scalar `T_3` alone.  It must keep at least the coupled pair

\[
\mathcal C_3(t)
=
\left(
\|u(t)\|_3,
\|\nabla |u(t)|^{3/2}\|_2^2
\right)
\]

and the signed pressure channel `Pi_3`.

Suggested typed block:

- diagonal channel `q_{L3}`: `||u||_3`;
- diagonal derivative/dissipation channel `q_{G3}`: `||grad |u|^(3/2)||_2^2`;
- off-diagonal pressure coupling `q_{P3}`: `Pi_3`;
- status gate `q_absorb`: sign of `4 nu/3 - C_* ||u||_3`.

The off-diagonal channel is essential: the earlier benchmark calculations show that pressure and nonlinear cross-couplings cannot be inferred from static diagonal magnitudes alone.

## 7. What this eliminates

The following shortcuts should no longer be pursued as primary proof routes:

1. `T_3` is universally monotone decreasing.
2. `Pi_3` is universally zero by incompressibility.
3. `Pi_3` can be bounded by a function of `T_3` alone at one instant.
4. A scalar static DSD aggregate can close the critical balance without a derivative/off-diagonal channel.

## 8. Remaining proof target

The unresolved large-data problem is now sharper:

\[
\boxed{
\text{Can the DSD channel structure prevent the pressure coupling from overcoming the scale-matched dissipation for arbitrary admissible data?}
}
\]

Equivalent useful targets include any non-circular estimate that produces one of the following:

\[
\sup_{0\le t<T}\|u(t)\|_3<\infty,
\]

or a stronger established regularity-sufficient critical/local bound, without assuming regularity in the estimate itself.

The next computational/analytic work should therefore resolve `Pi_3` by spatial scale, center, sign, and alignment rather than only by a global scalar integral.

## 9. External regularity anchor

The endpoint `L^\infty_tL^3_x` regularity theorem of Escauriaza–Seregin–Šverák is retained as an external target: boundedness of the critical `L^3` norm up to a candidate finite singular time is sufficient to rule out that singularity.

This note does not re-prove that theorem; it uses it only to identify why controlling the DSD `L^3` channel would be decisive.
