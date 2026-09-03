# DSD M16-028 — A bounded-lift great-circle phase is trivial; any survivor requires zero-set winding

Date: 2026-09-03
Canonical ID: **M16-028**

Status: **INTERNAL TOPOLOGICAL REDUCTION / IN THE RANK-ONE GREAT-CIRCLE BRANCH, THE WEIGHTED HARMONIC-DIRECTOR EQUATION BECOMES THE CONSERVATION LAW `div(rho^2 grad psi)=0`. THE ASSOCIATED PHASE CURRENT HAS A DIVISION-FREE POLYNOMIAL REPRESENTATION IN `W` AND EXTENDS ACROSS VORTICITY ZEROS. IF THE `S^1` DIRECTOR ADMITS A GLOBALLY BOUNDED REAL PHASE LIFT, A CUTOFF ENERGY TEST FORCES THE PHASE TO BE CONSTANT; DIVERGENCE-FREE PLUS `W in L^2(R^3)` THEN FORCES `W=0`. HENCE ANY NONZERO RANK-ONE SURVIVOR MUST CARRY NONTRIVIAL `S^1` WINDING LINKED TO THE VORTICITY ZERO SET / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Great-circle phase equation

M16-026 gives the great-circle form

\[
\xi
=\cos\psi\,e_1+\sin\psi\,e_2
\]

with fixed orthonormal `e_1,e_2` and

\[
\boxed{
\nabla\cdot(\rho^2\nabla\psi)=0.
}
\]

Define the phase current

\[
\boxed{
J_\psi:=\rho^2\nabla\psi.
}
\]

Then

\[
\boxed{\nabla\cdot J_\psi=0.}
\]

---

## 2. Division-free representation across zeros of W

Choose coordinates in the great-circle plane so that

\[
W=(W_1,W_2,0)
=\rho(\cos\psi,\sin\psi,0).
\]

A direct differentiation gives

\[
\boxed{
(J_\psi)_i
=\rho^2\partial_i\psi
=W_1\partial_iW_2-W_2\partial_iW_1.
}
\]

The right-hand side is polynomial in `W` and its first derivatives. Therefore it is smooth (indeed analytic at each ancient time) even where

\[
\rho=|W|=0.
\]

Thus the phase-current conservation law has a globally meaningful division-free formulation.

---

## 3. Finite weighted phase energy

The direction Dirichlet charge is

\[
P_{dir}
=\int\rho^2|\nabla\xi|^2dy.
\]

For a great-circle phase,

\[
|\nabla\xi|=|\nabla\psi|,
\]

so

\[
\boxed{
\int_{\mathbb R^3}\rho^2|\nabla\psi|^2dy
=P_{dir}<\infty.
}
\]

Also

\[
\int\rho^2dy=E<\infty.
\]

These are enough for the cutoff argument below.

---

## 4. Bounded real lift implies zero phase energy

Assume the `S^1` director has a globally defined real phase lift `psi` satisfying

\[
\boxed{|\psi-c|\le M_\psi<\infty}
\]

for some constant `c`.

Let `eta_R` be a standard cutoff equal to `1` on `B_R`, supported in `B_{2R}`, with

\[
|\nabla\eta_R|\le C/R.
\]

Test

\[
\nabla\cdot(\rho^2\nabla\psi)=0
\]

against

\[
\eta_R^2(\psi-c).
\]

Then

\[
\int\eta_R^2\rho^2|\nabla\psi|^2
=-2\int\eta_R(\psi-c)\rho^2\nabla\psi\cdot\nabla\eta_R.
\]

By Cauchy--Young,

\[
\frac12\int\eta_R^2\rho^2|\nabla\psi|^2
\le
C\frac{M_\psi^2}{R^2}
\int_{R<|y|<2R}\rho^2dy.
\]

Since `rho in L^2`, the right-hand side tends to zero as `R -> infinity`. Therefore

\[
\boxed{
\int\rho^2|\nabla\psi|^2dy=0.
}
\]

Hence

\[
\boxed{\nabla\psi=0}
\]

on the active set.

Thus `xi` is constant wherever `W != 0`.

---

## 5. Constant vorticity direction plus L2 forces W=0

Let

\[
\xi\equiv e
\]

with fixed unit vector `e`. Then

\[
W=\rho e.
\]

Because

\[
\nabla\cdot W=0,
\]

we have

\[
\boxed{e\cdot\nabla\rho=0.}
\]

Therefore `rho` is constant along every complete line parallel to `e`.

If `rho` were positive at one point, continuity would give a positive value on the entire corresponding line, producing infinite `L^2(R^3)` norm.

Hence

\[
\boxed{\rho\equiv0}
\]

and

\[
\boxed{W\equiv0.}
\]

This contradicts the marked nonzero hard component.

---

## 6. Topological consequence

A nonzero rank-one great-circle survivor therefore cannot admit a globally bounded real lift of its `S^1` director phase.

Consequently it must use the topology of

\[
\mathbb R^3\setminus Z_W,
\qquad
Z_W:=\{W=0\},
\]

where the phase is undefined as an angle even though the division-free current `J_psi` remains smooth.

The surviving possibility is

\[
\boxed{
B_{wind}^{S^1}:
\text{nontrivial phase winding around components of }Z_W.
}
\]

Equivalently, there must exist closed loops `gamma` in the active complement for which

\[
\boxed{
\frac1{2\pi}\oint_\gamma d\psi
\in\mathbb Z\setminus\{0\}.
}
\]

---

## 7. Audit firewall

This does **not** yet prove that such winding is impossible.

The weight `rho^2` vanishes on the defect set, so the ordinary unweighted harmonic-map/phase energy lower bounds do not directly apply. A phase defect may in principle hide where vorticity amplitude becomes small.

The next correct question is therefore quantitative:

\[
\boxed{
\text{Can analytic vorticity zeros support persistent nonzero }S^1\text{ winding}
\text{ while }P_{dir}\text{ and the CE-H genealogy remain recurrent?}
}
\]

The analytic zero-set / finite-transversal machinery of M13--M14 is directly relevant here.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
