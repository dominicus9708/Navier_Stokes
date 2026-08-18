# Unit-cell audit against the local critical vorticity-coherence criterion

Date: 2026-08-18

Status: **LITERATURE-CROSS-CHECK + SCALING AUDIT. THE SAME-SCALE UNIT-CELL BRANCH SATURATES, RATHER THAN AUTOMATICALLY IMPROVES, THE KNOWN LOCAL HYBRID VORTICITY-MAGNITUDE / DIRECTION-COHERENCE REGULARITY CLASS. GLOBAL REGULARITY NOT PROVED.**

## 1. External criterion used only as a boundary check

Grujic--Guberovic (Commun. Math. Phys. 298 (2010), 407--418, DOI 10.1007/s00220-010-1000-4) define

\[
\rho_{\gamma,r}(x,t)
=
\sup_{y\in B(x,r),\,y\ne x}
\frac{|\sin\phi(\eta(x,t),\eta(y,t))|}{|x-y|^\gamma}
\]

for the vorticity direction `eta`.  Their local hybrid criterion uses

\[
\int
\left(
\int
|\omega|^\alpha
\rho_{\gamma,2r}^\alpha
\,dx
\right)^\delta dt
<\infty,
\]

where

\[
0<\gamma<1,
\qquad
\frac{3}{\gamma+2}<\alpha<\frac3\gamma,
\qquad
\delta
=
\frac{2}{(2+\gamma)\alpha-3}.
\]

The special critical direction-coherence case is

\[
\gamma=\frac12,
\qquad
\alpha=2,
\qquad
\delta=1,
\]

so the hybrid quantity is

\[
\boxed{
\mathcal H_{1/2,2}
=
\int\!\int
\left(\rho_{1/2,2r}|\omega|\right)^2dxdt.
}
\]

This criterion is imported only as a known regularity boundary; no novelty is claimed for it.

## 2. Natural physical unit-cell scaling

Let the terminal physical vorticity frequency be

\[
K=\sqrt W.
\]

A natural packet has

\[
r\asymp K^{-1},
\qquad
|\omega|\asymp K^2,
\qquad
|B_r|\asymp K^{-3},
\qquad
\Delta t\asymp K^{-2}.
\]

To obtain an order-one change of vorticity direction across a natural ball at the critical Holder exponent `1/2`, the physical seminorm has size

\[
\boxed{
\rho_{1/2,r}\asymp K^{1/2}.
}
\]

Hence on one packet

\[
\left(\rho_{1/2,r}|\omega|\right)^2
\asymp
K^5.
\]

Multiplying by natural packet volume and natural time gives

\[
\boxed{
K^5\,K^{-3}\,K^{-2}
\asymp1.
}
\]

Thus one critically rough natural packet contributes order one to the local hybrid criterion.

## 3. Packet multiplicity

For `N` bounded-overlap natural packets active in the same natural time block, the spatial integral is additive up to overlap constants. Therefore

\[
\boxed{
\mathcal H_{1/2,2}^{\rm block}
\gtrsim cN
}
\]

provided a fixed fraction of the packets carry the critical directional roughness throughout a fixed fraction of the block.

Consequently a compact multiplicity cascade with

\[
N_j\to\infty
\]

is not automatically excluded by the known hybrid theorem: it can evade the regularity hypothesis precisely by making the hybrid critical quantity diverge.

## 4. Relation to exact angular damping

The repository's exact magnitude equation supplies a different but compatible quantity,

\[
P_{\rm ang}
=\int |\omega|^2|\nabla\xi|^2dx.
\]

A smooth unit-scale direction variation of order one gives, in physical variables,

\[
|\nabla\xi|\asymp K,
\]

and hence one packet has instantaneous angular palinstrophy

\[
P_{\rm ang,packet}
\asymp
K^4K^2K^{-3}
=K^3.
\]

Over one natural physical time `K^-2`,

\[
\boxed{
\int P_{\rm ang,packet}dt
\asymp K.
}
\]

There is no known global finite budget for this palinstrophy action, so this scaling alone is not a contradiction.  The exact adjoint-kernel magnitude identity instead states that this angular loss must be repaid by stretching.

## 5. Why `H1` angular control does not imply the Holder criterion

The local angular damping quantity is an `H1`-type control of the direction weighted by `|omega|^2`.  In three spatial dimensions, `H1` does not embed in `C^(1/2)`.  Therefore one cannot deduce a bound on the pointwise Holder seminorm `rho_(1/2,r)` from angular palinstrophy alone.

Closing that bridge would require additional regularity, such as a higher derivative / Morrey-type reserve, which is already a V2/high-derivative branch in the repository.

Hence the critical Holder criterion cannot be silently invoked to close the angular lane.

## 6. Stress-test conclusion

The same-scale compact branch reaches the known geometric-analytic regularity boundary exactly:

\[
\boxed{
\rho_{1/2,r}\sim K^{1/2}
\quad\text{on}\quad
r\sim K^{-1}
}
\]

is scale critical, and each natural packet contributes order one to the critical hybrid spacetime quantity.

Therefore the known criterion confirms the location of the wall rather than removing it.

The DSD route must exploit additional organization not present in the generic hybrid condition, namely one or more of

- signed/projective packet organization;
- exact I/V genealogy;
- heterochiral mixing necessity;
- common-strain cone extraction;
- local Betchov compensation;
- cross-scale/derivative packing.

Status: **KNOWN LOCAL HYBRID CRITERION EXACTLY SATURATED BY A CRITICALLY ROUGH UNIT CELL / NO AUTOMATIC REGULARITY GAIN / FINAL COMPACT WALL REMAINS STRUCTURED SAME-SCALE INTERACTION.**