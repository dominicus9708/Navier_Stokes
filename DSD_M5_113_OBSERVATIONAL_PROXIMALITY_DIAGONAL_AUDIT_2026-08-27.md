# DSD M5-113 — Observational Proximality / Diagonal Audit

Date: 2026-08-27

Status: **CORRECTION TO THE M5-112 INTERPRETATION / LARGE-R ANNULAR NONOBSERVABILITY DOES NOT BY ITSELF PRODUCE ONE FIXED BACKWARD-PROXIMAL PAIR / THE VALID OBJECT IS A GENEALOGY-RESOLUTION OBSERVATIONAL PROXIMALITY RELATION / TRUE STATE-SPACE PROXIMALITY REQUIRES AN ADDITIONAL DIAGONAL-COMPACTNESS/MODULUS BRIDGE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Why this correction is needed

M5-112 correctly derived the pairwise genealogy estimate

\[
\begin{aligned}
&\Big|
\|\mathcal O_{Re^\rho}(V)-\mathcal O_{Re^\rho}(W)\|_{L^3}
-
\|\mathcal O_R(V(-2\rho))-\mathcal O_R(W(-2\rho))\|_{L^3}
\Big|\\
&\qquad\le2CR^{-1/2}.
\end{aligned}
\]

It is also correct that for each **fixed** finite `R`, the annular observation `O_R` is injective and has a positive separation modulus `delta_R(epsilon)`.

However, an asymptotic nonobservability statement usually allows

\[
R=R_n\to\infty
\]

and the pair of states may also depend on `n`.

Therefore one may not replace this family immediately by one fixed pair whose backward trajectories approach each other in the state metric.

That would be a diagonal-limit inference requiring an additional compactness argument at moving radii.

---

## 2. Two distinct notions

### True backward proximality

A fixed pair `V != W` is backward proximal if there exist

\[
h_n\to\infty
\]

such that

\[
\boxed{d_M(V(-h_n),W(-h_n))\to0.}
\]

This is a state-space dynamical property.

### Genealogy-resolution observational proximality

For a scale `R`, two states are observationally unresolved at genealogy accuracy if

\[
\boxed{
\|\mathcal O_R(V)-\mathcal O_R(W)\|_{L^3}
\lesssim R^{-1/2}.
}
\]

This is a resolution-dependent shell property.

It does not require the state metric distance to be small.

---

## 3. The valid consequence of annular ill-conditioning

If M5-111 O2 occurs, then for some fixed state-space tolerance `epsilon_*>0` and arbitrarily large radii `R_n`, there exist states

\[
V_n,W_n\in M
\]

with

\[
d_M(V_n,W_n)\ge\epsilon_*
\]

but

\[
\boxed{
\|\mathcal O_{R_n}(V_n)-\mathcal O_{R_n}(W_n)\|_{L^3}
\lesssim R_n^{-1/2}.
}
\]

This is a rigorous **observational proximality sequence**.

It says that order-one-distinct W1 states can be hidden below the natural genealogy transport error on sufficiently remote shells.

---

## 4. Why compactness alone does not produce a fixed proximal pair

By compactness one may take subsequences

\[
V_n\to V_*,
\qquad
W_n\to W_*.
\]

The present-state separation can survive:

\[
d_M(V_*,W_*)\ge\epsilon_*.
\]

But the shell observations are taken at

\[
R_n\to\infty.
\]

Local W1 convergence of `V_n,W_n` does not control their values on the moving annuli

\[
R_n<|Y|<2R_n.
\]

Therefore one cannot pass

\[
\mathcal O_{R_n}(V_n)-\mathcal O_{R_n}(W_n)\to0
\]

to a statement about the asymptotic shell difference of the fixed limit pair `V_*,W_*` without an additional tail compactness theorem.

This is precisely a diagonal local-vs-moving-boundary obstruction.

---

## 5. Corrected dynamical split

The valid split after M5-111 is therefore:

### O1 — quantitatively observable

The genealogy error eventually lies below the fixed-state separation modulus needed to recover the relevant core observable.

### O2 — observationally proximal / ill-conditioned

There are scale-dependent pairs of order-one-distinct states that become indistinguishable on remote shells at genealogy resolution.

Only with an additional diagonal bridge may O2 be upgraded to

\[
\text{one fixed backward-proximal pair}.
\]

Thus the phrase `backward proximality` in M5-112 is retained only as a **possible stronger realization**, not as an already proved consequence of O2.

---

## 6. Required diagonal bridge

A sufficient upgrade would be a theorem of the following form.

If

\[
V_n\to V_*,
\qquad
W_n\to W_*,
\qquad
R_n\to\infty,
\]

and

\[
\|\mathcal O_{R_n}(V_n)-\mathcal O_{R_n}(W_n)\|_{L^3}	o0,
\]

then the canonical tail compactification should imply a corresponding asymptotic identification of `V_*` and `W_*` on the radial-history factor.

No such moving-radius compactness theorem has yet been proved at the strength needed to conclude state-space proximity.

---

## 7. DSD four-chain audit

### Formation

A fixed pair and a scale-dependent pair sequence are different formed objects.

### Axis

State-space distance, fixed-radius shell distance, and moving-radius shell distance remain distinct axes.

### Static aggregation

Compactness at fixed spatial radius is not applied to a moving-radius observation.

### Dynamics

True proximality is not inferred until one complete pair of trajectories has been formed.

### RED rule

The following diagonal shortcut is forbidden:

\[
\boxed{
V_n\to V_*,\ W_n\to W_*,\ R_n\to\infty,
\ \mathcal O_{R_n}(V_n)-\mathcal O_{R_n}(W_n)\to0
\Rightarrow
\mathcal O_{\infty}(V_*)=\mathcal O_{\infty}(W_*).
}
\]

There is no such automatically defined continuous `O_infinity` in the retained topology.

---

## 8. Updated frontier

The robust unresolved gate is now

\[
\boxed{
\text{quantitative annular observability}
\quad\text{vs}\quad
\text{genealogy-resolution observational proximality}.
}
\]

If the observable lane wins, the finite-core payer becomes readable in the static radial genealogy.

If the ill-conditioned lane survives, the next task is to construct the appropriate **tail compactification / factor map** before making any dynamical proximality claim.

This correction keeps the DSD dependency graph acyclic and prevents a moving-radius compactness loop from re-entering the argument.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
