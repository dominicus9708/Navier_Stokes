# DSD M5-349 — Affine Shield Saturates the Leslie--Shvydkoy Energy-Measure Exponent Frontier

Date: 2026-08-30

Status: **CRITICAL SCALING FIREWALL / AFFINE 1/5 SHIELD FORCES FAILURE OF EVERY POSITIVE-DIMENSION ENERGY-MEASURE LqLp CORRIDOR AND SATURATES THE ENDPOINT LINE STAGE-BY-STAGE / GLOBAL REGULARITY UNPROVED.**

## 1. Published energy-measure frontier

Leslie--Shvydkoy derive lower local-dimension/concentration-dimension estimates for terminal energy measures from space-time `L_t^q L_x^p` control. In the three-dimensional Navier--Stokes specialization, the finite-`p` positive-density region is represented by the strict inequality

\[
\boxed{
\frac6p+\frac5q<3,
}
\]

with an endpoint line

\[
\frac6p+\frac5q=3.
\]

A positive local-energy radius exponent excludes point atoms. The separate `(p,q)=(infinity,2)` velocity-Type-I endpoint is treated by their Type-I argument and was used in M5-346.

This note audits how the saturated affine shield sits relative to the finite-`p` frontier.

## 2. Affine shield geometry

Let `r -> 0` be the natural first-hitting length. On the saturated energy-bearing affine branch,

\[
\boxed{d\asymp r^{4/5}}
\]

and

\[
|u(x,t)|\asymp r^{-2}|x-X|
\]

on a fixed fraction of `B_d(X)`.

Assume the critical-clock occupancy

\[
\Theta\asymp1,
\]

so the stage persists for natural time

\[
|I|\asymp r^2.
\]

## 3. Spatial Lp size

For finite `p`,

\[
\begin{aligned}
\|u(t)\|_{L^p(B_d)}
&\asymp
r^{-2}d^{1+3/p}\\
&=
 r^{-2}r^{\frac45(1+3/p)}.
\end{aligned}
\]

Hence

\[
\boxed{
\|u(t)\|_{L^p(B_d)}
\asymp
r^{-\frac65+\frac{12}{5p}}.
}
\]

## 4. One-stage LqLp contribution

The `q`th power of the mixed-norm contribution on one natural stage is

\[
\int_I\|u(t)\|_p^qdt
\gtrsim
r^2
r^{-\frac{6q}{5}+\frac{12q}{5p}}.
\]

Therefore

\[
\boxed{
\int_I\|u(t)\|_p^qdt
\gtrsim
r^{e(p,q)},
}
\]

with

\[
\boxed{
e(p,q)
=2-\frac{6q}{5}+\frac{12q}{5p}
=\frac{2q}{5}
\left(\frac6p+\frac5q-3\right).
}
\]

This is the exact exponent identity.

## 5. Compare with the no-atom side

### 5.1 Strict positive-dimension region

If

\[
\frac6p+\frac5q<3,
\]

then

\[
e(p,q)<0.
\]

Thus a late affine stage has

\[
\int_I\|u\|_p^qdt
\gtrsim r^{e(p,q)}\to\infty.
\]

So an energy-bearing saturated affine shield cannot belong uniformly to any strict Leslie--Shvydkoy positive-local-dimension `LqLp` corridor.

### 5.2 Endpoint line

If

\[
\frac6p+\frac5q=3,
\]

then

\[
e(p,q)=0.
\]

Each geometric late stage pays a fixed positive mixed-norm amount. Infinitely many disjoint stages therefore give

\[
\boxed{
\int^{T_*}\|u(t)\|_p^qdt=\infty
}
\]

on the endpoint line as well, provided the affine occupancy repeats on every late first-hitting stage.

### 5.3 Supercritical side

Only

\[
\frac6p+\frac5q>3
\]

gives a positive per-stage exponent and therefore leaves room for summability of the affine contribution.

## 6. Meaning of the 1/5 exponent

The spatial shield exponent `4/5` and the natural time exponent `2` combine so that the exact energy-measure mixed-norm boundary appears without remainder:

\[
\boxed{
e(p,q)\propto \frac6p+\frac5q-3.}
\]

Thus the affine shield is not merely an arbitrary anti-model that happens to evade known criteria. Its energy-saturated spatial extent is exactly tuned to the terminal energy-measure integrability frontier.

This reinforces the interpretation of the `1/5` normalized radius / `4/5` physical radius as a genuine critical barrier.

## 7. Formation consequence

An energy-bearing affine atom cannot be removed merely by searching for a standard `L_t^q L_x^p` energy-measure criterion on the positive-dimension side.

The shield itself forces those norms to fail.

Therefore the remaining information must use structure beyond scalar mixed-norm membership:

- dual hyperbolic axis alignment;
- parent/Oseen same-lineage rigidity;
- dynamic transition/turnover;
- or a new endpoint theorem exactly at/beyond the energy-measure frontier.

## 8. Firewall

Do not infer a contradiction from the divergence of a Leslie--Shvydkoy critical mixed norm. The affine atom predicts exactly such divergence.

Do not claim the published theorem applies in the supercritical region `6/p+5/q>3`; this calculation identifies that region as the only one in which the affine contribution can be summable.

## 9. Audit verdict

### PROVED

- exact one-stage affine `LqLp` exponent `e(p,q)`;
- exact factorization by `6/p+5/q-3`;
- strict no-atom-side norms are incompatible with a saturated affine shield;
- endpoint-line mixed action is nonsummable across geometric stages.

### OPEN

- structural exclusion beyond scalar `LqLp` criteria;
- dual-hyperbolic endpoint rigidity;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]