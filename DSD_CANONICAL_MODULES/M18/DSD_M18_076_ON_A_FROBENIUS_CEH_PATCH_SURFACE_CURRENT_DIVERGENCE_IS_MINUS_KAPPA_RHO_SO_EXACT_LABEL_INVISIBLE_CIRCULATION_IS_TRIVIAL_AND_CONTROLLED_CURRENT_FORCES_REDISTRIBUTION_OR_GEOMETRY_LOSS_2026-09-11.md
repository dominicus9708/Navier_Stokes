# M18-076 — On a Frobenius CE-H patch, surface-current divergence is minus kappa rho; exact label-invisible circulation is trivial, and controlled current forces redistribution or geometry loss

**Date:** 2026-09-11  
**Status:** EXACT SURFACE DIVERGENCE IDENTITY / PURE-CIRCULATION CLOSURE / CONDITIONAL QUANTITATIVE REDISTRIBUTION GAP

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M18-075 splits the current on a controlled Frobenius-integrable material patch into

\[
J_\Sigma=J_G+J_C,
\]

where

- \(J_G\) is the surface-gradient component seen by scalar material-label moments;
- \(J_C\) is orthogonal to all such gradients and is interior surface-divergence-free.

M18-075 leaves open the possibility that a recurrent CE-H patch carries a large nonzero current almost entirely through \(J_C\), thereby avoiding scalar label redistribution.

The exact CE-H amplitude and surface-continuity equations rule out the **pure** version of this escape.

On a vortex-transverse material patch,

\[
\boxed{
\operatorname{div}_\Sigma J_\Sigma=-\kappa\rho.
}
\]

Thus the redistributive current is exactly the weak inverse-Laplacian response to the coefficient source \(\kappa\rho\).

If the redistributive component vanishes identically on an active open patch, then \(\kappa=0\) there, and the CE-H Laplacian eigenline plus spatial analyticity forces the entire finite-energy state to vanish.

Hence exact label-invisible current circulation is impossible on the nonzero marked CE-H component.

## 2. Surface continuity law

M5-520 gives on a smooth material surface \(\Sigma(\theta)\)

\[
\boxed{
D_Bf
+(1-\sigma_n)f
+
\operatorname{div}_\Sigma J_\Sigma
=0,
}
\]

where

\[
f=W\cdot n,
\]

\[
\sigma_n=n\cdot\Sigma n,
\]

and

\[
J_\Sigma=(\nabla\times W)\times n.
\]

On the Frobenius CE-H branch of M18-073--074, choose the vortex-transverse material patch with

\[
\boxed{n=\xi.}
\]

Then

\[
f=\rho,
\qquad
\sigma_n=\sigma.
\]

Therefore

\[
\boxed{
D_B\rho
+(1-\sigma)\rho
+
\operatorname{div}_\Sigma J_\Sigma
=0.
}
\]

## 3. Insert the CE-H amplitude law

The exact CE-H material amplitude equation is

\[
\boxed{
D_B\rho
=(\sigma+\kappa-1)\rho.
}
\]

Substitute into Section 2:

\[
(\sigma+\kappa-1)\rho
+(1-\sigma)\rho
+
\operatorname{div}_\Sigma J_\Sigma
=0.
\]

The strain and similarity terms cancel exactly, leaving

\[
\boxed{
\operatorname{div}_\Sigma J_\Sigma
=-\kappa\rho.
}
\]

This identity is local on every smooth vortex-transverse material patch in CE-H.

It is the surface form of viscous flux redistribution.

## 4. Gradient Hodge component solves a surface Poisson problem

Use the M18-075 orthogonal decomposition

\[
J_\Sigma=J_G+J_C,
\]

with

\[
J_C\perp
\overline{\nabla_\Sigma H_0^1(\Sigma)}.
\]

Then

\[
\operatorname{div}_\Sigma J_C=0
\]

in the interior weak sense, so

\[
\boxed{
\operatorname{div}_\Sigma J_G
=-\kappa\rho.
}
\]

Write

\[
J_G=\nabla_\Sigma\psi
\]

