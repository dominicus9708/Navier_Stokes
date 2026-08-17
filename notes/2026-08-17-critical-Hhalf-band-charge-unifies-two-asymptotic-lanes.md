# Critical H^(1/2) band charge unifies the compact and coherent lanes

Date: 2026-08-17

Status: **DERIVED AS A COMMON SCALE-CRITICAL BAND LEDGER. BOTH EXHAUSTIVE ASYMPTOTIC LANES FORCE NONVANISHING HIGH-FREQUENCY `dot H^(1/2)` VELOCITY CHARGE UNLESS THEY ALREADY ENTER A DERIVATIVE BRANCH. THIS IDENTIFIES THE MOVING-BAND WALL WITH A STANDARD CRITICAL-SCALE CASCADE. GLOBAL REGULARITY NOT PROVED.**

## 1. Physical critical band variable

For a physical Littlewood--Paley shell at frequency

\[
K_k=2^k,
\]

let

\[
E_k^\omega=\|P_k\omega\|_2^2.
\]

Because `omega=curl u`, on a dyadic shell

\[
E_k^\omega\asymp K_k^2\|P_ku\|_2^2.
\]

Define

\[
\boxed{
\mathfrak h_k
:=\frac{E_k^\omega}{K_k}
\asymp
K_k\|P_ku\|_2^2.
}
\]

Then

\[
\boxed{
\sum_k\mathfrak h_k
\asymp
\|u\|_{\dot H^{1/2}}^2.
}
\]

This is exactly scale invariant under the three-dimensional Navier--Stokes scaling.

## 2. Compact/natural-scale lane

On the compact lane, after terminal first-hitting normalization, the active Gaussian radius is `r~1` and the residual variance has an order-one lower bound

\[
B_r(x_*)\ge m_0>0.
\]

The pointwise-to-band bridge gives

\[
r^3B_r(x_*)
\lesssim
\Delta\mathcal B(4r)+r^2P.
\]

Hence either the normalized palinstrophy is already order one/high, or a scale-local strain/vorticity band has order-one `L2` charge. By Riesz-transform equivalence on that dyadic shell, the vorticity part may be used as the band representative:

\[
E_{k_j,\mathrm{norm}}^\omega\gtrsim c.
\]

Terminal scaling with `W_j` gives

\[
E_{k_j,\mathrm{phys}}^\omega
=\sqrt{W_j}\,E_{k_j,\mathrm{norm}}^\omega
\gtrsim c\sqrt{W_j},
\]

while the physical active frequency is

\[
K_{k_j}\asymp\sqrt{W_j}.
\]

Therefore

\[
\boxed{
\mathfrak h_{k_j}\gtrsim c>0
}
\]

unless the episode is already in the derivative/palinstrophy branch.

Thus the compact lane cannot remain dangerous while carrying vanishing critical band charge.

## 3. Coherent large-R lane

Let

\[
L_R\asymp R\sqrt{\log R}
\]

be the terminal-normalized logarithmically enlarged coherent radius.

The Gaussian mean-termination identity gives a positive outward scale-band charge

\[
\sum_{r_k\ge L_R}\mathfrak b_{r_k}(\omega)
\gtrsim
L_R^3|m_{L_R}|^2
\gtrsim cL_R^3.
\]

Returning to physical variables multiplies vorticity `L2` band energy by `sqrt(W)`. Every outward termination shell has normalized frequency at most `~L_R^-1`, hence physical frequency at most

\[
K\lesssim\frac{\sqrt W}{L_R}.
\]

Consequently `1/K >= c L_R/sqrt(W)` on this band family. Therefore the total critical charge in the termination bands obeys

\[
\begin{aligned}
\sum_{\rm term}\mathfrak h_k
&=\sum_{\rm term}\frac{E_{k,\rm phys}^\omega}{K_k}\\
&\gtrsim
\frac{L_R}{\sqrt W}
\left(
\sqrt W\,L_R^3
\right).
\end{aligned}
\]

Hence

\[
\boxed{
\sum_{\rm term}\mathfrak h_k
\gtrsim
L_R^4
=R^4(\log R)^2.
}
\]

Thus the coherent lane carries an even stronger high-frequency critical charge before the affine mean can terminate.

## 4. Unified interpretation

The exhaustive asymptotic split is now represented by one common object.

### Compact lane

\[
\boxed{
\text{dangerous episode}
\to
\mathfrak h_{k_j}\gtrsim c
\quad\lor\quad
\text{derivative concentration}.
}
\]

### Coherent lane

\[
\boxed{
\text{dangerous episode}
\to
\sum_{\rm termination}\mathfrak h_k
\gtrsim R^4(\log R)^2
\quad\lor\quad
\text{local Betchov/derivative compensation}.
}
\]

In both cases the active physical frequencies tend to infinity.

Therefore the moving-band endgame may be restated as:

\[
\boxed{
\text{Can a finite-energy smooth solution repeatedly create nonvanishing}
\;\dot H^{1/2}\text{ charge at frequencies }K_j\to\infty
}
\]

by alternating direct critical stretching and derivative-supported commutator transfer?

This is a standard critical-scale type of obstruction rather than a purely DSD-specific norm.

## 5. Limitation

A nonvanishing or even diverging `dot H^(1/2)` critical charge near a hypothetical singularity is not itself a contradiction. The result identifies the correct common critical quantity but does not yet provide a finite global budget for it.

The next target is to derive a scale-time variation/flux estimate for `mathfrak h_k` and determine whether repeated high-frequency repopulation has a non-summable kinetic-energy, direct-strain, or derivative cost.

Status: **TWO ASYMPTOTIC LANES UNIFIED BY HIGH-FREQUENCY CRITICAL H-HALF BAND CHARGE / DERIVATIVE COMPLEMENT RETAINED / CRITICAL CASCADE STILL OPEN.**