# DSD M5-50 — Renormalized Return Cocycle and the Critical `p=3` Ledger

Date: 2026-08-27

Status: **CONDITIONAL RIGIDITY LEMMA + EXACT CRITICAL-DRIFT CANCELLATION / A BOUNDED SIGNED LYAPUNOV-COCYCLE WOULD EXCLUDE INFINITE SAME-TRAJECTORY RETURNS / THE EXISTING M5-37 PRESSURE-TAIL GAP IS ONLY A NECESSARY INSTANTANEOUS PAYER AND DOES NOT YET SUPPLY SUCH A COCYCLE / GLOBAL REGULARITY UNPROVED.**

## 1. Gate inherited from M5-49

M5-49 closes ordinary multiscale budget counting.

The remaining target is not to assign another positive raw cost to each shrinking copy.

Instead, one must find a quantity that changes with a fixed sign across each nontrivial normalized return and whose changes telescope along the same trajectory.

Schematically,

\[
\boxed{
\text{recurrent return}
\Longrightarrow
\text{irreversible critical signed defect}.
}
\]

This memo states the exact abstract criterion and tests the current `p=3`/pressure-tail ledger against it.

---

## 2. Terminal Leray variables

Let

\[
\tau:=T-t,
\qquad
\eta:=-\log\tau,
\qquad
y:=\frac{x-x_*}{\sqrt{\tau}},
\]

and write

\[
u(x,t)=\tau^{-1/2}U(y,\eta),
\qquad
p(x,t)=\tau^{-1}P(y,\eta).
\]

Then the incompressible Navier--Stokes equations become

\[
\boxed{
\partial_\eta U
+\frac12U
+\frac12(y\cdot\nabla)U
+(U\cdot\nabla)U
+\nabla P
-\nu\Delta U
=0,
}
\]

\[
\nabla\cdot U=0.
\]

M5-44 identified physical scaling with translation in `eta`.

Therefore the same-trajectory multiscale problem is naturally a recurrence problem for the normalized orbit

\[
\eta\mapsto U(\eta).
\]

---

## 3. Abstract return-cocycle exclusion lemma

Let `X` be a state space for normalized profiles and suppose the forward normalized orbit

\[
\mathcal O:=\{U(\eta):\eta\ge\eta_0\}
\]

has compact closure `K` in the topology used for the return extraction.

Assume there exists a continuous functional

\[
\mathfrak L:K\to\mathbb R
\]

which is bounded below on `K`.

Suppose further that every accepted nontrivial pump return interval

\[
[\eta_n,\eta_{n+1}]
\]

obeys a uniform strict decrement

\[
\boxed{
\mathfrak L(U(\eta_{n+1}))
\le
\mathfrak L(U(\eta_n))-\delta_*,
\qquad
\delta_*>0.
}
\]

Then infinitely many such returns are impossible.

### Proof

Iterating gives

\[
\mathfrak L(U(\eta_N))
\le
\mathfrak L(U(\eta_0))-N\delta_*.
\]

As `N\to\infty`, the right-hand side tends to `-infinity`, contradicting boundedness below of `\mathfrak L` on `K`.

The same statement holds with signs reversed for a functional bounded above.

Thus

\[
\boxed{
\text{bounded critical Lyapunov functional}
+
\text{uniform signed return gap}
\Rightarrow
\text{no infinite recurrence}.
}
\]

---

## 4. Cocycle formulation

The previous lemma can be stated without privileging a particular primitive.

Let

\[
\mathfrak C(\eta_a,\eta_b)
\]

be an additive cocycle along the normalized orbit:

\[
\mathfrak C(\eta_a,\eta_c)
=
\mathfrak C(\eta_a,\eta_b)
+
\mathfrak C(\eta_b,\eta_c).
\]

If every nontrivial return satisfies

\[
\mathfrak C(\eta_n,\eta_{n+1})\ge\delta_*>0
\]

and the accumulated cocycle is bounded on the recurrent compact set, then recurrence is again impossible.

This is exactly the structural feature missing from a collection of merely positive, nonadditive local costs.

---

## 5. Exact critical cancellation at `p=3`

Let

\[
a:=|U|.
\]

Under sufficient decay/integrability to justify global integration, multiply the normalized equation by

\[
aU.
\]

The time term is

\[
\int \partial_\eta U\cdot aU
=
\frac13\frac d{d\eta}\int a^3.
\]

The linear similarity term gives

\[
\frac12\int a^3.
\]

The similarity drift gives

\[
\frac12\int (y\cdot\nabla U)\cdot aU
=
\frac16\int y\cdot\nabla(a^3)
=-\frac12\int a^3.
\]

