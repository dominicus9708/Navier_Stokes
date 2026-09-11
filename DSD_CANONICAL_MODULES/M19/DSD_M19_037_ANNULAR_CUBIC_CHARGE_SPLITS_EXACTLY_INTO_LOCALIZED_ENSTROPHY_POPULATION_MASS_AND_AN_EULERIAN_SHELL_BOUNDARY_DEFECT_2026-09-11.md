# M19-037 — Annular cubic charge splits exactly into localized enstrophy population mass and an Eulerian shell-boundary defect

**Date:** 2026-09-11  
**Status:** CALCULATION / R-AC POPULATION-REALIZATION BRIDGE / LOCAL HODGE IDENTITY / BOUNDARY-DEFECT FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-036 exposed the bridge

\[
\mathcal B_{J\to pop}:
J_{k,i}
\text{ must be realized by a material-population state variable before population switching taxes can be applied.}
\]

M18-054 and the older bounded-Z cubic-tail bridge show that the annular charge is

\[
\boxed{
J(A_R,t)
:=
R\int_{A_R}|\nabla u(x,t)|^2dx,
}
\]

not an amplitude moment by definition.

The present calculation identifies its exact local relation to vorticity/enstrophy.

## 2. Local div-curl identity

Let

\[
\omega=\nabla\times u,
\qquad
\nabla\cdot u=0.
\]

The pointwise identity is

\[
|\omega|^2
=
|\nabla u|^2
-
\partial_i u_j\,\partial_j u_i.
\]

Since

\[
\partial_i u_j\,\partial_j u_i
=
\partial_j(u_i\partial_i u_j)
-u_i\partial_i(\partial_j u_j)
\]

and \(\partial_j u_j=0\),

\[
\boxed{
|\nabla u|^2-|\omega|^2
=
\nabla\cdot((u\cdot\nabla)u).
}
\]

Integrating over a smooth annular domain \(A\),

\[
\boxed{
\int_A|\nabla u|^2dx
=
\int_A|\omega|^2dx
+
\int_{\partial A}
 n\cdot (u\cdot\nabla)u\,dS.
}
\]

## 3. Exact annular charge split

Define

\[
Z_A
:=
R\int_A|\omega|^2dx
\]

and the signed shell-boundary defect

\[
\boxed{
B_A
:=
R\int_{\partial A}
 n\cdot (u\cdot\nabla)u\,dS.
}
\]

Then

\[
\boxed{J_A=Z_A+B_A.}
\]

Thus the cubic-tail charge is not a pure material amplitude quantity.  It consists of

1. an enstrophy-type bulk state \(Z_A\), which is the \(p=2\) amplitude moment restricted to an Eulerian shell;
2. a signed Eulerian boundary/harmonic transport defect \(B_A\).

This is the exact realization firewall missing in M19-036.

## 4. Bulk-dominant branch

If

\[
|B_A|\le\theta J_A,
\qquad 0\le\theta<1,
\]

then

\[
Z_A=J_A-B_A
\ge(1-\theta)J_A.
\]

Hence

\[
\boxed{
J_A\lesssim Z_A
}
\]

on the bulk-dominant branch.

There the ancestry mass really is carried, up to a fixed factor, by the local vorticity-amplitude moment

\[
\int_A\rho^2dx.
\]

This is the same amplitude order \(p=2\) used by the material-population framework of M18-068 and M18-088--089.

## 5. Boundary-dominant branch

If instead

\[
|B_A|\ge\theta J_A
\]

for some fixed \(\theta>0\), the ancestry charge is strongly influenced by transport across the shell boundary.

This is not a material-population state variable and must not be silently assigned to a lineage node.

The boundary term is explicitly

\[
B_A
=R\int_{\partial A} n_j u_i\partial_i u_j\,dS.
\]

Therefore a large boundary-dominant ancestry event is an Eulerian transport/harmonic/interface event.

It naturally belongs to the already existing families

\[
G_{shell\ transport},
\quad
G_{harmonic/nonlocal\ velocity},
\quad
G_{interface\ gradient},
\quad
G_{remote/critical\ tail},
\]

but no automatic contradiction is claimed here.

## 6. Why global enstrophy equality is insufficient

Globally on \(\mathbb R^3\), for decaying divergence-free fields,

