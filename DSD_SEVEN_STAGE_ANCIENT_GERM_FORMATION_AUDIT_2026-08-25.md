# DSD Seven-Stage Ancient-Germ Formation Audit — 2026-08-25

Status: **FIXED-BASE LOCAL ANCIENT GERM CAN BE TYPED THROUGH THE FORMATION STAGES / INFINITE CUBIC TAIL IS NOT A STAGE-VII FINITE COMPOSITION / FINITE-WITNESS REFORMULATION DERIVED / GLOBAL REGULARITY NOT PROVED.**

This note audits the Navier–Stokes ancient-germ construction against the actual seven-stage Formation Axiom System rather than against generic PDE terminology.

The Formation Axiom System is static. Its order is:

\[
\boxed{
I\to II\to III\to IV\to V\to VI\to VII,
}
\]

where I, II, III, V are primitive constraints and IV, VI, VII are definitional closures.

The key correction is that Stage VII forms a composition only from a **finite set of already formed channels**. An infinite shell sum is therefore not automatically one Stage-VII formed object.

---

## 1. Fixed-base candidate representation

Fix a finite local base

\[
B=(M,T,N),
\]

where

- \(M<\infty\) fixes a spatial compact window;
- \(T<\infty\) fixes a finite ancient-time window;
- \(N<\infty\) fixes a finite derivative/channel depth.

For a first-hitting stage \(j\), use a normalized representation containing

\[
\mathfrak P_{j,B}
=
\left(
U_j,\Omega_j,P_j,\text{normalization record},\text{retained finite channel declarations}
\right)
\]

restricted to the chosen base.

The normalization record must retain at least the information needed to distinguish the stage-dependent physical center, time, and scale from the fixed normalized base. These are records/tags, not formal DSD axes unless separately realized through the Axis-Property system.

---

## 2. Stage I — structural approval

Stage I asks whether the candidate representation itself is an approved representation.

For the PDE bridge this requires the representation type to be declared before any values are aggregated. In particular, one must distinguish

\[
\boxed{
\text{field data},\quad
\text{normalization/provenance data},\quad
\text{channel-role declarations},\quad
\text{derived quantities}.
}
\]

A bare tuple of numerical norms is not enough to recover the structure from which they came.

For a fixed finite base, the normalized smooth Navier–Stokes fields together with their provenance/normalization record provide a valid candidate representation once this typing is declared.

**Status: BRIDGE-CONSTRUCTIBLE / no contradiction found.**

---

## 3. Stage II — sound restriction

Stage II requires a smaller representation cut from a larger one to inherit the relevant materials, anchors, and records consistently.

Let

\[
B_1=(M_1,T_1,N_1)
\preceq
B_2=(M_2,T_2,N_2)
\]

mean

\[
M_1\le M_2,\qquad
T_1\le T_2,\qquad
N_1\le N_2.
\]

At a fixed first-hitting stage \(j\), restriction from \(B_2\) to \(B_1\) is ordinary restriction of the same normalized field and records. Hence

\[
\boxed{
\operatorname{Res}_{B_2\to B_1}\mathfrak P_{j,B_2}
=
\mathfrak P_{j,B_1}
}
\]

provided the channel declarations are nested consistently.

For the ancient limit, a **single diagonal subsequence** across increasing bases is essential. If unrelated subsequences were chosen independently for each base, Stage-II inheritance of the limiting object would not be established.

With one diagonal subsequence, restriction commutes with local convergence on every fixed smaller base:

\[
\boxed{
\operatorname{Res}_{B_2\to B_1}U_{\infty,B_2}
=U_{\infty,B_1}.
}
\]

**Status: PROVED CONDITIONAL on using one common diagonal extraction and nested channel declarations.**

---

## 4. Stage III — sound construction realization

Stage III requires a realized construction to activate only material available in the restricted representation and to preserve the location/provenance record required by the construction.

For the fixed-base ancient germ, the realized object is the local limit

\[
U_{j_n}\to U_\infty,
\qquad
\Omega_{j_n}\to\Omega_\infty
\]

in the compactness topology already established on the relevant branch.

The normalized construction does not need to invent values outside the fixed base. Its retained physical provenance is a **record of the prelimit normalization**, not an assertion that all stages are the same material object.

This distinction prevents Stage III from being misused as a genealogy theorem.

**Status: PROVED/CONSTRUCTIBLE at fixed base on the existing compactness branch; material genealogy NOT supplied.**

---

## 5. Stage IV — definitional describability closure

Stage IV is not an additional physical law. Once the required Stage-I/II/III witnesses and consistency conditions are present, the construction is declared describable within that regime.

Therefore the correct formed object is

\[
\boxed{
\text{the fixed-base local ancient germ with its retained records},
}
\]

not automatically a global material core-plus-tail genealogy.

**Status: CLOSED BY DEFINITION once Stages I–III are satisfied.**

---

## 6. Stage V — typed partial value assignment

The smooth local germ allows ordinary PDE quantities to be assigned on their actual domains. Examples include

\[
U,\quad
\Omega,\quad
S,\quad
|\Omega|,\quad
D^m\Omega,
\]

and pressure oscillation after a gauge convention.

But partial-domain quantities must remain partial.

The clearest example is vorticity direction

\[
\xi=\frac{\Omega}{|\Omega|}.
\]

Its domain is

\[
\boxed{\{(x,t):|\Omega(x,t)|>0\}.}
\]

At \(\Omega=0\), \(\xi\) is **undefined**, not a defined zero direction.

Likewise, if a selected maximum point is nonunique, a single `maximum center` is not automatically a uniquely assigned value. One must either retain the maximizer set, give a selection rule, or record the selected witness as additional data.

