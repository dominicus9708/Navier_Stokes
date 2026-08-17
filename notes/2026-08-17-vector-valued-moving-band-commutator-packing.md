# Vector-valued moving-band commutator packing

Date: 2026-08-17

Status: **DERIVED MODULO THE STANDARD VECTOR-VALUED COIFMAN--MEYER/LITTLEWOOD--PALEY COMMUTATOR BOUND. MULTIPLE MOVING BANDS CANNOT REUSE ONE DERIVATIVE PULSE WITHOUT A SINGLE GLOBAL PALINSTROPHY/V2 PRICE. GLOBAL REGULARITY NOT PROVED.**

## 1. Setup

Let `P_k` be a smooth dyadic Littlewood--Paley partition at physical frequency

\[
K_k=2^k,
\]

and let

\[
\eta_k=P_k\omega,
\qquad
E_k=\|\eta_k\|_2^2.
\]

The exact band production decomposition is

\[
\Pi_k
=\mathcal L_k+\mathcal C_k,
\]

where

\[
\mathcal L_k=\langle S\eta_k,\eta_k\rangle
\]

and

\[
\mathcal C_k
=\langle R_k,\eta_k\rangle,
\qquad
R_k=[u\cdot\nabla,P_k]\omega+[P_k,S]\omega.
\]

On a first-hitting past we retain

\[
\|\omega\|_\infty\le W
\]

in physical variables, or `<=1` after terminal normalization.

## 2. Vector-valued commutator bound

The dyadic commutator symbols satisfy a uniform first-order Coifman--Meyer structure. In the terminal-normalized variables, the standard vector-valued LP commutator theorem gives

\[
\boxed{
\left(
\sum_kK_k^2\|R_k\|_2^2
\right)^{1/2}
\lesssim
P^{1/2}+P^{3/4}Z^{1/4},
}
\]

where

\[
P=\|\nabla\omega\|_2^2,
\qquad
Z=\|\nabla^2\omega\|_2^2.
\]

The first term comes from `[P_k,S]omega`; the second comes from the advective commutator.

The key improvement over the previous per-band estimate is that the right-hand side is paid **once**, not once for every `k`.

## 3. Couple to the kinetic-energy square function

By Littlewood--Paley and Biot--Savart,

\[
\boxed{
\sum_kK_k^{-2}E_k
\asymp
\|\omega\|_{\dot H^{-1}}^2
\asymp
\|u\|_2^2.
}
\]

Therefore Cauchy--Schwarz over the band index gives

\[
\begin{aligned}
\sum_k|\mathcal C_k|
&\le
\left(
\sum_kK_k^2\|R_k\|_2^2
\right)^{1/2}
\left(
\sum_kK_k^{-2}E_k
\right)^{1/2}\\
&\lesssim
\|u\|_2
\left(
P^{1/2}+P^{3/4}Z^{1/4}
\right).
\end{aligned}
\]

Thus

\[
\boxed{
\sum_k|\mathcal C_k(t)|
\lesssim
\|u_0\|_2
\left(
P^{1/2}+P^{3/4}Z^{1/4}
\right).
}
\]

The energy factor is globally bounded on the smooth lifespan.

## 4. High-frequency critical weighting

For a high-frequency tail `k>=k0`,

\[
\sum_{k\ge k_0}K_k^{-1}|\mathcal C_k|
\]

is bounded by

\[
\left(
\sum_{k\ge k_0}K_k^2\|R_k\|_2^2
\right)^{1/2}
\left(
\sum_{k\ge k_0}K_k^{-4}E_k
\right)^{1/2}.
\]

Because

\[
K_k^{-4}E_k
\le
K_{k_0}^{-2}K_k^{-2}E_k,
\]

we obtain

\[
\boxed{
\sum_{k\ge k_0}K_k^{-1}|\mathcal C_k|
\lesssim
K_{k_0}^{-1}\|u_0\|_2
\left(
P^{1/2}+P^{3/4}Z^{1/4}
\right).
}
\]

Hence positive transfer of a scale-critical `E_k/K_k` charge to frequencies tending to infinity forces the derivative action to grow at least proportionally to the active frequency floor unless direct stretching supplies the charge instead.

## 5. Interpretation

The previous loophole was:

\[
\text{one derivative pulse}
\to
\text{many bands all claim the same price}.
\]

The vector-valued estimate removes that bookkeeping artifact. All commutator-driven repopulations occurring at the same time are charged to one global derivative quantity.

This does **not** yet yield a contradiction, because the palinstrophy/V2 action may diverge near a hypothetical singular time. The remaining task is to combine the moving-band lower charge with the scale-critical direct-stretch lane and determine whether alternating between the two can remain compatible with the finite-energy solution class.

Status: **COMMUTATOR MULTIPLICITY REMOVED / HIGH-FREQUENCY CRITICAL TRANSFER REQUIRES GLOBAL DERIVATIVE GROWTH / NO GLOBAL-REGULARITY CONTRADICTION YET.**