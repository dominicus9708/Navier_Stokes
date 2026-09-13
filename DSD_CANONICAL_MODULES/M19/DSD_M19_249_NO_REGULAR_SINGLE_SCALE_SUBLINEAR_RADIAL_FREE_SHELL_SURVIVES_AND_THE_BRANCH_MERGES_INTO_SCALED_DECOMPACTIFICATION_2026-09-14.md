# M19-249 — No regular single-scale sublinear radial-free shell survives; the branch merges into scaled decompactification

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / MESOSCOPIC SHELL RIGIDITY + BRANCH REDUCTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-248 excludes a regular shell that remains tight at fixed physical distance from the cavity wall. A remaining possibility is a mesoscopic boundary layer whose thickness satisfies

\[
D_j\to\infty,
\qquad
D_j/R_j\to0.
\]

This module shows that the same leading poloidal rigidity persists at **every single sublinear shell scale**. Consequently, on the radial-free critical branch, a surviving escape sequence must lose scaled compactness or move to the macroscopic \(D_j\asymp R_j\) regime.

## 2. General sublinear shell scale

Let

\[
R_j\to\infty,
\qquad
0<D_j=o(R_j).
\]

Write

\[
\xi:=\frac{R_j-r}{D_j}.
\]

A normalized tangential shell occupying volume \(O(R_j^2D_j)\) has natural amplitude

\[
(R_j^2D_j)^{-1/2}
=
\frac1{R_j\sqrt{D_j}}.
\]

Define

\[
\boxed{
V_{T,j}:=R_j\sqrt{D_j}\,w_{T,j},
}
\]

\[
\boxed{
V_{r,j}:=\frac{R_j^2}{\sqrt{D_j}}\,w_{r,j},
}
\]

and the pressure scale

\[
\boxed{
P_j:=\frac{D_j^{3/2}}{R_j}\,\pi_j.
}
\]

Thus

\[
w_T=\frac1{R\sqrt D}V_T,
\qquad
w_r=\frac{\sqrt D}{R^2}V_r,
\qquad
\pi=\frac{R}{D^{3/2}}P.
\]

## 3. Tangential mass is scale invariant; radial mass is lower order

Since

\[
dy
=R_j^2D_j(1+o(1))\,d\xi\,d\omega
\]

on bounded \(\xi\)-intervals,

\[
\int|w_T|^2dy
=
\int|V_T|^2d\xi d\omega+o(1).
\]

For the radial component,

\[
\int|w_r|^2dy
=
\frac{D_j^2}{R_j^2}
\int|V_r|^2d\xi d\omega+o(1).
\]

Hence when \(D_j/R_j\to0\), any nonzero normalized shell mass is tangential at leading order.

## 4. Scale comparison

The leading tangential similarity-normal drift is

\[
-\frac r2\partial_rw_T
=
\frac1{2D_j^{3/2}}\partial_\xi V_T
+o(D_j^{-3/2}).
\]

The tangential pressure force is

\[
-\frac1r\nabla_{S^2}\pi
=
-\frac1{D_j^{3/2}}\nabla_{S^2}P
+o(D_j^{-3/2}).
\]

By comparison:

\[
\partial_sw_T
=O\left(\frac1{R_j\sqrt{D_j}}\right),
\]

so relative to the leading scale it is smaller by

\[
\frac{D_j}{R_j}\to0
\]

under bounded scaled time frequency.

Radial viscosity satisfies

\[
\nu\partial_{rr}w_T
=O\left(\frac{\nu}{R_jD_j^{5/2}}\right),
\]

smaller than the leading scale by

\[
\frac\nu{R_jD_j}\to0
\]

for the retained shell scales. The explicit amplitude term, curvature corrections, and radial-free background mixing are also lower order.

Thus the same quasi-static pressure/similarity balance governs every regular sublinear shell.

## 5. Radial momentum freezes the leading pressure in xi

The radial pressure force has size

\[
-\partial_r\pi
=
\frac{R_j}{D_j^{5/2}}\partial_\xi P.
\]

The radial similarity-drift scale for

\[
w_r=\frac{\sqrt{D_j}}{R_j^2}V_r
\]

is only

\[
O\left(\frac1{R_j\sqrt{D_j}}\right).
\]

Their ratio is

\[
\frac{R_j^2}{D_j^2}\to\infty.
\]

Therefore a regular balanced limit requires

\[
\boxed{
\partial_\xi P_0=0.
}
\]

Thus

\[
P_0=P_0(\omega,s).
\]

If this conclusion fails, the pressure/radial derivatives themselves decompactify at the shell scale and belong to the scaled-decompactification branch.

## 6. Universal leading tangential shell equation

Dividing the tangential equation by the common scale \(D_j^{-3/2}\) gives

\[
\boxed{
\frac12\partial_\xi V_T
=\nabla_{S^2}P_0.
}
\]

