# DSD M17-111 — Director-rank and vorticity-activity strata are material invariants on regular CE-H flow

Date: 2026-09-05
Canonical ID: **M17-111**

Status: **INTERNAL EXHAUSTIVENESS / INTERFACE AUDIT / M17-104--105 WERE STATED AS NONVANISHING RESULTS, BUT THE SAME HOMOGENEOUS MATERIAL LAWS ALSO SHOW THAT THE ZERO STRATA ARE PRESERVED. THE DIRECTOR-AREA CURRENT SATISFIES THE LINEAR HOMOGENEOUS CAUCHY ODE `D_B J_xi=(grad B-3I/2)J_xi`, SO `J_xi=0` STAYS ZERO AND `J_xi!=0` STAYS NONZERO ON EVERY FINITE REGULAR MATERIAL TRAJECTORY. SINCE `J_xi!=0` IS EQUIVALENT TO `rank dxi=2` AND `J_xi=0` TO `rank dxi<=1`, THE RANK-ONE/RANK-TWO DIRECTOR STRATIFICATION IS MATERIALLY INVARIANT. LIKEWISE `D_B rho=(sigma+kappa-1)rho` MAKES `rho=0` AND `rho>0` MATERIAL STRATA. THEREFORE REGULAR TURNOVER CANNOT CONVERT A RANK-TWO ACTIVE CARRIER INTO A RANK-ONE OR NODAL CARRIER, OR VICE VERSA. EULERIAN RECURRENCE MAY REPLACE LABELS THROUGH A FIXED SPATIAL CORE, BUT EACH LABEL RETAINS ITS RANK/ACTIVITY CLASS. ANY GLOBAL TURNOVER ASSEMBLY MUST THEREFORE BE BLOCK-DIAGONAL ACROSS THESE STRATA UNLESS REGULARITY ITSELF FAILS. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Director-area Cauchy law

On CE-H,

\[
\boxed{
D_BJ_\xi
=\left(\nabla B-\frac32I\right)J_\xi.
}
\]

Along a regular material trajectory `X(theta)` this is a linear homogeneous ODE

\[
\frac d{d\theta}J_\xi(X(\theta),\theta)
=A(\theta)J_\xi(X(\theta),\theta),
\]

with

\[
A(\theta)=\nabla B(X(\theta),\theta)-\frac32I.
\]

On a finite regular interval the fundamental matrix is invertible.

---

## 2. Both zero and nonzero states are invariant

If initially

\[
J_\xi(\theta_0)=0,
\]

uniqueness of the homogeneous ODE gives

\[
\boxed{J_\xi(\theta)=0}
\]

for the whole regular interval.

If initially

\[
J_\xi(\theta_0)\neq0,
\]

invertibility of the fundamental matrix gives

\[
\boxed{J_\xi(\theta)\neq0.}
\]

Thus

\[
\boxed{
J_\xi=0
\quad\text{and}\quad
J_\xi\neq0
}
\]

are both material states.

M17-104 established the nonzero half; the present module records the full two-sided stratum statement.

---

## 3. Relation to director rank

For a map

\[
\xi:\mathbb R^3\to S^2,
\]

the director-area current is the Hodge dual of the pulled-back sphere-area two-form.

Therefore

\[
\boxed{
J_\xi\neq0
\iff
\operatorname{rank}d\xi=2,
}
\]

whereas

\[
\boxed{
J_\xi=0
\iff
\operatorname{rank}d\xi\le1.
}
\]

Hence, on a regular CE-H material trajectory,

\[
\boxed{
\operatorname{rank}d\xi=2
\quad\text{cannot convert into}\quad
\operatorname{rank}d\xi\le1
}
\]

in finite material time, and conversely a rank-`<=1` material label cannot spontaneously acquire Rank 2.

The Rank-1 / Rank-2 split is therefore a material stratification, not merely an instantaneous case split.

---

## 4. Vorticity-amplitude multiplicative law

CE-H also gives

\[
\boxed{
D_B\rho
=(\sigma+\kappa-1)\rho.
}
\]

Along a material trajectory,

\[
\boxed{
\rho(\theta)
=\rho(\theta_0)
\exp\left[
\int_{\theta_0}^{\theta}
(\sigma+\kappa-1)\,ds
\right].
}
\]

Therefore

