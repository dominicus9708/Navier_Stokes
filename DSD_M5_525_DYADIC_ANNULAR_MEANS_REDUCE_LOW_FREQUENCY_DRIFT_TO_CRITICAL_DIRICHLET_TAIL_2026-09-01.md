# DSD M5-525 — Dyadic annular means reduce the low-frequency velocity drift to a critical Dirichlet tail

Date: 2026-09-01

Status: **LOW-FREQUENCY/DIRICHLET RECONNECTION / GLOBAL `L2` COMPACTNESS OF THE VORTICITY HULL PASSES THROUGH THE RIESZ TRANSFORMS TO GLOBAL `L2` COMPACTNESS AND UNIFORM SPATIAL TIGHTNESS OF `grad U` / DYADIC POINCARE ESTIMATES THEN CONTROL THE DIFFERENCE OF VELOCITY MEANS ON ADJACENT LARGE ANNULI / TELESCOPE TO INFINITY USING M5-523'S UNIFORM `U->0` TO OBTAIN `|(U)_{A_R}| <= C R^(-1/2) epsilon_D(R/2)^(1/2)` / SOBOLEV--POINCARE CONTROLS THE FLUCTUATION AROUND THAT MEAN AND YIELDS `int_{A_R}|U|^3 <= C (R epsilon_D(R/2))^(3/2)` / THEREFORE THE LOW-FREQUENCY/L3 OBSTRUCTION IS NOW TIED TO THE SCALE-CRITICAL DIRICHLET TAIL `R epsilon_D(R)` RATHER THAN AN UNTYPED GALILEAN DRIFT / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Dirichlet field as a Riesz transform of vorticity

For a divergence-free whole-space velocity with the Galilean constant fixed,

\[
\nabla U
\]

is obtained from

\[
W=\nabla\times U
\]

by Calderon--Zygmund/Riesz transforms.

Thus there is a bounded linear map on `L2`, schematically

\[
\boxed{
\nabla U=\mathcal R W.
}
\]

M5-508 gives global strong precompactness of the vorticity hull in `L2(R3)`.

A bounded linear map sends a precompact set to a precompact set.

Therefore

\[
\boxed{
\{\nabla U:\ U\in\widehat{\mathfrak H}\}
\text{ is precompact in }L^2(\mathbb R^3).
}
\]

---

## 2. Precompactness implies uniform Dirichlet tightness

Every compact subset of `L2(R3)` is uniformly spatially tight.

Indeed, for any `eta>0`, cover the compact set by finitely many `L2` balls of radius `eta`; choose one large spatial radius making the exterior `L2` tail of every center small, then use the triangle inequality.

Hence define

\[
\boxed{
\varepsilon_D(R)
:=
\sup_{\widehat{\mathfrak H}}
\int_{|y|>R}|\nabla U(y)|^2dy.
}
\]

Then

\[
\boxed{
\varepsilon_D(R)\to0
\quad(R\to\infty).
}
\]

This is stronger than merely having a uniform global Dirichlet bound.

---

## 3. Dyadic annular means

Let

\[
A_R:=\{R<|y|<2R\}
\]

and define the annular mean

\[
\boxed{
c_R:=(U)_{A_R}
=\frac1{|A_R|}\int_{A_R}U(y)dy.
}
\]

M5-523 gives

\[
\sup_{\widehat{\mathfrak H}}\sup_{|y|>R}|U(y)|\to0.
\]

Therefore

\[
\boxed{c_R\to0}
\]

uniformly along `R->infinity`.

This supplies the terminal value needed for a dyadic telescoping argument.

---

## 4. Adjacent means differ only by annular Dirichlet energy

Consider the connected thick annulus

\[
D_R:=\{R<|y|<4R\}
\]

and let `c_D` be the mean of `U` on `D_R`.

Scale-invariant Sobolev--Poincare gives

\[
\boxed{
\|U-c_D\|_{L^6(D_R)}
\le
C\|\nabla U\|_{L^2(D_R)}.
}
\]

For the inner annulus,

\[
\begin{aligned}
|c_R-c_D|
&\le
\frac1{|A_R|}
\int_{A_R}|U-c_D|dy\\
&\le
|A_R|^{-1/6}
\|U-c_D\|_{L^6(D_R)}\\
&\le
C R^{-1/2}
\|\nabla U\|_{L^2(D_R)}.
\end{aligned}
\]

The same estimate holds for `c_(2R)`.

Therefore

\[
\boxed{
|c_{2R}-c_R|
\le
C R^{-1/2}
\left(
\int_{R<|y|<4R}|\nabla U|^2dy
\right)^{1/2}.
}
\]

---

## 5. Telescope the mean to infinity

Apply Section 4 at scales

\[
R,2R,4R,\ldots
\]

and use

\[
c_{2^kR}\to0.
\]

Then

\[
|c_R|
\le
\sum_{k=0}^\infty
|c_{2^{k+1}R}-c_{2^kR}|.
\]

Let

\[
E_k
:=
\int_{2^kR<|y|<2^{k+2}R}
|\nabla U|^2dy.
\]

The overlap multiplicity of these thick annuli is bounded universally.

Hence

\[
\begin{aligned}
|c_R|
&\le
C R^{-1/2}
\sum_{k\ge0}
2^{-k/2}E_k^{1/2}\\
&\le
C R^{-1/2}
\left(\sum_{k\ge0}2^{-k}\right)^{1/2}
\left(\sum_{k\ge0}E_k\right)^{1/2}.
\end{aligned}
\]

Using bounded overlap and Dirichlet tightness,

\[
\sum_kE_k
\le
C\varepsilon_D(R).
\]

Thus

\[
\boxed{
|c_R|
\le
C R^{-1/2}\varepsilon_D(R)^{1/2}.
}
\]

