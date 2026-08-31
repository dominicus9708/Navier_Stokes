# DSD M5-359 — Sequential Circulation Renewal: Near-Partner / Log-Transport / Viscous-H Barrier

Date: 2026-08-31

Status: **SEQUENTIAL RENEWAL DOES NOT BYPASS THE CIRCULATION LEDGER FOR FREE / A DESCENDANT WITH GROWING CIRCULATION CAN BE REMOVED WITHIN ONE NATURAL STAGE ONLY BY A SAME-SCALE OPPOSITE-SIGNED PARTNER, A LOGARITHMIC MATERIAL-CONTRACTION ACTION, OR A VISCOSITY/DERIVATIVE H EVENT / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

M5-357 showed that each quiet affine-shield circulation descendant carries an order-one kinetic-energy occupancy, so only finitely many can coexist.

M5-358 correctly blocked the false inference that positive-density descendant loss alone gives a contradiction: one may imagine sequential renewal, where one old descendant disappears whenever one new descendant is created.

The missing question is therefore not the number of simultaneous descendants but the cost of deleting a descendant whose circulation is large.

For the saturated affine-shield scaling, write

\[
 r_j\downarrow0
\]

for the natural first-hitting length and

\[
 d_j\asymp r_j^{4/5}
\]

for the energy-shield radius.

The characteristic circulation is

\[
 \Gamma_j\asymp r_j^{-2/5}.
\]

Hence \(\Gamma_j\to\infty\).

## 2. Existing same-scale partner dichotomy

The older circulation-buffer audit already proves that failure of a clean signed circulation buffer at the natural radius creates a same-scale opposite-signed vorticity partner carrying natural enstrophy.

Thus if cancellation-ready opposite flux is already present within distance

\[
 O(r_j),
\]

we are in the previously typed signed/projective-partner or reach-collapse branch.

This note studies the complementary case.

## 3. Nearest cancellation distance

Let \(\delta_j\) denote the material distance from the coherent descendant bundle to the nearest opposite-signed circulation reservoir capable of cancelling a fixed fraction of \(\Gamma_j\).

There are two possibilities:

\[
 \boxed{\delta_j/r_j=O(1)}
\]

or

\[
 \boxed{\delta_j/r_j\to\infty.}
\]

The first is exactly the natural-scale partner branch.

Assume the second.

## 4. Material contraction barrier

For two material trajectories before collision, the relative distance obeys

\[
 \frac{d}{dt}|X_1-X_2|
 \ge
 -\|\nabla u(t)\|_\infty |X_1-X_2|.
\]

Hence to reduce a separation from \(\delta_j\) to \(Cr_j\), one needs

\[
 Cr_j
 \ge
 \delta_j
 \exp\!\left(-\int_{I_j}\|\nabla u(t)\|_\infty dt\right),
\]

and therefore

\[
 \boxed{
 \int_{I_j}\|\nabla u(t)\|_\infty dt
 \ge
 \log\frac{\delta_j}{Cr_j}.
 }
\]

If the descendant is shield-clean up to its full affine radius, so that

\[
 \delta_j\gtrsim d_j,
\]

then

\[
 \boxed{
 \int_{I_j}\|\nabla u\|_\infty dt
 \gtrsim
 \log\frac{d_j}{r_j}
 =
 \frac15|\log r_j|-O(1).
 }
\]

Thus sequential renewal by material recruitment requires a logarithmically diverging Lipschitz/strain action on late stages.

This is much stronger than merely requiring a fixed positive turnover action per stage.

## 5. Intermediate-distance formation split

The full shield-clean assumption is not necessary for the qualitative routing.

For any exponent \(0<\alpha<1\), define

\[
 \delta_{\alpha,j}
 :=
 r_j\left(\frac{d_j}{r_j}\right)^\alpha.
\]

Then either

\[
 \delta_j\le C\delta_{\alpha,j},
\]

in which case an opposite-signed reservoir already lies in an intermediate-scale neighborhood and the problem is routed to an intermediate partner/reach packet,

or

\[
 \delta_j\ge c\delta_{\alpha,j},
\]

