# DSD M5-107 — Recurrent Lp Moment Balance and Critical Anomaly

Date: 2026-08-27

Status: **W1-CONDITIONAL EXACT GLOBAL p>3 MOMENT BALANCE / INVARIANT AVERAGING DERIVED / p DOWNARROW 3 PRODUCES THE CRITICAL CUBIC RESIDUE AS A FINITE ANOMALY / THE ANOMALY IS EXACTLY THE MEAN PRESSURE-MINUS-VISCOUS CRITICAL CURRENT / NO NEW INDEPENDENT BUDGET IS CREATED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Setup

Work on the retained smooth recurrent W1 Leray trajectory

\[
\partial_sU-\nu\Delta U+(U\cdot\nabla)U
+\frac12Y\cdot\nabla U+\frac12U+\nabla P=0,
\qquad \nabla\cdot U=0.
\]

Write

\[
a:=|U|,
\qquad
b:=U\cdot\nabla\log a
\]

on `a>0`.

For every

\[
3<p\le 6,
\]

the W1 class has global `L^p` control and precompactness, while the critical `1/r` tail makes the displayed weighted derivative and pressure terms integrable at infinity.

Define

\[
M_p(s):=\int_{\mathbb R^3} a^p\,dY.
\]

Also define the positive viscous p-dissipation

\[
\boxed{
\mathcal D_p
:=
\int a^{p-2}
\left(
|\nabla U|^2+(p-2)|\nabla a|^2
\right)dY
}
\]

and the pressure-amplitude work

\[
\boxed{
\Pi_p
:=
\int P\,a^{p-2}b\,dY.
}
\]

---

## 2. Exact p-moment identity

Multiply the Leray equation by

\[
a^{p-2}U
\]

and integrate over space.

The time derivative gives

\[
\frac1p M_p'.
\]

Incompressibility removes the nonlinear transport contribution:

\[
\int a^{p-2}U\cdot(U\cdot\nabla U)
=
\int U\cdot\nabla\left(\frac{a^p}{p}\right)=0.
\]

The dilation term gives

\[
\frac12\int a^{p-2}U\cdot(Y\cdot\nabla U)
=
-\frac{3}{2p}M_p,
\]

while the linear Leray term gives

\[
\frac12M_p.
\]

Thus their net coefficient is

\[
\frac{p-3}{2p}M_p.
\]

Integration by parts in the viscous term gives exactly `nu D_p`.

For pressure,

\[
\operatorname{div}(a^{p-2}U)
=(p-2)a^{p-2}b,
\]

so

\[
\int a^{p-2}U\cdot\nabla P
=-(p-2)\Pi_p.
\]

Hence

\[
\boxed{
\frac1pM_p'
+\nu\mathcal D_p
+\frac{p-3}{2p}M_p
=(p-2)\Pi_p.
}
\]

This is an exact global identity for every retained `p>3` W1 state.

---

## 3. DSD axis audit

The terms have distinct roles.

- `M_p' / p`: state-change channel.
- `((p-3)/(2p)) M_p`: self-similar dilation/linear channel.
- `nu D_p`: positive viscous/formation channel.
- `(p-2) Pi_p`: pressure-amplitude work channel.

At `p=3`, the explicit dilation coefficient vanishes.

This is the same critical neutrality already seen in the log-radius conveyor, now in one exact global moment identity.

No term is relabeled as another term in later aggregation.

---

## 4. Invariant recurrent averaging

Let `mu` be an invariant probability measure supported on the compact minimal W1 set.

Since `M_p` is finite, continuous, and bounded on that compact set,

\[
\left\langle M_p'\right\rangle_\mu=0.
\]

Therefore

\[
\boxed{
\nu\langle\mathcal D_p\rangle_\mu
+\frac{p-3}{2p}\langle M_p\rangle_\mu
=(p-2)\langle\Pi_p\rangle_\mu.
}
\]

This direction is

\[
\text{precompact W1 orbit}
\to
\text{invariant measure}
\to
\text{averaged identity}.
\]

The averaged identity is not used to create recurrence retroactively.

---