in the weak projected sense. Then \(\psi\in H_0^1(\Sigma)\) solves

\[
\boxed{
-\Delta_\Sigma\psi
=
\kappa\rho
}
\]

weakly.

Accordingly,

\[
\boxed{
\|J_G\|_{L^2(\Sigma)}
=
\|\kappa\rho\|_{H^{-1}_0(\Sigma)}
}
\]

when the \(H^{-1}_0\) norm is defined using the Dirichlet energy norm on \(H_0^1(\Sigma)\).

Thus the scalar-label-redistributive current is exactly the negative-order surface size of the coefficient source \(\kappa\rho\).

## 5. Exact pure circulation forces kappa zero

Suppose the surface current is entirely label-invisible:

\[
\boxed{J_G=0.}
\]

Then

\[
\operatorname{div}_\Sigma J_\Sigma
=
\operatorname{div}_\Sigma J_C
=0.
\]

The exact identity of Section 3 gives

\[
\boxed{
\kappa\rho=0
}
\]

on the patch.

The patch lies in the active region and was constructed with

\[
\rho\ge a_0>0.
\]

Hence

\[
\boxed{\kappa=0}
\]

through the active open patch.

## 6. Kappa zero on an open CE-H patch makes Delta W vanish there

CE-H gives

\[
\boxed{
\Delta W=\kappa W.
}
\]

Therefore on the active open patch of Section 5,

\[
\boxed{
\Delta W=0.
}
\]

The CE-H hard component has the spatial analyticity already used in M5-599.

Hence each component of

\[
\Delta W
\]

is real analytic in space at the fixed retained time.

Vanishing on a nonempty open set implies

\[
\boxed{
\Delta W\equiv0
\quad\text{on }\mathbb R^3
}
\]

at that time.

## 7. Finite-energy harmonic state is zero

The marked CE-H state satisfies

\[
W\in L^2(\mathbb R^3).
\]

A whole-space harmonic \(L^2\) vector field is zero.

For example, Fourier transformation gives

\[
|\xi_{Fourier}|^2\widehat W=0,
\]

so \(\widehat W\) is supported at the origin; an \(L^2\) function with such support vanishes.

Therefore

\[
\boxed{W=0.}
\]

This contradicts the persistent nonzero mark of the CE-H hard component.

Hence

\[
\boxed{
J_G=0
\quad\text{on a nonzero active Frobenius current patch is impossible.}
}
\]

## 8. Exact circulation branch is closed

The M18-075 alternative

\[
G_{surface\ circulation}
\]

must therefore be interpreted carefully.

A nonzero divergence-free component \(J_C\) may coexist with redistribution, but it cannot carry **all** of the current on a nonzero active Frobenius CE-H patch.

Thus

\[
\boxed{
\text{nonzero controlled Frobenius current}
\Longrightarrow
J_G\ne0.
}
\]

This gives a genuine scalar material-label redistribution channel at every such exact patch, although the quantitative size of \(J_G\) still requires geometry/compactness control.

## 9. Quantitative compactness upgrade on a controlled patch family

Consider a family of current-carrying Frobenius material patches with the following uniform controls:

- each patch is represented on one fixed reference disk by uniformly bi-Lipschitz charts;
- the induced metrics and their required finite derivatives are precompact;
- the active amplitude has a fixed positive lower bound;
- the surface-current action has a fixed lower bound
  \[
  \|J_\Sigma\|_2^2\ge j_*>0;
  \]
- the CE-H fields converge strongly in the topology needed to pass the surface current and coefficient source.

Suppose no quantitative redistribution floor existed. Then there would be a sequence with

\[
\|J_G^{(n)}\|_2\to0.
\]

Pull back to the fixed reference disk and extract a compact limit.

The total-current lower bound survives, so the limit current is nonzero.

Continuity of the Hodge/Dirichlet projection under the controlled metric convergence gives

\[
J_G^{(\infty)}=0.
\]

Sections 5--7 then force the limiting CE-H state to be zero, contradicting persistence of the nonzero current/active mark.

Therefore, on any such controlled compact patch family, there exists

\[
\boxed{g_*>0}
\]

such that

