# DSD M17-366 — Critical negative-kappa measure splits moving nodal concentration into compact, strict-subscale, escape, or diffuse-multiplicity branches

Date: 2026-09-08  
Canonical ID: **M17-366**

Status: **ACTIVE CONCENTRATION-COMPACTNESS ORGANIZATION OF THE MOVING NODAL BRANCH**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Record-normalized critical coefficient measures

Consider a sequence of record-normalized CE-H states indexed by `j` on the surviving moving-center/state branch of M17-365.

Define the nonnegative critical measures

\[
\boxed{
d\mu_j(x)
:=
\kappa_{j,-}(x)^{3/2}dx.
}
\]

Because `kappa` has inverse-length-squared scaling in physical variables, `mu_j` is scale critical.

Assume the nondecompactified critical-mass branch

\[
\boxed{
0<m_*\le\mu_j(\mathbb R^3)\le M_*<\infty.
}
\]

If the upper bound fails, record immediately

\[
G_{coefficient\ L^{3/2}\ decompactification}.
\]

## 2. Concentration function

For `R>0` define

\[
Q_j(R)
:=
\sup_{x\in\mathbb R^3}
\mu_j(B_R(x)).
\]

Since the total mass is bounded below, the sequence must fall into one of the following broad behaviors after passage to subsequences.

## 3. Localized critical mass

Suppose there exist fixed

\[
R_*<\infty,
\qquad
m_0>0
\]

and centers `x_j` such that

\[
\boxed{
\mu_j(B_{R_*}(x_j))\ge m_0.
}
\]

There are then two geometric subcases.

### 3.1 Bounded centers

If

\[
|x_j|\le C,
\]

then the critical coefficient mass remains in a fixed compact normalized region.

Because the measures have uniformly bounded total mass, a subsequence converges weak-* as finite Radon measures on compact sets:

\[
\mu_j\rightharpoonup^*\mu.
\]

The lower local mass gives

\[
\boxed{
\mu(B_{R_*+1})\ge m_0
}
\]

up to the standard boundary-radius adjustment.

Now split according to equiintegrability of `kappa_{j,-}^{3/2}` on this compact region.

- If equiintegrable, the critical mass is represented by an actual local `L^{3/2}` coefficient limit rather than a concentration defect. Further descent inside one fixed limit state is then subject to the M17-365 local Sobolev absorption gate.
- If not equiintegrable, a positive part of the measure concentrates on sets of vanishing volume. Record this as
  \[
  \boxed{G_{strict\ subscale\ nodal\ concentration}.}
  \]

Thus bounded-center motion does not remain an untyped moving-state escape.

### 3.2 Escaping centers

If instead

\[
|x_j|\to\infty,
\]

then the critical negative coefficient mass leaves every fixed marked compact region:

\[
\boxed{G_{spatial\ coefficient\ escape/decompactification}.}
\]

This is a genuine remote-source branch and is not identified with compact nodal concentration.

## 4. Diffuse/vanishing local concentration

Suppose for every fixed `R<infty`,

\[
\boxed{
Q_j(R)\to0.
}
\]

Then no bounded normalized ball carries a fixed fraction of the critical negative coefficient mass.

Because the total mass satisfies

\[
\mu_j(\mathbb R^3)\ge m_*>0,
\]

the mass must be distributed among an increasing number of spatial regions or over an expanding spatial extent.

For any fixed packet threshold `epsilon>0`, a covering/allocation of the mass into pieces of size at most `epsilon` requires at least

\[
\boxed{
N_j(\epsilon)
\ge
\frac{m_*}{\epsilon}
}
\]

nontrivial pieces in the ideal disjoint allocation.

As the local mass ceiling tends to zero, the required multiplicity diverges.

Thus the diffuse alternative is typed as

\[
\boxed{
G_{diffuse\ coefficient\ multiplicity/remote\ spread}.
}
\]

This is structurally analogous to the allocation difficulty already seen at M17-298, but no equality with the raw-`H2` allocation problem is claimed.

## 5. Intermediate splitting/dichotomy

A sequence may also split into several separated clusters, none carrying the whole mass.

Iterating the cluster extraction yields either

1. a finite collection with one cluster carrying a fixed positive mass, returning to Section 3; or
2. an increasing number of smaller clusters, returning to the diffuse-multiplicity branch of Section 4; or
3. clusters whose centers escape, returning to spatial decompactification.

Thus no separate unnamed `dichotomy` branch is needed after recursive allocation.

## 6. Why this is useful for M17-365

M17-365 showed that one fixed locally `L^{3/2}` state cannot hide an autonomous critical nodal carrier at arbitrarily small nested scales around one point.

The present module shows how an infinite sequence can still evade that result:

\[
\boxed{
\text{it must change scale, center, state, or multiplicity in a noncompact way.}
}
\]

Those changes are now explicitly typed rather than absorbed into the word `nodal`.

## 7. Cross-generation firewall

The measure `mu_j` is scale critical, but weak-* compactness of critical coefficient measures does **not** imply compactness of the full Navier--Stokes state or of the material genealogy.

Likewise, concentration of `mu_j` does not automatically produce a finite physical budget.

No such implication is used here.

## 8. DSD-theory role

The useful heuristic is to separate persistence of a critical descriptor from persistence of its location and carrier identity. The mathematical organization is ordinary finite-measure compactness, local concentration functions, and recursive mass allocation.

No DSD axiom is used as a PDE hypothesis.

## 9. Updated moving nodal branch

\[
\boxed{
\begin{aligned}
G_{moving\ center/state\ nodal\ concentration}
\Longrightarrow{}&
H_{compact\ local\ L^{3/2}\ coefficient\ mass}\\
&\lor G_{strict\ subscale\ nodal\ concentration}\\
&\lor G_{spatial\ coefficient\ escape}\\
&\lor G_{diffuse\ coefficient\ multiplicity}\\
&\lor G_{coefficient\ L^{3/2}\ decompactification}.
\end{aligned}
}
\]

On the first branch, M17-365 prevents further fixed-state infinite descent. The genuinely new hard cases are strict subscale concentration and diffuse multiplicity, both of which now have explicit scale/allocation structure.

## 10. Next target

The highest-value next step is to compare the strict-subscale/diffuse coefficient branches with the already open M17-298 raw-`H2` allocation problem and ask whether the CE-H equation

\[
\Delta W=\kappa W
\]

forces any critical coefficient cluster carrying `kappa_-^{3/2}` mass to carry a quantitatively related share of raw `H2` charge, without reintroducing the amplitude firewall.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
