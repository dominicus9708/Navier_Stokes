# Bounded-Z Tail Local Decoupling and Cutoff-Commutator Decay

Date: 2026-08-25

Status: **LOCAL BIOT–SAVART TAIL DECOUPLING PROVED / PRESSURE FAR-FIELD DECAY PROVED / VORTICITY CUTOFF COMMUTATOR DECAYS IN H^{-1} / NO GLOBAL L3 CORE-SOLUTION EXTRACTION YET / GLOBAL REGULARITY UNPROVED.**

## 1. Scope

This note applies only on the corrected bounded-normalized-enstrophy ancient branch

\[
\boxed{
\sup_{t\le0}\|\Omega(t)\|_2^2\le Z_*<\infty.
}
\]

For a divergence-free whole-space field,

\[
\|\nabla U\|_2=\|\Omega\|_2,
\]

and homogeneous Sobolev gives

\[
\boxed{
\|U\|_6\le C_S Z_*^{1/2}.
}
\]

The purpose is to determine whether a non-\(L^3\) remote tail can still exert an order-one instantaneous influence on a fixed recurrent core.

---

## 2. Biot–Savart far-tail decomposition

Write schematically

\[
U=\mathcal K*\Omega,
\qquad
|\nabla^m\mathcal K(z)|\le C_m|z|^{-2-m}.
\]

Fix a core ball \(B_M\). For \(R>2M\), define the remote-vorticity contribution

\[
U_{>R}(x)
:=
\int_{|y|>R}\mathcal K(x-y)\Omega(y)\,dy.
\]

For \(|x|\le M\),

\[
|x-y|\ge\frac12|y|.
\]

Hence for every integer \(m\ge0\),

\[
\begin{aligned}
|\nabla^mU_{>R}(x)|
&\le
C_m
\int_{|y|>R}|y|^{-2-m}|\Omega(y)|dy\\
&\le
C_m
\|\Omega\|_{L^2(|y|>R)}
\left(
\int_{|y|>R}|y|^{-4-2m}dy
\right)^{1/2}.
\end{aligned}
\]

Since in three dimensions

\[
\int_R^\infty r^{-4-2m}r^2dr
\asymp R^{-1-2m},
\]

we obtain

\[
\boxed{
\|\nabla^mU_{>R}\|_{L^\infty(B_M)}
\le
C_{m,M}
R^{-m-1/2}
\|\Omega\|_{L^2(|y|>R)}.
}
\]

In particular, using only the global bounded-\(Z\) ceiling,

\[
\boxed{
\sup_{t\le0}
\|\nabla^mU_{>R}(t)\|_{L^\infty(B_M)}
\le
C_{m,M}Z_*^{1/2}R^{-m-1/2}.
}
\]

Therefore the remote tail vanishes on each fixed core ball in every fixed spatial derivative order.

**Status: PROVED.**

---

## 3. Shell-by-shell form

For a remote annulus of radius \(K\) with

\[
J_K
=K\int_{A_K}|\nabla U|^2dy,
\]

we have

\[
\|\Omega\|_{L^2(A_K)}
\le C\left(\frac{J_K}{K}\right)^{1/2}.
\]

Its contribution to core strain is bounded by

\[
\boxed{
\|\nabla U_K\|_{L^\infty(B_M)}
\le
C_MJ_K^{1/2}K^{-2}.
}
\]

More generally,

\[
\boxed{
\|\nabla^mU_K\|_{L^\infty(B_M)}
\le
C_{m,M}J_K^{1/2}K^{-m-1}
\qquad(m\ge0),
}
\]

where \(m=0\) gives \(J_K^{1/2}K^{-1}\).

On bounded-overlap geometric annuli,

\[
\sum_k\frac{J_k}{K_k}
\lesssim Z_*.
\]

Hence Cauchy–Schwarz yields, for example,

\[
\sum_{k\ge N}J_k^{1/2}K_k^{-2}
=
\sum_{k\ge N}
\left(\frac{J_k}{K_k}\right)^{1/2}K_k^{-3/2}
\le
C Z_*^{1/2}K_N^{-3/2}.
\]

Thus the total remote-shell strain is absolutely summable and its tail vanishes quantitatively.

**Status: PROVED.**

---

## 4. Far pressure also decouples locally

Use the whole-space pressure representation

\[
P=\mathcal L_{ij}*(U_iU_j),
\]

where

\[
|\nabla^m\mathcal L(z)|\le C_m|z|^{-3-m}.
\]

Define the remote-source pressure contribution

\[
P_{>R}(x)
:=
\int_{|y|>R}
\mathcal L_{ij}(x-y)U_i(y)U_j(y)dy.
\]

Since \(U^2\in L^3\), Hölder with exponents \(3\) and \(3/2\) gives for \(|x|\le M\),

