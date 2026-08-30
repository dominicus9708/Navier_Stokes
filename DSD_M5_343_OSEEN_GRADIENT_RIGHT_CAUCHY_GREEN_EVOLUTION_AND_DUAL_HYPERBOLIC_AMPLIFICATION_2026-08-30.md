# DSD M5-343 — Oseen-Gradient Right Cauchy–Green Evolution / Dual Hyperbolic Amplification

Date: 2026-08-30

Status: **EXACT EVOLUTION OF `C_H=(grad H)^T grad H` DERIVED / PARENT COMPRESSION AMPLIFIES OSEEN DERIVATIVE ENERGY IN THE COMPRESSIVE DIRECTION WHILE THE SAME STRAIN CAN AMPLIFY PHYSICAL VORTICITY IN THE EXTENSIONAL PLANE / SAME-SECTOR DUAL-AXIS GEOMETRY IS DYNAMICALLY NATURAL, NOT ALGEBRAICALLY FRUSTRATED / PRESSURE, DIFFUSION, ROTATION, OR STRAIN REFORMATION ARE THE ONLY COUNTER-CHANNELS / GLOBAL REGULARITY UNPROVED.**

## 1. Constrained Oseen equation

Let `H` solve the constrained solenoidal Oseen equation

\[
\partial_tH+(u\cdot\nabla)H+\nabla\pi_H=\nu\Delta H,
\qquad
\nabla\cdot H=0.
\]

Set

\[
G=\nabla H,
\qquad
A=\nabla u=S+W.
\]

Differentiating gives

\[
\boxed{
D_tG+GA+\nabla^2\pi_H=\nu\Delta G.
}
\]

## 2. Right Cauchy–Green tensor

Define the positive semidefinite derivative-space tensor

\[
\boxed{
C_H=G^TG.
}
\]

Let

\[
\mathcal D_G
:=\sum_m(\partial_mG)^T(\partial_mG)\ge0.
\]

Using

\[
\Delta(G^TG)
=(\Delta G)^TG+G^T\Delta G+2\mathcal D_G,
\]

one obtains

\[
\boxed{
D_tC_H
=\nu\Delta C_H
-2\nu\mathcal D_G
-A^TC_H-C_HA
-(\nabla^2\pi_H)G
-G^T(\nabla^2\pi_H).
}
\]

## 3. Strain/rotation split

Since

\[
A=S+W,
\qquad S^T=S,
\qquad W^T=-W,
\]

\[
-A^TC_H-C_HA
=-SC_H-C_HS
+WC_H-C_HW.
\]

Thus

\[
\boxed{
D_tC_H
=\nu\Delta C_H
-2\nu\mathcal D_G
-SC_H-C_HS
+[W,C_H]
-\mathcal P_H,
}
\]

where

\[
\mathcal P_H
:=(\nabla^2\pi_H)G+G^T(\nabla^2\pi_H).
\]

The commutator `[W,C_H]` rotates the derivative tensor, while `-SC_H-C_HS` changes its directional amplitudes.

## 4. Compressive-direction amplification

Work instantaneously in the parent strain eigenframe.
If `C_H` is approximately diagonal in that frame, then the strain contribution to its diagonal entries is

\[
\boxed{
(D_tC_H)_{ii}\supset -2\lambda_i(C_H)_{ii}.
}
\]

In the same-sector geometry

\[
\lambda_1\ge\lambda_2>0>\lambda_3,
\]

therefore

\[
-2\lambda_3(C_H)_{33}
=2|\lambda_3|(C_H)_{33}>0.
\]

Hence parent compression **amplifies spatial derivative energy of the Oseen field along the compressive direction**.

By contrast

\[
-2\lambda_{1,2}(C_H)_{11,22}<0
\]

for the extensional derivative directions.

## 5. Physical vorticity experiences the complementary action

The physical vorticity obeys

\[
D_t\omega=S\omega+\nu\Delta\omega.
\]

Thus vorticity components in the extensional `e_1,e_2` plane are amplified by the same parent strain that amplifies Oseen derivative energy along `e_3`.

This gives the local hyperbolic duality

\[
\boxed{
\begin{array}{c}
\text{physical vorticity: extensional-plane amplification},\\
\text{Oseen gradient: compressive-direction derivative amplification}.
\end{array}
}
\]

The two demands are complementary rather than contradictory.

## 6. Consequence for the proof strategy

The dual-axis same-sector branch cannot be closed by an orientation-counting argument.
Indeed the strain itself dynamically reinforces the two axis occupancies selected by the first-hitting and atom mechanisms.

To disrupt this dual amplification, at least one of the remaining terms in the `C_H` equation must act nontrivially:

\[
\boxed{
\text{Oseen diffusion}
\lor
\text{parent rotation/eigenframe commutator}
\lor
\text{Oseen pressure-Hessian coupling}
\lor
\text{parent strain reformation}.
}
\]

These are second-order/projective/pressure/turnover channels.

## 7. Integrated H1 energy compatibility

Taking the trace and integrating over space recovers the Oseen H1 identity. The pressure term vanishes after integration by parts against the divergence-free Oseen field, while the strain contraction gives

\[
-\int S:C_H.
\]

Thus the pointwise directional evolution is consistent with the earlier atom production ledger.

## 8. Formation/axis verdict

The formation analysis now identifies the same-sector endpoint as a **dual hyperbolic amplifier** rather than a conflicting two-axis state.

Its minimal dynamic descriptor is

\[
\boxed{
(S,\xi,C_H,[W,C_H],\mathcal P_H,\mathcal D_G).
}
\]

The next useful question is whether a persistent dual amplifier can keep all three counter-channels small while remaining compatible with finite-energy parent ancestry.

## 9. Scope

No claim is made that the dual hyperbolic amplifier is impossible.
On the contrary, the calculation shows why it is a plausible hard local blow-up geometry.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
