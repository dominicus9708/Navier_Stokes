# Local Betchov divergence identity and axial-extension routing

Date: 2026-08-15

Status: **EXACT LOCAL DIVERGENCE IDENTITY + CUTOFF ROUTING. A COHERENT AXIAL-EXTENSION CORE CANNOT REALIZE ITS LOCAL VORTEX-STRETCHING ACTION AS A CLOSED INTERNAL STATE: THE LOCAL BETCHOV MISMATCH MUST BE CARRIED BY A BOUNDARY CUBIC FLUX OR BY FAILURE OF THE AXIAL-EXTENSION/COHERENCE APPROXIMATION. THE BOUNDARY FLUX IS CONTROLLED BY ENSTROPHY AND PALINSTROPHY. GLOBAL REGULARITY NOT PROVED.**

## 1. Velocity-gradient notation

Let

\[
A_{ij}=\partial_j u_i,
\qquad
A=S+R,
\]

where

\[
S^T=S,
\qquad
R^T=-R,
\qquad
\operatorname{tr}A=\operatorname{tr}S=0.
\]

For vorticity `omega=curl u`,

\[
R v=\frac12\omega\times v,
\]

so

\[
R^2
=\frac14(\omega\otimes\omega-|\omega|^2I).
\]

Consequently

\[
\boxed{
\operatorname{tr}(A^3)
=
\operatorname{tr}(S^3)
+\frac34\omega\cdot S\omega.
}
\]

Because a trace-free symmetric `3x3` matrix satisfies

\[
\operatorname{tr}(S^3)=3\det S,
\]

this is the algebraic core of the Betchov relation.

## 2. `tr(A^3)` is an exact divergence

In components,

\[
\operatorname{tr}(A^3)
=
\partial_j u_i\,\partial_k u_j\,\partial_i u_k.
\]

Define

\[
\boxed{
(\mathcal F_A)_i
=
 u_k\,\partial_j u_i\,\partial_k u_j
-
\frac12u_i\,\operatorname{tr}(A^2).
}
\]

Differentiate the first term:

\[
\begin{aligned}
\partial_i
\left(u_k\partial_j u_i\partial_k u_j\right)
={}&
\partial_i u_k\partial_j u_i\partial_k u_j\\
&+u_k\partial_i\partial_j u_i\partial_k u_j\\
&+u_k\partial_j u_i\partial_i\partial_k u_j.
\end{aligned}
\]

The middle term vanishes because `div u=0`. The first term is `tr(A^3)`. For the last term,

\[
u_k\partial_k\operatorname{tr}(A^2)
=2u_k\partial_j u_i\partial_i\partial_k u_j,
\]

so incompressibility gives

\[
 u_k\partial_j u_i\partial_i\partial_k u_j
=
\frac12\nabla\cdot
\left(u\operatorname{tr}(A^2)\right).
\]

Hence

\[
\boxed{
\operatorname{tr}(A^3)
=\nabla\cdot\mathcal F_A.
}
\]

Combining with the algebraic decomposition yields the exact local Betchov divergence identity

\[
\boxed{
\omega\cdot S\omega
+4\det S
=\frac43\nabla\cdot\mathcal F_A.
}
\]

The usual whole-space Betchov relation follows by integrating this divergence for a sufficiently decaying smooth field.

## 3. Coherent axial-extension sign

Let `e` be the coherent vorticity axis and consider the ideal axial-extension strain

\[
\boxed{
S_{\rm ax}(a,e)
=a\left(e\otimes e-\frac12(I-e\otimes e)\right).
}
\]

Its eigenvalues are

\[
(-a/2,-a/2,a).
\]

For

\[
\omega=\Omega e,
\]

we have

\[
\omega\cdot S_{\rm ax}\omega
=a\Omega^2
\]

and

\[
4\det S_{\rm ax}=a^3.
\]

Therefore

\[
\boxed{
\omega\cdot S_{\rm ax}\omega
+4\det S_{\rm ax}
=a(\Omega^2+a^2).
}
\]

For genuine axial extension `a>0`, this is strictly positive.

Thus an aligned extensional vortex core is **not** locally self-Betchov-balanced. Its positive local vortex stretching plus positive determinant must be accompanied by a nonzero outward/localization flux in the exact divergence identity.

## 4. Stability under coherent-core errors

Suppose on a core region

\[
\omega=\Omega e+\eta,
\]

\[
S=S_{\rm ax}(a,e)+E_S,
\]

with

\[
|\Omega|\ge c_0,
\qquad
|\eta|+|E_S|\le\varepsilon
\]

and `a>=0`.

Polynomial continuity gives

\[
\boxed{
\omega\cdot S\omega+4\det S
\ge
c\,a(c_0^2+a^2)
-C_{c_0,a}\varepsilon.
}
\]

Hence on any subregion where the coherent axial-extension error is sufficiently small relative to the active extension rate, the local Betchov mismatch has a fixed positive sign and size comparable to

\[
a(1+a^2).
\]

In the critical coherent crossing, the vorticity coherence error is already `L2`-small because `V_omega=O(R^-4)`. If the strain-shape error is not small, that is a separate shape/projective/high-curvature defect and is routed outside the ideal Branch-3 core.

