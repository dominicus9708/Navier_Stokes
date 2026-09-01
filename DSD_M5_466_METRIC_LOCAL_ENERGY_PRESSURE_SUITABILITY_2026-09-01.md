# DSD M5-466 — Metric local-energy identity and pressure decomposition

Date: 2026-09-01

Status: **THE TIME-DEPENDENT METRIC COVECTOR SYSTEM HAS A NATURAL LOCAL ENERGY BALANCE WITH ONLY ONE EXTRA LOWER-ORDER `G'` SOURCE TERM / THE PRESSURE IS RECOVERED FROM A SPATIALLY CONSTANT UNIFORMLY ELLIPTIC OPERATOR AND SPLITS INTO THE STANDARD QUADRATIC CZ PRESSURE PLUS A LOWER-ORDER METRIC-VARIATION PART / THIS SUPPLIES THE SUITABILITY/PRESSURE STRUCTURE NEEDED FOR METRIC WEAK-`L3` COMPACTNESS, MODULO STANDARD APPROXIMATION DETAILS / GLOBAL REGULARITY REMAINS UNPROVED.**

Let

\[
m=Cw,
\qquad
w=Gm,
\qquad
\nabla\cdot w=\nabla\cdot(Gm)=0.
\]

Use the covector equation

\[
\partial_t m
+(w\cdot\nabla)m
+(\nabla w)^Tm
=-\nabla\Pi
+\nabla\cdot(G\nabla m).
\]

Define the metric kinetic-energy density

\[
\boxed{
e_C:=m\cdot Gm=w\cdot Cw.}
\]

## 1. Local energy identity

Because `G=G(t)` only,

\[
m_t\cdot w
=\frac12\partial_t e_C
-\frac12m\cdot G'm.
\]

Moreover the two Lie-transport terms satisfy

\[
[(w\cdot\nabla)m]\cdot w
+[(\nabla w)^Tm]\cdot w
=w\cdot\nabla e_C.
\]

Since `div w=0`, this is `div(w e_C)`.

The pressure term is

\[
-\nabla\Pi\cdot w=-\nabla\cdot(\Pi w).
\]

For diffusion,

\[
w\cdot\nabla\cdot(G\nabla m)
=\nabla\cdot\mathcal F_G-\mathcal D_G,
\]

where the flux is explicit and

\[
\boxed{
\mathcal D_G
=
G_{ij}G_{k\ell}
(\partial_i m_\ell)(\partial_jm_k)
\ge c_\kappa|\nabla m|^2
}
\]

on a uniformly elliptic metric class.

Therefore smooth solutions obey

\[
\boxed{
\frac12\partial_t e_C
+\nabla\cdot(w e_C+\Pi w-\mathcal F_G)
+\mathcal D_G
=
\frac12m\cdot G'm.
}
\]

For nonnegative compact cutoffs this yields the natural metric local-energy inequality after weak lower semicontinuity. The right-hand side is a controlled lower-order source when `G'` is locally bounded.

## 2. Pressure equation

For pressure reconstruction it is convenient to use the equivalent form

\[
\partial_t m+(w\cdot\nabla)m
=-\nabla p+\nabla\cdot(G\nabla m),
\]

where the gradient `((grad w)^T m)` has been absorbed into `p`.

Differentiate the constraint

\[
\nabla\cdot(Gm)=0.
\]

Since `G` is spatially constant and the metric diffusion commutes with this divergence,

\[
\boxed{
\nabla\cdot(G\nabla p)
=
\nabla\cdot(G'm)
-\nabla\cdot\left(G(w\cdot\nabla)m\right).
}
\]

Using `div w=0`,

\[
(w\cdot\nabla)m=\nabla\cdot(w\otimes m).
\]

Thus the pressure splits as

\[
\boxed{p=p_{NL}+p_{met},}
\]

where

\[
p_{NL}
=-(\nabla\cdot G\nabla)^{-1}
\nabla\cdot\,G\nabla\cdot(w\otimes m),
\]

and

\[
p_{met}
=(\nabla\cdot G\nabla)^{-1}
\nabla\cdot(G'm).
\]

The first is an order-zero constant-coefficient CZ operator on `w tensor m`. Hence

\[
\boxed{
\|p_{NL}\|_{L^r}
\le C_{r,\kappa}\|w\otimes m\|_{L^r},
\qquad1<r<\infty.
}
\]

In particular the critical local class is `L^{3/2}` when `w,m in L3`.

The metric term is one derivative smoother:

\[
p_{met}\sim |D|^{-1}(G'm),
\]

so for an energy correction `m in L2` it belongs locally to the Sobolev/HLS class `L6`, modulo the usual harmless low-frequency pressure constant. Thus it is better than the nonlinear pressure for local-energy compactness.

## 3. Stability consequence

Combined with M5-464--465, a coefficient/data sequence in a common metric class has:

- uniform global metric-energy control of the correction;
- strong local velocity/covector compactness;
- uniform local `L^{3/2}` control of the quadratic pressure;
- locally controlled metric pressure;
- a local-energy inequality with a convergent lower-order coefficient source.

This supplies the suitability structure required for the finite-interval weak-`L^{3,infinity}` stability program.

Firewall: a full published-quality construction still requires the standard approximation and initial-trace bookkeeping. The terminal Besov regularity/Liouville theorem is not claimed here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]