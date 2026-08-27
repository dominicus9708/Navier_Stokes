# DSD M5-128 — Same-Tail Fiber Relative Energy and the Large Weak-L3 Boundary

Date: 2026-08-27

Status: **EXACT RELATIVE L2 LEDGER DERIVED FOR TWO W1 STATES WITH THE SAME CANONICAL TAIL / COMMON TAIL CUTOFF IS A HARMLESS BOUNDED COEFFICIENT AND STRONG-L3 QUOTIENT PART IS UNIFORMLY INFINITESIMALLY FORM-BOUNDED / TERMINAL PHYSICAL L2 COLLAPSE STILL DOES NOT FORCE FIBER UNIQUENESS BECAUSE THE SIMILARITY-TIME GRONWALL COEFFICIENT IS CRITICAL / CURRENT WHOLE-TIME WEAK-L3 UNIQUENESS THEOREMS REQUIRE SMALLNESS OR RELATED EXTRA CONDITIONS NOT AVAILABLE FOR A GENERAL LARGE CANONICAL TAIL / GLOBAL REGULARITY UNPROVED.**

---

## 1. Same-tail pair

Let

\[
V_1,V_2\in M
\]

satisfy

\[
\boxed{T_{V_1}=T_{V_2}=:T.}
\]

Factor equivariance preserves the same-tail relation for all forward W1 times.

Let

\[
\boxed{Z:=V_1-V_2.}
\]

M5-115 gives

\[
Z\in L^2\cap L^3.
\]

Choose one fixed canonical cutoff radius `R0` and write

\[
V_i=B_T+Q_i,
\]

where the same divergence-free cutoff background `B_T` is used for both states and

\[
Q_i\in L^2\cap L^3.
\]

Then

\[
Z=Q_1-Q_2.
\]

---

## 2. Exact relative Leray equation

Define

\[
\overline V:=\frac12(V_1+V_2).
\]

Because

\[
V_1\otimes V_1-V_2\otimes V_2
=Z\otimes\overline V+\overline V\otimes Z,
\]

the difference satisfies

\[
\boxed{
\partial_sZ
-\nu\Delta Z
+\frac12Z
+\frac12Y\cdot\nabla Z
+\mathbb P\nabla\cdot
(Z\otimes\overline V+\overline V\otimes Z)
=0.
}
\]

The common canonical-tail forcing cancels exactly.  This is the correct P1 relative equation.

---

## 3. Exact relative `L2` ledger

Take the `L2` pairing with `Z`.

The divergence-free transport term

\[
\overline V\cdot\nabla Z
\]

has zero energy contribution.

The Leray linear drift gives

\[
-\frac14\|Z\|_2^2
\]

on the left-hand side.

Thus

\[
\boxed{
\frac12\frac d{ds}\|Z\|_2^2
+\nu\|\nabla Z\|_2^2
-\frac14\|Z\|_2^2
=
-\int Z^TS_{\overline V}Z\,dY,
}
\]

where

\[
S_{\overline V}
=\frac12(\nabla\overline V+\nabla\overline V^T).
\]

This identity is exact.

---

## 4. Split common background and strong quotient

Write

\[
\overline V
=B_T+\overline Q,
\qquad
\overline Q:=\frac12(Q_1+Q_2).
\]

Then

\[
\int Z^TS_{\overline V}Z
=
\int Z^TS_{B_T}Z
+
\int Z^TS_{\overline Q}Z.
\]

These two terms have different mathematical character and must be audited separately.

---

## 5. Common cutoff-tail term

For one fixed large cutoff radius, `B_T` is smooth and bounded globally because it vanishes near the origin and equals the critical tail only in the exterior.

The canonical shell derivative bounds give

\[
\boxed{
\|S_{B_T}\|_\infty
\le C_{R_0},
}
\]

and in the exterior/transition scaling one has schematically

\[
C_{R_0}=O(R_0^{-2})
\]

up to fixed cutoff constants.

Therefore

\[
\boxed{
\left|
\int Z^TS_{B_T}Z
\right|
\le C_{R_0}\|Z\|_2^2.
}
\]

The common canonical tail does not create a singular coefficient in the normalized relative-energy equation once the same cutoff is used on both states.

---

## 6. Strong-L3 quotient term is infinitesimally form-bounded

The family of quotient states on the compact W1 class is precompact in strong `L3` for fixed cutoff radius.

Hence it is uniformly equiintegrable in `L3`.

Given any `epsilon>0`, choose an amplitude truncation level `M_epsilon` uniformly over the compact quotient class and split

\[
\overline Q
=\overline Q_{lo}+\overline Q_{hi}
\]

such that

\[
\|\overline Q_{lo}\|_\infty\le M_\varepsilon
\]

and

\[
\|\overline Q_{hi}\|_3\le\delta_\varepsilon
\]

with `delta_epsilon` as small as required.

Integrating by parts,

\[
\left|
\int Z^TS_{\overline Q}Z
\right|
\lesssim
\int|\overline Q||Z||\nabla Z|.
\]

