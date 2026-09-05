# DSD M17-206 — Nonsummable cubic dyadic mass survives restriction to finite-neighbor-comparable good shells

Date: 2026-09-06  
Canonical ID: **M17-206**

Status: **COMBINATORIAL PACKING LEMMA / LET `b_k>=0` BE THE BOUNDED SCALE-CRITICAL SHELL SEQUENCE OF M5-526 AND FIX A FINITE NEIGHBORHOOD WIDTH `M`. CALL `k` GOOD IF EVERY `|m|<=M` SATISFIES `b_{k+m} <= C b_k`. IF `k` IS BAD, MOVE TO A NEIGHBOR WITH VALUE GREATER THAN `C b_k`. REPEATING MUST TERMINATE AT A GOOD INDEX BECAUSE `b_k` IS UNIFORMLY BOUNDED. CHARGING EACH BAD INDEX TO ITS TERMINAL GOOD INDEX, THE NUMBER OF DEPTH-`n` PREDECESSORS IS AT MOST `(2M)^n`, WHILE THEIR `3/2`-POWER MASS IS SUPPRESSED BY `C^{-3n/2}`. CHOOSING `C^(3/2)>2M` MAKES THE CHARGE SUMMABLE. THUS DIVERGENCE OF `sum b_k^(3/2)` FORCES DIVERGENCE ON THE GOOD-SHELL SUBFAMILY ITSELF. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Sequence and good-shell definition

Let

\[
\boxed{b_k\ge0,\qquad \sup_k b_k\le b_*<\infty.}
\]

In the application,

\[
b_k=R_kE_k
\]

is the M5-526 scale-critical shell cost.

Fix an integer

\[
M\ge1
\]

and a constant

\[
C>1.
\]

Call index `k` **good** if

\[
\boxed{
b_{k+m}\le Cb_k\qquad\forall |m|\le M}
\]

whenever the neighboring index exists.

Let `G` be the set of good indices.

---

## 2. Bad indices climb to a larger neighbor

If `k` is bad, there exists some `m` with

\[
0<|m|\le M
\]

such that

\[
\boxed{b_{k+m}>Cb_k.}
\]

Choose one such neighbor and call it `T(k)`.

Iterate:

\[
k,\quad T(k),\quad T^2(k),\dots
\]

As long as the current index is bad, the sequence values grow by at least `C` per step:

\[
\boxed{b_{T^n(k)}>C^n b_k.}
\]

Because `b<=b_*`, an infinite strictly `C`-growing chain is impossible for any `b_k>0`.
Thus every positive bad index reaches a good index after finitely many steps.

Zero entries carry no cubic mass and may be ignored.

---

## 3. Charge bad indices to terminal good indices

For each `k` with `b_k>0`, let

\[
g(k)\in G
\]

be one terminal good index reached by the iteration, and let `n(k)` be the number of steps.

Then

\[
\boxed{
b_k\le C^{-n(k)}b_{g(k)}.}
\]

Hence

\[
\boxed{
b_k^{3/2}\le C^{-3n(k)/2}b_{g(k)}^{3/2}.}
\]

---

## 4. Count possible predecessors

Each step changes the index by one of at most `2M` nonzero offsets.
Therefore, for one fixed terminal good index `g`, the number of possible depth-`n` predecessors is at most

\[
\boxed{(2M)^n.}
\]

Consequently the total cubic mass charged to `g` is bounded by

\[
\begin{aligned}
\sum_{k:g(k)=g}b_k^{3/2}
&\le
b_g^{3/2}
\sum_{n=0}^\infty
(2M)^nC^{-3n/2}.
\end{aligned}
\]

Choose

\[
\boxed{C^{3/2}>2M.}
\]

Then the geometric series converges.
Define

\[
C_{M,C}
:=\frac1{1-2M C^{-3/2}}.
\]

Thus

\[
\boxed{
\sum_{k:g(k)=g}b_k^{3/2}
\le C_{M,C}b_g^{3/2}.
}
\]

---

## 5. Global charging inequality

Summing over all good terminal indices,

\[
\boxed{
\sum_k b_k^{3/2}
\le
C_{M,C}
\sum_{g\in G}b_g^{3/2}.
}
\]

Therefore

\[
\boxed{
\sum_k b_k^{3/2}=\infty
\Longrightarrow
\sum_{g\in G}b_g^{3/2}=\infty.
}
\]

So the non-`L3` critical packing defect cannot hide entirely on shells with arbitrarily bad finite-neighbor ratios.

---

## 6. Convert good critical costs to shell-mass comparability

For dyadic radii

\[
R_{k+m}=2^mR_k.
\]

If `k` is good and `|m|<=M`,

\[
E_{k+m}
=\frac{b_{k+m}}{R_{k+m}}
\le
C2^{-m}E_k
\]

for positive `m`, while for negative `m`

\[
E_{k+m}\le C2^{|m|}E_k.
\]

Hence, for fixed `M`,

\[
\boxed{
\sum_{|m|\le M}E_{k+m}
\le C'_{M,C}E_k
\qquad(k\in G).
}
\]

This is exactly the finite-neighborhood comparability needed in M17-205.

---

## 7. DSD audit

- No monotonicity of the shell sequence is assumed.
- Long diffuse examples such as `b_k~k^(-2/3)` are allowed; they are in fact predominantly good for fixed `M`.
- The lemma uses only boundedness of `b_k` and the cubic exponent `3/2`.
- The neighbor width is fixed before the selection and may depend on the fixed material lag `T` through M17-205.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
