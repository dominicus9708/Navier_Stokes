# Factorial-normalized viscous budget and derivative-radius bridge

Date: 2026-08-13

Status: **DERIVED FACTORIAL V-BUDGET / OPEN S--V CYCLE CLOSURE**.

This note corrects an important scaling issue in the raw derivative ratio

\[
r_k=E_{k+1}/E_k.
\]

Raw `r_k` can grow like `(k+1)^2` even for a perfectly analytic field. The derivative-channel generating-function track therefore suggests using the factorial-normalized ratio instead.

## 1. Factorial derivative energies

Define

\[
\boxed{
\widehat E_k
=\frac{E_k}{(k!)^2}.
}
\]

Then

\[
\frac{\widehat E_{k+1}}{\widehat E_k}
=
\frac{E_{k+1}}{E_k}\frac{1}{(k+1)^2}.
\]

Define

\[
\boxed{
\rho_k
=\frac{r_k}{(k+1)^2}
=\frac{\widehat E_{k+1}}{\widehat E_k}.
}
\]

`rho_k` is the derivative-ratio channel naturally compatible with the factorial Cauchy-product normalization.

## 2. Factorial-radius certificate

Assume

\[
\rho_k\le R^{-2}
\]

for every `k>=0` at a fixed time.

Then iterating

\[
\widehat E_{k+1}\le R^{-2}\widehat E_k
\]

gives

\[
\widehat E_k\le E_0R^{-2k},
\]

or equivalently

\[
\boxed{
E_k
\le
E_0(k!)^2R^{-2k}.
}
\]

Consequently the factorial derivative generating series

\[
\sum_{k\ge0}
\frac{\tau^{2k}E_k}{(k!)^2}
\]

is bounded by a geometric series for every

\[
0\le\tau<R.
\]

This is an `L^2` factorial-derivative / analytic-Gevrey-compatible radius certificate. It is used here as an internal derivative-radius channel, not as a new analyticity theorem.

## 3. Positive viscous branch with factorial normalization

Recall

\[
V_k
=\nu r_k\mathcal A_k,
\]

where

\[
\mathcal A_k
=\frac12
\left[
J_k-J_{k+1}-\Delta_k^2
\right].
\]

The factorially normalized viscous rate is

\[
\boxed{
\widehat V_k
=\frac{V_k}{(k+1)^2}
=\nu\rho_k\mathcal A_k.
}
\]

Suppose `A_k>0` on a consecutive derivative-order block `k=m,...,n` and

\[
\rho_k\le R^{-2}
\]

on that block. Then

\[
\begin{aligned}
\sum_{k=m}^{n}\widehat V_k
&=\nu\sum_{k=m}^{n}\rho_k\mathcal A_k\\
&\le\frac{\nu}{R^2}
\sum_{k=m}^{n}\mathcal A_k\\
&\le\frac{\nu}{3R^2}.
\end{aligned}
\]

Therefore

\[
\boxed{
\sum_{k=m}^{n}
\frac{V_k}{(k+1)^2}
\le
\frac{\nu}{3R^2}
}
\]

for every consecutive positive-V block whose factorial derivative ratio remains bounded by `R^-2`.

## 4. Interpretation

This removes the misleading possibility that the raw factor `(k+1)^2` alone makes the V-chain look large.

After factorial normalization, a long positive viscous directional-mixing block has only two ways to remain strong:

1. the geometric dispersion-drop coefficients `A_k` consume their finite budget;
2. the normalized ratios

\[
\boxed{\rho_k}
\]

become large, corresponding to collapse of the factorial derivative radius.

Thus the V-branch is now directly tied to the same derivative scaling used by the nonlinear generating-function track.

## 5. Relation to log-convexity of derivative energies

For the ordered derivative norm,

\[
E_k
=\int_{\mathbb R^3}|\xi|^{2k}|\widehat\omega(\xi)|^2d\xi
\]

(up to the Fourier normalization convention).

Cauchy--Schwarz gives

\[
\boxed{
E_k^2\le E_{k-1}E_{k+1}.
}
\]

Hence the raw ratios

\[
r_k=E_{k+1}/E_k
\]

are nondecreasing in `k` whenever the relevant moments are finite.

This reinforces the distinction between

- generic high-order growth of `r_k`, and
- genuine collapse measured after factorial normalization by `rho_k`.

No monotonicity of `rho_k` is claimed.

## 6. Revised S/V cycle

The derivative-order projective cycle should now be read as

\[
\boxed{
\textbf{S: }\sqrt{J_k}L_k
\qquad\text{versus}\qquad
\textbf{V: }\nu\rho_k\mathcal A_k
}
\]

after factorial normalization of derivative order.

If `rho_k` stays uniformly bounded on positive-V blocks, their normalized geometric contribution is finite.

If `rho_k` becomes unbounded, the derivative-radius channel collapses and the higher-derivative analyticity/sparseness track becomes active.

Therefore an infinite residual S--V cycle must alternate between

- nonlinear regeneration strong enough to rebuild directional dispersion, and/or
- factorial derivative-radius collapse.

The next target is to place the nonlinear S-channel `L_k` under the same factorial generating-function weight and test whether the two normalized branches admit a common summable majorant.

Status: **OPEN COMMON FACTORIAL S/V MAJORANT**.
