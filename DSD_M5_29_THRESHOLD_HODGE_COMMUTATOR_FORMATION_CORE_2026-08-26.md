# DSD M5-29 — Threshold--Hodge Commutator as the Formation Core

Date: 2026-08-26

Status: **EXACT COMPRESSION OF M5-23--28 / PRESSURE WORK, GRADIENT-HODGE WORK AND SOLENOIDAL LAMB TRANSFER ARE ALL THE SAME THRESHOLD--HODGE COMMUTATOR ACTION / HELICAL POLARIZATION IS A GEOMETRIC REALIZATION CHANNEL, NOT AN INDEPENDENT SOURCE / GLOBAL REGULARITY UNPROVED.**

## 1. Definitions

On the normalized first-hit cell let

\[
a=|V|,
\qquad
f(a)=(1-a^{-1})_+,
\]

\[
W=f(a)V,
\qquad
Z=\mathbb PW.
\]

Let the Lamb field be

\[
L:=\Omega\times V.
\]

Its solenoidal projection is

\[
L_s:=\mathbb PL.
\]

M5-28 identifies the high-amplitude formation work as

\[
\boxed{
T_{form}
:=-\langle L_s,Z\rangle
=
\mathcal G'+\nu\mathcal D_{exc}.
}
\]

At a first fixed positive hitting,

\[
T_{form}\ge c_{form}>0.
\]

## 2. Pointwise Lamb orthogonality

The unprojected Lamb field is pointwise orthogonal to the velocity:

\[
L\cdot V
=(\Omega\times V)\cdot V
=0.
\]

Since `W=f(a)V` is parallel to `V`,

\[
\boxed{
L\cdot W=0
}
\]

pointwise.

Thus the positive formation work cannot come from an ordinary pointwise Lamb--velocity alignment.

It is created only after the Hodge projection is inserted.

## 3. Exact commutator representation

Because `V` is divergence free,

\[
\mathbb PV=V.
\]

Therefore

\[
[\mathbb P,f]V
=
\mathbb P(fV)-f\mathbb PV
=Z-W.
\]

But

\[
Z-W=-\mathbb QW.
\]

Hence

\[
\boxed{
[\mathbb P,f]V
=-\mathbb QW.
}
\]

Now

\[
\langle L_s,Z\rangle
=
\langle \mathbb PL,Z\rangle
=
\langle L,Z\rangle
\]

because `Z` is divergence free.

Using

\[
Z=fV+[\mathbb P,f]V
\]

and the pointwise orthogonality `L·fV=0`,

\[
\langle L_s,Z\rangle
=
\langle L,[\mathbb P,f]V\rangle.
\]

Therefore

\[
\boxed{
T_{form}
=-\langle L,[\mathbb P,f]V\rangle.
}
\]

This is the exact threshold--Hodge commutator form of the first-hit formation action.

## 4. Gradient-Hodge representation

Since

\[
[\mathbb P,f]V=-\mathbb QW,
\]

we also have

\[
T_{form}
=\langle L,\mathbb QW\rangle.
\]

Because `mathbb QW` is a gradient field, only the gradient projection of `L` contributes:

\[
\boxed{
T_{form}
=\langle\mathbb QL,\mathbb QW\rangle.
}
\]

Thus the same scalar work is an exact pairing of the two gradient Hodge components.

## 5. Bernoulli/pressure representation

For physical/rescaled Navier--Stokes,

\[
(V\cdot\nabla)V
=L+\nabla(a^2/2).
\]

Applying `mathbb Q` to the projected momentum equation gives

\[
\mathbb QL
=-\nabla\left(
\Pi+\frac{a^2}{2}
\right).
\]

Define the Bernoulli function

\[
B:=\Pi+a^2/2.
\]

Then

\[
T_{form}
=-\langle\nabla B,\mathbb QW\rangle
=
\int B\,\operatorname{div}W.
\]

The kinetic term vanishes after integration:

\[
\int \frac{a^2}{2}\operatorname{div}W
=-\int \nabla(a^2/2)\cdot W
=0,
\]

because `W` is parallel to `V` and the resulting expression is a divergence along the incompressible transport field.

Hence

\[
\boxed{
T_{form}
=
\int\Pi\,\operatorname{div}W.
}
\]

This recovers exactly the pressure source in M5-23.

## 6. Solenoidal-Lamb representation

M5-28 already gives

\[
\boxed{
T_{form}
=-\langle
\mathbb P(\Omega\times V),
\mathbb PW
\rangle.
}
\]

Combining Sections 3--5,

\[
\boxed{
\begin{aligned}
T_{form}
&=-\langle L,[\mathbb P,f]V\rangle\\
&=\langle\mathbb QL,\mathbb QW\rangle\\
&=\int\Pi\,\operatorname{div}W\\
&=-\langle\mathbb PL,\mathbb PW\rangle.
\end{aligned}
}
\]

All four expressions are one scalar formation action.

## 7. DSD reduction

The current endpoint can therefore be typed as

\[
\boxed{
\text{high-amplitude threshold formation}
=
\text{failure of }f(|V|)
\text{ to commute with the Hodge projection}
\text{ in the presence of Lamb geometry}.
}
\]

The pressure picture and the solenoidal-transfer picture are complementary projections of this noncommutation.

This means that the following must **not** be counted as independent payers:

- pressure-amplitude work;
- Hodge-gradient work;
- projected Lamb work;
- the first-hit `P` and `Q` formation action.

They encode the same formation scalar.

## 8. Role of helicity after this compression

M5-27 splits the mandatory solenoidal component into

\[
\text{two-helicity mixed}
\quad\lor\quad
\text{nearly homochiral / direction-twist}.
\]

M5-29 clarifies that this polarization split concerns **how the solenoidal side realizes the commutator work**, not where the work comes from.

Therefore helicity is a secondary geometry of the formation cell unless it yields an estimate that constrains

\[
\langle L,[\mathbb P,f]V\rangle
\]

directly.

## 9. Critical commutator floor

At the fixed positive first hit,

\[
T_{form}
\ge c_{form}>0.
\]

Thus

\[
\boxed{
-\langle
\Omega\times V,
[\mathbb P,(1-|V|^{-1})_+]V
\rangle
\ge c_{form}>0.
}
\]

This is a compact single-line necessary condition for every large-threshold W1 formation event.

It is scale invariant in the normalized phase cell.

## 10. What would close M5 from here

A successful endpoint estimate could now take one of the following direct forms:

1. **commutator absorption**
   \[
   |\langle L,[\mathbb P,f]V\rangle|
   \le
   \theta\nu\mathcal D_{exc},
   \qquad \theta<1;
   \]
2. **commutator compactness decay** across large physical thresholds;
3. **geometric cancellation** showing that the mixed/helical or twist branches force the commutator pairing to vanish or lose a fixed factor;
4. **critical integrability** proving that fixed commutator events cannot occur at infinitely many nested thresholds.

None is proved here.

Thus M5 remains open, but its W1-specific dynamic source has been compressed to one exact threshold--Hodge commutator.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