## 5. Cutoff local Betchov identity

Let `chi_R` be a smooth cutoff equal to one on `B_R`, supported in `B_{2R}`, with

\[
|\nabla\chi_R|\lesssim R^{-1}.
\]

Multiplying the exact divergence identity by `chi_R` and integrating gives

\[
\boxed{
\int\chi_R
\left(
\omega\cdot S\omega+4\det S
\right)dx
=-\frac43
\int\nabla\chi_R\cdot\mathcal F_A\,dx.
}
\]

Thus a positive coherent axial-extension mismatch inside the core must be balanced by a cubic velocity-gradient flux through the buffer annulus.

There is no purely interior cancellation if the core remains close to the aligned axial-extension configuration.

## 6. Bound the boundary cubic flux by enstrophy and palinstrophy

The flux satisfies schematically

\[
|\mathcal F_A|
\lesssim |u||\nabla u|^2.
\]

Therefore

\[
\left|
\int\nabla\chi_R\cdot\mathcal F_A dx
\right|
\lesssim
R^{-1}
\int_{B_{2R}\setminus B_R}
|u||\nabla u|^2dx.
\]

Using whole-space norms only enlarges the right-hand side. Sobolev gives

\[
\|u\|_6\lesssim\|\nabla u\|_2.
\]

Interpolation gives

\[
\|\nabla u\|_{12/5}
\lesssim
\|\nabla u\|_2^{3/4}
\|\nabla^2u\|_2^{1/4}.
\]

For incompressible whole-space flow,

\[
\|\nabla u\|_2\asymp\|\omega\|_2=E^{1/2},
\]

\[
\|\nabla^2u\|_2\asymp\|\nabla\omega\|_2=P^{1/2}.
\]

Hence

\[
\boxed{
\left|
\int\nabla\chi_R\cdot\mathcal F_A dx
\right|
\lesssim
R^{-1}E^{5/4}P^{1/4}.
}
\]

This yields the localized compatibility estimate

\[
\boxed{
\left|
\int\chi_R
(\omega\cdot S\omega+4\det S)dx
\right|
\lesssim
R^{-1}E^{5/4}P^{1/4}.
}
\]

## 7. Axial-extension core consequence

Suppose on a substantial fraction of a radius-`R` coherent core

\[
|\omega|\gtrsim1,
\qquad
S\approx S_{\rm ax}(a,e),
\qquad a>0,
\]

with sufficiently small shape/coherence error. Then

\[
\int\chi_R
(\omega\cdot S\omega+4\det S)dx
\gtrsim
R^3a
\]

when `a` is bounded, and more generally `~R^3a(1+a^2)`.

Consequently

\[
\boxed{
R^3a
\lesssim
R^{-1}E^{5/4}P^{1/4}
+\text{shape/coherence error}.
}
\]

Ignoring only the explicitly typed error branch,

\[
\boxed{
aR^4\lesssim E^{5/4}P^{1/4}.}
\]

Equivalently,

\[
\boxed{
P
\gtrsim
\frac{a^4R^{16}}{E^5}.
}
\]

Thus a coherent axial-extension core can be maintained only by paying through at least one of

1. large global/nearby enstrophy `E`;
2. large palinstrophy `P`;
3. strain-shape/coherence breakdown;
4. large boundary/shell cubic flux, which is exactly what the displayed `E`--`P` bound measures.

## 8. Single-core compact specialization

If the relevant state is a single coherent core with

\[
E\lesssim CR^3,
\]

then

\[
\boxed{
P\gtrsim c\,a^4R.
}
\]

Therefore a source-active coherent axial extension with no large enstrophy reservoir necessarily activates a derivative/palinstrophy channel.

If instead

\[
E\gg R^3,
\]

then the local coherent core is embedded in a large external enstrophy reservoir. This is the global-enstrophy/multicore branch already routed to positive-middle-strain and spatial aggregation geometry.

## 9. Revised Branch-3 interpretation

The final coherent strain lane is no longer simply

\[
\text{axial extension of a vortex tube}.
\]

It has the exact local routing

\[
\boxed{
\text{coherent axial extension}
\Rightarrow
\text{Betchov boundary flux}
\lor
\text{shape/coherence defect}.
}
\]

Quantitatively this becomes

\[
\boxed{
\text{coherent axial extension}
\Rightarrow
\text{large enstrophy reservoir}
\lor
\text{palinstrophy}
\lor
\text{shape defect}.
}
\]

Thus even the Burgers-vortex-like final structure cannot be treated as a closed local amplification mechanism in a finite-energy whole-space flow.

The remaining proof obligation is to show that the compensating enstrophy/palinstrophy/shape-defect action cannot be repeated on infinitely many adaptive first-hitting steps without entering an already regularity-controlling critical norm.

Status: **LOCAL AXIAL-EXTENSION SELF-CLOSURE EXCLUDED / FINAL STRAIN LANE ROUTED TO ENSTROPHY RESERVOIR, PALINSTROPHY, OR SHAPE DEFECT / GLOBAL REGULARITY NOT PROVED.**
