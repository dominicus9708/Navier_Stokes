# M21-008 — Strong gamma-K anti-correlation yields two robust finite-depth populations, but an interface cost requires common-cell localization; the survivor splits into strain-gradient transition, low-vorticity bottleneck, projective-alignment separator, or spatial phase separation

Date: 2026-09-20  
Canonical ID: **M21-008**  
Status: **TWO-POPULATION INTERFACE AUDIT / THE M21-007 STRONG ANTI-CORRELATION BRANCH FORCES BOTH A ROBUST EXTENSIONAL ENSTROPHY POPULATION AND A ROBUST COMPRESSIVE PROJECTIVE POPULATION AT THE SAME DEPTH / HOWEVER INVARIANT q-SPHERE AVERAGES DO NOT BY THEMSELVES PLACE BOTH POPULATIONS IN ONE CONNECTED LOCAL CELL / IF A UNIFORMLY POINCARE COMMON CELL EXISTS AND VORTICITY/PROJECTIVE SUPPORT DOES NOT COLLAPSE, THE SIGN CHANGE OF Gamma FORCES A STRAIN-DIRECTION GRADIENT PACKET, HENCE PALINSTROPHY/STRAIN-GRADIENT ACTIVITY / OTHERWISE THE SURVIVOR IS A LOW-VORTICITY BOTTLENECK, PROJECTIVE-ALIGNMENT K-COLLAPSE, OR q-ANGULAR PHASE-SEPARATION LOCALIZATION FIREWALL / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Anti-correlation branch at z_omega

Work at the M5-587 enstrophy-production depth

\[
z=z_\omega.
\]

M21-007's strong anti-correlation branch satisfies

\[
\bar\Gamma
=
\mathbb E_{\pi}[\Gamma]
>0,
\]

and

\[
\boxed{
\mathbb E_\pi[\Gamma K]<0.
}
\]

Here

\[
d\pi
=
\frac{E}{W}d\mu,
\qquad
E=|G|^2,
\]

and

\[
K
=
\|[\Sigma_F,Q]\|_F^2
\ge0.
\]

## 2. Robust extensional population

Let

\[
|\Gamma|\le\Gamma_{\max}
\]

on the compact corridor.

Set

\[
\gamma_+
:=
\frac12\bar\Gamma>0.
\]

If

\[
p_+
:=
\pi\{\Gamma\ge\gamma_+\},
\]

then

\[
\bar\Gamma
=
\mathbb E\Gamma
\le
\gamma_+
+
\Gamma_{\max}p_+.
\]

Therefore

\[
\boxed{
p_+
\ge
\frac{\bar\Gamma}{2\Gamma_{\max}}
>0.
}
\]

Thus there is a robust positive enstrophy-weighted extensional population

\[
\boxed{
A_+
:=
\{\Gamma\ge\gamma_+\}.
}
\]

## 3. Robust compressive-projective population

Assume quantitatively

\[
\mathbb E[\Gamma K]
\le
-\mu_*<0.
\]

M21-007 gives a positive-measure set

\[
\boxed{
A_-
:=
\{
\Gamma\le-\gamma_-,
\quad
K\ge k_-
\}
}
\]

with

\[
\gamma_->0,
\qquad
k_->0,
\]

and

\[
\boxed{
\pi(A_-)\ge p_->0.
}
\]

Thus at the same finite depth there are two robust populations:

\[
A_+:
\text{extensional enstrophy production},
\]

and

\[
A_-:
\text{compressive projective noncommutation}.
\]

## 4. What invariant averaging does not give

The probability \(\pi\) is the invariant q-sphere enstrophy measure.

Positive \(\pi\)-mass of both populations does not automatically imply:

- both occur on the same q-sphere;
- both occur in one connected angular patch;
- a short path of uniformly positive vorticity joins them;
- a fixed-thickness transition layer exists.

Therefore

\[
\boxed{
\text{two positive invariant populations}
\not\Rightarrow
\text{one robust local interface}.
}
\]

A localization theorem is required before applying Poincare or coarea arguments.

## 5. Common-cell branch

Suppose there exists a normalized finite-depth cell

\[
\mathcal C
\subset
[q_0-L,q_0+L]\times S^2
\]

with:

1. uniformly controlled geometry;
2. a Poincare constant

\[
C_P<\infty;
\]

3. subsets

\[
A_+^{\mathcal C},
\quad
A_-^{\mathcal C}
\]

of fixed positive cell measure carrying the margins from Sections 2--3.

Then \(\Gamma\) has two robust separated value populations inside one connected regular cell:

\[
\Gamma\ge\gamma_+
\quad\text{on }A_+^{\mathcal C},
\]

\[
\Gamma\le-\gamma_-
\quad\text{on }A_-^{\mathcal C}.
\]

## 6. Poincare forces a Gamma-gradient packet

The two-population variance argument gives

\[
\boxed{
\int_{\mathcal C}
|\Gamma-\bar\Gamma_{\mathcal C}|^2
\ge
v_\Gamma>0,
}
\]

where \(v_\Gamma\) depends only on the two population masses, the cell volume ceiling, and

\[
\gamma_++\gamma_-.
\]

Poincare then gives

\[
\boxed{
\int_{\mathcal C}
|\nabla_{q,S}\Gamma|^2
\ge
\frac{v_\Gamma}{C_P}
=:g_*>0.
}
\]

Thus a robust common-cell extensional/compressive split is not free.

## 7. Derivative of the axial stretching scalar

Recall

\[
\Gamma=\xi^T\Sigma_F\xi.
\]

Differentiate in q/angular directions:

\[
\nabla\Gamma
=
2(\nabla\xi)^T\Sigma_F\xi
+
\xi^T(\nabla\Sigma_F)\xi.
\]

Hence

