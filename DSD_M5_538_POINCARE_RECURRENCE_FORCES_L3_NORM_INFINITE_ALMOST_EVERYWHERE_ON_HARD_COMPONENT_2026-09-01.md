# DSD M5-538 — Poincare recurrence forces the L3 norm to be infinite almost everywhere on the nontrivial hard component

Date: 2026-09-01

Status: **EXACT L3 ENDPOINT FAILURE / M5-527 USES THE ALBRITTON--BARKER ANCIENT LIOUVILLE THEOREM TO EXCLUDE ANY NONTRIVIAL MILD ANCIENT SOLUTION WITH A BACKWARD SEQUENCE OF UNIFORMLY BOUNDED `L3` NORMS / IF THE NONTRIVIAL INVARIANT HARD COMPONENT GAVE POSITIVE MEASURE TO ANY FINITE `L3` SUBLEVEL SET, BACKWARD POINCARE RECURRENCE WOULD PRODUCE EXACTLY SUCH A FORBIDDEN SEQUENCE / THEREFORE `||U||_3=INFINITY` FOR INVARIANT-ALMOST EVERY HARD-CORE STATE / COMBINED WITH M5-537, A TYPICAL HARD STATE LIES IN EVERY `Lp`, `p>3`, BUT NOT IN `L3` / THE LOW-FREQUENCY OBSTRUCTION IS THUS AN EXACT LEBESGUE ENDPOINT DEFECT / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Extended L3 observable

On the invariant hard component

\[
(\widehat{\mathfrak H},\phi^\theta,\nu),
\]

define

\[
\boxed{
\mathcal L_3(Y)
:=
\|U_Y\|_{L^3(\mathbb R^3)}
\in[0,\infty].
}
\]

The value may be infinite because the current hard branch has only low-frequency endpoint failure; local smoothness and `Linfinity` boundedness do not imply global `L3` integrability.

---

## 2. Measurability

For `R<infinity`, define

\[
\mathcal L_{3,R}(Y)^3
:=
\int_{|y|<R}|U_Y|^3dy.
\]

The M5-508 global/local smooth topology makes each truncated observable continuous.

Moreover

\[
\mathcal L_{3,R}(Y)
\uparrow
\mathcal L_3(Y)
\qquad(R\to\infty).
\]

Hence `L_3` is a measurable extended observable.

---

## 3. External ancient Liouville theorem from M5-527

M5-527 imported the Albritton--Barker theorem:

if a mild ancient three-dimensional Navier--Stokes solution has a sequence

\[
s_n\to-\infty
\]

such that

\[
\sup_n\|v(s_n)\|_3<\infty,
\]

then

\[
\boxed{v\equiv0.}
\]

The hard component is nontrivial because it carries the marked first-hitting/ratchet/dual/production structure.

Therefore no typical nontrivial complete orbit may possess a bounded `L3` backward sequence.

---

## 4. Suppose finite L3 occurs on positive invariant measure

Assume

\[
\nu(\mathcal L_3<\infty)>0.
\]

Since

\[
\{\mathcal L_3<\infty\}
=
\bigcup_{K=1}^\infty
\{\mathcal L_3\le K\},
\]

there exists finite `K` such that

\[
\boxed{
\nu(B_K)>0,
\qquad
B_K:=\{Y:\|U_Y\|_3\le K\}.
}
\]

---

## 5. Backward recurrence creates the forbidden sequence

Fix `tau_0>0` and use the invertible measure-preserving map

\[
T=\phi^{-\tau_0}.
\]

Poincare recurrence gives, for `nu`-almost every `Y in B_K`, infinitely many integers

\[
n_j\to\infty
\]

with

\[
T^{n_j}Y
=
\phi^{-n_j\tau_0}Y
\in B_K.
\]

Hence

\[
\boxed{
\|U(\phi^{-n_j\tau_0}Y)\|_3
\le K
}
\]

along a sequence of similarity times tending to `-infinity`.

Under the inverse similarity map this is a backward-time sequence of the corresponding mild ancient solution.

The Albritton--Barker theorem then forces the solution to be zero, contradicting the nontrivial hard component.

---

## 6. Main conclusion

Therefore

\[
\boxed{
\nu(\mathcal L_3<\infty)=0.
}
\]

Equivalently,

\[
\boxed{
\|U_Y\|_3
=\infty
\quad
\text{for }\nu\text{-almost every }Y.
}
\]

Thus the current invariant hard measure lives entirely at the failure of strong `L3` integrability.

---

## 7. Combine with M5-537

M5-537 gives

\[
U_Y\in L^p
\qquad
\forall p>3
\]

for `nu`-almost every hard state.

M5-538 gives

\[
U_Y\notin L^3.
\]

Therefore

\[
\boxed{
U_Y
\in
\left(\bigcap_{p>3}L^p(\mathbb R^3)\right)
\setminus
L^3(\mathbb R^3)
\quad
\nu\text{-a.e.}
}
\]

This is an exact Lebesgue endpoint obstruction.

---

## 8. The divergence is necessarily low-amplitude / large-volume

The similarity velocity is uniformly bounded:

\[
\|U\|_\infty\le M_U.
\]

Hence

\[
\|U\|_3^3
=
3
\int_0^{M_U}
\lambda^2
\left|
\{|U|>\lambda\}
\right|d\lambda.
\]

Since the upper amplitude is finite, divergence of the `L3` integral cannot come from arbitrarily large pointwise velocity.

It is produced by the low-amplitude end

\[
\lambda\downarrow0,
\]

i.e. by sufficiently large spatial volume occupied by very small velocities.

This matches the vanishing-amplitude remote dust morphology of M5-533.

---

## 9. Relation to first radial moment

M5-531 proved

\[
\mathcal M_1
=
\infty
\quad\nu\text{-a.e.}
\]

and M5-526/529 gave the implication

\[
\mathcal M_1<\infty
\Longrightarrow
U\in L^3.
\]

M5-538 shows that both endpoint failures are in fact invariant-almost-everywhere properties of the same hard component:

\[
\boxed{
\mathcal M_1=\infty
\quad\text{and}\quad
\|U\|_3=\infty
\quad\nu\text{-a.e.}
}
\]

while all subcritical moments and all `Lp`, `p>3`, remain finite.

---

## 10. DSD interpretation

The surviving tail is no longer described merely as a possible `1/r`-type obstruction.

Its exact audited class is

\[
\boxed{
\text{strong-}L3\text{ fails everywhere in invariant measure},
}
\]

but any arbitrarily small positive displacement above the endpoint restores integrability:

\[
\boxed{
L^{3+\varepsilon}
\text{ is finite for every }\varepsilon>0.
}
\]

This is a much narrower functional endpoint.

---

## 11. Highest-value next target

The next natural question is whether the information

\[
U\in\bigcap_{p>3}L^p
\setminus L^3
\]

forces any Lorentz endpoint control.

It does not follow formally: one must distinguish

\[
L^{3,q},
\quad q<\infty,
\]

from

\[
L^{3,\infty}.
\]

A function-space audit should construct explicit low-amplitude radial witnesses showing which endpoint conclusions do and do not follow from the current `Lp`, `p>3`, package.

Only after that audit should the proof attempt import an endpoint Lorentz regularity theorem.

---

## 12. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
