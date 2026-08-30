# DSD M5-329 — Atom to First-Hitting Critical Action

Date: 2026-08-30

Status: **ATOM FORCES NONSUMMABLE PARENT CRITICAL GRADIENT ACTION ON THE FIRST-HITTING PARTITION / GLOBAL REGULARITY UNPROVED.**

## 1. Atom action

From M5-327, every sufficiently late Huang cell `I_j` obeys

\[
\int_{I_j}\|\nabla u\|_3^2dt\ge c_3\nu>0.
\]

Because the Huang cells are disjoint and accumulate at `T_*`, summation gives

\[
\boxed{\int^{T_*}\|\nabla u(t)\|_3^2dt=\infty.}
\]

## 2. First-hitting partition

Let `J_k=[t_k,t_{k+1}]` be the late first-hitting stages and set

\[
\mathcal A_k:=\int_{J_k}\|\nabla u\|_3^2dt.
\]

Since these stages form another partition of the same terminal interval,

\[
\boxed{\sum_k\mathcal A_k=\infty.}
\]

Thus exact alignment between Huang cell endpoints and first-hitting endpoints is not required for this additive quantity.

## 3. Exact normalization

At natural length `r_k`, write

\[
U_k(y,\tau)=r_k u(X_k+r_ky,t_k+r_k^2\tau).
\]

Then

\[
\boxed{\mathcal A_k=\int_{\widehat J_k}\|\nabla U_k\|_3^2d\tau,}
\]

so the action is exactly Navier–Stokes scale invariant.

Define

\[
D_k=\int_{\widehat J_k}\|\nabla U_k\|_2^2d\tau,
\qquad
H_k=\int_{\widehat J_k}\|\nabla^2U_k\|_2^2d\tau.
\]

Interpolation gives

\[
\mathcal A_k\lesssim\sqrt{D_kH_k}.
\]

Hence

\[
\boxed{\sum_k\sqrt{D_kH_k}=\infty.}
\]

## 4. Non-H corridor

For a divergence-free whole-space normalized field,

\[
\|\nabla^2U_k\|_2^2=\|\nabla\Omega_k\|_2^2.
\]

If the pure non-H corridor gives `P_Omega<=P_*` and normalized stage length `<=L_*`, then

\[
H_k\le P_*L_*.
\]

Therefore an atom forces

\[
\boxed{\sum_k\sqrt{D_k}=\infty}
\]

on that corridor.

This is not by itself a contradiction because physical dissipation is weighted by the shrinking scale `r_k`:

\[
\sum_k r_kD_k<\infty
\]

may still hold.

## 5. Scope

The current result is a parent-only nonsummable critical action statement. It must not be identified with the corrected spatial shell reformation action, which is a different quantity.

The next task is to determine whether repeated `sqrt(D_k H_k)` action forces actual shell reformation, projective/axis turnover, or a persistent critical current.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
