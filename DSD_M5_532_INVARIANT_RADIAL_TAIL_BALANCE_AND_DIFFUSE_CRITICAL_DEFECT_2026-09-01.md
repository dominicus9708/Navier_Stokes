# DSD M5-532 — Invariant radial-tail balance splits strong critical mass from a diffuse conservative defect

Date: 2026-09-01

Status: **INVARIANT RADIAL DEFECT EQUATION / AVERAGING THE M5-530 LOG-RADIUS TRANSPORT LAW OVER THE M5-531 NONTRIVIAL INVARIANT COMPONENT ELIMINATES THE SIMILARITY-TIME DERIVATIVE AND PRODUCES THE EXACT ONE-DIMENSIONAL RADIAL BALANCE `1/2 d_rho Tbar = Sbar` / M5-531 AND TONELLI FORCE THE MEAN CRITICAL TAIL `Tbar` TO HAVE INFINITE LOG-RADIUS INTEGRAL / THEREFORE THE HARD CORE EITHER HAS UNBOUNDED MEAN CRITICAL EXTERIOR ENSTROPHY OR A BOUNDED BUT NONINTEGRABLE DIFFUSE TAIL WHOSE SIGNED RADIAL SOURCE HAS BOUNDED PRIMITIVE / THE SECOND CASE IS A CONSERVATIVE/OSCILLATORY RADIAL DEFECT, NOT A MONOTONE ESCAPE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M5-530

For

\[
R=e^\rho,
\]

define

\[
\mathfrak T(\rho,Y)
:=
R\int_{|y|>R}|W_Y(y)|^2dy.
\]

M5-530 proved

\[
\boxed{
\left(\partial_\theta+\frac12\partial_\rho\right)
\mathfrak T
=
\mathcal S,
}
\]

where

\[
\boxed{
\begin{aligned}
\mathcal S(\rho,Y)
={}&
2R\int_{|y|>R}
\left(W\cdot\Sigma W-|\nabla W|^2\right)dy\\
&+
R\int_{|y|=R}
\left(U_r|W|^2-\partial_r|W|^2\right)dS.
\end{aligned}
}
\]

---

## 2. Invariant mean tail

Let `nu` be the nontrivial invariant ergodic measure from M5-531.

For every finite `rho`, define

\[
\boxed{
\overline{\mathfrak T}(\rho)
:=
\int_{\widehat{\mathfrak H}}
\mathfrak T(\rho,Y)d\nu(Y).
}
\]

Since

\[
0\le\mathfrak T(\rho,Y)
\le e^\rho Z_*,
\]

this quantity is finite for every fixed `rho`.

Likewise define

\[
\boxed{
\overline{\mathcal S}(\rho)
:=
\int\mathcal S(\rho,Y)d\nu(Y).
}
\]

All fixed-radius traces and derivatives are integrable because the M5-508 hull is globally smooth and compact in every fixed Sobolev order.

---

## 3. Invariance kills the time derivative

For fixed `rho`, the observable

\[
Y\mapsto\mathfrak T(\rho,Y)
\]

is bounded and continuous on the global `L2` compact hull.

For every `tau`, invariance gives

\[
\int
\mathfrak T(\rho,\phi^\tau Y)d\nu(Y)
=
\int
\mathfrak T(\rho,Y)d\nu(Y).
\]

Taking a difference quotient and using the uniform fixed-radius smooth bounds yields

\[
\boxed{
\int\partial_\theta\mathfrak T(\rho,Y)d\nu(Y)=0.
}
\]

Averaging the M5-530 transport equation therefore gives

\[
\boxed{
\frac12
\frac{d}{d\rho}
\overline{\mathfrak T}(\rho)
=
\overline{\mathcal S}(\rho).
}
\]

The identity may also be understood distributionally in `rho`, which is sufficient for all conclusions below.

---

## 4. Infinite log-radius occupation

M5-531 proved

\[
\mathcal M_1(Y)
=
\int_{-\infty}^{\infty}
\mathfrak T(\rho,Y)d\rho
=
\infty
\]

for `nu`-almost every hard-core state.

Because the integrand is nonnegative, Tonelli gives

\[
\begin{aligned}
\int_{-\infty}^{\infty}
\overline{\mathfrak T}(\rho)d\rho
&=
\int
\left[
\int_{-\infty}^{\infty}
\mathfrak T(\rho,Y)d\rho
\right]d\nu(Y)\\
&=
\infty.
\end{aligned}
\]

Hence

\[
\boxed{
\int^{\infty}
\overline{\mathfrak T}(\rho)d\rho
=
\infty
}
\]

on the remote side of the hard component.

The near-origin part is irrelevant for the present tail classification.

---

## 5. Exact radial dichotomy

There are now two fundamentally different possibilities.

### Branch A — unbounded mean critical tail

\[
\boxed{
\sup_{\rho\ge\rho_0}
\overline{\mathfrak T}(\rho)
=\infty.
}
\]

