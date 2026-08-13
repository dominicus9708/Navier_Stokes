# Exact global `L^2` packing of new Gaussian between-scale residual increments

Date: 2026-08-13

Status: **EXACT GAUSSIAN SEMIGROUP / LITTLEWOOD--PALEY-TYPE PACKING IDENTITY; DOES NOT BY ITSELF PROVE REGULARITY**.

## 1. Setup

Let `P_Sigma` denote convolution with the centered Gaussian of covariance `Sigma`, and for a vector/matrix field `g` define

\[
\mathcal B_\Sigma[g]
=P_\Sigma(|g|^2)-|P_\Sigma g|^2.
\]

For nested covariances

\[
\Sigma_{k+1}=\Sigma_k+\Delta\Sigma_k,
\qquad \Delta\Sigma_k\succeq0,
\]

the Gaussian law of total variance gives

\[
\mathcal B_{\Sigma_{k+1}}[g]
=P_{\Delta\Sigma_k}\mathcal B_{\Sigma_k}[g]
+\mathcal B_{\Delta\Sigma_k}[P_{\Sigma_k}g].
\]

Define the genuinely new between-scale increment

\[
\boxed{
\Delta\mathcal B_k
:=\mathcal B_{\Delta\Sigma_k}[P_{\Sigma_k}g]
\ge0.
}
\]

The inherited first term is not counted again.

## 2. Exact global identity

Gaussian convolution preserves spatial integrals.  Therefore

\[
\begin{aligned}
\int_{\mathbb R^3}\Delta\mathcal B_k\,dx
&=
\int |P_{\Sigma_k}g|^2dx
-
\int|P_{\Delta\Sigma_k}P_{\Sigma_k}g|^2dx\\
&=
\boxed{
\|P_{\Sigma_k}g\|_2^2
-
\|P_{\Sigma_{k+1}}g\|_2^2.
}
\end{aligned}
\]

Summing over `k` telescopes:

\[
\boxed{
\sum_{k=0}^{N-1}
\int\Delta\mathcal B_k\,dx
=
\|P_{\Sigma_0}g\|_2^2
-
\|P_{\Sigma_N}g\|_2^2
\le
\|g\|_2^2.
}
\]

For the Navier--Stokes residual analysis, take

\[
g=\nabla U.
\]

Thus new scale-to-scale non-affinity is globally almost-orthogonal in the exact Gaussian-semigroup sense and is packed by the normalized enstrophy.

## 3. Fourier form

For isotropic heat scales `P_t=e^{t\Delta}`, Parseval gives

\[
\int\Delta\mathcal B_kdx
=
\int
\left(
 e^{-2t_k|\xi|^2}
-e^{-2t_{k+1}|\xi|^2}
\right)
|\widehat g(\xi)|^2d\xi.
\]

The multipliers are nonnegative and their sum telescopes frequency by frequency.  This is the precise Littlewood--Paley-type interpretation.

## 4. Important critical-wall audit

This identity removes double counting but does **not** create a logarithmic contradiction by itself.

A pointwise order-one increment at spatial scale `R` requires an `L^2` amount on the order of the corresponding volume `R^3`.  Across geometric scales the spatial cost is therefore dominated by the largest active scale rather than by the number of scales.

Consequently a repeated residual route can remain scale-critical by descending toward smaller natural scales.  Any successful closure must add a strict gain from geometry, axis coherence, precursor capacity, material flux, or another non-scale-neutral channel.

## 5. DSD interpretation

The identity implements a strict aggregation rule:

- inherited residual = already-described lower-scale information;
- between-scale residual = genuinely new information created between two resolutions.

Only the second term is charged to the scale ledger.

This is the appropriate non-double-counting rule for the DSD-assisted scale graph.
