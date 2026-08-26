# DSD M5-63 — Squared-Overpay Critical Scaling Audit

Date: 2026-08-27

Status: **EXACT NAVIER--STOKES SCALING AUDIT / THE CANONICAL M5-62 SQUARED-OVERPAY ACTION IS EXACTLY SCALE-CRITICAL WHEN THE AMPLITUDE BAND IS TRANSPORTED COVARIANTLY WITH THE PUMP SCALE / EACH SYNDETIC RECURRENT COPY CARRIES THE SAME ORDER-ONE ACTION / THE REMAINING OBSTRUCTION IS A FINITE SCALE-COVARIANT GLOBAL BUDGET / GLOBAL REGULARITY UNPROVED.**

## 1. Threshold entropy covariance

For the quadratic positive-part threshold entropy used in the M5 first-hit branch, write

\[
E_\lambda[u](t)
:=
\frac12\int_{\mathbb R^3}
(|u(x,t)|-\lambda)_+^2\,dx.
\]

The irrelevant factor `1/2` can be changed without affecting the scaling conclusions below.

Under the Navier--Stokes scaling

\[
u_\Lambda(x,t)
=
\Lambda u(\Lambda x,\Lambda^2t),
\qquad
p_\Lambda(x,t)
=
\Lambda^2p(\Lambda x,\Lambda^2t),
\]

the matching amplitude threshold is

\[
\lambda_\Lambda=\Lambda\lambda.
\]

Changing variables `y=Lambda x` gives

\[
\begin{aligned}
E_{\Lambda\lambda}[u_\Lambda](t)
&=
\frac12\int
\bigl(\Lambda|u(\Lambda x,\Lambda^2t)|-\Lambda\lambda\bigr)_+^2dx\\
&=
\Lambda^{-1}
E_\lambda[u](\Lambda^2t).
\end{aligned}
\]

Hence

\[
\boxed{
E_{\Lambda\lambda}[u_\Lambda](t)
=
\Lambda^{-1}E_\lambda[u](\Lambda^2t).
}
\]

The threshold entropy is subcritical by one spatial power.

---

## 2. Covariant transport of the amplitude mollifier

Let `w` be the fixed normalized W1 amplitude weight from M5-56, with

\[
\int_0^\infty w(\lambda)d\lambda=1.
\]

At physical pump scale `Lambda`, the same normalized amplitude band is represented by

\[
\boxed{
w_\Lambda(\lambda)
:=
\Lambda^{-1}w(\lambda/\Lambda).
}
\]

Then

\[
\int_0^\infty w_\Lambda(\lambda)d\lambda=1,
\]

and the support is transported from

\[
[\lambda_-,\lambda_+]
\]

to

\[
[\Lambda\lambda_-,\Lambda\lambda_+].
\]

This covariant transport is essential. Keeping one fixed physical amplitude interval while changing the pump scale would no longer describe the same normalized recurrent event.

---

## 3. Scaling of the mollified entropy

Define

\[
\bar E_w[u](t)
:=
\int_0^\infty
w(\lambda)E_\lambda[u](t)d\lambda.
\]

Then

\[
\begin{aligned}
\bar E_{w_\Lambda}[u_\Lambda](t)
&=
\int_0^\infty
\Lambda^{-1}w(\lambda/\Lambda)
E_\lambda[u_\Lambda](t)d\lambda.
\end{aligned}
\]

Set `lambda=Lambda mu`. Using the threshold covariance from Section 1,

\[
\boxed{
\bar E_{w_\Lambda}[u_\Lambda](t)
=
\Lambda^{-1}
\bar E_w[u](\Lambda^2t).
}
\]

Thus the mollified entropy has the same `Lambda^{-1}` scaling as the single-level threshold entropy.

---

## 4. Scaling of the signed pressure overpay

Recall

\[
X_w[u](t)
:=
\bar J_w[u](t)
-
\nu\bar D_w[u](t)
=
\partial_t\bar E_w[u](t).
\]

Differentiate the covariance relation:

\[
\begin{aligned}
X_{w_\Lambda}[u_\Lambda](t)
&=
\partial_t
\left[
\Lambda^{-1}\bar E_w[u](\Lambda^2t)
\right]\\
&=
\Lambda X_w[u](\Lambda^2t).
\end{aligned}
\]

Hence

\[
\boxed{
X_\Lambda(t)=\Lambda X(\Lambda^2t).
}
\]

The first-order entropy velocity is therefore instantaneous scaling degree `+1`.

The same conclusion is consistent with direct scaling of both `bar J_w` and `nu bar D_w`.

---

## 5. Exact criticality of the squared-overpay action

Let `I` be one normalized pump interval and let its physical scaled copy be

