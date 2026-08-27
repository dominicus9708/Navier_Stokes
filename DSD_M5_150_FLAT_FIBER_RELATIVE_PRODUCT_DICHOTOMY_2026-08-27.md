# DSD M5-150 — Flat-Fiber Relative-Product Dichotomy

Date: 2026-08-27

Status: **DSD DYNAMICAL SPLIT FOR P1_B / THE SAME-TAIL RELATION IS A COMPACT INVARIANT RELATIVE PRODUCT; ANY NONINJECTIVE FLAT FIBER MUST EITHER SUPPORT AN INVARIANT PAIR MEASURE WITH POSITIVE OFF-DIAGONAL MASS OR BE PURELY PROXIMAL-IN-MEAN WITH ALL INVARIANT PAIR MEASURES SUPPORTED ON THE DIAGONAL / ONLY THE FIRST BRANCH MAY USE INVARIANT PAIR AVERAGING / GLOBAL REGULARITY UNPROVED.**

---

## 1. Relative product over the canonical tail factor

Let

\[
\pi:M\to\mathcal T,
\qquad
\pi(V)=T_V
\]

be the continuous canonical tail factor from M5-114/M5-118.

Define

\[
\boxed{
\mathcal R
:=
M\times_{\mathcal T}M
=
\{(V,W)\in M\times M:\pi(V)=\pi(W)\}.
}
\]

Because `pi` is continuous and `M` compact, `R` is compact.

Tail covariance gives

\[
\pi(S_hV)=D_h\pi(V),
\]

so

\[
(V,W)\in\mathcal R
\Rightarrow
(S_hV,S_hW)\in\mathcal R.
\]

Thus `R` is invariant under the pair flow.

The diagonal

\[
\Delta:=\{(V,V):V\in M\}
\]

is a closed invariant subset.

---

## 2. Noninjectivity means an off-diagonal point

The tail factor is noninjective iff

\[
\mathcal R\setminus\Delta\ne\varnothing.
\]

By M5-145 every such off-diagonal pair has a difference that is Fuchsian-flat to every algebraic order.

However off-diagonal existence does **not** imply the existence of an off-diagonal recurrent pair.  A pair orbit may approach the diagonal in its long-time statistics.

This distinction must be preserved before using recurrence or invariant averaging.

---

## 3. Branch S — statistical/non-diagonal invariant fiber

Take an invariant Borel probability measure `rho` on `R`.

Call the branch statistical/non-diagonal if there exists such a measure with

\[
\boxed{
\rho(\mathcal R\setminus\Delta)>0.
}
\]

Equivalently, for a continuous pair-separation observable such as

\[
d_2(V,W):=\min\{1,\|V-W\|_{L^2}\},
\]

one has

\[
\boxed{
\int_{\mathcal R}d_2(V,W)\,d\rho>0.
}
\]

On this branch, pair-flow invariance provides a legitimate stationary averaging device for genealogical/time derivatives.

This is the branch on which inverse-Fuchsian normal energy identities may be averaged without assuming recurrence of one arbitrarily chosen pair.

---

## 4. Branch P — purely proximal-in-mean fiber

Suppose instead that

\[
\boxed{
\rho(\mathcal R\setminus\Delta)=0
\quad\text{for every invariant probability measure }\rho\text{ on }\mathcal R.
}
\]

Then every invariant pair measure is supported on the diagonal.

For any off-diagonal pair `(V,W)` and any sequence of empirical pair measures

\[
\rho_H:=\frac1H\int_0^H
\delta_{(S_hV,S_hW)}\,dh,
\]

every weak limit is invariant and therefore diagonal-supported.

Hence for every continuous nonnegative separation observable `d` vanishing exactly on `Delta`,

\[
\boxed{
\frac1H\int_0^H d(S_hV,S_hW)\,dh\to0.
}
\]

Thus noninjectivity, if present, is invisible to invariant statistics and survives only as a proximal/mean-contracting topological extension.

---

## 5. Why the split matters

A calculation such as

\[
\langle Z,\partial_\eta Z\rangle=0
\]

requires an invariant averaging framework.

It is valid on Branch S after averaging under an invariant pair measure, but cannot be imposed on one arbitrary off-diagonal pair in Branch P.

Conversely, Branch P cannot be excluded merely because no non-diagonal invariant pair measure exists; proximal extensions of minimal systems are a genuine dynamical possibility.

---

## 6. DSD four-chain audit

### Formation — GREEN

The relative product is formed from the already continuous tail factor.  No new pair recurrence is assumed.

### Axis — GREEN

Single-state recurrence and pair recurrence are kept distinct.

### Static aggregation — GREEN

Off-diagonal existence is not counted as positive invariant off-diagonal mass.

### Dynamics — GREEN

Invariant-measure averaging is used only on Branch S.  Branch P is explicitly retained.

### Cross-audit — GREEN

This prevents the earlier diagonal-limit/proximal error from reappearing under the stronger flat-fiber formulation.

---

## 7. Updated P1_B tree

\[
\boxed{
P1_B
=
P1_B^{S}
\ \lor\ 
P1_B^{P},
}
\]

where

- `P1_B^S`: a statistically persistent non-diagonal flat fiber;
- `P1_B^P`: a purely proximal-in-mean noninjective flat fiber.

The next calculation attacks `P1_B^S` by invariant-pair averaging of the pressure-free vorticity normal equation.

`P1_B^P` remains a separate backward/proximal uniqueness gate and must not be used as input to that calculation.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]