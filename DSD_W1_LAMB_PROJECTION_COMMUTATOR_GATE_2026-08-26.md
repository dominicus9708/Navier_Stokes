# DSD W1 Lamb Projection-Commutator Gate

Date: 2026-08-26

Status: **CRITICAL p=3 SOURCE IDENTIFIED AS A HELMHOLTZ--AMPLITUDE COMMUTATOR PAIRING IN THE REGULARIZED/GAUSSIAN DUALITY FRAMEWORK / POINTWISE LAMB ORTHOGONALITY REMOVES THE DIRECT MULTIPLIER TERM / PREVIOUS WHOLE-SPACE W1 L2-WORK CANCELLATION REMOVED BECAUSE A CRITICAL 1/R W1 TAIL NEED NOT BE IN L2 / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The solenoidal Lamb force is

\[
L_s=\mathbb P(\Omega\times U).
\]

The full Lamb vector

\[
L=\Omega\times U
\]

is pointwise perpendicular to the velocity:

\[
U\cdot L=0.
\]

The p=3 velocity multiplier can nevertheless receive nonzero projected nonlinear work because multiplication by a nonconstant amplitude does not commute with the Helmholtz projector.

---

## 2. Critical multiplier

For the Gaussian p=3 scale ledger, set

\[
\phi_R(Y)
=
\exp\left(-\frac{|Y|^2}{8\nu R^2}\right),
\]

and

\[
\boxed{m_R(Y):=\phi_R(Y)|U(Y)|.}
\]

The nonlinear source is

\[
F_R
=-\int m_R U\cdot L_s\,dY.
\]

Since `L_s=P L`,

\[
F_R
=-\langle m_RU,\mathbb P L\rangle.
\]

The brackets in this note are understood through the same Gaussian/localized regularization used in the p=3 ledger; no global W1 L2 pairing is assumed.

---

## 3. Move the projector to the multiplier

For a regularized Gaussian pairing the Leray/Helmholtz projector may be moved by self-adjoint duality:

\[
F_R
=-\langle \mathbb P(m_RU),L\rangle.
\]

Because `PU=U` distributionally,

\[
\mathbb P(m_RU)
=
m_RU+[\mathbb P,m_R]U,
\]

where

\[
[\mathbb P,m_R]U
:=
\mathbb P(m_RU)-m_R\mathbb P U.
\]

The direct term vanishes pointwise:

\[
\langle m_RU,L\rangle
=
\int m_R U\cdot(\Omega\times U)dY
=0.
\]

Therefore

\[
\boxed{
F_R
=-
\left\langle
[\mathbb P,m_R]U,
\Omega\times U
\right\rangle.
}
\]

This is the correct regularized commutator identity.

Importantly, its proof uses the pointwise identity `U dot L=0`; it does **not** require the invalid whole-space W1 statement `int U dot L_s=0`.

---

## 4. Structural meaning

The p=3 source has three required ingredients:

1. nonzero Lamb force `Omega x U`;
2. nonconstant scalar multiplier `m_R=phi_R |U|`;
3. nonlocal Helmholtz projection.

If `m_R` were spatially constant, then

\[
[\mathbb P,m_R]=0
\]

and hence

\[
F_R=0.
\]

Thus the critical nonlinear source is not direct work by the Lamb vector. It is **projection conversion caused by amplitude inhomogeneity**.

---

## 5. Large-radius form and scope

As `R->infinity`,

\[
\phi_R\to1
\]

on every fixed region. Formally, and rigorously only in a framework where the endpoint domination/renormalized pairing has been justified,

\[
F_\infty
=-
\left\langle
[\mathbb P,|U|]U,
\Omega\times U
\right\rangle.
\]

The notation `F_infinity` must therefore be interpreted as an endpoint/renormalized limit, not as an ordinary whole-space L2 inner product on the W1 state.

This is consistent with the separately identified positive p=3 scale-infinity residue.

---

## 6. Relation to standard commutator theory

The Helmholtz projector is built from Riesz transforms. Classical Calderon--Zygmund commutator theory gives, in admissible `1<p<infinity` frameworks, estimates schematically of the form

\[
\|[\mathbb P,m]f\|_p
\lesssim
\|m\|_{BMO}\|f\|_p.
\]

Thus the identity shows that a positive critical source requires nontrivial amplitude oscillation in any localized dual framework in which the remaining Lamb factor is controlled.

This note does not claim a globally finite or small BMO norm for the W1 amplitude.

---

## 7. Combination with the vorticity current

The pressure-free vorticity current depends on

\[
\nabla\times L_s
=
\nabla\times L.
\]

Thus the survivor simultaneously requires

\[
\boxed{
\text{nonzero projection commutator}
}
\]

and

\[
\boxed{
\text{nonzero curl activity of the same Lamb field}.
}
\]

In DSD language these are

- **projection conversion**: a pointwise transverse nonlinear force becomes nonzero critical multiplier work after nonlocal projection and nonconstant weighting;
- **structural reformation/cascade**: the same force has sufficient curl action to maintain the vorticity current.

---

## 8. Corrected endpoint signature

A hypothetical nontrivial W1 survivor must satisfy the regularized critical-work condition

\[
\boxed{
-\left\langle
[\mathbb P,m_R]U,L
\right\rangle
=F_R,
}
\]

with the invariant endpoint surplus

\[
\boxed{
\langle F_R-\nu D_R\rangle
\longrightarrow
\frac{\mathscr R_3}{6}>0,
}
\]

and the derivative pairing

\[
\boxed{
\left\langle
\int\Delta U\cdot L_s
\right\rangle
=
\frac14\langle Z\rangle+
u\langle P_\Omega\rangle
>0.
}
\]

What may **not** be added at the W1 level is

\[
\int_{\mathbb R^3}U\cdot L_s=0,
\]

because a critical `1/R` W1 tail generally gives `U notin L2(R3)`.

The exact zero nonlinear-energy work remains true on every finite-energy physical prelimit and on genuine L2 tail-subtracted quotients.

The gap between that prelimit cancellation and the positive W1 critical commutator is therefore itself an interface/scale-infinity problem.

---

## 9. What remains

The commutator representation isolates the sharper target

\[
\boxed{
\text{control the recurrent W1 amplitude/Hodge commutator from the finite-energy prelimit,}
\quad
F_R-\nu D_R\to\mathscr R_3/6>0.
}
\]

Possible routes are:

1. a critical localized BMO/Hardy estimate with a prelimit-uniform interface bound;
2. an expanding-window compactness theorem that transfers the finite-energy cancellation to similarity infinity;
3. a canonical-tail subtraction producing a finite-energy quotient and an exact forced commutator ledger.

No estimate of sufficient strength has yet been proved.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
