# DSD M17-363 — Fixed negative-line flux and bounded transversal area force a positive high-amplitude capture fraction

Date: 2026-09-08  
Canonical ID: **M17-363**

Status: **ACTIVE CONDITIONAL FLUX-AREA CLOSURE OF M17-362 WHOLE-LINE LOW-AMPLITUDE BRANCH**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Setting

Take the M17-362 negative-coefficient vortex-line family at one retained time.

Assume a coherent oriented transversal `Sigma` meets the relevant line family once in the chosen fundamental tube chart and has bounded area

\[
\boxed{|\Sigma|\le A_*<\infty.}
\]

Assume the negative-line family carries a fixed positive oriented material flux

\[
\boxed{
\Phi_-:=\int_{\Sigma_-}W\cdot n\,dA\ge\Phi_*>0.
}
\]

The orientation is chosen so that `W·n>=0` on the retained flux family.

If no such fixed negative-line flux allocation is available, retain the M17-362 exit

\[
G_{negative\text{-}line\ flux\ thinning}.
\]

## 2. Low-amplitude flux capacity

Fix an amplitude threshold `a>0` and split the transversal into

\[
\Sigma_{lo}:=\{x\in\Sigma_-:\rho(x)<a\},
\]

\[
\Sigma_{hi}:=\{x\in\Sigma_-:\rho(x)\ge a\}.
\]

Since

\[
0\le W\cdot n\le|W|=\rho,
\]

the low-amplitude part can carry at most

\[
\int_{\Sigma_{lo}}W\cdot n\,dA
\le
 a|\Sigma_{lo}|
\le
 aA_*.
\]

Therefore the high-amplitude part carries

\[
\boxed{
\Phi_{hi}
:=
\int_{\Sigma_{hi}}W\cdot n\,dA
\ge
\Phi_*-aA_*.
}
\]

## 3. Choose a threshold below the flux-capacity scale

Choose

\[
0<a_*\le\frac{\Phi_*}{2A_*}.
\]

Then

\[
\boxed{
\Phi_{hi}\ge\frac{\Phi_*}{2}>0.
}
\]

Thus a fixed positive fraction of the negative-line flux must meet the transversal at amplitude at least `a_*`.

Consequently a fixed-flux negative-line population cannot remain entirely below arbitrarily small amplitude inside a uniformly bounded transversal area.

## 4. Upgrade a high-amplitude point to a captured line segment

On the compact all-order branch, assume

\[
|\nabla\rho|\le M_1<\infty
\]

on the retained tube neighborhood.

Apply Section 3 with threshold `2a_*` chosen so that

\[
2a_*A_*\le\frac{\Phi_*}{2}.
\]

Then at least

\[
\Phi_*/2
\]

of negative-line flux crosses the set

\[
\rho\ge2a_*.
\]

For a line meeting such a point `x_0`, arclength-Lipschitz control gives

\[
|\rho(\gamma(s))-ho(x_0)|
\le
M_1|s-s_0|.
\]

Hence for

\[
|s-s_0|\le\frac{a_*}{M_1},
\]

we have

\[
\rho(\gamma(s))\ge a_*.
\]

Therefore every such line carries a high-amplitude captured segment of length at least

\[
\boxed{
\ell_*
:=
\frac{2a_*}{M_1}
}
\]

if both sides of the point remain in the retained chart, or at least `a_*/M_1` in the one-sided boundary case. Any failure caused by immediate exit from the chart is an explicit interface/capture-boundary exit.

## 5. Combine with line constancy of kappa

M17-362 gives

\[
D_\xi\kappa=0.
\]

Therefore every line in the high-amplitude flux subfamily remains a negative-`kappa` line along the captured segment.

Thus, subject to the retained negative-coefficient moment allocation, this positive-flux subfamily routes back to the M17-312 high-amplitude negative flux-length occupancy branch.

Symbolically,

\[
\boxed{
\begin{aligned}
&\Phi_-\ge\Phi_*>0
+\text{ bounded transversal area}
+\text{ compact }|\nabla\rho|\\
&\qquad\Longrightarrow
H_{positive\text{-}flux\ high\text{-}amplitude\ negative\ line\ capture}
\lor
G_{transversal/interface\ exit}.
\end{aligned}
}
\]

## 6. What remains of whole-line low-amplitude segregation

Under Sections 1--5, the M17-362 branch

\[
G_{whole\text{-}line\ low\text{-}amplitude\ segregation}
\]

cannot carry a fixed positive negative-line flux.

It can survive only through

\[
\boxed{G_{negative\text{-}line\ flux\ thinning},}
\]

\[
\boxed{G_{transversal\ area/chart\ decompactification},}
\]

\[
\boxed{G_{amplitude\ gradient/tube\ geometry\ decompactification},}
\]

or the already typed nodal/interface/rank/domain exits.

## 7. No circular use of M17-314

This module does **not** use the M17-314 conclusion that the high-amplitude branch already carries a fixed negative-label flux mass.

Instead, it is explicitly conditional on an independent negative-line flux allocation `Phi_->=Phi_*` in the critical nodal branch.

If that allocation is unavailable, `negative-line flux thinning` remains open. This prevents circular closure of M17-311 through one of its own descendants.

## 8. DSD-theory role

The heuristic is to ask for the capacity of the low-amplitude channel to carry a fixed conserved/transported structural measure. The calculation is the elementary flux-area inequality plus compact derivative control.

No DSD axiom is used as a PDE hypothesis.

## 9. Updated nodal branch

\[
\boxed{
\begin{aligned}
G_{critical\ nodal\ \kappa_-}
\Longrightarrow{}&
G_{negative\text{-}line\ flux\ thinning}\\
&\lor G_{transversal/tube\ geometry\ decompactification}\\
&\lor G_{capture/interface\ collapse}\\
&\lor G_{nodal/rank/domain\ exit}\\
&\lor H_{high\text{-}amplitude\ negative\ capture}.
\end{aligned}
}
\]

The highest-value remaining subbranch is now `negative-line flux thinning`: determine whether fixed critical `L^{3/2}` negative-coefficient mass can coexist with vanishing material-flux allocation without forcing an independent geometric or amplitude cost.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
