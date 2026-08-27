# DSD M5-97 — Positive-Crossing Regular-Component Extraction

Date: 2026-08-27

Status: **COAREA/SARD REPAIR OF THE M5-92->M5-93 INTERFACE / A POSITIVE FIXED-BAND CROSSING INTEGRAL SELECTS A POSITIVE-MEASURE FAMILY OF REGULAR AMPLITUDE LEVELS AND AT LEAST ONE BOUNDED CONNECTED SUPERLEVEL COMPONENT WITH NONZERO CROSSING / NO TOPOLOGY-PERSISTENCE ASSUMPTION IS NEEDED / GLOBAL REGULARITY UNPROVED.**

---

## 1. The interface to be repaired

M5-93 uses a limiting returned upstroke satisfying

\[
T_w[U_*]>0
\]

and, under a contradiction sequence,

\[
G_w[U_*]=0.
\]

M5-92 excludes a nontrivial bounded smooth `G=0` crossing configuration on a regular positive-amplitude component.

The missing logical edge was:

\[
\boxed{
T_w>0
\quad\Longrightarrow\quad
\text{there exists a bounded regular level component carrying nonzero crossing}.
}
\]

This memo proves that edge directly in the limiting state.

---

# 2. Formation chain — fixed positive amplitude band

Let

\[
a:=|U|,
\]

and let the fixed mollifier satisfy

\[
\operatorname{supp}w
\subset I=[\lambda_-,\lambda_+]\Subset(0,\infty).
\]

On the W1 returned pump cell, the positive-band localization gives a radius `R_w` such that

\[
|Y|>R_w
\quad\Longrightarrow\quad
a(Y)<\lambda_-/2.
\]

Hence every superlevel set with

\[
\lambda\in I
\]

is spatially bounded:

\[
\boxed{
\{a>\lambda\}\Subset B_{R_w}.
}
\]

The same statement passes to every local smooth W1 limit used in M5-93.

Thus a selected positive-band component cannot escape to spatial infinity.

---

# 3. Axial chain — exact coarea representation of T

Recall

\[
T_w
:=
\int
w(a)\frac{|U\cdot\nabla a|^2}{a}\,dY.
\]

For every regular value `lambda`, write

\[
\Gamma_{\lambda,k}
:=\partial\Omega_{\lambda,k},
\]

where

\[
\{a>\lambda\}
=\bigsqcup_k\Omega_{\lambda,k}.
\]

At regular points set

\[
n=\frac{\nabla a}{|\nabla a|}.
\]

Then

\[
U\cdot\nabla a
=|\nabla a|\,U\cdot n.
\]

Coarea therefore gives

\[
\boxed{
T_w
=
\int_{\lambda_-}^{\lambda_+}
\frac{w(\lambda)}{\lambda}
\sum_k
\int_{\Gamma_{\lambda,k}}
|\nabla a|\,|U\cdot n|^2\,dS\,d\lambda.
}
\]

Define the nonnegative level crossing density

\[
\boxed{
\tau(\lambda)
:=
\sum_k
\int_{\Gamma_{\lambda,k}}
\frac{|\nabla a|}{\lambda}|U\cdot n|^2\,dS.
}
\]

Then

\[
\boxed{T_w=\int w(\lambda)\tau(\lambda)d\lambda.}
\]

---

# 4. Critical points do not hide positive T

At every critical point of the amplitude,

\[
\nabla a=0,
\]

hence pointwise

\[
U\cdot\nabla a=0.
\]

Thus the volume integrand defining `T_w` is zero on the critical set itself.

Moreover, for the smooth amplitude field on the positive band, Sard's theorem implies that the set of critical values has one-dimensional Lebesgue measure zero.

Consequently a positive value

\[
T_w>0
\]

cannot be supported only on critical amplitude values.

There must be a positive-measure set of regular values inside the region where `w(lambda)>0` for which

\[
\boxed{\tau(\lambda)>0.}
\]

---

# 5. Static aggregation — select one connected component

Fix one such regular value `lambda`.

Because

\[
\tau(\lambda)
=
\sum_k	au_k(\lambda)>0,
\]

where

\[
\tau_k(\lambda)
:=
\int_{\Gamma_{\lambda,k}}
\frac{|\nabla a|}{\lambda}|U\cdot n|^2\,dS\ge0,
\]

at least one connected superlevel component satisfies

\[
\boxed{
\tau_k(\lambda)>0.
}
\]

The collection of connected components is at most countable because each open component contains a rational point.

Since `lambda>=lambda_->0` and the positive-band superlevel is contained in `B_{R_w}`, this selected component is bounded:

\[
\boxed{
\Omega_{\lambda,k}\Subset B_{R_w}.
}
\]

Its regular boundary carries genuine crossing on a positive surface-measure subset.

---

# 6. Apply the exact G=0 limit without topology persistence

Suppose now that the limiting state also satisfies

\[
G_w=0,
\]

where

\[
G_w
=
\int
\frac{w(a)}a
|U\times\nabla a|^2\,dY.
\]

Since the integrand is nonnegative and the fields are smooth, on the open active region where

\[
w(a)>0
\]

we have

\[
\boxed{U\times\nabla a=0.}
\]

Select the regular value `lambda` above from the interior set where `w(lambda)>0`.

Then on its selected bounded component boundary,

\[
U\parallel\nabla a
\]

and the component has nonzero normal crossing by `tau_k(lambda)>0`.

This is exactly the statewise configuration excluded by M5-92.

Crucially, the component was selected **after taking the limiting state**.

No assertion is made that a component label or topology from the approximating sequence persists into the limit.

---

# 7. Dynamical chain — consequence for M5-93

On the robust returned upstroke class M5-93 supplies a uniform crossing floor

\[
T_w\ge T_*>0.
\]

Assume for contradiction that

\[
G_{w,n}\to0.
\]

Local smooth compactness yields a limit `U_*` with

\[
T_w[U_*]\ge T_*>0,
\qquad
G_w[U_*]=0.
\]

The present coarea/Sard lemma selects, directly in `U_*`, a bounded regular positive-crossing component.

M5-92 excludes that component.

Therefore the compactness contradiction is complete and

\[
\boxed{
G_w\ge G_*>0
}
\]

on a sufficiently small compact returned upstroke neighborhood.

---

# 8. DSD four-chain audit

## Formation — GREEN

The regular component is formed from the limit state itself. No historical component identity is inherited by assumption.

## Axial property — GREEN

The signed normal crossing is converted to a nonnegative level density through the exact coarea projection.

## Static aggregation — GREEN

Positive total level density forces at least one positive connected-component density; no cancellation can hide it because the density is quadratic.

## Dynamics — GREEN

Compactness is used only to produce the limiting smooth state and retain `T>0,G=0`. The regular component is then selected statewise.

## Cross-audit — GREEN

Critical topology changes in the approximating sequence do not affect the conclusion because neither component labels nor regular values are transported through the sequence.

---

# 9. Repair verdict

The M5-92 statewise zero-angular-gap obstruction and the M5-93 compactness promotion are now connected without a hidden topology-persistence hypothesis.

Thus, inside the W1-conditional returned pump class,

\[
\boxed{G_w\ge G_*>0}
\]

is promoted from YELLOW to GREEN.

Together with M5-96, the two technical W1 interfaces isolated by M5-95 are repaired.

The next task is not yet to compute R1/R2, but to freeze the repaired dependency graph and state precisely what is stable internally and what remains an upstream GLOBAL obligation.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