The M19-245 inner impedance and total M19-232 H1 currency determine the outer trace. If

\[
a_T=\frac1{R_j\sqrt{D_j}}B_T,
\]

then the leading inner layer dissipation is

\[
\frac{R_j}{4}\int_{S_{R_j}}|a_T|^2dS
=
\frac{R_j}{4D_j}
\int_{S^2}|B_T|^2d\omega.
\]

Because the total viscous currency is \(O(1)\) while \(D_j/R_j\to0\),

\[
\boxed{
B_T\to0
\quad\text{in period-integrated }L^2(S^2).
}
\]

Therefore the shell limit obeys

\[
\boxed{V_T(0)=0.}
\]

and hence

\[
\boxed{
V_T(\xi)=2\xi\nabla_{S^2}P_0.
}
\]

## 7. Half-line L2 rigidity at arbitrary sublinear scale

Assume the shell is **single-scale tight** after the \(D_j\) rescaling and that scaled radial/angular/time compactness is retained. Then the limit satisfies

\[
V_T\in L^2([0,\infty)_\xi\times S^2\times[0,S]).
\]

But

\[
\int_0^\infty|V_T|^2d\xi
=
4|\nabla_{S^2}P_0|^2
\int_0^\infty\xi^2d\xi.
\]

Therefore

\[
\boxed{
\nabla_{S^2}P_0=0,
\qquad
V_T\equiv0.
}
\]

The leading incompressibility equation

\[
\partial_\xi V_r
=\operatorname{div}_{S^2}V_T,
\qquad V_r(0)=0
\]

then gives

\[
\boxed{V_r\equiv0.}
\]

Thus no nonzero regular single-scale shell survives at any scale

\[
\boxed{D_j=o(R_j).}
\]

## 8. Canonical median-scale formulation

Let the one-period boundary-distance mass distribution be

\[
\mu_j([0,D])
:=
\int_0^{S_j}\int_{R_j-D<|y|<R_j}|w_j|^2dy\,ds,
\]

with total mass \(\mu_j([0,R_j])=1\).

Choose a median scale \(D_j\) satisfying

\[
\mu_j([0,D_j])\ge\frac12,
\qquad
\mu_j([0,D_j^-])\le\frac12.
\]

M19-240 prevents \(D_j\to0\): the no-slip shell inequality would otherwise force the mass in \([0,D_j]\) to vanish. Hence, after subsequence,

\[
D_j\gtrsim1
\]

in the fixed-viscosity normalization.

There are only two geometric possibilities:

\[
\boxed{
D_j/R_j\to0
\quad\text{or}\quad
\liminf D_j/R_j>0.
}
\]

If \(D_j/R_j\to0\), the present theorem says that a regular scale-tight limit is impossible. Therefore the median-scale sequence must lose scaled compactness.

If \(D_j\asymp R_j\), the sequence is macroscopic and falls under the M19-238--239 macroscopic rigidity analysis; retaining positive mass while the regular weak macroscopic limit is zero again requires loss of strong/scaled compactness.

## 9. Radial-free branch reduction

Therefore the regular radial-free shell-return branch has no independent compact survivor:

\[
\boxed{
A_r=0
\quad+\quad
\text{regular scale-compact escape}
\Longrightarrow
\text{contradiction}.
}
\]

Equivalently, any radial-free escaping unit cavity mode must enter a decompactification mechanism:

\[
\boxed{
\mathcal T_{shell}^{rad-free}
\subset
\mathcal T_{scaled-deriv/freq}.
}
\]

Here the right-hand side includes loss of scaled radial derivative, angular frequency, time/Floquet frequency, pressure compactness, or strong shell-profile compactness.

This is a genuine branch reduction: the radial-free **regular poloidal shell** no longer remains an independent bounded-period theorem obligation.

## 10. What remains

The bounded-period escape problem is reduced to:

\[
\boxed{
\text{nonzero critical radial transport }A_r
\quad\lor\quad
\text{scaled derivative/frequency/profile decompactification}.
}
\]

The core-tight cavity branch remains separate because a nonzero whole-space linearized core limit still needs classification and hard-bundle membership.

The next natural calculation is therefore the complementary \(A_r\neq0\) shell scaling: determine whether critical radial transport changes the universal linear-in-distance poloidal normal form enough to permit an \(L^2\) scale-tight shell, or merely changes its slope/weight without removing the half-line rigidity.

## 11. Scope firewall

This module does not prove compactness. It proves rigidity **if** the relevant rescaled shell sequence is compact enough to pass the leading equations.

Therefore

\[
\boxed{
\text{regular shell rigidity}
\neq
\text{control of scaled decompactification}.
}

Global regularity remains open until that decompactification branch, the \(A_r\neq0\) branch, the core branch, the aperiodic frontier, ROOT-CERT, and the historical non-CE-H roots are all independently closed and audited.
