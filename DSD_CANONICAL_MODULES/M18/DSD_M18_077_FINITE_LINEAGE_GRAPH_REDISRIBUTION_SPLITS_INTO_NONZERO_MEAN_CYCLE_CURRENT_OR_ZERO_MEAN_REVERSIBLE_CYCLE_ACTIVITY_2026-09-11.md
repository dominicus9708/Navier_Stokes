# M18-077 — Finite-lineage redistribution splits into nonzero mean cycle current or zero-mean reversible cycle activity

**Date:** 2026-09-11  
**Status:** FINITE-LINEAGE GRAPH CONSERVATION / CYCLE-SPACE REDUCTION / FALSE MONOTONICITY FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-076 proves on a controlled Frobenius CE-H material patch that a nonzero current cannot remain purely label-invisible:

\[
\boxed{
\operatorname{div}_\Sigma J_\Sigma=-\kappa\rho,
}
\]

and, on the nonzero marked component,

\[
\boxed{
J_G\neq0
}
\]

unless surface/label geometry degenerates.

Under compact patch control this becomes a fixed quantitative material-label redistribution event.

The next question is where indefinitely repeated redistribution can go once M5-497/M5-514 have reduced the quiet compact branch to a finite persistent lineage network.

A tempting shortcut is

\[
\text{finite graph + recurrent transfer}
\Longrightarrow
\text{nonzero signed cycle current}.
\]

That statement is false without an orientation bias: equal forward/backward transfers may cancel.

This module derives the exact graph-theoretic replacement.

---

## 2. Finite persistent lineage graph

Let

\[
G=(V,E)
\]

be the finite persistent lineage graph on the retained compact ergodic component, with

\[
|V|=N<\infty.
\]

Choose one orientation for each geometric edge. Reversing physical transfer is represented by a negative signed current on the same oriented edge.

Let

\[
j(\theta)\in\mathbb R^{E}
\]

be the instantaneous signed redistribution current between persistent lineages after all newly created/replacement/export events have been routed to their typed exits.

Let

\[
m(\theta)\in\mathbb R^V
\]

be a bounded vector of lineage-carried scalar material-label moments or another conserved redistributable lineage quantity.

Write the incidence matrix as

\[
B\in\mathbb R^{V\times E}.
\]

On a no-export/no-new-label interval the redistribution law has the abstract conservation form

