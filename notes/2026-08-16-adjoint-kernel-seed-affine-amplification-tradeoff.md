# Adjoint-kernel seed versus affine amplification tradeoff

Date: 2026-08-16

Status: **DERIVED EXACT GRONWALL TRADEOFF FOR FRESH COHERENT-VORTICITY GENERATION. A PARABOLIC-CRITICAL RECENT EPISODE MUST PAY EITHER RESIDUAL SEED ACTION OR LOGARITHMIC AFFINE-STRAIN ACTION. GLOBAL REGULARITY NOT PROVED.**

## 1. Terminal-conditioned weighted mean

Fix a good point in the future coherent core and use the exact scalar adjoint kernel `K(s,x)` ending at that point.

Define

\[
\bar\Omega_K(s)=\int K(s,x)\Omega(s,x)\,dx,
\qquad
\bar S_K(s)=\int K(s,x)S(s,x)\,dx.
\]

Define the exact covariance remainder

\[
J_K(s)
=\int K S\Omega
-\bar S_K\bar\Omega_K.
\]

The exact kernel-weighted DSD state gives

\[
\boxed{|J_K(s)|\le C B_K(s),}
\]

where

\[
B_K=V_{S,K}+\frac12V_{\omega,K}.
\]

Because `K` solves the adjoint transport-diffusion equation,

\[
\boxed{
\frac{d}{ds}\bar\Omega_K
=\bar S_K\bar\Omega_K+J_K.
}
\]

This is an exact vector ODE along the terminal-conditioned kernel state.

## 2. Fresh-generation initial condition

Use the adaptive recent horizon from the dissipation-tail cutoff.

On the parabolic critical-saturation branch, choose a recent interval

\[
I_R=[s_0,s_c],
\qquad
|I_R|\le C_R R^2
\]

with `C_R` bounded up to an arbitrarily slow cutoff factor.

The clean precursor plus old-source erasure implies that the homogeneous/older contribution at the left edge can be made

\[
\boxed{|\bar\Omega_K(s_0)|=o(1)}
\]

on the good-core subsequence.

At the coherent crossing,

\[
\boxed{|\bar\Omega_K(s_c)|\ge c_0>0.}
\]

## 3. Gronwall tradeoff

Set

\[
A_R
:=\int_{s_0}^{s_c}\|\bar S_K(s)\|_{op}\,ds,
\]

and

\[
\mathcal B_R
:=\int_{s_0}^{s_c}B_K(s)\,ds.
\]

Variation of constants and `|J_K| <= C B_K` give

\[
|\bar\Omega_K(s_c)|
\le
\exp(A_R)
\left[
|\bar\Omega_K(s_0)|
+C\mathcal B_R
\right].
\]

Hence

\[
\boxed{
1
\lesssim
\exp(A_R)
\bigl(o(1)+\mathcal B_R\bigr).
}
\]

Equivalently, whenever `mathcal B_R -> 0`,

\[
\boxed{
A_R
\ge
\log\frac1{\mathcal B_R}-O(1).
}
\]

This is the exact seed-amplification law: residual covariance can create seed vorticity, while affine mean strain can only amplify what seed is present.

## 4. Power-threshold family

For every fixed `gamma>0`, the preceding inequality yields the dichotomy

\[
\boxed{
\mathcal B_R\ge R^{-\gamma}
\quad\text{or}\quad
A_R\ge\gamma\log R-O(1).
}
\]

In particular, choosing `gamma=1`,

\[
\boxed{
\mathcal B_R\ge R^{-1}
\quad\text{or}\quad
A_R\ge\log R-O(1).
}
\]

If the critical recent horizon has length `O(R^2)`, the first branch implies that at some time

\[
\boxed{
B_K(s)\gtrsim R^{-3}.
}
\]

Thus a minimal recent episode cannot remain uniformly at the tiny residual level throughout its parabolic source window unless it pays logarithmically divergent affine strain.

## 5. Interpretation of the two branches

### S1. Residual-seed branch

A non-negligible integral of `B_K` appears. If it is spread across a positive fraction of the parabolic window, the local residual Reynolds number becomes supercritical. If it is squeezed into a thinner terminal layer, Gaussian Poincare and the existing V2/pressure-Hessian ledgers become active.

### S2. Affine-amplification branch

The residual seed is too small, and then

\[
\boxed{A_R\gtrsim\log R.}
\]

This is precisely the material-area/strain-action branch already identified in the flux-retaining analysis. Fast coherent rotation does not remove this symmetric-strain cost because the skew part is energy preserving.

## 6. Relation to fast rotation

At the coherent crossing, standard `R`-scale Navier--Stokes rescaling turns the order-one coherent mean rotation into an `O(R^2)` skew/Coriolis background while leaving the critical residual at order one.

The seed-amplification law therefore says that a surviving rapidly rotating episode must obtain its order-one slow/coherent vorticity from either

\[
\boxed{\text{residual covariance seed}}
\]

or

\[
\boxed{\text{logarithmic symmetric-strain amplification}.}
\]

Nonresonant fast interactions and the exact slow-fast-fast resonance have already been reduced elsewhere; thus the remaining residual-seed branch is naturally tied to near-resonant/near-slow localization or to derivative/time modulation.

## 7. Claim boundary

Neither `mathcal B_R >= R^-gamma` nor `A_R >= gamma log R` is by itself incompatible with a hypothetical singular cascade. The physical costs can still shrink on a super-separated sequence, while logarithmic BKM/strain action is allowed to diverge at a singular time.

The result is a branch reduction, not a regularity theorem.

Status: **FRESH SOURCE FACTORED INTO RESIDUAL SEED + AFFINE AMPLIFICATION / POWER-LAW RESIDUAL SMALLNESS FORCES LOGARITHMIC STRAIN / GLOBAL REGULARITY NOT PROVED.**