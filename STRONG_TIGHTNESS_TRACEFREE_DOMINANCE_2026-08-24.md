# Strong-Tightness Trace-Free Dominance — 2026-08-24

Status: **MASTER CERTIFICATE SIMPLIFIED ON THE STRONG VORTICITY-TIGHTNESS LANE / GLOBAL REGULARITY NOT PROVED.**

This note compares the two tail-independent master exponents after the optimized tightness frequency floor is inserted.

The conclusion is that for the practically relevant strong-tightness range, including the quarter-tail corridor, the universal trace-free route is already stronger than the Betchov-residual absorption route. The latter remains useful outside strong tightness or when stage-wide tightness is unavailable.

---

## 1. Two tightness exponents

Let

\[
\lambda
=
\frac{\Lambda_{tight}(\varepsilon)}{R_Z^2},
\]

\[
Z_+
=
\frac{4\pi R_Z^3}{3(1-\varepsilon)}.
\]

The trace-free exponent per unit `K_I` is

\[
F_{TF}
=
\frac2{\sqrt3}-2\nu\lambda.
\]

The Betchov-absorption exponent per unit `K_I` is

\[
F_B(\delta)
=
1
-2(1-\delta)\nu\lambda
+
\frac{32}{729\pi^4}
\frac{Z_+^2}{\nu^3\delta^3}.
\]

Thus

\[
\boxed{
F_B(\delta)-F_{TF}
=
1-\frac2{\sqrt3}
+2\nu\lambda\delta
+
\frac{32}{729\pi^4}
\frac{Z_+^2}{\nu^3\delta^3}.
}
\]

---

## 2. Optimize the positive correction

Write

\[
a=2\nu\lambda,
\qquad
b=
\frac{32}{729\pi^4}
\frac{Z_+^2}{\nu^3}.
\]

For `delta>0`,

\[
a\delta+b\delta^{-3}
\]

has unconstrained minimum at

\[
\delta_*=(3b/a)^{1/4},
\]

with minimum

\[
\boxed{
\frac43a^{3/4}(3b)^{1/4}.
}
\]

If `delta_*>1`, restricting to `delta<=1` only raises the minimum, so the unconstrained value gives a valid lower bound for all admissible `delta`.

Substitute

\[
\lambda=\Lambda_{tight}/R_Z^2,
\qquad
Z_+=\frac{4\pi R_Z^3}{3(1-\varepsilon)}.
\]

All powers of `R_Z` and `nu` cancel. The result depends only on the tail fraction:

\[
\boxed{
h(\varepsilon)
:=
\inf_{\delta>0}
\left[
2\nu\lambda\delta
+
\frac{32}{729\pi^4}
\frac{Z_+^2}{\nu^3\delta^3}
\right]
}
\]

with

\[
\boxed{
h(\varepsilon)
=
\frac{32}{\sqrt\pi\,3^{11/4}\sqrt{1-\varepsilon}}
\Lambda_{tight}(\varepsilon)^{3/4}.
}
\]

Using

\[
\Lambda_{tight}(\varepsilon)
=
[\sqrt\pi(1-\varepsilon)^{1/4}-\varepsilon^{1/4}]^4,
\]

this becomes

\[
\boxed{
h(\varepsilon)
=
\frac{32
[\sqrt\pi(1-\varepsilon)^{1/4}-\varepsilon^{1/4}]^3}
{\sqrt\pi\,3^{11/4}\sqrt{1-\varepsilon}}.
}
\]

Therefore

\[
\boxed{
F_B(\delta)-F_{TF}
\ge
D(\varepsilon)
:=
1-\frac2{\sqrt3}+h(\varepsilon).
}
\]

---

## 3. Quarter-tail corridor

At

\[
\varepsilon=\frac14,
\]

one has

\[
\Lambda_{tight}\approx0.7885770233
\]

and

\[
\boxed{
h(1/4)\approx0.85034282.}
\]

Hence

\[
\boxed{
D(1/4)
\approx0.69564228>0.
}
\]

So throughout the quarter-tail stage-wide tightness corridor,

\[
\boxed{
F_{TF}<F_B(\delta)
\qquad
\text{for every }0<\delta\le1.
}
\]

Thus the trace-free + tightness-viscosity gate strictly dominates the Betchov-absorption gate there.

---

## 4. Strong-tightness crossover

The equation

\[
D(\varepsilon_c)=0
\]

has numerical root

\[
\boxed{
\varepsilon_c\approx0.64554624.
}
\]

Therefore, at least throughout

\[
\boxed{
0\le\varepsilon_Z\lesssim0.6455,
}
\]

the trace-free gate is no weaker than the Betchov-absorption gate after both are combined with the same optimized Dirichlet tightness floor.

This includes all currently used `epsilon_Z<=1/4` robust corridors by a wide margin.

---

## 5. Consequence for the mainline

On the strong stage-wide vorticity-tight branch the master endgame can be reduced to the single certificate

\[
\boxed{
2K_I
\left(
\frac1{\sqrt3}
-
u\frac{\Lambda_{tight}(\varepsilon_Z)}{R_Z^2}
\right)_+
<\frac12.
}
\]

The Betchov/Hadamard absorption calculation remains valuable for

1. weak tightness `epsilon_Z` near one;
2. corridors where a fixed `R_Z` is unavailable stage-wide;
3. auditing spatial Betchov segregation without declaring it a turnover event.

But it is not an independent mainline obstruction on the quarter-tail tight branch.

---

## 6. Updated priority

For strong tightness, further work on the cubic Betchov remainder does not improve the current best scalar inequality. The only high-leverage constants are now

\[
\boxed{
K_I
\quad\text{and}\quad
R_Z
}
\]

for a chosen `epsilon_Z`.

Therefore the next mainline calculation should either

- lower the continuous first-hitting Type-I constant `K_I`; or
- show that sufficiently large tightness radius `R_Z` necessarily activates a separate multicore/non-tight/remote mechanism.

Status: **ON THE STRONG VORTICITY-TIGHTNESS CORRIDOR, INCLUDING QUARTER TAILS, THE TRACE-FREE VORTEX-STRETCHING BOUND PLUS THE OPTIMIZED DIRICHLET FREQUENCY FLOOR IS STRICTLY STRONGER THAN THE GLOBAL BETCHOV-ABSORPTION ROUTE. THE TIGHT-BRANCH ENDGAME IS THEREFORE REDUCED TO `K_I` VERSUS `R_Z`. GLOBAL REGULARITY REMAINS UNPROVED.**