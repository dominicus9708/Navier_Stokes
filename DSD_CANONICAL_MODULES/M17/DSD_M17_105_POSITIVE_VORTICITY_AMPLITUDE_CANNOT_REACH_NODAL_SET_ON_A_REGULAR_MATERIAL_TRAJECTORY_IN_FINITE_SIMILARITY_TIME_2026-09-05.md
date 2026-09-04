# DSD M17-105 — Positive vorticity amplitude cannot reach the nodal set on a regular material trajectory in finite similarity time

Date: 2026-09-05
Canonical ID: **M17-105**

Status: **INTERNAL CE-H ACTIVE-DIRECTOR-CHART NONVANISHING GATE / M17-104 EXCLUDES FINITE-TIME MATERIAL LOSS OF NONZERO DIRECTOR-AREA CURRENT `J_xi`. THE OTHER NATURAL CARRIER EXIT IS THE VORTICITY NODAL SET `rho=|W|=0`, WHERE THE DIRECTOR `xi=W/rho` CEASES TO BE DEFINED. ON CE-H, HOWEVER, THE AMPLITUDE SATISFIES THE EXACT HOMOGENEOUS SCALAR LAW `D_B rho=(sigma+kappa-1)rho`. THEREFORE A MATERIAL LABEL WITH `rho(theta_0)>0` HAS `rho(theta)=rho(theta_0) exp(int(sigma+kappa-1))` AND CANNOT REACH `rho=0` AT FINITE REGULAR SIMILARITY TIME WHILE THE COEFFICIENT IS LOCALLY INTEGRABLE. THUS THE ACTIVE DIRECTOR CHART IS FINITE-TIME MATERIAL-INVARIANT, JUST AS NONZERO `J_xi` IS. A NODAL FILAMENT MAY STILL EXIST AND MOVE AS ITS OWN MATERIAL ZERO SET, BUT A NONZERO CE-H MATERIAL CARRIER CANNOT CROSS INTO IT IN FINITE REGULAR TIME. ASYMPTOTIC `rho->0`, EULERIAN REPLACEMENT AT FIXED SPATIAL LOCATIONS, SPATIAL/CHART BOUNDARY TRANSPORT, OR LOSS OF REGULARITY REMAIN POSSIBLE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. CE-H amplitude law

On CE-H,

\[
\Delta W=\kappa W,
\qquad
\Sigma W=\sigma W.
\]

The similarity material vorticity equation reduces to

\[
D_BW
=(\sigma+\kappa-1)W.
\]

Write

\[
W=\rho\xi,
\qquad
\rho=|W|>0.
\]

Since the director is materially frozen,

\[
D_B\xi=0,
\]

the amplitude satisfies

\[
\boxed{
D_B\rho
=(\sigma+\kappa-1)\rho.
}
\]

Equivalently,

\[
\boxed{
D_B\log\rho
=\sigma+\kappa-1.
}
\]

---

## 2. Exact material solution

Along a material trajectory

\[
\dot X=B(X,\theta),
\]

set

\[
a_\rho(\theta)
:=\sigma(X(\theta),\theta)
+\kappa(X(\theta),\theta)-1.
\]

Then

\[
\frac d{d\theta}\rho(X(\theta),\theta)
=a_\rho(\theta)\rho(X(\theta),\theta).
\]

Hence

\[
\boxed{
\rho(\theta)
=ho(\theta_0)
\exp\left(
\int_{\theta_0}^{\theta}a_\rho(s)\,ds
\right).
}
\]

---

## 3. Finite-time positivity preservation

If

\[
\rho(\theta_0)>0
\]

and `a_rho` is integrable on a finite interval, then the exponential factor is strictly positive.

Therefore

