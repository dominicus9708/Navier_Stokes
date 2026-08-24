# DSD Singular-Time Formation-Status Audit — 2026-08-25

Status: **SINGULAR-TIME `INFINITE VALUE` LANGUAGE REJECTED / FINITE FIRST-HITTING WITNESS FORMULATION REQUIRED / ANCIENT GERM SEPARATED FROM THE UNFORMED ENDPOINT / GLOBAL REGULARITY NOT PROVED.**

This note audits the hypothetical first singular time \(T^*\) against the Formation Axiom System's distinction between undefined/unassigned data and defined values.

---

## 1. Smooth-regime domain

Assume for contradiction that a classical Navier–Stokes solution exists smoothly on

\[
[0,T^*)
\]

but cannot be continued smoothly through a finite \(T^*\).

For every

\[
t<T^*,
\]

the smooth-regime quantities used in the proof are defined and finite, including

\[
U(t),\quad
\Omega(t),\quad
\|\Omega(t)\|_\infty,
\]

and fixed finite spatial derivatives.

At \(t=T^*\), however, the smooth-regime representation has **not** been assumed to extend.

Therefore the expression

\[
\Omega(x,T^*)
\]

is not automatically an assigned smooth-regime value.

---

## 2. `Infinity` is not an assigned vorticity value

If the chosen blow-up quantity satisfies

\[
\|\Omega(t)\|_\infty\to\infty
\qquad(t\uparrow T^*),
\]

the correct statement is about the failure of finite bounded assignment along the pre-endpoint regime.

It is **not** a Stage-V assignment

\[
\|\Omega(T^*)\|_\infty=+\infty
\]

inside the same ordinary real-valued quantity channel unless an extended codomain containing \(+\infty\) has explicitly been declared.

The DSD-correct status is

\[
\boxed{
\text{the smooth-regime quantity remains defined at every }t<T^*,
\text{ while no finite endpoint assignment is supplied by that regime.}
}
\]

Thus `undefined/unassigned at the endpoint` must not be silently replaced by `defined infinite value`.

**Status: REQUIRED FORMATION-TYPING CORRECTION.**

---

## 3. Finite-witness formulation of blow-up

Unboundedness can be expressed entirely through formed finite states:

\[
\boxed{
\forall A<\infty\;\exists t_A<T^*:
\|\Omega(t_A)\|_\infty>A.
}
\]

For a geometric threshold sequence

\[
W_j=q^jW_0,
\]

continuity of the smooth pre-endpoint quantity gives first-hitting times

\[
t_j<T^*
\]

with

\[
\boxed{
\|\Omega(t_j)\|_\infty=W_j<\infty.
}
\]

Every stage \(j\) is therefore a finite formed witness. No singular endpoint value is needed.

This is the correct DSD basis for the first-hitting tower.

**Status: PROVED under the usual smooth pre-endpoint continuity and unboundedness hypothesis.**

---

## 4. The first-hitting tower does not form a singular material object at \(T^*\)

The sequence

\[
(t_j,X_j,r_j)
\]

provides increasingly extreme finite pre-endpoint descriptions.

It does not by itself produce one formed material object located at \(T^*\).

In DSD terms,

\[
\boxed{
\text{arbitrarily late finite formation witnesses}
\not\Rightarrow
\text{an endpoint object with assigned infinite values}.
}
\]

Any argument referring to `the singular core at \(T^*\)` must therefore be read either as shorthand for a quantified family of pre-endpoint witnesses or as a separately constructed limit model.

---

## 5. The ancient germ is a separate formed limit model

The normalized ancient germ is obtained from finite first-hitting stages by recentering/rescaling and compactness:

\[
U_{j_n}\to U_\infty
\]

on fixed finite bases.

The ancient germ has its own normalized representation, values, and channel assignments. It is therefore a **separate limit construction**.

It must not be identified with the undefined smooth-regime endpoint state:

