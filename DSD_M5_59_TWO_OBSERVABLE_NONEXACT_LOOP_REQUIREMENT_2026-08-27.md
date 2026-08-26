# DSD M5-59 — Two-Observable Non-Exact Loop Requirement

Date: 2026-08-27

Status: **EXACT DIFFERENTIAL-FORM AUDIT / EVERY SIGNED DEFECT OBTAINED BY REWEIGHTING THE M5-58 OVERPAY WITH A FUNCTION OF THE SAME MOLLIFIED ENTROPY REMAINS AN EXACT DIFFERENTIAL / A GENUINELY NON-EXACT RECURRENT LOOP REQUIRES AT LEAST ONE ADDITIONAL INDEPENDENT STATE OBSERVABLE / NATURAL TWO-OBSERVABLE LOOP INTEGRALS ARE AVAILABLE BUT NO ORIENTATION/SIGN THEOREM IS YET DERIVED / GLOBAL REGULARITY UNPROVED.**

## 1. The M5-58 exact one-form

Let

\[
E(t):=\bar E_w(t),
\qquad
X(t):=\bar J_w(t)-\nu\bar D_w(t).
\]

M5-58 gives exactly

\[
\boxed{X(t)=\dot E(t).}
\]

Thus the basic signed pressure overpay is the pullback of the exact one-form

\[
dE
\]

along the recurrent W1 orbit.

---

## 2. Scalar reweighting cannot repair exactness

A natural attempt is to weight the signed overpay according to the current entropy level. Let

\[
f\in C^1(\mathbb R).
\]

Then

\[
f(E)X
=f(E)\dot E.
\]

Choose an antiderivative `F` satisfying

\[
F'(s)=f(s).
\]

Then

\[
\boxed{
f(E(t))X(t)
=\frac d{dt}F(E(t)).
}
\]

Consequently

\[
\boxed{
\int_0^T f(E(t))X(t)dt
=F(E(T))-F(E(0)).
}
\]

On the compact recurrent orbit this is uniformly bounded whenever `F(E)` is bounded on the range of `E`.

Therefore no scalar weighting depending only on the same mollified entropy can create a non-telescoping defect.

---

## 3. More generally, one scalar state coordinate is insufficient

Any one-form on a one-dimensional state coordinate has the form

\[
\omega=f(E)dE.
\]

It is locally and globally exact on an interval of entropy values:

\[
\omega=dF(E).
\]

Hence a proof search restricted to

\[
E,\quad \dot E,\quad f(E)\dot E
\]

cannot distinguish a recurrent upstroke/downstroke loop from a reversible traversal in the same scalar coordinate.

The scalar entropy coordinate records position along the vertical axis but loses the branch/history information required for hysteresis.

This is a DSD describability limitation of the one-coordinate projection, not a Navier--Stokes contradiction.

---

## 4. Introduce a second independent observable

Let

\[
Y(t)=\mathcal Y(U(t))
\]

be a second state observable that is not a function of `E` alone.

Natural candidates already present in the M5 chain include

\[
Y=\bar S_w
=\int |U|w(|U|)|P|^2dy,
\]

\[
Y=\bar D_w,
\]

or a local Hodge/formation-action observable on the finite-band pump cell.

Then the line integral

\[
\boxed{
\mathcal C_Y[T_0,T_1]
:=
\int_{T_0}^{T_1}Y(t)\dot E(t)dt
=
\int_{\gamma}Y\,dE
}
\]

need not be exact on the two-dimensional projected state plane `(E,Y)`.

---

## 5. Closed-loop interpretation

Suppose a recurrent segment returns exactly to the same projected state:

\[
(E(T_1),Y(T_1))=(E(T_0),Y(T_0)).
\]

Then

\[
\oint Y\,dE
\]

is the circulation of the one-form `Y dE` around the projected loop.

By integration by parts,

\[
\int_{T_0}^{T_1}Y\dot E\,dt
=
[YE]_{T_0}^{T_1}
-
\int_{T_0}^{T_1}E\dot Y\,dt.
\]

For a closed loop the endpoint term vanishes, hence

\[
\boxed{
\oint Y\,dE
=-\oint E\,dY.
}
\]

For a simple oriented loop in the `(E,Y)` plane this circulation is, up to orientation convention, the enclosed signed area.

Thus a nonzero value measures a genuine phase lag/hysteresis between the threshold entropy and the second observable.

---

## 6. Why `Y >= 0` does not determine the loop sign

The natural pressure payer satisfies

\[
\bar S_w\ge0,
\]

and the averaged dissipation satisfies

\[
\bar D_w\ge0.
\]

However positivity of `Y` alone does not determine

\[
\oint Y\,dE.
\]

The sign depends on whether `Y` is systematically larger on the upstroke or on the downstroke at the same entropy value.

Schematically, if two branches can be represented as

\[
Y_{up}(E),
\qquad
Y_{down}(E),
\]

then

\[
\boxed{
\oint Y\,dE
=
\int_{E_{min}}^{E_{max}}
\bigl(Y_{up}(E)-Y_{down}(E)\bigr)dE
}
\]

with the sign set by the branch ordering.

None of M5-37 through M5-58 has yet proved a uniform ordering

\[
Y_{up}(E)>Y_{down}(E)
\]

or the opposite.

---

## 7. Pressure-Poisson relation is instantaneous, not an orientation theorem

The pressure is determined instantaneously by

\[
-\Delta P
=\partial_i\partial_j(U_iU_j)
\]

up to the usual normalization.

This elliptic relation constrains which pairs `(U,P)` are admissible at one state.

By itself it does not assign a temporal orientation to a recurrent loop in state space.

Therefore the inference

\[
\text{pressure is nonlocal/elliptic}
\Rightarrow
\text{one fixed sign of }\oint \bar S_w\,d\bar E_w
\]

is not justified.

A sign theorem would need an additional dynamical or geometric asymmetry, for example a Hodge formation quantity that distinguishes creation from relaxation at the same entropy level.

---

## 8. DSD audit

### GREEN

All defects of the form

\[
f(\bar E_w)(\bar J_w-\nu\bar D_w)
\]

are exact derivatives and telescope.

### GREEN

A second independent observable permits genuinely non-exact projected loop integrals such as

\[
\oint \bar S_w\,d\bar E_w.
\]

### RED

Nonnegativity of pressure cost or dissipation does not supply the orientation/sign of this loop.

### YELLOW

A Hodge/formation observable could, in principle, separate the pump upstroke from the compensating downstroke. No such branch-ordering theorem has yet been proved.

---

## 9. Immediate consequence

The pressure branch is sharpened from

\[
\text{find a non-exact defect}
\]

to

\[
\boxed{
\text{find a second independent state observable and prove a one-sided hysteresis/orientation inequality on recurrent pump loops.}
}
\]

Before investing in such an observable, however, one more audit is required: even a sign-definite non-exact loop circulation may accumulate indefinitely on a compact recurrent dynamical system without contradicting recurrence.

That budget question is M5-60.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