Hence at exactly `p=3`,

\[
\boxed{
\frac12\int a^3
-
\frac12\int a^3
=0.
}
\]

The convective term vanishes globally by incompressibility:

\[
\int (U\cdot\nabla U)\cdot aU
=
\frac13\int U\cdot\nabla(a^3)
=0.
\]

Define the positive critical dissipation

\[
\mathcal D_3(U)
:=
\int
\left[
|U||\nabla U|^2
+
|U|^{-1}
\sum_j(U\cdot\partial_jU)^2
\right]dy,
\]

with the second term interpreted as zero at `U=0`.

Then the exact formal global ledger is

\[
\boxed{
\frac13\frac d{d\eta}\int |U|^3dy
+
\nu\mathcal D_3(U)
=
\int P\,\nabla\cdot(|U|U)\,dy.
}
\]

There is no positive or negative similarity-drift remainder at `p=3`.

This is the precise reason that the cubic ledger sits at the critical frontier.

---

## 6. Why the global cubic mass is not yet the required Lyapunov functional

The M5-42/M5-48 outer-cell ancestry permits the critical tail

\[
|U(y,\eta)|\sim \frac{1}{|y|}
\times
\text{bounded angular/log-radial structure}.
\]

For a pure `1/r` magnitude,

\[
\int_{|y|<R}|U|^3dy
\sim
c\log R.
\]

Therefore

\[
\int_{\mathbb R^3}|U|^3dy
\]

need not be finite on the weak-critical blow-up cell.

So the exact global `p=3` identity cannot simply be declared to be a bounded Lyapunov functional on the current recurrent class.

This is a genuine endpoint obstruction, not a technicality to ignore.

---

## 7. Localized cubic identity and its boundary defect

Let `chi_R` be a smooth cutoff equal to one on `|y|\le R` and supported in `|y|\le2R`.

Define

\[
\mathfrak L_R(\eta)
:=
\int \chi_R|U|^3dy.
\]

Repeating the previous calculation gives

\[
\frac13\frac d{d\eta}\mathfrak L_R
+
\nu\mathcal D_{3,R}
=
\int \chi_R P\,\nabla\cdot(|U|U)dy
+
\mathcal B_R[U,P],
\]

where

\[
\mathcal D_{3,R}
:=
\int\chi_R
\left[
|U||\nabla U|^2
+
|U|^{-1}\sum_j(U\cdot\partial_jU)^2
\right]dy
\]

and the cutoff boundary remainder is

\[
\boxed{
\begin{aligned}
\mathcal B_R[U,P]
={}&
\frac16\int |U|^3 y\cdot\nabla\chi_R\,dy
+
\frac13\int |U|^3 U\cdot\nabla\chi_R\,dy\\
&+
\int P|U|U\cdot\nabla\chi_R\,dy
+
\frac\nu3\int |U|^3\Delta\chi_R\,dy.
\end{aligned}
}
\]

Thus localization makes the cubic mass finite but introduces a log-shell boundary flux.

The unresolved issue is now sharply visible:

\[
\boxed{
\text{control/sign of }\mathcal B_R
+
\text{pressure work}
}
\]

must survive the critical `1/r` tail and the recurrent scaling limit.

---

## 8. Three candidate critical objects

### Candidate A — cutoff cubic mass

\[
\mathfrak L_R(U)=\int\chi_R|U|^3.
\]

Advantage: exact local differential identity.

Failure at present: it grows like `log R` for a `1/r` tail and carries the uncontrolled boundary term `\mathcal B_R`.

### Candidate B — tail-renormalized cubic mass

If one could prove a time-independent asymptotic coefficient `kappa`, one could test

\[
\mathfrak L_R^{ren}(U)
:=
\int\chi_R|U|^3
-\kappa\log R.
\]

Advantage: potentially bounded on the critical tail class.

Failure at present: M5-42 allows angular/log-radial structure, so a uniform, orbit-compatible `kappa` has not been proved.

### Candidate C — weak `L^3` or log-shell descriptor

The weak critical quantity

\[
\|U\|_{L^{3,\infty}}^3
\]

is compatible with a `1/r` tail.

Likewise a logarithmic shell mass

\[
\mathfrak S(\rho,\eta)
:=
\int_{e^\rho<|y|<e^{\rho+1}}|U(y,\eta)|^3dy
\]

is order one for a critical `1/r` profile.

Advantage: both are naturally scale critical.

Failure at present: neither has yet been shown to possess a differentiable, sign-definite, additive evolution law along the normalized orbit.

These remain candidate branches, not results.

---