\[
\boxed{
m'(\theta)=Bj(\theta).}
\]

This is the finite-network version of local material-label redistribution.

---

## 3. Bounded storage kills long-time mean divergence

Integrate from \(0\) to \(T\):

\[
m(T)-m(0)
=
B\int_0^Tj(\theta)\,d\theta.
\]

Divide by \(T\):

\[
\frac{m(T)-m(0)}{T}
=
B\bar j_T,
\]

where

\[
\boxed{
\bar j_T
:=
\frac1T\int_0^Tj(\theta)\,d\theta.
}
\]

On the compact finite-lineage branch the lineage moment vector is bounded:

\[
\sup_T|m(T)|<\infty.
\]

Hence

\[
\boxed{
B\bar j_T\to0
\qquad(T\to\infty).
}
\]

Every convergent subsequence

\[
\bar j_{T_n}\to\bar j
\]

therefore satisfies

\[
\boxed{B\bar j=0.}
\]

Thus every long-time mean redistribution current lies in the graph cycle space

\[
\boxed{
\ker B.
}
\]

---

## 4. Cycle-space interpretation

For a finite graph, every vector in

\[
\ker B
\]

is a linear combination of cycle currents.

Choose a cycle basis

\[
c_1,\dots,c_g,
\qquad
g=|E|-|V|+\#\text{components}.
\]

Then

\[
\boxed{
\bar j
=
\sum_{r=1}^{g}\gamma_r c_r.
}
\]

Therefore if

\[
\bar j\neq0,
\]

at least one coefficient satisfies

\[
\gamma_r\neq0.
\]

Hence recurrent bounded redistribution with nonzero signed mean necessarily contains a persistent oriented cycle current.

This part is exact finite-dimensional graph theory.

---

## 5. Nonzero-mean branch

Define

\[
G_{cycle}^{mean}
:
\exists\text{ a subsequential ergodic mean }\bar j\neq0.
\]

Then

\[
\boxed{
G_{cycle}^{mean}
\Longrightarrow
\text{at least one persistent lineage cycle carries nonzero signed mean flux}.
}
\]

Because the graph is finite, one can choose a fixed simple cycle

\[
C_*
\]

and a fixed orientation such that its cycle coefficient has nonzero mean.

This is the strongest signed conclusion available from bounded storage alone.

It does **not** yet imply a contradiction: a conservative circulation on a finite graph may persist indefinitely without changing vertex storage.

---

## 6. Zero-mean branch is genuinely possible

Now suppose every long-time mean current vanishes:

\[
\boxed{
\bar j_T\to0
}
\]

(or every ergodic mean cycle coefficient is zero).

This does not imply

\[
j(\theta)=0.
\]

A two-lineage example already shows the obstruction. Let one edge be oriented \(1\to2\) and take periodic current

\[
j(\theta)=
\begin{cases}
+j_0,&0<\theta<1,\\
-j_0,&1<\theta<2,
\end{cases}
\]

extended periodically.

Then

\[
\bar j=0,
\]

while

\[
\frac1T\int_0^T|j(\theta)|\,d\theta
\to j_0>0.
\]

The lineage storage simply oscillates and returns.

Therefore

\[
\boxed{
\text{recurrent redistribution}
\not\Rightarrow
\text{nonzero signed mean circulation}.
}
\]

This is the finite-graph monotonicity firewall.

---

## 7. Total-variation activity supplied by M18-076

M18-076 gives, on a controlled recurrent patch family, a fixed lower redistributive current scale unless geometry degenerates.

After event thickening and bounded-gap recurrence, this yields a positive mean unsigned activity on the retained branch, schematically

\[
\boxed{
\liminf_{T\to\infty}
\frac1T
\int_0^T|j(\theta)|\,d\theta
\ge a_*>0
}
\]

for at least one finite set of lineage-transfer channels, after the usual finite pigeonhole refinement.

Thus the zero-mean branch is not inactivity. It is

\[
\boxed{
\bar j=0,
\qquad
\langle|j|\rangle>0.
}

Call this

\[
\boxed{G_{cycle}^{rev}}
\]

for reversible cycle activity.

---

## 8. Exact finite-graph dichotomy

On the compact no-new-label/no-export branch with unavoidable recurrent redistribution,

\[
\boxed{
G_{material\ redistribution}
\Longrightarrow
G_{cycle}^{mean}
\lor
G_{cycle}^{rev}
\lor
G_{graph/label\ realization\ loss}.
}
\]

where

### Mean-cycle branch

\[
\boxed{
G_{cycle}^{mean}:
\bar j\in\ker B\setminus\{0\}.
}
\]

### Reversible branch

\[
\boxed{
G_{cycle}^{rev}:
\bar j=0,
\qquad
\langle|j|\rangle>0.
}
\]

### Realization-loss branch

The finite persistent graph, bounded lineage storage, material-label chart, or no-export/no-replacement assumptions fail.

This routes back to an already typed turnover/geometry/root exit.

---

## 9. Why a vertex potential does not close the mean-cycle branch

Let

\[
\phi\in\mathbb R^V
\]

be any bounded vertex potential.

The edge gradient is

\[
B^T\phi.
\]

For a cycle current

\[
j_C\in\ker B,
\]

one has

\[
(B^T\phi)\cdot j_C
=
\phi\cdot Bj_C
=0.
\]

Hence no scalar potential on lineage vertices can detect or monotonically price a pure cycle-space current.

This is important:

\[
\boxed{
\text{bounded lineage potential}
\text{ sees storage transfer but is blind to conservative cycle circulation}.
}
\]

Thus the mean-cycle branch requires a genuinely cycle-sensitive observable, not another vertex-storage moment.

---

## 10. Why total variation does not close the reversible branch

On \(G_{cycle}^{rev}\), the accumulated variation

\[
\int_0^T|j|d\theta
\]

grows linearly.

But M18-059 already establishes the general unsigned-payer firewall: a positive local action is not useful without a finite additive parent budget of matching homogeneity.

Therefore

\[
\boxed{
\langle|j|\rangle>0
}

alone is not a contradiction.

The reversible branch needs either

1. a signed phase-lag/hysteresis observable;
2. a coercive cycle-dissipation budget;
3. a rigidity theorem excluding nontrivial periodic/recurrent reversible circulation.

---

## 11. Relation to M18-066--067 hysteresis audit

M18-066 identifies recurrent phase covariance with oriented moment-space hysteresis circulation.

M18-067 shows that such circulation does not automatically create an additional unsigned diffusion payment: strain can drive the loop while diffusion opposes it.

The present graph result is the finite-lineage analogue.

A nonzero \(G_{cycle}^{mean}\) is an oriented circulation in lineage space.
A zero-mean \(G_{cycle}^{rev}\) is a back-and-forth recurrent loop with positive variation but no signed drift.

Neither is eliminated by unsigned cost counting alone.

---

## 12. Pairing with a cycle 1-form

Although vertex potentials are blind to cycle currents, a graph 1-form

\[
\alpha\in\mathbb R^E
\]

with nonzero circulation around a chosen cycle can detect them.

For a fixed cycle \(C\), choose \(\alpha_C\) such that

\[
\boxed{
\oint_C\alpha_C\neq0.
}
\]

Then define the signed cycle observable

\[
\boxed{
\mathcal J_C(T)
:=
\int_0^T\alpha_C\cdot j(\theta)d\theta.
}
\]

On \(G_{cycle}^{mean}\), one can choose a cycle basis element so that

\[
\boxed{
\lim_{T\to\infty}\frac{\mathcal J_C(T)}{T}\neq0.
}
\]

However \(\mathcal J_C\) is an integrated current, not yet a bounded state observable.

To turn it into a contradiction one would need to prove that the corresponding 1-form is exact on the **physical recurrent state space** or that its accumulated circulation is bounded by a finite physical quantity.

That theorem is not currently available.

---

## 13. New frontier after M18-077

The material-current route is now

\[
\boxed{
\text{mandatory CE-H current}
\Longrightarrow
\begin{cases}
G_{self\text{-}helicity/twist},\\
G_{surface/label\ geometry\ loss},\\
G_{cycle}^{mean},\\
G_{cycle}^{rev}.
\end{cases}
}
\]

The old undifferentiated `material-label redistribution` endpoint has been resolved into two recurrent finite-graph mechanisms.

---

## 14. Highest-value next target

The mean-cycle and reversible branches should not be attacked by another unsigned payer.

The next useful question is whether the CE-H PDE supplies a **physical graph 1-form / cocycle** whose circulation is tied to a bounded state quantity.

Natural candidates are built from the exact CE-H scalars

\[
\sigma,
\qquad
\kappa,
\qquad
\rho,
\]

and the surface Poisson relation

\[
-\Delta_\Sigma\psi=\kappa\rho.
\]

A successful construction would have one of the forms

\[
\boxed{
\alpha\cdot j
=
\frac{d}{d\theta}\Phi(state)
+
D,
\qquad D\ge0,
}
\]

or

\[
\boxed{
\oint_C\alpha=0
}
\]

for every physically realizable CE-H cycle.

Either would turn graph circulation into a rigidity or monotonicity statement.

---

## 15. Audit verdict

### Certified

1. Bounded finite-lineage storage implies every long-time mean transfer current is divergence-free on the lineage graph:
   \[
   \bar j\in\ker B.
   \]
2. A nonzero mean current therefore contains a nonzero cycle-space component.
3. Recurrent redistribution does not force nonzero signed mean current; exact forward/backward cancellation is possible.
4. Under recurrent redistribution, the zero-mean branch retains positive unsigned variation.
5. Vertex potentials cannot detect pure cycle currents.
6. Positive total variation alone is blocked by the M18-059 unsigned-payer firewall.
7. The remaining endpoints are nonzero mean cycle circulation, reversible zero-mean circulation, or graph/label realization loss.

### Still open

1. A physical cycle-sensitive signed cocycle.
2. Exclusion of reversible zero-mean lineage circulation.
3. Exclusion of the self-helicity/twist branch.
4. Surface/label geometry degeneration.
5. Ancestry, remote, and critical roots.
6. Global 3D Navier--Stokes regularity.

## 16. Next target

M18-078 should search for a **CE-H cycle cocycle** by combining

\[
\operatorname{div}_\Sigma J_\Sigma=-\kappa\rho,
\]

\[
D_B\rho=(\sigma+\kappa-1)\rho,
\]

and material label moments.

The first audit should determine whether the natural logarithmic amplitude differential

\[
D_B\log\rho=\sigma+\kappa-1
\]

is exact enough to kill graph circulation, or whether its strain term permits a nontrivial closed-loop phase work.
