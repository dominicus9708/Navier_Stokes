# Vorticity-direction / strain-axis bridge

Date: 2026-08-12

Status: **DERIVED IDENTITY + BRIDGE DESIGN + EXTERNAL REGULARITY ANCHOR + OPEN PROOF OBLIGATION**.

## 1. Motivation

The scalar stretching channel

\[
\sigma=\omega^TS\omega,
\qquad
S=\frac12(\nabla u+\nabla u^T),
\]

mixes at least three different pieces of information:

1. vorticity magnitude;
2. strain eigenvalues;
3. alignment of the vorticity direction with the strain eigenframe.

DSD should keep these typed separately before aggregation.

## 2. General pointwise decomposition

At a point where

\[
|\omega|>0,
\]

define

\[
\xi=\frac{\omega}{|\omega|}.
\]

Because `S` is real symmetric, choose an orthonormal eigenframe

\[
Se_i=\lambda_i e_i,
\qquad i=1,2,3.
\]

Incompressibility gives

\[
\lambda_1+\lambda_2+\lambda_3=\operatorname{tr}S=0.
\]

Define alignment weights

\[
a_i=(\xi\cdot e_i)^2,
\qquad
\sum_i a_i=1.
\]

Then exactly

\[
\gamma:=\xi^TS\xi
=\sum_i\lambda_i a_i,
\]

and

\[
\boxed{\sigma=|\omega|^2\gamma}.
\]

This is not a new Navier–Stokes theorem; it is the spectral decomposition of the vortex-stretching term.

## 3. DSD layer interpretation

### Formation layer

The direction channel `xi` and all alignment channels `a_i` are applicable only where `|omega|>0`.

At a zero-vorticity point, `xi` is **undefined/inapplicable**, not a zero vector.

### Axis-property layer

The strain eigenvectors `e_i` and vorticity direction `xi` are local directions inside the same realized 3D spatial span. They do not create extra spatial dimensions.

The strain matrix is a property/coupling block attached to the three realized axes.

### Static Aggregation layer

Do not aggregate only `sigma`. Retain, at minimum,

\[
\bigl(|\omega|^2,\lambda_1,\lambda_2,\lambda_3,a_1,a_2,a_3,\gamma\bigr)
\]

where defined.

### Structural Reorganization Dynamics layer

`gamma>0` indicates instantaneous stretching of the vorticity magnitude along its current direction; `gamma<0` indicates compression in that directional quadratic form. These are descriptive channel labels, not independent forces.

## 4. Exact Gaussian benchmark simplification

For the current `z`-axis Gaussian double-curl benchmark,

\[
\omega
=4(2|x|^2-5)e^{-|x|^2}(y,-x,0).
\]

Thus away from the vorticity-zero set the vorticity direction lies on the local azimuthal line around the `z` axis.

Moreover,

\[
|\omega|^2
=16(x^2+y^2)(2|x|^2-5)^2e^{-2|x|^2},
\]

and the previously derived stretching density is

\[
\sigma
=64z(x^2+y^2)(2|x|^2-5)^2e^{-3|x|^2}.
\]

Therefore, wherever `|omega|>0`,

\[
\boxed{
\gamma=\frac{\sigma}{|\omega|^2}
=4ze^{-|x|^2}.
}
\]

The sign split is immediately visible:

\[
z>0\Rightarrow\gamma>0,
\qquad
z<0\Rightarrow\gamma<0,
\qquad
z=0\Rightarrow\gamma=0
\]

at points where the direction channel is applicable.

## 5. Removable formula versus defined state

The benchmark vorticity vanishes on

\[
x^2+y^2=0
\]

and also on

\[
|x|^2=\frac52.
\]

On these sets,

\[
\xi=\frac{\omega}{|\omega|}
\]

and

\[
\gamma=\frac{\sigma}{|\omega|^2}
\]

are not defined as vorticity-direction quantities.

The simplified expression

\[
4ze^{-|x|^2}
\]

can have a perfectly finite value on parts of those sets. DSD typing therefore distinguishes:

- the **algebraically/continuously extendable expression**, and
- the **actually applicable vorticity-direction channel**.

The latter remains undefined when `|omega|=0` unless a separate extension object is explicitly introduced and given a different type.

This is another direct application of the DSD distinction between undefined and defined zero/nonzero values.

## 6. External geometric regularity anchor

Constantin and Fefferman initiated a classical line of 3D Navier–Stokes regularity results based on geometric control of the vorticity direction rather than only its magnitude. Their 1993 paper is *Direction of Vorticity and the Problem of Global Regularity for the Navier-Stokes Equations*, Indiana University Mathematics Journal 42, 775–789.

Later work has refined and relaxed vorticity-direction coherence criteria. Therefore the idea that vorticity direction can matter for regularity is **external established mathematics**, not a novelty claim of DSD.

The DSD-specific role here is narrower: provide a typed representation that simultaneously retains magnitude, local realized directions, strain eigenvalues, alignment weights, zero-vorticity applicability, scale localization, and aggregation collisions.

## 7. Next proof target

The useful question is no longer whether direction matters; that is already represented in established geometric regularity theory.

The DSD-assisted target is whether the combined channel system can produce an a-priori estimate of a form such as

\[
\int_0^T\int_{\mathbb R^3}
|\omega|^2\,\gamma_+\,dxdt
\]

or a scale-local/angular-coherence analogue, using only quantities that are already controlled or can be closed without circularly assuming regularity.

Here

\[
\gamma_+=\max(\gamma,0).
\]

This is **OPEN PROOF OBLIGATION**.

## 8. Immediate computational program

`src/vorticity_alignment_baseline.py` verifies for deterministic benchmark points:

- the exact factorization `sigma=|omega|^2 gamma`;
- `gamma=xi^T S xi=sum_i lambda_i a_i`;
- `sum_i a_i=1`;
- positive, negative, and zero directional-stretch samples;
- undefined alignment status on both components of the benchmark vorticity-zero set;
- `tr S=0` in the sampled eigenframes.

The next generalization should replace one analytic seed by translated, rotated, and superposed seeds and measure how the alignment channels change under the nonlinear cross couplings already identified in the pressure source.

## Reference

Peter Constantin and Charles Fefferman, *Direction of Vorticity and the Problem of Global Regularity for the Navier-Stokes Equations*, Indiana Univ. Math. J. 42 (1993), 775–789, DOI `10.1512/iumj.1993.42.42034`.
