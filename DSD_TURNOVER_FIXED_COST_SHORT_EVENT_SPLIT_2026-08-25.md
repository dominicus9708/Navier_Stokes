# DSD Turnover Fixed-Cost / Short-Event Split

Date: 2026-08-25

Status: **ORDER-ONE COMPENSATED TURNOVER SPLIT INTO A FIXED VISCOUS PAYER OR A SHORT FIXED-ACTION BOUNDARY EVENT / BOUNDARY EVENT FINITELY PARTITIONED INTO MATERIAL, RADIAL, VISCOUS-BOUNDARY, PRESSURE PAYERS / GLOBAL REGULARITY UNPROVED.**

## 1. Inputs

From the vorticity-circulation variance floor, on the coherent tracked core

\[
\mathcal W(s)\ge\mathcal W_{core,-}>0,
\]

with

\[
\boxed{
\mathcal W_{core,-}
=
\frac\pi{512q}
\varrho_*^5,
\qquad
\varrho_*
=
\min\left\{
R_Z,
\frac{\rho_0}{2M_0}
\right\}.
}
\]

The compensated moving-ball identity is

\[
\frac12\mathcal W'+\nu E=F_w.
\]

Define on an event interval `J`

\[
\mathscr D_J:=\nu\int_JEds,
\qquad
\mathscr B_J:=\int_J|F_w|ds.
\]

An order-one absolute-action turnover event satisfies at least

\[
\boxed{
\mathscr B_J+\mathscr D_J
>\frac12\mathcal W_{core,-}.
}
\]

This includes the compensated-variation complement. The direct large-boundary-action complement is even stronger.

## 2. Viscous payer or boundary payer

By a two-term pigeonhole,

\[
\boxed{
\mathscr D_J
>\frac14\mathcal W_{core,-}
\quad\lor\quad
\mathscr B_J
>\frac14\mathcal W_{core,-}.
}
\]

The first branch is a fixed local viscous-action event.

The second branch is a fixed absolute physical-boundary-work event.

Thus no order-one compensated turnover is uncharged.

## 3. If the viscous payer is absent, the event is short

Payne-Weinberger plus the compensated variance floor gives pointwise

\[
E(s)
\ge
\frac{\pi^2}{4R_Z^2}\mathcal W(s)
\ge
\frac{\pi^2}{4R_Z^2}\mathcal W_{core,-}.
\]

Therefore

\[
\mathscr D_J
\ge
\nu\frac{\pi^2}{4R_Z^2}
\mathcal W_{core,-}|J|.
\]

If the viscous payer branch is absent, i.e.

\[
\mathscr D_J
\le
\frac14\mathcal W_{core,-},
\]

then

\[
\boxed{
|J|
\le
\frac{R_Z^2}{\pi^2\nu}.
}
\]

Thus any turnover event that tries to avoid a fixed viscous payment must occur inside a uniformly short dynamic-normalized interval.

Status: **PROVED.**

## 4. Split the boundary payer into physical mechanisms

The exact moving relative-variance ledger decomposes the physical boundary term into

\[
F_w
=e^{-A}
\left(
T_{mat}+T_{rad}+T_{vis}+T_{pres}
\right).
\]

Hence pointwise

\[
|F_w|
\le
 e^{-A}
\left(
|T_{mat}|+|T_{rad}|+|T_{vis}|+|T_{pres}|
\right).
\]

If

\[
\mathscr B_J
>
\frac14\mathcal W_{core,-},
\]

then

\[
\sum_{X\in\{mat,rad,vis,pres\}}
\int_J e^{-A}|T_X|ds
>
\frac14\mathcal W_{core,-}.
\]

Therefore at least one physical boundary mechanism satisfies

\[
\boxed{
\int_J e^{-A}|T_X|ds
>
\frac1{16}\mathcal W_{core,-}.
}
\]

Using the explicit variance floor,

\[
\boxed{
\int_J e^{-A}|T_X|ds
>
\frac\pi{8192q}\varrho_*^5.
}
\]

Thus a non-viscous turnover event is not merely short; one of four physical boundary mechanisms carries a fixed absolute action.

## 5. Resulting finite partition

Every order-one compensated turnover event satisfies

\[
\boxed{
T_{abs}
\Longrightarrow
X_{D}
\lor
X_{mat}
\lor
X_{rad}
\lor
X_{vis,bdy}
\lor
X_{pres},
}
\]

where

### Interior viscous payer

\[
X_D:
\qquad
\mathscr D_J
>\frac14\mathcal W_{core,-}.
\]

### Boundary payers

For one `X in {mat,rad,vis,pres}`,

\[
X_X:
\qquad
|J|\le\frac{R_Z^2}{\pi^2\nu},
\]

and

\[
\int_J e^{-A}|T_X|ds
>
\frac1{16}\mathcal W_{core,-}.
\]

This is a finite event partition with explicit event size and, on non-viscous branches, explicit event duration.

## 6. Routing interpretation

- `X_D` feeds the recurrent viscous/enstrophy/H1 ledgers.
- `X_mat` is material/center crossing and feeds replacement/export/return topology.
- `X_rad` is moving-scale radial export/contraction and likewise feeds the turnover/export geometry.
- `X_vis,bdy` is a viscous boundary leakage event and feeds derivative/palinstrophy localization.
- `X_pres` is a fixed pressure-work event on a uniformly short interval; remote pressure cannot be treated as an arbitrarily slow, arbitrarily weak payer on this branch.

The last statement does not yet prove pressure closure; it supplies the missing fixed action and time scale needed by the existing finite parent-pressure/local-residual routing.

## 7. Relation to long-time event frequency

The local event now has two nondegeneracies:

1. fixed normalized action size;
2. for every non-interior-viscous payer, a fixed upper event duration.

Therefore a positive-frequency recurrence of `T_abs` can no longer lose all quantitative content through either

\[
\mathcal W_-	o0
\]

or

\[
|J|\to\infty.
\]

The remaining global issue is event **separation/density** in the appropriate Leray/dynamic clock and the routing of material/radial outward action into recurrent return versus permanent escape.

## 8. Updated frontier

After this split, the only boundary payer with a genuinely global topological option is material/radial export:

\[
\boxed{
\text{return/replenish}
\quad\lor\quad
\text{permanent escape to similarity infinity}.
}
\]

Pressure and viscous payers remain finite local action branches to be compared with existing residual/H1 budgets; they do not create a new geometric infinity by themselves.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]