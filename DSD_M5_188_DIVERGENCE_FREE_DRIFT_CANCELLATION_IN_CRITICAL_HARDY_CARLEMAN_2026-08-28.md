# DSD M5-188 — Divergence-Free Drift Cancellation in Critical Hardy–Carleman

Date: 2026-08-28

Status: **P1_B CRITICAL CARLEMAN REFINEMENT / GENERAL SCALE-CRITICAL GRADIENT-POTENTIAL THEOREMS REQUIRE SMALLNESS OR DYADIC CONTROL THAT IS NOT AVAILABLE FOR A GENERAL LARGE W1 TYPE-I DRIFT; HOWEVER THE NAVIER–STOKES TRANSPORT FIELD IS DIVERGENCE FREE, SO ITS TOP FIRST-ORDER CONTRIBUTION IS SKEW IN THE CONJUGATED ENERGY AND ONLY THE WEIGHT COMMUTATOR SURVIVES, AT THE SAME INVERSE-SQUARE ORDER AS THE ALREADY-CRITICAL POTENTIAL / THIS REDUCES THE LARGE-DRIFT OBSTRUCTION TO PRESSURE/STRETCHING AND A COUPLED PARABOLIC–ELLIPTIC CARLEMAN PROBLEM / GLOBAL REGULARITY UNPROVED.**

---

## 1. Literature boundary

The refined Hardy-type parabolic Carleman estimate of Banerjee–Garofalo–Manna uses the weight

\[
r^{-\alpha}e^{\alpha r^\varepsilon}
\]

and yields a critical inverse-square coercive term together with an additional subcritical positive term.  It handles an unrestricted scalar potential of size `M/r^2` by taking the Carleman parameter sufficiently large.

By contrast, the general Koch–Tataru parabolic theory allows gradient potentials in scale-invariant spaces only under smallness/dyadic summability hypotheses.  The W1 Type-I drift is scale-critical but not known small.

Therefore the implication

\[
|a|\lesssim \rho^{-1}
\Longrightarrow
\text{apply a generic gradient-potential SUCP theorem}
\]

is **RED**.

---

## 2. Relative velocity equation

For two same-tail physical realizations let

\[
Z=u^V-u^W.
\]

Use the asymmetric relative form

\[
\boxed{
Z_t-\nu\Delta Z
+(u^V\cdot\nabla)Z
+(Z\cdot\nabla)u^W
+\nabla q=0,
\qquad \nabla\cdot Z=0.
}
\]

Set

\[
a:=u^V,
\qquad
B:=\nabla u^W.
\]

The W1 Type-I geometry gives

\[
|a|\le C\rho^{-1},
\qquad
|B|\le C\rho^{-2},
\qquad
\rho^2=|x-x_*|^2+T_*-t.
\]

Most importantly,

\[
\boxed{\nabla\cdot a=0.}
\]

---

## 3. Conjugated divergence-free transport

Let a Carleman weight be `phi` and write

\[
Z=e^{-s\phi}V.
\]

Then

\[
e^{s\phi}(a\cdot\nabla)(e^{-s\phi}V)
=
a\cdot\nabla V
-s(a\cdot\nabla\phi)V.
\]

For compactly supported test fields,

\[
\operatorname{Re}\int (a\cdot\nabla V)\cdot V
=
\frac12\int a\cdot\nabla|V|^2
=-\frac12\int (\nabla\cdot a)|V|^2
=0.
\]

Hence

\[
\boxed{
\text{the top first-order drift is energy-skew.}
}
\]

The only scalar contribution created by the Carleman conjugation is

\[
-s(a\cdot\nabla\phi)V.
\]

For any critical radial weight with

\[
|\nabla\phi|\lesssim \rho^{-1},
\]

we obtain

\[
\boxed{
|s a\cdot\nabla\phi|
\lesssim
s\rho^{-2}.
}
\]

Thus the large Type-I transport is converted from a gradient perturbation into an inverse-square zeroth-order perturbation.

---

## 4. Consequence for large drift

A critical Hardy–Carleman inequality is designed to control terms of the form

\[
M\rho^{-2}V
\]

for arbitrary finite `M` by choosing the large Carleman parameter.

