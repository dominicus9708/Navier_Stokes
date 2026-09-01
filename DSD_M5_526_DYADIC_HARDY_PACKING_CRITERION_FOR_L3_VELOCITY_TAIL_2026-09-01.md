# DSD M5-526 — Dyadic Hardy packing criterion controls the full `L3` velocity tail by critical Dirichlet shell costs

Date: 2026-09-01

Status: **DYADIC PACKING REDUCTION / M5-525 CONTROLS EACH ANNULAR VELOCITY FLUCTUATION BY SCALE-CRITICAL DIRICHLET ENERGY AND CONTROLS THE ANNULAR MEAN BY A DYADIC TELESCOPE TO INFINITY / REWRITING THE TELESCOPE WITH SHELL COSTS `b_k=R_k E_k` PRODUCES A ONE-SIDED DISCRETE HARDY CONVOLUTION WITH KERNEL `2^-m` / YOUNG'S INEQUALITY ON `ell^3` THEN GIVES `int_(|y|>R0)|U|^3 <= C sum_k b_k^(3/2)` / THUS `ell^(3/2)` PACKING OF THE SCALE-CRITICAL DIRICHLET SHELL COSTS IS A SUFFICIENT CONDITION FOR GLOBAL VELOCITY `L3` INTEGRABILITY / FAILURE OF `L3` CLOSURE IS NOW AN EXPLICIT NONSUMMABLE LOG-SCALE DIRICHLET-PACKING DEFECT, NOT AN UNTYPED LOW-FREQUENCY DRIFT / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Dyadic shell notation

Fix a sufficiently large base radius

\[
R_0>0
\]

and set

\[
R_k:=2^kR_0,
\qquad
A_k:=\{R_k<|y|<2R_k\}.
\]

For the Poincare estimates use a fixed-factor enlarged shell, for example

\[
A_k^*:=\{R_k/2<|y|<4R_k\}.
\]

Define

\[
\boxed{
E_k(\theta)
:=
\int_{A_k^*}|\nabla U(y,\theta)|^2dy
}
\]

and the scale-critical shell cost

\[
\boxed{
b_k(\theta):=R_kE_k(\theta).}
\]

Because the enlarged shells have uniformly bounded overlap,

\[
\sum_kE_k(\theta)
\le
C\|\nabla U(\theta)\|_2^2.
\]

The sequence `b_k`, however, is critical and is not summable merely from finite Dirichlet energy.

---

## 2. Annular mean difference in critical variables

Let

\[
c_k(\theta):=(U(\theta))_{A_k}.
\]

M5-525 gives

\[
|c_{k+1}-c_k|
\le
C R_k^{-1/2}E_k^{1/2}.
\]

Since

\[
E_k^{1/2}=R_k^{-1/2}b_k^{1/2},
\]

this becomes

\[
\boxed{
|c_{k+1}-c_k|
\le
C R_k^{-1}b_k^{1/2}.
}
\]

M5-523 gives `c_k -> 0` uniformly as `k->infinity`, so telescope from scale `k` to infinity:

\[
|c_k|
\le
C\sum_{j=k}^\infty R_j^{-1}b_j^{1/2}.
\]

Since

\[
R_j=2^{j-k}R_k,
\]

we obtain

\[
\boxed{
R_k|c_k|
\le
C\sum_{m=0}^\infty
2^{-m}b_{k+m}^{1/2}.
}
\]

Thus the broad velocity mean is a discrete Hardy convolution of the critical Dirichlet shell costs.

---

## 3. Fluctuation contribution to annular `L3`

Scale-invariant Sobolev--Poincare gives

\[
\|U-c_k\|_{L^6(A_k)}
\le
C E_k^{1/2}.
\]

By Holder and `|A_k|~R_k^3`,

\[
\|U-c_k\|_{L^3(A_k)}
\le
C R_k^{1/2}E_k^{1/2}
=
C b_k^{1/2}.
\]

Therefore

\[
\boxed{
\int_{A_k}|U-c_k|^3dy
\le
C b_k^{3/2}.
}
\]

---

## 4. Mean contribution to annular `L3`

The constant mean contributes

\[
\|c_k\|_{L^3(A_k)}
\asymp
R_k|c_k|.
\]

Using Section 2,

\[
\boxed{
\|c_k\|_{L^3(A_k)}
\le
C
\sum_{m=0}^\infty
2^{-m}b_{k+m}^{1/2}.
}
\]

Hence

\[
\boxed{
\int_{A_k}|c_k|^3dy
\le
C
\left(
\sum_{m=0}^\infty
2^{-m}b_{k+m}^{1/2}
\right)^3.
}
\]

Combining mean and fluctuation,

\[
\boxed{
\int_{A_k}|U|^3dy
\le
C b_k^{3/2}
+
C
\left(
\sum_{m=0}^\infty
2^{-m}b_{k+m}^{1/2}
\right)^3.
}
\]

---

## 5. Discrete Hardy--Young estimate

Set

\[
x_k:=b_k^{1/2}
\]

and the one-sided kernel

\[
K_m:=2^{-m},
\qquad m\ge0.
\]

Then the mean term is

\[
(K*x)_k
:=
\sum_{m\ge0}K_mx_{k+m}.
\]

Since

\[
K\in\ell^1,
\qquad
\|K\|_{\ell^1}=2,
\]

Young's convolution inequality gives

\[
\|K*x\|_{\ell^3}
\le
\|K\|_{\ell^1}\|x\|_{\ell^3}.
\]