\[
\begin{aligned}
|\nabla^mP_{>R}(x)|
&\le
C_{m,M}\|U\|_{L^6(|y|>R)}^2
\left(
\int_{|y|>R}|y|^{-(3+m)3/2}dy
\right)^{2/3}\\
&\le
C_{m,M}\|U\|_6^2R^{-m-1}.
\end{aligned}
\]

Hence

\[
\boxed{
\sup_{t\le0}
\|\nabla^mP_{>R}(t)\|_{L^\infty(B_M)}
\le
C_{m,M}Z_*R^{-m-1}.
}
\]

Pressure itself is defined up to a function of time, so the physically relevant statements are pressure oscillation and derivatives. In particular,

\[
\boxed{
\|\nabla P_{>R}\|_{L^\infty(B_M)}
\lesssim Z_*R^{-2}.
}
\]

**Status: PROVED.**

---

## 5. A smooth vorticity cutoff and its exact commutator

Choose \(\chi_R\in C_c^\infty\) with

\[
\chi_R=1\text{ on }B_R,
\qquad
\chi_R=0\text{ outside }B_{2R},
\]

and

\[
|\nabla\chi_R|\le CR^{-1},
\qquad
|\Delta\chi_R|\le CR^{-2}.
\]

Set

\[
\Omega_R=\chi_R\Omega.
\]

Starting from

\[
\partial_t\Omega+U\cdot\nabla\Omega
=\Omega\cdot\nabla U+\nu\Delta\Omega,
\]

a direct product calculation gives

\[
\boxed{
\begin{aligned}
\partial_t\Omega_R
+U\cdot\nabla\Omega_R
-\nu\Delta\Omega_R
&=
\chi_R(\Omega\cdot\nabla U)
+\mathcal C_R,
\\
\mathcal C_R
&=
(U\cdot\nabla\chi_R)\Omega
-2\nu\nabla\chi_R\cdot\nabla\Omega
-\nu(\Delta\chi_R)\Omega.
\end{aligned}
}
\]

The entire failure of static truncation to commute with the vorticity dynamics is localized to the transition annulus

\[
A_R=B_{2R}\setminus B_R.
\]

**Status: PROVED.**

---

## 6. Nonlinear transport commutator vanishes in \(H^{-1}\)

By Sobolev duality,

\[
L^{6/5}(\mathbb R^3)\hookrightarrow H^{-1}(\mathbb R^3).
\]

On \(A_R\),

\[
\|U\Omega\|_{3/2}
\le
\|U\|_6\|\Omega\|_2.
\]

Because \(|A_R|\asymp R^3\), finite-volume embedding gives

\[
\|f\|_{6/5}(A_R)
\le
|A_R|^{1/6}\|f\|_{3/2}(A_R)
\lesssim
R^{1/2}\|f\|_{3/2}(A_R).
\]

Therefore

\[
\begin{aligned}
\|(U\cdot\nabla\chi_R)\Omega\|_{H^{-1}}
&\le
CR^{-1}
\|U\Omega\|_{6/5(A_R)}\\
&\le
CR^{-1/2}
\|U\|_6\|\Omega\|_2.
\end{aligned}
\]

Using bounded \(Z_*\),

\[
\boxed{
\sup_{t\le0}
\|(U\cdot\nabla\chi_R)\Omega\|_{H^{-1}}
\le
CZ_*R^{-1/2}.
}
\]

Thus the nonlinear transport boundary action vanishes uniformly as \(R\to\infty\).

**Status: PROVED.**

---

## 7. Viscous cutoff commutator also vanishes in \(H^{-1}\)

Let

\[
\mathcal V_R
=-2\nu\nabla\chi_R\cdot\nabla\Omega
-\nu(\Delta\chi_R)\Omega.
\]

For a test field \(\varphi\in H^1\), integrate the first term by parts:

\[
\begin{aligned}
\langle\mathcal V_R,\varphi\rangle
&=
\nu\int(\Delta\chi_R)\Omega\cdot\varphi
+2\nu\int\Omega\,\nabla\chi_R:\nabla\varphi.
\end{aligned}
\]

Hence

\[
|\langle\mathcal V_R,\varphi\rangle|
\le
C\nu
\left(
R^{-2}\|\Omega\|_2\|\varphi\|_2
+R^{-1}\|\Omega\|_2\|\nabla\varphi\|_2
\right).
\]

Therefore for \(R\ge1\),

\[
\boxed{
\|\mathcal V_R\|_{H^{-1}}
\le
C\nu Z_*^{1/2}R^{-1}.
}
\]

**Status: PROVED.**

---

## 8. Total dynamic cutoff defect

Combining Sections 6 and 7,

\[
\boxed{
\sup_{t\le0}\|\mathcal C_R(t)\|_{H^{-1}}
\le
C\left(
Z_*R^{-1/2}
+\nu Z_*^{1/2}R^{-1}
\right).
}
\]

Thus

