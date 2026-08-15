# Deep-checkpoint stochastic loop energy--reach dichotomy

Date: 2026-08-16

Status: **DERIVED CONDITIONAL TUBULAR-LOOP ENERGY PACKING LEMMA / STRENGTHENS STOCHASTIC SCALE-SPACE ESCAPE / GLOBAL REGULARITY NOT PROVED.**

## 1. Coherent crossing and deeper adaptive checkpoint

At a coherent Reynolds-one crossing retain

\[
\Gamma_c\gtrsim R^2,
\qquad
R\to\infty,
\]

for the signed circulation around a transverse loop of the coherent core.

Instead of stopping at the automatic reset ratio `W/R^10`, choose a deeper first-hitting ratio

\[
\boxed{
q_\beta=\frac{W}{R^\beta},
\qquad 0<\beta<4.
}
\]

Then the earlier vorticity level is

\[
W_-=W/q_\beta=R^\beta\to\infty,
\]

so this checkpoint remains in the late singular cascade.

In terminal normalization the earlier cap is

\[
\|\Omega_-\|_\infty\le q_\beta^{-1}.
\]

By stochastic Kelvin, there exists a backward stochastic ancestor loop `C_-` whose circulation has the same sign and satisfies

\[
\boxed{
\Gamma_-\ge cR^2.
}
\]

Write

\[
\Gamma:=\Gamma_-,
\qquad
L:=\operatorname{Length}(C_-),
\qquad
\rho:=\operatorname{reach}(C_-).
\]

The terminal-normalized kinetic energy satisfies

\[
K_U=\|U\|_2^2\le C_E W^{1/2}.
\]

---

## 2. Parallel-loop circulation stability under the first-hitting cap

Assume `C_-` has an embedded tubular neighborhood of radius `rho0 <= c rho`. For every small normal offset `z`, let `C_z` be the corresponding parallel loop.

The ribbon joining `C_-` to `C_z` has area

\[
\operatorname{Area}(\mathcal R_z)\lesssim L|z|
\]

as long as `|z|` is below a fixed fraction of the reach.

By Stokes and the pointwise vorticity cap,

\[
|\Gamma(C_z)-\Gamma(C_-)|
\le
q_\beta^{-1}\operatorname{Area}(\mathcal R_z)
\lesssim
\frac{L|z|}{q_\beta}.
\]

Hence all offsets with

\[
|z|\le
c\frac{q_\beta\Gamma}{L}
\]

retain, after choosing the constant small enough,

\[
\boxed{
|\Gamma(C_z)|\ge\Gamma/2.
}
\]

---

## 3. Tube energy lower bound

For each retained offset loop, Cauchy--Schwarz gives

\[
\Gamma(C_z)^2
\le
L_z\int_{C_z}|U|^2ds.
\]

For offsets below a fixed reach fraction, `L_z asymp L`. Thus

\[
\int_{C_z}|U|^2ds
\gtrsim
\frac{\Gamma^2}{L}.
\]

Integrating over a two-dimensional disk of normal offsets of radius

\[
\rho_0
\asymp
\frac{q_\beta\Gamma}{L}
\]

and using tubular coordinates yields

\[
K_U
\gtrsim
\rho_0^2\frac{\Gamma^2}{L}
\asymp
\frac{q_\beta^2\Gamma^4}{L^3},
\]

provided the reach is at least a fixed multiple of `rho0`.

Therefore

\[
\boxed{
L
\gtrsim
q_\beta^{2/3}\Gamma^{4/3}K_U^{-1/3}.
}
\]

Using

\[
\Gamma\gtrsim R^2,
\qquad
K_U\lesssim W^{1/2},
\qquad
q_\beta=W/R^\beta,
\]

we obtain

\[
\boxed{
L_*
\gtrsim
W^{1/2}R^{(8-2\beta)/3}.
}
\]

The earlier natural radius in terminal coordinates is

