# Correction: projective partner variance forces magnitude-or-angular gradient damping, not angular damping alone

Date: 2026-08-18

Status: **EXHAUSTIVENESS CORRECTION. A BROAD WINDOW CONTAINING NONCOLLINEAR INTENSE PACKETS NEED NOT PAY ANGULAR PALINSTROPHY IF THE VORTICITY MAGNITUDE DROPS TO NEAR ZERO BETWEEN THE PACKETS. IN THAT CASE THE DIRECTION MAY ROTATE CHEAPLY, BUT THE MAGNITUDE INTERFACE PAYS IN P_mag. GAUSSIAN POINCARE GIVES A ROBUST TOTAL-GRADIENT DICHOTOMY. GLOBAL REGULARITY NOT PROVED.**

## 1. The gap in the angular-only statement

Write

\[
\omega=\rho\xi,
\qquad \rho=|\omega|.
\]

On the nonzero set,

\[
\boxed{
|\nabla\omega|^2
=|\nabla\rho|^2+ho^2|\nabla\xi|^2.
}
\]

A previous packet-network interpretation said that a positive broad-window projective defect automatically yields positive angular palinstrophy

\[
P_{\rm ang}=\int\rho^2|\nabla\xi|^2.
\]

That requires a **thick intense connection** between the differing directions.  It is false for two separated intense blobs if `rho` first decays to almost zero, the direction changes in the low-magnitude gap, and `rho` rises again.

## 2. Robust Gaussian Poincare bridge

Let `gamma_r` be a Gaussian probability weight of scale `r`.  The Gaussian Poincare inequality gives componentwise

\[
\operatorname{Var}_{\gamma_r}(\omega)
\lesssim
r^2\int\gamma_r|\nabla\omega|^2.
\]

Using the magnitude-direction decomposition,

\[
\boxed{
\operatorname{Var}_{\gamma_r}(\omega)
\lesssim
r^2\left(
P_{\rm mag,\gamma_r}
+P_{\rm ang,\gamma_r}
\right),
}
\]

where

\[
P_{\rm mag,\gamma_r}
=\int\gamma_r|\nabla\rho|^2,
\]

\[
P_{\rm ang,\gamma_r}
=\int\gamma_r\rho^2|\nabla\xi|^2.
\]

The weighted vector variance already splits exactly into projective and signed-line defects:

\[
\operatorname{Var}_{\gamma_r}(\omega)
=D_{\rm proj,\gamma_r}+D_{\rm line,\gamma_r}.
\]

Hence

\[
\boxed{
D_{\rm proj,\gamma_r}+D_{\rm line,\gamma_r}
\lesssim
r^2(P_{\rm mag,\gamma_r}+P_{\rm ang,\gamma_r}).
}
\]

## 3. Partner-network consequence

Suppose a bounded-geometry same-scale source requires an order-one broad-window projective/signed partner variance.  Then

\[
D_{\rm proj}+D_{\rm line}\ge d_0>0
\]

and therefore

\[
\boxed{
P_{\rm mag}+P_{\rm ang}
\gtrsim d_0 r^{-2}.
}
\]

There are two geometric realizations.

### Thick-direction transition

If the vorticity magnitude remains bounded below through the connection between the packet directions, the cost appears substantially in

\[
P_{\rm ang}.
\]

### Magnitude-gap transition

If the field avoids angular cost by reducing `rho` before rotating the direction, it must create interfaces where `rho` falls and rises.  The cost then appears in

\[
P_{\rm mag}.
\]

Thus the correct exhaustive statement is

\[
\boxed{
\text{projective partner supply}
\Rightarrow
\text{angular gradient damping}
\quad\lor\quad
\text{magnitude-interface damping},
}
\]

up to the already typed kernel-weight/reach concentration escape.

## 4. Exact magnitude-energy equation pays both costs

The squared vorticity-magnitude equation is

\[
(\partial_t+u\cdot\nabla-\nu\Delta)\frac{\rho^2}{2}
=
\rho^2\xi^TS\xi
-\nu|\nabla\rho|^2
-\nu\rho^2|\nabla\xi|^2.
\]

Therefore both `P_mag` and `P_ang` enter with the same negative viscous sign.  The low-magnitude-gap construction does not evade the direct dissipative ledger; it merely changes which piece pays.

Using the exact terminal adjoint kernel removes cutoff and transport errors from the integrated version.

## 5. Revised source-partner branch

The corrected bounded-geometry branch is

\[
\boxed{
\text{order-one pair source}
\Rightarrow
D_{\rm proj/line}\gtrsim1
\Rightarrow
P_{\rm mag}+P_{\rm ang}\gtrsim r^{-2},
}
\]

unless the source is concentrated on anomalously weighted close pairs, which remains the reach/kernel-concentration branch.

This supersedes any statement that broad projective partner variance **by itself** forces angular palinstrophy without a thickness hypothesis.

Status: **ANGULAR-ONLY PARTNER CLAIM CORRECTED / ROBUST TOTAL MAGNITUDE+ANGULAR GRADIENT DAMPING RESTORED / SEPARATED-BLOB LOOPHOLE CLOSED INTO P_mag / GLOBAL REGULARITY NOT PROVED.**