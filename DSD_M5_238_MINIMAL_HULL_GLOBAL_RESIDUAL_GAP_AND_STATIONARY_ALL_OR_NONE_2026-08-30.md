# DSD M5-238 — Minimal-Hull Global Residual Gap and Stationary All-or-None Dichotomy

Date: 2026-08-30

Parent: `DSD_M5_237_EXACT_DESCENDANT_RG_EQUATION_AND_RESIDUAL_FIRST_CORRECTION_2026-08-30.md`

Status: **COMPACT-MINIMALITY SHARPENING / THE SET OF STATIONARY CANONICAL TAILS IS CLOSED AND DILATION-INVARIANT, SO A MINIMAL TAIL HULL IS EITHER ENTIRELY STATIONARY OR CONTAINS NO STATIONARY POINT AT ALL / IN THE NONSTATIONARY CASE A CONTINUOUS GLOBAL RESIDUAL METRIC HAS A STRICT POSITIVE MINIMUM ON THE COMPACT HULL / THE RESIDUAL-ACTIVE BRANCH THEREFORE HAS A UNIFORM GLOBAL GAP FROM THE STATIONARY SET, NOT MERELY A POSITIVE-DENSITY LOCAL WITNESS / GLOBAL REGULARITY UNPROVED.**

---

## 1. Tail hull and residual

Let

\[
\mathcal T
=\mathfrak T(M)
\]

be the compact minimal canonical-tail hull obtained after M5-217/218.

The dilation flow is

\[
D_\tau T(Y)
=e^{-\tau/2}T(e^{-\tau/2}Y).
\]

Define

\[
\boxed{
\mathcal F(T)
:=
\nu\Delta T
-\mathbb P\nabla\cdot(T\otimes T).
}
\]

Then

\[
\mathcal F(T)=0
\]

is exactly the projected stationary Navier--Stokes equation on the punctured space.

---

## 2. Stationary set is closed

Use the retained punctured local topology and derivative compactness.

If

\[
T_n\to T
\]

in the tail topology and

\[
\mathcal F(T_n)=0,
\]

then local passage through viscosity and the quadratic term gives

\[
\mathcal F(T)=0.
\]

Hence

\[
\boxed{
\mathcal S_{stat}
:=
\{T\in\mathcal T:\mathcal F(T)=0\}
}
\]

is closed in `mathcal T`.

---

## 3. Stationary set is dilation invariant

Stationary Navier--Stokes is scale invariant.

If

\[
\mathcal F(T)=0,
\]

then for every `tau`,

\[
\boxed{
\mathcal F(D_\tau T)=0.
}
\]

Therefore

\[
D_\tau\mathcal S_{stat}
=\mathcal S_{stat}.
\]

So `S_stat` is a compact invariant subset of the minimal tail hull.

---

## 4. Minimality gives all or none

If

\[
\mathcal S_{stat}\ne\varnothing,
\]

then it is a nonempty closed invariant subset of `mathcal T`.

Minimality forces

\[
\boxed{
\mathcal S_{stat}=\mathcal T.
}
\]

Thus there is no mixed minimal hull containing both stationary and nonstationary tail states.

The exact dichotomy is

\[
\boxed{
\mathcal T\subset\mathcal S_{stat}
\quad\lor\quad
\mathcal T\cap\mathcal S_{stat}=\varnothing.
}
\]

The first is the large stationary fixed-force branch audited in M5-221--236.

The second is the genuinely residual-active branch.

---

## 5. Define a global residual metric

Choose a countable punctured compact exhaustion, for example

\[
K_m
=
\{2^{-m}<|Y|<2^m\},
\qquad m\ge1,
\]

with slightly enlarged cells `K_m^+` for `H^-1` testing.

Define

\[
\boxed{
\mathbf F(T)
:=
\sum_{m=1}^\infty
2^{-m}
\min\left(
1,
\|\mathcal F(T)\|_{H^{-1}(K_m^+)}
\right).
}
\]

