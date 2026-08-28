# DSD M5-189 — Whole-Space Polynomial-Weight Route and Exact Type-I Criticality Audit

Date: 2026-08-28

Status: **P1_B PRESSURE-COMPATIBLE ROUTE / THE LEI--YANG--YUAN WHOLE-SPACE POLYNOMIAL-WEIGHT METHOD IS STRUCTURALLY MATCHED TO THE RELATIVE NAVIER--STOKES EQUATION BECAUSE IT RETAINS THE LERAY/CALDERÓN--ZYGMUND OPERATOR, BUT THE W1 BACKGROUND IS EXACTLY SCALE-CRITICAL: `sqrt(tau)|U|` AND `tau|nabla U|` ARE O(1), SO SHORTENING THE TERMINAL TIME WINDOW DOES NOT MAKE THE CONTROL SMALL / DIVERGENCE-FREE TRANSPORT REMAINS SKEW AT LEADING ORDER, WHILE THE STRETCHING CHANNEL IS A CRITICAL INVERSE-SQUARE FORM / DIRECT BOUNDED-MILD THEOREM INSERTION IS RED, A CRITICAL FORM ESTIMATE IS THE NEXT INTERNAL GATE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Reverse-time whole-space equation

Set

\[
\tau:=T_*-t.
\]

Let `U_1,U_2` be the two physical W1 realizations and

\[
W:=U_1-U_2.
\]

After reverse time, the exact relative equation has the form

\[
\boxed{
\partial_\tau W
+\nu\Delta W
+\mathbb P\nabla\cdot
\bigl(U_1\otimes W+W\otimes U_2\bigr)=0,
\qquad \nabla\cdot W=0.
}
\]

This formulation retains pressure through the whole-space Leray projection and therefore avoids an artificial exterior boundary.

---

## 2. Exact Type-I coefficient class

Use

\[
\rho^2:=|x-x_*|^2+\tau.
\]

The W1 Type-I realization gives

\[
\boxed{
|U_i(x,\tau)|\le C\rho^{-1},
\qquad
|\nabla U_i(x,\tau)|\le C\rho^{-2}.
}
\]

Consequently

\[
\boxed{
\sqrt\tau\,|U_i|\le C,
\qquad
\tau|\nabla U_i|\le C.
}
\]

These are dimensionless scale-invariant quantities.

Parabolic rescaling of a terminal window therefore leaves the coefficient size unchanged.

Hence

\[
\boxed{
\text{short terminal window}
\not\Rightarrow
\text{small Oseen coefficient}.
}
\]

This is a permanent firewall.

---

## 3. Why the Lei--Yang--Yuan architecture is still relevant

The recent whole-space backward-uniqueness proof for bounded mild 3D Navier--Stokes solutions uses a time-singular weight and a polynomial spatial weight,

\[
h(\tau)^{-2a}(1+|x|^2)^{-k},
\]

rather than an exponential spatial Carleman weight.

This is specifically designed to keep Calderón--Zygmund/Leray terms inside a weighted `L^2` estimate.

That is structurally the same obstruction present here:

\[
\mathbb P\nabla\cdot(U_1\otimes W+W\otimes U_2).
\]

Thus the architecture is relevant even though its published bounded-mild theorem is not directly applicable.

---

## 4. Direct theorem insertion is not allowed

The bounded-mild theorem assumes, schematically,

\[
\|U_i\|_{L^\infty_{x,t}}<\infty
\]

and bounded vorticity on the entire whole-space cylinder.

The present physical W1 realization allows

\[
|U_i(x,\tau)|\sim \rho^{-1},
\]

and therefore

\[
\sup_x|U_i(x,\tau)|\sim \tau^{-1/2}
\]

as `tau downarrow 0`.

Hence

\[
\boxed{
\text{Lei--Yang--Yuan theorem}
\not\Rightarrow
P1_B=0
}
\]

without a new critical-coefficient extension.

Status: RED as a direct insertion.

---

## 5. Leading transport is not the true coercivity loss

Expand the projected relative nonlinearity before applying the projector:

\[
(U_1\cdot\nabla)W+(W\cdot\nabla)U_2.
\]

Because

\[
\nabla\cdot U_1=0,
\]

the first term is skew in the unweighted `L^2` energy:

\[
\boxed{
\int W\cdot(U_1\cdot\nabla W)\,dx=0.
}
\]

