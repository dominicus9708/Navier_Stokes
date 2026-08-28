# DSD M5-185 — Type-I Critical Oseen–Stokes Hardy–Carleman Target — CORRECTED

Date: 2026-08-28

Status: **W1-CONDITIONAL / THE SAME-TAIL PHYSICAL DIFFERENCE HAS THE EXACT SCALE-CRITICAL COEFFICIENT CLASS `|a|~rho^-1`, `|B|~rho^-2`, BUT DIFFERENTIAL-ORDER MATCHING DOES NOT IMPLY ARBITRARY-AMPLITUDE BACKWARD ABSORPTION / A TERMINAL `1/tau` POTENTIAL CAN ITSELF SUPPORT NONZERO TERMINAL-ZERO SOLUTIONS / ANY VALID CARLEMAN MUST USE ADDITIONAL DIVERGENCE-FREE, STOKES, CANONICAL-TAIL, SIGN, OR SPECTRAL STRUCTURE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Physical coefficient class

Let

\[
\vartheta:=T_*-t,
\qquad
r:=|x-x_*|,
\qquad
\rho:=(r^2+\vartheta)^{1/2}.
\]

The compact W1 Type-I class gives

\[
\boxed{|u(x,t)|\le C\rho^{-1}},
\qquad
\boxed{|\nabla u(x,t)|+|\omega(x,t)|\le C\rho^{-2}}.
\]

For the same-tail difference `Z=u^V-u^W`,

\[
\partial_t Z-\nu\Delta Z+a\cdot\nabla Z+BZ+\nabla q=0,
\qquad \nabla\cdot Z=0,
\]

with

\[
\boxed{|a|\le C\rho^{-1},\qquad |B|\le C\rho^{-2}}.
\]

This coefficient class is exactly parabolically scale-critical.

---

## 2. Terminal flatness

M5-145/M5-181 give, for every fixed `x != x_*`,

\[
\boxed{\partial_t^mZ(x,T_*)=0\qquad\forall m<\infty.}
\]

At the Fuchsian level the same-tail difference is flat to every algebraic normal order.

---

## 3. Differential-order audit remains GREEN

The lower terms satisfy

\[
|a\cdot\nabla Z|^2\lesssim\rho^{-2}|\nabla Z|^2,
\]

\[
|BZ|^2\lesssim\rho^{-4}|Z|^2.
\]

Thus the drift and stretching sit exactly at the critical derivative orders expected in a Hardy/Carleman estimate.

What is **not** valid is the former inference that a sufficiently large Carleman parameter must absorb an arbitrary finite coefficient amplitude.

---

## 4. Terminal-critical ODE firewall

Consider reverse time `tau=T_*-t` and the scalar equation

\[
\boxed{\partial_\tau f-\frac c\tau f=0,\qquad c>0.}
\]

It has

\[
\boxed{f(\tau)=C\tau^c},
\]

so

\[
f(0)=0
\]

while `f` is not identically zero.

At the Type-I center,

\[
\rho^{-2}\sim\tau^{-1}.
\]

Hence an arbitrary signed terminal-critical zeroth-order coefficient can generate a genuine terminal-zero branch.

Therefore

\[
\boxed{
|B|\lesssim\rho^{-2}
+\text{large Carleman parameter}
\not\Rightarrow
\text{backward uniqueness at arbitrary amplitude}.
}
\]

This is a permanent RED firewall.

---

## 5. Spatial inverse-square theorems do not remove this firewall

Strong unique continuation for spatial inverse-square potentials concerns a different mechanism.

Here the same parabolic coefficient becomes a **terminal time singularity** `~1/tau` at the center.

Thus spatial Hardy control and terminal backward injectivity must not be identified.

---

## 6. Corrected Stokes-Carleman target

A pressure-compatible estimate may still contain weighted critical coercivities such as

\[
s\int e^{2s\Phi}\rho^{-2}|\nabla v|^2
+s^3\int e^{2s\Phi}\rho^{-4}|v|^2,
\]

but a valid proof must contain an additional mechanism excluding the ODE-type critical mode.

Legitimate candidates are:

1. divergence-free transport skewness;
2. a canonical-tail adapted symmetrizer;
3. a spectral/log-convexity gap for the full common-tail operator;
4. Stokes pressure/divergence structure;
5. a genuinely small Hardy subbranch.

No one of these is assumed by coefficient order alone.

---

## 7. Pressure is not the sole obstruction

M5-190 shows that for the finite-energy same-tail difference the Leray projection is harmless at the `L2/H^-1` form level and the strong-`L3` quotient is infinitesimally form-bounded.

The non-small obstruction is the common canonical-tail stretching form.

Thus the earlier statement that pressure was the only theorem-level issue is withdrawn.

---

## 8. Corrected first large target

The remaining analytic problem is

\[
\boxed{
\text{backward injectivity for the finite-energy common-tail Oseen operator at actual W1 critical amplitude},
}
\]

with the strong-`L3` quotient treated perturbatively.

A generic arbitrary-amplitude `rho^-2` backward-uniqueness theorem would be false without additional hypotheses.

---

## 9. DSD audit

### Formation — GREEN

The Type-I coefficient class is derived from actual W1 scaling.

### Axis — GREEN

Spatial inverse-square order and terminal `1/tau` singularity are distinguished.

### Static aggregation — CORRECTED

Critical differential order is no longer converted into automatic arbitrary-amplitude absorption.

### Dynamics — YELLOW

Backward injectivity of the actual canonical-tail principal operator remains open.

### Cross-audit — GREEN

This correction is consistent with M5-190/M5-191 and prevents importing spatial Hardy or bounded-coefficient backward uniqueness into the terminal-critical class.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