Therefore the amplitude of the divergence-free drift does not by itself force a smallness hypothesis.

The legitimate target is now

\[
\boxed{
\text{Hardy–Carleman for the Oseen operator with divergence-free drift}
}
\]

rather than a generic gradient-potential Carleman estimate.

---

## 5. Remaining terms

Two non-skew channels remain.

### 5.1 Stretching / matrix potential

\[
BZ=(Z\cdot\nabla)u^W,
\qquad
|B|\lesssim\rho^{-2}.
\]

This is exactly critical zeroth order and is compatible in differential order with the Hardy coercive term.

### 5.2 Pressure

\[
\nabla q
\]

is not eliminated by the divergence-free transport cancellation.

Taking curl removes pressure but introduces the coupled velocity terms

\[
(Z\cdot\nabla)\omega^W-(\omega^W\cdot\nabla)Z.
\]

Thus pressure/nonlocality remains the actual obstruction.

---

## 6. Coupled local formulation

Let

\[
\eta=\nabla\times Z.
\]

Then

\[
\boxed{
\begin{cases}
\eta_t-\nu\Delta\eta
+(u^V\cdot\nabla)\eta
-(\eta\cdot\nabla)u^V
+(Z\cdot\nabla)\omega^W
-(\omega^W\cdot\nabla)Z=0,\\
-\Delta Z=\nabla\times\eta,\\
\nabla\cdot Z=0.
\end{cases}
}
\]

The coefficient sizes are

\[
|u^V|\lesssim\rho^{-1},
\quad
|\nabla u^V|+|\omega^W|\lesssim\rho^{-2},
\quad
|\nabla\omega^W|\lesssim\rho^{-3}.
\]

After the drift cancellation, the remaining critical terms have the schematic sizes

\[
\rho^{-2}\eta,
\qquad
\rho^{-2}\nabla Z,
\qquad
\rho^{-3}Z.
\]

This makes the next required estimate explicit.

---

## 7. Shifted elliptic Carleman required by the coupling

A standard elliptic Carleman scale for

\[
-\Delta Z=\nabla\times\eta
\]

has the form, schematically,

\[
\tau^3\int r^{-2\tau-4}|Z|^2
+
\tau\int r^{-2\tau-2}|\nabla Z|^2
\lesssim
\int r^{-2\tau}|\Delta Z|^2.
\]

Applying the same estimate with the exponent shifted by one gives the critical matching

\[
\boxed{
\tau^3\int r^{-2\tau-6}|Z|^2
+
\tau\int r^{-2\tau-4}|\nabla Z|^2
\lesssim
\int r^{-2\tau-2}|\nabla\eta|^2.
}
\]

This is exactly the scale needed to absorb

\[
r^{-3}Z
\quad\text{and}\quad
r^{-2}\nabla Z
\]

into a parabolic Carleman estimate for `eta`, provided the latter exports a weighted gradient coercive term.

This is a **target estimate**, not yet a completed coupled proof.

---

## 8. DSD audit

### Formation — GREEN

The divergence-free property belongs to the actual NSE drift and is not an added hypothesis.

### Axis — GREEN

Drift, stretching, pressure, and elliptic reconstruction are kept as separate channels.

### Static aggregation — GREEN

The drift is not squared as a generic forcing before exploiting its skew structure.

### Dynamics — GREEN for drift cancellation / YELLOW for coupled closure

The large drift obstruction is removed at the conjugated-energy level.  Pressure/velocity reconstruction remains open.

### Cross-audit — GREEN

This does not contradict Koch–Tataru: their generic gradient-potential smallness is bypassed only because NSE supplies the additional divergence-free algebraic structure.

---

## 9. Next gate

The next concrete calculation is:

1. extract/derive a **gradient-retaining refined Hardy parabolic Carleman** for vector heat/vorticity;
2. pair it with the shifted elliptic Carleman above;
3. verify that
   \[
   \rho^{-2}\eta,
   \quad
   \rho^{-2}\nabla Z,
   \quad
   \rho^{-3}Z
   \]
   are all absorbable for sufficiently large Carleman parameter;
4. only then reinsert the terminal-flat condition.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
