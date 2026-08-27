# DSD M5-83 — Exact Endpoint Residual-Square Identity

Date: 2026-08-27

Status: **EXACT ALGEBRAIC COLLAPSE / THE ENTIRE SURPLUS ABOVE THE SHARP M5-69 UNIVERSAL PAYER FLOOR IS EXACTLY THE WEIGHTED L2 SQUARE OF THE M5-70 ENDPOINT EQUATION RESIDUAL / CAUCHY MISALIGNMENT AND BALANCE MISMATCH ARE ORTHOGONAL PIECES OF ONE RESIDUAL / NEAR-MINIMAL PAYMENT NOW DIRECTLY IMPLIES NEAR-ENDPOINT ALIGNMENT / GLOBAL REGULARITY UNPROVED.**

## 1. Definitions

Set

\[
a:=|U|,
\qquad
b:=U\cdot\nabla\log a,
\]

and on each connected regular superlevel branch define the centered pressure

\[
f
:=
P-m_{P,k}(a,t).
\]

Use the weighted measure

\[
\boxed{
d\mu
:=
a\,w(a)\,dY.
}
\]

Then M5-68/M5-70 give

\[
S_{comp,w}
=
\int |f|^2d\mu,
\]

\[
T
=
\int |b|^2d\mu,
\]

and

\[
J
:=
\bar J_w
=
\int fb\,d\mu.
\]

The entropy ledger is

\[
\boxed{
J=\nu D_w+X_w.
}
\]

Write

\[
B:=A_w+G_w,
\qquad
D_w=T+B.
\]

Hence

\[
\boxed{
J
=\nu T+\nu B+X_w.
}
\]

---

## 2. Square the exact M5-70 residual

Consider

\[
r
:=
f-2\nu b.
\]

Its weighted square is

\[
\begin{aligned}
\|r\|_{L^2(d\mu)}^2
&=
\int|f-2\nu b|^2d\mu\\
&=
S_{comp,w}
-4\nu J
+4\nu^2T.
\end{aligned}
\]

Insert

\[
J=\nu T+\nu B+X_w.
\]

Then

\[
\begin{aligned}
\|r\|_2^2
&=
S_{comp,w}
-4\nu(\nu T+\nu B+X_w)
+4\nu^2T\\
&=
S_{comp,w}
-4\nu^2B
-4\nu X_w.
\end{aligned}
\]

Therefore

\[
\boxed{
S_{comp,w}
-4\nu^2(A_w+G_w)
-4\nu X_w
=
\int a\,w(a)
\left|
P-m_{P,k}(a,t)
-2\nu U\cdot\nabla\log a
\right|^2dY.
}
\]

This is an exact identity.

---

## 3. Sharp M5-69 inequality becomes immediate

Because the right-hand side is nonnegative,

\[
\boxed{
S_{comp,w}
\ge
4\nu^2(A_w+G_w)
+4\nu X_w.
}
\]

Thus the sharp universal M5-69 lower bound is precisely the statement that a square is nonnegative.

Its equality condition is exactly

\[
\boxed{
P-m_{P,k}(a,t)
=2\nu U\cdot\nabla\log a
}
\]

on the active weighted region.

Therefore M5-70 is not merely an equality-case consequence obtained by combining two separate arguments; it is the zero set of the exact payer-surplus square.

---

## 4. Relation to the old Cauchy gap and Hw

Define the Cauchy projection coefficient

\[
c:=\frac JT.
\]

The exact Cauchy gap is

\[
\boxed{
C_w
:=
S_{comp,w}-\frac{J^2}{T}
=
\int|f-cb|^2d\mu
\ge0.
}
\]

M5-69 defined

\[
H_w
=
\frac{[\nu T-(\nu B+X_w)]^2}{T}.
\]

But

\[
c-2\nu
=
\frac{\nu B+X_w-\nu T}{T}.
\]

Hence

\[
\boxed{
T|c-2\nu|^2
=H_w.
}
\]

Since `f-cb` is orthogonal to `b` in `L2(dmu)`,

\[
\begin{aligned}
\|f-2\nu b\|_2^2
&=
\|f-cb\|_2^2
+|c-2\nu|^2\|b\|_2^2\\
&=
C_w+H_w.
\end{aligned}
\]

