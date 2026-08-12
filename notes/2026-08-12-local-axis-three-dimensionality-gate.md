# Local-axis / fully-three-dimensional vorticity gate

Date: 2026-08-12

Status: **EXTERNAL REGULARITY ANCHOR + DSD AXIS-PROPERTY BRIDGE / OPEN LOCAL-PLANE APPROXIMATION ESTIMATE**.

This note integrates Evan Miller's locally anisotropic vorticity criterion into the DSD residual-class map.

## 1. External theorem

Let `n(x,t)` be a unit vector field,

\[
|n(x,t)|=1,
\]

with spatial gradient locally bounded in time,

\[
\nabla n
\in
L^\infty_{\rm loc}
([0,\infty);L^\infty(\mathbb R^3)).
\]

Miller's locally anisotropic criterion gives an `Hdot^1` bound involving

\[
\int_0^t
\|n(\cdot,\tau)\times\omega(\cdot,\tau)\|_2^4d\tau.
\]

Consequently, if a mild solution blows up at finite `T*`, then for every such admissible local direction field used in the theorem,

\[
\boxed{
\int_0^{T^*}
\|n\times\omega\|_2^4dt
=\infty.
}
\]

External source:

- Evan Miller, *A locally anisotropic regularity criterion for the Navier--Stokes equation in terms of vorticity*, arXiv:2002.02152 / Proc. AMS Series B 8 (2021).

## 2. Axis interpretation

For any unit `n`,

\[
\boxed{
|n\times\omega|^2
=|\omega|^2-(n\cdot\omega)^2
=|\omega|^2\sin^2\theta.
}
\]

Thus `n x omega` is the component of vorticity lying in the plane orthogonal to `n`.

If the flow is locally close to a two-dimensional flow whose vorticity is aligned with `n`, this defect is small.

The external theorem therefore says that a finite-time blowup cannot remain sufficiently close, in the scale-critical sense of the theorem, to **any spatially smooth moving local plane structure**.

This is the precise meaning of the statement that a residual blowup must be locally fully three dimensional.

## 3. DSD axis-property channel

This does not change the realized spatial rank:

\[
\operatorname{rank}_{\rm space}=3.
\]

Instead define a local axis property

\[
\boxed{
\mathcal T[n](t)
=\|n\times\omega\|_2^2.
}
\]

For a local observation region `B`, one may also use

\[
\mathcal T_B[n]
=
\int_B|n\times\omega|^2dx.
\]

The geometric identity

\[
\mathcal T_B[n]
=
\int_B|\omega|^2\sin^2\theta_n dx
\]

shows that this is an enstrophy-weighted directional misalignment channel.

## 4. Smooth-plane approximation family

For a gradient cap `K>0`, define schematically the admissible family

\[
\mathscr N_K
=
\{n:|n|=1,\ \|\nabla n\|_\infty\le K\}.
\]

A descriptive local planarity defect is

\[
\boxed{
\Pi_K(B,t)
=
\inf_{n\in\mathscr N_K}
\frac{
\int_B|n\times\omega|^2dx
}{
\int_B|\omega|^2dx
}
}
\]

when the denominator is nonzero.

`Pi_K` belongs to the DSD static aggregation layer.  It is **not** itself Miller's theorem, because the theorem is global in space/time and requires a single admissible direction field in the functional class stated there.

The purpose of `Pi_K` is to quantify how well a local vorticity structure can be represented by a smoothly varying plane normal.

## 5. Exact connection to the vorticity direction

Where `omega != 0`, let

\[
\xi=\omega/|\omega|.
\]

Then

\[
|n\times\omega|
=|\omega||n\times\xi|.
\]

If one could take

\[
n=\xi
\]

and `grad xi` were bounded in the theorem's class, then

\[
n\times\omega=0.
\]

This recovers the geometric message that sufficiently regular vorticity direction prevents blowup.

The reason a residual flow can evade this trivial choice is precisely that the direction field may fail the required spatial regularity.

## 6. Smooth approximation versus misalignment tradeoff

The residual direction problem can be reframed as an approximation tradeoff.

- A smoother `n` lowers `||grad n||_infinity` but may increase `|n x xi|`.
- Taking `n` closer to the raw direction `xi` lowers the misalignment but may make `||grad n||_infinity` large.

Thus the relevant DSD pair is

\[
\boxed{
\left(
\|\nabla n\|_\infty,
\|n\times\omega\|_2
\right).
}
\]

This is a mathematically grounded version of a **local directional describability cost**: a rapidly changing direction field is hard to represent by a smooth local axis without leaving a large three-dimensional residual component.

## 7. Residual blowup requirement

A hypothetical singularity must evade this gate for every useful smooth local-axis choice.

In qualitative terms, it must produce either

1. a large cross-plane vorticity defect `n x omega` for every sufficiently smooth local axis field, or
2. require the axis field to rotate/warp so rapidly that its spatial gradient leaves the admissible regularity class.

This complements the log-BMO branch:

- relatively smooth direction -> locally anisotropic / direction-coherence gates;
- log-BMO-level roughness within the 2026 critical-point preprint scope -> logarithmic depletion gate;
- still rougher direction -> large direction-gradient / segregation / higher-derivative channels.

## 8. Temporal intermittency consequence

The energy inequality gives

\[
\int_0^{T^*}\|\omega(t)\|_2^2dt<\infty
\]

on the smooth lifespan (equivalently the finite kinetic-energy dissipation).

Since

\[
\|n\times\omega\|_2^2
\le
\|\omega\|_2^2,
\]

we also have

\[
\int_0^{T^*}\|n\times\omega\|_2^2dt<\infty.
\]

But a blowup requires, by the external theorem,

\[
\int_0^{T^*}\|n\times\omega\|_2^4dt=\infty.
\]

Hence the local-three-dimensionality defect must be **temporally intermittent**: its square is integrable while its fourth-power time integral diverges.

This is another residual-class restriction, not a contradiction.

## 9. Next bridge target

The natural next question is whether the moving-sphere spatial occupancy channels can construct an admissible smooth axis field `n` for which

\[
\int_0^{T^*}\|n\times\omega\|_2^4dt<\infty.
\]

A positive result would exclude the fully-three-dimensional residual branch.

The obstacle is topological/spatial: local best-fit directions on neighboring moving spheres must be patched into a global/spatially Lipschitz unit field without creating excessive gradient.

This is now an **axis-field gluing problem**.

Status: **OPEN SMOOTH AXIS-FIELD GLUING ESTIMATE**.
