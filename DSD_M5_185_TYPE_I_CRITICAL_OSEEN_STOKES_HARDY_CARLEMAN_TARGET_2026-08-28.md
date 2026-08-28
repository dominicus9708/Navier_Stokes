# DSD M5-185 — Type-I Critical Oseen–Stokes Hardy–Carleman Target

Date: 2026-08-28

Status: **W1-CONDITIONAL / THE WHOLE-SPACE SAME-TAIL PHYSICAL DIFFERENCE HAS AN EXACT SCALE-CRITICAL OSEEN–STOKES COEFFICIENT CLASS `|a|~rho^-1`, `|B|~rho^-2` WITH `rho^2=|x-x_*|^2+(T_*-t)` / AT THE LEVEL OF DIFFERENTIAL ORDER THESE TERMS ARE PRECISELY ABSORBABLE BY A HARDY-TYPE PARABOLIC CARLEMAN ESTIMATE WITH LARGE PARAMETER / THE ONLY UNPROVED OBJECT IS A PRESSURE-COMPATIBLE DIVERGENCE-FREE STOKES VERSION OF THAT CRITICAL CARLEMAN ESTIMATE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Physical coefficient class

Let

\[
\vartheta:=T_*-t,
\qquad
r:=|x-x_*|,
\qquad
\rho(x,t):=(r^2+\vartheta)^{1/2}.
\]

For every W1 state in the compact normalized class, previous tail and local-smooth bounds give a uniform profile estimate of the schematic form

\[
|U(Y,s)|\le \frac{C}{1+|Y|},
\qquad
|\nabla_YU(Y,s)|+|\Omega(Y,s)|
\le \frac{C}{(1+|Y|)^2}.
\]

Under inverse Leray scaling

\[
u(x,t)=\vartheta^{-1/2}U\!\left(\frac{x-x_*}{\sqrt\vartheta},s\right),
\]

this becomes

\[
\boxed{
|u(x,t)|\le \frac{C}{\rho(x,t)},
}
\]

and

\[
\boxed{
|\nabla u(x,t)|+|\omega(x,t)|
\le \frac{C}{\rho(x,t)^2}.
}
\]

Higher derivatives have the corresponding parabolic inverse-distance powers.

These estimates are uniform over the compact W1 class.

---

## 2. Relative velocity-pressure system

For same-tail physical realizations `u^V,u^W`, define

\[
Z:=u^V-u^W,
\qquad
q:=p^V-p^W.
\]

Then

\[
\boxed{
\partial_t Z-\nu\Delta Z
+a\cdot\nabla Z
+B Z
+\nabla q=0,
\qquad
\nabla\cdot Z=0,
}
\]

where one may take

\[
a:=u^V,
\qquad
BZ:=(Z\cdot\nabla)u^W.
\]

Therefore

\[
\boxed{
|a(x,t)|\le C\rho^{-1},
\qquad
|B(x,t)|\le C\rho^{-2}.
}
\]

This is exactly scale-critical under the Navier–Stokes parabolic scaling.

---

## 3. Terminal flatness

M5-145/M5-181 give, away from the terminal center,

\[
\partial_t^m Z(x,T_*)=0
\qquad\forall m<\infty,\ x\neq x_*.
\]

At the Fuchsian level the same-tail difference is flat to every algebraic normal order.

The objective is to prove that the homogeneous critical Oseen–Stokes system cannot support a nonzero solution with this terminal flatness.

---

## 4. Differential-order audit

The lower-order terms satisfy

\[
|a\cdot\nabla Z|^2
\le C\rho^{-2}|\nabla Z|^2,
\]

and

\[
|BZ|^2
\le C\rho^{-4}|Z|^2.
\]

Thus the first-order drift costs exactly one critical inverse distance and the zeroth-order strain costs exactly the critical inverse-square potential.

There is **no supercritical coefficient** in the physical relative equation.

This is stronger structural information than the coarse statement

\[
a\in L_t^\infty L_x^{3,\infty}.
\]

---

## 5. Scalar Hardy-Carleman precedent

For scalar heat operators, critical inverse-square potentials are known to admit strong unique-continuation Carleman estimates even for arbitrary finite potential size `M`.

The structural lesson used here is only:

\[
\boxed{
\text{critical }\rho^{-2}\text{ order is not by itself beyond Carleman absorption.}
}
\]

No scalar theorem is inserted as a Stokes theorem.

