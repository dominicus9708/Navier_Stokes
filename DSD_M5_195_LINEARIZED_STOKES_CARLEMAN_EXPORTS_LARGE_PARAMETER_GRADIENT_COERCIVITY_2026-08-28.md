# DSD M5-195 — Linearized Stokes Carleman Exports Large-Parameter Gradient Coercivity

Date: 2026-08-28

Status: **P1_B CARLEMAN FRONTIER ADVANCE / IMANUVILOV–LORENZI–YAMAMOTO'S LINEARIZED NAVIER–STOKES CARLEMAN CONTROLS `s |nabla v|^2 + s^3 |v|^2` TOGETHER WITH PARABOLIC SECOND-DERIVATIVE TERMS, AND ITS REMARK ALLOWS `s^-1 |nabla p|^2` TO BE ADDED TO THE LEFT; THEREFORE THE EXACT CRITICAL STRAIN BARRIER FOUND IN M5-194 IS NOT INTRINSIC TO STOKES CARLEMAN THEORY BUT TO THE POLYNOMIAL-WEIGHT BACKWARD ESTIMATE USED THERE / THE PAPER ALSO POINTS TO LINEARIZED-NS CARLEMAN WEIGHTS SINGULAR AT THE TEMPORAL ENDPOINTS; THE NEXT GATE IS HYPOTHESIS/BORDER-TERM MATCHING FOR SUCH A SINGULAR-TIME STOKES ESTIMATE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Linearized NSE treated by the theorem

Imanuvilov–Lorenzi–Yamamoto consider

\[
\boxed{
\partial_t v-\Delta v+(A\cdot\nabla)v+(v\cdot\nabla)B+\nabla p=F,
\qquad \operatorname{div}v=0.
}
\]

This is algebraically the same relative velocity structure as the W1 same-tail pair after coefficient relabeling.

---

## 2. Regular Carleman phase

On a bounded smooth domain and an interior time interval, they choose

\[
\varphi(x,t)
=
\exp\{\lambda(d(x)-\beta(t-t_0)^2)\},
\qquad |\nabla d|\ne0.
\]

For sufficiently large `s`, Theorem 1 controls, schematically,

\[
\boxed{
\begin{aligned}
&\int_Q\Bigl[
 s^{-1}(|\partial_t\operatorname{rot}v|^2+|\partial_tv|^2
       +|\Delta\operatorname{rot}v|^2+|\Delta v|^2)\\
&\qquad\qquad
+s(|\nabla\operatorname{rot}v|^2+|\nabla v|^2)
+s^3(|\operatorname{rot}v|^2+|v|^2)
\Bigr]e^{2s\varphi}
\end{aligned}
}
\]

by source plus spatial-boundary and time-endpoint terms.

The exact feature needed after M5-194 is

\[
\boxed{s\int |\nabla v|^2e^{2s\varphi}.}
\]

Thus the gradient coercivity *does* carry the large parameter.

---

## 3. Pressure is compatible with the same estimate

Their Remark 1 states that one can also estimate

\[
\boxed{
\frac1s|\nabla p|^2e^{2s\varphi}
}
\]

on the left if the source side is strengthened from `|rot F|^2` to `|F|^2+|rot F|^2`.

Hence pressure does not have to be removed by Biot–Savart or by a separate unweighted elliptic reconstruction.

This directly answers the pressure-compatibility question left open in M5-183/M5-190.

---

## 4. Why this matters for the Type-I strain barrier

M5-194 isolated a critical strain contribution of the same unweighted differential scale as

\[
C_S\int |\nabla v|^2.
\]

A Stokes Carleman term

\[
s\int|\nabla v|^2
\]

can absorb any fixed finite `C_S` once

\[
\boxed{s\gg C_S.}
\]

Likewise inverse-square/critical zeroth-order channels can in principle be paid by the stronger

\[
s^3|v|^2
\]

coercivity after the scale weights are matched.

Therefore the obstruction found in M5-194 is **weight-specific**, not a proof that arbitrary Type-I strain is impossible to absorb in any Stokes Carleman estimate.

---

## 5. What the regular theorem does NOT solve

The theorem in this paper uses an interior regular time phase and carries explicit terms at both time endpoints of the local cylinder, plus spatial-boundary terms.

It is designed for lateral continuation/inverse problems, not directly for terminal backward uniqueness.

Thus one may **not** insert Theorem 1 directly into the W1 terminal problem.

The paper itself notes that another type of Carleman weight with singularities at `t=0,T` is available for linearized Navier–Stokes equations in earlier literature.

That remark identifies the correct next literature/derivation gate.

---

## 6. Required singular-time form

The W1 target now has to export, near reverse terminal time `t=0`, a coercive structure of the form

\[
\boxed{
\begin{aligned}
&s\Theta(t,x)|\nabla Z|^2
+s^3\Theta(t,x)^3|Z|^2
+s^{-1}\Theta(t,x)^{-1}|\nabla q|^2\\
&\qquad\lesssim
|L_{A,B}Z+\nabla q|^2
+\text{controlled spatial-boundary/cutoff terms},
\end{aligned}
}
\]

where the time phase is singular strongly enough to suppress the earlier-time cutoff when terminal data vanish.

The exact powers of `Theta` must be taken from the singular-time Stokes theorem rather than guessed.

---

## 7. DSD audit

### Formation — GREEN

The displayed coercive powers are taken from an actual linearized Navier–Stokes Carleman theorem.

### Axis — GREEN

Gradient coercivity, zero-order coercivity, pressure, and endpoint propagation are treated as distinct channels.

### Static aggregation — GREEN

The large `s` gradient gain is not confused with the polynomial-weight estimate of M5-194, where no such gain existed.

### Dynamics — GREEN for regular Stokes coercivity / YELLOW for terminal singular adaptation

The critical strain barrier is potentially absorbable; terminal backward propagation remains to be matched.

### Cross-audit — GREEN

No conclusion that `P1_B` is closed is made from an interior-time Carleman estimate.

---

## 8. Next gate

Recover the singular-time linearized Navier–Stokes Carleman cited by the paper, and audit:

1. exact time/spatial phase;
2. coefficient regularity and amplitude assumptions;
3. parameter-enhanced gradient/zero-order terms;
4. pressure treatment;
5. time-endpoint and lateral-boundary terms;
6. whether W1 terminal all-jet flatness removes the terminal contribution and whether spatial cutoff terms can be exponentially separated.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
