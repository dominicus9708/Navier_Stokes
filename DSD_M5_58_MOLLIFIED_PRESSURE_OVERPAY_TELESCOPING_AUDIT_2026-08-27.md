# DSD M5-58 — Mollified Pressure-Overpay Telescoping Audit

Date: 2026-08-27

Status: **EXACT SIGNED-COCYCLE AUDIT / THE NATURAL FINITE-BAND PRESSURE OVERPAY `bar J_w - nu bar D_w` IS EXACTLY THE TIME DERIVATIVE OF THE BOUNDED RECURRENT MOLLIFIED ENTROPY / ITS LONG-TIME MEAN IS ZERO AND POSITIVE-DENSITY UPSTROKES MUST BE COMPENSATED BY DOWNSTROKES / THIS FIRST-ORDER SIGNED DEFECT CANNOT CLOSE GLOBAL REGULARITY / GLOBAL REGULARITY UNPROVED.**

## 1. Exact averaged ledger

M5-56 gives

\[
\boxed{
\partial_t\bar E_w
+
\nu\bar D_w
=
\bar J_w.
}
\]

Define the signed finite-band pressure overpay

\[
\boxed{
\mathcal X_w(t)
:=
\bar J_w(t)-\nu\bar D_w(t).
}
\]

Then identically

\[
\boxed{
\mathcal X_w(t)
=
\partial_t\bar E_w(t).
}
\]

Thus the most obvious signed candidate produced by M5-56 is an exact differential along the W1 orbit.

---

## 2. Boundedness on the compact recurrent orbit

The amplitude weight `w` has fixed compact support and the active set lies in the retained fixed W1 phase cell.

The compact W1 orbit therefore gives a uniform bound

\[
0\le\bar E_w(t)\le E_{w,max}<\infty.
\]

Consequently, for every `T>0`,

\[
\int_0^T\mathcal X_w(t)dt
=
\bar E_w(T)-\bar E_w(0).
\]

Hence

\[
\boxed{
\left|
\int_0^T\mathcal X_w(t)dt
\right|
\le
E_{w,max}.
}
\]

Dividing by `T` gives

\[
\boxed{
\frac1T
\int_0^T\mathcal X_w(t)dt
\longrightarrow0
}
\]

as `T -> infinity`.

This does not require periodicity. Boundedness alone suffices.

---

## 3. Consequence for the M5-57 positive-density upstrokes

M5-57 produced a syndetic family of intervals `I_n` of uniform positive width on which

\[
\partial_t\bar E_w
\ge c_1>0.
\]

Equivalently,

\[
\mathcal X_w
\ge c_1>0
\quad\text{on }I_n.
\]

After selecting a disjoint subfamily, the union of these intervals has positive lower density. Therefore the positive part satisfies a linear-in-time lower growth estimate

\[
\int_0^T(\mathcal X_w)_+dt
\ge c_+T-O(1)
\]

for some `c_+>0` along sufficiently large times.

But the signed integral of `X_w` stays uniformly bounded.

Therefore the negative part must compensate at the same linear order:

\[
\boxed{
\int_0^T(\mathcal X_w)_-dt
\ge c_+T-O(1).
}
\]

Thus recurrent positive pump overpay necessarily comes with recurrent pressure-underpay/downstroke elsewhere on the orbit.

The compensation is not optional; it follows from exact telescoping.

---

## 4. Mean pressure/dissipation equality

From

\[
\bar J_w
=
\nu\bar D_w+\partial_t\bar E_w
\]

and the vanishing long-time average of the derivative, every existing long-time average satisfies

\[
\boxed{
\overline{\bar J_w}
=
\nu\overline{\bar D_w}.
}
\]

More generally, for invariant probability measures on the compact recurrent set, stationarity gives

\[
\int \partial_t\bar E_w\,d\mu=0,
\]

so

\[
\boxed{
\int\bar J_w\,d\mu
=
\nu\int\bar D_w\,d\mu.
}
\]

Hence a positive mean pressure payer is entirely compatible with recurrence: pressure work replenishes the viscous loss on average.

This is a balance law, not a contradiction.

---

## 5. Why the strict M5-56 band margin does not defeat telescoping

At an upward crossing M5-56 gives the finite-band pressure-square requirement

\[
\bar S_w
\ge
\nu^2\bar D_w+
u^2\bar A_w.
\]

This is stronger than a one-level statement and is supported on a nonzero amplitude band.

However `bar S_w` is nonnegative. It is a required resource, not a signed derivative.

The compact recurrent orbit may revisit states carrying the same order-one value of `bar S_w` indefinitely without consuming a finite conserved budget.

Thus the two natural quantities play different roles:

\[
\boxed{
\begin{array}{rcl}
\bar S_w
&=&\text{finite positive pressure resource, but no finite cumulative budget},\\
\mathcal X_w
&=&\text{signed quantity, but exact derivative and hence telescoping}.
\end{array}
}
\]

Neither property alone closes the survivor.

---

## 6. Closed branch

The following proposed contradiction is invalid:

\[
\text{syndetically many strict upward crossings}
\Rightarrow
\int_0^T
(\bar J_w-\nu\bar D_w)dt
\to+\infty.
\]

The exact identity instead gives

\[
\int_0^T
(\bar J_w-\nu\bar D_w)dt
=
\bar E_w(T)-\bar E_w(0),
\]

which is uniformly bounded.

Therefore the **first-order mollified entropy-overpay route is closed as a monotonicity argument**.

This is a DSD pruning result, not a failure of M5-56: M5-56 remains useful because it identifies the finite-band local pressure structure that any survivor must reproduce.

---

## 7. What a genuinely new signed defect must satisfy

A closing cocycle cannot be an exact time derivative of a bounded state function on the compact recurrent orbit.

It must have at least one of the following properties:

1. a non-exact circulation around recurrent pump loops;
2. a one-sided sign forced by pressure-Poisson/Hodge geometry, preventing compensating downstrokes;
3. a scale-to-scale defect that telescopes in the physical radius direction with a nonzero terminal sign;
4. or a finite global resource whose decrement is fixed on every syndetic return.

M5-49 already ruled out ordinary energy/dissipation as the fourth type.

M5-58 rules out the simplest averaged threshold entropy as the first/second type.

---

## 8. New narrowed target

The remaining pressure branch is no longer

\[
\text{find a positive pressure cost}
\]

or

\[
\text{find a signed first derivative of threshold entropy}.
\]

It is

\[
\boxed{
\text{find a non-exact pressure/Hodge loop defect on the recurrent finite-band pump segment}
}
\]

or prove that no such loop can be supported by the local pressure-Poisson geometry of the core plus finitely many adjacent logarithmic shells.

This target is strictly narrower than M5-54 because the amplitude-thickness and recurrence-persistence issues have now been resolved and audited.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
