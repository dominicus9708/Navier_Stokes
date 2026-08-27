# DSD M5-156 — Proximal Flat Branch Is Invariant-Measure Almost One-to-One

Date: 2026-08-27

Status: **P1_B^P MEASURE-THEORETIC REDUCTION / IF THE SAME-TAIL RELATION CARRIES NO OFF-DIAGONAL INVARIANT PAIR MEASURE, THEN THE CANONICAL TAIL FACTOR IS ONE-TO-ONE ALMOST EVERYWHERE FOR EVERY INVARIANT W1 MEASURE; EXCEPTIONAL PROXIMAL FIBERS MAY STILL EXIST TOPOLOGICALLY BUT THEY ARE INVISIBLE TO ALL INVARIANT-AVERAGE COCYCLE/RESIDUAL ARGUMENTS / GLOBAL REGULARITY UNPROVED.**

---

## 1. Same-tail relation

Let

\[
\pi:M\to\mathcal T,
\qquad
\pi(V)=T_V
\]

be the canonical tail factor from M5-114.

Define the relative same-tail relation

\[
\boxed{
\mathcal R
:=
M\times_{\mathcal T}M
=
\{(V,W):\pi(V)=\pi(W)\}.
}
\]

It is compact and invariant under the diagonal W1 flow.

Let

\[
\Delta:=\{(V,V):V\in M\}
\]

be the diagonal.

---

## 2. Branch-P hypothesis

Branch `P1_B^P` is the case in which there is **no statistically persistent off-diagonal fiber**:

\[
\boxed{
\rho(\mathcal R\setminus\Delta)=0
}
\]

for every invariant probability measure `rho` on the relative system `mathcal R`.

This does not assert that every fiber is a singleton.

It permits exceptional proximal/asymptotic pairs, but requires them to disappear from every invariant pair statistic.

---

## 3. Disintegrate an arbitrary invariant W1 measure

Let `mu` be any invariant probability measure on `M`.

Push it to the tail factor:

\[
\nu:=\pi_\#\mu.
\]

Disintegrate `mu` over `nu`:

\[
\boxed{
\mu
=
\int_{\mathcal T}
\mu_T\,d\nu(T),
}
\]

where `mu_T` is supported on the fiber

\[
\pi^{-1}(T)
\]

for `nu`-almost every `T`.

---

## 4. Relative independent joining

Form

\[
\boxed{
\rho_\mu
:=
\int_{\mathcal T}
\mu_T\otimes\mu_T\,d\nu(T).
}
\]

This measure is supported on `mathcal R`.

Because `mu` and `nu` are invariant and the disintegration is equivariant under the factor flow, `rho_mu` is an invariant probability measure for the diagonal relative flow.

Therefore the Branch-P hypothesis forces

\[
\boxed{
\rho_\mu(\Delta)=1.
}
\]

---

## 5. Diagonal relative product forces Dirac conditional measures

For one probability measure `m`,

\[
(m\otimes m)(\Delta)=1
\]

if and only if `m` is a Dirac mass.

Indeed, if `m` assigns positive mass to two disjoint measurable sets, then `m x m` assigns positive mass to their off-diagonal product.

Apply this fiberwise. Since

\[
1
=
\rho_\mu(\Delta)
=
\int
(\mu_T\otimes\mu_T)(\Delta)
\,d\nu(T),
\]

we obtain

\[
\boxed{
\mu_T=\delta_{V(T)}
\quad\text{for }\nu\text{-almost every }T.
}
\]

Thus

\[
\boxed{
\pi:M\to\mathcal T
\text{ is one-to-one }\mu\text{-almost everywhere.}
}
\]

The statement holds for **every invariant W1 measure `mu`**.

---

## 6. Consequence for invariant observables

Let `F` be any integrable W1 observable.

On Branch P, there exists a tail-factor observable `f_mu(T)` such that

\[
F(V)=f_\mu(T_V)
\]

for `mu`-almost every `V` after choosing the measurable inverse on the full-measure singleton-fiber set.

Hence all invariant averages may be evaluated entirely on the tail factor:

\[
\boxed{
\int_M F(V)d\mu(V)
=
\int_{\mathcal T}f_\mu(T)d\nu(T).
}
\]

This applies in particular to the critical overpay, residual, and core-tail cocycle observables whenever they are integrable.

---

## 7. Relation to M5-122

M5-122 descended the **fiber average** residual to the tail factor without assuming injectivity.

The present result is stronger on Branch P: every invariant measure sees singleton fibers almost everywhere, so conditional fiber variance vanishes `mu`-a.e.

Thus the only branch on which nontrivial fiber variance can contribute to invariant statistics is

\[
\boxed{P1_B^S.}
\]

---

## 8. What remains topologically open

The theorem does not prove that every fiber of `pi` is a singleton.

A minimal factor can in principle be an almost-one-to-one extension with exceptional proximal fibers of zero measure for every invariant measure.

Therefore Branch P remains relevant to a **pointwise topological proof of injectivity**, but it is quarantined from all measure-averaged W1 contradiction routes.

---

## 9. DSD four-chain audit

### Formation — GREEN

The relative joining is formed only inside the actual same-tail relation.

### Axis — GREEN

Topological noninjectivity and measure-theoretic noninjectivity are kept distinct.

### Static aggregation — GREEN

Exceptional fibers are not counted as positive invariant fiber mass.

### Dynamics — GREEN

Only invariant measures are used; no recurrence of an arbitrary off-diagonal pair is assumed.

### Cross-audit — GREEN

The result preserves the M5-150 split while showing that Branch P cannot contaminate invariant-average arguments.

---

## 10. Updated role of the two flat branches

\[
\boxed{
P1_B^S
=
\text{the only statistically visible noninjective flat branch},
}
\]

while

\[
\boxed{
P1_B^P
=
\text{an exceptional almost-one-to-one topological branch}.
}
\]

Accordingly the next quantitative work can focus on `P1_B^S` without silently assuming that `P1_B^P` is empty.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
