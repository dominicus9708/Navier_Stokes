# DSD M5-181 — Physical Exterior Backward-Uniqueness Hypothesis Bridge

Date: 2026-08-28

Status: **P1_B EXTERIOR REDUCTION / EVERY SAME-TAIL W1 PAIR PRODUCES TWO PHYSICAL NAVIER–STOKES REALIZATIONS THAT ARE UNIFORMLY SMOOTH AND BOUNDED ON EACH FIXED EXTERIOR CYLINDER UP TO THE TERMINAL TIME, AND THEIR DIFFERENCE HAS ZERO TERMINAL JET THERE / THIS MATCHES THE GEOMETRIC SETTING OF CLASSICAL EXTERIOR BACKWARD-UNIQUENESS RESULTS, BUT THE EXACT FUNCTION-SPACE/BOUNDARY HYPOTHESES OF THE NAVIER–STOKES EXTERIOR THEOREM HAVE NOT YET BEEN VERIFIED / NO CLOSURE CLAIM IS MADE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Same-tail physical realizations

Let `V,W` be two W1 states with the same canonical tail.

Let their complete Leray trajectories generate physical inverse-similarity solutions near a common terminal point `(x_*,T_*)`:

\[
u^V(x,t)
=\tau^{-1/2}V\left(\frac{x-x_*}{\sqrt\tau},s\right),
\qquad
u^W(x,t)
=\tau^{-1/2}W\left(\frac{x-x_*}{\sqrt\tau},s\right),
\]

where

\[
\tau=T_*-t,
\qquad
s=-\log\tau.
\]

Both solve the standard incompressible Navier--Stokes equations for `t<T_*` on the realized W1 interval.

Define

\[
z:=u^V-u^W,
\qquad
q:=p^V-p^W.
\]

---

## 2. Uniform exterior coefficient bounds

Fix `R>0` and set

\[
\Omega_R:=\{x:|x-x_*|>R\}.
\]

The canonical tail and all audited subleading corrections satisfy the far-Leray derivative hierarchy

\[
|\nabla_Y^k U(Y,s)|
\le C_k|Y|^{-1-k}
\]

uniformly on the compact W1 class for sufficiently large `|Y|`.

Physical differentiation gives

\[
\nabla_x^k u
=\tau^{-(1+k)/2}\nabla_Y^kU.
\]

Since

\[
|Y|=\frac{|x-x_*|}{\sqrt\tau},
\]

we obtain the exact cancellation

\[
\boxed{
|\nabla_x^ku(x,t)|
\le
C_k|x-x_*|^{-1-k}
\le C_{k,R}
}
\]

uniformly as `t↑T_*` on `Omega_R`.

Likewise, with the pressure tail order `P=O(|Y|^-2)`,

\[
\boxed{
|\nabla_x^kp(x,t)|
\le C_{k,R}.
}
\]

For vorticity,

\[
\boxed{
|\nabla_x^k\omega(x,t)|
\le C_{k,R}.
}
\]

Thus the apparent Type-I singular coefficient is confined to the shrinking center.  On every fixed exterior cylinder, the physical coefficients are uniformly regular up to the terminal time.

---

## 3. Terminal equality on the exterior

M5-145 proves equality of every algebraic terminal/Fuchsian coefficient for two same-tail W1 states.

M5-139 identifies

\[
z_{Fuchsian}
=\frac{T_*-t}{|x-x_*|^2}.
\]

Therefore for each fixed `x!=x_*`, the physical difference has zero Taylor jet at `t=T_*`:

\[
\boxed{
\partial_t^m z(x,T_*)=0
\qquad\forall m<\infty.
}
\]

In particular,

\[
\boxed{z(x,T_*)=0\qquad x\in\Omega_R.}
\]

The same holds for the relative vorticity.

This is stronger than merely superalgebraic far-field decay in Leray coordinates: it is literal zero terminal data on every fixed punctured physical exterior.

---

## 4. Exact relative Navier--Stokes system

The velocity difference satisfies

\[
\boxed{
\partial_tz-\nu\Delta z
+(u^V\cdot\nabla)z
+(z\cdot\nabla)u^W
+\nabla q=0,
\qquad
\nabla\cdot z=0.
}
\]

All coefficients multiplying `z` or `grad z` are uniformly bounded on

\[
\Omega_R\times[T_* -\varepsilon,T_*]
\]

