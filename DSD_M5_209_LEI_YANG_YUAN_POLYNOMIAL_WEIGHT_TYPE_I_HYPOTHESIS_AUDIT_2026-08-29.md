# DSD M5-209 — Lei–Yang–Yuan Polynomial-Weight BU vs Type-I Same-Tail Corridor

Date: 2026-08-29

Parent: `DSD_M5_208_BACKWARD_UNIQUENESS_VS_SPATIAL_SUCP_SCOPE_AUDIT_2026-08-29.md`

Status: **DIRECT THEOREM INSERTION CLOSED / THE 2024 LEI–YANG–YUAN WHOLE-SPACE BACKWARD-UNIQUENESS ARGUMENT REALLY DOES REMOVE THE CALDERÓN–ZYGMUND / NONLOCAL-PRESSURE OBSTRUCTION BY A POLYNOMIAL SPATIAL WEIGHT, BUT ITS NONLINEAR ABSORPTION USES UNIFORM `L^∞` BOUNDS FOR BOTH BACKGROUND VELOCITIES AND THEIR VORTICITIES ON THE TERMINAL WINDOW / THE CURRENT TYPE-I CORRIDOR DOES NOT SUPPLY SUCH UNIFORM TERMINAL-WINDOW BOUNDS / THE CRITICAL SERRIN SCALE IS ALSO ONLY LOGARITHMICALLY BORDERLINE UNDER TYPE-I SCALING / THEREFORE THE PUBLISHED THEOREM IS NOT COUNTED AS APPLIED / GLOBAL REGULARITY UNPROVED.**

---

## 1. External result being audited

Lei–Yang–Yuan prove backward uniqueness for two bounded mild 3D Navier–Stokes solutions in the whole space with the same final data.

Their key weighted estimate uses

\[
h(t)=te^{-t}
\]

and the polynomial spatial weight

\[
(1+|x|^2)^{-k}.
\]

The crucial advantage over a classical exponential Carleman weight is compatibility with the nonlocal Leray / Calderón–Zygmund structure.

Their Lemma 4.1 proves, for

\[
0\le k<\frac52,
\]

a weighted divergence–Calderón–Zygmund estimate of the schematic form

\[
\boxed{
\int (1+|x|^2)^{-k}|\mathcal R\nabla\!\cdot f|^2
\lesssim
\int (1+|x|^2)^{-k}(|\nabla f|^2+|f|^2).
}
\]

This is exactly the kind of pressure-compatible estimate that was missing from the earlier exterior-Hodge discussion.

---

## 2. What their nonlinear absorption actually uses

For the reversed difference `u=u_1-u_2`, their proof estimates

\[
\partial_tu+\Delta u
+\mathbb P\nabla\!\cdot(u_1\otimes u+u\otimes u_2)=0.
\]

After applying the polynomial weighted estimate and Lemma 4.1, the nonlinear part is bounded by

\[
\boxed{
C_{bg}
\int
\chi^2h^{-2a}(1+|x|^2)^{-k}
(|u|^2+|\nabla u|^2),
}
\]

where schematically

\[
\boxed{
C_{bg}
\sim
\|u_1\|_{L^\infty_{t,x}}^2
+\|\nabla\times u_1\|_{L^\infty_{t,x}}^2
+\|u_2\|_{L^\infty_{t,x}}^2
+\|\nabla\times u_2\|_{L^\infty_{t,x}}^2.
}
\]

The proof then uses the short terminal-window length `T_+` to obtain

\[
\boxed{T_+C_{bg}\ll1.}
\]

This absorbs the nonlinear term into the positive weighted heat terms.

So the polynomial weight solves the **nonlocality problem**, but it does not remove the need for a uniformly bounded background on the terminal window.

---

## 3. Type-I terminal scaling fails this hypothesis globally

On the current singular corridor, write

\[
\tau=T^*-t\downarrow0.
\]

Type-I scaling has the natural magnitudes

\[
\|u(t)\|_\infty\sim \tau^{-1/2},
\qquad
\|\omega(t)\|_\infty\sim \tau^{-1}
\]