\[
\boxed{
\mathcal C_R\to0
\quad\text{in }L_t^\infty H_x^{-1}
\text{ as }R\to\infty.
}
\]

This is stronger than merely saying that the tail's instantaneous strain is small: even the vorticity cutoff's boundary transport and viscosity errors vanish in a negative Sobolev topology.

**Status: PROVED.**

---

## 9. What this does not yet produce

For each finite \(R\), \(\Omega_R\) is compactly supported, and its Biot–Savart velocity has improved far-field decay and belongs to strong critical spaces such as \(L^3\) under the usual cancellation/regularity conditions.

However, \((U_R,\Omega_R)\) is not an exact Navier–Stokes solution: the equation contains \(\mathcal C_R\), and the nonlinear term also involves the full \(U\) and \(\nabla U\).

Letting \(R\to\infty\) makes the defect vanish, but it simultaneously restores the entire non-\(L^3\) tail. The strong \(L^3\) norms of the truncations need not remain uniformly bounded; indeed the cubic-tail branch is exactly the case where they can diverge.

Therefore the following tempting conclusion is invalid:

\[
\boxed{
\text{tail locally decouples}
\not\Rightarrow
\text{there exists an exact global }L^3\text{ ancient core solution}.
}
\]

**Status: NOT DERIVED.**

---

## 10. External Liouville-theorem cross-check

Koch–Nadirashvili–Seregin–Šverák, *Liouville theorems for the Navier–Stokes equations and applications*, Acta Mathematica 203 (2009), 83–105, arXiv:0709.3599, studies bounded ancient solutions. Their general three-dimensional Liouville problem is not solved there; the theorem-level results are two-dimensional and special/axisymmetric three-dimensional cases.

A literature cross-check performed on 2026-08-25 did not identify a general 3D ancient Liouville theorem whose hypotheses are merely the present bounded-velocity / \(L^6\)-velocity / finite-enstrophy conditions and which would eliminate this branch directly.

Therefore no external theorem is imported to close the present general 3D ancient tail.

**Status: EXTERNAL CROSS-CHECK / NO APPLICABLE GENERAL 3D CLOSURE IDENTIFIED.**

---

## 11. New structural reduction

On bounded \(Z\), a diffuse non-\(L^3\) tail has two sharply different properties:

1. **globally critical mass can diverge:**
   \[
   \sum_kJ_k^{3/2}=\infty;
   \]
2. **its instantaneous influence on every fixed core is smooth and vanishing:**
   \[
   \|\nabla^mU_{>R}\|_{L^\infty(B_M)}
   \to0,
   \qquad
   \|\nabla^mP_{>R}\|_{L^\infty(B_M)}
   \to0.
   \]

Moreover, smooth cutoff dynamics incur only a vanishing \(H^{-1}\) boundary defect as \(R\to\infty\).

Thus the final tail obstruction is not strong instantaneous forcing of the recurrent core. It is a **global topology / exact-solution problem**: the tail prevents access to existing strong global Liouville hypotheses even while disappearing locally.

---

## 12. Audit table

| Statement | Status |
|---|---|
| Bounded \(Z\) gives uniform \(U\in L^6\) | PROVED |
| Remote vorticity tail velocity vanishes on fixed core balls | PROVED |
| Remote tail strain and all fixed spatial derivatives vanish faster | PROVED |
| Far pressure gradient/higher derivatives vanish locally | PROVED |
| Vorticity cutoff transport commutator is \(O(R^{-1/2})\) in \(H^{-1}\) | PROVED |
| Viscous cutoff commutator is \(O(R^{-1})\) in \(H^{-1}\) | PROVED |
| Compact truncations are exact NS solutions | FALSE |
| Their strong \(L^3\) norms are uniformly bounded | NOT DERIVED; generally incompatible with cubic divergence |
| Existing general 3D bounded-ancient Liouville theorem closes this branch | NOT IDENTIFIED / DO NOT ASSUME |
| Global regularity | UNPROVED |

---

## 13. Updated frontier

The bounded-\(Z\) diffuse-tail survivor has now been reduced to

\[
\boxed{
\text{locally invisible but globally non-}L^3\text{ persistent tail}.
}
\]

The next viable closure must exploit dynamics or topology beyond the present static norms. Concretely, one needs one of:

\[
\boxed{
\begin{aligned}
&\text{a quotient/local Liouville theorem stable under vanishing }H^{-1}\text{ cutoff defects},\\
&\text{a uniform critical estimate for the approximate compact truncations independent of their diverging }L^3\text{ mass},\\
&\text{or a recurrence theorem forcing the diffuse tail itself to re-enter a nonvanishing core-scale channel.}
\end{aligned}
}
\]

This is narrower than the previous generic packet-coverage problem: the tail is now known to decouple from fixed core dynamics in every fixed derivative order, but not yet removable from the global ancient-solution class.