# Close-packet reach collapse is a merge-or-defect event

Date: 2026-08-18

Status: **STRUCTURAL COMPACT-LANE REDUCTION. TWO DISTINCT NATURAL-SCALE INTENSE PACKETS CANNOT APPROACH TO O(r) SEPARATION AND GAIN LARGE BIOT--SAVART WEIGHT WITHOUT EITHER CREATING VORTICITY MAGNITUDE/PROJECTIVE GRADIENT DEFECT, CREATING NON-AFFINE STRAIN VARIANCE, OR BECOMING ONE LARGER SIGNED-COHERENT AFFINE PATCH. GLOBAL REGULARITY NOT PROVED.**

## 1. Two close natural packets

Let the physical natural scale be

\[
r=K^{-1}.
\]

Suppose two dangerous packet cores of radius comparable to `r` have center separation at most `Cr`, with vorticity magnitude comparable to `K^2` on a fixed fraction of each core.

Choose a Gaussian probability window `gamma_L` of scale

\[
L\asymp r
\]

large enough to contain fixed fractions of both packets and the region between them.

Normalize the vorticity by the dangerous amplitude `K^2`, so the intense packet values are order one in this window.

## 2. Vorticity merge versus variance defect

Let

\[
m_\gamma=\int\gamma\Omega,
\qquad
\operatorname{Var}_\gamma(\Omega)
=\int\gamma|\Omega-m_\gamma|^2.
\]

There are two alternatives.

### A. Nontrivial vector variance

If the two packet values differ substantially in projective direction, sign, or magnitude, or if the field drops strongly between them, then

\[
\boxed{
\operatorname{Var}_\gamma(\Omega)
\ge v_0>0.
}
\]

The robust Gaussian Poincare bridge gives

\[
\operatorname{Var}_\gamma(\Omega)
\lesssim
L^2\int\gamma|\nabla\Omega|^2.
\]

Hence

\[
\boxed{
P_{\rm mag,\gamma}+P_{\rm ang,\gamma}
=\int\gamma|\nabla\Omega|^2
\gtrsim
v_0L^{-2}.
}
\]

In physical units this is exactly the natural-scale magnitude-interface / angular-gradient branch.

### B. Small vector variance

If

\[
\operatorname{Var}_\gamma(\Omega)\ll1,
\]

then the field is `L2(gamma)`-close to one constant **signed** vector `m_gamma` across the combined window.  Thus the two nominal packets are not projectively independent objects on this observation scale; their vorticity has merged into one larger signed-coherent patch.

This statement includes the region between the packet centers because a low-magnitude gap would itself contribute to the vector variance and hence to Case A.

## 3. Add the strain channel

On the combined window define

\[
V_{S,\gamma}
=\int\gamma|S-\bar S_\gamma|^2.
\]

In the small-vorticity-variance case, either

\[
\boxed{V_{S,\gamma}\ge s_0>0}
\]

and the event is a non-affine strain residual / same-scale source branch, or

\[
\boxed{V_{S,\gamma}\ll1}
\]

and both vorticity and strain are close to one affine signed-coherent state on the larger combined window.

The latter is exactly a **larger coherent patch**, not an unresolved close-pair interaction.

## 4. Compact reach-collapse trichotomy

Therefore a close-pair / reach-collapse event has the structural form

\[
\boxed{
\text{close packets}
\Longrightarrow
\begin{cases}
\text{magnitude/projective gradient defect},\\
\text{non-affine strain variance},\\
\text{larger signed-coherent affine merge}.
\end{cases}
}
\]

The third case migrates to the previously developed large-radius coherent / flux / Betchov geometry as the merged physical radius grows relative to the natural scale.

## 5. Consequence for the partner-source loophole

A same-scale Biot--Savart source cannot obtain an arbitrarily large weight merely by collapsing packet reach while avoiding all other ledgers.

- nonparallel/opposite/gapped close partners pay total vorticity-gradient action;
- close partners with strong strain mismatch pay residual-strain action;
- fully compatible close partners cease to be separate packets and become a larger coherent object.

Thus compact reach collapse is not an independent untyped reproduction mechanism.

## 6. Limitation

The lemma is structural and uses fixed nondegeneracy thresholds.  It does not prohibit the gradient/non-affine/coherent alternatives themselves, all of which remain compatible with a hypothetical singular cascade.

Status: **REACH COLLAPSE ROUTED TO GRADIENT DEFECT, NON-AFFINE STRAIN, OR LARGER COHERENT MERGE / NO FREE CLOSE-PAIR SOURCE / GLOBAL REGULARITY NOT PROVED.**