at the active singular scale.

Therefore on any full window touching `T^*`,

\[
\sup_{0<\tau\le\delta}\|u(t)\|_\infty=\infty,
\qquad
\sup_{0<\tau\le\delta}\|\omega(t)\|_\infty=\infty.
\]

Hence the Lei–Yang–Yuan background constant is not finite on the required full terminal window:

\[
\boxed{C_{bg}=\infty}
\]

in the direct global Type-I interpretation.

Even a heuristic endpoint substitution

\[
C_{bg}(\tau)
\sim
\tau^{-1}+\tau^{-2}
\]

would give no small-window absorption.

Thus

\[
\boxed{
\text{`choose the terminal interval shorter'}
\not\Rightarrow
T_+C_{bg}\ll1
}
\]

for the singular global background.

---

## 4. Critical Serrin audit

The same failure is visible in the scale-invariant Serrin family.

At a Type-I core of radius `sqrt(tau)`, one has for `q>3`

\[
\|u(t)\|_{L^q}
\sim
\tau^{-\frac12+\frac{3}{2q}}.
\]

At the critical Serrin exponent

\[
\frac2p+\frac3q=1,
\]

we have

\[
p=\frac{2}{1-3/q}.
\]

Consequently

\[
\|u(t)\|_{L^q}^p
\sim
\tau^{-1}.
\]

Therefore

\[
\boxed{
\int_0^\delta\|u(t)\|_{L^q}^pdt
\sim
\int_0^\delta\frac{d\tau}{\tau}
=\infty.
}
\]

So the standard critical Ladyzhenskaya–Prodi–Serrin route is exactly logarithmically borderline on the Type-I survivor.

This is consistent with the fact that the current branch is genuinely critical rather than a missed subcritical estimate.

---

## 5. What is genuinely gained from Lei–Yang–Yuan

The paper nevertheless removes one false bottleneck.

The weighted estimate shows that whole-space pressure / Leray projection need not force the use of an exponential spatial Carleman weight.

In particular, the following statement is now audited as too pessimistic:

\[
\text{`Calderón–Zygmund pressure makes whole-space backward uniqueness inaccessible.'}
\]

The correct statement is

\[
\boxed{
\text{CZ nonlocality can be handled polynomially;
 the remaining problem is the singular critical background.}
}
\]

---

## 6. Direct theorem shortcut is RED

The implication

\[
\text{same terminal data}
+\text{finite-energy difference}
\Longrightarrow
\text{apply Lei–Yang–Yuan Theorem 1.1}
\]

is **RED** because the individual backgrounds are not bounded uniformly up to the Type-I terminal time.

The theorem is for bounded mild solutions on the whole terminal interval, not for two singular Type-I realizations whose difference happens to be better behaved.

---

## 7. Correct next test

The correct question is whether the nonlinear absorption can be rebuilt using the already available same-tail decomposition

\[
U_i=B_T+Q_i,
\]

where

- `B_T` is the common weak-`L^3` critical tail;
- `Q_i` are strong-`L^3` quotient terms.

The target is not the published `L^∞` estimate but a critical-form replacement:

\[
\boxed{
\text{polynomial CZ estimate}
+
\text{strong-}L^3\text{ infinitesimal form bound}
+
\text{common-tail principal operator}.
}
\]

The next audit must determine whether the polynomial spatial weight improves the common-tail transport/stretching obstruction found in M5-190/M5-194.

---

## 8. DSD verdict

### Formation — GREEN

The theorem hypotheses and the actual Type-I scalings are compared directly.

### Axis — GREEN

Pressure/CZ compatibility is separated from coefficient size.

### Static aggregation — GREEN

The theorem is not counted as applicable merely because the difference is finite energy.

### Dynamics — YELLOW

A critical-form adaptation of the polynomial weighted estimate remains open.

### Cross-audit — GREEN

This agrees with M5-190: the common arbitrary-amplitude critical background, not pressure itself, is the final whole-space form obstruction.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]