Therefore

\[
\boxed{
S_{comp,w}
-4\nu^2B
-4\nu X_w
=
C_w+H_w.
}
\]

The previously separate geometric alignment defect and scalar balance defect are orthogonal components of one exact residual.

---

## 5. Quantitative near-saturation statement

Define the total endpoint surplus

\[
\boxed{
\mathcal E_w
:=
S_{comp,w}
-4\nu^2(A_w+G_w)
-4\nu X_w
\ge0.
}
\]

Then

\[
\boxed{
\mathcal E_w
=
\|P-m_{P,k}(a,t)-2\nu b\|_{L^2(d\mu)}^2.
}
\]

Consequently

\[
\mathcal E_w\to0
\]

is **equivalent** to

\[
\boxed{
P-m_{P,k}(a,t)-2\nu b
\to0
\quad\text{strongly in }L^2(d\mu).
}
\]

No separate extraction of the Cauchy alignment factor and no separate proof that `H_w->0` is required.

---

## 6. Robust positive pump remains visible

On the returned upstroke,

\[
X_w\ge c_1>0.
\]

Therefore the sharp decomposition reads

\[
S_{comp,w}
=
4\nu^2(A_w+G_w)
+4\nu X_w
+\mathcal E_w.
\]

Thus pressure payment splits exactly into

\[
\boxed{
\begin{array}{rcl}
4\nu^2(A_w+G_w)
&=&\text{formation baseline},\\
4\nu X_w
&=&\text{positive pump payment},\\
\mathcal E_w
&=&\text{distance from the exact M5-70 endpoint}.
\end{array}
}
\]

This is stronger than treating the endpoint only qualitatively.

---

## 7. Component independence

The centering function `m_{P,k}` may differ between disconnected superlevel components.

The identity remains valid because the componentwise centered variance and componentwise pressure flux are defined using the same branch assignment.

No pressure offset between different components appears in `mathcal E_w`.

Thus the residual measures only the physically relevant internal pressure/crossing mismatch already isolated by M5-68.

---

## 8. Relation to the local tangential defect M5-82

Let

\[
q:=P-2\nu b.
\]

Then

\[
r=q-m_{P,k}(a,t).
\]

M5-83 gives smallness of `r` in the weighted volume norm.

M5-82 requires at exact endpoint

\[
\Pi_\tau\nabla q=0.
\]

Since tangential differentiation annihilates every branch function of amplitude,

\[
\Pi_\tau\nabla r
=
\Pi_\tau\nabla q.
\]

Therefore the remaining stability problem is now sharply formulated:

\[
\boxed{
\|r\|_{L^2(d\mu)}\to0
\quad\stackrel{?}{\Longrightarrow}\quad
\|\Pi_\tau\nabla q\|\to0
}
\]

using the uniform W1 analytic derivative bounds.

This is an interpolation problem, not a pressure-estimation problem.

---

## 9. DSD audit

### GREEN

The payer surplus is exactly the weighted square of the M5-70 residual.

### GREEN

The M5-69 sharp inequality follows immediately from nonnegativity of this square.

### GREEN

The old Cauchy gap and `H_w` are orthogonal pieces of the same residual norm.

### GREEN

Near-minimal pressure payment is quantitatively equivalent to strong weighted `L2` convergence toward the exact endpoint equation.

### YELLOW

Weighted `L2` smallness of the scalar endpoint residual does not by itself imply small tangential derivatives; a stability/interpolation estimate is still required.

### RED

No contradiction has yet been obtained from `mathcal E_w=0`; nonexistence of a nonzero recurrent exact endpoint remains open.

---

## 10. Next calculation

Exploit tangent vector fields that annihilate all functions of amplitude.

For

\[
L_{ij}
:=(\partial_i a)\partial_j-(\partial_j a)\partial_i,
\]

we have

\[
L_{ij}a=0,
\qquad
L_{ij}m(a)=0.
\]

Moreover the vector field defining `L_ij` is divergence free.

This suggests an integration-by-parts interpolation estimate controlling the M5-82 tangential defect directly from `mathcal E_w`, without differentiating the unknown branch means and without counting connected components.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
