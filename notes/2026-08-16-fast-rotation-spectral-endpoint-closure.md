# Fast-rotation spectral endpoint closure on the spatially tight branch

Date: 2026-08-16

Status: **LOW TURNOVER FREQUENCY IS DEPLETED BY SPATIAL UNCERTAINTY; HIGH TURNOVER FREQUENCY IS ROUTED TO DERIVATIVE/HIGH-HERMITE CONCENTRATION. COMBINED WITH THE ANALYTIC NEAR-RESONANCE LEMMA, THE SPATIALLY TIGHT BOUNDED-DERIVATIVE FAST-ROTATION SPECTRAL BRANCH HAS NO SURVIVING ORDER-ONE SECULAR SOURCE. GLOBAL REGULARITY NOT PROVED.**

## 1. Spatially tight turnover packet

Let `G(z)` denote a turnover-scale residual-gradient packet localized to a fixed ball

\[
|z|\le C.
\]

Then

\[
\|G\|_1\le C\|G\|_2,
\]

and Fourier inversion gives

\[
\boxed{
\|\widehat G\|_\infty
\le C\|G\|_2.
}
\]

This is the same localization input used in the near-slow and analytic near-resonance depletion lemmas.

## 2. Low-frequency endpoint

For `0<lambda<1`,

\[
\begin{aligned}
\|P_{\le\lambda}G\|_2^2
&=
\int_{|\xi|\le\lambda}|\widehat G(\xi)|^2d\xi\\
&\le
C\lambda^3\|\widehat G\|_\infty^2.
\end{aligned}
\]

Hence

\[
\boxed{
\|P_{\le\lambda}G\|_2
\lesssim
\lambda^{3/2}\|G\|_2.
}
\]

At the coherent source scale the quadratic residual-gradient source carries the basic factor `R^-2`. Therefore, if one input is confined to frequencies `|xi|<=lambda_R` with `lambda_R->0`,

\[
|J_{\rm low}|
\lesssim
R^{-2}\lambda_R^{3/2},
\]

and over the full `O(R^2)` source interval,

\[
\boxed{
\int_0^{cR^2}|J_{\rm low}|dt
\lesssim
\lambda_R^{3/2}
\to0.
}
\]

Thus a spatially tight low-frequency escape cannot provide an order-one secular source.

## 3. High-frequency endpoint

For `Lambda>1`, Plancherel gives

\[
\begin{aligned}
\|P_{\ge\Lambda}G\|_2^2
&=
\int_{|\xi|\ge\Lambda}|\widehat G|^2d\xi\\
&\le
\Lambda^{-2}
\int|\xi|^2|\widehat G|^2d\xi.
\end{aligned}
\]

Therefore

\[
\boxed{
\|P_{\ge\Lambda}G\|_2
\le
\Lambda^{-1}\|\nabla G\|_2.
}
\]

If `||nabla G||_2` remains bounded on the turnover block, every escape `Lambda_R->infinity` is negligible.

If the high-frequency contribution remains non-negligible, then necessarily

\[
\boxed{
\|\nabla G\|_2
\gtrsim
\Lambda_R
}
\]

along a subsequence.

Since `G` is already a residual-gradient packet, `nabla G` is one more spatial derivative of the residual velocity / vorticity-scale state. Hence the surviving high-frequency endpoint is exactly a higher-Hermite / palinstrophy / derivative-radius-collapse channel.

## 4. Spectral trichotomy

Choose frequency cutoffs

\[
0<\lambda\ll1\ll\Lambda.
\]

Every spatially tight packet decomposes into

\[
G
=
P_{\le\lambda}G
+P_{[\lambda,\Lambda]}G
+P_{\ge\Lambda}G.
\]

The first term is small by Section 2.

The third term is small on the bounded-derivative branch and otherwise is the derivative escape of Section 3.

The middle term lies on a fixed compact turnover-frequency annulus. There:

1. nonresonant interactions are oscillatory and perturbative unless time/modulation derivatives become large;
2. near-slow spatially tight inputs were already depleted by the `delta^(1/2)` uncertainty gain;
3. uniformly-fast near-resonant interactions were depleted by the real-analytic sublevel estimate, including Van-Hove critical points through a degraded but positive sublevel exponent.

Thus the compact middle-frequency branch does not sustain the required order-one secular source under the established bounded-modulation hypotheses.

## 5. Fast-rotation branch after spectral closure

A source-active fast-rotation sequence must therefore trigger at least one of

\[
\boxed{
\text{spatial non-tightness},
\quad
\text{high-derivative/high-Hermite concentration},
\quad
\text{rapid time/axis modulation},
\quad
\text{symmetric-affine deformation}.
}
\]

The last two are already typed by projective/time-mixing and affine-strain ledgers.

Consequently there is no remaining **purely spectral, spatially tight, bounded-derivative resonant escape**.

## 6. Relation to the renormalization loop

The residual-seed branch of the recent-source renormalization loop returns to a fast coherent Reynolds-one crossing.

This note shows that, once at such a crossing, the fast-rotation resonant source cannot remain both

- spatially tight, and
- derivative/modulation bounded.

Hence recursive return through the residual-seed branch must pay a new structural cost each cycle:

\[
\boxed{
\text{spatial escape}
\quad\lor\quad
\text{derivative/modulation growth}
\quad\lor\quad
\text{logarithmic symmetric strain}.
}
\]

This is stronger than a scalar energy/time lower bound, but a cross-cycle nonrepeatability theorem is still needed to prove global regularity.

Status: **LOW-FREQUENCY TIGHT ESCAPE CLOSED / HIGH-FREQUENCY ESCAPE ROUTED TO DERIVATIVES / COMPACT-FREQUENCY NEAR-RESONANCE ALREADY DEPLETED / NO PURE TIGHT BOUNDED-DERIVATIVE FAST-ROTATION SPECTRAL SURVIVOR / GLOBAL REGULARITY NOT PROVED.**