---

## 6. Exact Stokes-Carleman target

A sufficient estimate would have the following form.

For a terminal/backward weight `Phi` adapted to

\[
\rho^2=r^2+\vartheta
\]

and sufficiently large Carleman parameter `s`, prove for smooth divergence-free test fields `(v,pi)`

\[
\boxed{
\begin{aligned}
& s\int e^{2s\Phi}\rho^{-2}|\nabla v|^2
+s^3\int e^{2s\Phi}\rho^{-4}|v|^2\\
&\qquad\le
C\int e^{2s\Phi}
|\partial_t v-\nu\Delta v+\nabla\pi|^2
+\mathcal B_s[v,\pi].
\end{aligned}}
\]

Here `B_s` must either vanish in the whole-space formulation or be controllable without prescribing artificial lateral boundary data.

The precise powers of `s` may differ in a final optimized estimate; the essential structural outputs are the two critical weighted coercivities

\[
\rho^{-2}|\nabla v|^2,
\qquad
\rho^{-4}|v|^2.
\]

---

## 7. Critical lower-order absorption

Assume the target estimate of Section 6.

For the actual relative solution,

\[
\partial_tZ-\nu\Delta Z+\nabla q
= -a\cdot\nabla Z-BZ.
\]

Hence

\[
\begin{aligned}
\int e^{2s\Phi}|PZ+\nabla q|^2
&\le
C_1\int e^{2s\Phi}\rho^{-2}|\nabla Z|^2\\
&\quad+C_2\int e^{2s\Phi}\rho^{-4}|Z|^2.
\end{aligned}
\]

Because `C_1,C_2` are fixed W1-class constants, sufficiently large `s` absorbs both terms into the left side:

\[
\boxed{
\text{no smallness of the Type-I coefficient is needed once the critical Stokes Carleman is available.}
}
\]

This is the central order calculation of the present note.

---

## 8. Why pressure is now the genuine theorem-level issue

The scalar critical Hardy-Carleman theory does not automatically control

\[
\nabla q,
\qquad
\nabla\cdot Z=0.
\]

Eliminating pressure via vorticity reintroduces the elliptically coupled velocity terms identified in M5-183.

Thus the two equivalent target formulations are:

### Velocity-pressure form

Prove Section 6 directly for the nonstationary Stokes operator.

### Vorticity-velocity form

Combine a critical parabolic Hardy-Carleman estimate for `eta=curl Z` with a simultaneously weighted elliptic estimate for

\[
-\Delta Z=\nabla\times\eta.
\]

The latter is the M5-183 formulation.

No direct equivalence is asserted until the weights and boundary terms are audited.

---

## 9. Relation to existing literature

Current audited literature provides complementary pieces:

- classical heat backward uniqueness with bounded lower-order terms;
- strong unique continuation for critical inverse-square parabolic potentials;
- Stokes/Oseen Carleman estimates and spatial unique continuation;
- whole-space bounded-mild Navier–Stokes backward uniqueness with weighted Calderón–Zygmund control.

No retrieved theorem has yet supplied **all** of:

1. terminal backward propagation;
2. nonstationary Stokes pressure/divergence structure;
3. arbitrary-size critical `rho^-1/rho^-2` coefficients;
4. no artificial boundary equality.

Therefore the target estimate remains YELLOW.

---

## 10. DSD four-chain audit

### Formation — GREEN

The coefficient class is derived from the actual W1 physical scaling, not introduced as an ansatz.

### Axis — GREEN

Spatial inverse distance and terminal parabolic distance are combined only through the scale-covariant quantity `rho`.

### Static aggregation — GREEN

Drift and strain are not treated as new independent budgets; they are lower-order terms to be absorbed into one Carleman coercivity.

### Dynamics — YELLOW

The critical Stokes Hardy-Carleman estimate is not yet proved.

### Cross-audit — GREEN

No smallness, terminal analyticity, artificial boundary condition, or theorem-name substitution is used.

---

## 11. Closure consequence

If the critical Stokes-Carleman target is proved with admissible whole-space/boundary-free terminal weights, then the actual same-tail difference satisfies

\[
Z\equiv0.
\]

Hence both remaining flat branches disappear simultaneously:

\[
\boxed{P1_B^S=P1_B^P=\varnothing.}
\]

This would close the same-tail injectivity problem **inside W1 only**.

The separate global branch-completeness gate would remain open.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
