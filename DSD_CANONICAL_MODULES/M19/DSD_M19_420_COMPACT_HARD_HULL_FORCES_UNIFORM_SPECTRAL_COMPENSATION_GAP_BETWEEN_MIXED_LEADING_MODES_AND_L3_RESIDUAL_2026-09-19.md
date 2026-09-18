# M19-420 — Compact hard hull forces a uniform spectral-compensation gap between mixed leading modes and l=3 residual leakage

Date: 2026-09-19  
Canonical ID: **M19-420**  
Status: **COMPACT SPECTRAL-GAP UPGRADE / M19-419 EXCLUDES THE SIMULTANEOUS ZERO SET “PURE TOROIDAL l1 LEADING TRACE + ZERO l3 FIRST RESIDUAL” / COMPACTNESS PROMOTES THIS TO A UNIFORM GAP / FINITE-WINDOW REDUCTION AND MINIMALITY GIVE A SYNDETIC FIXED SPECTRAL WITNESS / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Hard terminal hull

Let \(\mathcal T\) be the retained compact minimal hard terminal hull after M19-413.

The zero terminal trace is excluded on this hull by the hard nontriviality inherited from M5-571:
\[
c_3>0,
\qquad
c_\omega>0.
\]

M19-418 gives mandatory syndetic mean-free first-jet activity.

M19-419 proves that a nonzero bounded recurrent pure-toroidal \(l=1\) leading trace cannot have a first residual supported only in \(l=1\): it necessarily generates \(l=3\) leakage.

## 2. Pure toroidal l1 subspace of the leading trace

Let
\[
\Pi_{tor,1}
\]
denote the projection of a divergence-free leading trace onto the componentwise \(l=1\) toroidal sector.

The leading degree-minus-one incompressibility constraint implies, exactly as in the first-jet matrix calculation with the adjusted homogeneity, that a bounded recurrent leading field supported entirely in componentwise \(l=1\) is necessarily toroidal.

Thus
\[
\boxed{
(I-\Pi_{tor,1})A=0
}
\]
means precisely that
\[
A(q,\omega)=a(q)\times\omega
\]
for a bounded recurrent vector coefficient \(a(q)\).

## 3. Define two continuous global metrics

Choose a countable exhaustion of the log cylinder by fixed normalized windows \(I_j\times S^2\).

Define a leading-mode mixing metric
\[
\boxed{
\mathbf D_{mix}(T)
:=
\sum_{j\ge1}
2^{-j}
\min\left(
1,
\|
(I-\Pi_{tor,1})A_T
\|_{L^2(I_j\times S^2)}
\right).
}
\]

Then
\[
\mathbf D_{mix}(T)=0
\]
iff the complete leading trace is pure toroidal \(l=1\).

Define the \(l=3\) first-residual metric
\[
\boxed{
\mathbf R_3(T)
:=
\sum_{j\ge1}
2^{-j}
\min\left(
1,
\|
\Pi_3C_T
\|_{L^2(I_j\times S^2)}
\right).
}
\]

Then
\[
\mathbf R_3(T)=0
\]
iff the complete first jet has no componentwise \(l=3\) part.

On the retained smooth punctured topology, both maps are continuous.

## 4. Their simultaneous zero set is empty

Assume
\[
\mathbf D_{mix}(T)=0
\]
and
\[
\mathbf R_3(T)=0.
\]

Then the leading trace is a bounded recurrent pure-toroidal \(l=1\) field and its first residual has no \(l=3\) component.

M19-419 implies
\[
A_T\equiv0.
\]

The canonical pressure and stationary residual then vanish, so
\[
C_T\equiv0.
\]

This is the trivial terminal state, excluded from the retained hard hull.

Hence
\[
\boxed{
\{T\in\mathcal T:
\mathbf D_{mix}(T)=0,
\ \mathbf R_3(T)=0
\}
=
\varnothing.
}
\]

## 5. Compactness upgrades exclusion to a uniform gap

The continuous function
\[
T
\mapsto
\mathbf D_{mix}(T)+\mathbf R_3(T)
\]
is strictly positive on compact \(\mathcal T\).

Therefore
\[
\boxed{
\varepsilon_{spec}
:=
\min_{T\in\mathcal T}
\left[
\mathbf D_{mix}(T)+\mathbf R_3(T)
\right]
>0.
}
\]

Thus every retained hard terminal state obeys
\[
\boxed{
\mathbf D_{mix}(T)
+
\mathbf R_3(T)
\ge
\varepsilon_{spec}.
}
\]

