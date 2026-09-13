# M19-239 — H(div) normal-trace inheritance closes the regular potential macroscopic bulk branch

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / POTENTIAL-BULK CLOSURE

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-238

For the cavity-scale rescaling

\[
V_j(x,s)=R_j^{3/2}w_j(R_jx,s),
\qquad x\in B_1,
\]

M19-238 shows that any macroscopic bulk limit with locally \(L^2\)-controlled scaled vorticity has zero curl under the exact relative-periodic inviscid dilation equation.

Thus its regular rotational part vanishes and the surviving regular bulk must satisfy

\[
\nabla_x\times V=0,
\qquad
\nabla_x\cdot V=0.
\]

M19-238 left this as a potential-flow matching branch. The no-slip cavity geometry supplies one more piece of information that closes it.

## 2. Rescaled fields have exact zero normal trace

For every \(j\),

\[
\nabla_x\cdot V_j=0
\]

and the no-slip condition gives

\[
V_j|_{\partial B_1}=0.
\]

In particular,

\[
\boxed{V_j\cdot n=0\quad\text{on }\partial B_1.}
\]

The one-period normalization gives a uniform \(L^2\) bound. Since the divergence is identically zero, \(V_j\) is uniformly bounded in

\[
H(\operatorname{div};B_1)
=
\{V\in L^2(B_1):\nabla\cdot V\in L^2(B_1)\}.
\]

The normal-trace map

\[
\gamma_n:H(\operatorname{div};B_1)\to H^{-1/2}(\partial B_1)
\]

is continuous. Therefore weak \(H(\operatorname{div})\) convergence preserves the zero normal trace:

\[
\boxed{V\cdot n=0\quad\text{on }\partial B_1}
\]

for every weak macroscopic bulk limit \(V\).

This conclusion does not require uniform H1 control and therefore survives the M19-237 thin tangential no-slip layer.

## 3. Curl-free + divergence-free + zero normal trace implies zero

The unit ball is simply connected. Hence a curl-free \(L^2\) field is a gradient:

\[
V=\nabla\Phi
\]

for an appropriate weak scalar potential.

Divergence-free gives

\[
\boxed{\Delta\Phi=0\quad\text{in }B_1.}
\]

The inherited normal trace gives

\[
\boxed{\partial_n\Phi=0\quad\text{on }\partial B_1.}
\]

Fix the additive constant by zero mean. Testing the harmonic equation with \(\Phi\) gives

\[
\int_{B_1}|\nabla\Phi|^2dx
=
\int_{\partial B_1}\Phi\,\partial_n\Phi\,dS
=0.
\]

Therefore

\[
\boxed{V\equiv0.}
\]

## 4. The regular potential-flow branch is closed

M19-238 proposed

\[
\mathcal T_{cav}^{bulk-return}
\subset
\mathcal T_{pot}^{match}
\cup
\mathcal T_{scaled-deriv}.
\]

The present normal-trace argument proves that every **nonzero regular macroscopic potential bulk** is impossible.

Thus

\[
\boxed{\mathcal T_{pot}^{match}\text{ is closed for nonzero weak macroscopic limits}.}
\]

The pressure degeneracy identified in M19-238 is real in an unconstrained interior problem, but the inherited no-penetration trace removes that freedom on the ball.

## 5. What remains when the weak macroscopic limit is zero

The conclusion \(V=0\) does not by itself contradict the original normalization

\[
\int_0^{S_j}\|V_j\|_2^2ds=1,
\]

because weak convergence may lose norm through concentration or oscillation.

Therefore the escape branch is now forced into a genuine macroscopic noncompactness mechanism:

1. **scaled derivative/oscillation loss** on interior macroscopic annuli; or
2. **velocity concentration into a shrinking relative boundary region**, so that \(V_j\rightharpoonup0\) although its total L2 norm stays one.

Both mechanisms are stronger than the already proved vorticity boundary localization.

## 6. Updated bulk-return frontier

The regular nonzero bulk alternative is removed. The remaining escape theorem is

\[
\boxed{
\mathcal T_{cav}^{bulk-loss}:
\begin{array}{l}
\text{exclude normalized cavity unit modes whose macroscopic weak limit is zero}\\
\text{through interior scaled-derivative decompactification or relative-boundary velocity concentration.}
\end{array}}
\]

Equivalently,

\[
\boxed{
\text{escape unit mode}
\Longrightarrow
\text{macroscopic L2 noncompactness beyond the regular potential sector}.}
\]

## 7. Important firewall

The argument uses only the normal component of the no-slip trace. Tangential trace is not weakly stable under the available L2/H(div) compactness because the M19-237 layer carries unbounded rescaled gradients.

Hence

\[
\boxed{
V\cdot n=0\text{ is inherited}
\quad\not\Rightarrow\quad
V|_{\partial B_1}=0\text{ is inherited}.}
\]

No full Dirichlet trace is claimed for the macroscopic weak limit.

## 8. Next calculation

The next target is to quantify the only remaining way for unit L2 mass to disappear weakly. A radial no-slip Hardy/Poincare estimate can test how thin a relative velocity-concentration layer may be under the fixed physical H1 currency from M19-232. In parallel, interior macroscopic oscillation can be measured by the rescaled derivative currency.

---

\[
\boxed{\text{M19-239 COMPLETE: EVERY NONZERO REGULAR POTENTIAL MACROSCOPIC BULK LIMIT IS EXCLUDED BY THE INHERITED ZERO NORMAL TRACE.}}
\]
