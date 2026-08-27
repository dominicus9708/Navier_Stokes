# DSD M5-155 — Uniform W1 Time-Analytic Scale for the Flat-Fiber Problem

Date: 2026-08-27

Status: **ANALYTIC-SCALE INPUT / THE COMPACT W1 CLASS HAS A UNIFORM POSITIVE TIME-ANALYTIC RADIUS ON EVERY FIXED LERAY WINDOW AFTER INVERSE-SIMILARITY TRANSFER TO BOUNDED MILD NAVIER-STOKES SOLUTIONS; TOGETHER WITH EXISTING SPATIAL ANALYTICITY THIS PROVIDES A UNIFORM CROSS-SECTION ANALYTIC CEILING FOR THE M5-154 FREQUENCY-ESCAPE PROBLEM / DERIVATIVES ARE CONTROLLED ONLY AFTER ANALYTIC-RADIUS LOSS, PRESERVING THE M5-152 FIREWALL / GLOBAL REGULARITY UNPROVED.**

---

## 1. Why this input is needed

M5-154 showed that any nonzero flat same-tail fiber must transfer its distinguishability to cross-section frequencies growing at least at the parabolic scale.

M5-152 correctly forbids the shortcut

\[
\|\partial_s f\|\le C\|f\|
\]

on one fixed norm merely from compact analyticity.

The correct framework is an **analytic scale**: a uniform bound on a larger complex strip, with derivative bounds only after shrinking the strip.

---

## 2. Global boundedness of the W1 normalized orbit

The compact W1 class has local smooth compactness on every fixed ball and the established remote Type-I bound

\[
|U(Y,s)|\le A_0(1+|Y|)^{-1}
\]

outside a fixed radius, uniformly in W1 time.

Combining the compact core and the remote tail gives

\[
\boxed{
\sup_{V\in M}\sup_{s\in\mathbb R}\|U(\cdot,s)\|_{L^\infty(\mathbb R^3)}
\le M_\infty<\infty.
}
\]

The same compactness plus the already audited spatial-analytic corridor gives uniform bounds for finitely many spatial derivatives on normalized parent shells.

---

## 3. Transfer one Leray window to standard Navier--Stokes

Fix a Leray time `s0` and a bounded window

\[
|s-s_0|\le h_0.
\]

Using the inverse similarity map with a terminal parameter chosen so that the corresponding physical times stay a fixed positive distance from the similarity endpoint on this finite window, the W1 orbit becomes a standard whole-space Navier--Stokes solution

\[
u(x,t)
\]

on a finite physical time interval.

Because the scale factor varies only by a finite amount on the chosen Leray window and `U` has the global ceiling `M_infty`, the physical solution is a bounded mild solution with a bound depending only on `h0` and `M_infty`, not on the chosen state or the center time `s0`.

No finite-energy or global strong-L3 assumption is needed for this local-in-Leray-time transfer.

---

## 4. External time-analyticity theorem

Dong--Zhang proved pointwise time analyticity for bounded mild incompressible Navier--Stokes solutions in the whole space without a spatial decay assumption.

Joint space--time analyticity estimates for mild Navier--Stokes solutions are also available in the standard equation.

Applied on the uniformly bounded physical windows above and transferred back to Leray time, these results give a radius

\[
\boxed{\delta_s>0}
\]

and a ceiling

\[
\boxed{M_{an}<\infty}
\]

such that every W1 state admits a complex-time extension on

\[
|\operatorname{Im}s|<\delta_s
\]

through every real Leray time, with the corresponding local spatial analytic bounds on every fixed normalized parent shell.

Compactness makes the same `delta_s` and `M_an` usable over the whole minimal W1 class.

---

## 5. Same-tail differences inherit the analytic ceiling

For a same-tail pair `(V,W)`, let

\[
Z=V-W
\]

or use the relative vorticity variable `K` from M5-153.

Both are differences of two functions belonging to the same uniform analytic class. Hence they satisfy an **absolute** analytic ceiling on the same strip.

This does not imply a same-radius relative derivative estimate.

Instead, for any

\[
0<\delta_1<\delta_0<\delta_s,
\]

Cauchy estimates give

\[
\boxed{
\|\partial_s^m f\|_{\delta_1}
\le
\frac{m!}{(\delta_0-\delta_1)^m}
\|f\|_{\delta_0}.
}
\]

This is the only derivative mechanism permitted below.

---

## 6. Flatness passes to a smaller analytic strip

M5-145 gives equality of every algebraic Fuchsian/Taylor coefficient of two same-tail states.

Thus on the real cross-section, for every finite `N`,

\[
\|K(\xi,\cdot)\|_{real}
\le C_N\xi^{-N}
\qquad(\xi\to\infty).
\]

At the same time there is a uniform absolute analytic ceiling on a wider strip.

By standard three-lines/interpolation for analytic functions, for every strictly smaller strip one obtains

\[
\boxed{
\|K(\xi,\cdot)\|_{\delta_1}
\le C_{N,\delta_1}\xi^{-N}
\qquad\forall N.
}
\]

Hence the flat boundary condition is available not only in `C^k` norms but also in every strictly reduced analytic cross-section norm.

---

## 7. Relation to M5-152

There is no contradiction with the M5-152 example

\[
f_n(s)=e^{-n}\sin(ns).
\]

At one fixed strip radius the derivative/amplitude ratio can still diverge.

The present input says only:

1. there is a larger strip with a uniform absolute ceiling;
2. one may spend a positive amount of strip width to estimate derivatives;
3. flatness survives on every strictly smaller strip.

Thus the correct next method is an Ovsyannikov/Cauchy radius-loss argument, not a same-norm Bernstein inequality.

---

## 8. DSD four-chain audit

### Formation — GREEN

The analytic scale is inherited from the actual bounded W1 orbit through finite-window inverse similarity; no terminal-time boundedness is assumed.

### Axis — GREEN

Leray time analyticity is separated from physical terminal-time analyticity.  M5-141 remains unchanged.

### Static aggregation — GREEN

Uniform analytic ceilings are not treated as relative spectral gaps.

### Dynamics — GREEN

Only finite real Leray windows are transferred to the standard bounded mild equation, after which compactness makes the constants uniform along the complete orbit.

### Cross-audit — GREEN/YELLOW

The theorem-level input is standard for bounded mild NSE solutions.  A future final proof package should state explicitly the finite-window inverse-similarity transfer and the uniform selection of the analytic constants as one lemma.

---

## 9. New analytic flat-fiber gate

The M5-154 frequency escape must now satisfy two facts simultaneously:

\[
\Omega(\tau)\gtrsim e^{\tau/2}
\]

and

\[
\|K(\tau)\|_{\delta_1}=O(e^{-N\tau})\quad\forall N
\]

inside a cross-section analytic scale with a fixed positive reserve

\[
\delta_s-\delta_1>0.
\]

The next step is to use the integrable `e^-tau` coefficient in the exact relative equation to prove or disprove a finite analytic-radius-loss Volterra inversion from the flat boundary.

---

## 10. Literature boundary

The external bounded-mild time-analyticity theorem is a local-in-time bounded-solution statement.  It does **not** imply analyticity of the singular physical solution through the terminal time and therefore does not erase the M5-141 flat-terminal gate by itself.

The present use is only on the complete normalized W1 orbit at finite Leray times.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