in which case

\[
 \int_{I_j}\|\nabla u\|_\infty dt
 \gtrsim
 \alpha\log\frac{d_j}{r_j}
 \sim
 \frac{\alpha}{5}|\log r_j|.
\]

Thus no choice of intermediate cancellation radius creates a free branch.

## 6. Viscous communication clock

Suppose instead that opposite signed flux is not brought into natural-scale contact by transport and cancellation is delegated to viscosity.

Diffusive communication across distance \(\delta_j\) requires the clock

\[
 t_{\rm diff}\sim \frac{\delta_j^2}{\nu}.
\]

The natural first-hitting stage time is

\[
 |I_j|\asymp r_j^2
\]

in the critical-clock corridor.

Therefore

\[
 \frac{t_{\rm diff}}{|I_j|}
 \asymp
 \frac{1}{\nu}
 \left(\frac{\delta_j}{r_j}\right)^2.
\]

If \(\delta_j/r_j\to\infty\), ordinary diffusion is too slow by an unbounded factor.

For the full affine-shield separation,

\[
 \frac{d_j^2}{r_j^2}
 \asymp
 r_j^{-2/5}\to\infty.
\]

Hence cancelling a fixed fraction of \(\Gamma_j\) in one natural stage without material approach requires a non-quiet derivative/palinstrophy event, precisely the viscous-H route already identified in M5-356.

## 7. Sequential-renewal master routing

A quiet circulation descendant cannot simply disappear between consecutive late first-hitting stages.

Its fixed-fraction removal obeys

\[
 \boxed{
 \text{descendant loss}
 \Longrightarrow
 P_{\rm opp}^{\rm near}
 \lor
 H_{\rm Lip/log}
 \lor
 H_{\rm visc/der}
 \lor
 T_{\rm spatial/export}.
 }
\]

Here:

- \(P_{\rm opp}^{\rm near}\): same/intermediate-scale opposite-signed partner or reach collapse;
- \(H_{\rm Lip/log}\): material contraction pays a logarithmically growing Lipschitz action;
- \(H_{\rm visc/der}\): diffusion must act faster than its natural parabolic clock;
- \(T_{\rm spatial/export}\): the descendant is not destroyed but transported out of the controlled parent region.

## 8. Relation to absolute circulation inventory

Define the absolute coherent circulation inventory at time \(t\) by

\[
 \mathcal C_{\rm abs}(t)
 =
 \sum_{\alpha\in\mathcal Q(t)}|\Gamma_\alpha(t)|
\]

over a disjoint family of quiet coherent descendants.

M5-357 gives a finite simultaneous occupancy bound for \(\mathcal Q(t)\).

The present result says that keeping \(\mathcal C_{\rm abs}\) uniformly bounded by sequentially deleting old large-\(\Gamma\) descendants requires one of the H/T events above with increasing severity.

Thus sequential renewal removes the false branching contradiction, but does not remove the need for a scale-sensitive charge.

## 9. Firewall

Do not claim that the logarithmic Lipschitz lower bound by itself contradicts Navier--Stokes blow-up.

BKM-type divergence of

\[
 \int^{T_*}\|\nabla u\|_\infty dt
\]

is compatible with a singular solution.

The gain is structural: the previous positive-density turnover branch is strengthened to a late-stage action whose lower bound grows like \(|\log r_j|\) whenever cancellation partners are not already at the natural scale.

## 10. Audit verdict

### PROVED / STANDARD

- natural-scale buffer failure produces an opposite-signed partner packet (existing ledger);
- material contraction from \(\delta_j\) to \(r_j\) requires \(\int\|\nabla u\|_\infty\ge\log(\delta_j/r_j)\);
- full shield-clean renewal costs \(\gtrsim\frac15|\log r_j|\) Lipschitz action;
- ordinary diffusion cannot cancel across \(\delta_j\gg r_j\) within one natural stage.

### OPEN

- converting the growing logarithmic action into a non-summable contradiction;
- controlling intermediate partner cascades without returning to H/T;
- global regularity.

\[
 \boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
