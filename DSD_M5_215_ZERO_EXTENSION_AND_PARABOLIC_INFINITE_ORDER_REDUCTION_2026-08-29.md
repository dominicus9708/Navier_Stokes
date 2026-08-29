# DSD M5-215 — Zero Extension and Parabolic Infinite-Order Reduction

Date: 2026-08-29

Parent: `DSD_M5_214_RELATIVE_PRESSURE_POISSON_AND_LARGE_S_ABSORPTION_LEDGER_2026-08-29.md`

Status: **POSITIVE REDUCTION / SAME-TAIL ALL-ORDER TERMINAL FLATNESS PLUS EXACT TERMINAL ZERO ALLOWS ZERO EXTENSION PAST `T_*` ON EVERY FIXED PUNCTURED EXTERIOR WITHOUT A DISTRIBUTIONAL TIME DELTA / THE EXTENDED RELATIVE VELOCITY VANISHES TO INFINITE PARABOLIC SPACE-TIME ORDER AT EVERY TERMINAL EXTERIOR POINT / THIS REPLACES THE NEED FOR TERMINAL TIME ANALYTICITY BY A POINTWISE PARABOLIC SUCP TARGET / THE AUDITED LIN–WANG THEOREM USES A DIFFERENT, STRONGER SPATIAL-VANISHING CONDITION OVER A FIXED TIME WINDOW AND IS NOT COUNTED AS APPLIED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Fixed terminal exterior point

Fix

\[
x_0\ne x_*
\]

and choose

\[
0<\rho<\frac14|x_0-x_*|.
\]

Then

\[
K:=\overline{B_{2\rho}(x_0)}
\]

is a compact punctured set separated from the singular center.

M5-145 gives, for every finite derivative order `k` and every integer `N`,

\[
\boxed{
\|Z(t)\|_{C^k(K)}
\le
C_{N,k,K}(T_*-t)^N
}
\]

for `t<T_*` sufficiently close to `T_*`.

The same statement holds for the relative pressure after fixing the common terminal pressure gauge.

In particular,

\[
Z(\cdot,T_*)=0
\]

smoothly on `K`.

---

## 2. Zero extension past the terminal time

Define on a small interval beyond `T_*`

\[
\widetilde Z(t,x)
:=
\begin{cases}
Z(t,x),&t<T_*,\\
0,&t\ge T_*.
\end{cases}
\]

Likewise choose the relative pressure gauge and set

\[
\widetilde q=0
\qquad(t\ge T_*).
\]

Extend the bounded exterior Oseen coefficients smoothly and arbitrarily to `t>T_*`.

The distributional derivative of a piecewise smooth time function contains a jump term

\[
[Z]_{T_*}\,\delta_{t=T_*}.
\]

But

\[
[Z]_{T_*}=0.
\]

Hence

\[
\boxed{
\partial_t\widetilde Z
}
\]

has no terminal delta source.

Because the equation contains no time derivative of the pressure, the pressure extension likewise creates no temporal delta distribution.

Thus the extended pair satisfies the same linear generalized Oseen–Stokes equation weakly across `t=T_*` on every fixed punctured neighborhood.

With the all-order flatness already available, the extension is in fact `C^∞` in time at `T_*` on each such compact set.

Status: **PROVED.**

---

## 3. Exact parabolic infinite-order estimate

For sufficiently small `r<rho`, define the backward parabolic cylinder

\[
Q_r^-(T_*,x_0)
:=
(T_*-r^2,T_*)\times B_r(x_0).
\]

Using the `k=0` terminal-flat bound,

\[
|Z(t,x)|
\le
C_N(T_*-t)^N
\]

on this cylinder.

Therefore

\[
\begin{aligned}
\iint_{Q_r^-}|Z|^2dxdt
&\le
C_N^2|B_r|
\int_0^{r^2}\tau^{2N}d\tau\\
&=
C_N' r^3 r^{4N+2}.
\end{aligned}
\]

Hence

\[
\boxed{
\iint_{Q_r^-}|Z|^2dxdt
\le
C_N' r^{4N+5}
\qquad\forall N.
}
\]

After zero extension, the same estimate holds on the full centered parabolic cylinder

