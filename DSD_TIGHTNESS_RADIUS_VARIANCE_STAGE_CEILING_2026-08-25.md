# DSD Tightness-Radius Variance Stage Ceiling

Date: 2026-08-25

Status: **L_+ ELIMINATED ON THE PURE LOW-TURNOVER SURVIVOR / FAILURE ROUTED TO THE EXISTING VARIANCE-BOUNDARY TURNOVER COMPLEMENT / EXPLICIT SMALL-R_Z CLOSURE DERIVED / GLOBAL REGULARITY UNPROVED.**

## 1. Scope correction

The repository previously used a finite stage ceiling

\[
0<L_j\le L_+<\infty
\]

on the recurrent non-H/T corridor. A direct audit shows that `L_+` must not be treated as a universal consequence of compact recurrence alone.

However, the existing moving-ball variance identity supplies an explicit stage ceiling on the **pure low-turnover variance corridor**. The key is to use that ledger at the already selected enstrophy-tightness radius instead of introducing a second independent radius.

Let the moving tightness ball be

\[
B_{R_Z}(X(s)),
\]

where

\[
\int_{B_{R_Z}(X(s))}|\Omega|^2
\ge
(1-\varepsilon_Z)Z
\]

on the tight recurrent lane.

On this same moving ball define

\[
V_{R_Z}(s)
=
\int_{B_{R_Z}(X(s))}
|U-(U)_{B_{R_Z}}|^2dy.
\]

If the selected center cannot be followed coherently, or the moving ball ceases to represent the same active core, that is the already typed center/material-turnover branch and this pure calculation is not applied.

## 2. Pure variance/boundary partition at R_Z

Use the existing dimensionless descriptors

\[
\Lambda_V=V_+/V_-,
\qquad
\delta_V=\kappa_V/V_-,
\qquad
f_V=F_0/V_-,
\]

and boundary absorption fraction `eta`.

Define the pure low-turnover lane at `R_Z` by

\[
\boxed{
\Lambda_V\le2,
\qquad
\delta_V\le1,
\qquad
f_V\le1,
\qquad
\eta\le\frac12.
}
\]

Failure of any one condition is not retained as an unclassified survivor. It is routed to

\[
\boxed{
T_{var/bdry}(R_Z)
}
\]

consisting of variance excursion, endpoint reshaping, net material/pressure boundary flux, or excessive absorption of interior viscous cost.

Thus the dichotomy is

\[
\boxed{
\text{pure variance persistence at }R_Z
\quad\lor\quad
T_{var/bdry}(R_Z).
}
\]

## 3. Explicit stage ceiling on the pure branch

The exact moving-ball variance/Poincare calculation gives

\[
L_j
\le
\Pi_B\frac{R_Z^2}{\nu},
\]

where

\[
\Pi_B
=\frac{4/\pi^2}{1-\eta}
\left[
\frac14(\log q)\Lambda_V
+f_V
+\frac12\delta_V
\right].
\]

Under the pure thresholds,

\[
\boxed{
\Pi_B
\le
\Pi_{pure}(q)
:=
\frac8{\pi^2}
\left(
\frac12\log q+rac32
\right).
}
\]

Hence every pure stage satisfies

\[
\boxed{
L_j
\le
L_{var,+}
:=
\Pi_{pure}(q)\frac{R_Z^2}{\nu}.
}
\]

For `q=2`,

\[
\boxed{
\Pi_{pure}(2)
\approx1.4967761748.
}
\]

Status: **PROVED on the explicitly stated pure variance corridor.**

## 4. Combine with first-hitting amplification action

The preceding stage-lower-length note proved that a factor-`q` first-hitting amplification requires

\[
\log q
\le
B_0L_j,
\]

where the explicit strain ceiling is

\[
B_0
=
C_I
\left(\frac{M_0}{\rho_0}\right)^{3/5}
Z_{D,tight}^{1/5},
\]

\[
C_I
=
\frac{5\sqrt3}{3}6^{1/5}\pi^{-1/5},
\]

and

\[
Z_{D,tight}
=
\frac{4\pi R_Z^3}{3(1-\varepsilon_Z)}.
\]

