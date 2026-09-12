# DSD M19-112 — Compact quotient-nondegenerate solution components project open and closed in parameter space, so one empty parameter kills the whole connected corridor

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / GLOBAL CONTINUATION LEMMA FOR THE IDENTITY-MINUS-COMPACT RSS/RDSS FIXED-POINT PROBLEM / IF ALL SOLUTIONS IN A CONNECTED PARAMETER CORRIDOR ARE COMPACT AND QUOTIENT-NONDEGENERATE, THEN THE EXISTENCE SET IS OPEN AND CLOSED / A SINGLE LIOUVILLE-EMPTY PARAMETER VALUE FORCES THE WHOLE CORRIDOR EMPTY / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Parameterized reduced fixed-point problem

Let

\[
\mathcal P
\]

be a connected parameter manifold/corridor for RSS/RDSS data, and let

\[
F(p,\omega)=0
\]

be the phase- and rotation-quotiented fixed-point equation of M19-111 on a Banach space `X_red`.

Assume:

1. `F` is continuously differentiable on the retained corridor;
2. the solution set
   \[
   \mathscr S:=\{(p,\omega):F(p,\omega)=0\}
   \]
   is compact in `P x X_red`;
3. every solution is quotient-nondegenerate:
   \[
   \boxed{D_\omega F(p,\omega)\text{ is invertible}.}
   \]

The third condition is exactly the absence of any symmetry-transverse unit Floquet multiplier.

---

## 2. Local projection is a diffeomorphism

By the implicit-function theorem, near every solution

\[
(p_0,\omega_0)\in\mathscr S,
\]

there is a unique local graph

\[
\omega=\omega(p).
\]

Therefore the parameter projection

\[
\pi:\mathscr S\to\mathcal P,
\qquad
\pi(p,\omega)=p,
\]

is a local diffeomorphism on every connected solution component.

In particular,

\[
\boxed{
\pi(\mathscr C)
\text{ is open in }\mathcal P
}
\]

for every connected component `C` of the solution set.

---

## 3. Compactness makes the projection closed

If

\[
\mathscr C\subset\mathscr S
\]

is compact, then its continuous image

\[
\pi(\mathscr C)
\]

is compact and hence closed in the Hausdorff parameter corridor.

Thus every nonempty connected compact quotient-nondegenerate solution component has projection

\[
\boxed{
\pi(\mathscr C)
\text{ both open and closed in }\mathcal P.
}
\]

Since `P` is connected,

\[
\boxed{
\pi(\mathscr C)=\mathcal P.
}
\]

So every nonempty component must pass over **every** parameter value in the connected corridor.

---

## 4. One empty parameter removes all compact nondegenerate components

Suppose there exists one parameter

\[
p_*\in\mathcal P
\]

for which a Liouville theorem or other certified argument gives

\[
\boxed{
F(p_*,\omega)=0
\Longrightarrow
\omega=0
}
\]

and the zero state has already been removed from the nontrivial solution set.

If a nontrivial compact quotient-nondegenerate component existed, its projection would equal all of `P` and in particular contain `p_*`.

That is impossible.

Hence

\[
\boxed{
\mathscr S_{nontrivial}=\varnothing.
}
\]

This gives the continuation principle:

\[
\boxed{
\begin{array}{c}
\text{connected parameter corridor}
+\text{compact solution set}
+\text{no extra unit multiplier}
+\text{one empty parameter}
\\[2mm]
\Longrightarrow
\text{no nontrivial RSS/RDSS anywhere in the corridor}.
\end{array}
}
\]

---

## 5. Why an isola cannot evade the argument

A disconnected closed branch (`isola`) entirely inside the parameter corridor would still be a compact connected solution component.

If quotient-nondegenerate everywhere, its parameter projection is simultaneously open and compact/closed.

Therefore in a connected corridor it must cover all parameters, contradicting the empty parameter value.

Hence an interior isola requires at least one of:

\[
\boxed{
\text{extra unit multiplier}
\lor
\text{compactness loss}
\lor
\text{parameter-boundary escape}.
}
\]

This is the global version of M19-111.

---

## 6. Consequence for the M19 architecture

If the extra-center theorem

\[
E^c_{extra}=0
\]

is proved uniformly and the periodic/RDSS solution set has an a priori compact parameter corridor, then a separate parameter-by-parameter Liouville proof is unnecessary.

It suffices to know one empty anchor point in each connected corridor.

Thus the two previously separated hard cores

\[
\text{aperiodic extra center}
\quad\text{and}\quad
\text{moderate periodic/RDSS existence}
\]

can potentially be merged into the same theorem plus compactness/continuation bridge.

---

## 7. Firewall

The compactness assumption is substantial.

A solution component may evade the lemma by:

- period `S -> infinity`;
- loss of Type-I or pressure bounds;
- spatial/tail decompactification;
- parameter escape such as an uncontrolled rotation representation;
- or any other failure of the retained smooth compact corridor.

Therefore

\[
\boxed{
\text{quotient nondegeneracy alone}
\neq
\text{global parameter exclusion}.
}
\]

---

## 8. Next target

Apply the lemma separately to:

1. RSS, whose parameter is essentially the rotation rate and for which external small/large-rotation empty anchors are known;
2. RDSS, where the principal rotation holonomy is automatically bounded once a positive period floor is known, leaving `S -> infinity` as the main remaining parameter noncompactness.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
