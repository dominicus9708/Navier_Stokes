# DSD M17-207 — Divergent cubic packing survives on globally tempered dyadic shells with all finite-neighbor comparability

Date: 2026-09-06  
Canonical ID: **M17-207**

Status: **ALL-LAG TEMPERED PACKING LEMMA / M17-206 EXTRACTS A DIVERGENT SUBFAMILY GOOD FOR ONE FIXED NEIGHBORHOOD WIDTH. TO REMOVE THE CIRCULARITY THAT THE MASS-EXPLOSION LAG IS CHOSEN ONLY AFTER A PACKET SEQUENCE IS EXTRACTED, DEFINE A STRONGER TEMPERED INDEX BY `b_{k+m} <= A^{|m|} b_k` FOR EVERY DYADIC OFFSET `m`. IF AN INDEX IS NOT TEMPERED, JUMP TO A VIOLATING NEIGHBOR; THE CRITICAL COST GROWS BY AT LEAST `A^{|m|}`. A PATH-CHARGING ARGUMENT HAS ONE-STEP TOTAL WEIGHT `sum_{m!=0} A^{-p|m|}=2/(A^p-1)`, WITH `p=3/2`. CHOOSING `A^p>3` MAKES THE FULL PATH TREE SUMMABLE. THEREFORE THE ENTIRE NONSUMMABLE CUBIC MASS IS CONTROLLED BY THE TEMPERED SUBFAMILY, WHICH AUTOMATICALLY HAS UNIFORM COMPARABILITY ON EVERY FIXED FINITE NEIGHBORHOOD. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Critical sequence

Let

\[
\boxed{b_k\ge0,\qquad \sup_kb_k\le b_*<\infty.}
\]

Set

\[
p:=\frac32.
\]

Choose a fixed

\[
A>1
\]

such that

\[
\boxed{A^p>3.}
\]

For example `A=4` is more than sufficient.

---

## 2. Globally tempered indices

Call `k` tempered if

\[
\boxed{
b_{k+m}\le A^{|m|}b_k\qquad\forall m\in\mathbb Z}
\]

for every available tail index.

Let

\[
G_{temp}
\]

denote the tempered set.

This single condition controls every fixed finite neighborhood, with a constant depending only on its width.

---

## 3. Bad index jump

If `k` is not tempered, choose one violating offset `m!=0` such that

\[
\boxed{b_{k+m}>A^{|m|}b_k.}
\]

Move from `k` to `k+m` and repeat while the current index remains non-tempered.

After a path with offsets `m_1,...,m_n`,

\[
\boxed{
b_{end}>A^{\sum_{i=1}^n|m_i|}b_{start}.}
\]

Since every nonzero step has integer length at least one and `b<=b_*`, an infinite path is impossible for `b_start>0`.
Thus each positive index reaches a tempered terminal index after finitely many jumps.

---

## 4. Path charge

If a path from `k` to terminal tempered `g` has total length

\[
L=\sum_i|m_i|,
\]

then

\[
b_k^p\le A^{-pL}b_g^p.
\]

Instead of counting distinct predecessors exactly, overcount by all signed jump sequences.
The total one-step weight is

\[
q_A
:=\sum_{m\ne0}A^{-p|m|}
=2\sum_{m=1}^\infty A^{-pm}
=\frac{2}{A^p-1}.
\]

Because `A^p>3`,

\[
\boxed{q_A<1.}
\]

The weight of all paths of `n` jumps is at most `q_A^n`.
Therefore the total charge to one terminal good index is bounded by

\[
\sum_{n=0}^\infty q_A^n
=\frac1{1-q_A}.
\]

---

## 5. Global inequality

Summing over terminal tempered indices,

\[
\boxed{
\sum_kb_k^{3/2}
\le
\frac1{1-q_A}
\sum_{g\in G_{temp}}b_g^{3/2}.
}
\]

Hence

\[
\boxed{
\sum_kb_k^{3/2}=\infty
\Longrightarrow
\sum_{g\in G_{temp}}b_g^{3/2}=\infty.
}
\]

The nonsummable critical defect therefore cannot avoid the globally tempered subfamily.

---

## 6. Every fixed material lag is controlled on a tempered shell

For dyadic radii,

\[
R_{k+m}=2^mR_k.
\]

On a tempered index,

\[
E_{k+m}=\frac{b_{k+m}}{R_{k+m}}
\le
A^{|m|}2^{-m}E_k.
\]

Thus for every fixed finite width `M`,

\[
\boxed{
\sum_{|m|\le M}E_{k+m}
\le C_{A,M}E_k
\qquad(k\in G_{temp}).
}
\]

This is exactly the all-fixed-lag neighborhood control needed to combine with M17-205 without choosing the shell sequence after the lag is known.

---

## 7. DSD audit

- The path counting deliberately overcounts; this is harmless for an upper charging bound.
- No decay rate of `b_k` is assumed.
- Diffuse examples such as `b_k~k^(-2/3)` are globally tempered for large `k` for any fixed `A>1`.
- The lemma is purely combinatorial and does not use Navier--Stokes dynamics.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