The series converges uniformly and the local residual map is continuous, so

\[
\boxed{
\mathbf F:\mathcal T\to[0,1]
\text{ is continuous}.
}
\]

Moreover

\[
\boxed{
\mathbf F(T)=0
\iff
\mathcal F(T)=0
\text{ on }\mathbb R^3\setminus\{0\}.
}
\]

---

## 6. Uniform residual gap in the nonstationary branch

Assume

\[
\mathcal T\cap\mathcal S_{stat}=\varnothing.
\]

Then

\[
\mathbf F(T)>0
\qquad\forall T\in\mathcal T.
\]

Because `mathcal T` is compact and `F` is continuous,

\[
\boxed{
\varepsilon_{glob}
:=
\min_{T\in\mathcal T}\mathbf F(T)
>0.
}
\]

Thus

\[
\boxed{
\mathbf F(T)
\ge
\varepsilon_{glob}
\quad\forall T\in\mathcal T.
}
\]

This is stronger than the original M5-220 positive-density threshold formulation.

No state in the nonstationary minimal hull can approach the stationary set in the global residual topology.

---

## 7. Finite-annulus reduction

Choose `M` so large that

\[
\sum_{m>M}2^{-m}
<rac{\varepsilon_{glob}}2.
\]

Then for every `T in mathcal T`,

\[
\sum_{m=1}^M
2^{-m}
\min(1,\|\mathcal F(T)\|_{H^{-1}(K_m^+)})
\ge
\frac{\varepsilon_{glob}}2.
\]

Hence for every tail state there exists at least one index

\[
1\le m\le M
\]

with

\[
\boxed{
\|\mathcal F(T)\|_{H^{-1}(K_m^+)}
\ge
\varepsilon_{fin}
}
\]

for a fixed `epsilon_fin>0` depending only on `epsilon_glob` and the finite weights.

Thus the global residual gap can always be witnessed on one of finitely many normalized spatial windows.

---

## 8. Positive-density fixed-window selection

Along any invariant probability measure on the minimal hull, assign each state deterministically to the first index `m` that meets the finite residual threshold.

The finite partition has `M` cells.

Therefore at least one index `m_*` has positive invariant measure, and along a generic recurrent trajectory the corresponding residual event occurs with positive lower time/log density.

Thus one recovers a fixed-window statement

\[
\boxed{
\|\mathcal F(T(s))\|_{H^{-1}(K_{m_*}^+)}
\ge
\varepsilon_{fin}
}
\]

on a positive-density set, now as a consequence of the stronger global gap.

---

## 9. Relation to M5-237

M5-237 proves

\[
 e^h(T-\mathcal D_h)
\to
\mathcal F(T).
\]

Therefore the nonstationary minimal hull has a uniform gap in the **first descendant correction**:

\[
\boxed{
\mathbf F(T)\ge\varepsilon_{glob}>0.
}
\]

But the physical descendant correction is still multiplied by

\[
e^{-h}=R^{-2}.
\]

Hence the uniform residual gap does not by itself create a non-summable physical energy cost.

It is a rigidity/range condition, not an ordinary energy contradiction.

---

## 10. DSD verdict

The M5-220 fork sharpens to

\[
\boxed{
A_{min}^{aper}
\Longrightarrow
\begin{cases}
\textbf{S-all}:&
\mathcal F(T)=0
\text{ for every }T\in\mathcal T,\\
\textbf{R-gap}:&
\mathbf F(T)\ge\varepsilon_{glob}>0
\text{ for every }T\in\mathcal T.
\end{cases}
}
\]

There is no residual-quiet subsequence inside a genuinely nonstationary minimal hull when residual quietness is measured globally.

### Remaining tasks

- `S-all`: arbitrary-large fixed-force stationary/nondegeneracy problem;
- `R-gap`: characterize which uniformly residual-active critical tails lie in the backward-RG reconstruction range of M5-237.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]