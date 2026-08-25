# DSD W1 Descendant as a Vanishing-Time Navier--Stokes Step

Date: 2026-08-26

Status: **CO-MOVING W1 EQUATION EXACTLY REPARAMETRIZED AS ORDINARY UNFORCED NAVIER--STOKES ON A TIME INTERVAL OF LENGTH R^-2 / CANONICAL DESCENDANT IDENTIFIED AS THE R^-2 NS SEMIGROUP STEP OF THE SHELL BLOW-DOWN / REMOTE FREEZING GIVEN A PRECISE DIFFUSIVE-TIME INTERPRETATION / GLOBAL REGULARITY UNPROVED.**

## 1. Co-moving equation

For a W1 state `V`, define

\[
W_R(z,h)
=
Re^{h/2}
(S(h)V)(Re^{h/2}z).
\]

The exact equation is

\[
\boxed{
\partial_hW_R
=
R^{-2}e^{-h}
\mathcal N(W_R),
}
\]

where

\[
\boxed{
\mathcal N(W)
:=
\nu\Delta W
-
\mathbb P\nabla\cdot(W\otimes W).
}
\]

All similarity drift has already been removed by the co-moving rescaling.

---

## 2. Slow-time reparametrization

Define

\[
\boxed{
\tau
:=
R^{-2}(1-e^{-h}).
}
\]

Then

\[
\frac{d\tau}{dh}
=
R^{-2}e^{-h}.
\]

Therefore

\[
\boxed{
\partial_\tau W_R
=
\nu\Delta W_R
-
\mathbb P\nabla\cdot(W_R\otimes W_R).
}
\]

This is precisely the standard projected, unforced incompressible Navier--Stokes equation in the fixed `z` variable.

No approximation has been made.

---

## 3. The infinite Leray-age interval is a finite NS-time interval

As

\[
h:0\to\infty,
\]

we have

\[
\tau:0\to R^{-2}.
\]

Hence the entire infinite future of one co-moving W1 shell corresponds to only

\[
\boxed{\Delta\tau=R^{-2}}
\]

units of ordinary shell-scale Navier--Stokes time.

Let `S_NS(tau)` denote the ordinary unforced Navier--Stokes evolution in the rescaled coordinates, on the smooth W1 shell class.

Then

\[
W_R(\tau)
=
S_{NS}(\tau)\,[\mathcal F_R[V]],
\]

where

\[
\mathcal F_R[V](z)=RV(Rz).
\]

Taking `h->infinity`, equivalently `tau->R^-2`, gives

\[
\boxed{
C_R[V]
=
S_{NS}(R^{-2})\,[\mathcal F_R[V]].
}
\]

Thus the canonical descendant is an ordinary NS time step of length exactly `R^-2`.

---

## 4. Exact Duhamel form

Without assuming any Taylor expansion,

\[
\boxed{
C_R[V]-\mathcal F_R[V]
=
\int_0^{R^{-2}}
\mathcal N(W_R(\tau))d\tau.
}
\]

Equivalently in the original co-moving age,

\[
C_R[V]-\mathcal F_R[V]
=
R^{-2}
\int_0^\infty
 e^{-h}\mathcal N(W_R(h))dh.
\]

The previously obtained `O(R^-2)` H^-1 defect is therefore the natural first-order time-step size.

---

## 5. Diffusive-time interpretation

A normalized shell at radius `R` corresponds to a physical radius

\[
r=\lambda R,
\qquad
\lambda=\sqrt{T_*-t}.
\]

The remaining physical time to the candidate singular time is

\[
T_*-t=\lambda^2.
\]

The shell's diffusive time scale is

\[
r^2=\lambda^2R^2.
\]

Their ratio is

\[
\boxed{
\frac{T_*-t}{r^2}
=
R^{-2}.
}
\]

Thus the mathematical slow time `R^-2` has an exact physical interpretation:

\[
\boxed{
\text{remaining time before }T_*
\ /
\text{local diffusive time of the shell}.
}
\]

For `R->infinity` this ratio tends to zero.

The remote shell freezes because it has vanishingly little local NS evolution time left before the singular time.

---

## 6. Consequence for tail self-dynamics

The far tail cannot use its own local nonlinear/viscous evolution to create order-one changes after it has entered a very large normalized radius.

Its entire remaining local NS evolution is only an `R^-2` time step.

Therefore

\[
\boxed{
\text{order-one far radial variation}
\neq
\text{order-one future self-dynamics of one remote shell}.
}
\]

Such variation must already be present in the ancestral data carried into successive shell radii.

This is exactly the backward-time genealogy interpretation.

---

## 7. First-correction interpretation

If, in an additional topology, the ordinary NS generator is sufficiently continuous along the shell family, the Duhamel formula suggests

\[
C_R[V]
=
\mathcal F_R[V]
+R^{-2}\mathcal N(C_R[V])
+o(R^{-2}),
\]

or equivalently

\[
\mathcal F_R[V]
=
C_R[V]
-R^{-2}\mathcal N(C_R[V])
+o(R^{-2}).
\]

This is the rigorous structural origin of the previously observed nonresonant `R^-2` correction.

Because uniform H2 control is not available on the full W1 branch, this strong Taylor expansion is **not** asserted as a proved H^-1 estimate here.

The exact Duhamel representation, however, is sufficient for the descendant construction.

---

## 8. Relation to the scale-infinity interface

At a fixed physical radius, `R` grows like `e^(s/2)`. Therefore

\[
R^{-2}
\asymp
 e^{-s}
\asymp
 T_*-t.
\]

So the tail correction to its frozen physical trace naturally occurs at first order in the remaining physical time, at least in weak topologies.

This explains why a nonzero static-tail residual can be balanced by a terminal-zero correction without contradiction: the available correction scale is exactly the remaining time.

A proof still needs a topology strong enough to turn this structural statement into a backward-uniqueness or forcing-rigidity theorem.

---

## 9. DSD audit consequence

The tail has three distinct layers:

1. **genealogical state:** which ancestor shell was inserted;
2. **passive similarity transport:** moves that shell outward in normalized radius without changing physical radius;
3. **remaining local NS evolution:** only an `R^-2` ordinary time step.

The third layer is summably small at large radius.

Thus future calculations should focus on the genealogy/interface and not repeatedly search for an order-one remote tail self-interaction.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
