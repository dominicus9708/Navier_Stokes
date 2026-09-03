# DSD M5-677 — Zero-curvature CE-H linearizes Navier–Stokes; compact recurrence forces a uniform curvature floor

Date: 2026-09-03

Status: **INTERNAL CE-H BRANCH CLOSURE / IF THE VORTEX-LINE CURVATURE `K=(xi·grad)xi` VANISHES GLOBALLY AT ONE CE-H STATE, ANALYTICITY EXTENDS EACH NONZERO STRAIGHT VORTEX-LINE DIRECTION THROUGH ITS NODAL POINTS, `U(y)->0` AND `(xi·grad)U=sigma xi` FORCE `U x W=0`, AND THE HOMOGENEOUS MATERIAL CURVATURE LAW PROPAGATES `K=0` FOR ALL TIMES / THEN THE NAVIER-STOKES NONLINEARITY IS A PURE GRADIENT AND THE SIMILARITY VORTICITY SATISFIES THE LINEAR HEAT/ORNSTEIN-UHLENBECK EQUATION, WHOSE EXACT ENSTROPHY LEDGER `1/2 E' + 1/4 E + P = 0` CONTRADICTS ANY NONZERO RECURRENT INVARIANT COMPONENT / CONSEQUENTLY A COMPACT MARKED CE-H HULL HAS A UNIFORM POSITIVE CURVATURE POLYNOMIAL GAP, AND EVERY STATE CONTAINS A FIXED-STRENGTH CURVATURE PACKET / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Curvature polynomial without division by `|W|`

On the active set write

\[
W=\rho\xi,
\qquad
\mathcal K:=(\xi\cdot\nabla)\xi.
\]

Then

\[
(W\cdot\nabla)W
=\rho(\xi\cdot\nabla\rho)\xi+\rho^2\mathcal K.
\]

Hence the division-free analytic polynomial

\[
\boxed{
\mathcal C_W
:=
W\times((W\cdot\nabla)W)
}
\]

satisfies

\[
|\mathcal C_W|=\rho^3|\mathcal K|.
\]

Therefore

\[
\mathcal C_W\equiv0
\]

is exactly the statement that every nonzero vortex line is locally straight:

\[
\boxed{\mathcal K=0\quad\text{where }W\ne0.}
\]

The advantage of `C_W` is that it remains a globally analytic vector field even across the zero set of `W`.

---

## 2. Analytic continuation of a straight vortex line through nodal points

Fix a point `y0` with `W(y0)!=0` and let

\[
e:=\xi(y_0).
\]

Because `K=0`, the unit tangent is constant along its vortex line while `W!=0`.
Thus on an open segment of the affine line

\[
y(s)=y_0+se
\]

we have

\[
W(y(s))\parallel e.
\]

For every fixed vector `e_perp perpendicular e`, the scalar function

\[
s\mapsto e_\perp\cdot W(y_0+se)
\]

is real analytic in `s` and vanishes on an open interval.
Hence it vanishes for all real `s`.

Thus the same affine line continues through possible nodal points of `W` with

\[
\boxed{W(y_0+se)\parallel e\quad\forall s\in\mathbb R.}
\]

So the zero set does not terminate the underlying straight analytic vortex-line carrier.

---

## 3. CE-H velocity derivative on the straight line

M5-600 gives on CE-H

\[
\boxed{(W\cdot\nabla)U=\sigma W.}
\]

On a nonzero part of the affine vortex line this becomes

\[
\boxed{(e\cdot\nabla)U=\sigma e.}
\]

Therefore the transverse velocity

\[
P_e^\perp U(y_0+se)
\]

is constant in `s`.

M5-523 established the uniform far-field decay

\[
U(y,\theta)\to0
\qquad(|y|\to\infty)
\]

on the compact hard hull.
Taking `s->+/-infinity` along the affine line therefore gives

\[
P_e^\perp U=0.
\]

Hence on every nonzero vortex line

\[
\boxed{U\parallel W.}
\]

By continuity,

\[
\boxed{U\times W\equiv0.}
\]

---

## 4. Propagation of zero curvature in CE-H

M5-620 gives the exact material curvature law

\[
\boxed{
D_B\mathcal K
=-(\sigma+\tfrac12)\mathcal K.
}
\]

This is a homogeneous ODE along every material vortex-line label.
Therefore if `K=0` at one complete spatial state, it remains zero under both forward and backward continuation of the complete CE-H trajectory:

\[
\boxed{
\mathcal K(\cdot,\theta_0)=0
\Longrightarrow
\mathcal K(\cdot,\theta)=0
\quad\forall\theta\in\mathbb R.
}
\]

Consequently

\[
U\times W=0
\]

holds for the entire trajectory.

---

## 5. Navier–Stokes nonlinearity becomes a gradient

For a divergence-free velocity,

\[
(U\cdot\nabla)U
=\nabla\frac{|U|^2}{2}-U\times W.
\]

Thus on the global zero-curvature CE-H branch,

