# Parallel Pruning + Direct Closure Frontier — 2026-08-20

Overall status: **ACTIVE 3D NAVIER--STOKES PROOF ATTEMPT — GLOBAL REGULARITY NOT PROVED.**

The proof strategy is now explicitly parallel rather than sequential. Branch pruning continues, but the best-pruned survivor is attacked directly at the same time. New direct inequalities are then fed back into the pruning tree.

## 1. Updated System I

First-hitting analyticity gives uniform normalized `L-infinity` bounds on every fixed derivative order at the checkpoint sequence. Hence `H` can no longer mean

- pointwise normalized derivative blow-up;
- or derivative-mass blow-up on one fixed normalized ball.

The remaining derivative branch is

\[
\boxed{H_{remote}=\text{spatial non-tightness of derivative mass}.}
\]

Ordinary Eulerian spatial transport was already reduced, on the coherent material track, to translation, viscous derivative erosion, or large material deformation.

Thus System I is now

\[
\boxed{H_{remote}\lor T.}
\]

The global energy-packing barrier remains: an `O(1)` natural-scale cost per geometric vorticity stage is summable. A successful System-I closure must gain the missing half-power or identify a different critical global budget.

## 2. Updated System II

The recurrent non-H/T survivor is a precompact Leray `P_V` class.

The exact H1 production is

\[
N=\frac12\int S:(G^TG-GG^T),
\qquad G=\nabla\omega.
\]

This yields the universal ceiling

\[
\boxed{N\le\sqrt2\|S\|_\infty P,}
\]

which is already stronger than the older static `4/sqrt(6)` ceiling.

At a compact recurrent `P`-maximum state,

\[
\boxed{N=\frac34P+\nu H.}
\]

At a compact recurrent `E`-maximum state,

\[
\boxed{-4\int\det S=\frac12E+2\nu P.}
\]

Thus one compact invariant class must satisfy two exact extremal ledgers.

## 3. Direct coherent positive-middle closure

A two-parameter high-strain ball selection gives the explicit self-consistency inequality

\[
\boxed{\beta[1+\Gamma(\beta,e)]\le1.}
\]

For the coherent compatibility branch, the fixed choice

\[
a=0.235,
\qquad h=0.995
\]

gives, at zero annular leakage,

\[
\boxed{\beta\le0.9998431096.}
\]

This is a literal strict production ceiling, not merely an abstract compactness gap.

## 4. Direct nonnormality spectral closure

For positive-middle spectrum

\[
s=(-2m,m-d,m+d),
\qquad x=d/m,
\]

the exact nonnormality efficiency is

\[
\Theta_{NN}(x)
=\frac{3+x}{2\sqrt{3+x^2}}.
\]

Use

\[
x_*=rac{3(\sqrt3-1)}4
\approx0.5490381.
\]

On the high-strain subbranch `x <= x_*`, optimized selection yields

\[
\boxed{
\frac{q}{\sqrt2B_*}
\le0.9969095157.
}
\]

Therefore the remaining H1-efficient spectrum is driven toward the middle-zero side `x > x_*`.

## 5. L2 ledger pushes in the opposite direction

The determinant efficiency is

\[
\Theta_{det}(x)
=\frac{3\sqrt3(1-x^2)}{(3+x^2)^{3/2}}.
\]

At `x=x_*`,

\[
\Theta_{det}(x_*)\approx0.605101397.
\]

Hence an `E`-maximizing recurrent state living entirely on `x >= x_*` must satisfy

\[
\boxed{\|S\|_\infty\ge1.51802435}
\]

even after the positive viscous term is discarded.

Thus H1 efficiency pushes toward middle-zero geometry, while L2 recurrence pushes toward determinant-efficient max-mid geometry unless strain amplitude is at least `1.518`.

## 6. Second-order Biot--Savart closure criterion

Parity of the strain kernel cancels both constant and linear vorticity Taylor terms in the near field. With

\[
K_2
=\sup_{x,|v|=1}|(v\cdot\nabla)^2\omega(x)|,
\]

and vorticity tightness radius `R_Z`, one obtains

\[
\boxed{
q
\le
\frac74
K_2^{3/7}
R_Z^{6/7}
(1-\varepsilon_Z)^{-2/7}.
}

Therefore the recurrent `P_V` system closes whenever its Leray lower requirement exceeds this explicit ceiling.

## 7. Direct P_V-to-H bridge

Using Hardy instead of the vorticity `L2` far-field bound gives

\[
\boxed{
q
\le
\frac{15}{4}\pi^{-2/5}
K_2^{1/5}Q^{2/5},
\qquad
Q=\|\nabla\omega\|_2^2.
}
\]

Hence every recurrent survivor must carry

\[
\boxed{
Q
\ge
\pi\left(\frac4{15}\right)^{5/2}
q_-^{5/2}K_2^{-1/2}.
}
\]

So System II cannot avoid System I for free: failed direct closure forces a quantitative derivative-mass floor.

## 8. Current coupled proof tree

A hypothetical singularity is now forced into

\[
\boxed{
\begin{aligned}
& H_{remote}\lor T,\\
&\text{or a recurrent }P_V\text{ class satisfying all direct ceilings.}
\end{aligned}
}
\]

But the second line itself implies a positive palinstrophy floor and therefore approaches the first line as the derivative mass spreads.

The remaining difficult regimes are therefore not independent branches; they form a coupled loop:

\[
\boxed{
P_V\text{ recurrence}
\to
\text{required derivative mass}
\to
\begin{cases}
\text{tight} &\to P_V/T\text{ rigidity},\\
\text{remote} &\to H_{remote}.
\end{cases}
}
\]

## 9. Principal next calculations

1. **Middle-zero branch:** quantify differential compatibility of near-rank-one `grad omega` with finite-energy strain; seek a direct loss from the `sqrt(2)` nonnormality ceiling.
2. **Spectral excursion:** quantify the action needed for one compact recurrent orbit to move between the determinant-efficient and nonnormality-efficient spectral sectors.
3. **Remote-H packing:** use the analytic derivative-amplitude bounds plus the aggregate halo inequality to determine whether `P_tail >= cR` on infinitely many first-hitting stages forces either secondary core turnover or the missing `W^(1/2)` global packing gain.
4. **Parameter closure:** sharpen `K_2`, `R_Z`, and the Leray lower floor `q_-` enough to test the explicit `7/4` Biot--Savart criterion numerically/analytically.

Status: **THE WORKFLOW IS NOW PARALLEL: BRANCH PRUNING CONTINUES WHILE SYSTEM II IS ATTACKED DIRECTLY. THE DIRECT P_V INEQUALITIES FEED BACK INTO SYSTEM I BY FORCING QUANTITATIVE DERIVATIVE MASS. GLOBAL REGULARITY REMAINS UNPROVED.**