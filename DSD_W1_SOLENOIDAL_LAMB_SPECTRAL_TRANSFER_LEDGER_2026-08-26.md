# DSD W1 Solenoidal-Lamb Spectral Transfer Ledger — Audit Correction

Date: 2026-08-26

Status: **AUDIT-CORRECTED / GLOBAL W1 ZERO-L2-WORK AND WHOLE-SPACE FOURIER TRANSFER CLAIMS WITHDRAWN / EXACT ZERO NONLINEAR ENERGY WORK RETAINED ON EACH FINITE-ENERGY PRELIMIT AND ON GENUINE L2 QUOTIENTS / POSITIVE ENSTROPHY-WEIGHTED LAMB PAIRING RETAINED WHERE THE W1 DERIVATIVE INTEGRALS ARE FINITE / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose of the correction

The solenoidal Lamb field is

\[
L_s:=\mathbb P(\Omega\times U).
\]

A previous version of this note wrote the whole-space W1 identity

\[
\int_{\mathbb R^3}U\cdot L_s=0
\]

and then introduced a whole-space Fourier transfer density for the invariant W1 state.

That step is not justified at the endpoint currently under study.

A critical W1 tail may satisfy

\[
U(Y)\sim |Y|^{-1},
\]

and therefore

\[
\int_{|Y|>R}|U|^2dY
\sim
\int_R^\infty dr
=\infty.
\]

Thus the invariant W1 limit need not belong to `L2(R3)`.  The standard whole-space L2 self-adjoint pairing with the Helmholtz projector and the corresponding Parseval/Fourier transfer identity cannot be invoked without an additional finite-energy subtraction or cutoff argument.

This is a substantive audit correction, not merely a technical wording change.

---

## 2. What remains exactly true on the physical prelimit

For every physical time `t<T_*`, the smooth finite-energy Navier--Stokes prelimit satisfies

\[
u(\cdot,t)\in L^2(\mathbb R^3).
\]

Write

\[
\omega=\nabla\times u,
\qquad
\ell_s:=\mathbb P(\omega\times u).
\]

Then the standard nonlinear kinetic-energy cancellation is legitimate:

\[
\int u\cdot \ell_s
=
\int \mathbb P u\cdot(\omega\times u)
=0.
\]

Hence

\[
\boxed{
\int_{\mathbb R^3}u\cdot\mathbb P(\omega\times u)\,dx=0
\qquad (t<T_*).
}
\]

Equivalently, each finite Leray-time prelimit profile has finite normalized L2 norm and the same cancellation before the limiting escape of normalized energy to similarity infinity is taken.

The obstruction is therefore a **noncommutation of the limits**

\[
s\to\infty
\qquad\text{and}\qquad
R\to\infty,
\]

not a failure of the physical nonlinear energy cancellation.

---

## 3. Localized W1 pairing is a projection-cutoff commutator

Let `chi_R` be a smooth radial cutoff.  Since `U` is divergence-free,

\[
\int \chi_R U\cdot L_s
=
\langle \mathbb P(\chi_RU),\Omega\times U\rangle.
\]

Because

\[
\mathbb P(\chi_RU)
=
\chi_RU+[
\mathbb P,\chi_R
]U
\]

and

\[
U\cdot(\Omega\times U)=0
\]

pointwise,

\[
\boxed{
\int \chi_R U\cdot L_s
=
\left\langle
[
\mathbb P,\chi_R
]U,
\Omega\times U
\right\rangle.
}
\]

Thus the failure of global normalized zero work is entirely an **interface/projection defect** at similarity infinity.

No decay rate for this cutoff commutator is asserted here without an independent estimate.

This is the correct W1 replacement for the invalid whole-space L2 pairing.

---

## 4. Positive enstrophy-weighted Lamb pairing survives

The vorticity identity uses derivative quantities that are integrable on the critical `1/r` tail under the current W1 derivative bounds.

Let

\[
Z:=\|\Omega\|_2^2,
\qquad
P_\Omega:=\|\nabla\Omega\|_2^2,
\qquad
Q:=\int\Omega\cdot S\Omega.
\]

Using

\[
\nabla\times\Omega=-\Delta U
\]

and curl integration by parts in the admissible derivative class gives

\[
\boxed{
Q
=
\int \Delta U\cdot L_s\,dY.
}
\]

The invariant W1 enstrophy identity yields

\[
\boxed{
\langle Q\rangle_\mu
=
\frac14\langle Z\rangle_\mu
+\nu\langle P_\Omega\rangle_\mu
>0.
}
\]

Therefore the positive high-derivative nonlinear pairing remains a valid endpoint requirement.

---

## 5. Whole-space Fourier transfer is not an invariant-W1 theorem

The previous whole-space definition

\[
T(k,s)
=-\operatorname{Re}
(\widehat U\cdot\overline{\widehat{L_s}})
\]

was useful heuristically, but it is not a justified invariant-W1 object when `U` is not in L2.

Accordingly the claims

\[
\int T=0,
\qquad
\int |k|^2T>0
\]

are withdrawn as whole-space W1 identities.

They remain legitimate in either of two settings:

1. each finite-energy physical/Leray prelimit before taking `s->infinity`;
2. a genuinely L2 remainder/quotient, such as the divergence-free periodic quotient constructed after subtracting the canonical DSS tail, provided all forcing/background terms are retained.

In the second setting the quotient is forced, so the transfer ledger must include the background and forcing terms.  It cannot be imported as an unforced W1 contradiction.

---

## 6. DSD interpretation after the correction

The correct structural statement is now

\[
\boxed{
\text{physical prelimit nonlinear work}=0
}
\]

but the invariant normalized endpoint may retain

\[
\boxed{
\text{positive critical p=3 projection work}
+
\text{positive enstrophy-weighted Lamb work}
}
\]

because normalized L2 energy can escape to similarity infinity before the W1 limit is formed.

Hence the missing bridge is not simply `cascade nonrepeatability`.  It is more precisely

\[
\boxed{
\text{finite-energy prelimit cancellation}
\Longrightarrow
\text{control of the similarity-infinity projection/interface defect}.
}
\]

This places the endpoint back on the same interface/injection frontier previously found in the periodic tail analysis.

---

## 7. Corrected endpoint search

A closing theorem may take one of the following forms:

- show that the cutoff projection defect
  \[
  \langle [\mathbb P,\chi_R]U,\Omega\times U\rangle
  \]
  vanishes sufficiently fast as `R->infinity` on every W1 state;
- prove that any nonvanishing limit of that defect forces a quantified critical shell export/turnover event incompatible with the finite physical prelimit budget;
- in the periodic branch, use the canonical-tail subtraction to turn the defect into the forcing/interface term of the finite-energy quotient and prove a forced-Liouville/backward-uniqueness theorem;
- in the aperiodic branch, construct an analogous canonical/statistical tail object before making any global L2 transfer claim.

No one of these is yet proved.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
