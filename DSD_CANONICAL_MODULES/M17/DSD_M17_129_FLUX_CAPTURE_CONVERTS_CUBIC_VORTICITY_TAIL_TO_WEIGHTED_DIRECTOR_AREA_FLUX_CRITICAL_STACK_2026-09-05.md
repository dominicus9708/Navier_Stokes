# DSD M17-129 — Flux capture converts the cubic vorticity tail to a weighted director-area-flux critical stack

Date: 2026-09-05
Canonical ID: **M17-129**

Status: **EXACT CONDITIONAL SEQUENCE BRIDGE / M17-121 CONVERTS THE M5 NON-L3 DIRICHLET OBSTRUCTION TO A DIVERGENT VORTICITY CRITICAL STACK. IF A SUBSET OF THAT STACK IS CARRIED BY UNIFORMLY NONDEGENERATE COMPLETE RIBBON BUNDLES, M17-122 GIVES `J_{k,rib}^omega asymp K_k Phi_k`. HENCE CUBIC DIVERGENCE ON THE RIBBON SUBSET IS EXACTLY A WEIGHTED DIRECTOR-AREA FLUX DIVERGENCE `sum (K_k Phi_k)^(3/2)=infinity`. THE M5 AMPLITUDE-SENSITIVE HIGH-RATIO SELECTION BECOMES `K_k^(5/2) Phi_k^(1/2) >> 1`. THE SHARP MODEL `Phi_k~K_k^-1` HAS DIVERGENT WEIGHTED CUBIC STACK BUT SUMMABLE UNWEIGHTED TOTAL FLUX, SO ORDINARY FINITE DIRECTOR-AREA FLUX CANNOT CLOSE THE BRANCH. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Vorticity critical stack

M17-121 gives

\[
\boxed{
\sum_k(J_k^\omega)^{3/2}=\infty,
\qquad
J_k^\omega:=K_k\int_{A_{K_k}}|W|^2dy,
}
\]

on the retained ancient non-`L^3` tail, up to the fixed dyadic/enlarged-annulus equivalence.

---

## 2. Amplitude-sensitive arithmetic selection

Set

\[
a_k:=(J_k^\omega)^{1/2}.
\]

Since

\[
\sum_ka_k^3=\infty
\]

and `K_k` grows geometrically, for every finite `C>0` the set

\[
\boxed{
S_C^\omega
:=
\{k:a_kK_k^2>C\}
}
\]

still satisfies

\[
\boxed{
\sum_{k\in S_C^\omega}a_k^3=\infty.
}
\]

Indeed, on the complement

\[
a_k\le CK_k^{-2}
\]

and the cubic sum is geometric.

---

## 3. Ribbon allocation hypothesis

Let `S_R` be a subset of shell indices on which a uniformly nondegenerate complete-ribbon bundle carries a definite part of the vorticity shell mass.
Write

\[
J_{k,rib}^\omega
:=
K_kE_{k,rib}^\omega.
\]

Assume the selected ribbon contribution itself has divergent cubic mass,

\[
\boxed{
\sum_{k\in S_R}(J_{k,rib}^\omega)^{3/2}=\infty.
}
\]

M17-122 gives

\[
\boxed{
 c_FK_k\Phi_k
\le
J_{k,rib}^\omega
\le
C_FK_k\Phi_k
}
\]

for fixed compact nondegeneracy constants.

---

## 4. Exact weighted flux-stack equivalence

Therefore

\[
\boxed{
\sum_{k\in S_R}
(J_{k,rib}^\omega)^{3/2}=\infty
\iff
\sum_{k\in S_R}
(K_k\Phi_k)^{3/2}=\infty.
}
\]

The Rank-2 ribbon form of the ancient cubic obstruction is thus

\[
\boxed{
\sum_{k\in S_R}
K_k^{3/2}\Phi_k^{3/2}
=\infty.
}
\]

This is the first direct critical sequence written entirely in the inherited director-area flux variable.

---

## 5. High-ratio selection in flux variables

On a shell where

\[
J_{k,rib}^\omega\asymp K_k\Phi_k,
\]

the M5 high-ratio quantity becomes

\[
(J_{k,rib}^\omega)^{1/2}K_k^2
\asymp
K_k^{5/2}\Phi_k^{1/2}.
\]

Hence the high-ratio selected set is equivalently characterized by

\[
\boxed{
K_k^{5/2}\Phi_k^{1/2}>C',
}
\]

or

\[
\boxed{
\Phi_k>C''K_k^{-5}.
}
\]

The lower threshold `K_k^-5` is extremely weak; the cubic critical model is much larger.

---

## 6. Sharp flux survivor

Take

\[
\boxed{
\Phi_k\sim K_k^{-1}.
}
\]

Then

\[
K_k\Phi_k\sim1
\]

and therefore

\[
\sum_k(K_k\Phi_k)^{3/2}=\infty.
\]

But because `K_k` grows geometrically,

\[
\boxed{
\sum_k\Phi_k
\sim
\sum_kK_k^{-1}
<\infty.
}
\]

Thus a finite unweighted director-area flux inventory is fully compatible with the critical ribbon obstruction.

This is the geometric-flux analogue of the M5 `U~1/r` energy-cheap critical tail.

---

## 7. Consequence for possible closure routes

Any argument using only

\[
\sum_k\Phi_k<\infty
\]

or a finite total amount of frozen director-area charge is too weak.

A successful ribbon-tail closure must control a scale-weighted quantity strong enough to see

\[
\boxed{K_k\Phi_k}
\]

or directly its `ell^{3/2}` stack.

Possible sources would have to be one of:

1. a weighted director-area flux moment with physical/geometric meaning;
2. a topological/degree rigidity that quantizes or forbids the `K_k^-1` flux cascade;
3. a boundary-throughput estimate whose cost grows with shell radius;
4. a tail-decoupling/Liouville theorem that eliminates the remote flux stack without summing it by ordinary charge.

None is currently established.

---

## 8. DSD audit

### Audit A — total vorticity stack automatically belongs to ribbons

Rejected. The sequence bridge applies only to the subset actually carried by the nondegenerate ribbon branch. Other director branches/interfaces must retain their own ledgers.

### Audit B — finite unweighted director flux closes cubic divergence

False. `Phi_k~K_k^-1` is an explicit counter-scaling.

### Audit C — high-ratio threshold equals critical scaling

Rejected. `Phi_k>>K_k^-5` is only the no-quiet-forgetting arithmetic threshold. The scale-critical cubic ribbon model is `Phi_k~K_k^-1`.

### Audit D — signed and unsigned flux

`Phi_k` here denotes the positive tube-flux amount of the ribbon bundle. A signed degree/closed-surface flux may have additional cancellations and must not be substituted without a separate theorem.

### Audit E — proof status

The tail is reparameterized in a sharper geometric carrier variable, but the weighted flux stack is not yet bounded.

---

## 9. Updated ribbon-tail frontier

On a nondegenerate ribbon subset carrying divergent cubic vorticity mass,

\[
\boxed{
\sum(K_k\Phi_k)^{3/2}=\infty.
}
\]

The sharp unresolved model is

\[
\boxed{
\Phi_k\sim K_k^{-1}.
}
\]

The next high-value calculation is to test whether the divergence-free director-area current admits a **radially weighted flux moment identity** or a topological shell-flux constraint that is incompatible with this `K^-1` cascade. If not, the ribbon tail must be handed back to the Liouville/tail-decoupling route.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