\[
\boxed{
|\nabla\Gamma|^2
\le
C
\left(
|\Sigma_F|^2|\nabla\xi|^2
+
|\nabla\Sigma_F|^2
\right).
}
\]

On the compact corridor,

\[
|\Sigma_F|\le M_\Sigma.
\]

Therefore the \(\Gamma\)-gradient packet is paid by:

- vorticity-direction gradient;
- strain gradient.

## 8. If vorticity stays uniformly nonzero, the first term is palinstrophy

Suppose on the connecting cell one has

\[
E=|G|^2\ge e_*>0.
\]

Then

\[
|\nabla\xi|^2
\le
e_*^{-1}
E|\nabla\xi|^2.
\]

The latter is the direction-gradient component of vorticity palinstrophy.

Thus

\[
\boxed{
\int_{\mathcal C}
|\Sigma_F|^2|\nabla\xi|^2
\le
C(e_*,M_\Sigma)
\int_{\mathcal C}
E|\nabla\xi|^2.
}
\]

## 9. Strain gradient is also a first-vorticity-derivative channel

Whole-space Hodge/Biot--Savart structure gives, at the \(L^2\) level,

\[
\nabla\Sigma
\sim
\text{singular integral of }\nabla\omega.
\]

Thus the strain-gradient term is of palinstrophy derivative order.

On a localized finite-depth cell, a direct estimate may require a cutoff/tail correction.

Therefore the correct typing is

\[
\boxed{
\Gamma\text{-transition}
\Longrightarrow
P_{\rm pal/strain-grad}
\lor
P_{\rm localization-tail}.
}
\]

No raw-\(H^2\) derivative is automatically needed at this stage.

## 10. Low-vorticity bottleneck branch

The common-cell argument can fail because every path between the two populations passes through

\[
E\ll1.
\]

This is precisely a low-vorticity bottleneck.

If the bottleneck has robust normalized thickness and uniformly Poincare geometry, M17-447 applies:

\[
\boxed{
\text{robust low-amplitude separator}
\Longrightarrow
\text{order-one palinstrophy packet}.
}
\]

Therefore survival requires one of:

- vanishing bottleneck thickness;
- Poincare/neck degeneration;
- vanishing population participation;
- temporal sparsity;
- chart/topology/localization failure.

## 11. Projective-alignment separator

Another escape is that vorticity remains nonzero but projective noncommutation collapses:

\[
\boxed{
K\approx0.
}
\]

Because

\[
K=2|P_\xi^\perp\Sigma_F\xi|^2,
\]

this means the vorticity direction approaches a strain eigenspace.

Thus the two populations may be separated by an approximate projective-alignment layer rather than a low-vorticity layer.

A robust transition from

\[
K\ge k_-
\]

to

\[
K\approx0
\]

inside a uniformly regular common cell forces variation of the projective strain field.

But a quantitative derivative lower bound requires a thickness/localization hypothesis.

Therefore retain

\[
\boxed{
P_{K\text{-separator}}
:
\text{projective-alignment layer}
}
\]

as a typed branch rather than silently charging it to palinstrophy.

## 12. q-angular spatial separation branch

The final escape is that \(A_+\) and \(A_-\) have positive invariant masses but are never captured together in one uniformly controlled cell.

Then the anti-correlation is maintained by large-scale q/angular phase separation.

This is not an interface theorem failure; it is a separate localization mechanism.

Denote it

\[
\boxed{
P_{\rm phase-localization}.
}
\]

Its future audit must quantify:

- separation length in q;
- angular patch multiplicity;
- recurrence density;
- and whether transition zones can remain sparse enough to avoid derivative budgets.

## 13. Exact M21-008 geometric fork

The strong anti-correlation branch therefore refines to

\[
\boxed{
C_{\Gamma K}^{-}
\Longrightarrow
P_{\Gamma\text{-grad}}
\lor
P_{E\text{-bottleneck}}
\lor
P_{K\text{-separator}}
\lor
P_{\rm phase-localization}.
}
\]

Here:

- \(P_{\Gamma\text{-grad}}\): robust common-cell sign transition paid by strain/direction gradient;
- \(P_{E\text{-bottleneck}}\): low-vorticity separator;
- \(P_{K\text{-separator}}\): projective-alignment separator;
- \(P_{\rm phase-localization}\): populations remain separated in q/angular location.

## 14. Relation to existing analytic ledgers

The first two branches already tend back toward existing palinstrophy/interface firewalls.

The potentially new geometry is concentrated in:

\[
P_{K\text{-separator}}
\]

and

\[
P_{\rm phase-localization}.
\]

These encode how extensional production and compressive projective activity avoid a direct strain-sign transition.

## 15. What remains unproved

M21-008 does not prove that:

- the two populations share one connected cell;
- a projective-alignment separator has fixed thickness;
- q/angular phase separation has high multiplicity;
- any separator persists for a non-negligible physical time.

Thus no ancestry contradiction follows yet.

## 16. Next target

The more sharply defined new branch is the projective-alignment separator

\[
K\approx0.
\]

M21-009 should determine whether a robust finite-depth \(K\)-separator between two positive enstrophy populations can remain thin and recurrent without paying:

- strain-direction gradient;
- pressure-Hessian rotation;
- or low-vorticity degeneration.

This reuses the coordinate-free commutator

\[
[\Sigma_F,Q]
\]

and avoids choosing strain eigenvectors across degeneracies.

\[
\boxed{\text{M21-008 COMPLETE; STRONG GAMMA-K ANTI-CORRELATION BECOMES A TWO-POPULATION GEOMETRIC FORK: GRADIENT TRANSITION, LOW-VORTICITY BOTTLENECK, PROJECTIVE-ALIGNMENT SEPARATOR, OR q-ANGULAR PHASE LOCALIZATION.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