Thus the scale-critical first-order amplitude `rho^-1` does not by itself create an unweighted energy loss.

With a polynomial radial weight `w_k(x)`, the defect is only the weight commutator:

\[
\int w_k W\cdot(U_1\cdot\nabla W)
=-\frac12\int |W|^2U_1\cdot\nabla w_k.
\]

Since

\[
|\nabla\log w_k|\lesssim \frac1{1+r},
\]

and

\[
|U_1|\lesssim \rho^{-1},
\]

this defect is of potential order rather than full first-derivative order.

So the true critical channel is the inverse-square form.

---

## 6. Stretching is exactly a Hardy-critical form

The second Oseen term obeys

\[
\left|
\int W^T(\nabla U_2)W\,dx
\right|
\le
C\int\rho^{-2}|W|^2dx.
\]

Since

\[
\rho^{-2}\le |x-x_*|^{-2}
\]

away from the center in the limiting sense, the three-dimensional Hardy inequality gives

\[
\boxed{
\int\frac{|W|^2}{|x-x_*|^2}\,dx
\le4\int|\nabla W|^2dx.
}
\]

Therefore the stretching channel has precisely the same differential order as viscosity in the quadratic form.

This explains why:

- it is not subcritical;
- shortening time does not make it small;
- ordinary energy gives coercivity only under a small-amplitude Hardy threshold;
- a general large-background proof needs genuine critical Carleman/log-convexity structure rather than Grönwall.

---

## 7. Small-Hardy subbranch

If one had the quantitative strain bound

\[
|S_{U_2}(x,\tau)|\le C_*\rho^{-2}
\]

with

\[
4C_*<\nu,
\]

then the unweighted relative energy identity yields

\[
\frac12\frac d{dt}\|W\|_2^2
+(\nu-4C_*)\|\nabla W\|_2^2\le0.
\]

This identifies a genuinely easier small-Hardy subbranch.

However W1 imposes no such smallness.

Thus the large-Hardy branch remains the real endpoint.

The smallness condition is recorded only as a conditional pruning, not as a W1 theorem.

---

## 8. What a successful critical polynomial-weight estimate must prove

A useful extension of the whole-space weighted method must exploit three structures simultaneously:

1. divergence-free skewness of `U_1 dot nabla`;
2. Hardy-critical control of `nabla U_2`;
3. divergence structure inside `P nabla dot`, so that the polynomial Calderón--Zygmund estimate loses at most one derivative.

The required schematic estimate is not

\[
\|U_i\|_\infty\ll1.
\]

It is instead a form estimate of the type

\[
\boxed{
|\mathfrak B_{U}(W,W)|
\le
\varepsilon\,\mathfrak C_a(W)
+C_{\varepsilon,U}\,\mathfrak L_a(W),
}
\]

where

- `mathfrak C_a` is the positive large-Carleman-parameter part;
- `mathfrak L_a` is a lower weighted `L^2` term already controlled by the time singularity;
- the coefficient `C_{epsilon,U}` may depend on the finite W1 Type-I amplitude but must not require smallness.

This is the exact next analytic gate.

---

## 9. DSD audit

### Formation — GREEN

The reverse-time relative equation is exact and whole-space; no artificial boundary is introduced.

### Axis — GREEN

Velocity amplitude, strain amplitude, temporal distance, and spatial distance are kept distinct through `rho`.

### Static aggregation — GREEN

The dimensionless Type-I coefficient is not incorrectly made small by choosing a shorter time interval.

### Dynamics — GREEN / OPEN CRITICAL FORM

Transport skewness and Hardy order are GREEN.  Pressure-compatible arbitrary-amplitude critical absorption remains OPEN.

### Cross-audit — GREEN

This node does not claim that Hardy's inequality alone proves backward uniqueness and does not import a bounded-mild theorem into an unbounded Type-I class.

---

## 10. Updated first large gate

The first remaining large gate can now be stated sharply:

\[
\boxed{
\text{prove a polynomial-weight backward estimate for the relative whole-space Oseen--Stokes equation}
}
\]

under

\[
\boxed{
|U|\lesssim\rho^{-1},
\qquad
|\nabla U|\lesssim\rho^{-2},
}
\]

with no smallness assumption on the finite Type-I amplitude.

If this succeeds, the entire flat same-tail fiber is removed directly, without the statistical/proximal split.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