\[
\int_{\mathbb R^3}|\nabla u|^2dx
=
\int_{\mathbb R^3}|\omega|^2dx.
\]

That global equality does **not** justify replacing each shell charge \(J_k\) by local enstrophy.

The missing information is exactly the shell-boundary term \(B_A\).

Thus any R-AC proof that localizes the global equality shell-by-shell without controlling \(B_A\) is invalid.

## 7. Eulerian shell versus material population

Even when \(J_A\lesssim Z_A\), one more bridge remains.

The shell \(A\) is Eulerian, while M18-088 population moments live on material regions \(P_i(t)\).

If a compatible material population partition covers the relevant bulk vorticity,

\[
A\cap\{\rho>0\}
=
\bigcup_i (A\cap P_i)
\]

up to negligible/typed residual, then

\[
Z_A
=R\sum_i
\int_{A\cap P_i}\rho^2dx
+
Z_A^{res}.
\]

Define

\[
Z_{A,i}:=
R\int_{A\cap P_i}\rho^2dx.
\]

Then

\[
\boxed{
Z_A=\sum_i Z_{A,i}+Z_A^{res}.
}
\]

If \(Z_A^{res}\) is a fixed small fraction, finite-label pigeonhole selects a population carrying a fixed fraction of the bulk charge.

If \(Z_A^{res}\) is large, the ancestry mass lies in fresh/unrepresented material and the event belongs to replacement/turnover/export rather than quiet same-lineage recurrence.

This is a conditional realization, not yet an automatic theorem for every annular tail shell.

## 8. Relation to the population balance

For a material population \(P_i(t)\), the \(p=2\) amplitude moment is

\[
M_{2,i}(t)=\int_{P_i(t)}\rho^2dx.
\]

M18-088--089 supplies an exact balance of the schematic form

\[
M_{2,i}'
=
S_{2,i}
+
\sum_j e_{ji}^{(2)},
\qquad
 e_{ji}^{(2)}=-e_{ij}^{(2)}.
\]

Therefore, once a shell charge is realized by a persistent material population with controlled shell truncation, the M19-036 switching-cost mechanism becomes available.

However

\[
Z_{A,i}
=R\int_{A\cap P_i}\rho^2dx
\]

contains an Eulerian shell indicator. Its derivative has additional shell-crossing terms even though \(P_i\) itself is material.

Hence the exact remaining issue is not only node balance but also radial shell residence.

## 9. Sharpened population-realization bridge

The old bridge

\[
\mathcal B_{J\to pop}
\]

now splits into two explicit subbridges:

\[
\boxed{
\mathcal B_{J\to pop}
=
\mathcal B_{Hodge}
+
\mathcal B_{shell\to material},
}
\]

where

\[
\mathcal B_{Hodge}:
|B_A|\ll J_A
\quad\text{or boundary dominance is typed},
\]

and

\[
\mathcal B_{shell\to material}:
Z_A
\text{ is carried by persistent material populations rather than fresh/unrepresented mass}.
\]

The first is now an exact algebraic dichotomy.
The second is a genuine genealogy/transport problem.

## 10. Updated R-AC quiet branch

Modulo the boundary-dominant and fresh-material exits,

\[
\boxed{
\text{cubic ancestry mass}
\to
\text{persistent }p=2\text{ material population mass}
+
\text{radial shell residence problem}.
}
\]

Thus M19-036's generic correlation theorem has been narrowed further:

\[
\boxed{
\mathcal T_{AC}^{corr}
\to
\mathcal T_{same\ population\ radial\ residence}
}
\]

provided the Hodge and population-coverage bridges remain on their quiet sides.

## 11. Next calculation

The highest-value next step is to differentiate a material population moment localized by a radial shell cutoff,

\[
M_{2,i}^{\chi}(t)
=
\int_{P_i(t)}\chi_R(x)\rho^2dx,
\]

and identify the exact radial shell-crossing current.

This should decide whether small ancestry return is equivalent to a large radial transport current, or whether a material population can remain shell-return deficient without paying an existing flux/deformation currency.

---

\[
\boxed{\text{M19-037 COMPLETE; }J_k\text{ IS POPULATION-LIKE ONLY AFTER AN EXACT HODGE/BOUNDARY SPLIT.}}
\]