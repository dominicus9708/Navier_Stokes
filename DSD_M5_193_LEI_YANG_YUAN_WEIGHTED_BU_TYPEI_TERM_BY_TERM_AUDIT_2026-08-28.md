# DSD M5-193 — Lei–Yang–Yuan Weighted Backward-Uniqueness: Type-I Term-by-Term Audit

Date: 2026-08-28

Status: **P1_B BACKWARD-WEIGHT REFINEMENT / THE 2024 LEI–YANG–YUAN POLYNOMIAL-SPATIAL/TIME-SINGULAR ESTIMATE IS PRESSURE-COMPATIBLE THROUGH A WEIGHTED CALDERON–ZYGMUND LEMMA, BUT THEIR PUBLISHED ABSORPTION USES GLOBAL BOUNDED VELOCITY/VORTICITY AND A SMALL TIME INTERVAL; FOR THE W1 TYPE-I CLASS THE STRETCHING-SQUARED CHANNEL CAN BE REFACTORED BY A CRITICAL L3–GAGLIARDO–NIRENBERG ESTIMATE INTO EPSILON GRADIENT PLUS `a/t` ZERO-ORDER COERCIVITY, WHILE THE TRANSPORT-SQUARED CHANNEL REMAINS NONSMALL; THEREFORE THE ONLY PRINCIPAL OBSTRUCTION IS TO INCORPORATE THE LARGE DIVERGENCE-FREE TRANSPORT INTO THE CARLEMAN OPERATOR RATHER THAN SQUARE IT AS A FORCING / GLOBAL REGULARITY UNPROVED.**

---

## 1. External weighted estimate

After reversing time, Lei–Yang–Yuan use a weighted estimate of the form

\[
\int h(t)^{-(2a+1)}(1+|x|^2)^{-k}
\bigl((a+1)|Z|^2+|\nabla Z|^2\bigr)
\lesssim
\int h(t)^{-2a}(1+|x|^2)^{-k}|(\partial_t+\Delta)Z|^2,
\]

where

\[
h(t)=te^{-t}.
\]

Their pressure/Leray term is handled by a weighted Calderon–Zygmund estimate valid for `k<5/2` despite the polynomial weight falling outside the ordinary `A_p` class for part of this range.

This is structurally ideal for the NSE difference.

---

## 2. Where boundedness enters their proof

For bounded mild solutions they obtain, schematically,

\[
A
\lesssim
\bigl(
\|u_1\|_\infty^2+\|\omega_1\|_\infty^2
+
\|u_2\|_\infty^2+\|\omega_2\|_\infty^2
\bigr)
\int h^{-2a}w_k(|Z|^2+|\nabla Z|^2).
\]

Since

\[
h^{-2a}=h\,h^{-(2a+1)},
\]

they bound `h<=T_+` and choose the time interval so that

\[
T_+ C_{bounded}\ll1.
\]

For W1 Type-I physical realizations the spacetime sup norms blow at the terminal center, so this published absorption cannot be reused verbatim.

---

## 3. W1 Type-I coefficient profile after time reversal

Let reverse time be

\[
t=T_*-t_{physical}>0.
\]

The W1 coefficient envelope is

\[
\boxed{
|u_i(x,t)|\le \frac{C_0}{(r^2+t)^{1/2}},
\qquad
|\nabla u_i|+|\omega_i|\le \frac{C_1}{r^2+t},
}
\]

with `r=|x-x_*|`.

Thus

\[
t|u_i|^2\le C_0^2,
\]

but

\[
t|\nabla u_i|^2
\le
C_1^2\frac{t}{(r^2+t)^2}.
\]

The latter is unbounded pointwise as `t->0` at the center.

---

## 4. Stretching-squared channel is form-subcritical relative to the full Carleman pair

Define

\[
V_t(x):=\frac{t}{(r^2+t)^2}.
\]

In three dimensions,

\[
\boxed{
\|V_t\|_{L^3_x}\asymp t^{-1/2}.
}
\]

For an unweighted test field `F`, Hölder and Gagliardo–Nirenberg give

\[
\int V_t|F|^2
\le
\|V_t\|_3\|F\|_3^2
\lesssim
 t^{-1/2}\|F\|_2\|F\|_6
\lesssim
 t^{-1/2}\|F\|_2\|\nabla F\|_2.
\]

Hence for every `epsilon>0`,

\[
\boxed{
\int V_t|F|^2
\le
\epsilon\|\nabla F\|_2^2
+C_\epsilon t^{-1}\|F\|_2^2.
}
\]

For the slowly varying polynomial spatial weight `w_k=(1+|x|^2)^{-k}`, the same estimate survives after conjugating `F=w_k^{1/2}Z`; the weight derivative produces only bounded lower-order terms because

