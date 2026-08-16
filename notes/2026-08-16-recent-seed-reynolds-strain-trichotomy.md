# Recent seed -- Reynolds -- strain trichotomy

Date: 2026-08-16

Status: **DERIVED ON THE PARABOLIC-CRITICAL RECENT-SOURCE BRANCH. RESIDUAL SEEDING, TEMPORAL CONCENTRATION, AND LOGARITHMIC AFFINE STRAIN ARE NOW CONNECTED DIRECTLY TO THE EARLIER DYNAMIC REYNOLDS-CROSSING TREE. GLOBAL REGULARITY NOT PROVED.**

## 1. Starting tradeoff

On a critical-saturation recent source interval of normalized length

\[
T_R\asymp R^2
\]

(up to bounded or arbitrarily slow factors), define

\[
A_R=\int\|\bar S_K\|ds,
\qquad
\mathcal B_R=\int B_K ds.
\]

The exact kernel mean equation gives

\[
1\lesssim e^{A_R}(o(1)+\mathcal B_R).
\]

Hence for every fixed `0<epsilon<2`,

\[
\boxed{
\mathcal B_R\ge R^{-2+\epsilon}
\quad\text{or}\quad
A_R\ge(2-\epsilon)\log R-O(1).
}
\]

## 2. Split the residual seed in parabolic age

Fix `0<c_0<C_0<infinity` and split the recent interval into

\[
I_{\rm bulk}
=\{c_0R^2\le\tau\le C_0R^2\}
\]

and the complementary thinner/earlier layers.

Suppose a fixed fraction of the residual seed action lies in the parabolic bulk:

\[
\int_{I_{\rm bulk}}B_Kd\tau
\ge c\mathcal B_R.
\]

If

\[
\mathcal B_R\ge R^{-2+\epsilon},
\]

then the bulk interval has length `O(R^2)`, so for some bulk age

\[
\boxed{
B_K\gtrsim R^{-4+\epsilon}.
}
\]

The kernel covariance radius there is comparable to `R`, and therefore the corresponding Gaussian local Reynolds number obeys

\[
\boxed{
\mathcal R_G
=R^2\sqrt{B_K}
\gtrsim R^{\epsilon/2}\to\infty.
}
\]

Thus parabolically distributed residual seeding automatically recreates a supercritical residual pulse.

## 3. Return to the dynamic crossing tree

The endpoint of a point-conditioned Gaussian kernel has vanishing residual variance as the covariance collapses. Hence a bulk state with

\[
\mathcal R_G\gg1
\]

and a terminal state with

\[
\mathcal R_G\ll1
\]

must pass continuously through a Reynolds-one state

\[
\boxed{BR^4\asymp1.}
\]

Therefore the recent residual-seed branch is not new. It feeds back into the established dynamic critical-Reynolds crossing:

\[
\boxed{
\text{parabolic residual seed}
\Rightarrow
\text{supercritical pulse}
\Rightarrow
\text{Reynolds-one crossing}.
}
\]

At that crossing the previous low-curvature/high-curvature/spatial-nontightness/fast-rotation analysis applies again.

## 4. Terminally concentrated residual seed

The only way for `mathcal B_R >= R^(-2+epsilon)` to avoid the parabolic-bulk conclusion is to push most of the residual seed action into a thinner age layer.

For Gaussian covariance age `tau`, Poincare gives schematically

\[
B_K(\tau)
\lesssim
\tau K_K(\tau),
\]

where `K_K` is the corresponding derivative/curvature energy.

Thus squeezing a fixed seed action toward smaller ages raises the required derivative density. The exact residual-variance dynamics further show that maintaining such a terminal pulse requires one of

\[
\boxed{
\text{V2/high-curvature concentration},
\quad
\text{pressure-Hessian concentration},
\quad
\text{affine-deformation concentration}.
}
\]

This is the already typed thin-source branch.

## 5. Logarithmic affine-strain branch

If residual seed action is instead below the threshold,

\[
\mathcal B_R<R^{-2+\epsilon},
\]

then

\[
\boxed{
A_R\ge(2-\epsilon)\log R-O(1).
}
\]

Hence an almost seed-free fresh-generation episode must accumulate logarithmically divergent symmetric affine strain.

The skew coherent rotation cannot pay this cost because it is energy preserving. The symmetric action routes to the existing material-area contraction, strain-deformation, Betchov mismatch, and positive-middle-strain ledgers.

## 6. Unified recent-source trichotomy

For every fixed `epsilon in (0,2)`, a parabolic-critical fresh-generation episode must enter at least one of:

\[
\boxed{
\text{R1. parabolic-bulk supercritical residual pulse}
}
\]

\[
\boxed{
\text{R2. thin residual seed}
\Rightarrow
\text{V2/pressure/curvature concentration}
}
\]

\[
\boxed{
\text{R3. }(2-\epsilon)\log R
\text{ symmetric-strain action}.
}
\]

R1 recursively returns to the previously derived Reynolds-one crossing tree. R2 is the higher-derivative branch. R3 is the critical strain/material-deformation branch.

Thus the recent-source endgame has not created a genuinely new fourth mechanism. It closes back onto the same three structural channels already isolated by the earlier DSD branch reductions.

## 7. Claim boundary

The trichotomy is not yet contradictory. A super-separated hypothetical cascade may repeatedly revisit R1, R2, or R3 while its physical scalar costs shrink. The missing theorem is a cross-episode nonrepeatability or packing theorem for these recursively regenerated channels.

Status: **RECENT SOURCE RECURSIVELY CLOSED BACK TO SUPERCRITICAL RESIDUAL / THIN DERIVATIVE-PRESSURE / LOG-STRAIN CHANNELS / GLOBAL REGULARITY NOT PROVED.**