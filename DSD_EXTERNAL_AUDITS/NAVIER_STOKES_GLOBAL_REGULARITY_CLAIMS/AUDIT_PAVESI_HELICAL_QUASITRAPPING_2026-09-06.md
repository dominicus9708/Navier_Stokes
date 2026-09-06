# DSD Audit — Pavesi Geometric Frustration / Helical Quasi-Trapping

Date: 2026-09-06
Paper family: Luca Eliseo Pavesi, *Global Regularity for the Three-Dimensional Incompressible Navier–Stokes Equations via Geometric Frustration and Helical Quasi-Trapping*, Zenodo 21158572 / 21172740 / 21194906.
Conditional predecessor: Zenodo 21113042.
Audit status: **UNCONDITIONAL HINGE FAIL; CONDITIONAL PREDECESSOR RETAINED**

## 1. Architecture

The manuscript separates its logic cleanly:

- Theorem 5.1: if a spectral flux estimate holds for every K, then regularity follows.
- Theorem 6.1: claims to prove that flux estimate unconditionally.
- Theorem 7.1: invokes 6.1 inside 5.1.

The central estimate is

\[
\boxed{
|\Pi(K,t)|\le C_*\frac{E_{>K}(t)^{1/2}E(t)^{1/2}}{K}
}
\]

with absolute data-independent `C_*`.

## 2. Amplitude-homogeneity audit

At a fixed instant, the Navier–Stokes nonlinear energy-transfer/flux functional is cubic in the velocity amplitude. Under

\[
u\mapsto Au,
\]

one has schematically

\[
\Pi(K;Au)=A^3\Pi(K;u).
\]

Energy is quadratic:

\[
E(Au)=A^2E(u),\qquad E_{>K}(Au)=A^2E_{>K}(u).
\]

Therefore the claimed right-hand side transforms as

\[
C_*\frac{E_{>K}(Au)^{1/2}E(Au)^{1/2}}K
=A^2C_*\frac{E_{>K}(u)^{1/2}E(u)^{1/2}}K.
\]

For any smooth divergence-free configuration with nonzero instantaneous spectral flux,

\[
A^3|\Pi(K;u)|
\le A^2 C_*\frac{E_{>K}^{1/2}E^{1/2}}K
\]

cannot hold for arbitrarily large A with one absolute constant.

This is a direct scaling counterexample to the unconditional form of Theorem 6.1.

## 3. Fourier-support audit of Lemma 6.2

The proof defines

\[
V_K=\{u:\hat u(k)=0\text{ for }|k|\le K\}
\]

and argues that the nonlinear cross-product interaction is essentially closed in `V_K`, with leakage below K of order `1/K` because dominant triads have comparable wave numbers.

But Fourier convolution obeys

\[
k=p+q.
\]

There is no support-theoretic exclusion of

\[
|p|,|q|\gg K,\qquad |p+q|\ll K.
\]

Take, for example,

\[
q=-p+k_0
\]

with fixed small nonzero `k_0` and arbitrarily large `|p|`. Both inputs lie arbitrarily high above K while the output is low frequency.

Therefore

\[
V_K\times V_K\not\subset V_K+O(K^{-1})
\]

as a deterministic support statement. A quantitative `1/K` gain would require additional cancellation/null structure with an explicit symbol estimate, not the assertion that the dominant triads are comparable.

## 4. Cross-helicity averaging audit

The cross-helicity lemma attributes an additional `1/K` gain to angular averaging after summing triads. Statistical angular cancellation cannot provide an unconditional deterministic bound for arbitrary smooth initial phases unless the spherical-harmonic sum is controlled in absolute/operator norm. Numerical observations of near-zero flux for selected aligned fields cannot substitute for such an estimate.

## 5. Conditional Theorem 5.1

The conditional implication should be preserved separately. Assuming the displayed flux inequality, the manuscript derives a tail inequality with strong K-decay. Even if some subsequent tail-to-enstrophy details require a separate audit, this conditional direction is mathematically distinct from the false unconditional derivation.

The paper family's earlier helicity-dominance preprint is therefore correctly classified as **conditional**, not as disproved merely because the unconditional upgrade fails.

## 6. DSD verdict

\[
\boxed{
\text{Theorem 6.1 cannot hold in its stated absolute form.}
}
\]

Two independent reasons are recorded:

1. amplitude degree `3` versus `2`;
2. high×high→low convolution leakage contradicting the asserted support closure.

Hence Theorem 7.1 does not follow.

Surviving research value: the helical decomposition, the conditional quasi-trapping criterion, and any correctly normalized symbol-level cancellation estimates remain worth independent study.

Global regularity remains unproved.
