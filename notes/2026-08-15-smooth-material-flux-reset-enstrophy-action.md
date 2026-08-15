# Smooth material-flux reset: a bounded-distortion enstrophy-action lower bound

Date: 2026-08-15

Status: **DERIVED CONDITIONAL RESET-COST LEMMA / DISTORTION-OR-ZENO ROUTING / GLOBAL REGULARITY NOT PROVED.**

This note targets the final repeated material-vorticity-flux reset branch.

The purpose is to replace the singular circulation of one material loop by a smooth material flux observable whose viscous change can be estimated directly by the globally time-integrable enstrophy.

The result is conditional on quantitative control of the transported test function through second spatial derivatives. Failure of that control is itself a material-deformation / high-derivative branch.

---

## 1. Terminal-normalized vorticity equation

Write the normalized incompressible Navier--Stokes vorticity equation as

\[
\partial_s\Omega
+(U\cdot\nabla)\Omega
-(\Omega\cdot\nabla)U
=\nu\Delta\Omega,
\qquad \nabla\cdot U=0.
\]

Let

\[
E(s)=\|\Omega(s)\|_2^2.
\]

At a coherent Reynolds-one crossing of radius `R`, the terminal core carries order-one nearly axial vorticity on an `O(R^3)` region and a signed flux scale

\[
\Phi_R\asymp R^2.
\]

---

## 2. Inviscid-adjoint material test

Let `psi` solve

\[
\boxed{
\partial_s\psi
+(U\cdot\nabla)\psi
+(\nabla U)^T\psi
=0.
}
\]

This is the adjoint transport equation that cancels the Euler vorticity operator in the pairing with `Omega`.

Define

\[
F(s)=\int_{\mathbb R^3}\Omega(y,s)\cdot\psi(y,s)\,dy.
\]

A direct integration by parts gives

\[
\boxed{
F'(s)
=\nu\int\Omega\cdot\Delta\psi\,dy.
}
\]

Thus material advection and stretching do not directly change this observable. Its change is purely viscous, up to whatever geometry is encoded in the transported test itself.

---

## 3. Terminal smooth flux probe

Choose a fixed smooth compactly supported profile `Psi` adapted to an oriented unit cylinder/ball and define at the crossing

\[
\boxed{
\psi_R(y)=R^{-1}\Psi(y/R).
}
\]

The factor `R^{-1}` is chosen so that order-one vorticity on an `R^3` core gives an `R^2` observable:

\[
F\asymp R^2.
\]

The Euclidean scaling is

\[
\boxed{
\|\psi_R\|_2^2\asymp R,
\qquad
\|\Delta\psi_R\|_2^2\asymp R^{-3}.
}
\]

This is a smoothed material-flux observable, not a claim that a codimension-one surface trace is controlled directly by `L^2` data.

---

## 4. Bounded-distortion hypothesis

On a candidate reset interval `I=[s_0,s_1]`, transport the terminal probe backward by the inviscid adjoint equation.

Assume that throughout `I`

\[
\boxed{
\|\psi(s)\|_2^2\le C_0R,
\qquad
\|\Delta\psi(s)\|_2^2\le C_2R^{-3},
}
\]

with constants independent of the late crossing.

The first estimate is a material-size/metric control.

The second is stronger: it excludes explosive second-derivative distortion of the material probe. If it fails, the reset has already entered the high-derivative / strong-deformation branch and is not counted as a cheap geometry-controlled reset.

---

## 5. Occupancy lower bound

Normalize the observable by

\[
\boxed{f(s)=F(s)/R^2.}
\]

By Cauchy--Schwarz,

\[
|F|^2
\le E\,\|\psi\|_2^2
\le C_0 R E.
\]

Hence

\[
\boxed{
E(s)
\ge
\frac{R^3}{C_0}|f(s)|^2.
}
\]

So a nontrivial smooth material flux cannot persist without an `R^3`-scale enstrophy occupancy.

---

## 6. Viscous rate lower bound

The exact pairing identity gives

\[
|F'|
\le
\nu E^{1/2}\|\Delta\psi\|_2
\le
\nu C_2^{1/2}R^{-3/2}E^{1/2}.
\]

Since `F=R^2f`,

\[
R^2|f'|
\le
\nu C_2^{1/2}R^{-3/2}E^{1/2}.
\]

Therefore

\[
\boxed{
E(s)
\ge
\frac{R^7}{\nu^2C_2}|f'(s)|^2.
}
\]

A very fast reset is therefore expensive in enstrophy even when the persistence time is short.

---

## 7. Duration-free reset cost

At every time,

