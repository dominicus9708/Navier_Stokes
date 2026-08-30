# DSD M5-328 — Atom Parent H1–H2 Product: First-Hitting Scaling and Cell-Alignment Audit

Date: 2026-08-30

Status: **THE M5-327 PARENT PRODUCT IS EXACTLY SCALE INVARIANT IN FIRST-HITTING VARIABLES / NON-H PALINSTROPHY WOULD CONTROL ITS SECOND FACTOR ON AN ALIGNED BOUNDED LERAY CELL / HUANG ATOM CELLS ARE NOT AUTOMATICALLY FIRST-HITTING STAGE CELLS, SO THE REMAINING ISSUE IS CELL ALIGNMENT / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

`M5-327` proves that every sufficiently late atom-selected Huang cell

\[
I_j=[\tau_j,\tau_{j+1}]
\]

obeys

\[
\boxed{
 d_j h_j\ge c_{12}\nu^2,
}
\]

where

\[
d_j=\int_{I_j}\|\nabla u\|_2^2dt,
\qquad
h_j=\int_{I_j}\|\nabla^2u\|_2^2dt.
\]

The repository already has normalized first-hitting palinstrophy and local-H2 ceilings on non-H corridors. This note checks whether they are the same quantities.

## 2. Exact first-hitting scaling

Fix a natural first-hitting length `r` and define

\[
U(y,\tau)
=r\,u(X+ry,t_0+r^2\tau).
\]

Then

\[
\nabla_yU=r^2\nabla_xu,
\qquad
\nabla_y^2U=r^3\nabla_x^2u,
\]

and

\[
dx=r^3dy,
\qquad
dt=r^2d\tau.
\]

Therefore

\[
\boxed{
\int_{I_{phys}}\|\nabla u\|_{L^2_x}^2dt
=r
\int_{I_{norm}}\|\nabla U\|_{L^2_y}^2d\tau.
}
\]

Likewise

\[
\boxed{
\int_{I_{phys}}\|\nabla^2u\|_{L^2_x}^2dt
=r^{-1}
\int_{I_{norm}}\|\nabla^2U\|_{L^2_y}^2d\tau.
}
\]

Hence the product is exactly invariant:

\[
\boxed{
 d_{phys}h_{phys}
=D_I H_I,
}
\]

with

\[
D_I:=\int_{I_{norm}}\|\nabla U\|_2^2d\tau,
\qquad
H_I:=\int_{I_{norm}}\|\nabla^2U\|_2^2d\tau.
\]

Thus the atom condition becomes

\[
\boxed{D_IH_I\ge c_{12}\nu^2.}
\]

## 3. Second derivative equals palinstrophy for divergence-free fields

For a smooth divergence-free whole-space field,

\[
\|\nabla U\|_2^2=\|\Omega\|_2^2,
\]

and Fourier calculus gives

\[
\boxed{
\|\nabla^2U\|_2^2
=\|\nabla\Omega\|_2^2.
}
\]

Hence

\[
\boxed{
H_I=\int_{I_{norm}}P_\Omega(\tau)d\tau.
}
\]

This is the same global normalized palinstrophy that appears in the repository non-H hierarchy, not merely an analogous derivative norm.

## 4. Consequence on an aligned non-H stage

Suppose an atom cell, after choosing the relevant first-hitting scale, is contained in a normalized interval of length at most `L_*` on which the non-H corridor supplies

\[
\boxed{P_\Omega(\tau)\le P_*}
\]

for all times in the interval.

Then

\[
\boxed{H_I\le P_*L_*.}
\]

The atom product floor gives

\[
\boxed{
D_I\ge
\frac{c_{12}\nu^2}{P_*L_*}>0.
}
\]

Thus an aligned atom cell necessarily carries a fixed normalized dissipation amount.

This is a legitimate conclusion, but it is not by itself a contradiction: physical dissipation of that stage is `r D_I`, and geometric `r` is summable along a Type-I tower.

## 5. What the local-H2 compactness lemma contributes

`PV_LOCAL_COMPACTNESS_BOOTSTRAP_2026-08-20.md` proves that on a bounded normalized threshold cell, non-H palinstrophy plus no-shell-H escalation gives uniform local H2 compactness.

This is consistent with the aligned estimate above. It does not provide a universal small upper bound on `H_I`; it supplies boundedness unless a shell-H/T exit occurs.

Therefore M5-327 cannot be contradicted merely by citing local-H2 precompactness.

## 6. The true alignment issue

Huang's times `tau_j` are selected from nested atomic/Hodge level crossings. The first-hitting tower times are selected by vorticity amplitude thresholds.

These are different selection mechanisms.

There is currently no proved identity of the form

\[
\boxed{
[\tau_j,\tau_{j+1}]
=\text{one first-hitting stage}
}
\]

or even a uniform bounded-overlap containment in first-hitting stages.

Without such a bridge one may not import a stagewise palinstrophy ceiling into every Huang cell.

## 7. Formation-axiom decomposition of the time-cell problem

The correct descriptors for a dangerous time cell are

\[
\boxed{
\mathscr C
=(\text{atom level},\text{vorticity level},\text{duration},\text{overlap count},D_I,H_I).
}
\]

The cell can fail alignment in only three structural ways:

1. `C_short`: it lies inside one/finitely many first-hitting stages;
2. `C_long`: it crosses increasingly many stages;
3. `C_offset`: its endpoints repeatedly sit near stage boundaries but the overlap number remains bounded.

Cases 1 and 3 permit bounded-overlap import of stage estimates. Case 2 is the genuinely new branch.

## 8. Long-cell consequence

If a Huang cell crosses `N_j -> infinity` first-hitting stages, then it contains a long normalized history of geometric vorticity-amplitude change.

This is not automatically a contradiction, but it must be routed to one of the already existing historical mechanisms:

- repeated projective/shape action;
- repeated replacement/export;
- H-frequency escalation;
- passive historical tail.

Thus cell misalignment is not a free technical nuisance; an unbounded overlap count is itself a historical long-memory object.

A quantitative routing theorem is still required.

## 9. Axis-property interpretation

The product `D_I H_I` contains no direction information. The stronger M5-326 source

\[
\int_{I_j}\|(\nabla u)^Tg_j\|_2dt
\]

retains the alignment between the parent gradient and the Helmholtz leakage direction.

If temporal alignment with first-hitting stages proves difficult, this directional source may be localized directly in time and space without requiring exact stage endpoints.

## 10. Firewall

Do not identify Huang atom cells with first-hitting cells merely because both approach `T_*`.

Do not identify the remote annular critical-H2 quantity

\[
\mathfrak E_2(R)=R^3\int_{A_R}|\nabla^2U|^2
\]

with the whole-space time-cell quantity

\[
H_I=\int_I\|\nabla^2U\|_2^2d\tau.
\]

They are different objects, despite sharing second derivatives.

## 11. Updated target

The next useful lemma is a **cell-overlap theorem**:

\[
\boxed{
\text{every late Huang atom cell either overlaps only O(1) first-hitting stages,}
}
\]

or

\[
\boxed{
\text{unbounded stage overlap forces an already typed H/T historical action.}
}
\]

This would connect the atom parent product to the existing first-hitting proof tree without conflating normalizations.

## 12. Audit verdict

### PROVED

- exact scaling of the two parent actions;
- exact scale invariance of their product;
- normalized H2 action equals integrated palinstrophy;
- an aligned bounded-length non-H cell has a bounded H2 factor and fixed dissipation floor.

### OPEN

- Huang-cell / first-hitting-stage overlap theorem;
- contradiction from the fixed critical product;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
