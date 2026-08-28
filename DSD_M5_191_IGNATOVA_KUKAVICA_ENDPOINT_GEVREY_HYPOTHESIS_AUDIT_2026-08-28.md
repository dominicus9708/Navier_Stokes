# DSD M5-191 — Ignatova–Kukavica Endpoint/Gevrey Hypothesis Audit

Date: 2026-08-28

Status: **EXTERNAL THEOREM BRIDGE AUDIT / IGNATOVA–KUKAVICA 2013 DIRECTLY TREATS DIFFERENCES OF TWO NAVIER–STOKES SOLUTIONS THROUGH A MATCHED ELLIPTIC–PARABOLIC CARLEMAN SYSTEM, BUT ITS MAIN STRONG-UC THEOREM IS A FIXED-INTERIOR-TIME RESULT ON A TWO-SIDED TIME CYLINDER AND REQUIRES GEVERY CONTROL `sigma <= 1+eta` TO CONVERT QUANTITATIVE PROPAGATION INTO FINITE VANISHING ORDER / THE W1 SAME-TAIL PAIR IS TERMINAL-ONE-SIDED AND ONLY C-INFINITY TERMINAL FLATNESS IS CURRENTLY PROVED; DIRECT THEOREM INSERTION IS RED/YELLOW / THE MATCHED CARLEMAN ARCHITECTURE REMAINS REUSABLE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Exact theorem setting

Ignatova–Kukavica consider two solutions `(u1,p1)` and `(u2,p2)` of 3D NSE with the same Gevrey forcing on

\[
B_2\times[t_0-\delta^2,t_0+\delta^2].
\]

They assume two-sided Gevrey derivative bounds for each solution,

\[
\|\partial_t^m\partial_x^\alpha u_j(\cdot,t)\|_{L^\infty(B_2)}
\le
\frac{M_j m!^\sigma |\alpha|!^\sigma}
{\delta_0^{2m+|\alpha|}},
\qquad
 t_0-\delta^2\le t\le t_0+\delta^2,
\]

and analogous normalized Gevrey control for the difference `v=u1-u2` and pressure difference `p=p1-p2`.

They also assume a doubling property comparing `L2(B2)` and `L2(B1)` norms uniformly across the same time cylinder.

---

## 2. Coupled system exactly matches the NSE difference structure

The difference obeys

\[
\partial_t v-\Delta v+u_1\cdot\nabla v+v\cdot\nabla u_2+\nabla p=0,
\]

and pressure obeys the elliptic equation

\[
-\Delta p
-\partial_j u_{1i}\,\partial_i v_j
-\partial_i u_{2j}\,\partial_j v_i
=0.
\]

This is the same pressure-compatible elliptic–parabolic architecture sought in M5-183/M5-185.

Thus the paper is structurally relevant even though its theorem cannot yet be inserted directly.

---

## 3. Theorem 2.1 is quantitative fixed-time propagation, not terminal backward uniqueness

Under hypotheses (2.1)–(2.4), their Theorem 2.1 gives a quantitative propagation estimate at each time in the cylinder, schematically

\[
\|v(\cdot,t)\|_{L^2(B_2)}
\le
\exp(P)\,
\|v(\cdot,t)\|_{L^\infty(B_{4\delta})}.
\]

This is a spatial propagation/doubling statement.

It does **not** say that

\[
v(\cdot,T_*)=0
\Longrightarrow
v(\cdot,t)=0\quad(t<T_*).
\]

Therefore Theorem 2.1 cannot replace the missing backward-time step.

---

## 4. Theorem 2.2 has an additional Gevrey threshold

The strong unique continuation conclusion at fixed time requires

\[
\boxed{\sigma\le1+\eta}
\]

for a universal `eta>0`.

The paper explicitly remarks that generic *local* Gevrey regularity in time for NSE/heat is at most `G^2`, even for analytic forcing.  Boundary-value solutions can inherit stronger forcing regularity, but that is a distinct global/boundary-value input.

Thus the implication

\[
\text{smooth exterior W1 solution}
\Rightarrow
\sigma\le1+\eta
\]

is **not available**.

---

## 5. W1 data at the terminal endpoint

For every exterior point `x0 != x_*`, choose a ball

\[
B_{2r_0}(x_0)\Subset\mathbb R^3\setminus\{x_*\}.
\]

M5-145 and the physical Fuchsian relation imply

\[
\boxed{
\partial_t^m Z(x,T_*)=0
\quad\forall m\ge0,
\quad x\in B_{2r_0}(x_0),
}
\]

where `Z=u^V-u^W`.

The two physical realizations are smooth up to `T_*` on this exterior ball from the left.

What is **not** proved is:

1. a solution extension to `t>T_*` satisfying NSE on the same ball;
2. a two-sided uniform Gevrey radius around `T_*`;
3. the threshold `sigma<=1+eta`;
4. the paper's uniform doubling condition across a two-sided terminal cylinder.

---

## 6. Smooth terminal flatness is not time analyticity

The all-jet identity

\[
\partial_t^m Z(\cdot,T_*)=0\quad\forall m
\]

does not by itself imply

\[
Z\equiv0
\]

on a left neighborhood of `T_*`.

A `C^infinity` function can be flat at an endpoint without being zero before it.

Therefore the route

\[
\text{all terminal jets zero}
\to
\text{Taylor series zero}
\to
Z=0
\]

is **RED** unless a genuine one-sided time-analyticity theorem with a uniform terminal radius is separately proved.

This preserves the M5-141 firewall.

---

## 7. What can legitimately be reused

The valuable part of Ignatova–Kukavica for W1 is not Theorem 2.2 as a black box. It is the construction of **Carleman inequalities for the Laplacian and heat operator with the same singular spatial weight**, allowing pressure and velocity to be estimated together without Biot–Savart nonlocality.

This directly supports the M5-183 architecture:

\[
\boxed{
\text{parabolic velocity/vorticity equation}
+
\text{elliptic pressure equation}
}
\]

with matched weights.

The next internal question is whether their matched-weight proof can be adapted to a **one-sided terminal parabolic cylinder**, where the W1 difference is infinitely flat at the terminal face.

---

## 8. DSD audit

### Formation — GREEN

The external theorem hypotheses have been separated from the properties actually proved for the W1 physical pair.

### Axis — GREEN

Fixed-time spatial unique continuation, Gevrey regularity, and terminal backward propagation are distinct axes.

### Static aggregation — GREEN

`C-infinity terminal flatness` is not counted as `Gevrey/analytic terminal regularity`.

### Dynamics — YELLOW

The matched Carleman architecture is relevant; the endpoint adaptation is unproved.

### Cross-audit — GREEN

No theorem-name shortcut is used. The M5-141 prohibition against upgrading punctured smoothness to terminal analyticity remains in force.

---

## 9. Next calculation

Inspect the matched Laplace/heat Carleman proof and test a terminal one-sided time cutoff.  The target is to determine whether the time-boundary contribution at `t=T_*` vanishes automatically from the all-jet flatness and whether the lower time boundary can be sent backward by iteration.

If that fails, record the exact boundary term obstructing the endpoint adaptation.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
