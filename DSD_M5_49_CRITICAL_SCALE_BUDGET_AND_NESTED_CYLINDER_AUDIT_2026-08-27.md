# DSD M5-49 — Critical-Scale Budget and Nested-Cylinder Audit

Date: 2026-08-27

Status: **EXACT PARABOLIC-SCALING AUDIT / REPEATED SCALE-INVARIANT BADNESS AT SHRINKING RADII DOES NOT FORCE DIVERGENCE OF THE ORDINARY PHYSICAL ENERGY OR DISSIPATION BUDGET / NESTED PARABOLIC CYLINDERS CANNOT BE SUMMED AS INDEPENDENT COSTS / THE NAIVE MULTISCALE COUNTING BRANCH IS CLOSED / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

M5-47 showed that a recurrent normalized pump may carry order-one critical action at every return while ordinary physical costs shrink.

M5-48 then fixed the coordinate interpretation: the outer `1/r` ancestry of the blow-up cell represents intermediate physical radii near the same singular point, not original physical infinity.

The next question is whether infinitely many bad scales near the same point can nevertheless be excluded by adding local-energy or Caffarelli--Kohn--Nirenberg-type costs over those scales.

This memo audits that route exactly.

---

## 2. Parabolic rescaling around the candidate singular point

Let `(x_*,T)` be a candidate singular point and, for `r>0`, define

\[
v_r(y,s)
:=r\,u(x_*+ry,T+r^2s),
\]

\[
q_r(y,s)
:=r^2 p(x_*+ry,T+r^2s).
\]

Write

\[
Q_r:=B_r(x_*)\times(T-r^2,T).
\]

For the pressure, let

\[
\pi_r(x,t):=p(x,t)-(p)_{B_r}(t)
\]

with the spatial mean taken at each time.

---

## 3. Standard scale-invariant local quantities

Define

\[
A(r)
:=
\frac1r
\sup_{T-r^2<t<T}
\int_{B_r(x_*)}|u(x,t)|^2\,dx,
\]

\[
E(r)
:=
\frac1r
\int_{Q_r}|\nabla u|^2\,dx\,dt,
\]

\[
C(r)
:=
\frac1{r^2}
\int_{Q_r}|u|^3\,dx\,dt,
\]

and

\[
D(r)
:=
\frac1{r^2}
\int_{Q_r}|\pi_r|^{3/2}\,dx\,dt.
\]

Under the above parabolic scaling,

\[
\boxed{
A(r)=A_{v_r}(1),\qquad
E(r)=E_{v_r}(1),\qquad
C(r)=C_{v_r}(1),\qquad
D(r)=D_{q_r}(1).
}
\]

Thus all four quantities are dimensionless and can remain order one at every recurrent normalized copy.

---

## 4. What the same statements mean in the original physical variables

Undoing the normalizations gives

\[
\boxed{
\sup_{T-r^2<t<T}
\int_{B_r}|u|^2\,dx
=rA(r),
}
\]

\[
\boxed{
\int_{Q_r}|\nabla u|^2\,dx\,dt
=rE(r),
}
\]

\[
\boxed{
\int_{Q_r}|u|^3\,dx\,dt
=r^2C(r),
}
\]

and

\[
\boxed{
\int_{Q_r}|\pi_r|^{3/2}\,dx\,dt
=r^2D(r).
}
\]

Therefore a fixed positive lower bound in normalized coordinates has the following raw physical costs:

| normalized quantity | possible fixed normalized cost | raw physical scaling |
|---|---:|---:|
| local kinetic energy `A` | `O(1)` | `O(r)` |
| spacetime dissipation `E` | `O(1)` | `O(r)` |
| cubic velocity action `C` | `O(1)` | `O(r^2)` |
| pressure `3/2` action `D` | `O(1)` | `O(r^2)` |

The shrinking physical costs are not a defect of the estimate. They are exactly what Navier--Stokes critical scaling requires.

---

## 5. Infinite recurrence still admits a geometrically separated subsequence

Suppose the same normalized trajectory returns at infinitely many scales

\[
r_n\downarrow0.
\]

No density assumption is required.

From any such sequence one can select a subsequence, again denoted `r_n`, for which

\[
r_{n+1}\le \theta r_n
\]

with any fixed `0<theta<1`, for example `theta=1/2`.

Consequently