\[
\boxed{
\rho(\theta)>0
}

throughout the same finite regular material interval.

Thus

\[
\boxed{
\rho>0
\quad\Longrightarrow\quad
\text{no finite-time material transition to }\rho=0
}
\]

inside the regular CE-H branch.

---

## 4. Director chart is materially preserved

The director is

\[
\xi=\frac W{|W|}.
\]

Therefore the chart exists exactly where

\[
\rho>0.
\]

Section 3 gives

\[
\boxed{
\rho(\theta_0)>0
\Longrightarrow
\xi(X(\theta),\theta)\text{ remains defined for finite regular material time}.
}
\]

A nonzero CE-H material carrier cannot cross into the vorticity nodal set at finite regular similarity time.

---

## 5. Relation to material nodal filaments

M17-007 shows that regular winding nodal filaments are material zero sets.

There is no contradiction with M17-105.

The two statements are complementary:

- a material label starting on `W=0` may remain on the nodal set;
- a material label starting with `W!=0` cannot reach `W=0` in finite regular CE-H time.

Thus the nodal set is a material separator for the homogeneous CE-H amplitude dynamics.

---

## 6. Combine with director-area nonvanishing

M17-104 gives

\[
J_\xi(\theta_0)\neq0
\Longrightarrow
J_\xi(\theta)\neq0
\]

for finite regular material time.

M17-105 gives

\[
\rho(\theta_0)>0
\Longrightarrow
\rho(\theta)>0.
\]

Therefore a material Rank-2 active carrier satisfying

\[
\boxed{
\rho>0,
\qquad
J_\xi\neq0
}
\]

at one time remains in the same active full-Rank-2 director class for every finite time on which the CE-H coefficients remain regular/integrable.

---

## 7. Consequence for finite-time carrier exits

After M17-103, potential carrier exits included endpoint/domain transitions and `J_xi=0`.

M17-104 removes finite-time exact `J_xi=0` on the same material carrier.
M17-105 removes finite-time exact `rho=0` on the same material carrier.

Thus neither

\[
\boxed{J_\xi=0}
\]

nor

\[
\boxed{\rho=0}
\]

is an ordinary finite-time internal turnover mechanism for a regular Rank-2 CE-H material tube.

The surviving finite-time changes are transport of the persistent carrier across a chosen spatial/domain/chart boundary, or failure of the regularity assumptions themselves.

---

## 8. Eulerian/material distinction

At a fixed spatial point, `rho(x,theta)` may vanish or become positive because different material labels pass through the location.

Therefore M17-105 does not claim that the Eulerian nodal set is stationary.

It claims only

\[
\boxed{
\text{same positive material label}
\not\to
\text{zero material label in finite regular CE-H time}.
}
\]

This is exactly the carrier-level statement needed for the genealogy audit.

---

## 9. Asymptotic degeneration remains possible

The exponential law does not give a uniform positive lower bound for all infinite similarity time unless additional recurrence/compactness hypotheses are imposed.

It remains possible that

\[
\rho(\theta)\to0
\]

as

\[
|\theta|\to\infty
\]

through an integral

\[
\int(\sigma+\kappa-1)\to-\infty.
\]

Such asymptotic degeneration is separate from finite-time nodal crossing.

On a same-marker recurrent hard branch with `rho` bounded above and below, this asymptotic exit is absent by hypothesis.

---

## 10. DSD analysis

The phrase "active-domain exit" hides two different mechanisms:

1. the material amplitude actually reaches zero;
2. the persistent material carrier leaves a chosen local spatial/chart domain.

M17-105 excludes the first at finite regular time.
The second is only transport across an observational/domain boundary and must be audited by a flux balance rather than counted as carrier destruction.

---

## 11. DSD audit

### Audit A — concluding a uniform lower bound from positivity preservation
Rejected. Positivity at finite time does not imply an infinite-time lower bound.

### Audit B — confusing nodal-set motion with material crossing into the nodal set
Rejected.

### Audit C — extending the law beyond CE-H
Not done. The homogeneous scalar amplitude equation is a CE-H consequence.

### Audit D — treating chart-boundary transport as physical annihilation
Rejected. That is a separate spatial flux problem.

### Audit E — proof status
Finite-time material nodal exit is closed, but global endpoint/interface transport and asymptotic recurrence remain open.

---

## 12. Updated Rank-2 active-carrier frontier

For a regular CE-H material label with

\[
\rho>0,
\qquad
J_\xi\neq0,
\]

we now have

\[
\boxed{
\rho(\theta)>0,
\qquad
J_\xi(\theta)\neq0
}
\]

for every finite regular material time.

Combined with M17-103,

\[
\boxed{
\text{finite internal peak/type/tangency genealogy}
\text{ is recyclable and the carrier cannot die internally.}
}
\]

The next high-value gate is therefore purely a **spatial carrier-flux boundary gate**: determine whether repeated passage of persistent active Rank-2 tubes through the compact hard-hull boundary can support recurrence while maintaining the Riccati compensation and finite-energy transport budgets, or whether the global flux ledgers force a nonrecyclable boundary cost.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
