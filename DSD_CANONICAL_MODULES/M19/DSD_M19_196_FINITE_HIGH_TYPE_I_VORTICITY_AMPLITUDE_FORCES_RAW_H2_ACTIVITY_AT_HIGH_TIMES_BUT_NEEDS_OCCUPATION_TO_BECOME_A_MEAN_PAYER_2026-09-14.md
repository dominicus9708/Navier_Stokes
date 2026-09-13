# M19-196 — Finite-high Type-I vorticity amplitude forces raw-H2 activity at high times, but needs occupation to become a mean payer

**Date:** 2026-09-14  
**Status:** CONDITIONAL PAYER / FINITE-HIGH BRANCH AUDIT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Intrinsic amplitude

Let

\[
K(s):=\|\Omega(s)\|_{L^\infty},
\qquad
K^\sharp=\sup_s K(s)<\infty.
\]

A finite-high value of \(K^\sharp\) is not Type-II behavior; Type-II is the separate unbounded-amplitude complement.

## 2. Instantaneous derivative payer

On the retained smooth W1 corridor, the three-dimensional Gagliardo--Nirenberg inequality gives

\[
\|\Omega\|_\infty
\le C\|D^2\Omega\|_2^{3/4}\|\Omega\|_2^{1/4}.
\]

Writing

\[
Z=\|\Omega\|_2^2,
\qquad
H=\|D^2\Omega\|_2^2,
\]

this becomes

\[
K\le C H^{3/8}Z^{1/8}.
\]

Hence, whenever \(Z\le Z_+\),

\[
\boxed{
H(s)\ge c\,K(s)^{8/3}Z_+^{-1/3}.
}
\]

Thus a genuinely large finite Type-I amplitude at a given similarity time forces a raw-H2 event at that time.

## 3. Occupation-dependent mean payer

For a threshold \(k>0\), let

\[
E_k:=\{s:K(s)\ge k\}.
\]

If an invariant time mean assigns occupation fraction \(\theta_k>0\) to this set, then

\[
\boxed{
\overline H
\ge
c\,\theta_k\,k^{8/3}Z_+^{-1/3}.
}
\]

Therefore the finite-high \(K\)-branch converts to a persistent derivative payer **only after** an occupation lower bound is certified.

## 4. What the supremum alone does not imply

A large value of \(K^\sharp\) can be produced by rare recurrent spikes whose time density tends to zero. The instantaneous H2 lower bound then does not give a positive quantitative long-time mean independent of the spike occupation.

Hence

\[
\boxed{
K^\sharp\text{-high}
\not\Longrightarrow
\overline H\text{-high}
}
\]

without an occupation theorem.

## 5. Branch verdict

Finite-high Type-I amplitude is therefore not a new closed root and is not identical to Type-II. Its certified routing is

\[
\boxed{
K^\sharp\text{-high}
\Longrightarrow
\text{instantaneous raw-H2 activity at high times}
\quad+
\text{occupation problem}.
}
\]

This supports M19-195: the invariant mean-palinstrophy frontier remains primary.