\[
R_-=\sqrt{q_\beta}
=W^{1/2}R^{-\beta/2}.
\]

Hence

\[
\boxed{
\frac{L_*}{R_-}
\gtrsim
R^{(16-\beta)/6}.
}
\]

---

## 4. Clean reach alternative

Define

\[
\rho_*
:=
 c\frac{q_\beta\Gamma}{L_*}.
\]

If `L<L_*` and `rho >= rho_*`, use offsets only up to `rho_*`. Their circulations remain comparable to `Gamma`, and the preceding energy estimate contradicts the definition of `L_*` after constants are fixed.

Thus every retained stochastic ancestor satisfies the dichotomy

\[
\boxed{
L\gtrsim L_*
\quad\lor\quad
\rho\lesssim\rho_*.
}
\]

Since

\[
q_\beta\Gamma
\asymp
W R^{2-\beta},
\]

one obtains

\[
\rho_*
\asymp
W^{1/2}R^{-(2+\beta)/3}.
\]

Dividing by the earlier natural radius,

\[
\boxed{
\frac{\rho_*}{R_-}
\asymp
R^{(\beta-4)/6}.
}
\]

For every fixed

\[
0<\beta<4,
\]

this tends to zero.

Therefore

\[
\boxed{
\frac{L}{R_-}
\gtrsim
R^{(16-\beta)/6}
\quad\lor\quad
\frac{\rho}{R_-}
\lesssim
R^{(\beta-4)/6}\to0.
}
\]

This is the deep-checkpoint stochastic loop energy--reach dichotomy.

---

## 5. Canonical example beta=2

For

\[
q_2=W/R^2,
\]

the previous level is `W_-=R^2 -> infinity`. The dichotomy becomes

\[
\boxed{
\frac{L}{R_-}
\gtrsim R^{7/3}
\quad\lor\quad
\frac{\rho}{R_-}
\lesssim R^{-1/3}.
}
\]

Thus a stochastic ancestor either spans a super-polynomially growing number (in `R`) of previous natural radii, or loses tubular reach below the previous natural scale.

---

## 6. Diameter--curvature consequence on the long branch

For a closed curve, Chakerian's packing inequality / the elementary integration-by-parts estimate gives

\[
L\lesssim D\,\mathcal K,
\]

where `D` is a containing diameter scale and

\[
\mathcal K=\int_C|\kappa|ds
\]

is total curvature.

On the long branch,

\[
\boxed{
\frac{D}{R_-}\,\mathcal K
\gtrsim
R^{(16-\beta)/6}.
}
\]

Hence at least one of

\[
\boxed{
\frac{D}{R_-}
\gtrsim
R^{(16-\beta)/12}
}
\]

or

\[
\boxed{
\mathcal K
\gtrsim
R^{(16-\beta)/12}
}
\]

must occur.

For `beta=2`, the exponent is `7/6`.

Thus the previous vague scale-space escape is sharpened to

\[
\boxed{
\text{many-natural-radius diameter escape}
\lor
\text{large total curvature}
\lor
\text{sub-natural reach collapse}.
}
\]

The curvature branch returns to the existing strain/Hessian evolution inequality. Reach collapse is a geometric folding / near-self-approach branch and must be charged to higher derivative or multiscale packing. The diameter branch is the remaining genuine spatial escape.

---

## 7. Claim boundary

The parallel-loop tube argument requires an embedded tubular neighborhood and uniform geometric comparability of nearby offsets. Failure of those hypotheses is deliberately recorded as the reach-collapse branch rather than hidden.

The result does not exclude the long-diameter branch and does not prove global regularity.

Overall status: **DEEP ADAPTIVE CHECKPOINTS FORCE STOCHASTIC ANCESTORS INTO POLYNOMIALLY STRONG SCALE-SPACE ESCAPE OR SUB-NATURAL REACH DEGENERATION.**
