# DSD M5-465 — Compactness of metric Calderon energy corrections

Date: 2026-09-01

Status: **THE M5-464 ENERGY CORRECTIONS ARE LOCALLY COMPACT UNDER METRIC COEFFICIENT CONVERGENCE WHEN WRITTEN IN THE COVECTOR VARIABLE `m_U=C U` / THE COVECTOR EQUATION HAS A STANDARD GRADIENT PRESSURE AND NO EXPLICIT `C'` TERM, SO DIVERGENCE-FREE TESTS GIVE A UNIFORM NEGATIVE-SOBOLEV TIME-DERIVATIVE BOUND AND AUBIN--LIONS YIELDS STRONG LOCAL `L2` CONVERGENCE / THIS ESTABLISHES THE CORE COMPACTNESS STEP OF A METRIC LARGE-DATA WEAK-`L3` THEORY, SHORT OF SUITABILITY/TERMINAL REGULARITY / GLOBAL REGULARITY REMAINS UNPROVED.**

Let

\[
w=V+U,
\qquad
m=Cw,
\qquad
m_V=CV,
\qquad
m_U=CU.
\]

The full metric covector equation is

\[
\partial_t m+\mathcal L_wm
=-\nabla\Pi+\nabla\cdot(G\nabla m),
\]

where

\[
\mathcal L_wm
:=(w\cdot\nabla)m+(\nabla w)^Tm.
\]

Subtract the strong equation for `(V,m_V)`:

\[
\boxed{
\partial_t m_U
+\mathcal L_Vm_U
+\mathcal L_Um_V
+\mathcal L_Um_U
=-\nabla\Pi_U
+\nabla\cdot(G\nabla m_U).
}
\]

## 1. Energy bounds

M5-464 gives, uniformly over a compact coefficient class,

\[
\boxed{
U\in L_t^\infty L_x^2
\cap
L_t^2H_x^1.
}
\]

Since `C` is uniformly elliptic and spatially constant,

\[
\boxed{
m_U\in L_t^\infty L_x^2
\cap
L_t^2H_x^1}
\]

with comparable bounds.

The strong component satisfies, for some `p>3`,

\[
V,m_V\in L_t^\infty L_x^{2p}
\]

and the corresponding subcritical derivative bounds from the metric mild theory.

## 2. Pressure-free weak time derivative

Let `phi` be compactly supported and divergence free. Pair the correction equation with `phi`. The pressure vanishes:

\[
\langle\nabla\Pi_U,\phi\rangle=0.
\]

Each Lie-derivative term is a first-order divergence-type bilinear form. On a fixed compact ball, the energy interpolation

\[
U\in L_t^4L_x^3
\]

follows from `L_t^infinity L2` and `L_t^2L6`.

Consequently the quadratic term `L_Um_U` belongs to a standard negative-Sobolev class, schematically

\[
\boxed{
\mathcal L_Um_U
\in L_t^{4/3}H_x^{-1}(B_R).
}
\]

The mixed terms with `V,m_V` are at least as good because the strong component is subcritical. The diffusion term belongs to `L_t^2H^{-1}`.

Therefore

\[
\boxed{
\partial_t m_U
\text{ is bounded in }
L^{4/3}(I;H^{-1}(B_R))
}
\]

for every compact space-time cylinder.

## 3. Aubin--Lions compactness

The embeddings

\[
H^1(B_R)\Subset L^2(B_R)\hookrightarrow H^{-1}(B_R)
\]

and the bounds above give

\[
\boxed{
m_{U,n}\to m_U
\quad\text{strongly in }L^2_{loc}(space\text{-}time)
}
\]

after a subsequence for any coefficient/data sequence with common bounds.

If

\[
C_n\to C
\]

uniformly in time, then

\[
U_n=G_nm_{U,n}
\to
Gm_U=U
\]

strongly locally in `L2` as well.

This is sufficient to pass the quadratic energy-correction terms in the distributional covector equation.

## 4. What this establishes

Together with M5-463, we now have the following stability skeleton for a Calderon-decomposed metric sequence:

1. strong/small component `V_n` converges in Kato spaces;
2. energy correction `U_n` is uniformly bounded;
3. `U_n` converges strongly locally after subselection;
4. coefficient histories converge;
5. the limit satisfies the metric covector equation distributionally.

## 5. What is not yet claimed

The Albritton--Barker/Barker--Seregin--Sverak weak-`L^{3,infinity}` class contains additional structure beyond distributional energy compactness, notably a suitable/local-energy formulation, pressure convergence, and precise initial/terminal trace properties.

Those pieces are not silently inferred here.

The remaining transfer gap is now concentrated in:

- metric pressure/local-energy suitability;
- weak-`L^{3,infinity}` trace stability;
- terminal Besov regularity and Liouville contradiction.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]