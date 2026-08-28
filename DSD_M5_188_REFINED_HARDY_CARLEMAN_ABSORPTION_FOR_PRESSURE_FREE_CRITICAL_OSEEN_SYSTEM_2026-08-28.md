# DSD M5-188 — Refined Hardy–Carleman Absorption for the Pressure-Free Critical Oseen System

Date: 2026-08-28

Status: **PRESSURE-FREE CRITICAL LOWER-ORDER ABSORPTION: GREEN / TERMINAL-BACKWARD PROPAGATION: YELLOW / THE REGBAOUI-TYPE PARABOLIC CARLEMAN ESTIMATE WITH LOG-SQUARE SPATIAL WEIGHT HAS EXACTLY THE GRADIENT AND ZEROTH-ORDER COERCIVE TERMS NEEDED TO ABSORB `r^-1 grad U` AND `r^-2 U` WITH ARBITRARY FINITE COEFFICIENT SIZE BY TAKING THE CARLEMAN PARAMETER LARGE / THIS REPLACES THE FAILED PURE `-log rho` COMMUTATOR OF M5-187 / IT DOES NOT YET HANDLE PRESSURE OR, BY ITSELF, PROVIDE THE TERMINAL BACKWARD STEP / GLOBAL REGULARITY UNPROVED.**

---

## 1. Why M5-187 failed and what must replace it

M5-187 showed that the naive parabolic-distance weight

\[
\Phi=-\log\rho,
\qquad
\rho^2=|x-x_*|^2+(T_*-t),
\]

has the correct critical homogeneity but an indefinite Hessian.  In particular the tangential Hessian eigenvalue is negative, so the standard symmetric/skew commutator does not yield a positive critical gradient term.

The correct lesson is not that the critical drift is too singular.  It is that the weight was wrong.

The Hardy-type parabolic SUCP literature supplies a different singular Carleman mechanism: use the **spatial radius**

\[
r:=|x-x_*|
\]

and a Regbaoui-type log-square weight.

Because

\[
\rho\ge r,
\]

we have the pointwise domination

\[
\boxed{
\rho^{-1}\le r^{-1},
\qquad
\rho^{-2}\le r^{-2}.
}
\]

Thus any Carleman estimate capable of absorbing the spatial critical terms `r^-1 grad U` and `r^-2 U` is automatically strong enough for the W1 Type-I coefficients from M5-185.

---

## 2. Refined Hardy/Regbaoui parabolic Carleman input

For the heat operator in dimension `n=3`, the refined singular Carleman estimate has the schematic form

\[
\boxed{
\begin{aligned}
&\beta^3\int r^{-3}e^{\beta(\log r)^2}|U|^2
+\beta\int r^{-1}e^{\beta(\log r)^2}|\nabla U|^2\\
&\qquad\le
C\int r\,e^{\beta(\log r)^2}
|\partial_t U-\nu\Delta U|^2,
\end{aligned}}
\]

for sufficiently large `beta` and compactly supported smooth `U` in a sufficiently small punctured spatial ball crossed with a finite time interval.

The complete variable-coefficient version also contains higher-order coercive terms.  Only the two displayed terms are needed for the present order audit.

Reference class:

- Banerjee–Garofalo–Manna, strong unique continuation for the heat operator with Hardy-type potential;
- Banerjee–Ganguly–Ghosh, variable-coefficient parabolic operators with Hardy-type potential, including the Regbaoui-type second Carleman estimate.

The important structural point is the **positive `beta` coefficient in front of the weighted gradient term**.  This is exactly what the first Carleman estimate used earlier did not provide strongly enough for an arbitrary critical first-order drift.

---

## 3. Pressure-free relative Oseen model

Consider a vector field `U` satisfying componentwise

\[
\boxed{
\partial_t U-\nu\Delta U
+a(x,t)\cdot\nabla U
+B(x,t)U=0
}
\]

in a punctured parabolic neighborhood, with

\[
\boxed{
|a(x,t)|\le \frac{M_1}{r},
\qquad
|B(x,t)|\le \frac{M_2}{r^2}.
}
\]

No smallness of `M_1,M_2` is assumed.

Move the lower-order terms to the right:

\[
P U:=\partial_t U-\nu\Delta U
=-a\cdot\nabla U-BU.
\]

Then

\[
|PU|^2
\le
2M_1^2r^{-2}|\nabla U|^2
+2M_2^2r^{-4}|U|^2.
\]

Multiplying by the Carleman RHS weight gives