Then there exist radii `R_j -> infinity` and hull states with

\[
\boxed{
R_j
\int_{|y|>R_j}|W|^2dy
\to\infty.
}
\]

This is a genuinely strong critical exterior-enstrophy branch.

### Branch B — bounded but nonintegrable mean tail

Otherwise

\[
\boxed{
0\le
\overline{\mathfrak T}(\rho)
\le T_*<\infty
}
\]

for all sufficiently large `rho`, while

\[
\boxed{
\int^{\infty}\overline{\mathfrak T}(\rho)d\rho
=\infty.
}
\]

This is a diffuse critical occupation defect.

---

## 6. Bounded branch has bounded signed radial-source primitive

Integrate the averaged radial equation:

\[
\boxed{
\int_{\rho_0}^{\rho}
\overline{\mathcal S}(\eta)d\eta
=
\frac12
\left[
\overline{\mathfrak T}(\rho)
-
\overline{\mathfrak T}(\rho_0)
\right].
}
\]

On Branch B, the right side is uniformly bounded.

Therefore

\[
\boxed{
\sup_{\rho>\rho_0}
\left|
\int_{\rho_0}^{\rho}
\overline{\mathcal S}(\eta)d\eta
\right|
<\infty.
}
\]

Yet the occupancy satisfies

\[
\int^{\infty}
\overline{\mathfrak T}d\rho
=\infty.
\]

Thus the radial source/flux cannot have a persistent one-sign mean sufficient to empty or fill the tail monotonically.

It must cancel in signed cumulative balance.

---

## 7. Plateau versus diffuse-vanishing subbranches

The bounded branch can be sharpened without overclaiming.

### B1 — critical plateau recurrence

If

\[
\limsup_{\rho\to\infty}
\overline{\mathfrak T}(\rho)
\ge\tau_*>0,
\]

then arbitrarily remote radii carry a fixed mean critical exterior-enstrophy amount.

### B2 — diffuse subcritical-per-radius tail

If instead

\[
\overline{\mathfrak T}(\rho)
\to0,
\]

then the divergence

\[
\int^\infty\overline{\mathfrak T}d\rho=\infty
\]

must be genuinely diffuse, e.g. through a nonintegrable slow decay in log radius.

M5-532 does not exclude B2.

This is exactly the kind of branch that cannot be detected by a fixed critical lower bound on one shell.

---

## 8. Uniform unweighted tightness remains compatible

M5-508 gives

\[
\sup_Y
\int_{|y|>R}|W_Y|^2dy
\to0
\qquad(R\to\infty).
\]

This does not contradict either A or B because

\[
\mathfrak T(R,Y)
=R E_>(R,Y)
\]

contains the critical radial factor `R`.

Thus the current endpoint is precisely a failure of **weighted** uniform integrability while every unweighted Sobolev norm remains compact.

---

## 9. Source terms remain distinct

The averaged source is

\[
\overline{\mathcal S}
=
\overline{\mathcal S}_{stretch}
-
\overline{\mathcal S}_{pal}
+
\overline{\mathcal S}_{adv,bdy}
+
\overline{\mathcal S}_{diff,bdy}.
\]

Explicitly,

\[
\overline{\mathcal S}_{stretch}
=
2R\left\langle
\int_{|y|>R}W\cdot\Sigma W
\right\rangle,
\]

\[
\overline{\mathcal S}_{pal}
=
2R\left\langle
\int_{|y|>R}|\nabla W|^2
\right\rangle,
\]

and the two boundary terms are the averaged radial advective and diffusive enstrophy currents.

No cancellation among these channels may be assumed pointwise.

Only their signed total has the bounded primitive of Section 6.

---

## 10. DSD interpretation

The infinite first moment has now been converted from a static weighted defect into an invariant radial balance.

The bounded survivor is not merely

\[
\text{``mass exists very far away.''}
\]

It is

\[
\boxed{
\text{infinite log-radius critical occupation}
+
\text{bounded cumulative signed radial source}.
}
\]

This is structurally analogous to the earlier zero-mean material-flux and angle-cycling obstructions:

positive absolute activity can persist indefinitely while every signed primitive remains bounded by recurrence.

---

## 11. Highest-value next target

The next question is whether the infinite weighted tail can still be carried by coherent fixed-strength structures.

M5-508 already gives uniform high-Sobolev tail tightness. Therefore Sobolev embedding should imply

\[
\sup_{Y}
\sup_{|y|>R}|\nabla^jW_Y(y)|
\to0
\]

for every fixed derivative order `j`.

If so, the infinite first moment is necessarily carried by a **vanishing-amplitude diffuse tail**, not by repeated fixed-amplitude remote coherent packets.

That would separate the finite persistent flux-lineage core from a low-amplitude radial dust reservoir and allow a quantitative nonlocal-decoupling estimate for its strain contribution to the core.

---

## 12. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
