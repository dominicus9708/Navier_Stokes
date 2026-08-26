# DSD M5-62 — Canonical Squared-Overpay Loop Action

Date: 2026-08-27

Status: **DERIVED SIGN-DEFINITE NON-EXACT LOOP ACTION / CHOOSING THE SECOND OBSERVABLE TO BE THE MOLLIFIED ENTROPY VELOCITY ITSELF TURNS THE M5-59 LOOP CIRCULATION INTO THE POSITIVE ACTION `int X_w^2 dt` / ROBUST SYNDETIC PUMP RETURNS CARRY A UNIFORM POSITIVE ACTION LOWER BOUND / THE ORIENTATION PROBLEM IS SOLVED BUT THE INDEPENDENT FINITE-BUDGET PROBLEM FROM M5-60 REMAINS / GLOBAL REGULARITY UNPROVED.**

## 1. Exact pressure-overpay velocity

From M5-56 and M5-58, define

\[
E(t):=\bar E_w(t),
\]

and

\[
\boxed{
X(t):=
\bar J_w(t)-\nu\bar D_w(t)
=\dot E(t).
}
\]

`X` is a state observable along the autonomous W1 flow: it is the Lie derivative of the mollified entropy functional in the Navier--Stokes vector field direction.

It is not, in general, a function of `E` alone. The same entropy level may be crossed on an upstroke and a downstroke with opposite signs of `X`.

Thus `(E,X)` is the minimal canonical two-coordinate projection that distinguishes those branches.

---

## 2. Canonical non-exact one-form

M5-59 considered loop one-forms of the type

\[
Y\,dE.
\]

Choose canonically

\[
\boxed{Y=X.}
\]

Then along the W1 trajectory,

\[
X\,dE
=X\dot E\,dt
=X^2dt.
\]

Therefore the associated path action is

\[
\boxed{
\mathcal A_X[I]
:=
\int_I X\,dE
=
\int_I X^2dt
\ge0.
}
\]

This gives the missing orientation automatically.

---

## 3. Closed-loop circulation

For a recurrent or exactly closed projected loop `gamma` in the `(E,X)` plane,

\[
\boxed{
\oint_\gamma X\,dE
=
\int_{cycle}X^2dt.
}
\]

Hence

\[
\oint_\gamma X\,dE>0
\]

for every nonconstant cycle of `E`.

If the one-form `X dE` were exact on a neighborhood containing such a closed loop, its closed-loop integral would vanish. Therefore a nonconstant recurrent pump loop realizes a genuinely non-exact circulation in the `(E,X)` projection.

This is stronger than merely choosing an arbitrary second observable and hoping for a favorable hysteresis orientation.

---

## 4. Robust lower bound from the pump rise

Let a robust pump segment `I=[t_0,t_1]` have

\[
\Delta E
:=E(t_1)-E(t_0)>0.
\]

Since

\[
\Delta E
=
\int_I Xdt,
\]

Cauchy--Schwarz gives

\[
(\Delta E)^2
\le
|I|\int_I X^2dt.
\]

Therefore

\[
\boxed{
\mathcal A_X[I]
=
\int_I X^2dt
\ge
\frac{(\Delta E)^2}{|I|}.
}
\]

This lower bound does not require a pointwise lower bound for `X`; a definite entropy rise over a bounded normalized time interval is sufficient.

---

## 5. Stronger bound from M5-57 transverse intervals

M5-57 produced returned intervals of uniformly positive width on which

\[
X(t)
=
\partial_t\bar E_w(t)
\ge c_1>0.
\]

If each such interval has length at least `tau_1>0`, then

\[
\boxed{
\mathcal A_X(I_n)
\ge
c_1^2\tau_1
=:a_*>0.
}
\]

The constants are fixed in normalized W1 variables.

Thus every sufficiently accurate recurrent pump copy carries one fixed positive amount of canonical squared-overpay action.

---

## 6. Syndetic recurrence gives positive action density

By M5-52 and M5-57, a disjoint recurrent subfamily can be chosen with uniformly bounded Leray-time gaps.

Hence the number of robust pump intervals up to W1 time `H` satisfies

\[
N(H)\ge c_HH-O(1).
\]

Summing the lower bound gives

\[
\boxed{
\sum_{n\le N(H)}
\mathcal A_X(I_n)
\ge
a_*N(H)
\gtrsim H.
}
\]

Thus the canonical loop action has positive lower density in normalized recurrent time.

---

## 7. Relation to M5-58 telescoping

There is no contradiction with M5-58.

M5-58 showed

\[
\int Xdt
=E(T)-E(0),
\]

so the signed first-order action telescopes.

M5-62 instead uses

\[
\boxed{
\int X^2dt,
}
\]

which does not telescope and records both the compensating upstroke and downstroke positively.

Indeed, if recurrence forces a positive upstroke and an equally necessary compensating downstroke, both contribute positively to `X^2`.

Thus the exact cancellation mechanism of M5-58 becomes an additional source of squared action rather than a cancellation.

---

## 8. DSD audit

### GREEN

The choice `Y=X` is canonical and uses no new arbitrary geometric observable.

### GREEN

The loop orientation/sign issue from M5-59 is solved exactly:

\[
X\,dE=X^2dt\ge0.
\]

### GREEN

Robust recurrent pump returns imply a fixed positive per-return action in normalized variables.

### RED

Positive non-exact action still does not contradict compact recurrence by itself, exactly as M5-60 warned.

### YELLOW

The remaining question is now exceptionally sharp: determine the Navier--Stokes scaling of `int X^2dt` and whether any initial-data-controlled finite budget can dominate it.

---

## 9. New proof gate

The hysteresis/orientation search can be removed from the primary branch.

The primary accumulation candidate is now

\[
\boxed{
\mathcal A_X
=
\int
\left(
\bar J_w-
u\bar D_w
\right)^2dt.
}
\]

M5-63 will audit its exact scaling under the covariantly transported amplitude band.

If it is critical, M5-61 implies that the entire accumulation problem reduces to a single endpoint-budget question.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
