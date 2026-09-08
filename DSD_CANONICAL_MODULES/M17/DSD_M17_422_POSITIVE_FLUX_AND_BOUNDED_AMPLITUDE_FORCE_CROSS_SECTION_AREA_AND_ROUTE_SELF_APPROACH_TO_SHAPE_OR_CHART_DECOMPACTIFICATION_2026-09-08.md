# DSD M17-422 — Positive flux plus bounded amplitude forces cross-section area and routes nonlocal self-approach to shape/chart decompactification

Date: 2026-09-08  
Canonical ID: **M17-422**

Status: **ACTIVE SELF-APPROACH REDUCTION / FLUX-AREA GEOMETRY / CROSS-SECTION DECOMPACTIFICATION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-421

M17-421 gives the exact geometry split

\[
G_{reach\ collapse}
\Longrightarrow
G_{curvature/C^2\ decompactification}
\lor
G_{nonlocal\ self\text{-}approach}.
\]

Inside a genuinely `C^2`-precompact loop family, curvature blow-up is excluded, so only nonlocal self-approach remains.

Geometry alone cannot send this second branch to palinstrophy.

The present module adds the retained **positive vortex flux**.

## 2. Material vortex-tube flux

Let `T` be a regular material vortex tube around the closed vortex loop, and let `S` be a material cross-section transverse to the vorticity.

Its oriented flux is

\[
\Phi
=
\int_S\Omega\cdot n\,dA.
\]

On the retained positive-flux branch,

\[
\boxed{\Phi\ge\Phi_*>0.}
\]

Assume also the compact amplitude ceiling

\[
\boxed{|\Omega|\le M_\rho<\infty.}
\]

Then

\[
\Phi
\le
\int_S|\Omega|dA
\le
M_\rho |S|.
\]

Hence every retained material cross-section satisfies

\[
\boxed{
|S|
\ge
A_*:=\frac{\Phi_*}{M_\rho}>0.
}
\]

This lower bound uses no CE-H coefficient information.

## 3. Consequence for cross-section diameter

For every measurable planar cross-section,

\[
|S|
\le C\,\operatorname{diam}(S)^2
\]

with a universal planar constant. Therefore

\[
\boxed{
\operatorname{diam}(S)
\ge
c_A\sqrt{A_*}>0.
}
\]

A retained positive-flux tube with bounded amplitude therefore cannot collapse isotropically to a zero-radius filament.

If a normal-chart tube radius tends to zero, some other cross-sectional length must remain macroscopic.

## 4. Doubly-critical near-contact geometry

Let `p_j,q_j` be a doubly-critical self-approaching pair on the same centerline loop with

\[
d_j:=|p_j-q_j|\to0.
\]

At a doubly-critical pair, the chord

\[
e_j:=\frac{q_j-p_j}{|q_j-p_j|}
\]

is perpendicular to both loop tangents. Thus `e_j` lies in both normal planes.

If the vortex tube is represented by uniformly centered, uniformly shape-compact normal cross-sections around the centerline, embeddedness requires the available width of the two facing cross-sections in the `e_j` direction to shrink with `d_j`.

Schematically,

\[
w_{e_j}(S_{p_j})+w_{e_j}(S_{q_j})
\lesssim d_j.
\]

The precise constant depends only on the fixed centering/bounded-overlap convention.

## 5. Width-area tradeoff

For any planar set `S`, if `w_e(S)` is its width in one direction and `D(S)` is its diameter, then

\[
|S|\le w_e(S)D(S).
\]

Therefore, using `|S|>=A_*`,

\[
\boxed{
D(S)
\ge
\frac{A_*}{w_e(S)}.
}
\]

If self-approach forces

\[
w_e(S)\lesssim d_j\to0,
\]

then

\[
\boxed{
D(S)\gtrsim\frac{A_*}{d_j}\to\infty.
}
\]

Thus fixed positive flux cannot coexist with bounded amplitude, shrinking self-clearance, and uniformly compact cross-section shape/diameter.

## 6. Exact self-approach split

Consequently the nonlocal self-approach exit reduces to

\[
\boxed{
\begin{aligned}
G_{nonlocal\ self\text{-}approach}
\Longrightarrow{}&
G_{positive\ flux\ thinning/loss}
\\
&\lor G_{amplitude\ ceiling\ loss}
\\
&\lor G_{cross\text{-}section\ eccentricity/diameter\ decompactification}
\\
&\lor G_{normal\text{-}chart/centering\ failure}
\\
&\lor G_{tube\ injectivity/topology\ loss}.
\end{aligned}
}
\]

There is no separate retained compact self-approach state with all of these quantities uniformly controlled.

## 7. Bounded parent-cell version

Suppose in addition that each normalized record state remains in a fixed parent spatial cell of diameter `D_*`.

Then

\[
D(S)\le D_*.
\]

The width-area estimate gives

\[
w_e(S)
\ge
\frac{A_*}{D_*}.
\]

Hence the doubly-critical clearance has a positive lower bound

\[
\boxed{
d_j\ge c\frac{A_*}{D_*}>0}
\]

whenever the centered normal-chart convention and bounded-overlap embedding remain valid.

Thus in a fully retained parent-bounded geometry, nonlocal self-approach itself is impossible.

## 8. What is and is not closed

This module does **not** claim that positive flux alone supplies a round cross-section or a disk tube.

A tube may avoid collision by becoming arbitrarily ribbon-like, by shifting the vorticity-bearing region far from the chosen core, or by losing the normal-coordinate representation.

Those are precisely the explicit exits retained above.

Therefore the valid conclusion is not

\[
G_{self\text{-}approach}\Rightarrow\text{contradiction}
\]

without hypotheses, but rather

\[
\boxed{
G_{self\text{-}approach}
\Rightarrow
G_{flux/amplitude\ exit}
\lor
G_{cross\text{-}section/chart/topology\ decompactification}.
}
\]

## 9. Relation to M17-420

M17-420 assumed tubular reach or equivalent bounded-overlap segmentation as part of the retained compact loop state.

M17-421--422 now explain what failure of that hypothesis means:

- local curvature collapse is geometric `C^2` decompactification;
- nonlocal self-approach under positive flux is cross-section/chart/topology decompactification unless flux or amplitude compactness fails.

Thus `tubular reach/self-clustering` is no longer an opaque single exit.

## 10. Next target

The remaining new geometry subbranch is

\[
G_{cross\text{-}section\ eccentricity/shape\ decompactification}.
\]

The next audit should test whether incompressible material-area transport and strain deformation give a standard-energy cost for unbounded aspect ratio, or whether ribbonization can occur with only the already known logarithmic deformation cost.

This is M17-423.

## 11. DSD audit

DSD is used only to distinguish conserved/retained flux content from the geometric carrier shape.

The mathematical content is flux-area comparison plus elementary planar width-area geometry.

## 12. Audit verdict

**PASS as a self-approach compression theorem.**

Under retained positive flux and amplitude ceiling, self-approach cannot remain geometrically compact: it must produce cross-section/chart/topology decompactification or lose flux/amplitude compactness.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