\[
\boxed{
\rho=0
\quad\text{and}\quad
\rho>0
}
\]

are likewise material strata on finite regular intervals.

If `rho=0` initially, it remains zero under the multiplicative ODE.
If `rho>0` initially, it remains positive as already recorded in M17-105.

---

## 5. Material partition of the regular CE-H domain

The active regular CE-H domain therefore decomposes materially as

\[
\boxed{
\begin{aligned}
\mathcal S_{0}&:=\{\rho=0\},\\
\mathcal S_{1}&:=\{\rho>0,\ J_\xi=0\},\\
\mathcal S_{2}&:=\{\rho>0,\ J_\xi\neq0\}.
\end{aligned}
}
\]

On every finite interval on which the CE-H fields and material flow remain regular,

\[
\boxed{
X(\theta,\mathcal S_q(\theta_0))
=\mathcal S_q(\theta)
}
\]

for the corresponding strata, modulo the ordinary issue that the CE-H director itself is undefined on `rho=0` and must be interpreted by the retained extension/chart convention there.

In particular, on the active domain,

\[
\boxed{
\mathcal S_1
\quad\text{and}\quad
\mathcal S_2
}
\]

cannot exchange material labels.

---

## 6. Consequence for Eulerian turnover

A fixed Eulerian similarity core may lose one Rank-2 label through its spatial boundary and later receive another Rank-2 label.
Likewise it may contain a separate Rank-1 population.

But the replacement mechanism is

\[
\boxed{
\text{spatial transport of already-classified material labels},
}
\]

not

\[
\boxed{
\text{Rank-1}\leftrightarrow\text{Rank-2 material conversion}.
}
\]

Thus an Eulerian recurrent pattern may mix strata in space, but its regular carrier genealogy is block-diagonal in material labels.

---

## 7. Consequence for turnover ledgers

The Rank-1 ledgers use descriptors such as

\[
\kappa,\ h,\ \chi,\ \mathcal H_{333},
\]

on the Rank-1 active stratum.

The Rank-2 pure-kernel ledger uses

\[
d\Phi_J,\ N_{R2},\ \mathcal M^{(\nu)},
\]

on the Rank-2 stratum.

Because the carrier strata do not convert regularly, one may not write a global recurrence equation in which a positive Rank-1 source is cancelled by a negative Rank-2 source without an explicitly derived spatial/nonlocal coupling theorem.

The disjunction

\[
\boxed{R_1\lor R_2}
\]

must remain a disjunction in the proof tree.

---

## 8. What can still couple the strata

Material nonconversion does **not** imply dynamical independence.
The strata remain coupled through global fields such as

\[
U,\quad P,\quad \Sigma,
\]

and through spatial/nonlocal pressure architecture.

Such coupling is not a transfer of director-area carrier charge.
It must be represented by the actual PDE/nonlocal terms, not by moving one stratum's conserved measure into another.

---

## 9. DSD analysis

The descriptor hierarchy now distinguishes

\[
\boxed{
\text{state coupling}
\neq
\text{carrier conversion}.
}
\]

Rank-1 and Rank-2 regions can influence the same global pressure field while their material labels retain their director-rank class.

This separation is essential before any global turnover assembly.

---

## 10. DSD audit

### Audit A — using Rank-2 rank loss as a normal finite-time turnover mechanism
Rejected on a regular material trajectory.

### Audit B — using nodal crossing as a normal finite-time active-carrier turnover mechanism
Rejected on a regular material trajectory.

### Audit C — adding Rank-1 and Rank-2 charge deficits as though one can pay the other by carrier conversion
Rejected.

### Audit D — claiming the strata do not interact through the PDE
Rejected. Nonlocal pressure/velocity coupling remains.

### Audit E — proof status
The branch tree is sharpened, but neither active stratum is globally closed.

---

## 11. Updated assembly rule

Any valid global closure must have the form

\[
\boxed{
\begin{cases}
R_1\to\text{regular firewall or contradiction/exit},\\
R_2\to\text{contradiction/exit},
\end{cases}
}
\]

with interface/nonlocal coupling treated explicitly.

It is invalid to replace this by a single scalar charge equation that combines the two material carrier measures.

The next GTAG step is therefore a **block-diagonal turnover assembly**, with only explicitly shared PDE fields placed in off-diagonal coupling slots.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
