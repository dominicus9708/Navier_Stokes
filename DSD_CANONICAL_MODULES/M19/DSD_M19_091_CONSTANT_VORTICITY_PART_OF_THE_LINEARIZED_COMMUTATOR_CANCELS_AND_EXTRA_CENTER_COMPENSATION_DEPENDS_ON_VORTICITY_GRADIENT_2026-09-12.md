# DSD M19-091 — Constant-vorticity part of the linearized commutator cancels and extra-center compensation depends on vorticity gradient

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / EXACT COMMUTATOR CANCELLATION / THE OMEGA-GRAD-W TERM DOES NOT REQUIRE AN OMEGA-INFINITY PAYMENT / BOTH NONLOCAL LINEARIZED VORTICITY COMMUTATOR TERMS DESCEND TO GRAD-OMEGA / SHARPENS THE M19-090 QUARTER-GAP TARGET / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Starting compensation form

M19-087 defines

\[
\mathcal C_U[W]
=
I_S+I_\Omega-I_{tr},
\]

where

\[
I_S:=\int \eta\cdot S_U\eta,
\]

\[
I_\Omega:=\int \eta\cdot(\Omega\cdot\nabla)W,
\]

and

\[
I_{tr}:=\int \eta\cdot(W\cdot\nabla)\Omega.
\]

A crude estimate of `I_Omega` by `||Omega||_infty ||eta||_2 ||grad W||_2` loses an important cancellation.

---

## 2. Pointwise vector identity

For each coordinate direction `j`, use

\[
\nabla\cdot(W\times\partial_jW)
=
\partial_jW\cdot(\nabla\times W)
-W\cdot\nabla\times(\partial_jW).
\]

Since

\[
\eta=\nabla\times W,
\qquad
\nabla\times(\partial_jW)=\partial_j\eta,
\]

we obtain

\[
\partial_jW\cdot\eta
=
W\cdot\partial_j\eta
+\nabla\cdot(W\times\partial_jW).
\]

Also

\[
\partial_j(W\cdot\eta)
=
\partial_jW\cdot\eta
+W\cdot\partial_j\eta.
\]

Eliminating `W dot partial_j eta` gives

\[
\boxed{
\eta\cdot\partial_jW
=
\frac12\partial_j(W\cdot\eta)
+\frac12\nabla\cdot(W\times\partial_jW).
}
\]

---

## 3. Exact cancellation of constant vorticity

Now

\[
I_\Omega
=
\int \Omega_j\,\eta\cdot\partial_jW\,dy.
\]

Insert the identity:

\[
\begin{aligned}
I_\Omega
={}&
\frac12\int\Omega_j\partial_j(W\cdot\eta)dy\\
&+
\frac12\int\Omega_j\partial_k(W\times\partial_jW)_kdy.
\end{aligned}
\]

Integrate by parts.

The first term vanishes because

\[
\partial_j\Omega_j=\nabla\cdot\Omega=0.
\]

Therefore

\[
\boxed{
I_\Omega
=-\frac12
\int
(\partial_k\Omega_j)
(W\times\partial_jW)_k\,dy.
}
\]

In particular a spatially constant vorticity field contributes exactly zero to `I_Omega`.

---

## 4. Quantitative bound

By Holder and Sobolev,

\[
\begin{aligned}
|I_\Omega|
&\lesssim
\|\nabla\Omega\|_3
\|W\|_6
\|\nabla W\|_2\\
&\lesssim
\|\nabla\Omega\|_3
\|\eta\|_2^2,
\end{aligned}
\]

because for divergence-free whole-space perturbations

\[
\|W\|_6\lesssim\|\nabla W\|_2,
\qquad
\|\nabla W\|_2=\|\eta\|_2.
\]

Hence

\[
\boxed{
|I_\Omega|
\lesssim
\|\nabla\Omega\|_3\|\eta\|_2^2.
}
\]

---

