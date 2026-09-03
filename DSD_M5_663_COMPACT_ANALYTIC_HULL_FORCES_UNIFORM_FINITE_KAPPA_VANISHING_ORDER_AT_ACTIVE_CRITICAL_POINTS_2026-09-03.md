# DSD M5-663 — The compact analytic CE-H hull forces a uniform finite kappa vanishing order at active critical points

Date: 2026-09-03

Status: **INTERNAL COMPACTNESS/ANALYTICITY RIGIDITY / ON THE FIXED HIGH-AMPLITUDE CORE `rho>=a0`, KAPPA IS A SMOOTH/ANALYTIC QUOTIENT BECAUSE `Delta W=kappa W` AND `W` DOES NOT VANISH / IF ALL SPATIAL DERIVATIVES OF `kappa-kappa(p)` VANISHED AT AN ACTIVE POINT, ANALYTICITY WOULD MAKE KAPPA LOCALLY CONSTANT; THEN `Delta W=cW` ON AN OPEN SET AND ANALYTIC CONTINUATION WOULD FORCE A GLOBAL L2 LAPLACIAN EIGENFIELD, WHICH IS TRIVIAL / COMPACTNESS OF THE MARKED ALL-ORDER HULL THEREFORE UPGRADES POINTWISE FINITE ORDER TO A UNIFORM FINITE ORDER `m_*` AND A UNIFORM JET FLOOR `c_*` / HIGHER-DEGENERACY SILENT PATCHING CANNOT ESCAPE INTO INFINITE-ORDER FLATNESS / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Active high-amplitude region

Work on the fixed retained core where

\[
\boxed{\rho=|W|\ge a_0>0.}
\]

There the CE-H eigenfield identity

\[
\Delta W=\kappa W
\]

defines `kappa` without nodal ambiguity, for example by

\[
\boxed{
\kappa
=
\frac{W\cdot\Delta W}{|W|^2}.
}
\]

The compact all-order smooth hull and standard parabolic spatial analyticity make `kappa` smooth and real analytic on these retained high-amplitude neighborhoods.

---

## 2. Infinite-order flatness would force a local constant

Let `p` be an active point and suppose

\[
\nabla^m\kappa(p)=0
\qquad\forall m\ge1.
\]

Then the Taylor series of

\[
\kappa-\kappa(p)
\]

vanishes identically.

By real analyticity,

\[
\boxed{
\kappa\equiv c
}
\]

on a neighborhood of `p`, with `c=kappa(p)`.

Consequently

\[
\boxed{
\Delta W-cW=0
}
\]

on that open neighborhood.

---

## 3. Analytic continuation of the constant-eigenvalue relation

At a fixed positive ancient time the strong Navier-Stokes state is spatially analytic.

Hence the vector field

\[
\Delta W-cW
\]

is analytic.

If it vanishes on one open set, it vanishes on the connected whole-space slice:

\[
\boxed{
\Delta W=cW
\quad\text{on }\mathbb R^3.
}
\]

Take the Fourier transform:

\[
-(|\xi|^2)\widehat W(\xi)
=
c\widehat W(\xi).
\]

Thus `hat W` is supported on

\[
|\xi|^2=-c.
\]

If `c>0`, the support is empty.

If `c=0`, it is the single point `xi=0`.

If `c<0`, it is a sphere.

No nonzero `L2` function can be supported on a Lebesgue-null sphere/point.

Therefore

\[
\boxed{W\equiv0,}
\]

contradicting the marked hard component.

Hence an active point cannot be infinitely flat in `kappa`.

---

## 4. Pointwise finite vanishing order

For every active point `p` there exists a finite integer `m(p)>=1` such that

\[
\boxed{
\nabla^{m(p)}\kappa(p)\ne0.
}
\]

At a critical point,

\[
\nabla\kappa(p)=0,
\]

so `m(p)>=2`.

At the M5-659 higher-degenerate branch with `Hess kappa=0`,

\[
\boxed{m(p)>=3.}
\]

---

## 5. Uniform finite order by compactness

Suppose there were no uniform finite upper bound on the active critical vanishing order.

Then there would exist states `W_n` in the marked compact hull and active points `p_n` in the fixed bounded core such that

\[
\rho_n(p_n)\ge a_0
\]

and

\[
\nabla^m\kappa_n(p_n)=0
\qquad
1\le m\le n.
\]

After passing to a subsequence,

\[
W_n\to W_\infty
\]

in every fixed `C^m` topology on the core and

\[
p_n\to p_\infty.
\]

Because the denominator `rho>=a0` is uniformly separated from zero, the quotients `kappa_n` and all fixed derivatives converge as well.

Therefore

\[
\nabla^m\kappa_\infty(p_\infty)=0
\qquad\forall m.
\]

This is the forbidden infinite-order flatness of Sections 2--3.

Hence there exists

\[
\boxed{m_*<\infty}
\]

such that every active critical point has a nonzero derivative by order `m_*`.

---

## 6. Uniform quantitative jet floor

A second compactness argument gives more.

If no uniform positive floor existed, one could find active critical points with

\[
\max_{2\le m\le m_*}
|\nabla^m\kappa|
\to0.
\]

Passing to a compact limit would again produce an active point with every derivative through `m_*` zero.

By the definition of `m_*`, this is impossible after increasing `m_*` once if necessary to cover the compact active critical set.

Thus there is

\[
\boxed{c_*>0}
\]

such that

\[
\boxed{
\max_{2\le m\le m_*}
|\nabla^m\kappa(p)|
\ge c_*
}
\]

for every retained active critical point.

On the rank-zero branch the maximum can be taken over `3<=m<=m_*`.

---

## 7. Consequence for higher-degenerate sheet patching

The M5-662 unresolved branch cannot hide in an arbitrarily flat analytic critical point.

Instead every such event carries a finite-order jet:

\[
\boxed{
K_{higher}^{degenerate}
\Longrightarrow
J_{kappa}^{(m)},
\qquad
3\le m\le m_*,
\qquad
|\nabla^m\kappa|\ge c_*.
}
\]

Since there are only finitely many possible orders, positive-frequency higher-degeneracy events contain a positive-frequency fixed-order subbranch by pigeonhole.

---

## 8. Why this is not yet a contradiction

All-order Sobolev compactness already permits fixed finite higher derivatives to be nonzero recurrently.

Therefore the jet floor is not itself a forbidden cost.

Its use is structural: it allows the higher-degenerate critical set to be treated by a finite-order moving-branch expansion rather than an uncontrolled infinite-order analytic singularity.

---

## 9. Next target

For a smooth critical hypersurface whose first nonzero normal derivative of `kappa-kappa_Sigma` has order

\[
2\le m\le m_*,
\]

one should compute the first normal derivative of `h=D_B kappa` that detects mismatch between material velocity and critical-surface velocity.

The expected exact leading relation is

\[
\boxed{
(B-V_\Sigma)\cdot n
=
\frac{\partial_n^{m-1}(h-h_\Sigma)}{\partial_n^m\kappa}
}
\]

up to the precise factorial convention.

If this is correct, every finite-order silent fold is either a higher-jet force-creation event or another material barrier, extending M5-660 beyond the rank-one Hessian case.

---

## 10. External-dependency note

The step from infinite-order vanishing to local constancy uses standard real analyticity of strong Navier-Stokes spatial slices.

This should remain marked as an external regularity fact in the final audit.

---

## 11. Firewall

This document treats active points with `rho>=a0` only, where `kappa` is a legitimate analytic scalar quotient.

No global analytic extension of `kappa` through the vorticity nodal set is assumed.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]