After harmless radius shifts from cutoff/overlap conventions, we may record the robust form

\[
\boxed{
|c_R|
\le
C R^{-1/2}\varepsilon_D(R/2)^{1/2}.
}
\]

---

## 6. Control the fluctuation around the annular mean

Sobolev--Poincare directly on a fixed enlargement of `A_R` gives

\[
\boxed{
\|U-c_R\|_{L^6(A_R)}
\le
C
\|\nabla U\|_{L^2(A_R^*)},
}
\]

where `A_R^*` is a fixed-factor enlarged annulus.

By Holder,

\[
\begin{aligned}
\|U-c_R\|_{L^3(A_R)}
&\le
|A_R|^{1/6}
\|U-c_R\|_{L^6(A_R)}\\
&\le
C R^{1/2}
\varepsilon_D(R/2)^{1/2}.
\end{aligned}
\]

The constant mean part satisfies

\[
\|c_R\|_{L^3(A_R)}
=|A_R|^{1/3}|c_R|
\le
C R\cdot R^{-1/2}
\varepsilon_D(R/2)^{1/2}.
\]

Therefore

\[
\boxed{
\|U\|_{L^3(A_R)}
\le
C R^{1/2}
\varepsilon_D(R/2)^{1/2}.
}
\]

Cubing,

\[
\boxed{
\int_{A_R}|U|^3dy
\le
C
\big(R\,\varepsilon_D(R/2)\big)^{3/2}.
}
\]

---

## 7. The critical Dirichlet tail parameter

Define

\[
\boxed{
\mathfrak D(R)
:=
R\,\varepsilon_D(R/2).
}
\]

Then M5-525 gives the direct estimate

\[
\boxed{
\sup_{\widehat{\mathfrak H}}
\int_{A_R}|U|^3dy
\le
C\mathfrak D(R)^{3/2}.
}
\]

Therefore the large-scale velocity `L3` obstruction is controlled by one scale-critical Dirichlet quantity.

---

## 8. Exact tail dichotomy

There are two alternatives.

### Subcritical Dirichlet tail

\[
\boxed{
\mathfrak D(R)\to0.
}
\]

Then

\[
\boxed{
\sup_{\widehat{\mathfrak H}}
\int_{A_R}|U|^3dy
\to0.
}
\]

Thus every sufficiently remote dyadic annulus becomes individually small in critical `L3` mass.

### Critical Dirichlet tail

Otherwise there exist

\[
R_n\to\infty,
\qquad
d_*>0
\]

such that

\[
\boxed{
R_n
\sup_{\widehat{\mathfrak H}}
\int_{|y|>R_n/2}|\nabla U|^2dy
\ge d_*.
}
\]

This is a scale-critical remote Dirichlet tail.

Thus

\[
\boxed{
H_{low}^{velocity}
\Longrightarrow
T_{Dir}^{crit}
\lor
\text{annular-}L^3\text{ vanishing}.
}
\]

---

## 9. Relation to M5-481 terminal Dirichlet tail

M5-481 independently forced, on the regular terminal bounded-amplitude branch,

\[
R_m
\int_{aR_m<|x|<bR_m}
|\nabla V(x,0)|^2dx
\ge g_*>0
\]

along selected terminal record scales.

M5-525 produces the same scale-critical derivative order from the **interior recurrent similarity low-frequency audit**.

The two statements are not yet identical: one concerns the terminal physical tail of the first ancient element, while the other concerns large-radius tails inside members of the recurrent similarity hull.

However the former structural adjacency noted in M5-502 is now sharper:

\[
\boxed{
\text{failure of subcritical velocity decay}
\to
\text{critical Dirichlet occupancy at large similarity radius}.
}
\]

This is precisely the observable already carried by the terminal dilation genealogy.

---

## 10. Annular `L3` vanishing is not yet global `L3`

The condition

\[
\int_{A_R}|U|^3\to0
\]

on each remote annulus does not imply

\[
U\in L^3(\mathbb R^3).
\]

Infinitely many annuli may carry individually small but nonsummable critical mass.

Thus Chae's `L3` periodic-profile theorem still cannot be imported solely from

\[
\mathfrak D(R)\to0.
\]

A summability or packing improvement is required.

This is the next exact low-frequency obstruction.

---

## 11. DSD interpretation

The broad low-frequency velocity tail is no longer an arbitrary shellwise Galilean ambiguity.

Adjacent shell means cannot change independently because their difference is priced by Dirichlet energy.

After telescoping to the vanishing far-field velocity, the annular mean itself is priced by the cumulative exterior Dirichlet tail.

Thus

\[
\boxed{
\text{low-frequency drift}
\to
\text{Dirichlet tail budget}.
}
\]

This reconnects the low-frequency analysis to the existing derivative/dilation genealogy rather than introducing a new unrelated channel.

---

## 12. Highest-value next target

The remaining subcritical branch has

\[
\mathfrak D(R)\to0
\]

and hence remote annular `L3` mass tending to zero, but possibly nonsummably.

The next target is a **dyadic packing audit**.

Let

\[
a_k
:=
2^kR_0
\int_{|y|>2^{k-1}R_0}|\nabla U|^2dy.
\]

Determine whether the dilation recurrence / finite-lineage genealogy forces enough decay or bounded variation of `a_k` to make

\[
\sum_k a_k^{3/2}<\infty.
\]

If so, M5-525 would upgrade to

\[
U\in L^3
\]

on periodic/recurrent components, activating existing critical regularity/Liouville theory.

If not, the failure becomes a logarithmically occupied critical Dirichlet-tail cascade, which should reconnect directly to the M5-481--483 dilation hull.

---

## 13. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
