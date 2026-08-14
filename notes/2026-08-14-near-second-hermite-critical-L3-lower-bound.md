# Near-second-Hermite pulse forces critical local L3 mass

Date: 2026-08-14

Status: **LOW-CURVATURE TWO-SIDED CRITICAL-VELOCITY ESTIMATE / TRANSPORT DEMAND AMPLIFIED BY LOCAL REYNOLDS NUMBER**.

## 1. Setup

Use a centered isotropic Gaussian of covariance `R^2 I`. Let `r` be the affine-free residual velocity,

\[
\Pi_0r=\Pi_1r=0.
\]

Define

\[
B=\int\gamma_R|\nabla r|^2,
\qquad
D_g=\int\gamma_R|\nabla^2r|^2,
\]

and the Gaussian Poincare curvature surplus

\[
\boxed{H:=R^2D_g-B\ge0.}
\]

Write

\[
r=r_2+h,
\qquad
r_2=\Pi_2r,
\qquad
h=\Pi_{\ge3}r.
\]

The Hermite identities give

\[
B_{\ge3}:=\int\gamma_R|\nabla h|^2\le H.
\]

Hence if

\[
H\le\eta B
\]

with small fixed `eta`, then

\[
\int\gamma_R|\nabla r_2|^2
\ge(1-\eta)B.
\]

## 2. Second-chaos velocity size

For second Hermite chaos, Gaussian Poincare is exact with eigenvalue two:

\[
\int\gamma_R|\nabla r_2|^2
=\frac{2}{R^2}
\int\gamma_R|r_2|^2.
\]

Therefore

\[
\|r_2\|_{L^2(\gamma_R)}
\gtrsim R\sqrt B.
\]

Since the second-chaos space is finite dimensional after whitening, all fixed Gaussian `L^p` norms are equivalent. In particular,

\[
\|r_2\|_{L^3(\gamma_R)}
\gtrsim R\sqrt B.
\]

## 3. Higher-chaos error

The high-chaos part obeys

\[
\|h\|_{L^2(\gamma_R)}^2
\lesssim R^2H,
\qquad
\|\nabla_z h\|_{L^2(\gamma)}^2
\lesssim R^2H.
\]

The Gaussian Sobolev inequality then yields

\[
\|h\|_{L^3(\gamma_R)}
\lesssim R\sqrt H
\le
C\sqrt\eta\,R\sqrt B.
\]

For sufficiently small fixed `eta`, this cannot cancel more than a fixed fraction of the second-chaos `L^3` mass.

Thus

\[
\boxed{
\|r\|_{L^3(\gamma_R)}
\gtrsim R\sqrt B.
}
\]

## 4. Convert to an ordinary local ball

A fixed multiple `B_{CR}` contains a fixed fraction of the Gaussian `L^3` mass of every normalized second-chaos polynomial. The high-chaos error is already small in the full Gaussian `L^3` norm. Hence, after choosing fixed `C` and sufficiently small `eta`,

\[
\int_{B_{CR}}\gamma_R|r|^3
\gtrsim R^3B^{3/2}.
\]

On `B_{CR}`, the Gaussian density is comparable from above to `R^{-3}`, so

\[
\boxed{
\int_{B_{CR}}|r|^3dx
\gtrsim R^6B^{3/2}.
}
\]

Equivalently,

\[
\boxed{
\|r\|_{L^3(B_{CR})}
\gtrsim R^2\sqrt B.
}
\]

Combined with the previously derived upper bound, the near-second-chaos branch has the two-sided estimate

\[
\boxed{
\|r\|_{L^3(B_{CR})}
\asymp R^2\sqrt B
}
\]

up to fixed frame and `eta` constants.

## 5. Local Reynolds interpretation

Define

\[
\mathcal R_G=R^2\sqrt B.
\]

Then near Poincare/Hermite saturation,

\[
\boxed{
\int_{B_{CR}}|r|^3dx
\gtrsim \mathcal R_G^3.
}
\]

Thus an unbounded Gaussian local Reynolds number is accompanied by genuinely unbounded local scale-critical velocity mass; it cannot be only an artifact of the Gaussian gradient statistic.

## 6. Consequence for the transport branch

The previous-checkpoint heat inheritance is `o(B)` on a surviving adaptive pulse. The first-chaos product-gap calculation also shows that a locally stretching-generated near-Hermite pulse must create a higher-chaos certificate.

Therefore, in the complementary subcase where

- higher-chaos stretching production is insufficient;
- affine amplification is bounded;
- previous-checkpoint inheritance is negligible;

formation of the near-Hermite pulse requires critical velocity mass to enter through the local `L^3` balance.

The exact local `L^3` identity then upgrades the old order-one influx requirement to the scale-dependent demand

\[
\boxed{
\left|\int\mathcal F_3ds\right|
+
\left|\int\mathcal P_3ds\right|
\gtrsim
\mathcal R_G^3
}
\]

up to the portion that can be attributed to explicitly retained interior generation.

This is a quantitative strengthening of the shell/pressure branch: near-Hermite transport of a large-Reynolds pulse requires polynomially large critical influx, not merely a fixed positive amount.

## 7. Mesoscopic growth

On the surviving corridor

\[
B\gtrsim W^{-1/3}\Lambda,
\qquad
R\gg W^{1/10+\varepsilon},
\]

we have

\[
\mathcal R_G
=R^2\sqrt B
\gg
W^{1/30+2\varepsilon}\Lambda^{1/2}.
\]

Hence throughout the genuine mesoscopic window the near-Hermite transport demand diverges at least polynomially:

\[
\boxed{
\mathcal R_G^3
\gg
W^{1/10+6\varepsilon}\Lambda^{3/2}.
}
\]

This does not yet provide a finite global flux budget, but it substantially sharpens what a surviving transport branch must accomplish.

Status: **NEAR-HERMITE CRITICAL MASS QUANTIFIED / TRANSPORT BRANCH NOW REQUIRES DIVERGING L3 INFLUX; GLOBAL INFLUX EXHAUSTION STILL OPEN**.