## 9. Audit of the M5-37 strict pressure-tail gap

M5-37 proved that at a positive W1 defect first hit,

\[
\boxed{
\lambda[-Q_P'(\lambda)]
\ge
\nu^2D_\lambda^{surf}
+
\nu^2A_*,
\qquad
A_*>0.
}
\]

This is a strict critical pressure-tail overpay relative to the minimal viscous threshold.

However, its exact logical status is:

\[
\boxed{
\text{necessary payer at a first hit},
}
\]

not

\[
\boxed{
\text{irreversible expenditure of a bounded reservoir}.
}
\]

In particular, the inequality does **not** by itself prove that some bounded functional decreases by a fixed amount between two recurrent returns.

The pressure field is regenerated nonlocally through the pressure-Poisson coupling, and the same normalized critical tail can reappear at smaller physical scales without violating an ordinary finite physical budget.

Therefore M5-37 does not yet satisfy the return-cocycle criterion of Sections 3--4.

This corrects the strongest possible interpretation of the strict gap while preserving the gap itself.

---

## 10. Literature-boundary audit

The current recurrence gate must be kept distinct from already excluded exact self-similar classes.

Relevant partial results include:

1. D. Chae, *Remarks on the asymptotically discretely self-similar solutions of the Navier--Stokes and the Euler equations*, Nonlinear Analysis 125 (2015), 251--259, DOI `10.1016/j.na.2015.05.026`.
   - Locally asymptotically discretely self-similar Navier--Stokes blow-up is excluded when the profile is time-periodic and belongs to an `L^3`-based smooth class.

2. D. Chae and J. Wolf, *Removing discretely self-similar singularities for the 3D Navier--Stokes equations*, Communications in Partial Differential Equations 42 (2017), 1359--1374, DOI `10.1080/03605302.2017.1358275`.
   - The singularity is removed for discrete scaling parameter sufficiently near one; this is not a general elimination of every backward DSS scenario.

3. T. Barker and C. Prange, *Quantitative Regularity for the Navier--Stokes Equations Via Spatial Concentration*, Communications in Mathematical Physics 385 (2021), 717--792, DOI `10.1007/s00220-021-04122-x`.
   - The paper explicitly treats potential nonzero backward DSS solutions as an open class and derives quantitative critical concentration behavior under Type-I control.

The M5 recurrent orbit is more general than an exact periodic orbit in Leray time, and its `1/r` cell ancestry is naturally weak-critical rather than globally `L^3`.

The literature check therefore does not supply the missing cocycle automatically.

It instead confirms that the surviving target lies on a genuine critical/DSS-type boundary.

---

## 11. DSD branch audit

### GREEN — established in this memo

- Parabolic scaling becomes translation in terminal Leray time.
- At `p=3`, the linear similarity term and similarity-drift contribution cancel exactly in the global cubic ledger.
- A bounded functional with a uniform signed decrement on every accepted return would exclude infinite recurrence by telescoping.
- Localization of the cubic ledger produces explicit log-shell boundary terms.
- The M5-37 pressure-tail gap is a strict necessary first-hit payer.

### YELLOW — structurally promising but unclosed

- cutoff cubic mass;
- tail-renormalized cubic mass;
- weak-`L^3` descriptor;
- logarithmic-shell cubic descriptor;
- conversion of the M5-37 pressure-tail overpay into an additive return cocycle.

### RED — interpretations rejected

- treating the M5-37 first-hit gap as already proving monotone depletion;
- using global `L^3` mass as a bounded functional on a generic `1/r` blow-up cell;
- claiming exact/periodic self-similar nonexistence theorems automatically exclude arbitrary aperiodic recurrence.

---

## 12. New exact proof gate

After M5-49 and M5-50, the multiscale problem has been reduced to the following form.

Find a critical functional or cocycle `C` such that:

\[
\boxed{
\begin{array}{ll}
\text{(i)} & C \text{ is bounded on the normalized recurrent orbit closure},\\
\text{(ii)} & C \text{ is additive/telescoping across return intervals},\\
\text{(iii)} & \text{every positive W1 pump return produces a uniform signed gap},\\
\text{(iv)} & \text{the }1/r\text{ tail and pressure-Poisson coupling do not erase that gap}.
\end{array}
}
\]

If such a `C` is constructed, infinite same-trajectory recurrence is impossible.

If no such `C` exists in the cubic/pressure ledger, that branch should be closed rather than forcing a false monotonicity.

The immediate next calculation should therefore attack the **log-shell boundary/pressure term** in Section 7 and test whether the M5-37 strict pressure-tail margin can be converted into a signed shell-to-shell cocycle.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
