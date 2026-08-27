# DSD M5-112 — Tail Observability to Backward Proximality

Date: 2026-08-27

Status: **W1-CONDITIONAL DYNAMICAL REFORMULATION / PAIRWISE RADIAL GENEALOGY IDENTIFIES LARGE-R SHELL NONOBSERVABILITY WITH BACKWARD PROXIMALITY OF DISTINCT STATES ON THE MINIMAL W1 SET, UP TO THE O(R^-1/2) TRANSPORT ERROR / A DISTAL-PROXIMAL DYNAMICAL SPLIT REPLACES THE VAGUE ANALYTIC-CONTINUATION QUESTION / NEITHER DYNAMICAL BRANCH IS YET EXCLUDED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Pairwise genealogy

Fix one large base radius `R` and two states `V,W` on the compact minimal W1 set `M`.

Choose complete backward trajectories through both states.

The W1 genealogy law gives for every `rho>=0`

\[
\|\mathcal O_{Re^\rho}(V)-\mathcal O_R(V(-2\rho))\|_{L^3(A)}
\le CR^{-1/2}
\]

and

\[
\|\mathcal O_{Re^\rho}(W)-\mathcal O_R(W(-2\rho))\|_{L^3(A)}
\le CR^{-1/2}.
\]

Subtracting the two relations and using the triangle inequality yields

\[
\boxed{
\begin{aligned}
&\Big|
\|\mathcal O_{Re^\rho}(V)-\mathcal O_{Re^\rho}(W)\|_{L^3}
-
\|\mathcal O_R(V(-2\rho))-\mathcal O_R(W(-2\rho))\|_{L^3}
\Big|\\
&\qquad\le2CR^{-1/2}.
\end{aligned}
}
\]

Thus large-radius shell separation at the present phase is the fixed-radius shell separation of backward ancestors, up to the audited transport error.

---

## 2. Fixed-base shell observation is a state coordinate

M5-111 proved that for fixed finite `R`,

\[
\mathcal O_R:M\to L^3(A)
\]

is continuous and injective.

Hence on the compact set `M` it is a homeomorphism onto its image.

For every state-space tolerance `epsilon>0`, the separation modulus

\[
\delta_R(\epsilon)>0
\]

is defined by

\[
\delta_R(\epsilon)
=
\inf_{d_M(X,Y)\ge\epsilon}
\|\mathcal O_R(X)-\mathcal O_R(Y)\|_{L^3(A)}.
\]

Therefore fixed-base shell closeness below `delta_R(epsilon)` forces ancestor-state closeness below `epsilon`.

---

## 3. Backward proximality

Call a pair of distinct complete W1 trajectories backward proximal if there exists a sequence

\[
h_n\to\infty
\]

such that

\[
\boxed{
d_M(V(-h_n),W(-h_n))\to0.}
\]

This definition is made on the already-formed compact W1 dynamics.

It does not assert that backward solutions are globally well-posed outside the retained complete trajectories.

---

## 4. Remote shell collapse implies ancestral proximity

Suppose for fixed large base `R` and a sequence `rho_n->infinity`,

\[
\|\mathcal O_{Re^{\rho_n}}(V)-\mathcal O_{Re^{\rho_n}}(W)\|_{L^3}
\to0
\]

and the fixed genealogy error `CR^-1/2` is chosen smaller than the shell-separation threshold relevant to a prescribed `epsilon`.

Then the pairwise genealogy estimate gives

\[
\|\mathcal O_R(V(-2\rho_n))-\mathcal O_R(W(-2\rho_n))\|_{L^3}
\lesssim
2CR^{-1/2}+o(1).
\]

If this is below `delta_R(epsilon)`, then

\[
d_M(V(-2\rho_n),W(-2\rho_n))<\epsilon.
\]

Thus quantitative remote-shell collapse is a direct signature of backward approach of the ancestor states.

---

## 5. Dynamical branch split

The observability problem is therefore more naturally split by the dynamics on `M`.

### D1 — backward-distal lane

Distinct states that are separated at the present phase retain a definite separation along all sufficiently old ancestors at the fixed-shell resolution relevant to the genealogy error.

Then the far radial shell record remains quantitatively state-discriminating.

In this lane the M5-109 core payer history can, in principle, be encoded robustly into radial tail patterns once the corresponding modulus is made explicit.

### D2 — backward-proximal lane

There exist distinct present states with ancestor subsequences becoming arbitrarily close.

Then far radial shell patterns can lose the information distinguishing those current core states without violating exact analyticity or injectivity at any fixed radius.

This is a genuine dynamical information-loss mechanism, not an error in analytic continuation.

---

## 6. Why parabolic uniqueness does not automatically kill D2

Forward determinism says that one exact state has one exact future.

It does not imply a uniform lower bound preventing two distinct trajectories from becoming arbitrarily close at remote negative times and later separating over a long forward interval.

On a compact nonlinear flow such proximal behavior is a dynamical question.

Therefore the inference

\[
\text{forward uniqueness}
\Rightarrow
\text{uniform backward distality}
\]

is RED unless a quantitative stability theorem is supplied.

---

## 7. Relation to the static tail

The current far tail is a radial image of the backward orbit.

Hence the two lanes have distinct DSD meanings:

\[
\boxed{
D1:\ 
\text{tail = faithful radial genealogy at the relevant resolution},
}
\]

\[
\boxed{
D2:\ 
\text{tail = non-injective/asymptotically information-losing factor of the core dynamics}.
}
\]

Both remain compatible with bounded weak-L3 height and unbounded log-depth.

---

## 8. Four-chain DSD audit

### Formation

Pairs of complete trajectories are formed before proximality is discussed.

### Axis

Present-state separation, backward-time separation, and radial-shell separation are three distinct axes.

### Static aggregation

The two genealogy errors are added only once, giving `2 C R^-1/2`.

### Dynamics

Proximality is a property of the already-formed minimal dynamics, not a substitute for recurrence or compactness.

### Cross-audit

No qualitative uniqueness theorem is promoted to a quantitative inverse estimate.

---

## 9. New precise frontier

The previous broad question

\[
\text{Can the tail encode the recurrent core?}
\]

is replaced by the sharper dynamical alternative

\[
\boxed{
\text{W1 minimal flow is quantitatively backward-distal at genealogy resolution}
\quad\lor\quad
\text{it contains a backward-proximal information-loss lane}.
}
\]

A closure may therefore come from either:

1. proving sufficient backward distality and then exploiting the forced recurrent payer pattern in the static trace; or
2. proving that backward-proximal complete W1 trajectories are incompatible with the Navier--Stokes smoothing/critical-tail structure.

Neither theorem is currently available in the repository.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