Using the pure variance upper time,

\[
\log q
\le
B_0
\Pi_{pure}(q)
\frac{R_Z^2}{\nu}.
\]

Substitute the tightness ceiling:

\[
\boxed{
\log q
\le
C_I\Pi_{pure}(q)
\left(\frac{M_0}{\rho_0}\right)^{3/5}
\left[
\frac{4\pi}{3(1-\varepsilon_Z)}
\right]^{1/5}
\frac{R_Z^{13/5}}{\nu}.
}
\]

Therefore every pure recurrent survivor must satisfy the radius floor

\[
\boxed{
R_Z
\ge
R_{Z,var,-}
:=
\left[
\frac{\nu\log q}
{C_I\Pi_{pure}(q)}
\left(\frac{\rho_0}{M_0}\right)^{3/5}
\left(
\frac{3(1-\varepsilon_Z)}{4\pi}
\right)^{1/5}
\right]^{5/13}.
}
\]

Equivalently,

\[
\boxed{
R_Z
\ge
\left[
\frac{\log q}
{C_I\Pi_{pure}(q)}
\left(
\frac{3(1-\varepsilon_Z)}{4\pi}
\right)^{1/5}
\right]^{5/13}
\nu^{5/13}
\left(\frac{\rho_0}{M_0}\right)^{3/13}.
}
\]

Status: **NECESSARY CONDITION FOR THE PURE RECURRENT SURVIVOR.**

## 5. Numerical q=2 benchmarks

For `q=2`,

\[
C_I\approx3.2855618909,
\qquad
\Pi_{pure}(2)\approx1.4967761748.
\]

If `epsilon_Z=0`,

\[
\boxed{
R_Z
\gtrsim
0.4215625372
\nu^{5/13}
\left(\frac{\rho_0}{M_0}\right)^{3/13}.
}
\]

If `epsilon_Z=1/4`,

\[
\boxed{
R_Z
\gtrsim
0.4123360798
\nu^{5/13}
\left(\frac{\rho_0}{M_0}\right)^{3/13}.
}
\]

These are not universal physical lengths; `R_Z` is the normalized tightness radius in the dynamic first-hitting coordinates.

## 6. L_+ is no longer primitive on the pure survivor

On this branch one may now replace every occurrence of the abstract stage ceiling by

\[
\boxed{
L_+
\rightsquigarrow
L_{var,+}
=
\Pi_{pure}(q)R_Z^2/\nu.
}
\]

This replacement is legitimate only inside the pure low-turnover variance corridor at the selected tightness radius.

If the variance/boundary thresholds fail, the branch is not assigned this ceiling; it has already left to `T_var/bdry(R_Z)`.

Thus no circular use of `L_+` remains in the pure calculation.

## 7. Relation to the existing T ledger

The exact relative-variance identity decomposes the complement into

\[
T_{mat},
\quad
T_{rad},
\quad
T_{vis},
\quad
T_{pres},
\]

plus endpoint/shape variance excursion.

Therefore failure of the pure `R_Z`-ball persistence assumptions does not create a new untyped mathematical case. It feeds the already existing turnover/flux bookkeeping.

What remains globally is to show that positive-frequency recurrence of this complement cannot coexist indefinitely with all existing T budgets, or else to route it to the already isolated escaping passive-tail topology.

## 8. Updated parameter frontier

On the **pure recurrent core** the solution-dependent stage scalar `L_+` has now been eliminated.

The principal finite quantities are reduced to

\[
\boxed{
q,
R_Z,
\varepsilon_Z,
\nu,
M_0,
\rho_0.
}
\]

Here `M_0,rho_0` belong to the universal restart-analyticity input rather than being independent recurrent dynamics variables.

The only remaining alternative to the explicit pure radius window is

\[
\boxed{T_{var/bdry}(R_Z).}
\]

Thus the next high-leverage target is no longer another stage-time estimate. It is to combine positive-frequency `T_var/bdry(R_Z)` with the existing finite-memory replacement/export/flux ledgers and determine whether this complement is already charged, or whether a single precise turnover topology remains open.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]