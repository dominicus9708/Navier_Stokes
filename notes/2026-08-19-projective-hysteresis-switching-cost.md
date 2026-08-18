# Projective coherence/roughness hysteresis switching cost

Date: 2026-08-19

Status: **EXACT THRESHOLD-CROSSING CONSEQUENCE OF THE ENERGY-WEIGHTED PROJECTIVE IDENTITY. REPEATED COHERENT/ROUGH CHANNEL SWITCHING IS NOT FREE: UP-CROSSINGS REQUIRE NONLINEAR PROJECTIVE FORCING; DOWN-CROSSINGS REQUIRE EITHER THE SAME FORCING OR EXACT VISCOUS DERIVATIVE-COVARIANCE DISSIPATION. GLOBAL REGULARITY NOT PROVED.**

## 1. Exact k=0 projective identity

Let

\[
D_0=E_0J_0,
\qquad
J_0=1-\operatorname{tr}(C_0^2).
\]

The exact energy-weighted derivative-projective identity gives

\[
\boxed{
\dot D_0
+2\nu E_1\left[J_1+\|C_1-C_0\|_F^2\right]
=\mathcal N_0,
}
\]

with

\[
\boxed{
|\mathcal N_0|\le 6\sqrt{D_0}\,\mathcal F_0.
}
\]

Here `F0` denotes the L2 amplitude of the differentiated/nonlinear vorticity forcing at order zero.

## 2. Hysteresis thresholds

Fix two dimensionless thresholds

\[
0<d_-<d_+.
\]

Call

\[
D_0\le d_-
\]

a projectively coherent state and

\[
D_0\ge d_+
\]

a projectively rough state.

The gap prevents repeated threshold chatter from being counted as distinct channel changes.

## 3. Up-crossing cost

Suppose an interval begins with

\[
D_0(t_a)\le d_-
\]

and reaches

\[
D_0(t_b)\ge d_+.
\]

The viscous term is nonnegative, hence

\[
d_+-d_-
\le
\int_{t_a}^{t_b}|\mathcal N_0|dt.
\]

During the first threshold crossing one may stop at `D0=d+`, so `D0<=d+` on the counted interval. Therefore

\[
\boxed{
\int_{t_a}^{t_b}\mathcal F_0dt
\ge
\frac{d_+-d_-}{6\sqrt{d_+}}
=:c_\uparrow>0.
}
\]

Thus coherent-to-rough switching requires a fixed nonlinear projective-forcing action.

## 4. Down-crossing cost

Suppose instead

\[
D_0(t_a)\ge d_+,
\qquad
D_0(t_b)\le d_-.
\]

Integrating the exact identity gives

\[
2\nu\int_{t_a}^{t_b}
E_1\left[J_1+\|C_1-C_0\|_F^2\right]dt
=
D_0(t_a)-D_0(t_b)
+\int_{t_a}^{t_b}\mathcal N_0dt.
\]

Hence

\[
\boxed{
2\nu\int
E_1\left[J_1+\|C_1-C_0\|_F^2\right]dt
\ge
(d_+-d_-)
-6\sqrt{d_+}\int\mathcal F_0dt.
}
\]

Consequently every rough-to-coherent crossing satisfies the dichotomy

\[
\boxed{
\int\mathcal F_0dt\ge c_0
\quad\lor\quad
\nu\int
E_1\left[J_1+\|C_1-C_0\|_F^2\right]dt\ge c_1,
}
\]

for constants depending only on the chosen hysteresis thresholds.

## 5. Full cycle

A coherent -> rough -> coherent cycle therefore pays at least one fixed critical amount in

1. nonlinear projective forcing, or
2. exact viscous derivative-projective dissipation.

There is no free strategy in which a compact source-active cell alternates between the Sobolev-gap/coherent lane and the angular/partner rough lane without charging one of the already identified ledgers.

## 6. Limitation

The time integral of palinstrophy/derivative-projective dissipation is not controlled by the ordinary kinetic-energy identity, and the nonlinear projective forcing is itself a critical quantity that may diverge along a hypothetical singular cascade.

Thus the hysteresis lemma prevents unpriced channel switching but does not by itself prove global regularity.

Status: **CHANNEL SWITCHING PRICED / REPEATED SWITCHING ROUTED TO CRITICAL PROJECTIVE FORCING OR EXACT VISCOUS DERIVATIVE-COVARIANCE DISSIPATION.**