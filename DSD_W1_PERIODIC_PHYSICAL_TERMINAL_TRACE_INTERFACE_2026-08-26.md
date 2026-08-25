# DSD W1 Periodic Physical Terminal Trace Interface

Date: 2026-08-26

Status: **PERIODIC CANONICAL LERAY TAIL INVERTED TO A STATIC PHYSICAL `1/r` TERMINAL TRACE / TRACE IS LOCALLY FINITE-ENERGY BUT EXACTLY CRITICAL AT `L3` AND NON-`H1` / FIXED PHYSICAL ANNULI CONVERGE STRONGLY TO THE TRACE / FINITE ENERGY THEREFORE DOES NOT BY ITSELF EXCLUDE THE PERIODIC SURVIVOR / GLOBAL REGULARITY UNPROVED.**

## 1. Canonical periodic Leray tail

On the periodic W1 branch the canonical far tail has the form

\[
T(Y,s)
=
\frac1{|Y|}
\Phi\left(\widehat Y,\log|Y|-\frac s2\right),
\]

where `Phi` is periodic in its logarithmic argument with period

\[
L=\frac S2.
\]

The actual Leray profile satisfies, on same-phase remote cells,

\[
U-T\in L^2\cap L^3
\]

with quantitative cell decay. In particular, for a log cell at radius `R`,

\[
\|U-T\|_{L^2(C_R)}^2\lesssim R^{-1},
\]

and

\[
\int_{C_R}|U-T|^3dY\lesssim R^{-3/2}.
\]

---

## 2. Exact inverse Leray transform

Let

\[
\tau:=T_*-t,
\qquad
Y=\frac{x-X_*}{\sqrt\tau},
\qquad
s=-\log\tau.
\]

Set

\[
r:=|x-X_*|.
\]

Then

\[
|Y|=\frac r{\sqrt\tau}
\]

and

\[
\log|Y|-\frac s2
=
\log r.
\]

Therefore

\[
\begin{aligned}
u_T(x,t)
&=
\tau^{-1/2}T(Y,s)\\
&=
\frac1r
\Phi(\widehat{x-X_*},\log r).
\end{aligned}
\]

Thus the leading physical tail is **exactly time independent**:

\[
\boxed{
u_*(x)
:=
\frac1{|x-X_*|}
\Phi\bigl(\widehat{x-X_*},\log|x-X_*|\bigr).
}
\]

It is discretely scale invariant in physical space:

\[
\boxed{
u_*(X_*+\lambda x)=\lambda^{-1}u_*(X_*+x)
}
\]

for `lambda=e^L`.

---

## 3. Strong convergence on every fixed punctured annulus

Fix

\[
0<r_1<r_2<\infty.
\]

As `tau downarrow 0`, the corresponding Leray radii satisfy

\[
R\asymp \tau^{-1/2}\to\infty.
\]

The physical `L2` scaling gives

\[
\|u-u_*\|_{L_x^2(A_{r_1,r_2})}^2
=
\tau^{1/2}
\|U-T\|_{L_Y^2(A_{R_1,R_2})}^2.
\]

Using the cell estimate

\[
\|U-T\|_2^2\lesssim R^{-1}\asymp\tau^{1/2},
\]

we get

\[
\boxed{
\|u(t)-u_*\|_{L^2(A_{r_1,r_2})}
\lesssim\tau^{1/2}.
}
\]

Likewise `L3` is scaling invariant, and the cubic cell error gives

\[
\boxed{
\|u(t)-u_*\|_{L^3(A_{r_1,r_2})}
\lesssim\tau^{1/4}.
}
\]

Therefore the physical solution converges strongly to the same static critical trace on every fixed annulus away from the candidate singular point.

---

## 4. Exact local integrability of the trace

Assume `Phi` is bounded and nonzero on a positive-measure set, as forced by the occupied critical tail.

Since

\[
|u_*|\sim r^{-1},
\]

we have near `r=0`

\[
\int_{B_\rho}|u_*|^qdx
\sim
\int_0^\rho r^{2-q}dr.
\]

Hence

\[
\boxed{
u_*\in L^q_{loc}
\quad\text{for every }q<3,
}
\]

while the critical exponent has logarithmic divergence:

\[
\boxed{
u_*\notin L^3_{loc}
}
\]

for a nonzero log-periodic critical tail.

At the endpoint the bounded `1/r` profile belongs naturally to weak `L3` locally.

---

## 5. Finite energy but infinite enstrophy

For `q=2`,

\[
\int_{B_\rho}|u_*|^2dx
\sim
\int_0^\rho dr
\sim \rho.
\]

Thus

\[
\boxed{
u_*\in L^2_{loc},
\qquad
E_*(B_\rho)=O(\rho).
}
\]

This is the exact reason finite kinetic energy does not exclude the singular trace.

On the other hand

\[
|\nabla u_*|\sim r^{-2},
\]

so

\[
\int_{B_\rho\setminus B_\varepsilon}
|\nabla u_*|^2dx
\sim
\int_\varepsilon^\rho r^{-2}dr
\sim\frac1\varepsilon.
\]

Hence

\[
\boxed{
u_*\notin H^1_{loc}
}
\]

and the terminal enstrophy diverges with the exact inverse-radius law.

More generally,

\[
\nabla u_*\in L^p_{loc}
\quad\text{for }p<\frac32,
\]

with the `p=3/2` endpoint critical.

---

## 6. Critical shell interpretation

A physical logarithmic shell

\[
r<|x-X_*|<\lambda r
\]

contains

\[
\int |u_*|^3dx
=
\text{order one},
\]

independently of `r`.

But its kinetic energy is only

\[
\int |u_*|^2dx
=O(r).
\]

Thus as `r downarrow 0`,

\[
\boxed{
\text{critical `L3` memory remains order one per log shell}
}
\]

while

\[
\boxed{
\text{physical `L2` energy carried by that shell tends to zero linearly}.
}
\]

This is the terminal-trace form of the half-power/finite-parent barrier.

---

## 7. Why this does not imply a stationary Navier--Stokes profile

Although `u_*` is time independent, one must **not** conclude that it solves the stationary unforced Navier--Stokes equation.

The previously derived nonresonant correction has physical size schematically

\[
q(x,t)=O\left(\frac{\tau}{r^3}\right)
\]

on a fixed punctured region.

Hence

\[
q\to0
\]

as `t upward T_*`, but

\[
\partial_tq=O(r^{-3})
\]

need not vanish.

That time derivative can cancel the stationary viscous/nonlinear residual of `u_*`.

Therefore

\[
\boxed{
\text{static terminal trace}
\not\Rightarrow
\text{stationary NS solution}.
}
\]

This prevents an invalid reduction to stationary `-1` homogeneous Liouville theory.

---

## 8. Updated interface target

The periodic branch now has a particularly sharp formulation:

\[
\boxed{
\begin{array}{c}
\text{one finite-energy physical parent}\[1mm]
\downarrow\\[1mm]
\text{strong convergence off }X_*\\[1mm]
\downarrow\\[1mm]
 u_*(x)=r^{-1}\Phi(\theta,\log r)\\[1mm]
\text{with }u_*\in L^2_{loc}\cap L^{3,\infty}_{loc}
\text{ but }u_*\notin L^3_{loc},H^1_{loc}.
\end{array}
}
\]

So a useful global-anchor theorem must exploit how this exact critical terminal trace is dynamically attached to the unforced finite-energy parent. Merely invoking finite `L2` energy cannot remove it, because the trace itself already has finite local energy.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
