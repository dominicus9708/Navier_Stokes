# DSD W1 Solenoidal-Lamb Spectral Transfer Ledger

Date: 2026-08-26

Status: **EXACT ZERO TOTAL ENERGY WORK + POSITIVE INVARIANT ENSTROPHY-WEIGHTED WORK DERIVED FOR THE SAME SOLENOIDAL LAMB FORCE / W1 NONLINEAR ENDPOINT IDENTIFIED AS A CRITICAL CASCADE OPERATOR RATHER THAN AN ENERGY SOURCE / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The Lamb--Hodge note identified

\[
L_s:=\mathbb P(\Omega\times U)
\]

as the single nonlinear structural force behind both mandatory W1 critical currents.

The next DSD question is whether this force acts as an external source of energy or only redistributes already existing energy among scales.

The answer is exact: it performs zero total kinetic-energy work but positive enstrophy-weighted work on every nontrivial invariant W1 class.

Thus the endpoint is a cascade requirement.

---

## 2. Zero total nonlinear kinetic-energy work

Because `U` is divergence-free and the Leray projector is self-adjoint in whole-space L2,

\[
\int U\cdot L_s
=
\int U\cdot\mathbb P L
=
\int \mathbb P U\cdot L
=
\int U\cdot L.
\]

But

\[
U\cdot L
=
U\cdot(\Omega\times U)=0
\]

pointwise.

Therefore

\[
\boxed{
\int_{\mathbb R^3}U\cdot L_s\,dY=0.
}
\]

This is the nonlinear kinetic-energy conservation identity in Lamb form.

It is independent of recurrence and holds at each sufficiently regular time.

---

## 3. Positive enstrophy-weighted nonlinear work

The nonlinear vorticity term is

\[
\nabla\times L_s.
\]

Let

\[
Z:=\|\Omega\|_2^2,
\qquad
P_\Omega:=\|\nabla\Omega\|_2^2,
\]

and

\[
Q:=\int\Omega\cdot S\Omega.
\]

Using

\[
\nabla\times\Omega=-\Delta U,
\]

and curl integration by parts,

\[
\int \Omega\cdot(\nabla\times L_s)
=
\int L_s\cdot(\nabla\times\Omega)
=-\int L_s\cdot\Delta U.
\]

On the other hand,

\[
\int \Omega\cdot(\nabla\times L_s)
=
- Q.
\]

Hence

\[
\boxed{
Q
=
\int \Delta U\cdot L_s\,dY.
}
\]

The invariant W1 enstrophy identity already gives

\[
\boxed{
\langle Q\rangle_\mu
=
\frac14\langle Z\rangle_\mu
+\nu\langle P_\Omega\rangle_\mu
>0.
}
\]

Therefore

\[
\boxed{
\left\langle
\int \Delta U\cdot L_s
\right\rangle_\mu
>0.
}
\]

The same nonlinear force that performs zero total energy work must perform strictly positive Laplacian/enstrophy-weighted work on average.

---

## 4. Fourier transfer density

Use a Fourier convention in which Parseval constants are suppressed for readability.

Define the signed nonlinear kinetic-energy transfer density

\[
\boxed{
T(k,s)
:=-\operatorname{Re}
\bigl(\widehat U(k,s)\cdot\overline{\widehat{L_s}(k,s)}\bigr).
}
\]

Then the zero-energy-work identity becomes

\[
\boxed{
\int_{\mathbb R^3}T(k,s)\,dk=0.
}
\]

Also

\[
\int \Delta U\cdot L_s
=
-\int |k|^2
\operatorname{Re}
(\widehat U\cdot\overline{\widehat{L_s}})dk,
\]

so

\[
\boxed{
Q(s)
=
\int |k|^2T(k,s)\,dk.
}
\]

Invariant averaging yields

\[
\boxed{
\int |k|^2\langle T(k)\rangle_\mu dk
=
\frac14\langle Z\rangle_\mu
+\nu\langle P_\Omega\rangle_\mu
>0,
}
\]

while

\[
\boxed{
\int\langle T(k)\rangle_\mu dk=0.
}
\]

Therefore the nonlinear transfer cannot have one sign or remain spectrally neutral.  Positive energy transfer must be weighted toward higher wave numbers than the compensating negative transfer.

---

## 5. DSD interpretation: the nonlinear field is a transfer operator

The W1 survivor does not require the Navier--Stokes nonlinearity to create kinetic energy.

It requires

\[
\boxed{
\text{zero net nonlinear energy work}
+
\text{positive high-frequency-weighted nonlinear work}.
}
\]

Thus `L_s` acts as a scale-conversion operator:

\[
\boxed{
\text{lower-frequency donor sector}
\longrightarrow
\text{higher-frequency recipient sector}.
}
\]

Viscosity then acts on the recipient sector.

In backward Leray variables the similarity terms can replenish the normalized state, so this transfer pattern is not by itself contradictory with an unforced physical solution.

---

## 6. Relation to the p=3 critical current

The same field also satisfies

\[
\boxed{
F_R
=-\int\phi_R|U|U\cdot L_s.
}
\]

For the invariant W1 endpoint,

\[
\bar F_R
=
\nu\bar D_R+\mathcal S_B(R),
\]

with

\[
\mathcal S_B(R)\to\mathscr R_3/6>0.
\]

Thus `L_s` simultaneously has

1. zero unweighted L2 energy pairing with `U`;
2. strictly signed critical p=3 weighted pairing with `|U|U`;
3. strictly positive invariant Laplacian pairing with `U`.

Schematically,

\[
\boxed{
\langle U,L_s\rangle=0,
\qquad
-\langle |U|U,L_s\rangle_{critical}>0,
\qquad
\langle\Delta U,L_s\rangle_{avg}>0.
}
\]

This is the current three-moment signature of a hypothetical W1 singular cascade.

---

## 7. Why this does not yet contradict finite physical energy

A positive normalized cascade action per Leray time does not automatically produce a divergent physical energy cost.

The backward self-similar conversion attaches shrinking physical weights to late normalized events. This is the previously identified half-power barrier.

Similarly, ordinary physical enstrophy dissipation is compatible with a Type-I critical cascade because its late-time growth may remain time integrable.

Therefore the three-moment signature is a necessary structural condition, not yet a nonexistence theorem.

---

## 8. Updated endpoint search

The DSD reduction now suggests that a successful theorem should not seek an external energy source contradiction.

It should seek a **nonrepeatability or compactness obstruction for a recurrent critical transfer operator** satisfying all three pairings above.

Possible targets are:

- a phase-space packing inequality combining spatial critical-shell transport with positive spectral transfer;
- a commutator estimate showing that the p=3 signed pairing cannot stay positive while the zero-energy pairing and finite-energy prelimit constraints hold;
- a recurrent spectral-flux theorem forcing vanishing of the high-frequency second moment along some sequence;
- an endpoint improvement for the solenoidal Lamb force.

No such closing theorem is proved in this note.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
