# Localizing the Sobolev saturation gap: coherent extension, magnitude interface, or angular/projective defect

Date: 2026-08-18

Status: **LOCALIZATION AUDIT / CORRECTION OF SCOPE. THE BIANCHI--EGNELL COEFFICIENT GAP IS GLOBAL. APPLYING IT TO A COMPACT COHERENT CELL REQUIRES A BUFFERED CUTOFF; FAILURE OF AXIAL CUTOFF SMALLNESS IS NOT FREE BUT RETURNS TO LONG COHERENT L3 EXTENSION, MAGNITUDE-INTERFACE PALINSTROPHY, OR ANGULAR/PROJECTIVE DEFECT. GLOBAL REGULARITY NOT PROVED.**

## 1. Global gap versus local cell

The global coherence-versus-Sobolev lemma gives a strict sharp-Sobolev deficit when

\[
\|\partial_e\rho\|_2
\ll
\|\nabla\rho\|_2,
\qquad
\rho=|\omega|.
\]

For a compact cell one instead applies Sobolev to a localized scalar

\[
f=\chi\rho.
\]

Then

\[
\boxed{
\partial_e f
=\chi\partial_e\rho
+\rho\partial_e\chi.
}
\]

The second term prevents one from silently importing the global Bianchi--Egnell gap into an unbuffered unit ball.

## 2. Long axial buffer makes the cutoff term small

Consider a signed-coherent tube-like region of natural radius `r` and axial coherent length `L`.  Choose a cutoff that changes only near the ends on an axial scale comparable to `L`.

Schematically

\[
|\partial_e\chi|\lesssim L^{-1}.
\]

If the vorticity magnitude is of natural size `r^-2` in a tube volume `~r^2L`, then

\[
\|\rho\partial_e\chi\|_2^2
\lesssim
r^{-4}L^{-2}(r^2L)
\asymp
\frac1{r^2L}.
\]

After natural rescaling `r=1`, the cutoff directional derivative is `O(L^-1/2)` in `L2`.  Thus a sufficiently long coherent buffer allows the global directional-invariance/Sobolev-stability mechanism to become effective.

## 3. But long coherent extension pays endpoint L3

A signed circulation flux `Gamma>=gamma0` along a tube with radius `r` and embedded length `L` gives

\[
\boxed{
\|u\|_3^3
\gtrsim
c\Gamma^3\frac{L}{r}.
}
\]

Therefore making the axial cutoff error small by taking `L/r >>1` creates a proportionally large endpoint-critical `L3` cost.

## 4. Short termination pays magnitude gradient

Suppose instead the coherent magnitude drops from its natural value `~r^-2` to a much smaller value over an axial transition length `L` while the projective axis remains essentially fixed.

A one-dimensional Cauchy/Poincare estimate along each coherent cross-section gives schematically

\[
\int |\partial_e\rho|^2dz
\gtrsim
\frac{r^{-4}}{L}.
\]

Integrating over cross-sectional area `~r^2` yields

\[
\boxed{
P_{\rm mag,terminal}
\gtrsim
\frac1{r^2L}.
}
\]

Equivalently, in the scale-invariant normalized form,

\[
\boxed{
r^3P_{\rm mag}
\gtrsim
\frac{r}{L}.
}
\]

Combining with the circulation `L3` estimate gives the spatial duration-free product

\[
\boxed{
\left(r^3P_{\rm mag}
\right)
\|u\|_3^3
\gtrsim
c\Gamma^3,
}
\]

for a straight signed-coherent tube that terminates through magnitude decay.

Thus a short coherent buffer pays magnitude-gradient cost; a long coherent buffer pays `L3`.

## 5. Bending / closure pays angular or projective cost

A divergence-free vorticity tube need not terminate by magnitude decay; it may bend, close, spread, or interact with another flux structure.

If the vorticity direction changes while the magnitude remains intense, the cost appears in

\[
P_{\rm ang}
=\int\rho^2|\nabla\xi|^2.
\]

If the direction/magnitude changes through packet interfaces or partner interaction, the robust weighted variance/Poincare route gives

\[
D_{\rm proj}+D_{\rm line}
\lesssim
r^2(P_{\rm mag}+P_{\rm ang}).
\]

Thus bending/closure does not create an unpriced localization escape.

## 6. Correct localized use of the Bianchi--Egnell gap

A compact coherent cell therefore has the following localization alternatives:

\[
\boxed{
\begin{cases}
\text{long signed-coherent extension} &\Rightarrow \text{large }L^3,\\
\text{magnitude termination/interface} &\Rightarrow P_{\rm mag},\\
\text{direction bending/partner transition} &\Rightarrow P_{\rm ang}/\text{projective defect},\\
\text{derivative transverse axis content} &\Rightarrow C_1-C_0/J_1\text{ mismatch},\\
\text{well-buffered axis-coherent case} &\Rightarrow \text{Bianchi--Egnell strict Sobolev deficit}.
\end{cases}
}
\]

The global stability theorem is used only in the final well-buffered alternative.

## 7. Claim boundary

The tube estimates require a quantitatively coherent signed flux geometry on a fixed fraction of the indicated region.  Failure of that geometry is itself routed to the existing partner/residual/reach branches; no claim is made that every compact cell automatically contains such a tube.

Status: **GLOBAL SOBOLEV GAP LOCALIZED ONLY AFTER BUFFER AUDIT / CUTOFF ESCAPE ROUTED TO L3, P_mag, P_ang, OR DERIVATIVE PROJECTIVE MISMATCH / GLOBAL REGULARITY NOT PROVED.**