## 5. The transport-of-background-vorticity term has the same currency

For

\[
I_{tr}
=
\int\eta\cdot(W\cdot\nabla)\Omega,
\]

Holder gives

\[
|I_{tr}|
\le
\|\eta\|_2
\|W\|_6
\|\nabla\Omega\|_3.
\]

Thus

\[
\boxed{
|I_{tr}|
\lesssim
\|\nabla\Omega\|_3\|\eta\|_2^2.
}
\]

Consequently the two commutator terms together satisfy

\[
\boxed{
|I_\Omega-I_{tr}|
\lesssim
\|\nabla\Omega\|_3\|\eta\|_2^2.
}
\]

There is no independent `||Omega||_infty` payment in this sharpened estimate.

---

## 6. Strain term

The remaining compensation is

\[
I_S=\int\eta\cdot S_U\eta.
\]

Using

\[
\|S_U\|_3\lesssim\|\Omega\|_3
\]

by Calderon--Zygmund and

\[
\|\eta\|_3^2
\lesssim
\|\eta\|_2\|\nabla\eta\|_2,
\]

we get

\[
|I_S|
\lesssim
\|\Omega\|_3
\|\eta\|_2\|\nabla\eta\|_2.
\]

Young yields, for any `eps>0`,

\[
\boxed{
|I_S|
\le
\varepsilon\nu\|\nabla\eta\|_2^2
+C_\varepsilon\nu^{-1}\|\Omega\|_3^2\|\eta\|_2^2.
}
\]

---

## 7. Sharpened center-growth inequality

Insert the estimates into the exact M19-087 identity.

Choosing, for example, `eps=1/2`,

\[
\boxed{
\begin{aligned}
\frac12\frac d{d\theta}\|\eta\|_2^2
&+\frac\nu2\|\nabla\eta\|_2^2\\
&+\left[
\frac14
-C_1\nu^{-1}\|\Omega\|_3^2
-C_2\|\nabla\Omega\|_3
\right]\|\eta\|_2^2
\le0.
\end{aligned}
}
\]

Thus a sufficient strict-contraction condition is

\[
\boxed{
C_1\nu^{-1}\|\Omega\|_3^2
+C_2\|\nabla\Omega\|_3
<\frac14.
}
\]

A long-time averaged version gives the corresponding conditional exclusion of zero extra center.

---

## 8. Relation to the quarter-gap Ky-Fan budget

M19-090 requires

\[
\langle\kappa_1^\perp\rangle\ge\frac14
\]

for an extra center to exist.

M19-091 shows that the crude operator controlling `kappa_1^perp` can be reduced to

\[
\boxed{
\nu^{-1}\|\Omega\|_3^2
+\|\nabla\Omega\|_3,
}
\]

up to universal constants and the retained perturbation-palinstrophy term.

This removes a separate amplitude-only `||Omega||_infty` obstruction.

---

## 9. Why this does not close the theorem

The controlled recurrent corridor supplies boundedness and spacetime resource information for vorticity derivatives, but it does not presently imply the universal strict smallness

\[
C_1\nu^{-1}\|\Omega\|_3^2
+C_2\|\nabla\Omega\|_3
<\frac14
\]

at all times or in the exact projective average needed for every transverse center trajectory.

Therefore M19-091 sharpens the live spectral quantity but does not prove `E_extra=0`.

---

## 10. Immediate next question

The next useful calculation is to compare the new compensation currency

\[
\nu^{-1}\|\Omega\|_3^2
+\|\nabla\Omega\|_3
\]

against the invariant recurrent enstrophy/palinstrophy identities.

Two possibilities must be separated:

1. these quantities can be forced below the quarter-gap on a positive-density set sufficient for projective contraction;
2. persistent saturation above the gap creates a new quantitative background concentration event that can be routed to an existing M18/M19 payer branch.

This is the correct continuation of the finite-dimensional center program.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
