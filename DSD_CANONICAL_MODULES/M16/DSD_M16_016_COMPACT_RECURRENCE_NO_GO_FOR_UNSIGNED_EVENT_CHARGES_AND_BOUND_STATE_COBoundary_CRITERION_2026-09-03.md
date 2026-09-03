# DSD M16-016 — Compact-recurrence no-go for unsigned event charges and the bounded-state coboundary criterion

Date: 2026-09-03
Canonical ID: **M16-016**

Status: **INTERNAL STRUCTURAL AUDIT / A POSITIVE-DENSITY NONNEGATIVE EVENT CHARGE IS COMPATIBLE WITH COMPACT RECURRENCE. TO PRODUCE A CONTRADICTION IT MUST BE IDENTIFIED WITH, OR DOMINATE, THE DERIVATIVE OF A BOUNDED STATE RESOURCE OR A FINITE RESOURCE THAT CANNOT BE REPLENISHED ON THE SAME INVARIANT COMPONENT. THIS FORMALIZES THE REQUIRED CLOSURE TYPE FOR M16-015. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Compact invariant component

Let `X` denote the globally smooth compact CE-H hull retained after the previous compactness reductions, and let

\[
\Phi_t:X\to X
\]

be the similarity-time flow.

Let `mu` be an invariant probability measure on an ergodic component:

\[
(\Phi_t)_\#\mu=\mu.
\]

Suppose a coherent event family is represented by a continuous nonnegative state observable

\[
a:X\to[0,\infty)
\]

with

\[
\boxed{
\int_X a\,d\mu=\bar a>0.
}
\]

This is the abstract form of a positive-density P1/P4/P5-type occupancy after time thickening.

---

## 2. Positive additive path charge is not itself a contradiction

Define

\[
A_T(x)
:=
\int_0^T a(\Phi_t x)\,dt.
\]

By the ergodic theorem, for `mu`-almost every `x`,

\[
\boxed{
\frac{A_T(x)}{T}\to\bar a>0.
}
\]

Therefore

\[
A_T(x)\sim \bar a T.
\]

But `A_T` is a **path functional**, not a bounded state observable on `X`.

Its unbounded growth is completely compatible with recurrent motion of the state itself.

A periodic orbit gives the simplest model: the state returns exactly, while the time integral of a positive function increases by the same amount every period.

Thus

\[
\boxed{
\text{positive event count / positive integrated charge}
\not\Rightarrow
\text{failure of recurrence}.
}
\]

---

## 3. Bounded-state derivative has zero invariant mean

Let

\[
F:X\to\mathbb R
\]

be a bounded continuously differentiable observable along the flow, and write its generator derivative as

\[
\mathcal LF(x)
:=
\left.\frac d{dt}F(\Phi_t x)\right|_{t=0}.
\]

Invariance gives, for every `t`,

\[
\int_X F(\Phi_t x)d\mu(x)
=
\int_X F(x)d\mu(x).
\]

Differentiate at `t=0`:

\[
\boxed{
\int_X \mathcal LF\,d\mu=0.
}
\]

This is the continuous-time bounded-coboundary identity.

The discrete return-map analogue is

\[
\boxed{
\int_X(F\circ T-F)d\mu=0.
}
\]

---

## 4. Strict bounded-state payer would immediately contradict recurrence

Assume one could prove

\[
\mathcal LF\ge a
\]

with `a>=0` and

\[
\int a\,d\mu>0.
\]

Then

\[
0
=
\int \mathcal LF\,d\mu
\ge
\int a\,d\mu
>0,
\]

which is impossible.

More generally, if

\[
\mathcal LF
=
a-r,
\qquad a,r\ge0,
\]

then invariance forces

\[
\boxed{
\langle a\rangle=\langle r\rangle.
}
\]

Hence a dissipative event charge only becomes contradictory if the compensating recharge `r` is absent, quantitatively too small, or must consume a separately finite resource.

---

## 5. Interpretation for M16-015

For the derivative occupancy class

\[
\mathcal P_{der}=P_1\lor P_4\lor P_5,
\]

M16-015 currently gives only a positive-density nonnegative event charge.

Therefore the following strategy is invalid:

\[
\text{event repeats infinitely often}
\Rightarrow
\text{contradiction}.
\]

To close this branch one must instead construct one of the following.

### Type I — bounded strict state resource

A bounded `F` with

\[
\mathcal LF\ge c\,a
\]

or the opposite sign, on the retained component.

### Type II — finite resource with audited recharge

A resource `R>=0` satisfying

\[
R'\le-c\,a+r,
\]

where the total available recharge can be bounded independently of the number of recurrent events.

### Type III — signed material exit

An exact signed flux showing that each event removes a definite amount of a finite label/flux resource from the component.

These are structurally different from an unsigned occupancy estimate.

---

## 6. Connection to the M13--M15 genealogy program

M13--M15 already identified the natural finite-resource candidates:

- transverse vorticity flux;
- finite persistent material/vorticity lineages;
- fixed-threshold amplitude current;
- negative-`kappa` sheath replacement;
- critical-sheet crossing / turnover.

Therefore the correct use of the M16 payer floor is not to create a new event counter. It is to show that one payer must enter one of those **signed or finite-resource ledgers**.

This is the precise remaining closure task.

---

## 7. No-go for a naive bounded monotone state counter

Suppose one attempts to define a bounded continuous state counter `N(x)` on the compact hull which increases by at least `eta>0` at every payer event and never decreases.

After smoothing the event indicator, this would yield an observable `a>=0` of positive invariant mean and

\[
\mathcal LN\ge a.
\]

Section 4 shows that this is impossible on an invariant compact component.

Therefore either

1. the counter is genuinely path-dependent / lifted and unbounded;
2. the state exits the component;
3. there is an opposing reset/recharge event;
4. or the claimed monotonicity is false.

This explains the repeated cancellation failures of angle, flux, and finite-memory counters in earlier modules.

---

## 8. Updated proof-design criterion

The next calculation must preserve sign.

For an amplitude threshold `rho=a`, the natural quantity is not

\[
|\nabla\rho|
\]

but the material normal crossing speed

\[
\frac{D_B\rho}{|\nabla\rho|}.
\]

Likewise a strain packet must be tied to an actual production or compression current rather than `|grad sigma|` alone.

Thus the immediate next target is the exact CE-H material amplitude law and its induced signed threshold crossing relation.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
