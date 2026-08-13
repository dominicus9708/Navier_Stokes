# Adaptive `log q` action routing into middle-strain or extensional-alignment channels

Date: 2026-08-13

Status: **DERIVED CHECKPOINT ACTION ROUTING USING EXISTING MAXIMUM-VORTICITY IDENTITY / NO NEW EXTERNAL REGULARITY THEOREM**.

The bounded-affine Riccati analysis identifies a long adaptive step as BKM-critical.  The maximum-vorticity direction/strain identity further resolves the required logarithmic growth action into two geometric channels already present in the repository.

---

## 1. Maximum-vorticity growth rate

Let

\[
W(t)=\|\omega(t)\|_\infty,
\qquad
\rho=|\omega|,
\qquad
\xi=\omega/|\omega|.
\]

Where `omega != 0`,

\[
(\partial_t+u\cdot\nabla-\nu\Delta)\rho
=
\rho
\left(
\xi^TS\xi-
u|\nabla\xi|^2
\right).
\]

Define the maximum-vorticity growth channel

\[
\mathcal G(t)
=
\sup_{x:\,|\omega(x,t)|=W(t)}
\left(
\xi^TS\xi-
u|\nabla\xi|^2
\right)_+.
\]

The upper Dini derivative satisfies

\[
\boxed{
D^+\log W(t)
\le\mathcal G(t)
}
\]

on the smooth lifespan.

---

## 2. First-hitting amplification forces logarithmic geometric action

On an adaptive checkpoint step

\[
W(T)=qW(t_-),
\qquad q>1,
\]

integrating the Dini inequality gives

\[
\boxed{
\log q
\le
\int_{t_-}^{T}\mathcal G(t)dt.
}
\]

This statement is scale invariant.

---

## 3. Existing eigenframe decomposition

Let

\[
\lambda_1\le\lambda_2\le\lambda_3
\]

be the strain eigenvalues and let

\[
a_i^2=(\xi\cdot e_i)^2.
\]

The repository's middle-eigenvalue residual decomposition gives

\[
\mathcal G(t)
\le
\Lambda_{2,M}(t)+\mathcal E_3(t),
\]

where

\[
\Lambda_{2,M}(t)
=
\sup_{x:\,|\omega|=W(t)}\lambda_2^+(x,t),
\]

and

\[
\mathcal E_3(t)
=
\sup_{x:\,|\omega|=W(t)}
\left(
\lambda_3a_3^2
-
u|\nabla\xi|^2
\right)_+.
\]

Thus

\[
\boxed{
\log q
\le
\int_{t_-}^{T}\Lambda_{2,M}(t)dt
+
\int_{t_-}^{T}\mathcal E_3(t)dt.
}
\]

Consequently at least one of

\[
\boxed{
\int_{t_-}^{T}\Lambda_{2,M}(t)dt
\ge\frac12\log q
}
\]

or

\[
\boxed{
\int_{t_-}^{T}\mathcal E_3(t)dt
\ge\frac12\log q
}
\]

must hold.

---

## 4. Meaning of the two lanes

### M-lane: co-located positive middle strain

A logarithmic amount of positive middle-eigenvalue action reaches the maximum-vorticity set itself.

This is stronger than knowing only that the global norm

\[
\|\lambda_2^+\|_\infty
\]

is large somewhere.  The strain action is spatially co-located with the dangerous vorticity.

This lane returns to

- middle-eigenvalue regularity criteria;
- occupancy/thickness of the maximum-vorticity core;
- affine biaxial extension geometry;
- pressure-Hessian/eigenframe maintenance.

### E-lane: top-extensional alignment beats direction diffusion

The quantity

\[
\lambda_3a_3^2
\]

must repeatedly exceed the exact direction-diffusion penalty

\[
\nu|\nabla\xi|^2.
\]

Thus the vorticity must remain sufficiently aligned with the strongest extensional eigenaxis while avoiding excessive directional roughness.

This lane returns to

- vorticity/strain-axis covariance;
- projective coherence;
- direction-gradient depletion;
- extensional-axis rotation;
- off-axis generation.

---

## 5. Combine with the bounded-affine Riccati barrier

On a bounded self-consistent affine/Gaussian branch, a large adaptive step already requires

\[
\sigma\gtrsim q.
\]

The present lemma adds

\[
\boxed{
\text{same step}
\Longrightarrow
\text{at least }\frac12\log q
\text{ of M-lane or E-lane action}.
}
\]

Hence the surviving long-step route is not an undifferentiated long evolution.  It must repeatedly maintain a geometrically specific vorticity-stretching mechanism.

---

## 6. Relation to external criteria

The repository separately records Evan Miller's middle-eigenvalue criterion: a finite-time singularity requires divergence of a scale-critical integral involving `lambda_2^+`, including the `L_t^1 L_x^infinity` endpoint.

The present statement does not re-prove or strengthen that external theorem.  It only routes the checkpoint-by-checkpoint maximum-vorticity growth into a co-located middle-strain channel or a top-extensional alignment channel.

---

## 7. DSD interpretation

The scalar amplitude transition

\[
W_-\to qW_-
\]

is not retained as one undifferentiated growth number.  Its logarithmic action is assigned to a finite structural channel set:

\[
\boxed{
\log q
\longrightarrow
\text{middle-strain action}
\oplus
\text{extensional-alignment action}.
}
\]

This is a dynamic channel decomposition of the BKM-critical action.

---

## 8. Limitation

Both lane actions can in principle diverge along a hypothetical singular route.  No finite global budget for either lane has been proved here.

The next target is a strict depletion statement showing that one cannot accumulate `log q` in these channels while simultaneously remaining inside the non-affine mesoscopic window and avoiding the existing projective/sparseness/pressure/derivative gates.

Status: **LONG-STEP BKM ACTION TYPED INTO TWO GEOMETRIC LANES / STRICT GEOMETRIC DEPLETION REMAINS OPEN**.