\[
\sum_n r_n<\infty,
\qquad
\sum_n r_n^2<\infty.
\]

Hence even if every selected recurrent copy obeys fixed positive lower bounds

\[
A(r_n),E(r_n),C(r_n),D(r_n)\ge c_*>0,
\]

the corresponding raw physical costs are compatible with finite sums of the form

\[
\sum_n c_*r_n<\infty,
\qquad
\sum_n c_*r_n^2<\infty.
\]

So ordinary finite-energy or finite-dissipation accounting does not contradict an infinite recurrent scale ladder.

---

## 6. Nested-cylinder nonadditivity is an independent obstruction

There is an even more basic issue.

For a decreasing radius sequence,

\[
Q_{r_{n+1}}\subset Q_{r_n}.
\]

Thus lower bounds such as

\[
\int_{Q_{r_n}}|\nabla u|^2\ge c r_n
\]

cannot be added over `n` as if the cylinders were disjoint.

The same spacetime region is counted repeatedly.

Passing to annular spacetime shells

\[
Q_{r_n}\setminus Q_{r_{n+1}}
\]

does not repair the argument automatically, because a lower bound on the full inner cylinder does not imply a uniform lower bound on each shell.

Therefore

\[
\boxed{
\text{infinitely many bad nested scales}
\not\Rightarrow
\text{sum of infinitely many independent positive physical costs}.
}
\]

This is a logical point in addition to the scaling point of Section 5.

---

## 7. Consequence for epsilon-regularity counting

A singular point can force scale-invariant quantities to stay above an epsilon-regularity threshold along arbitrarily small scales.

But the statement

\[
C(r_n)+D(r_n)\ge\varepsilon_*
\]

is dimensionless.

It does **not** imply

\[
\int_{Q_{r_n}}
\bigl(|u|^3+|\pi_{r_n}|^{3/2}\bigr)
\ge\varepsilon_*
\]

in physical units.

The actual unnormalized lower bound is only

\[
\int_{Q_{r_n}}
\bigl(|u|^3+|\pi_{r_n}|^{3/2}\bigr)
\gtrsim
\varepsilon_* r_n^2.
\]

These costs can be summable, and the cylinders are nested anyway.

Accordingly, a proof cannot close merely by saying that infinitely many epsilon-bad scales exhaust a finite physical budget.

---

## 8. Relation to M5-47

M5-47 distinguished two ledgers:

1. ordinary physical energy/dissipation costs, which shrink with the recurrent scale;
2. beta-zero critical actions, which can remain order one per normalized event.

M5-49 sharpens that statement in the local regularity language:

\[
\boxed{
\text{CKN-scale badness can persist at every return while ordinary raw costs remain summable.}
}
\]

The distinction is therefore not an artifact of the W1 notation. It is built into the parabolic scaling of the standard local quantities themselves.

---

## 9. DSD branch audit

### GREEN — retained exact statements

- The four quantities `A,E,C,D` above are scale invariant.
- Their raw physical counterparts scale respectively like `r,r,r^2,r^2`.
- Every infinite shrinking-radius sequence has a geometrically separated subsequence.
- Nested cylinders cannot be charged as independent costs without a shell lower bound.

### RED — branches closed by this audit

The following closure attempts are insufficient by themselves:

- `infinitely many epsilon-bad scales + finite energy`;
- `order-one normalized dissipation at every return + finite total physical dissipation`;
- summing positive lower bounds over nested parabolic cylinders;
- repeating an ordinary subcritical or raw physical budget under renormalization.

### OPEN — surviving closure target

A successful multiscale rigidity argument must produce something stronger than a positive cost in each normalized copy.

It needs, for example,

\[
\boxed{
\text{a scale-invariant signed defect that is additive/telescoping across returns}
}
\]

or an equivalent rigidity statement that forces recurrence to collapse to a forbidden exact profile.

This becomes the next gate.

---

## 10. Proof-search consequence

The surviving target is no longer

\[
\text{count bad scales}.
\]

It is

\[
\boxed{
\text{convert each nontrivial same-trajectory return into an irreversible signed increment/decrement.}
}
\]

Such an object would evade both failures identified above:

- it would be critical rather than raw/subcritical;
- and it would telescope over return intervals rather than double-count nested cylinders.

This is the natural interface with the M5-37 strict pressure-tail gap.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
