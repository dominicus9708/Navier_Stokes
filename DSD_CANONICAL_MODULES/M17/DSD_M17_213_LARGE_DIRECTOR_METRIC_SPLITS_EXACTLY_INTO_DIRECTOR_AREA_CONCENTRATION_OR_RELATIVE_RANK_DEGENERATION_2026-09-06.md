# DSD M17-213 — Large director metric splits exactly into director-area concentration or relative rank degeneration

Date: 2026-09-06  
Canonical ID: **M17-213**

Status: **DIRECTOR-SPECTRAL GEOMETRY SPLIT / ON A RANK-2 DIRECTOR MAP LET `s1>=s2>0` BE THE TWO NONZERO SINGULAR VALUES. THEN `|J_xi|=s1 s2` AND `|grad xi|^2=s1^2+s2^2`. DEFINING THE DIMENSIONLESS ANISOTROPY `A_xi=(s1^2+s2^2)/(2 s1 s2)>=1` GIVES THE EXACT FACTORIZATION `|grad xi|^2=2 |J_xi| A_xi`. CONSEQUENTLY THE M17-212 LARGE-DIRECTOR-METRIC SPECTRAL BRANCH CAN OCCUR ONLY THROUGH LARGE DIRECTOR-AREA CURRENT OR LARGE ANISOTROPY. IF `|J_xi|` REMAINS BOUNDED ABOVE WHILE THE METRIC DIVERGES, THE CONDITION NUMBER `s1/s2` DIVERGES AND THE MAP APPROACHES A RELATIVE RANK-1 GEOMETRY EVEN THOUGH ITS POINTWISE RANK MAY REMAIN TWO. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Singular values of the director derivative

For

\[
\xi:\mathbb R^3\to S^2,
\]

the derivative has rank at most two because

\[
\xi\cdot\partial_i\xi=0.
\]

On a Rank-2 point let the two nonzero singular values be

\[
\boxed{s_1\ge s_2>0.}
\]

Then the Frobenius metric is

\[
\boxed{|\nabla\xi|^2=s_1^2+s_2^2.}
\]

The director-area current magnitude is the product

\[
\boxed{|J_\xi|=s_1s_2.}
\]

---

## 2. Exact anisotropy factorization

Define

\[
\boxed{
\mathcal A_\xi
:=\frac{s_1^2+s_2^2}{2s_1s_2}.
}
\]

By AM--GM,

\[
\boxed{\mathcal A_\xi\ge1,}
\]

with equality only for conformal singular values `s1=s2`.

The metric factorizes exactly as

\[
\boxed{
|\nabla\xi|^2
=2|J_\xi|\mathcal A_\xi.
}
\]

Thus the two pieces have distinct meanings:

- `|J_xi|` measures director-area magnitude;
- `A_xi` measures shape anisotropy / condition number.

---

## 3. Large metric dichotomy

If

\[
|\nabla\xi|^2\to\infty,
\]

then from the product factorization at least one of

\[
\boxed{|J_\xi|\to\infty}
\]

or

\[
\boxed{\mathcal A_\xi\to\infty}
\]

must occur along a subsequence.

Therefore

\[
\boxed{
G_{director\ metric^2}
\Longrightarrow
G_{director\ area\ concentration}
\lor
G_{director\ anisotropy}.
}
\]

---

## 4. Bounded-area branch implies relative rank degeneration

Suppose instead that the director-area magnitude remains bounded above:

\[
|J_\xi|\le J^*<\infty
\]

while

\[
M:=|\nabla\xi|^2\to\infty.
\]

Since

\[
s_1^2+s_2^2=M,
\]

we have

\[
s_1^2\ge M/2.
\]

Then

\[
s_2=\frac{|J_\xi|}{s_1}
\le\frac{\sqrt2J^*}{\sqrt M}\to0
\]

whenever the product remains bounded.

The singular-value condition number satisfies

\[
\boxed{
\frac{s_1}{s_2}
=\frac{s_1^2}{|J_\xi|}
\ge\frac{M}{2J^*}	o\infty.
}
\]

Thus the map becomes increasingly one-directional:

\[
\boxed{
\text{Rank-2 pointwise}
\quad\text{but}\quad
\text{relative Rank-1 geometry}.
}
\]

This is the correct meaning of the anisotropic spectral exit.

---

## 5. Relation to the compact nondegenerate ribbon lane

Earlier compact ribbon modules often assume

\[
0<c_J\le|J_\xi|\le C_J<\infty
\]

and bounded director shape.

Under those hypotheses both factors in

\[
|\nabla\xi|^2=2|J_\xi|\mathcal A_\xi
\]

are bounded, so the director-metric part of the M17-212 spectral concentration is impossible.

Therefore any hard director-metric spectral sequence must **leave the compact nondegenerate ribbon class** through either area concentration or anisotropy/rank degeneration.

---

## 6. Relation to Rank-2 area current dynamics

The material current satisfies

\[
D_BJ_\xi=(\nabla B-\tfrac32I)J_\xi.
\]

This prevents finite-time creation/destruction of a nonzero material current but does not forbid its magnitude from becoming very large across a sequence of remote states or material labels.

Thus `G_director area concentration` remains a distinct amplitude-normalized geometry branch rather than being falsely removed by the finite-time nonvanishing theorem.

---

## 7. DSD audit

- Large anisotropy is a relative-rank statement, not literal rank loss unless `s2` reaches zero.
- A bounded product plus diverging sum forces the condition number to diverge; no converse compactness is assumed.
- Large `J_xi` itself is not yet a contradiction because the current is amplitude-free and may become large near low-vorticity regions.
- The result reduces geometry; it does not provide a cumulative cost.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
