# M19-199 — Aperiodic mean palinstrophy forces positive mean joint W1 severity

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / INVARIANT-MEAN W1 BRIDGE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Instantaneous W1 quantities

Define

\[
K(s):=\|\Omega(s)\|_\infty,
\qquad
\Gamma(s):=\sup_R\Gamma_R(s),
\qquad
W(s):=\|U(s)\|_{L^{3,\infty}}.
\]

The optimized core/tail split of M19-192 is pointwise in similarity time and gives

\[
\boxed{
Z(s):=\|\Omega(s)\|_2^2
\le
C_Z K(s)^{1/2}[\Gamma(s)W(s)]^{3/2}.
}
\]

## 2. Similarity enstrophy balance

The exact recurrent enstrophy identity is

\[
\frac12 Z'(s)+\frac14 Z(s)+\nu P(s)
=
\int\Omega\cdot S_U\Omega,
\qquad
P=\|\nabla\Omega\|_2^2.
\]

Calderon--Zygmund gives \(\|S_U\|_2\lesssim\|\Omega\|_2\). Interpolating

\[
\|\Omega\|_4^2
\le
\|\Omega\|_2\|\Omega\|_\infty
=Z^{1/2}K,
\]

we obtain

\[
\left|\int\Omega\cdot S_U\Omega\right|
\le C_s KZ.
\]

Long-time averaging on a compact recurrent component kills the \(Z'\) boundary term, hence

\[
\boxed{
\nu\overline P+\frac14\overline Z
\le C_s\langle KZ\rangle.
}
\]

## 3. Insert the pointwise W1 ceiling

From the pointwise optimized estimate,

\[
KZ
\le
C_Z K^{3/2}(\Gamma W)^{3/2}
=
C_Z[K\Gamma W]^{3/2}.
\]

Therefore

\[
\boxed{
\nu\overline P
\le
C_0\left\langle [K(s)\Gamma(s)W(s)]^{3/2}\right\rangle,
}
\]

where the positive \(\overline Z/4\) term was simply discarded.

## 4. Apply the aperiodic hard-dimension floor

M19-184--186 gives a positive threshold \(\mathcal P_*>0\) such that genuine aperiodicity requires

\[
\overline P\ge\mathcal P_*.
\]

Consequently

\[
\boxed{
\left\langle [K(s)\Gamma(s)W(s)]^{3/2}\right\rangle
\ge
c_0\nu\mathcal P_*>0.
}
\]

This is the persistent invariant-mean W1 severity condition.

## 5. Improvement over the supremum severity

The earlier coarse quantity

\[
\Xi_{W1}^\sharp
=\frac{K^\sharp(\Gamma^\sharp W^\sharp)^3}{\nu^3}
\]

is useful as a ceiling corollary but cannot distinguish persistent activity from rare spikes.

The new mean quantity

\[
\boxed{
\mathfrak S_{W1}
:=
\left\langle[K\Gamma W]^{3/2}\right\rangle
}
\]

is directly tied to the invariant palinstrophy payer and therefore is the sharper bridge.

## 6. Firewall

\[
\boxed{
\sup(K,\Gamma,W)\text{ information}
\neq
\text{mean joint severity},
}
\]

but genuine aperiodicity now forces the latter explicitly.

## 7. Next step

Because \(K,\Gamma,W\) are bounded on W1, the positive mean joint severity can be converted into a positive occupation fraction of a joint finite-high set. This removes the rare-spike escape at the product level and allows an occupation-weighted trichotomy.