\[
Q_r(T_*,x_0)
:=(T_*-r^2,T_*+r^2)\times B_r(x_0),
\]

since the future half contributes exactly zero.

Consequently

\[
\boxed{
\iint_{Q_r(T_*,x_0)}|\widetilde Z|^2
=O(r^M)
\qquad\forall M>0.
}
\]

Thus the extended same-tail difference vanishes to **infinite parabolic order at the spacetime point** `(T_*,x_0)`.

Status: **PROVED.**

---

## 4. Why this is stronger than mere terminal smoothness

A generic smooth function satisfying

\[
Z(T_*)=0
\]

need only obey

\[
|Z(t)|=O(T_*-t).
\]

Here all-order same-tail rigidity gives every power.

Therefore the current input is not just terminal Cauchy data; it is the spacetime-point condition naturally used in strong unique-continuation arguments:

\[
\boxed{
\text{infinite parabolic-order vanishing at }(T_*,x_0).
}
\]

No real-analyticity assumption is used.

---

## 5. Scope comparison with Lin–Wang

The audited generalized nonstationary-Stokes result of Lin–Wang studies

\[
\partial_tu-\Delta u+A\cdot\nabla u+Bu+\nabla p=0,
\qquad
\nabla\cdot u=0,
\]

and proves quantitative spatial vanishing estimates under subcritical singular coefficient bounds.

Its stated strong-unique-continuation condition is of the form

\[
\boxed{
\int_{-T}^{T}\int_{B_r(x_0)}|u|^2dxdt
=O(r^N)
\qquad\forall N,
}
\]

where the **time window remains fixed while `r->0`**.

The present M5-215 condition is instead

\[
\boxed{
\int_{T_*-r^2}^{T_*+r^2}
\int_{B_r(x_0)}|\widetilde Z|^2dxdt
=O(r^N)
\qquad\forall N.
}
\]

The time window shrinks parabolically with the spatial radius.

Neither condition implies the other in the direction needed here without an additional theorem.

Therefore Lin–Wang is **not counted as applied**.

---

## 6. New minimal target

The flat-fiber endgame can now be rephrased as follows.

### `PSUCP-OS`

For a generalized nonstationary Oseen–Stokes system with bounded coefficients near one spacetime point,

\[
\partial_tZ-\nu\Delta Z+A\cdot\nabla Z+BZ+\nabla q=0,
\qquad
\nabla\cdot Z=0,
\]

prove that

\[
\iint_{Q_r(t_0,x_0)}|Z|^2=O(r^N)
\quad\forall N
\]

implies

\[
Z\equiv0
\]

in a spacetime neighborhood of `(t0,x0)`.

If this pointwise parabolic SUCP is available, M5-215 supplies its hypothesis at every fixed terminal exterior point.

Then ordinary connected unique continuation at smooth preterminal times would identify the two same-tail realizations.

---

## 7. Relation to the terminal-Carleman route

`PSUCP-OS` and `TBU-OS-gap` are not two unrelated missing theorems.

Both are manifestations of the same local Carleman problem near the terminal hypersurface:

- `TBU-OS-gap` starts from exact terminal zero and uses a one-sided terminal weight;
- `PSUCP-OS` starts from the stronger infinite parabolic-order point condition produced by all-order same-tail rigidity.

The second formulation may be easier because no artificial inner boundary or global exterior geometry appears in the local theorem statement.

Therefore the next priority becomes

\[
\boxed{
\text{local pointwise parabolic SUCP for bounded-coefficient generalized Stokes.}
}
\]

---

## 8. DSD audit

### Formation — GREEN

The zero extension is an actual local distributional solution because the terminal velocity jump is zero.

### Axis — GREEN

Time analyticity and infinite-order parabolic vanishing are kept distinct.

### Static aggregation — GREEN

Lin–Wang's fixed-time-window spatial condition is not relabeled as parabolic-point vanishing.

### Dynamics — YELLOW, newly localized

A local spacetime-point SUCP theorem/estimate remains to be proved or matched.

### Cross-audit — GREEN

This preserves the M5-141 analyticity firewall while using the stronger all-order information of M5-145.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]