## 5. Critical limit

Set

\[
p=3+\varepsilon.
\]

The previously audited cubic residue is

\[
\boxed{
\mathscr R_3
:=
\lim_{\varepsilon\downarrow0}
\varepsilon
\left\langle
\int a^{3+\varepsilon}dY
\right\rangle_\mu
>0
}
\]

on the surviving W1 corridor.

Hence

\[
\frac{p-3}{2p}\langle M_p\rangle_\mu
\longrightarrow
\frac{\mathscr R_3}{6}.
\]

The W1 `1/r` envelope and local analytic bounds give dominated convergence for the derivative and pressure terms near `p=3+`:

\[
\mathcal D_p\to\mathcal D_3,
\qquad
\Pi_p\to\Pi_3,
\]

where

\[
\boxed{
\mathcal D_3
=
\int a\left(|\nabla U|^2+|\nabla a|^2\right)dY
}
\]

and

\[
\boxed{
\Pi_3
=
\int P\,a b\,dY
=
\int P\,U\cdot\nabla a\,dY.
}
\]

Therefore

\[
\boxed{
\langle\Pi_3\rangle_\mu
-
\nu\langle\mathcal D_3\rangle_\mu
=
\frac{\mathscr R_3}{6}.
}
\]

This is the critical anomaly balance.

---

## 6. Identification with the M5 critical ledger

At critical weight `w=1`, the M5 volume terms are

\[
A_3=\int a|\nabla U|^2,
\qquad
C_3=\int a|\nabla a|^2,
\qquad
D_3=A_3+C_3.
\]

Thus

\[
\mathcal D_3=D_3.
\]

Also the M5 pressure flux is

\[
J_3
=
\int P\,U\cdot\nabla a
=
\Pi_3.
\]

So the anomaly identity is exactly

\[
\boxed{
\langle J_3-\nu D_3\rangle_\mu
=
\frac{\mathscr R_3}{6}.
}
\]

The cubic residue is therefore not a second independent resource sitting next to the pressure overpay.

It **is** the invariant mean critical pressure overpay left after viscosity.

---

## 7. Relation to the log-radius conveyor

For a critical tail

\[
U(Y,s)=r^{-1}V(\theta,\rho,s),
\qquad \rho=\log r,
\]

the cubic density is unweighted in `rho`.

The Leray dilation flux of the cubic density across `|Y|=R` is

\[
\mathcal J_{\rm dil,3}(R,s)
=
\int_{|Y|=R}
\frac{Y\cdot n}{2}
\frac{|U|^3}{3}\,dS
=
\frac16
\int_{S^2}|R U(R\theta,s)|^3d\theta.
\]

Thus the same `1/r` tail coefficient that creates the Abel/Mellin residue also carries an order-one cubic dilation current per log-radius shell.

The invariant mean of that critical current is the same anomaly measured by `R_3/6`.

This is a structural identification, not a new additive cost.

---

## 8. Four-chain DSD audit

### Formation

The `p>3` moments are formed finite observables before the critical limit is taken.

The `p=3` anomaly is defined only as the one-sided limit of those formed observables; no divergent global `L3` norm is silently inserted.

### Axis

Dilation, pressure work, viscous formation, and state derivative remain distinct channels.

### Static aggregation

The cubic residue, critical dilation current, and invariant pressure overpay are three representations of one critical defect and are **not summed as independent payers**.

### Dynamics

Invariant averaging is applied only after W1 recurrence/precompactness has already been formed.

### Cross-audit verdict

No reverse dependency is introduced.

---

## 9. Consequence and limitation

The surviving W1 state must satisfy

\[
\boxed{
\langle J_3\rangle_μ
=
\nu\langle D_3\rangle_μ
+\frac{\mathscr R_3}{6}.
}
\]

Therefore the passive far-tail conveyor cannot be treated as an extra independent dynamical burden: its critical current is exactly supplied by the already identified core pressure-minus-viscous anomaly.

A proof must therefore prevent this pressure/current matching itself, or prove the critical residue vanishes.

Ordinary energy/enstrophy budgets do not do so.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