In particular, with a harmless half split,
\[
\boxed{
\mathbf D_{mix}(T)
\ge
\frac{\varepsilon_{spec}}2
}
\]
or
\[
\boxed{
\mathbf R_3(T)
\ge
\frac{\varepsilon_{spec}}2.
}
\]

This is a genuine uniform spectral-compensation gap.

## 6. Finite-window reduction

Choose \(J\) so that the tail of the metric weights satisfies
\[
\sum_{j>J}2^{-j}
<
\frac{\varepsilon_{spec}}4.
\]

Then every state has at least one of finitely many fixed windows \(I_1,\ldots,I_J\) on which either

\[
\boxed{
\|
(I-\Pi_{tor,1})A
\|_{L^2(I_j\times S^2)}
\ge
\eta_A>0
}
\]

or

\[
\boxed{
\|
\Pi_3C
\|_{L^2(I_j\times S^2)}
\ge
\eta_3>0.
}
\]

The thresholds depend only on \(\varepsilon_{spec}\) and the finite detector family.

Thus the global compactness gap is witnessed on finitely many normalized log cells.

## 7. Minimality gives a syndetic fixed spectral witness

The strict finite-window inequalities define open subsets of the compact minimal hull.

At least one fixed detector among the finite family is nonempty.

By the M5-52 syndetic-return lemma, every orbit returns to that same detector with bounded log-radius gaps.

Therefore one fixed spectral alternative can be chosen as a syndetic witness:

### Branch M — mixed/higher leading trace
\[
\boxed{
\|
(I-\Pi_{tor,1})A
\|_{L^2(I_*)}
\ge
\eta_A
}
\]
with bounded return gaps;

or

### Branch R3 — l=3 first-residual leakage
\[
\boxed{
\|
\Pi_3C
\|_{L^2(I_*)}
\ge
\eta_3
}
\]
with bounded return gaps.

Hence
\[
\boxed{
\mathcal T
\Longrightarrow
A_{mix}^{syndetic}
\lor
C_{l=3}^{syndetic}.
}
\]

## 8. l=3 branch has a stronger angular eigenvalue but the same physical scaling

For a pure componentwise \(l=3\) scalar harmonic,
\[
-\Delta_{S^2}
=
12.
\]

Therefore
\[
\boxed{
\|
\nabla_{S^2}\Pi_3C
\|_2^2
=
12
\|
\Pi_3C
\|_2^2.
}
\]

This improves the generic mean-free Poincare constant from \(2\) to \(12\) on the extracted component.

However this is only a fixed numerical factor.

The physical first residual still has degree \(-3\), and one further angular derivative still has the raw-H2 critical parabolic cost
\[
R^{-3}.
\]

Thus
\[
\boxed{
\text{l=3 spectral gap}
\not\Rightarrow
\text{better physical power}.
}
\]

M19-414's critical-summability firewall therefore remains active.

## 9. Interpretation of the mixed-leading branch

If the \(l=3\) residual leakage is avoided, the leading trace cannot remain near the pure toroidal \(l=1\) manifold throughout the minimal hull.

It must carry a recurrent definite amount of one or more of

- radial/poloidal structure;
- toroidal \(l\ge2\) structure;
- mixed antipodal parity;
- multiple angular axes/modes.

This is precisely the class on which the earlier pressure, observability, RSS/RDSS, and finite-mode algebraic filters become relevant.

Therefore the residual analysis has now reconnected to the older global critical-tail geometry through a quantitative compactness gap, rather than by an informal branch merge.

## 10. Updated frontier

The current hard residual endpoint is

\[
\boxed{
A_{mix}^{syndetic}
\lor
C_{l=3}^{syndetic,critical}.
}
\]

The direct \(C_{l=3}\) unsigned ancestry route is still critical.

The higher-value next calculation is therefore to attack the **mixed-leading branch**:

determine whether the definite distance from the pure toroidal \(l=1\) manifold forces one of the already typed structures

\[
\boxed{
\text{radial/poloidal payer}
\lor
\text{mixed-parity pressure interaction}
\lor
\text{higher toroidal projective charge}.
}
\]

A finite Hodge/spherical decomposition of \((I-\Pi_{tor,1})A\) should identify which of these must occur with a fixed syndetic lower bound.

\[
\boxed{\text{M19-420 COMPLETE; THE PURE-l1 EXCLUSION IS PROMOTED TO A UNIFORM COMPACT SPECTRAL-COMPENSATION GAP.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
