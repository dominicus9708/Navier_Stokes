# DSD M5-111 — Quantitative Annular Observability Gate

Date: 2026-08-27

Status: **W1-CONDITIONAL OBSERVABILITY AUDIT / A FIXED OPEN ANNULUS OBSERVATION IS QUALITATIVELY INJECTIVE ON THE ANALYTIC MINIMAL W1 SET / COMPACTNESS GIVES AN INVERSE MODULUS FOR EACH FIXED R / THE RADIAL-GENEALOGY ERROR IS O(R^-1/2), BUT NO UNIFORM COMPARISON WITH THE INVERSE MODULUS IS PROVED / QUALITATIVE UNIQUE CONTINUATION MUST NOT BE USED AS QUANTITATIVE TAIL-TO-CORE DECODING / GLOBAL REGULARITY UNPROVED.**

---

## 1. Motivation

M5-109 proved that the nonzero cubic residue forces a recurrent payer inside one fixed normalized core.

The older log-radius genealogy theorem gives, for the complete W1 trajectory,

\[
\left\|
\mathcal F_{Re^\rho}[V_0]
-
\mathcal F_R[V(-2\rho)]
\right\|_{L^3(A)}
\le CR^{-1/2}
\]

uniformly in `rho>=0`, where

\[
\mathcal F_R[V](z)=RV(Rz),
\qquad 1<|z|<2.
\]

It is tempting to conclude that the far shell therefore determines the entire ancestor state and hence its core payer.

That conclusion requires a quantitative inverse estimate and is not automatic.

---

## 2. Fixed-annulus observation map

Let `M` be the compact minimal W1 set.

For fixed finite `R>0`, define

\[
\boxed{
\mathcal O_R:M\to L^3(A),
\qquad
\mathcal O_R(V):=RV(R\cdot)|_A.
}
\]

Local smooth W1 compactness makes `O_R` continuous.

---

## 3. Qualitative injectivity

Every W1 state is spatially real analytic on finite regions at the retained smooth times.

If

\[
\mathcal O_R(V_1)=\mathcal O_R(V_2)
\]

in `L^3(A)`, then the analytic vector fields agree almost everywhere, hence everywhere, on the open physical annulus

\[
R<|Y|<2R.
\]

Real-analytic continuation on connected `R^3` gives

\[
\boxed{V_1=V_2.}
\]

Therefore

\[
\boxed{\mathcal O_R\text{ is injective for every fixed finite }R.}
\]

---

## 4. Compactness gives a fixed-R inverse modulus

Fix any metric `d_M` generating the retained compact W1 topology.

For `epsilon>0`, define the shell-separation modulus

\[
\boxed{
\delta_R(\epsilon)
:=
\inf
\left\{
\|\mathcal O_R(V)-\mathcal O_R(W)\|_{L^3(A)}:
V,W\in M,
\ d_M(V,W)\ge\epsilon
\right\}.
}
\]

The constraint set is compact.

Injectivity implies

\[
\boxed{\delta_R(\epsilon)>0}
\]

for every fixed `R<infinity` and every `epsilon>0`.

Equivalently, `O_R^{-1}` is uniformly continuous on the compact image `O_R(M)`.

---

## 5. The missing comparison

The genealogy theorem does not give exact shell equality.

It gives the error scale

\[
\boxed{e_R:=CR^{-1/2}.}
\]

To reconstruct an ancestor state to `d_M` accuracy `epsilon`, one would need

\[
\boxed{
e_R<\delta_R(\epsilon).
}
\]

The fixed-R compactness argument proves only

\[
\delta_R(\epsilon)>0.
\]

It does **not** give a lower bound on how `delta_R(epsilon)` behaves as

\[
R\to\infty.
\]

The inverse problem may become arbitrarily ill-conditioned at large radius.

Thus no implication of the form

\[
CR^{-1/2}\to0
\quad\Longrightarrow\quad
\text{core reconstruction error}\to0
\]

is currently justified.

---

## 6. Why qualitative analyticity is insufficient

Analytic continuation is notoriously unstable as a quantitative inverse problem.

Two uniformly analytic states may differ by order one in the core while their difference on a remote annulus is extremely small.

Therefore the facts

\[
\mathcal O_R\text{ injective}
\]

and

\[
e_R\to0
\]

cannot be combined without controlling the conditioning of `O_R^{-1}`.

This is exactly the kind of hidden implication that the DSD algorithmic audit is designed to prevent.

---

## 7. Observability branch split

For any fixed state tolerance `epsilon_*>0`, compare

\[
\delta_R(\epsilon_*)
\]

with

\[
e_R=CR^{-1/2}.
\]

### O1 — quantitatively observable tail

There exist arbitrarily large `R` for which

\[
\boxed{
CR^{-1/2}
<
\frac12\delta_R(\epsilon_*).
}
\]

Then the genealogy shell determines the ancestor state to accuracy smaller than `epsilon_*`.

Every continuous core observable, including the M5-109 payer, becomes robustly readable from the corresponding far-shell pattern.

### O2 — asymptotically ill-conditioned tail

For all sufficiently large `R`,

\[
\boxed{
\delta_R(\epsilon_*)
\lesssim
R^{-1/2}.
}
\]

Then order-one-distinct core states can become shell-indistinguishable at or below the same scale as the genealogy error.

In this branch the passive far tail is an information-losing factor of the full core dynamics at the available quantitative resolution.

Neither branch is presently excluded.

---

## 8. Relation to the core payer

Let

\[
\mathcal H_{core}(V)
:=
\mathcal H_{3,R_*}(V)
\]

be the continuous fixed-core payer from M5-109.

In O1, uniform continuity of

\[
\mathcal H_{core}\circ\mathcal O_R^{-1}
\]

on `O_R(M)` implies that sufficiently accurate far-shell genealogy reproduces the payer/no-payer distinction of the ancestor state.

Thus the static tail becomes a quantitative radial record of the recurrent payer history.

In O2, this conclusion is unavailable.

The tail may retain critical cubic height while losing quantitative information about which core payer state generated the historical phase.

---

## 9. DSD four-chain audit

### Formation

The observation map and its inverse modulus are defined before any decoding claim.

### Axis

Remote shell accuracy and core-state accuracy are different channels and are related only through `delta_R`.

### Static aggregation

Qualitative injectivity is not added to a vanishing shell error as if they were numerical bounds.

### Dynamics

The genealogy error is inserted only after the fixed-state observability modulus has been defined.

### Cross-audit RED rule

The following inference is forbidden:

\[
\boxed{
\text{analytic unique continuation}
+
O(R^{-1/2})\text{ shell error}
\Rightarrow
O(R^{-1/2})\text{ core error}.
}
\]

No such quantitative estimate has been proved.

---

## 10. Updated frontier

The next genuinely new theorem target is

\[
\boxed{
\text{compare }\delta_R(\epsilon)
\text{ with the genealogy error }R^{-1/2}
\text{ on the compact W1 minimal set.}
}
\]

A sufficiently strong lower bound would make the recurrent core payer visible in the static radial genealogy.

Failure of such a lower bound would identify a new asymptotic nonobservability structure that must itself be analyzed rather than silently treated as exact tail/core equivalence.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
