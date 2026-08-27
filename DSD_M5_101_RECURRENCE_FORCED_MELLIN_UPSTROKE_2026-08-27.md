# DSD M5-101 — Recurrence-Forced Mellin Upstroke

Date: 2026-08-27

Status: **INDEPENDENT POSITIVE-UPSTROKE CONSTRUCTION FOR THE M5-100 MELLIN WEIGHT / USES ONLY PRIOR W1 GLOBAL-LP RECURRENCE AND THE EXACT INVERSE-LERAY SCALE FACTOR / A SUFFICIENTLY ACCURATE LARGE RETURN OF THE NORMALIZED PROFILE FORCES STRICT GROWTH OF THE STANDARD-CELL LP/MELLIN MOMENT / NO PRESSURE-PAYER OR ENDPOINT RESULT IS USED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Inputs allowed by the acyclic DAG

This memo uses only nodes that precede the pressure-payer endpoint in M5-98:

1. the nonzero compact minimal recurrent W1 trajectory `U#`;
2. global `L^p` precompactness/recurrence for every `3<p<=6`;
3. the exact inverse-Leray representation from M5-41/M5-44.

No M5-69--100 endpoint conclusion is used to create the upstroke.

This is required by the DSD circularity firewall.

---

# 2. Fix the Mellin exponent

Choose

\[
1<\alpha<\frac32,
\qquad
p=\alpha+2\in(3,7/2).
\]

M5-100 defines

\[
\mathfrak E_\alpha[V]
=\frac{1}{\alpha(\alpha+1)(\alpha+2)}
\|V\|_p^p.
\]

Only positivity and scaling matter below, so write

\[
c_\alpha
:=\frac{1}{\alpha(\alpha+1)(\alpha+2)}>0.
\]

---

# 3. Exact inverse-Leray Lp scaling

M5-44 writes the ancient-to-terminal cell as

\[
V_*(z,\sigma)
=(\sigma_*-\sigma)^{-1/2}
U^\#\!\left(
\frac{z}{\sqrt{\sigma_*-\sigma}},
\eta(\sigma)
\right),
\]

where

\[
\eta(\sigma)
=\log\frac{\sigma_*}{\sigma_*-\sigma}.
\]

Changing variables gives exactly

\[
\boxed{
\|V_*(\sigma)\|_p^p
=(\sigma_*-\sigma)^{(3-p)/2}
\|U^\#(\eta)\|_p^p.
}
\]

Since

\[
\sigma_*-\sigma
=\sigma_*e^{-\eta},
\]

we obtain

\[
\boxed{
\mathfrak E_\alpha[V_*(\sigma(\eta))]
=c_\alpha\sigma_*^{-(\alpha-1)/2}
 e^{(\alpha-1)\eta/2}
\|U^\#(\eta)\|_p^p.
}
\]

The crucial factor is

\[
\boxed{e^{(\alpha-1)\eta/2}.}
\]

It is strictly increasing because `alpha>1`.

---

# 4. A large recurrent return forces strict moment growth

Fix one reference W1 phase `eta_0`.
The minimal orbit is nonzero, hence

\[
m_0:=\|U^\#(\eta_0)\|_p^p>0.
\]

Global `L^p` recurrence provides return times

\[
h_n\to\infty
\]

with

\[
U^\#(\eta_0+h_n)
\to U^\#(\eta_0)
\quad\text{in }L^p.
\]

Therefore for all sufficiently accurate returns,

\[
\|U^\#(\eta_0+h_n)\|_p^p
\ge\frac12m_0.
\]

Since `h_n->infinity`, choose one of those returns also satisfying

\[
e^{(\alpha-1)h_n/2}>2.
\]

Then the inverse-Leray moment formula gives

\[
\begin{aligned}
\mathfrak E_\alpha(\sigma(\eta_0+h_n))
&\ge
c_\alpha\sigma_*^{-(\alpha-1)/2}
 e^{(\alpha-1)(\eta_0+h_n)/2}
\frac{m_0}{2}\\
&>
c_\alpha\sigma_*^{-(\alpha-1)/2}
 e^{(\alpha-1)\eta_0/2}m_0\\
&=
\mathfrak E_\alpha(\sigma(\eta_0)).
\end{aligned}
\]

Hence

\[
\boxed{
\Delta\mathfrak E_\alpha>0
}
\]

between two preterminal times of the same standard Navier--Stokes cell.

This conclusion does **not** require the narrow-band first-hit entropy to have a particular sign.

---

# 5. A positive instantaneous upstroke exists

The cell is smooth for every `sigma<sigma_*` and the Mellin-weighted quantities are finite by M5-100.
Thus

\[
\sigma\mapsto\mathfrak E_\alpha[V_*(\sigma)]
\]

is differentiable on every compact preterminal interval.

By the mean value theorem, the strict endpoint difference above gives at least one time `sigma_0` with

\[
\boxed{
X_\alpha(\sigma_0)
:=\partial_\sigma\mathfrak E_\alpha[V_*(\sigma_0)]
>0.
}
\]

By smooth dependence, after shrinking around `sigma_0`, there are

\[
\delta_\sigma>0,
\qquad c_\alpha^X>0
\]

such that

\[
\boxed{
X_\alpha(\sigma)\ge c_\alpha^X>0
}
\]

on a nontrivial cell-time interval.

---

# 6. Scale recurrence preserves the sign

For standard Navier--Stokes scaling

\[
V_\Lambda(x,t)=\Lambda V(\Lambda x,\Lambda^2t),
\]

the homogeneous Mellin entropy has degree

\[
\mathfrak E_\alpha[V_\Lambda]
=\Lambda^{\alpha-1}\mathfrak E_\alpha[V],
\]

and therefore

\[
\boxed{
X_\alpha[V_\Lambda]
=\Lambda^{\alpha+1}X_\alpha[V].
}
\]

The multiplier is positive.
Thus every sufficiently accurate M5-44 terminal-scale return of a positive Mellin-upstroke segment remains a positive upstroke after its natural rescaling.

The numerical size changes with scale, but the sign and normalized geometry do not.

---

# 7. DSD four-chain audit

## Formation

The Mellin observable is formed from the standard-cell velocity and is finite before the terminal time.

**GREEN.**

## Axis

No new axis is introduced. The observable depends only on amplitude; the later payer audit will use the already typed normal/tangential channels.

**GREEN.**

## Static aggregation

Global `L^p` recurrence controls the normalized profile norm, while the inverse-Leray map contributes an independent explicit positive scale factor.
These are not the same quantity and are not double-counted.

**GREEN.**

## Dynamics

The strict increase follows from forward time translation `eta -> eta+h` and the monotone inverse-Leray scale factor.
The pressure payer is not invoked.

**GREEN.**

---

# 8. Circularity audit

The logic is

\[
\boxed{
W1\text{ recurrence}
+\text{ inverse-Leray scaling}
\to
X_\alpha>0.
}
\]

It is **not**

\[
\text{pressure endpoint}
\to X_\alpha>0
\to\text{pressure endpoint}.
\]

Therefore the new positive-upstroke node is upstream of the Mellin payer audit and does not create a feedback cycle.

---

# 9. Consequence

M5-100 proved that for the same exponent family an exact minimal-payer endpoint must satisfy

\[
X_\alpha\le0.
\]

The present memo independently proves existence of a cell interval with

\[
X_\alpha>0.
\]

Thus the next step may safely combine the two forward nodes and quantify the resulting **strict pressure-payer surplus**.

This does not yet imply a finite-budget contradiction.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
