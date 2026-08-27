# DSD M5-141 — Terminal-Analyticity Scope Audit for the Flat Fiber

Date: 2026-08-27

Status: **P1_B LITERATURE/SCOPE AUDIT / PUNCTURED `C^infinity` TERMINAL EXTENSION DOES NOT CURRENTLY UPGRADE, UNDER THE ESTABLISHED W1 HYPOTHESES ALONE, TO A UNIFORM TIME-ANALYTIC EXTENSION THROUGH THE TERMINAL TIME / AVAILABLE WHOLE-SPACE TIME/JOINED-ANALYTICITY THEOREMS USE GLOBAL BOUNDED-MILD, `L3`, SERRIN, OR RELATED FUNCTION-SPACE HYPOTHESES NOT AVAILABLE FOR THE LARGE CRITICAL `1/r` W1 PHYSICAL BACKGROUND / THE FUCHSIAN-FLAT FIBER REMAINS OPEN / GLOBAL REGULARITY UNPROVED.**

---

## 1. Why analyticity would matter

After M5-139/M5-140, a same-tail fiber can have an algebraic integer multipole hierarchy or, after all such coefficients are matched, a remainder flat at the Fuchsian boundary:

\[
Z=O(z^N)
\qquad\text{for every finite }N.
\]

If the physical difference were real analytic in terminal time at fixed punctured position, then

\[
z=\frac{T_*-t}{|x-x_*|^2}
\]

would make such infinite-order vanishing imply

\[
Z\equiv0
\]

in a terminal neighborhood.

Thus time analyticity would close `P1_B`.

---

## 2. What is already proved internally

The repository proves smooth extension to `t=T_*` on every compact subset of

\[
\mathbb R^3\setminus\{x_*\}.
\]

Consequently arbitrarily many finite terminal derivatives exist locally away from the center.

This is enough to eliminate every fixed noninteger Puiseux power, as in M5-139.

It is not enough to eliminate a flat function such as a schematic

\[
e^{-1/z}.
\]

`C^infinity` is not quasi-analytic.

---

## 3. External analyticity results and their scope

Known incompressible Navier–Stokes time and joint space-time analyticity results include:

- pointwise time analyticity for globally bounded mild solutions in the whole space;
- joint space-time analyticity for mild solutions under global critical-space hypotheses such as `L3`;
- analyticity results in Serrin/maximal-regularity classes;
- interior/spatial analyticity results on regular domains.

These are important, but the current W1 physical realization has a large critical punctured background

\[
|b(x)|\lesssim |x-x_*|^{-1}
\]

and is not globally bounded or globally strong-`L3` near the terminal event.

Therefore the available whole-space hypotheses cannot be inserted automatically.

---

## 4. Why local boundedness away from the center is not enough by itself

On a fixed punctured annulus the solution is uniformly bounded and smooth.

However pressure is nonlocal and the whole-space solution retains a singular center.

A theorem requiring a globally bounded mild solution cannot be localized merely by restricting the spatial domain, because the induced boundary/pressure data are not automatically known to satisfy the same analyticity hypotheses.

Thus the inference

\[
\text{locally bounded on an annulus}
\Rightarrow
\text{uniform terminal time analyticity on that annulus}
\]

requires a separate theorem adapted to the singular external environment.

No such theorem has been established in the current W1 audit.

---

## 5. DSD four-chain audit

### Formation — GREEN

The flat branch is defined only after all algebraic Fuchsian coefficients have been matched.

### Axis — GREEN

Finite differentiability, `C^infinity`, and real analyticity are treated as distinct regularity levels.

### Static aggregation — GREEN

Global analyticity theorems are not reclassified as local theorems by dropping their global hypotheses.

### Dynamics — GREEN

The terminal singular center remains part of the dynamical environment even when observing a punctured annulus.

### Cross-audit — GREEN

M5-139 remains valid: smoothness removes fractional powers. M5-141 only blocks the unjustified stronger conclusion that smoothness removes flat modes.

---

## 6. Literature boundary

Representative relevant results include:

- Dong–Zhang, time analyticity for bounded mild incompressible Navier–Stokes solutions;
- Wang–Gao–Xue, joint space-time analyticity of mild solutions under global critical-space hypotheses;
- later maximal-regularity/Serrin-class analyticity results.

None is presently imported as a theorem for a solution that is only locally regular away from one large critical terminal singular center.

---

## 7. RED firewall

The route

\[
\text{punctured }C^infinity
\Rightarrow
\text{punctured time analytic through }T_*
\Rightarrow
\text{flat fiber}=0
\]

is RED at the first implication under the current established hypotheses.

---

## 8. P1_B remains a genuine gate

The flat same-tail branch is now precisely:

\[
\boxed{
\text{a strong critical difference that vanishes to every algebraic order at the Fuchsian/terminal boundary but may concentrate at the parabolic center scale.}
}
\]

Closing it requires either

1. a backward-uniqueness theorem adapted to the large shared `1/r` critical background;
2. a terminal analyticity theorem valid under punctured local regularity plus controlled singular center;
3. or a global finite-energy prelimit argument excluding an infinitely flat center-concentrating difference.

---

## 9. Updated P1 status

`P1_A`: global selection of integer odd pressure multipoles.

`P1_B`: Fuchsian-flat / large-critical-background backward uniqueness.

Neither is closed by local smoothness alone.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]