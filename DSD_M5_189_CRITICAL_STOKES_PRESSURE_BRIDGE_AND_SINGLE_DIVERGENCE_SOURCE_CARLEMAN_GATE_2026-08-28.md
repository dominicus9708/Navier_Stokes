# DSD M5-189 — Critical Stokes Pressure Bridge and the Single Divergence-Source Carleman Gate

Date: 2026-08-28

Status: **PRESSURE-COUPLING ORDER AUDIT: GREEN / CRITICAL ABSORPTION ALGEBRA: GREEN / LOG-SQUARE DIVERGENCE-SOURCE PARABOLIC CARLEMAN: OPEN / THE SUBCRITICAL GENERALIZED-STOKES CARLEMAN ARCHITECTURE IDENTIFIES THE EXACT MISSING CRITICAL INPUT; REPLACING THE SUBCRITICAL WEIGHT BY A REGBAOUI LOG-SQUARE WEIGHT RESTORES THE REQUIRED `beta`-SIZED CONVEXITY AT `epsilon=0`, AND ALL CRITICAL OSEEN/STRETCHING TERMS THEN HAVE THE CORRECT ABSORBABLE POWERS / GLOBAL REGULARITY UNPROVED.**

---

## 1. Reference architecture: vorticity + elliptic recovery

For a divergence-free velocity difference `Z`, define the relative vorticity

\[
\eta:=\nabla\times Z.
\]

The pressure-free augmented system is

\[
\boxed{
-\Delta Z=\nabla\times\eta,
\qquad
\nabla\cdot Z=0,
}
\]

and the vorticity equation has divergence-form lower-order forcing

\[
\boxed{
\partial_t\eta-\nu\Delta\eta+\nabla\cdot F=0.
}
\]

For the physical W1 same-tail pair, the tensor `F` has the critical structure

\[
\boxed{
|F|
\le
C\left(r^{-1}|\nabla Z|+r^{-2}|Z|\right),
\qquad r=|x-x_*|.
}
\]

This is the same parabolic-elliptic reduction used in generalized nonstationary Stokes unique-continuation arguments.

---

## 2. What the known subcritical Stokes argument uses

The existing generalized-Stokes quantitative unique-continuation scheme assumes

\[
|A|\lesssim r^{-1+\varepsilon},
\qquad
|B|\lesssim r^{-2+\varepsilon},
\qquad \varepsilon>0.
\]

After taking curl, its forcing satisfies schematically

\[
r|F|
\lesssim
r^{\varepsilon}|\nabla Z|
+r^{-1+\varepsilon}|Z|.
\]

The specially constructed singular weight is designed so that

\[
\boxed{
\beta r^{\varepsilon}
\lesssim
1+\psi''.
}
\]

That inequality is the precise mechanism that turns the small spatial power `r^epsilon` into enough Carleman convexity to absorb the Stokes coupling.

Thus the published subcritical result does **not** directly include the W1 critical case `epsilon=0`.

---

## 3. Why the log-square critical weight changes the balance

The refined Regbaoui/Hardy weight has, in logarithmic radius

\[
y=-\log r,
\]

a quadratic phase of the form

\[
\boxed{
\Psi_\beta(y)\sim \frac\beta2 y^2.
}
\]

Therefore

\[
\boxed{
\Psi_\beta''\sim\beta.
}
\]

At the critical exponent `epsilon=0`, the old required inequality becomes simply

\[
\beta\lesssim1+\Psi_\beta'',
\]

which is now automatically true.

Hence the loss that prevented the subcritical Stokes weight from reaching the endpoint is not a differential-order obstruction; it is a **weight-convexity obstruction**.

The log-square weight supplies exactly the missing endpoint convexity.

---

## 4. Target divergence-source vorticity estimate

Let

\[
W_\beta(r):=e^{\beta(\log r)^2}
\]

up to the standard dimensional power factors.

The needed critical parabolic estimate is the log-square analogue of the divergence-source Carleman estimate:

\[
\boxed{
\begin{aligned}
&\beta\int W_\beta r^4|\nabla\eta|^2
+\beta^3\int W_\beta r^2|\eta|^2\\
&\qquad\le
C\beta^2\int W_\beta r^4|F|^2
+\text{cutoff/time-boundary terms}.
\end{aligned}}
\]

The exact harmless dimensional powers depend on the normalization of the conjugated unknown.  The crucial relative powers are:

- one positive `beta` on the vorticity-gradient channel;
- three powers of `beta` on the vorticity zeroth-order channel;
- only `beta^2` multiplying the divergence-source tensor.