\[
\boxed{
U_\infty
\neq
`u(\cdot,T^*)\text{ at infinite magnification}'
}
\]

as an object identity.

What is justified is the existence of a formation/provenance relation from the prelimit first-hitting sequence to the ancient germ.

This distinction is the endpoint analogue of the earlier rule

\[
\text{same scale}\not\Rightarrow\text{same material object}.
\]

---

## 6. Where a regular and nonregular continuation may first differ

Suppose one compares two candidate extension regimes using the same approved structural representation:

1. a smooth continuation regime through \(T^*\);
2. a regime in which the required smooth quantities cannot be assigned at \(T^*\).

If Stages I–IV and the underlying structural materials are held fixed by construction, the first difference can occur at the Stage-V partial quantity assignment:

\[
\boxed{
\text{finite smooth value assigned}
\quad\text{vs}\quad
\text{required endpoint value not in the assignment domain}.
}
\]

However this `first difference at Stage V` conclusion is **conditional on the two candidate regimes sharing the same earlier representation/restriction/realization data**. If the representation itself is changed at the endpoint, an earlier Formation-stage divergence is possible.

Thus DSD does not automatically declare the singularity a Stage-V failure; it tells us how to type the comparison correctly.

**Status: PROVED CONDITIONAL AS A FORMATION-MODEL COMPARISON.**

---

## 7. Consequence for proof language

The following phrases are unsafe if read literally:

- `the vorticity is infinite at the singular point`;
- `the singular object at \(T^*\) has property X`;
- `the tail/core at \(T^*\) returns`.

They must be replaced by one of two legitimate forms.

### Finite-witness form

\[
\forall j\;\exists t_j<T^*:\ \text{finite formed descriptor }D_j\text{ has property }P_j.
\]

### Separate-limit-model form

\[
D_{j_n}\to D_\infty,
\]

followed by an explicit statement of which properties pass to the limit.

No property may be transferred merely by speaking as though the endpoint itself were already a formed smooth object.

---

## 8. Interaction with the finite cubic-witness correction

The same DSD pattern now appears twice.

### Blow-up

Instead of one `infinite vorticity value`, use

\[
\forall A\;\exists\text{ finite first-hitting witness above }A.
\]

### Non-L3 cubic tail

Instead of one `infinite Stage-VII tail object`, use

\[
\forall L\;\exists\text{ finite shell block with cubic mass }>L.
\]

Therefore both major infinities in the current proof attempt admit a DSD-compatible **finite witness formulation**.

This is structurally important:

\[
\boxed{
\text{the proof can be conducted entirely with finite formed states and}\
\text{finite formed composites, with limits handled separately.}
}
\]

---

## 9. New DSD finite-witness principle for this proof attempt

For every claimed divergent/unbounded mechanism, require the proof to expose a finite witness family before applying dynamics.

Schematically:

\[
\boxed{
\text{unbounded/global-limit claim}
\to
\text{arbitrarily large finite formed witnesses}
\to
\text{typed static aggregation}
\to
\text{dynamic evolution of those witnesses}.
}
\]

This is not a new Formation axiom. It is a proof-discipline consequence of the existing Formation distinction between assigned values, undefined/unassigned data, finite composition, and later limit constructions.

---

## 10. Audit verdict

### PROVED / structurally valid

- all first-hitting stages lie inside the smooth regime and use finite defined values;
- blow-up can be expressed entirely by arbitrarily large finite first-hitting witnesses;
- the ancient germ is a separate limit construction, not an endpoint value;
- the infinite cubic tail can likewise be represented by arbitrarily large finite static witnesses.

### REJECTED

- treating \(+\infty\) as an ordinary assigned vorticity value without an extended codomain;
- treating the hypothetical singular endpoint as an already formed smooth material object;
- transferring properties to that endpoint without a finite-witness or limit-passage theorem.

### NOT DERIVED

- impossibility of the finite witness tower itself;
- global regularity.

The next proof step must therefore attempt a contradiction among **finite formed witnesses**, rather than against an imagined infinite-valued endpoint object.

Global regularity remains **UNPROVED**.