\[
\boxed{
\begin{aligned}
&\int r e^{\beta(\log r)^2}|PU|^2\\
&\quad\le
2M_1^2
\int r^{-1}e^{\beta(\log r)^2}|\nabla U|^2
+2M_2^2
\int r^{-3}e^{\beta(\log r)^2}|U|^2.
\end{aligned}}
\]

This has exactly the same weighted powers as the two positive terms on the Carleman left-hand side.

---

## 4. Arbitrary finite critical coefficients are absorbed

Choose `beta` so large that

\[
\boxed{
\beta\ge 4CM_1^2
}
\]

and

\[
\boxed{
\beta^3\ge 4CM_2^2.
}
\]

Then both lower-order contributions are absorbed into the left-hand side.

Consequently the pressure-free critical Oseen system satisfies the same local Carleman coercivity as the heat operator, with constants depending on `M_1,M_2` only through the threshold value of `beta`.

Thus

\[
\boxed{
\text{arbitrary finite }r^{-1}\text{ drift}
+
\text{arbitrary finite }r^{-2}\text{ potential}
\text{ are Carleman-subordinate.}
}
\]

This is an **order-and-absorption result**, not a small-data argument.

---

## 5. Application to the W1 physical Type-I coefficient class

M5-185 gives for a same-tail physical pair

\[
|a|\lesssim \rho^{-1},
\qquad
|B|\lesssim \rho^{-2}.
\]

Since `rho >= r`,

\[
|a|\lesssim r^{-1},
\qquad
|B|\lesssim r^{-2}.
\]

Therefore, **if pressure were absent**, the W1 Type-I lower-order coefficients would already lie in the refined Hardy–Carleman absorption class.

This removes the coefficient-size obstruction from the pressure-free branch.

---

## 6. What this does NOT prove

The estimate above is local in a punctured spatial ball and is a unique-continuation Carleman mechanism.

It does **not** yet justify the terminal implication

\[
U(\cdot,T_*)=0
\Longrightarrow
U\equiv0\text{ for }t<T_*
\]

for the full W1 pair.

Two distinct issues remain:

1. the actual relative velocity equation contains the pressure gradient `grad q`;
2. converting the local singular Carleman coercivity into the exact terminal-backward propagation required by the flat-fiber problem needs a time-direction argument or an appropriate backward Carleman localization.

Therefore the legitimate conclusion is

\[
\boxed{
\text{critical lower-order absorption: GREEN},
\qquad
\text{pressure/backward propagation: YELLOW}.
}
\]

---

## 7. Why componentwise application is legitimate at this stage

The pressure-free heat/Oseen principal part is diagonal in the vector components.  The scalar Carleman estimate can therefore be summed componentwise.

No divergence-free assumption is required for the absorption calculation itself.

The divergence-free structure becomes essential only when pressure is restored, because pressure is not an independent forcing but an elliptic constraint channel.

---

## 8. DSD four-chain audit

### Formation — GREEN

The spatial singular variable `r` is formed from the actual blow-up centre.  The parabolic coefficient bounds are only weakened via `rho >= r`; no new singularity is invented.

### Axis — GREEN

Spatial singular radius and terminal time are deliberately kept separate.  This avoids repeating the failed M5-186/M5-187 attempt to force all critical geometry into a single `rho`-weight.

### Static aggregation — GREEN

The drift and potential contributions are not counted as independent budgets.  They are absorbed into the exact matching weighted gradient and zeroth-order Carleman terms.

### Dynamics — GREEN for pressure-free coercivity / YELLOW for terminal propagation

The calculation proves only lower-order subordination.  It does not silently convert spatial strong unique continuation into backward uniqueness.

### Cross-audit — GREEN

No use is made of the invalid pure-log convexity claim, the spectral-infinity heuristic, or an unverified exterior Navier–Stokes theorem insertion.

---

## 9. New frontier

The first of the four remaining large gates is now split as

\[
\boxed{
\text{critical Oseen--Stokes backward Carleman}
=\underbrace{\text{critical drift/potential absorption}}_{\text{GREEN}}
+
\underbrace{\text{pressure-compatible coercivity}}_{\text{OPEN}}
+
\underbrace{\text{terminal-backward localization}}_{\text{OPEN}}.
}
\]

The next calculation should **restore pressure without treating it as arbitrary forcing**.

The correct route is to combine the refined Hardy Carleman estimate for the velocity/vorticity parabolic channel with the elliptic constraint

\[
-\Delta Z=\nabla\times\eta,
\qquad
\nabla\cdot Z=0,
\]

and determine whether the pressure/elliptic channel can be absorbed with the same log-square weight.

Only after that should the terminal-time localization be attempted.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