for every fixed `R,epsilon>0` sufficiently close to the terminal time.

The relative vorticity `eta=curl z` satisfies

\[
\boxed{
\begin{aligned}
\partial_t\eta-\nu\Delta\eta
&+(u^V\cdot\nabla)\eta
-(\eta\cdot\nabla)u^V\\
&+(z\cdot\nabla)\omega^W
-(\omega^W\cdot\nabla)z
=0.
\end{aligned}
}
\]

The velocity form carries pressure; the vorticity form removes pressure but retains the nonlocal recovery of `z` from `eta`.

---

## 5. Exact exterior heat-type theorem comparison

Escauriaza--Seregin--Sverak prove a backward-uniqueness theorem on an exterior region for functions satisfying a local inequality of the form

\[
|\partial_t w+\Delta w|
\le M(|w|+|\nabla w|),
\]

with at-most-Gaussian spatial growth and zero terminal data.

The present W1 exterior fields satisfy the required **coefficient boundedness and spatial growth** much more strongly: they decay algebraically and are uniformly smooth on every fixed exterior.

However the relative vorticity equation contains

\[
(z\cdot\nabla)\omega^W
-(\omega^W\cdot\nabla)z,
\]

and `z` is recovered from `eta` by the global div--curl/Biot--Savart system.  A local pointwise bound

\[
|z|+|\nabla z|
\le C(|\eta|+|\nabla\eta|)
\]

on an exterior domain has **not** been proved and is not generally automatic.

Therefore the scalar/vector heat-type theorem cannot yet be inserted directly into the relative-vorticity equation.

---

## 6. Navier--Stokes exterior theorem route

There is a classical paper:

Brian Straughan, *Backward uniqueness and unique continuation for solutions to the Navier--Stokes equations on an exterior domain*, J. Math. Pures Appl. 62 (1983), 49--62.

Its title and later literature establish that it addresses backward uniqueness for Navier--Stokes on exterior domains.  The exact hypotheses needed to apply its theorem to the pair `(u^V,u^W)` have not yet been recovered/verified in the present audit.

The missing theorem-hypothesis checklist is:

1. precise regularity class of each solution;
2. required spatial integrability/decay at infinity;
3. whether boundary data on the artificial sphere `|x-x_*|=R` must agree;
4. whether the theorem treats two nonlinear solutions directly or a prescribed-pressure/linearized difference;
5. whether finite-energy or bounded-gradient assumptions are required uniformly up to terminal time.

Until these are checked, the implication

\[
\boxed{
\text{terminal-zero exterior same-tail pair}
\Rightarrow
z\equiv0
}
\]

is **YELLOW**, not GREEN.

---

## 7. Why this route is potentially stronger than the spectral-infinity route

If an exterior Navier--Stokes backward-uniqueness theorem applies, then for each `R>0`

\[
z=0
\quad\text{on}\quad
\Omega_R\times[T_* -\varepsilon,T_*].
\]

Since `R` is arbitrary,

\[
z=0
\]

on the whole punctured space near terminal time.

At any earlier fixed smooth Leray time, spatial analyticity then extends equality across the connected whole space, giving

\[
V=W.
\]

This would eliminate **both** statistical and proximal flat fibers at once:

\[
P1_B^S=P1_B^P=\varnothing.
\]

Because this consequence is very strong, theorem-hypothesis verification must precede any use of it.

---

## 8. DSD four-chain audit

### Formation — GREEN

The exterior physical solutions and their terminal data are exact inverse-Leray realizations of the same-tail pair.

### Axis — GREEN

The shrinking singular center is separated from a fixed physical exterior domain.  Bounds are not transported from one axis to the other without the exact scaling calculation.

### Static aggregation — GREEN

No spectral seed/action budget is used in this route.

### Dynamics — GREEN reduction / YELLOW theorem insertion

The relative PDE and terminal-zero data are exact.  The external backward-uniqueness theorem has not yet passed its hypothesis checklist.

### Cross-audit — GREEN

This route does not rely on the corrected M5-179 channel exclusion or on M5-180 spectral regularity thresholds.

---

## 9. Next step

Recover the exact hypotheses of the Straughan exterior Navier--Stokes theorem, or prove a local exterior Stokes/Navier--Stokes backward-uniqueness lemma for the bounded coefficient class in Section 4.

If neither is available, return to the M5-180 coupled spectral action ledger.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
