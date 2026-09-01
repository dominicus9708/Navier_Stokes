# DSD M5-539 — Control of every Lp above 3 does not determine a Lorentz L3 endpoint class

Date: 2026-09-01

Status: **FUNCTION-SPACE ENDPOINT AUDIT / M5-537--538 PLACE A TYPICAL HARD VELOCITY IN EVERY `Lp`, `p>3`, WHILE `L3` IS INFINITE / THIS PACKAGE ALONE DOES NOT IMPLY MEMBERSHIP IN `L^(3,q)` FOR ANY FINITE `q`, NOR EVEN IN WEAK `L3` / EXPLICIT RADIAL LOW-AMPLITUDE WITNESSES SHOW THREE DISTINCT POSSIBILITIES WITH THE SAME `INTERSECTION_{p>3} Lp \ L3` PROPERTY: WEAK-`L3` WITH NO FINITE LORENTZ IMPROVEMENT, FINITE-`q` LORENTZ IMPROVEMENT ABOVE A THRESHOLD, AND FAILURE OF WEAK-`L3` ITSELF / THEREFORE NO ENDPOINT LORENTZ REGULARITY THEOREM MAY BE IMPORTED WITHOUT NEW QUANTITATIVE CONTROL AS `p -> 3+` / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Current package

M5-537--538 give, for invariant-almost every hard state,

\[
\boxed{
U\in\bigcap_{p>3}L^p(\mathbb R^3),
\qquad
U\notin L^3(\mathbb R^3).
}
\]

The question is whether this forces a Lorentz endpoint such as

\[
L^{3,q},
\qquad
q<\infty,
\]

or at least

\[
L^{3,\infty}.
\]

It does not.

---

## 2. Radial decreasing model

Consider, only as a function-space witness,

\[
f(r)
=\frac{L(r)}{r}
\qquad
(r\gg1),
\]

with a slowly varying logarithmic factor `L(r)`.

These scalar examples are not claimed to solve Navier--Stokes. Their role is solely to test which implications between function spaces are logically valid.

For every fixed

\[
p>3,
\]

a factor growing or decaying by powers of `log r` does not defeat the polynomial integrability

\[
\int^\infty r^{2-p}(\log r)^A dr<\infty.
\]

Thus all examples below lie in every `Lp`, `p>3`.

---

## 3. Weak-L3 without any finite Lorentz improvement

Take

\[
\boxed{
f_0(r)=\frac1r
\quad(r>1).
}
\]

Then

\[
f_0\in L^p
\qquad\forall p>3,
\]

but

\[
f_0\notin L^3.
\]

Its decreasing rearrangement satisfies

\[
f_0^*(t)\asymp t^{-1/3}.
\]

Hence

\[
\sup_{t>0}t^{1/3}f_0^*(t)<\infty,
\]

so

\[
\boxed{f_0\in L^{3,\infty}.}
\]

For any finite `q`, however,

\[
\int^\infty
\left[t^{1/3}f_0^*(t)\right]^q
\frac{dt}{t}
\asymp
\int^\infty\frac{dt}{t}
=\infty.
\]

Thus

\[
\boxed{
f_0\notin L^{3,q}
\qquad
\forall q<\infty.
}
\]

---

## 4. Logarithmic decay gives a finite-q threshold

Let

\[
\boxed{
f_a(r)
=\frac1{r(\log r)^a},
\qquad
r>e,
\qquad
a>0.
}
\]

Then

\[
f_a^*(t)
\asymp
\frac{t^{-1/3}}{(\log t)^a}
\]

up to harmless logarithmic equivalence.

Therefore

\[
\|f_a\|_{L^{3,q}}^q
\sim
\int^\infty
(\log t)^{-aq}
\frac{dt}{t}.
\]

This converges exactly when

\[
\boxed{aq>1.}
\]

For example, at

\[
a=\frac13,
\]

we have

\[
f_{1/3}\notin L^3,
\]

while

\[
\boxed{
f_{1/3}\in L^{3,q}
\quad\text{for every }q>3,
}
\]

and it fails at `q<=3`.

Thus even within weak `L3`, the finite Lorentz endpoint can vary continuously.

---

## 5. All p>3 without even weak-L3

Take instead

\[
\boxed{
g_a(r)
=\frac{(\log r)^a}{r},
\qquad
r>e,
\qquad a>0.
}
\]

Again

\[
g_a\in L^p
\qquad\forall p>3,
\]

and

\[
g_a\notin L^3.
\]

But now

\[
t^{1/3}g_a^*(t)
\asymp
(\log t)^a
\to\infty.
\]

Hence

\[
\boxed{
g_a\notin L^{3,\infty}.}
\]

So even weak `L3` does not follow from membership in every `Lp`, `p>3`.

---

## 6. Exact non-implications

The current M5-537 package therefore does **not** imply any of

\[
\boxed{
U\in L^{3,q}
\quad(q<\infty),
}
\]

or

\[
\boxed{
U\in L^{3,\infty}.
}
\]

The only valid universal statement is

\[
\boxed{
U\in\bigcap_{p>3}L^p
\setminus L^3.
}
\]

---

## 7. What extra information would be sufficient

To infer a Lorentz endpoint one needs quantitative control of how

\[
\|U\|_p
\]

behaves as

\[
p\downarrow3.
\]

Equivalently, through M5-537, one needs quantitative information on the growth of

\[
\mathcal M_\alpha
\]

as

\[
\alpha\uparrow1.
\]

For example, a sufficiently controlled blow-up rate in `1/(1-alpha)` could imply logarithmic endpoint information.

M5-536 currently proves finiteness for each fixed `alpha<1` but does not supply a uniform sharp rate as `alpha -> 1-` because the radius at which the far-field strain becomes absorbably small may itself grow arbitrarily fast.

---

## 8. Why the missing rate is genuine

M5-535 proves only

\[
\varepsilon_{far}(R)
:=
\sup_Y\sup_{|y|>R}
\left(
|\Sigma_Y(y)|+rac{|U_Y(y)|}{1+|y|}
\right)
\to0.
\]

No universal decay rate for `epsilon_far(R)` has been obtained.

In the M5-536 proof, the absorption radius `R_alpha` is chosen so that

\[
\varepsilon_{far}(R_\alpha)
\ll1-\alpha.
\]

Without a quantitative inverse modulus for `epsilon_far`, the resulting moment constant may deteriorate arbitrarily rapidly as `alpha -> 1`.

Thus no logarithmic/Lorentz endpoint may be silently inferred.

---

## 9. DSD audit verdict

The correct hierarchy is

\[
\boxed{
\text{all }Lp,\ p>3
\quad\text{proved},
}
\]

\[
\boxed{
L^3
\quad\text{excluded almost everywhere on the hard component},
}
\]

while

\[
\boxed{
L^{3,q},\ L^{3,\infty}
\quad\text{remain genuinely unresolved endpoint channels}.
}
\]

This prevents a false closure by importing a Lorentz regularity theorem under hypotheses not established by the proof line.

---

## 10. Highest-value next target

The next endpoint calculation should not guess a logarithmic class.

Instead define the actual uniform far-field modulus

\[
\varepsilon_{far}(R)
\]

from M5-535 and construct an **adaptive near-critical radial weight** whose damping deficit is chosen directly from that modulus.

Such a weight may yield a rigorously controlled Orlicz/slowly-varying endpoint tailored to the hard hull.

If the resulting adaptive endpoint is strong enough to imply a known critical regularity criterion, the tail closes. If not, it gives the precise remaining endpoint modulus rather than an arbitrary Lorentz label.

---

## 11. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