**Status: PROVED AS A TYPING REQUIREMENT; the main vorticity-direction calculations already respect the \(\Omega\neq0\) domain.**

---

## 7. Stage VI — channel formation requires role data

A PDE quantity being numerically defined does not by itself mean a DSD channel has formed.

Stage VI requires the combination of

\[
\boxed{
\text{describable construction}
+\text{defined value}
+\text{appropriate role}.
}
\]

Therefore terms such as

`core`, `tail`, `ancestor`, `return`, `singular mechanism`, `remote forcing`

must not be treated as channels merely because a corresponding number can be calculated.

For example, a remote velocity contribution \(W_R\) may be a defined nonzero value while its role as an order-one local singular mechanism fails because the local vorticity dynamic difference tends to zero.

Thus its value channel may exist while the stronger `active local singular mechanism` role is not formed.

**Status: IMPORTANT CURRENT RECLASSIFICATION.**

---

## 8. Stage VII — finite composition only

Stage VII forms a composite description from a **finite set of formed channels**.

Hence the following are legitimate finite compositions once their channels are formed:

\[
J_k,
\qquad
\sum_{k\in F}J_k^{3/2}
\quad(F\Subset\mathbb N),
\]

where \(F\) is finite.

However

\[
\boxed{
\sum_{k=1}^{\infty}J_k^{3/2}
}
\]

is not itself a Stage-VII finite composition merely by writing the series symbol.

Its convergence/divergence belongs to a later static-aggregation/limit layer or requires an explicit extension rule.

Therefore the previous phrase

`the infinite non-L3 tail is a formed Stage-VII global object`

would be too strong.

**Status: CORRECTED.**

---

## 9. DSD-native finite-witness reformulation of cubic divergence

The bounded-Z branch uses

\[
\sum_kJ_k^{3/2}=\infty.
\]

This statement can be reformulated without postulating one infinite formed tail object.

For nonnegative terms, divergence is equivalent to

\[
\boxed{
\forall L>0\;\exists F\Subset\mathbb N:
\sum_{k\in F}J_k^{3/2}>L.
}
\]

If the shell order is fixed, it is enough to use finite initial blocks:

\[
\boxed{
\forall L>0\;\exists K<\infty:
\sum_{k=1}^{K}J_k^{3/2}>L.
}
\]

Every witness on the right is a **finite static composition**.

Thus DSD does not need to form an ontologically single `infinite tail object` in order to retain the full mathematical content of cubic divergence.

The correct structure is a directed family of arbitrarily large finite witnesses.

**Status: PROVED.**

---

## 10. Finite-witness radius / describability depth

Define the threshold witness depth

\[
\boxed{
K_{\mathrm{wit}}(L)
:=
\min\left\{
K:\sum_{k=1}^{K}J_k^{3/2}\ge L
\right\}.
}
\]

Equivalently, with physical/normalized shell radii \(K_k\), define

\[
\boxed{
R_{\mathrm{wit}}(L)
:=K_{K_{\mathrm{wit}}(L)}.
}
\]

This is not a new physical law. It is a finite-witness descriptor answering:

> how far in shell depth must one go before the finite formed static description witnesses cubic mass \(L\)?

The diffuse saturation model shows why this matters. If

\[
J_k^{3/2}\sim\frac1k,
\]

then

\[
\sum_{k\le K}J_k^{3/2}\sim\log K,
\]

so schematically

\[
\boxed{
K_{\mathrm{wit}}(L)\sim e^L.
}
\]

For geometric shell radii \(K_k=q^{k/2}\), the corresponding physical/normalized witness radius can grow even faster as a function of \(L\).

Thus arbitrarily large global static distinction can require arbitrarily remote finite witnesses while remaining locally dynamically negligible.

This provides a DSD-typed explanation of the previously observed diffuse-tail decoupling.

---

## 11. Correction of the previous object hierarchy

The earlier hierarchy should be refined.

### F1 — fixed-base local ancient germ

**FORMED**, conditional on the common diagonal restriction consistency described above.

### F2 — finite shell/block descriptor

**FORMED/COMPOSABLE** once the Stage-VI channel roles are declared.

### F3 — unbounded family of finite cubic witnesses

\[
\forall L\;\exists K<\infty:
\sum_{k\le K}J_k^{3/2}>L.
\]

**VALID STATIC LIMIT PROPERTY / DOES NOT REQUIRE ONE INFINITE STAGE-VII OBJECT.**

### F4 — one persistent material infinite tail genealogy

**NOT DERIVED.**

This is a stronger and more faithful DSD typing than the earlier F3/F4 language.

---

## 12. Consequence for the proof frontier

The bounded-Z obstruction should now be written as

\[
\boxed{
\text{arbitrarily large finite global cubic witnesses}
}
\]

rather than

\[
\boxed{
\text{one already-formed infinite persistent tail object}.
}
\]

Combined with local dynamic descriptive equivalence, the actual unresolved relation is

\[
\boxed{
\begin{array}{c}
\forall L>0:\text{ a finite shell block witnesses cubic mass }>L,\\
\text{while every sufficiently remote part has vanishing effect}\
\text{on each fixed local vorticity dynamic base.}
\end{array}
}
\]

This is not a contradiction by itself. It identifies the remaining mismatch as one between **unbounded static witness depth** and **fixed-base local dynamic closure**.

The next DSD quantity to audit is therefore not `tail existence` but the growth law of

\[
R_{\mathrm{wit}}(L)
\]

and whether first-hitting formation/dynamics impose any upper bound on that growth incompatible with local decoupling.

Global regularity remains **UNPROVED**.