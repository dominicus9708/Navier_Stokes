# DSD M5-47 — Zeno Pump Ladder and the Critical Clock

Date: 2026-08-27

Status: **EXACT SCALING CONSEQUENCE OF M5-44 / RECURRENT PUMP EVENTS FORM A TERMINAL-ACCUMULATING ZENO LADDER AT ONE FIXED NORMALIZED AMPLITUDE LEVEL / ORDINARY DISSIPATION COSTS ARE SUMMABLE WHILE CRITICAL `D3`-TYPE ACTION IS SCALE-INVARIANT PER COPY / GLOBAL REGULARITY UNPROVED.**

## 1. Terminal-centered recurrence

Let

\[
\sigma_*:=\lambda_c^2.
\]

M5-44 gives recurrent terminal-centered scale returns

\[
\mathcal R_{h_n}V_*	o V_*
\]

for some

\[
h_n\to\infty.
\]

The anchor pump event is placed at

\[
\sigma=0.
\]

---

## 2. Image of the pump under one scaling return

Under terminal-centered scaling by `h`, the anchor time `0` is mapped to

\[
\boxed{
\sigma_h
=
\sigma_*-e^{-h}\sigma_*
=
\sigma_*(1-e^{-h}).
}
\]

Thus the pump copies accumulate at the terminal time:

\[
\sigma_h\uparrow\sigma_*
\qquad(h\to\infty).
\]

The remaining time is

\[
\boxed{
\delta_h
:=\sigma_*-\sigma_h
=
\sigma_*e^{-h}.
}
\]

---

## 3. Spatial and amplitude scales

The corresponding spatial scale is

\[
\boxed{r_h=e^{-h/2}}
\]

relative to the anchor cell, while the velocity amplitude scale is

\[
\boxed{A_h=e^{h/2}}.
\]

Therefore

\[
\boxed{A_hr_h=1.}
\]

Moreover

\[
A_h\sqrt{\delta_h}
=
e^{h/2}\sqrt{\sigma_*e^{-h}}
=
\sqrt{\sigma_*}
=
\lambda_c.
\]

Hence

\[
\boxed{
A_h\sqrt{\sigma_*-\sigma_h}
=\lambda_c
}
\]

for every recurrent pump copy.

Thus all copies lie on the same fixed normalized W1 amplitude level.

---

## 4. Exact Zeno topology

The nested pump sequence has

\[
A_h\to\infty,
\qquad
r_h\to0,
\qquad
\delta_h\to0,
\]

while preserving the Type-I product

\[
A_h\sqrt{\delta_h}=\lambda_c.
\]

This is a Zeno cascade: infinitely many scale-recurrent pump patterns may accumulate in the finite forward interval `[0,sigma_*)`.

The phenomenon is allowed by parabolic scaling and is not a timing contradiction.

---

## 5. Ordinary enstrophy cost per copy

Under Navier--Stokes scaling

\[
V_A(z,\sigma)=A V(Az,A^2\sigma),
\]

ordinary enstrophy scales as

\[
\int|\nabla V_A|^2dz
=A\int|\nabla V|^2dz.
\]

The event duration scales as

\[
\Delta\sigma_A=A^{-2}\Delta\sigma.
\]

Therefore the spacetime enstrophy cost of one normalized pump copy scales as

\[
\boxed{
A\cdot A^{-2}=A^{-1}=r_h.
}
\]

For geometric/nested scales these costs are summable.

Thus the classical total viscous-energy budget does not rule out the recurrent Zeno ladder.

---

## 6. Critical `D3` action per copy

The critical `p=3` dissipation has instantaneous scaling

\[
D_3(V_A)=A^2D_3(V).
\]

Multiplying by the event duration gives

\[
\boxed{
A^2\cdot A^{-2}=1.
}
\]

Hence every normalized recurrent pump copy carries an order-one critical `D3` action whenever the anchor event does.

The same statement holds for the other beta-zero critical formation actions previously identified, such as the streamline-amplitude transport norm at its critical time exponent.

---

## 7. Logarithmic critical divergence

If pump returns occur with positive/syndetic density in Leray time `h`, then the number of recurrent copies up to log-scale depth `H` grows proportionally to `H`.

Since each critical copy costs order one,

\[
\boxed{
\text{critical action up to depth }H
\gtrsim cH.
}
\]

Since

\[
H\sim\log\frac1{\sigma_*-\sigma},
\]

this is exactly the logarithmic strong-critical divergence already found in the earlier W1 endpoint audits.

Thus the Zeno ladder geometrizes the critical-clock saturation.

---

## 8. DSD audit

The nested copies must not be charged as independent order-one costs in ordinary energy or ordinary dissipation ledgers. Their physical costs shrink geometrically.

Conversely, critical beta-zero actions **are** legitimately order one per normalized copy and therefore diverge logarithmically.

This explains, within one same-trajectory spacetime object, why:

- energy remains finite;
- ordinary total dissipation can remain finite;
- strong critical norms/actions fail logarithmically;
- and weak-critical quantities can remain scale-invariant.

---

## 9. Consequence

M5-47 does not produce a contradiction. It proves that the recurrent pump-to-defect cell saturates the exact scaling needed to evade all subcritical budgets while remaining on the critical frontier.

Any new closure must therefore break the Zeno self-similar accounting by a genuinely scale-breaking or sign/rigidity mechanism, not by recounting ordinary costs.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