\[
\boxed{
(U\cdot\nabla)U
=\nabla\frac{|U|^2}{2}.
}
\]

The nonlinear term is therefore absorbed completely into the pressure.
Equivalently, taking curl removes the nonlinearity exactly.

The similarity vorticity equation reduces to

\[
\boxed{
\partial_\theta W
+W+\frac12(y\cdot\nabla)W
=\Delta W.
}
\]

This is the linear similarity heat/Ornstein–Uhlenbeck vorticity equation.

---

## 6. Strict linear enstrophy ledger

Multiply by `W` and integrate over `R^3`.
Since

\[
\int W\cdot(y\cdot\nabla W)
=-\frac32E,
\]

we obtain

\[
\boxed{
\frac12E'
+\frac14E
+P
=0,
}
\]

where

\[
E=\|W\|_2^2,
\qquad
P=\|\nabla W\|_2^2.
\]

On an invariant recurrent component the mean derivative of bounded `E` vanishes, hence

\[
\frac14\langle E\rangle+\langle P\rangle=0.
\]

Both terms are nonnegative, so

\[
E=P=0
\]

in the invariant measure.
Therefore

\[
W\equiv0,
\]

contradicting the marked nonzero hard component.

Thus

\[
\boxed{
E_{CEH}^{\mathcal K\equiv0}\Longrightarrow\bot.
}
\]

---

## 7. Compactness upgrades nonvanishing curvature to a uniform gap

Define the continuous polynomial functional on the global smooth compact CE-H hull

\[
\mathfrak C(Y)
:=
\|W_Y\times((W_Y\cdot\nabla)W_Y)\|_{L^2}.
\]

If `mathfrak C(Y)=0`, the preceding argument gives the forbidden global zero-curvature branch.
Hence

\[
\mathfrak C(Y)>0
\]

for every state `Y` in the marked compact hull.

Compactness therefore yields

\[
\boxed{
\inf_Y\mathfrak C(Y)
=:c_{curv}>0.
}
\]

This removes the earlier possibility that the recurrent survivor could asymptotically avoid the M5-619 curvature channel and live only on transverse magnitude gradients.

---

## 8. Fixed-strength curvature packet in every state

The all-order compact hull gives uniform bounds

\[
\|W\|_\infty\le M_0,
\qquad
\|\nabla W\|_\infty\le M_1,
\]

and global spatial tail tightness for every fixed derivative order.

The positive `L2` floor on `C_W`, finite-core localization, and smooth thickening therefore give constants

\[
\rho_*>0,
\quad
k_*>0,
\quad
r_*>0
\]

such that every recurrent CE-H state contains a ball `B_{r_*}` on which

\[
\boxed{
\rho\ge\rho_*,
\qquad
|\mathcal K|\ge k_*.
}
\]

Equivalently

\[
\boxed{
Z_{curv}:=\rho|\mathcal K|
\ge z_*:=\rho_*k_*>0.
}
\]

Direction coherence on the same ball extracts a nondegenerate directed transverse vorticity flux packet, so every state produces a curvature-active event eligible for the M5-621 finite-memory curvature/flux cocycle.

---

## 9. Consequence for the finite genealogy

M5-621 already proves that one retained fixed-flux material label can carry

\[
Z_{curv}\ge z_*
\]

for only a uniformly finite similarity-time lifetime.

M5-677 shows that such curvature activity is not optional:

\[
\boxed{
\text{every recurrent CE-H state contains a fixed-strength curvature packet.}
}
\]

Therefore

\[
\boxed{
E_{CEH}^{hard}
\Longrightarrow
T_{curv}^{label\ renewal}
}
\]

with positive asymptotic event rate after the usual uniform time-thickening.

The former M5-619 alternative

\[
\text{curvature}
\lor
\text{transverse magnitude}
\]

is strengthened: transverse magnitude may coexist, but it can no longer replace curvature completely on the recurrent hard hull.

---

## 10. Firewall

This document does **not** yet claim that positive-rate curvature-label renewal exhausts the finite base transverse-flux resource.

A very late curvature-active label may originate from an exponentially small base-slice flux element and be amplified before its first retained event.
The M5-647 finite total flux bound alone does not prohibit an infinite nested hierarchy of such small base labels.

Thus the remaining task is to control the **amplification/recharge of newly activated curvature labels**, not merely to count them.

No use is made here of the weak-Beltrami Liouville theorems; the contradiction comes directly from the Navier–Stokes linearization and the recurrent enstrophy ledger.

---

## 11. Updated frontier

The CE-H hard survivor now has simultaneously

\[
\boxed{
\text{fixed-strength curvature packet at every recurrent state}
}
\]

and

\[
\boxed{
\text{uniform finite curvature-active lifetime of each retained material flux label}.
}
\]

Hence the last cycle cannot be a finite set of eternally recycled curvature labels.
It must continually activate new/smaller material flux populations and recharge them strongly enough to reach the fixed retained flux threshold.

That amplification mechanism is the next target.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