For the high part, Sobolev gives

\[
\int|\overline Q_{hi}||Z||\nabla Z|
\le
C\|\overline Q_{hi}\|_3
\|Z\|_6
\|\nabla Z\|_2
\le
C\delta_\varepsilon\|\nabla Z\|_2^2.
\]

For the bounded part,

\[
\int|\overline Q_{lo}||Z||\nabla Z|
\le
M_\varepsilon\|Z\|_2\|\nabla Z\|_2
\le
\varepsilon\|\nabla Z\|_2^2
+C_\varepsilon\|Z\|_2^2.
\]

Therefore, uniformly on the compact same-tail fiber class,

\[
\boxed{
\left|
\int Z^TS_{\overline Q}Z
\right|
\le
\varepsilon\|\nabla Z\|_2^2
+C_\varepsilon\|Z\|_2^2.
}
\]

This is the exact strong-critical advantage of the same-tail fiber.

---

## 7. Relative Gronwall inequality

Choose `epsilon<nu/2`.  The exact energy identity yields

\[
\boxed{
\frac12\frac d{ds}\|Z\|_2^2
+(\nu-\varepsilon)\|\nabla Z\|_2^2
\le
\left(
\frac14+C_{R_0}+C_\varepsilon
\right)\|Z\|_2^2.
}
\]

Thus forward uniqueness from a finite normalized time is standard:

\[
Z(s_0)=0\Longrightarrow Z\equiv0\quad(s\ge s_0).
\]

But this is not the P1 problem.  Distinct same-tail states have no finite time at which their normalized difference is known to vanish.

---

## 8. Why physical terminal `L2` collapse does not supply that initial zero

Under inverse Leray scaling,

\[
z(x,t)
=(T_*-t)^{-1/2}
Z\left(\frac{x-x_*}{\sqrt{T_*-t}},s\right).
\]

Hence

\[
\boxed{
\|z(t)\|_2^2
=(T_*-t)^{1/2}\|Z(s)\|_2^2.
}
\]

Because the normalized fiber orbit is compact in `L2`, the right-hand side tends to zero even when `Z(s)` remains order one and recurrent.

Thus

\[
\boxed{
\|z(t)\|_2\to0
\quad\not\Rightarrow\quad
\|Z(s)\|_2\to0.
}
\]

In physical time, the normalized Gronwall coefficient transforms with

\[
\frac{ds}{dt}=\frac1{T_*-t},
\]

so a bounded coefficient in `s` becomes a critical nonintegrable coefficient of order

\[
(T_*-t)^{-1}
\]

near the terminal point.

Therefore terminal zero in physical `L2` cannot be propagated backward by the ordinary Gronwall argument.

---

## 9. Literature boundary audit

The current whole-time/half-line weak-`L3` uniqueness theory does not automatically close this branch.

Y. Taniuchi, *On uniqueness of mild L^{3,infinity}-solutions on the whole time axis to the Navier--Stokes equations in unbounded domains*, Math. Ann. 389 (2024), 2561--2594, DOI `10.1007/s00208-023-02702-x`, treats uniqueness under conditions that include a sufficiently small weak-`L3` solution, with precompact-range or spatial-decay assumptions on the comparison solution in the relevant variants.

Earlier whole-time results cited there likewise use smallness of at least one solution in the critical weak space.

Our W1 survivor may have a genuinely large canonical weak-`L3` background.  Same-tail cancellation makes the **difference** strong `L3`, but neither original physical solution is known to be small in weak `L3`.

Therefore these theorems cannot be invoked merely from

\[
Z\in L^2\cap L^3.
\]

This is a scope boundary, not a contradiction with the literature.

---

## 10. DSD four-chain audit

### Formation — GREEN

The same-tail relation is formed before the common background is canceled.

### Axis — GREEN

Common tail, strong quotient, and relative difference are separate channels.

### Static aggregation — GREEN

The common forcing cancels exactly; no tail forcing is counted in the relative equation.

### Dynamics — GREEN

The relative energy inequality is derived before using terminal scaling.

### Cross-audit — GREEN

Physical terminal `L2` collapse is not fed backward as normalized-time equality.

---

## 11. Updated P1 frontier

The P1 fiber is now reduced to a precise large-critical-background uniqueness problem:

\[
\boxed{
\begin{array}{c}
\text{same canonical tail}\\
+\text{ strong }L^2\cap L^3\text{ difference}\\
+\text{ compact normalized recurrence}\\
+\text{ physical terminal }L^2\text{ collapse}\\
+\text{ critical }(T_*-t)^{-1}\text{ relative coefficient}
\end{array}
}
\]

Existing small-background uniqueness does not remove it.

A successful next P1 step would need one of:

1. a new large-background relative backward-uniqueness theorem exploiting the **shared canonical tail** rather than smallness;
2. a dynamical argument that compact recurrent strong-L3 fibers cannot coexist with the parabolic frequency escape of M5-116;
3. a sign/coercivity property of the common canonical-tail strain beyond the generic weak-L3 form bound.

No such closure is presently proved.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
