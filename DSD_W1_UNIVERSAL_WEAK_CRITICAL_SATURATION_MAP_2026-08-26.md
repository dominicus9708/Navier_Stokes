# DSD W1 Universal Weak-Critical Saturation Map

Date: 2026-08-26

Status: **W1 ENDPOINT RECAST AS A LARGE WEAK-CRITICAL SATURATION CLASS ACROSS SERRIN, D3, AND STREAMLINE-AMPLITUDE VARIABLES / STRONG CRITICAL NORMS FAIL BY RECURRENCE / GLOBAL REGULARITY UNPROVED.**

## 1. Serrin family

Fix `p>3` and define the critical Serrin time exponent

\[
\boxed{
q_p=\frac{2p}{p-3}.
}
\]

The backward Leray scaling gives

\[
\boxed{
\|u(t)\|_{L_x^p}
=
\tau^{-\frac{p-3}{2p}}
\|U(s)\|_{L_Y^p},
\qquad
\tau=T_*-t=e^{-s}.
}
\]

On the compact W1 corridor,

\[
\|U(s)\|_p\le M_p.
\]

Hence

\[
\|u(t)\|_p
\le
M_p\tau^{-1/q_p}.
\]

Therefore

\[
\boxed{
u\in L_t^{q_p,\infty}L_x^p
}
\]

near the candidate singular time.

---

## 2. Strong critical Serrin norm diverges under nontrivial recurrence

On a nontrivial compact minimal W1 set, the continuous observable

\[
U\mapsto\|U\|_p
\]

has a strictly positive minimum. Indeed, if one state had zero `Lp` norm it would be the zero equilibrium, already excluded.

Thus for the minimal orbit

\[
\boxed{
\|U(s)\|_p\ge m_p>0.
}
\]

More generally, for a prelimit orbit recurrently shadowing the minimal class, fixed positive `Lp` events occur on infinitely many Leray intervals.

Since

\[
\|u(t)\|_p^{q_p}dt
=
\|U(s)\|_p^{q_p}ds,
\]

each fixed Leray interval pays a fixed strong-critical Serrin action.

Hence the W1 survivor necessarily violates the strong Serrin class:

\[
\boxed{
 u\notin L_t^{q_p}L_x^p.
}
\]

At the same time it remains in the weak-time endpoint supplied by the Type-I ceiling.

Thus

\[
\boxed{
 u\in L_t^{q_p,\infty}L_x^p
\setminus
L_t^{q_p}L_x^p.
}
\]

---

## 3. Structural criteria show the same pattern

### Streamline-amplitude flow

\[
e=u\cdot\nabla|u|
\]

satisfies on W1

\[
\boxed{
e\in L_t^{2,\infty}L_x^{3/2}
\setminus
L_t^2L_x^{3/2}.
}
\]

### D3 endpoint dissipation

\[
D_{3,phys}(t)
\]

obeys schematically

\[
\boxed{
D_{3,phys}
\in L_t^{1,\infty}
\setminus L_t^1.
}
\]

### Critical Gaussian currents

The Bernoulli and weighted-vorticity ledgers carry nonzero scale-current averages on the logarithmic clock.

All of these are manifestations of the same pattern.

---

## 4. DSD endpoint class

The W1 survivor does not occupy an arbitrary irregular class.

It is squeezed between:

1. a Type-I / compact normalized upper ceiling;
2. nontrivial recurrent lower activity;
3. exact Navier--Stokes scaling.

This forces the universal form

\[
\boxed{
\text{weak critical control}
+
\text{failure of strong critical integrability}.
}
\]

The endpoint is therefore best described as a **large weak-critical recurrent class**.

---

## 5. Consequence for proof search

Any criterion whose hypothesis is merely a strong critical norm automatically fails on W1 by construction.

Any criterion that requires smallness of a weak critical norm can exclude only the small-amplitude part of the class.

The unresolved part is the large weak-critical endpoint together with recurrence and the specific Navier--Stokes structural identities.

Therefore the final theorem must exploit at least one feature beyond generic weak-critical membership:

- recurrence/minimality;
- simultaneous velocity and vorticity scale currents;
- amplitude-direction/Lamb projection structure;
- a logarithmic improvement forced by the finite-energy parent;
- or an independent scale-breaking parent/interface constraint.

---

## 6. Current compressed proof map

\[
\boxed{
\text{hypothetical blow-up}
\to
W1
\to
\text{compact recurrent dynamics}
\to
\text{large weak-critical saturation}
\to
\text{missing endpoint incompatibility theorem}.
}
\]

This does not prove regularity. It identifies the exact class that any remaining DSD closure must eliminate.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