Therefore

\[
\boxed{
\sum_k
\left(
\sum_{m\ge0}2^{-m}b_{k+m}^{1/2}
\right)^3
\le
C\sum_kb_k^{3/2}.
}
\]

---

## 6. Full tail `L3` packing theorem

Summing the annular estimate over disjoint dyadic shells gives

\[
\boxed{
\int_{|y|>R_0}|U(y,\theta)|^3dy
\le
C
\sum_{k=0}^\infty
b_k(\theta)^{3/2}.
}
\]

Thus

\[
\boxed{
\{b_k(\theta)\}\in\ell^{3/2}
\Longrightarrow
U(\theta)\in L^3(\mathbb R^3).
}
\]

The bounded interior ball contributes a finite `L3` amount automatically on the smooth compact hull.

---

## 7. Uniform version on the compact hull

If

\[
\boxed{
\sup_{\theta}
\sum_{k\ge0}b_k(\theta)^{3/2}
<\infty,
}
\]

then

\[
\boxed{
\sup_\theta\|U(\theta)\|_3<\infty.
}
\]

Because `L3` is Navier--Stokes scale invariant, for the associated ancient physical solution

\[
\mathcal V(x,s)
=(-s)^{-1/2}
U\left(\frac{x}{\sqrt{-s}},-\log(-s)\right)
\]

we have

\[
\boxed{
\|\mathcal V(s)\|_3
=
\|U(\theta)\|_3.
}
\]

Hence a uniform packing bound becomes a uniform critical `L3` bound along that ancient orbit.

This fact is recorded here, but its implication for the original hypothetical singular solution requires a separate ancestry/terminal-transfer audit.

---

## 8. What finite Dirichlet energy does not give

Finite Dirichlet energy controls

\[
\sum_kE_k<\infty.
\]

But

\[
b_k=R_kE_k.
\]

For example the critical pattern

\[
E_k\asymp R_k^{-1}
\]

is perfectly summable because `R_k` grows geometrically, while

\[
b_k\asymp1.
\]

Then

\[
\sum_kb_k^{3/2}=\infty.
\]

Therefore the new packing condition is genuinely stronger than finite enstrophy/Dirichlet energy.

---

## 9. Subcritical but nonsummable packing remains possible

Even the M5-525 condition

\[
b_k\to0
\]

or its cumulative-tail analogue does not imply

\[
\sum_kb_k^{3/2}<\infty.
\]

For example

\[
b_k\asymp k^{-2/3}
\]

has

\[
b_k\to0
\]

but

\[
\sum_kb_k^{3/2}
\asymp
\sum_kk^{-1}
=\infty.
\]

Thus the remaining obstruction can be genuinely diffuse over logarithmic radius rather than supported on shells with a fixed positive lower cost.

---

## 10. Exact low-frequency packing dichotomy

The compact smooth branch now splits into

\[
\boxed{
\mathcal P_{Dir}^{3/2}
\lor
H_{Dir}^{nonsum},
}
\]

where

\[
\boxed{
\mathcal P_{Dir}^{3/2}:
\sup_\theta\sum_kb_k(\theta)^{3/2}<\infty
}
\]

implies uniform `L3`, while

\[
\boxed{
H_{Dir}^{nonsum}:
\text{the critical shell sequence fails uniform }\ell^{3/2}\text{ packing}.
}
\]

The second branch includes both

1. fixed-amplitude critical shell recurrence; and
2. subcritical-per-shell but nonsummable logarithmic occupation.

---

## 11. Relation to the terminal dilation genealogy

M5-481--483 produced a critical terminal Dirichlet tail and a complete dilation genealogy whose scale factors stay in a compact interval bounded away from one and infinity.

M5-526 shows that the only low-frequency obstruction to uniform velocity `L3` on the interior recurrent hull is likewise a log-scale packing failure of scale-critical Dirichlet shell costs.

Thus the two hard objects now use the same critical currency:

\[
\boxed{
R\int_{A_R}|\nabla U|^2.
}
\]

They are still not identified automatically, because the M5-481 quantity lives on terminal blow-down states whereas `b_k(theta)` lives on interior similarity states.

The next audit should determine whether the exact dilation genealogy transports nonsummable critical shell packing between these two representations.

---

## 12. DSD audit

M5-526 establishes a **sufficient** packing criterion for `L3`.

It does not claim the converse

\[
U\in L^3
\Longrightarrow
\{b_k\}\in\ell^{3/2}.
\]

Nor does it claim that failure of `ell^(3/2)` packing implies singularity.

The result only identifies the remaining low-frequency obstruction in a quantitatively explicit dyadic form.

---

## 13. Highest-value next targets

Two tasks now have unusually high leverage.

### P1 — Packing recurrence

Use the M5-482--485 dilation genealogy to determine whether `H_Dir^(nonsum)` must contain a recurrent positive-density family of critically occupied shells, rather than an arbitrarily diffuse sequence such as `b_k~k^(-2/3)`.

### P2 — Uniform `L3` transfer audit

On the `P_Dir^(3/2)` branch, audit exactly what

\[
\sup_\theta\|U(\theta)\|_3<\infty
\]

implies for

1. the second-generation ancient cell;
2. the first ancient element;
3. the original hypothetical first singular solution.

No Escauriaza--Seregin--Sverak or related endpoint theorem should be imported before that ancestry map is verified.

---

## 14. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