\[
\boxed{
\|J_G\|_{L^2(\Sigma)}
\ge g_*.
}
\]

If the patch family fails the required geometric compactness, record

\[
\boxed{G_{surface\ geometry/domain\ degeneration}.}
\]

Thus the quantitative routing is

\[
\boxed{
\text{fixed controlled surface current}
\Longrightarrow
\text{fixed label-redistributive current}
\lor
G_{surface\ geometry/domain\ degeneration}.
}
\]

## 10. Return to material-label moments

M18-075 gives for any material scalar label \(\varphi\in H_0^1(\Sigma)\)

\[
M_\varphi'
=
\int_\Sigma
\nabla_\Sigma\varphi\cdot J_G\,dA.
\]

A fixed lower bound on \(\|J_G\|_2\) gives a normalized test label with fixed nonzero moment derivative.

Uniform smoothness/time continuity then thickens this to

\[
\boxed{
|\Delta M_\varphi|
\ge m_*>0
}

on a short controlled material interval, unless label/surface geometry exits.

Therefore the exact Frobenius-current branch has now been reduced to

\[
\boxed{
\text{material-label redistribution}
\lor
\text{surface/label geometry turnover}.
}
\]

The purely circulatory escape is removed.

## 11. Why no monotone contradiction follows

A material-label moment may later reverse and return.

Therefore even a fixed redistributive event satisfies only

\[
\boxed{
\text{redistribution is priced and unavoidable locally},
}
\]

not

\[
\boxed{
\text{redistribution has one sign forever}.
}
\]

To close recurrence one still needs a same-label cycle argument, a finite-label replacement exhaustion, or a signed cocycle that cannot reverse without a second cost.

## 12. Updated material-current route

Combining M18-073--076 yields

\[
\boxed{
\text{mandatory CE-H non-Beltrami current}
\Longrightarrow
\begin{cases}
G_{self\text{-}helicity/twist},\\
G_{surface/label\ geometry\ loss},\\
G_{material\ label\ redistribution}.
\end{cases}
}
\]

The old independent `pure surface circulation` endpoint is removed on the controlled Frobenius branch.

## 13. Audit verdict

### Certified

1. On a vortex-transverse CE-H material surface,
   \[
   \operatorname{div}_\Sigma J_\Sigma=-\kappa\rho.
   \]
2. The Hodge-gradient current is the weak solution of
   \[
   -\Delta_\Sigma\psi=\kappa\rho.
   \]
3. Exact label-invisible pure circulation gives \(\kappa=0\) on the active patch.
4. CE-H then gives \(\Delta W=0\) on an open patch; spatial analyticity extends this globally at the time slice.
5. Finite-energy harmonicity forces \(W=0\), contradicting the marked nonzero state.
6. Hence every nonzero controlled Frobenius current patch has a nonzero redistributive component.
7. Under a compact controlled patch family, compactness upgrades this to a fixed quantitative redistribution floor unless surface geometry degenerates.

### Dependencies/firewalls

- spatial analyticity is the same external/internal dependency already used in M5-599;
- quantitative Hodge-projection continuity requires controlled surface-chart compactness and is not asserted when the surface geometry degenerates;
- redistribution may reverse later.

### Still open

- same-label recurrence versus replacement/export;
- exclusion of the uniform self-helicity/twist branch;
- a one-sign material cocycle;
- ancestry closure;
- remote/critical closure;
- global regularity.

## 14. Next target

M18-077 should now combine the **finite persistent lineage network** of M5-497/M5-514 with the unavoidable material-label redistribution event.

The main question is no longer whether redistribution occurs, but where it can go in a finite lineage graph:

\[
\boxed{
\text{same lineage reversible return}
\lor
\text{transfer to another persistent lineage}
\lor
\text{new/replacement label}
\lor
\text{export/flux loss}.
}
\]

Finite-memory saturation already controls the number of new labels.

The next audit should determine whether indefinite reversible redistribution on a finite directed lineage graph necessarily contains a recurrent directed cycle carrying a nonzero signed flux moment, and whether that cycle admits a bounded potential or remains a genuinely conservative critical circulation.
