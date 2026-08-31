# DSD M5-361 — Directional-Dissipation Capacity Scaling Firewall

Date: 2026-08-31

Status: **THE HALF-HOLDER DIRECTION-DEFECT NECESSITY DOES NOT BY ITSELF CONTRADICT THE CONSTANTIN--FEFFERMAN WEIGHTED DIRECTIONAL-DISSIPATION BUDGET / EVEN A VOLUME-FILLING AFFINE-TRANSITION CLOUD CAN PAY A GEOMETRICALLY SUMMABLE COST / THE DIRECTION CRITERION IS A ROUTING TOOL, NOT YET THE FINAL CHARGE / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

M5-360 inserted the geometric regularity criterion: a singular survivor must develop a high-vorticity half-Holder direction defect.

For rapidly decaying smooth data with integrable initial vorticity, the Constantin--Fefferman estimate gives

\[
 \nu\int_0^{T_*}\!\int |\omega|\,|\nabla\xi|^2\,dxdt
 <\infty.
\]

It is tempting to claim that repeated failure of half-Holder coherence contradicts this finite budget.

This note audits the scaling and rejects that shortcut.

## 2. One natural defect packet

At first-hitting length \(r\), assume

\[
 |\omega|\asymp r^{-2}
\]

on one natural spatial packet of diameter \(r\).

Let the vorticity direction change by an angle \(\theta\) across the packet.

Then a typical directional gradient scale is

\[
 |\nabla\xi|\sim \frac{\theta}{r}.
\]

The instantaneous weighted directional-dissipation cost is therefore

\[
 \int_{B_r}|\omega||\nabla\xi|^2dx
 \sim
 r^{-2}\frac{\theta^2}{r^2}r^3
 =
 \frac{\theta^2}{r}.
\]

On a natural parabolic stage of duration

\[
 \Delta t\asymp r^2,
\]

the space-time cost is

\[
 \boxed{
 \mathcal D_{\xi,\rm packet}
 \sim
 \theta^2 r.
 }
\]

For order-one angular mismatch this is only \(O(r)\).

Along geometric first-hitting scales \(r_j\sim q^{-j/2}\),

\[
 \sum_j r_j<\infty.
\]

Thus one order-one direction defect per stage is fully compatible with the finite global budget.

## 3. Fractional half-Holder defect

Suppose the defect is measured at a subscale

\[
 \ell=\rho r,
 \qquad 0<\rho\le1,
\]

and define the normalized half-Holder defect amplitude \(d\) by

\[
 \theta=d\rho^{1/2}.
\]

Then

\[
 |\nabla\xi|\sim \frac{d}{r\rho^{1/2}}.
\]

A defect packet of volume \(\ell^3\) has instantaneous weighted cost

\[
 \sim
 r^{-2}
 \frac{d^2}{r^2\rho}
 (\rho r)^3
 =
 \frac{d^2\rho^2}{r}.
\]

If it persists for one full natural stage \(r^2\),

\[
 \boxed{
 \mathcal D_{\xi,\rm frac}
 \sim
 d^2\rho^2 r.
 }
\]

This becomes even cheaper as \(\rho\downarrow0\) unless the defect amplitude grows correspondingly.

Therefore divergence of the half-Holder seminorm is not automatically expensive in the H1 directional budget.

## 4. Affine-transition cloud test

The saturated affine shield has normalized radius

\[
 R_{\rm scr}\sim r^{-1/5}
\]

and physical radius

\[
 d_{\rm scr}\sim r^{4/5}.
\]

A volume-filling natural-cell transition cloud contains at most/order

\[
 N(r)\sim R_{\rm scr}^3\sim r^{-3/5}
\]

natural packets.

Even if every one carries an order-one direction mismatch during one natural stage, the total weighted directional-dissipation cost is only

\[
 \boxed{
 N(r)\,r
 \sim
 r^{2/5}.
 }
\]

Again

\[
 \sum_j r_j^{2/5}<\infty.
\]

Thus even the strongest previously derived volume-filling transition cloud is compatible with the global finite directional-dissipation estimate.

## 5. Consequence

The geometric direction criterion remains extremely useful because it excludes a uniformly coherent high-vorticity singularity.

But the finite integral

\[
 \int |\omega||\nabla\xi|^2
\]

cannot by itself price a geometric first-hitting cascade strongly enough.

The remaining value of the direction variable is therefore structural:

\[
 \boxed{
 \text{coherent axis}
 \Rightarrow
 \text{regularity},
 }
\]

whereas

\[
 \boxed{
 \text{singular survivor}
 \Rightarrow
 \text{fractional axis defect / misaligned source network}.
 }
\]

The latter must be coupled to circulation, Biot--Savart stretching, projective action, or turnover to obtain a stronger charge.

## 6. Formation/axis lesson

This is a useful example of why the formation and axis-property analysis must remain distinct from the DSD closure audit.

The direction theorem identifies which geometric state cannot survive.

The scale audit then determines whether the complementary defect has enough cost to be a contradiction.

Here it does not: the natural directional-dissipation capacity is too large.

## 7. Firewall

Do not claim

\[
 D_{\xi,1/2}^{\rm frac}
 \Longrightarrow
 \text{infinite directional H1 budget}.
\]

The explicit first-hitting scaling above is a counterledger.

## 8. Next target

The next useful quantity is not \(|\nabla\xi|^2\) alone but the **Biot--Savart angular source of stretching**:

\[
 \gamma(x)
 =\xi(x)^TS[\omega](x)\xi(x),
\]

whose singular-integral representation vanishes under exact local alignment.

A first-hitting core that must pay positive longitudinal stretching therefore requires a quantitatively nontrivial misaligned vorticity source.

That angular source can potentially connect the geometric defect directly to the existing packet/projective/remote-strain ledgers.

## 9. Audit verdict

### DERIVED

- one natural order-one direction defect costs only \(O(r)\) in the weighted directional-dissipation budget;
- a volume-filling affine transition cloud costs only \(O(r^{2/5})\) per stage;
- both are geometrically summable.

### OPEN

- a stronger non-summable charge coupling angular defect to stretching/circulation;
- global regularity.

\[
 \boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