This estimate is **not yet declared proved** in the present repository.

---

## 5. Elliptic velocity estimate with the same weight

The matching singular elliptic Carleman estimate has schematic form

\[
\boxed{
\beta^2\int W_\beta r^2|\nabla Z|^2
+\beta^4\int W_\beta |Z|^2
\le
C\beta\int W_\beta r^4|\Delta Z|^2.
}
\]

Using

\[
-\Delta Z=\nabla\times\eta,
\]

we get

\[
\boxed{
\beta^2\int W_\beta r^2|\nabla Z|^2
+\beta^4\int W_\beta |Z|^2
\le
C\beta\int W_\beta r^4|\nabla\eta|^2.
}
\]

Thus the elliptic velocity channel is subordinate to the positive vorticity-gradient channel.

---

## 6. Critical forcing absorption closes algebraically

From the W1 forcing bound,

\[
|F|^2
\le
C\left(r^{-2}|\nabla Z|^2+r^{-4}|Z|^2\right).
\]

Hence

\[
\boxed{
\beta^2\int W_\beta r^4|F|^2
\le
C\beta^2\int W_\beta r^2|\nabla Z|^2
+C\beta^2\int W_\beta |Z|^2.
}
\]

The first term is exactly one of the positive elliptic velocity channels.

The second is dominated by

\[
\beta^4\int W_\beta |Z|^2
\]

once `beta` is sufficiently large.

Therefore, after multiplying the elliptic estimate by a sufficiently large fixed constant and combining it with the target vorticity estimate, all critical lower-order Stokes/Oseen forcing terms are absorbable.

No smallness of the Type-I coefficient amplitude is required.

Thus

\[
\boxed{
\text{critical pressure/vorticity coupling has no remaining power-counting obstruction.}
}
\]

---

## 7. The single missing lemma

The broad `pressure-compatible Carleman` gate is now reduced to one concrete endpoint statement:

> **Critical log-square divergence-source parabolic Carleman lemma.**  Prove the estimate in Section 4 for
> \[
> \partial_t\eta-\nu\Delta\eta+\nabla\cdot F=0
> \]
> with the same Regbaoui log-square spatial weight used in the critical Hardy estimate.

Once this lemma is GREEN, the elliptic estimate of Section 5 and the algebra of Section 6 close the pressure/Stokes coupling at the level of local singular Carleman coercivity.

The remaining problem would then be terminal-backward localization, not pressure absorption.

---

## 8. Why the published subcritical theorem is not silently promoted

The existing generalized nonstationary Stokes result explicitly assumes a positive subcritical exponent.

The endpoint `epsilon=0` is therefore **not** imported by continuity in epsilon.

The present argument only observes that:

1. the published proof identifies exactly where `r^epsilon` is consumed;
2. the critical log-square weight supplies `Psi'' ~ beta` instead;
3. the resulting endpoint powers close algebraically if the corresponding divergence-source Carleman estimate is proved.

Accordingly:

\[
\boxed{
\text{subcritical theorem} \not\Rightarrow \text{critical theorem}.
}
\]

Only the proof architecture is reused.

---

## 9. DSD four-chain audit

### Formation — GREEN

Pressure is removed only by the legitimate curl/elliptic Stokes structure.  It is not relabeled as an arbitrary forcing.

### Axis — GREEN

Vorticity parabolic coercivity and velocity elliptic recovery remain distinct axes until the final absorption step.

### Static aggregation — GREEN

The forcing tensor is counted once.  The elliptic estimate is an absorption mechanism, not an additional independent budget.

### Dynamics — GREEN for power counting / YELLOW for the endpoint divergence-source estimate

No endpoint Stokes uniqueness is asserted before the missing parabolic lemma is proved.

### Cross-audit — GREEN

No `epsilon -> 0` limit of the published subcritical theorem is assumed.

---

## 10. Updated first large gate

The first remaining major gate now has the form

\[
\boxed{
\begin{aligned}
\text{critical Oseen--Stokes backward Carleman}
={}&\underbrace{\text{critical drift/potential absorption}}_{\text{M5-188 GREEN}}\\
&+\underbrace{\text{critical divergence-source vorticity Carleman}}_{\text{ONE OPEN LEMMA}}\\
&+\underbrace{\text{elliptic Stokes recovery}}_{\text{ALGEBRA GREEN / ESTIMATE STANDARD}}\\
&+\underbrace{\text{terminal-backward localization}}_{\text{OPEN AFTER PRESSURE}}.
\end{aligned}}
\]

This is a substantially narrower obligation than the M5-185/M5-187 formulation.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