\[
I_\Lambda=\Lambda^{-2}I
\]

up to translation toward the terminal point.

The M5-62 action is

\[
\mathcal A_X[I]
:=
\int_I X(t)^2dt.
\]

Then

\[
\begin{aligned}
\mathcal A_{X,\Lambda}[I_\Lambda]
&=
\int_{I_\Lambda}
\Lambda^2X(\Lambda^2t)^2dt\\
&=
\int_I X(s)^2ds.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathcal A_{X,\Lambda}
=
\mathcal A_X.
}
\]

In the M5-61 notation,

\[
\boxed{\gamma=0.}
\]

The canonical squared-overpay loop action is exactly scale-critical.

---

## 6. Scale invariance of the pump lower bound

M5-62 also gave

\[
\mathcal A_X[I]
\ge
\frac{(\Delta E)^2}{|I|}.
\]

Under scaling,

\[
\Delta E_\Lambda
=
\Lambda^{-1}\Delta E,
\]

while

\[
|I_\Lambda|
=
\Lambda^{-2}|I|.
\]

Hence

\[
\boxed{
\frac{(\Delta E_\Lambda)^2}{|I_\Lambda|}
=
\frac{(\Delta E)^2}{|I|}.
}
\]

The lower bound is therefore itself exactly critical and survives every terminal-centered recurrent rescaling with the same numerical size.

---

## 7. Consequence for the syndetic Zeno ladder

M5-52/M5-57 provide a separated recurrent subladder with geometrically increasing amplitude scales

\[
\Lambda_n\to\infty.
\]

For the robust pump interval on every sufficiently accurate return,

\[
\mathcal A_X(I_n)
\ge a_*>0
\]

with one normalized constant `a_*`.

Since the copies are disjoint in physical time after selecting the separated terminal ladder,

\[
\boxed{
\sum_{n=1}^N
\mathcal A_X(I_n)
\ge Na_*.
}
\]

Thus the physical accumulated squared-overpay action diverges logarithmically in terminal scale depth, exactly like the other beta-zero critical actions in M5-47/M5-61.

---

## 8. Scaling of the finite-band pressure payer

For consistency, the M5-56 finite-band pressure quantity

\[
\bar S_w
=
\int |u|w(|u|)|p|^2dx
\]

with the covariantly transported weight satisfies

\[
\boxed{
\bar S_{w_\Lambda}[u_\Lambda](t)
=
\Lambda\bar S_w[u](\Lambda^2t).
}
\]

Likewise

\[
\bar D_{w_\Lambda}[u_\Lambda](t)
=
\Lambda\bar D_w[u](\Lambda^2t),
\]

and

\[
\bar J_{w_\Lambda}[u_\Lambda](t)
=
\Lambda\bar J_w[u](\Lambda^2t).
\]

This confirms directly that their difference `X` has degree `+1` and its squared spacetime action is critical.

---

## 9. DSD audit: one normalized band versus many physical bands

The recurrent action is not measured with one fixed physical threshold band.

At scale `Lambda_n`, the relevant band is

\[
\operatorname{supp}w_{\Lambda_n}
=
\Lambda_n\operatorname{supp}w.
\]

Therefore any proposed finite global estimate must control the **scale-covariant family**

\[
\left\{
X_{w_{\Lambda_n}}
\right\}_{n\ge1}
\]

on its corresponding disjoint pump intervals.

A bound for a single fixed physical threshold or one fixed physical mollifier would not be sufficient.

This prevents a hidden change-of-observable error when summing the Zeno ladder.

---

## 10. What the scaling result does and does not prove

### GREEN

The M5-62 action is a genuine beta-zero/critical event action.

### GREEN

Each robust recurrent copy contributes one fixed positive amount.

### GREEN

The terminal Zeno sum is nonsummable.

### RED

Criticality does not provide a finite total budget. The classical Leray energy inequality controls the `gamma=-1` spacetime enstrophy budget, not the present `gamma=0` squared pressure-overpay action.

### YELLOW

If one can derive an initial-data-controlled finite bound for the scale-covariant family of squared-overpay actions, the recurrent survivor is immediately excluded.

---

## 11. New endpoint question

The accumulation branch has now been reduced to one precise endpoint estimate:

\[
\boxed{
\sum_n
\int_{I_n}
\left(
\bar J_{w_{\Lambda_n}}
-
\nu\bar D_{w_{\Lambda_n}}
\right)^2dt
<\infty
\ ?
}
\]

for every Leray--Hopf/suitable solution generated by smooth finite-energy initial data before a hypothetical first singular time.

M5-64 will classify the temporal powers of `X` and identify why `L_t^2` is exactly the endpoint exponent that could close recurrence.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
