# M19-295 — Local population Poincaré gaps move the remaining low-frequency obstruction into a finite mean-velocity graph

**Date:** 2026-09-16  
**Status:** CALCULATION / LOW-FREQUENCY REDUCTION / FINITE POPULATION-MEAN GRAPH

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-294 isolates the required centered-velocity spectral condition

\[
\Lambda_\eta>\frac1{2\nu}.
\]

A natural response is to refine the active core into smaller material populations, where ordinary Poincaré constants are better. This module shows exactly what such a refinement gains and what it does not.

The unresolved low-frequency energy becomes a finite graph of population mean velocities.

## 2. Finite material partition

Let a closed active core be decomposed into finitely many disjoint material populations

\[
\Omega_{core}=\bigcup_{i=1}^N P_i.
\]

Let

\[
M_i:=|P_i|
\]

or the corresponding material-cutoff mass, and define the population mean velocity

\[
\boxed{
\bar U_i
:=
\frac1{M_i}\int_{P_i}U\,dy.
}
\]

Let

\[
M:=\sum_iM_i,
\qquad
\boxed{
\bar U
:=
\frac1M\sum_iM_i\bar U_i
}
\]

be the core mean velocity.

## 3. Exact ANOVA/variance decomposition

For each population define the internal centered energy

\[
\boxed{
K_i
:=
\frac12\int_{P_i}|U-\bar U_i|^2dy.
}
\]

The global centered core energy is

\[
K_{core}
:=
\frac12\int_{\Omega_{core}}|U-\bar U|^2dy.
\]

Using

\[
U-\bar U
=(U-\bar U_i)+(\bar U_i-\bar U)
\]

and

\[
\int_{P_i}(U-\bar U_i)dy=0,
\]

the cross term vanishes. Therefore

\[
\boxed{
K_{core}
=
\sum_{i=1}^N K_i
+
K_{mean},
}
\]

where

\[
\boxed{
K_{mean}
:=
\frac12
\sum_{i=1}^N
M_i|\bar U_i-\bar U|^2.
}
\]

This identity is exact.

## 4. What local Poincaré gaps control

Suppose every population satisfies

\[
\int_{P_i}|U-\bar U_i|^2dy
\le
C_{P,i}
\int_{P_i}|\nabla U|^2dy.
\]

Then

\[
\boxed{
K_i
\le
\frac{C_{P,i}}2D_i,
}
\]

where

\[
D_i:=\int_{P_i}|\nabla U|^2dy.
\]

If the cells are sufficiently small/nondegenerate that

\[
C_{P,i}<4\nu,
\]

then each **internal** population mode has positive centered dissipation surplus.

But the Poincaré inequalities say nothing directly about

\[
K_{mean}.
\]

## 5. The remaining low-frequency mode is finite dimensional

The vector

\[
\boxed{
\mathbf V
:=(\bar U_1,\ldots,\bar U_N)
}
\]

contains the unresolved between-population velocity information.

Modulo the global Galilean mode

\[
\bar U_1=\cdots=\bar U_N=V,
\]

which is removed by \(\bar U\), the dimension is at most

\[
3(N-1).
\]

Thus population refinement converts the infinite-dimensional low-frequency velocity obstruction into a finite-dimensional **mean-velocity graph mode**:

\[
\boxed{
\text{low-frequency core energy}
\to
K_{mean}(\mathbf V).
}
\]

## 6. Why this mode is not automatically controlled by bulk gradients

To estimate \(K_{mean}\) by \(D_{core}\), one needs quantitative communication between neighboring populations.

Schematically a discrete graph Poincaré inequality would require edge conductances \(g_{ij}>0\) such that

\[
\boxed{
\sum_iM_i|\bar U_i-\bar U|^2
\le
C_G
\sum_{(i,j)}g_{ij}|\bar U_i-\bar U_j|^2,
}
\]

and then a trace/bridge inequality connecting

\[
g_{ij}|\bar U_i-\bar U_j|^2
\]

to actual velocity-gradient cost near the shared interface.

Neither inequality follows merely from finite population count or local Poincaré gaps.

Thin necks, weak interfaces, large separation, or geometry decompactification can make the effective graph conductance small.

## 7. Relation to existing graph currents

M18-089 and M19-286 already produced finite conservative graphs for

- amplitude diffusion exchange;
- pressure/viscous kinetic-energy exchange.

M19-295 introduces a different graph variable: the population mean velocities \(\bar U_i\).

The corresponding low-frequency coercivity problem is not an exchange-current conservation law; it is a **graph spectral/conductance problem**.

A large internal exchange current does not by itself imply a large mean-velocity gap, and a mean-velocity gap does not by itself determine the sign of the energy current.

These objects must remain distinct.

## 8. Material momentum evolution of the graph nodes

M19-293 gives for each population

\[
\mathbf P_i'
=
\mathbf P_i+\mathbf X_{M,i},
\qquad
M_i'=\frac32M_i.
\]

Since

\[
\bar U_i=\mathbf P_i/M_i,
\]

we obtain

\[
\boxed{
\bar U_i'
=-\frac12\bar U_i
+
\frac{\mathbf X_{M,i}}{M_i}.
}
\]

Thus the population-mean graph is a finite forced dissipative system, with forcing supplied by pressure/viscous momentum exchange across material interfaces.

Internal momentum exchanges cancel in the total momentum balance, but they can sustain nontrivial relative mean velocities.

## 9. New exact frontier

The velocity spectral route now splits as

\[
\boxed{
\mathcal T_{vel}^{spectral}
\Longrightarrow
\mathcal T_{local}^{Poincare}
+
\mathcal T_{mean}^{graph-gap}.
}
\]

Here:

- \(\mathcal T_{local}^{Poincare}\) controls within-population fluctuations;
- \(\mathcal T_{mean}^{graph-gap}\) controls the finite vector of relative population means.

Localizing more finely can improve the first while worsening interface complexity in the second. There is no automatic free spectral gain from refinement.

## 10. Sufficient graph closure condition

A sufficient theorem would provide a uniform constant \(C_{graph}\) such that

\[
\boxed{
K_{mean}
\le
C_{graph}D_{core}
}
\]

with the combined internal+graph constant small enough that

\[
K_{core}
<2\nu D_{core}.
\]

Equivalently,

\[
\boxed{
\frac{D_{core}}{K_{core}}
>\frac1{2\nu}.
}
\]

This is simply the global centered velocity spectral threshold rewritten in finite-population coordinates, but the decomposition identifies exactly where the low-frequency obstruction lives.

## 11. Next target

Audit whether the finite persistent-population geometry supplies a uniform lower bound on inter-population conductance/trace coupling.

If not, record the precise survivor as

\[
\boxed{
G_{mean\text{-}velocity\ graph\ decompactification}.
}
\]

This would connect the current low-frequency problem directly to the older thin-neck/bi-Lipschitz geometry firewall rather than leaving it as an abstract \(\dot H^{-1}\) defect.

---

\[
\boxed{\text{M19-295 COMPLETE; LOCAL POINCARÉ CONTROL DOES NOT REMOVE LOW FREQUENCY, IT CONCENTRATES IT INTO A FINITE POPULATION-MEAN VELOCITY GRAPH.}}
\]
