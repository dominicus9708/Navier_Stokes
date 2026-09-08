# DSD M17-424 — Incompressibility forces any fixed positive-volume material CE-H tube to decompactify in similarity space

Date: 2026-09-08  
Canonical ID: **M17-424**

Status: **ACTIVE MATERIAL-VOLUME THEOREM / SIMILARITY-SPATIAL DECOMPACTIFICATION / TUBE-GENEALOGY AUDIT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Motivation

M17-421--423 reduce tubular-reach loss to curvature, self-approach, cross-section shape/chart, flux/amplitude, or spatial decompactification. M17-423 shows that ribbonization pays only logarithmic strain and therefore does not by itself beat the standard-energy weight.

The present module asks a different question:

> Can a **fixed material vortex tube of positive physical volume** remain bounded in similarity space as `t -> 0-`?

The answer is no, by incompressibility alone.

This is a spatial-decompactification theorem, not a global regularity contradiction.

## 2. Exact material genealogy input

M17-359 proves on exact regular CE-H that the physical/similarity material flow preserves vortex-line identity until a nodal, cutoff/interface, CE-H/rank, or flow/domain exit occurs.

M17-358 organizes a coherent regular material-flux family into material tube-label bands

\[
\Lambda=\bigsqcup_i\Lambda_i.
\]

Therefore there is a legitimate fixed-label subbranch: choose one nondegenerate material tube-label band at a reference time and transport the same labels by the material flow.

Important distinction:

- the **material labels** are fixed on this subbranch;
- the numerical vortex flux through that material tube is not generally conserved under viscosity.

M17-389 already gives the exact diffusive flux law on CE-H, so no frozen-in flux theorem is used here.

## 3. Positive initial physical volume

Let `T_ph(t0)` be a regular material tube-label band at some physical reference time `t0<0`.

Assume it is nondegenerate: its loop length is positive and its cross-sectional material label set has positive area. Equivalently,

\[
\boxed{
V_0:=|\mathcal T_{ph}(t_0)|>0.
}
\]

A retained positive flux together with a finite amplitude ceiling at the reference time is one sufficient way to guarantee positive cross-sectional area:

\[
\Phi(t_0)\le M_\rho(t_0) A(t_0),
\]

so `Phi(t0)>0` and `M_rho(t0)<infinity` imply `A(t0)>0`.

The argument below only needs `V0>0`.

## 4. Physical incompressibility preserves the tube volume

Let `X_ph(a,t)` be the physical Navier--Stokes flow map. Since

\[
\nabla\cdot u=0,
\]

its Jacobian satisfies

\[
\frac d{dt}\det D_aX_{ph}
=(\nabla\cdot u)(X_{ph},t)\det D_aX_{ph}=0.
\]

Hence

\[
\boxed{
\det D_aX_{ph}=1.
}
\]

For the fixed material label set,

\[
\boxed{
|\mathcal T_{ph}(t)|=V_0
}
\]

for every regular time on which the material genealogy persists.

This statement is completely independent of viscous vorticity-flux diffusion.

## 5. Similarity coordinates

Write

\[
s:=-t>0,
\qquad
\theta=-\log s,
\qquad
y=\frac{x}{\sqrt{s}}.
\]

Physical and similarity volume elements satisfy

\[
dx=s^{3/2}dy.
\]

Therefore the same fixed material tube has similarity volume

\[
|\mathcal T_{sim}(\theta)|
=s^{-3/2}|\mathcal T_{ph}(t)|.
\]

Using physical material-volume conservation,

\[
\boxed{
|\mathcal T_{sim}(\theta)|
=V_0e^{3\theta/2}.
}
\]

Thus

\[
\boxed{
|\mathcal T_{sim}(\theta)|\to\infty
\qquad(\theta\to\infty).
}
\]

This growth is exact.

## 6. Immediate bounded-domain contradiction

Suppose the entire fixed material tube remained in one similarity ball of uniformly bounded radius:

\[
\mathcal T_{sim}(\theta)\subset B_M
\]

for all sufficiently large `theta`.

Then

\[
|\mathcal T_{sim}(\theta)|\le |B_M|<\infty,
\]

contradicting

\[
|\mathcal T_{sim}(\theta)|=V_0e^{3\theta/2}\to\infty.
\]

Hence

\[
\boxed{
\text{fixed positive-volume material tube}
\Longrightarrow
\text{similarity-space spatial decompactification}.
}
\]

Equivalently, a fixed positive-volume material set cannot remain inside a physical core of diameter `O(sqrt{s})`, whose volume is only `O(s^{3/2})`.

## 7. Cross-section consequence under a regular tube chart

Assume additionally that a regular tube chart survives with uniformly comparable Jacobian and that the similarity centerline length remains bounded:

\[
0<\ell_*\le \ell_{sim}(\theta)\le\ell^*<\infty.
\]

Then the mean similarity cross-sectional area must obey

\[
\bar A_{sim}(\theta)
\gtrsim
\frac{|\mathcal T_{sim}(\theta)|}{\ell_{sim}(\theta)}.
\]

Thus

