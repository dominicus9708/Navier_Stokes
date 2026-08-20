# Positive-Middle Transverse Ribbon / Projective-Swap Gate — 2026-08-21

Status: **SMOOTH COHERENT-TUBE GEOMETRY GATE / GLOBAL REGULARITY NOT PROVED.**

This note attacks the complementary branch in which the scale-invariant signed vorticity flux is not substantially changed by viscosity. Then amplification must be supplied primarily by material deformation/vortex stretching. On the positive-middle lane this has a specific transverse geometric consequence.

## 1. Coherent transverse plane

Work at an actual smooth first-hitting stage. Assume the vorticity direction is aligned, to the already tracked small alignment error, with the largest strain eigenvector \(e_3\):

\[
\xi\simeq e_3.
\]

Write the strain eigenvalues

\[
s_1\le s_2\le s_3,
\qquad
s_1+s_2+s_3=0.
\]

On the positive-middle branch

\[
\boxed{s_1<0\le s_2\le s_3.}
\]

A material cross-section transverse to the vortex direction has instantaneous principal tangent rates \(s_1,s_2\) when the transverse eigenframe remains coherent with the material frame.

## 2. Area contraction versus aspect-ratio growth

Let \(\ell_1,\ell_2\) denote the two principal transverse material lengths. Then

\[
\frac d{dt}\log(\ell_1\ell_2)
=s_1+s_2
=-s_3.
\]

Thus the transverse area contracts at rate \(s_3\).

The aspect ratio obeys

\[
\frac d{dt}\log\frac{\ell_2}{\ell_1}
=s_2-s_1.
\]

Using trace freeness,

\[
s_2-s_1
=s_2+(s_2+s_3)
=s_3+2s_2
\ge s_3.
\]

Therefore

\[
\boxed{
\frac d{dt}\log(\mathrm{AR})
\ge
-\frac d{dt}\log(\mathrm{Area}).
}
\]

If one geometric first-hitting amplification step \(W\to qW\) is produced by coherent vortex stretching with approximately conserved material flux, then the transverse area must contract by approximately \(q^{-1}\):

\[
\Delta\log(\mathrm{Area})\lesssim-\log q.
\]

Hence

\[
\boxed{
\Delta\log(\mathrm{AR})\gtrsim\log q,
\qquad
\mathrm{AR}_{out}\gtrsim q\,\mathrm{AR}_{in}.
}
\]

For an initially round transverse disk this means that the coherent material image becomes at least \(q\)-times anisotropic after one stage unless the transverse eigenframe is substantially reorganized.

## 3. q=2 geometric replacement fraction

For the standard geometric step \(q=2\), consider the ideal coherent-affine case. An initially circular cross-section whose area is halved and whose aspect ratio is at least two becomes an ellipse with semiaxes

\[
R\sqrt2,
\qquad
R/\sqrt2,
\]

when compared with the next equal-area circular natural-scale disk of radius \(R\).

The ellipse is contained in the strip

\[
|y_2|\le R/\sqrt2.
\]

The fraction of the target disk contained in this strip is exactly

\[
F_2
=
\frac2\pi
\left[
\arcsin\frac1{\sqrt2}
+\frac1{\sqrt2}\sqrt{1-\frac12}
\right]
=
\frac12+\frac1\pi.
\]

Numerically,

\[
\boxed{F_2\approx0.8183098862.}
\]

Therefore a coherent affine positive-middle tube with no substantial transverse eigenframe reorganization cannot fill more than this fraction of the next round thick cross-section from the same material image. At least

\[
\boxed{
1-F_2
=
\frac12-\frac1\pi
\approx0.1816901138
}
\]

of the next transverse disk must be supplied by

1. different material labels;
2. non-affine transverse rearrangement;
3. viscous cross-surface flux transfer;
4. or a substantial rotation/reorganization of the transverse strain eigenframe.

This is a fixed one-stage geometric turnover fraction, not an asymptotic statement.

## 4. Why eigenframe reorganization is the only coherent escape

If the transverse eigenframe remains approximately fixed, the aspect ratio multiplies by at least \(q\) on every flux-preserving stage. Thus after \(n\) such stages

\[
\mathrm{AR}_n\gtrsim q^n\mathrm{AR}_0.
\]

A persistent analytic-scale thick core cannot remain round/thick under this unbounded ribbonization. Before that happens the core must either

- become one-dimensionally sparse in a transverse direction, activating the known geometric regularity gate;
- replace a fixed fraction of the high-vorticity transverse material set;
- or reorganize the eigenframe/projective strain geometry.

Therefore an indefinitely thick coherent positive-middle survivor requires repeated transverse eigenframe reorganization.

## 5. Projective distance of a transverse eigenaxis swap

For the positive-middle spectrum

\[
S=m\,\mathrm{diag}(-2,1-x,1+x),
\qquad 0\le x\le1,
\]

consider a 90-degree rotation about \(e_3\), which swaps the two transverse eigenaxes:

\[
S^{swap}=m\,\mathrm{diag}(1-x,-2,1+x).
\]

The normalized Frobenius inner product is

\[
\cos\Theta_{swap}(x)
=
\frac{2s_1s_2+s_3^2}
{s_1^2+s_2^2+s_3^2}.
\]

On the current H1-efficient middle-zero side

\[
x\in[x_*,1],
\qquad
x_*=\frac{3(\sqrt3-1)}4,
\]

this projective angle is bounded below by its value at \(x=1\):

\[
\boxed{
\Theta_{swap}(x)\ge\frac\pi3.
}
\]

Thus an actual transverse-axis swap costs at least \(\pi/3\) of normalized strain-shape path length in projective Frobenius geometry.

This does not yet prove that every thick survivor must execute an exact swap on every stage. It supplies the quantitative cost once the anti-ribbon mechanism is shown to require such a swap or an equivalent projective excursion.

## 6. Current smooth trichotomy

For a thick signed flux-carrying positive-middle first-hitting core, one finite stage is now forced toward

\[
\boxed{
\text{viscous material-flux change}
\ \lor\ 
\text{transverse material turnover/non-affine rearrangement}
\ \lor\ 
\text{projective eigenframe reorganization}.
}
\]

The first branch is now controlled by `SMOOTH_THICK_CORE_FLUX_ENSTROPHY_GATE_2026-08-21.md`.

The second branch is a literal fixed-fraction turnover in the coherent-affine benchmark (18.169% for \(q=2\)).

The third branch carries a projective shape-action requirement; a full 90-degree transverse swap has path length at least \(\pi/3\) on the remaining positive-middle spectral sector.

## 7. Main remaining obligation

The next rigorous target is a deformation-control lemma of the form

\[
\boxed{
\text{bounded transverse aspect ratio over a positive-middle stage}
\Longrightarrow
\text{projective/eigenframe action}\ge a_{rot}>0
}
\]

without assuming an exactly affine or perfectly coaxial material cross-section.

If the deformation ceases to be sufficiently affine/coherent for that lemma, the resulting spatial variation itself is to be measured against the existing derivative/eigenaxis-bending \(H/T\) channels.

Status: **FLUX-PRESERVING POSITIVE-MIDDLE STRETCHING HAS A BUILT-IN RIBBONIZATION TAX. COHERENT FIXED-AXIS CONTINUATION CANNOT REMAIN THICK; THICK SURVIVAL REQUIRES FIXED-FRACTION TRANSVERSE REPLACEMENT OR A QUANTITATIVE PROJECTIVE EIGENFRAME REORGANIZATION.**