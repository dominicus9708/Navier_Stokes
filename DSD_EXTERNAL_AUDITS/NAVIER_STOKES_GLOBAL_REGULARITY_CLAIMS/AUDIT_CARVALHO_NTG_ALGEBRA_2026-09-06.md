# DSD Audit — Carvalho NTG Algebra

Date: 2026-09-06
Source: Felipe Gaspar Gomes de Carvalho, *An Algebraic Reformulation of the Incompressible Navier–Stokes Equations: Sharp Estimates and a Regularity Criterion via the NTG Algebra*, Aug 10 2026, DOI 10.13140/RG.2.2.29020.55689.
Audit status: **BASE EVOLUTION COEFFICIENT INCONSISTENCY**

## 1. Claimed mechanism

The paper defines the traceless product at `λ=1/3`

\[
A\star B:=AB-\frac13\operatorname{tr}(AB)I,
\]

applies it to the velocity gradient `G=∇u`, separates the deviatoric pressure Hessian, derives a sharp correlation estimate, and then obtains a coercive differential inequality for

\[
F(t)=\int\operatorname{tr}(G^3)dx.
\]

The global regularity conclusion depends on the exact algebraic evolution equation for `G`.

## 2. Direct derivation from Navier–Stokes

Differentiate

\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u.
\]

For `G=∇u`,

\[
D_tG+G^2=-P+\nu\Delta G,
\qquad P:=\nabla^2p.
\]

Taking trace and using `tr G=0` gives the pressure Poisson relation

\[
\Delta p=-\operatorname{tr}(G^2).
\]

Decompose

\[
G^2=G\star G+\frac13\operatorname{tr}(G^2)I
\]

and

\[
P=P_{dev}+\frac13\Delta p\,I
=P_{dev}-\frac13\operatorname{tr}(G^2)I.
\]

Substitution yields

\[
D_tG
+
G\star G
+
\frac13\operatorname{tr}(G^2)I
=
-P_{dev}
+
\frac13\operatorname{tr}(G^2)I
+
u\Delta G.
\]

The isotropic terms cancel:

\[
\boxed{
D_tG+G\star G=-P_{dev}+\nu\Delta G.
}
\]

The coefficient of `G⋆G` is exactly **1** with the paper's stated star-product definition.

## 3. Manuscript's cubic evolution

The manuscript's displayed cubic-functional calculation gives a nonlinear term

\[
-\frac92\int\operatorname{tr}\bigl(G^2(G\star G)\bigr)dx.
\]

Because

\[
\frac d{dt}\operatorname{tr}(G^3)
=3\operatorname{tr}(G^2G_t),
\]

this coefficient corresponds to an evolution equation containing

\[
\frac32 G\star G,
\]

not coefficient 1.

With the exact coefficient 1, that term should instead carry coefficient

\[
-3\int\operatorname{tr}\bigl(G^2(G\star G)\bigr)dx,
\]

before accounting for pressure and viscosity.

## 4. Consequence for sharp dissipativity

The manuscript balances the nonlinear term against the pressure correlation and derives a negative coefficient using the stated sharp bound. Changing `9/2` to `3` changes that coercivity margin materially.

Therefore all downstream constants must be recomputed from the corrected base equation. It is not legitimate to retain the old pressure/nonlinearity margin after changing the coefficient.

## 5. Secondary algebra checks required

After correcting the base equation, separate audits are required for:

- the identity `tr(G^2(G⋆G)) = ||G⋆G||_F^2` for non-symmetric general `G`;
- the pressure correlation bound and its global integration;
- sign properties of `∫tr(G^3)` for general incompressible gradients;
- the bridge from the cubic functional to an LPS norm.

These are not decided by the present coefficient audit.

## 6. DSD verdict

\[
\boxed{
\text{The exact differentiated NSE gives coefficient 1, not 3/2, for }G\star G.
}
\]

Because the paper's central dissipative inequality uses the latter coefficient, the global regularity closure must be rebuilt from the corrected equation before it can be assessed.

Global regularity remains unproved.