\[
|\nabla\log w_k|\lesssim1.
\]

Therefore the Type-I terms arising from

\[
|\nabla u_i|^2|Z|^2
\quad\text{or}\quad
|\omega_i|^2|Z|^2
\]

can be split into

\[
\epsilon\,h^{-(2a+1)}w_k|\nabla Z|^2
+
C_\epsilon\,h^{-(2a+1)}w_k|Z|^2,
\]

where the second term is absorbed by `(a+1)|Z|^2` once the Carleman parameter is chosen sufficiently large.

Thus **arbitrary finite Type-I stretching amplitude does not by itself obstruct the weighted estimate.**

---

## 5. Transport-squared channel remains critical

The direct RHS-square treatment of

\[
(u_i\cdot\nabla)Z
\]

gives

\[
\int h^{-2a}w_k|u_i|^2|\nabla Z|^2
=
\int h^{-(2a+1)}w_k
\bigl(h|u_i|^2\bigr)|\nabla Z|^2.
\]

Since

\[
\boxed{h|u_i|^2\lesssim C_0^2}
\]

but is not known small, this is only a finite multiple of the **same gradient coercive term**.

The Carleman parameter multiplies the zero-order term, not the gradient term in the published weighted estimate.

Therefore one cannot absorb an arbitrary large `C_0` by increasing `a` after first squaring the drift.

This is a genuine critical obstruction.

---

## 6. Divergence-free algebra shows why squaring is wasteful

For the actual NSE drift,

\[
\nabla\cdot u_i=0.
\]

M5-188 already showed that under scalar conjugation the leading transport

\[
u_i\cdot\nabla
\]

is skew in the unweighted conjugated energy, up to commutators with the spatial weight.

For the polynomial factor,

\[
\operatorname{Re}\int w_k(u_i\cdot\nabla Z)\cdot Z
=
-\frac12\int (u_i\cdot\nabla w_k)|Z|^2,
\]

and

\[
|u_i\cdot\nabla\log w_k|
\lesssim
\frac{r}{(1+r^2)(r^2+t)^{1/2}}
\le C.
\]

Thus **at the first-order energy level**, the large Type-I transport creates only a bounded zeroth-order weight commutator, not a critical gradient cost.

The obstruction in Section 5 is therefore an artifact of treating the transport as an external forcing and squaring it before exploiting divergence-free skewness.

---

## 7. Refined target operator

The correct next Carleman target is not

\[
L_0=\partial_t+\Delta
\]

with `u_i·nabla Z` on the right.

It is the drift-inclusive operator

\[
\boxed{
L_b Z:=\partial_tZ+\Delta Z+b\cdot\nabla Z
}
\]

with

\[
\nabla\cdot b=0,
\qquad
|b|\lesssim(r^2+t)^{-1/2}.
\]

One must re-run the weighted commutator estimate with `b·nabla` placed in the skew component before taking norms.

The expected new lower-order commutators involve `nabla b`, which has critical inverse-square size and must be treated together with the already-audited stretching potential.

---

## 8. Pressure/Leray channel

Lei–Yang–Yuan Lemma 4.1 shows that polynomial spatial weights permit direct treatment of

\[
R\nabla\cdot f,
\qquad
R=\nabla(-\Delta)^{-1}\nabla\cdot,
\]

through

\[
\boxed{
\int w_k|R\nabla\cdot f|^2
\lesssim
\int w_k(|\nabla f|^2+|f|^2),
\qquad 0\le k<5/2.
}
\]

Therefore the pressure nonlocality itself is no longer the primary unknown.

The open issue is whether the drift-inclusive commutator can be combined with this weighted Calderon–Zygmund estimate **without re-squaring the critical transport derivative**.

---

## 9. DSD audit

### Formation — GREEN

The coefficient profile and all perturbation terms come from the physical W1 relative equation.

### Axis — GREEN

Transport, stretching, pressure, and Carleman zero/gradient coercivities are separated.

### Static aggregation — GREEN

The Type-I drift is not declared small merely because the time interval is short.

### Dynamics — GREEN for stretching form bound / YELLOW for drift-inclusive weighted Carleman

The only remaining principal absorption problem is large divergence-free transport.

### Cross-audit — GREEN

This avoids both invalid shortcuts: bounded-mild theorem insertion and generic gradient-potential smallness.

---

## 10. Next calculation

Re-derive the Lei–Yang–Yuan weighted commutator for

\[
\partial_t+\Delta+b\cdot\nabla
\]

with divergence-free Type-I `b`, and identify the exact `nabla b` commutators.  Test whether they reduce, after integration by parts, to the same form-subcritical potential class handled in Section 4.

If yes, the remaining Leray/stretching terms can be reinserted and the terminal time weight may close the W1 flat fiber.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