\[
\boxed{
\bar A_{sim}(\theta)
\gtrsim
cV_0e^{3\theta/2}.
}
\]

Using planar area versus diameter,

\[
A\le C D^2,
\]

at least one cross-section has

\[
\boxed{
D_{sim}(\theta)
\gtrsim
cV_0^{1/2}e^{3\theta/4}.
}
\]

Hence cross-section diameter escape is not merely possible on the fixed material-tube subbranch; it is forced.

The corresponding physical diameter lower scale is

\[
D_{ph}=\sqrt{s}D_{sim}
\gtrsim e^{-\theta/2}e^{3\theta/4}
=e^{\theta/4}
=s^{-1/4},
\]

provided the regular chart/mean-area comparison remains valid.

This last physical-diameter statement is chart-conditional; the total-volume decompactification theorem in Section 6 is not.

## 8. Similarity material divergence check

M17-359 uses the similarity material velocity

\[
B=U+\frac12y.
\]

Since `div U=0`,

\[
\boxed{
\nabla_y\cdot B=\frac32.
}
\]

Therefore a similarity material volume obeys

\[
\frac d{d\theta}|\mathcal T_{sim}|
=\frac32|\mathcal T_{sim}|,
\]

whose solution is exactly

\[
|\mathcal T_{sim}(\theta)|
=e^{3(\theta-\theta_0)/2}|\mathcal T_{sim}(\theta_0)|.
\]

This independently confirms Section 5.

## 9. Consequence for M17-420 retained hypotheses

M17-420 closes the compact positive-flux loop branch under retained regular geometry, including enough tubular reach or bounded-overlap segmentation for its raw-H2 packet construction.

The present theorem shows a crucial distinction:

- a **compact centerline loop state** may persist in similarity space;
- a **fixed positive-volume material tube around it cannot remain spatially compact**.

Therefore any use of a positive-flux tube family around the compact loop must fall into one of two cases:

\[
\boxed{
\begin{aligned}
H_{fixed\ material\ tube}
&\Longrightarrow
G_{forced\ similarity\ spatial\ decompactification},\\
H_{time\text{-}dependent\ selected\ tube}
&\Longrightarrow
G_{selection/allocation/genealogy\ bookkeeping}.
\end{aligned}
}
\]

The second case is not true destruction of the underlying material vortex-line genealogy; it means the activity-carrying tube band selected by the proof changes or shrinks in label measure.

## 10. Flux and volume must not be conflated

The present theorem does **not** assert conservation of vortex flux.

On CE-H the material flux changes diffusively according to the previously certified law. The invariant used here is only Lebesgue volume of a fixed material particle set.

Thus

\[
\boxed{
\text{material-label conservation}
\neq
\text{vortex-flux conservation}.
}
\]

This distinction is mandatory for all later tube arguments.

## 11. Reinterpretation of M17-421--423

For a fixed material tube, M17-421--423's cross-section/spatial decompactification is not an optional pathological scenario. It is required by similarity scaling and incompressibility.

Hence ribbonization or diameter escape should not be expected to yield a contradiction merely from its existence.

The contradiction target must instead be one of:

1. prove the late CE-H proof requires one fixed positive-volume tube to remain in a bounded similarity region — then Section 6 closes that subbranch immediately;
2. prove the activity-carrying selected tube cannot continually change/shrink in material-label measure;
3. attach a finite ancestral resource to the rate/multiplicity of the forced spatial escape;
4. route spatial escape to an already typed domain/genealogy exit.

## 12. Corrected geometry frontier

The late closed-loop tube branch now has the sharper split

\[
\boxed{
\begin{aligned}
H_{compact\ centerline\ loop}
\Longrightarrow{}&
G_{fixed\ material\ tube\ similarity\ decompactification}\\
&\lor G_{selected\ tube\ label\ thinning/turnover}\\
&\lor G_{flux/amplitude\ loss}\\
&\lor G_{normal\ chart/topology\ loss}\\
&\lor G_{jet\text{-}scale/record\text{-}scale\ mismatch}\\
&\lor G_{parent\text{-}to\text{-}record\ genealogy/domain\ loss}.
\end{aligned}
}
\]

The old idea that a positive-volume fixed tube might itself remain compact around a shrinking physical loop is removed.

## 13. Next target

The highest-value remaining tube question is now **material-label thinning/turnover**.

If positive retained flux at every record can be carried only by ever-changing or ever-thinner material-label bands, quantify the label-measure turnover and determine whether M17-358 additivity, M17-389 flux evolution, or the raw-H2/palinstrophy ledgers force a nonsummable cost.

This is the target of M17-425.

## 14. DSD audit

The DSD role is only to separate three measures that must not be conflated:

- material particle volume;
- vortex flux measure;
- proof-selected active tube-label measure.

The theorem itself is ordinary incompressible flow-map Jacobian calculus plus exact similarity scaling.

## 15. Audit verdict

**PASS — fixed positive-volume material-tube similarity compactness is impossible.**

This is a forced spatial-decompactification theorem, not a global Navier--Stokes contradiction. It converts a vague tube-shape exit into a precise material-volume/selection dichotomy.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
