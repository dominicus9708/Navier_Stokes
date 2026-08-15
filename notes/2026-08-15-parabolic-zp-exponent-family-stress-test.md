# Parabolic Zeno exponent family: stress test of the final reset ledgers

Date: 2026-08-15

Status: **ADVERSARIAL SCALING FAMILY SURVIVES ALL CURRENT RESET BUDGETS / SHOWS A NEW CRITICAL RIGIDITY INPUT IS STILL REQUIRED.**

This note tests whether the current final ledgers already contradict one another.

They do not.

A simple one-parameter power family simultaneously satisfies

- the automatic reset relation;
- coherent radius divergence;
- finite reset energy budget;
- finite physical Zeno time;
- divergent BKM-scale action.

Thus the remaining problem is genuinely critical and cannot be closed by the current power-counting inequalities alone.

---

## 1. Current reset variables

At a coherent crossing define

\[
q=\frac{W}{R^{10}},
\qquad
\ell=\frac{R}{\sqrt W}.
\]

The established bounded-distortion reset ledgers are

\[
\boxed{
\text{energy price}\asymp q^{-1/2},
}
\]

\[
\boxed{
\text{parabolic time}\gtrsim \ell^2/\nu,
}
\]

and

\[
\boxed{
\text{vorticity/BKM action}\gtrsim R^2/\nu.
}
\]

The coherent branch also requires

\[
R\to\infty.
\]

---

## 2. Power-law reset ratio

Fix any

\[
\boxed{0<\alpha<1}
\]

and set

\[
\boxed{
q=W^\alpha.
}
\]

The reset relation gives

\[
R^{10}=W/q=W^{1-\alpha},
\]

hence

\[
\boxed{
R=W^{(1-\alpha)/10}\to\infty.
}
\]

The physical core scale is

\[
\boxed{
\ell
=\frac{R}{\sqrt W}
=W^{-(4+\alpha)/10}.
}
\]

Thus all three scales are compatible for every fixed `alpha in (0,1)`.

---

## 3. Choose geometric first-hitting levels

Take the stress-test sequence

\[
\boxed{
W_j=2^j.
}
\]

Then

\[
q_j=2^{\alpha j},
\qquad
R_j=2^{(1-\alpha)j/10},
\qquad
\ell_j=2^{-(4+\alpha)j/10}.
\]

This is not asserted to be a Navier--Stokes solution. It is an adversarial sequence satisfying the current scalar constraints.

---

## 4. Energy-reset budget is summable

The per-reset physical energy-dissipation price is

\[
q_j^{-1/2}=2^{-\alpha j/2}.
\]

Therefore

\[
\boxed{
\sum_{j=1}^\infty q_j^{-1/2}<\infty
}
\]

for every `alpha>0`.

So the finite kinetic-energy budget does not exclude this sequence.

---

## 5. Parabolic reset times are summable

The physical parabolic time scale is

\[
\ell_j^2
=2^{-(4+\alpha)j/5}.
\]

Hence

\[
\boxed{
\sum_{j=1}^\infty\ell_j^2<\infty.
}
\]

Thus infinitely many resets can fit into a finite physical time at the current lower-bound level.

This is the literal Zeno property.

---

## 6. BKM action diverges

Each reset requires vorticity action of size at least

\[
R_j^2
=2^{(1-\alpha)j/5}.
\]

Therefore

\[
\boxed{
\sum_{j=1}^\infty R_j^2=\infty.
}
\]

This is fully compatible with a hypothetical finite-time singularity because BKM-critical vorticity action is required to diverge on a singular route.

---

## 7. Compatibility with the logarithmic coherent-tail barrier

The coherent-tail estimate implies asymptotically

\[
q\gtrsim (\log R)^5.
\]

For the present family,

\[
q=W^\alpha,
\qquad
\log R\asymp\log W.
\]

Any positive power `W^alpha` dominates `(log W)^5` as `W->infinity`.

Therefore the logarithmic tail improvement does not remove the power-law Zeno family.

---

## 8. Why another fixed power of `R` is unlikely to be enough by itself

Suppose a future estimate improved the reset price schematically to

\[
R^\beta q^{-1/2}.
\]

On the stress-test family this scales as

\[
W^{\beta(1-\alpha)/10-\alpha/2}.
\]

For a fixed `beta`, choosing `alpha` sufficiently close to `1` makes the exponent negative.

Therefore no fixed polynomial `R^beta` gain automatically defeats **all** `alpha in (0,1)`.

This does not prove that every such improvement is useless in a fuller coupled argument, but it shows why the final missing ingredient is more likely to be

- a scale-invariant rigidity theorem;
- a critical Carleson/contraction mechanism;
- an ancient-limit exclusion;
- or a nonlinear relation that restricts `q` and `R` beyond the algebraic identity `q=W/R^10`.

---

## 9. Final interpretation

The current proof architecture has genuinely excluded many algebraic and geometric escape routes, but it has now reached a critical Zeno family that survives every established scalar budget.

The adversarial normal form is

\[
\boxed{
W_j\uparrow\infty,
\quad
q_j=W_j^\alpha,
\quad
R_j=W_j^{(1-\alpha)/10},
\quad
\ell_j=W_j^{-(4+\alpha)/10},
\quad 0<\alpha<1.
}
\]

It has

\[
\boxed{
\text{finite energy-reset sum}
+\text{finite physical time}
+\text{divergent critical action}.
}
\]

That is exactly the signature a hypothetical singular cascade is allowed to have.

Status: **CURRENT POWER LEDGERS DO NOT CLOSE GLOBAL REGULARITY / FINAL TARGET MUST BREAK THE PARABOLIC ZENO FAMILY BY A GENUINELY CRITICAL STRUCTURAL ARGUMENT.**