\[
E\ge\max\left\{
\frac{R^3}{C_0}f^2,
\frac{R^7}{\nu^2C_2}(f')^2
\right\}.
\]

Using `max(A,B) >= sqrt(AB)`,

\[
\boxed{
E(s)
\ge
\frac{R^5}{\nu\sqrt{C_0C_2}}
|f(s)f'(s)|.
}
\]

If a reset episode changes the observable from

\[
|f(s_0)|\le a
\]

to

\[
|f(s_1)|\ge b,
\qquad 0\le a<b,
\]

then total variation gives

\[
\int_I |ff'|ds
\ge
\frac12(b^2-a^2).
\]

Hence

\[
\boxed{
\int_I E(s)ds
\ge
\frac{b^2-a^2}{2\nu\sqrt{C_0C_2}}
R^5.
}
\]

For a fixed fractional reset, for example `a<=1/4`, `b>=3/4`,

\[
\boxed{
\int_I E(s)ds
\gtrsim_{\nu,C_0,C_2} R^5.
}
\]

The important point is that the lower bound no longer contains the reset duration. Slow reset pays occupancy; fast reset pays viscous rate.

---

## 8. Return to physical kinetic-energy dissipation

At a terminal first-hitting level `W`, the normalization is

\[
y=\sqrt W\,(x-x_*),
\qquad
s=W(t-T),
\qquad
\Omega=W^{-1}\omega.
\]

Therefore

\[
E_{\rm norm}=W^{-1/2}E_{\rm phys},
\qquad
ds=Wdt,
\]

and so

\[
\boxed{
\int E_{\rm norm}ds
=\sqrt W\int E_{\rm phys}dt.
}
\]

The physical kinetic-energy identity dissipates

\[
\nu\int E_{\rm phys}dt.
\]

Thus one geometry-controlled fixed-fraction reset costs

\[
\boxed{
\nu\int_I E_{\rm phys}dt
\gtrsim
\frac{R^5}{\sqrt W}.
}
\]

Introduce the inheritance ratio

\[
\boxed{
q_0:=\frac{W}{R^{10}}.
}
\]

Then

\[
\boxed{
\frac{R^5}{\sqrt W}=q_0^{-1/2}.
}
\]

Hence every bounded-distortion reset costs at least a constant multiple of `q_0^{-1/2}` of the finite physical kinetic-energy budget.

---

## 9. Repeated-reset consequence

Take disjoint late reset intervals indexed by `j`, with crossing parameters `(W_j,R_j)` and

\[
q_j=W_j/R_j^{10}.
\]

If the bounded-distortion hypotheses hold uniformly on all those reset intervals, finite total energy dissipation forces

\[
\boxed{
\sum_j q_j^{-1/2}<\infty.
}
\]

Therefore a hypothetical singular cascade cannot repeat geometry-controlled resets with bounded or slowly growing `q_j`.

It must enter one of two regimes:

1. **super-separated Zeno reset**
   \[
   \sum_jq_j^{-1/2}<\infty,
   \qquad q_j\to\infty\text{ sufficiently rapidly};
   \]
2. **probe-distortion reset**
   the transported material test loses the uniform `L^2/H^2` shape control, activating strong strain / derivative / shell geometry.

This is not yet a contradiction. It is a new necessary condition on any surviving infinite reset cascade.

---

## 10. Relation to the previous automatic reset checkpoint

The previous frontier derived the inheritance ceiling

\[
q\lesssim C\frac{W}{R^{10}}
\]

for a coherent flux inherited to an earlier checkpoint.

Thus `q_0=W/R^10` is exactly the natural reset-separation parameter.

The present result shows that the same parameter also controls the **minimum physical energy-dissipation price** of rebuilding the smooth material flux:

\[
\boxed{
\text{inheritance horizon: }q_0,
\qquad
\text{reset price: }q_0^{-1/2}.
}
\]

This duality is the main new structural output.

---

## 11. Claim boundary

This note does **not** prove flux-reset nonrepeatability.

The second-derivative control of the inviscid-adjoint probe is a real hypothesis. A full theorem must show that failure of this probe regularity is itself charged to a cumulative derivative/strain budget strongly enough to prevent an infinite Zeno sequence.

Even under uniform probe control, the energy identity yields only

\[
\sum q_j^{-1/2}<\infty,
\]

which still permits sufficiently fast growth of `q_j`.

Therefore the new frontier is

\[
\boxed{
\text{super-separated Zeno reset}
\quad\lor\quad
\text{material-probe metric/derivative collapse}.
}
\]

Status: **RESET COST DERIVED UNDER BOUNDED MATERIAL-PROBE DISTORTION / INFINITE RESET REDUCED TO ZENO SEPARATION OR DISTORTION / GLOBAL REGULARITY NOT PROVED.**