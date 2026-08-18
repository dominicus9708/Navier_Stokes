# High-derivative saturation ratio: H cannot diverge independently of lower strain

Date: 2026-08-19

Status: **DERIVED INTERPOLATION REDUCTION + EXTERNAL REGULARITY ANCHOR / GLOBAL REGULARITY NOT PROVED**.

This note sharpens the `H` branch using Evan Miller's 2024 strain--vorticity interaction regularity criterion.

External anchor:

E. Miller, *On the interaction of strain and vorticity for solutions of the Navier--Stokes equation*, arXiv:2407.02691, especially Theorem 1.9.

For unit viscosity, finite-time blowup requires

\[
\limsup_{t\to T_*}
\frac{
\left\|P_{st}\left((u\cdot\nabla)S+S^2+\frac34\omega\otimes\omega\right)\right\|_2
}{
\| -\Delta S\|_2
}
\ge1.
\]

Thus large higher derivatives alone are not a blowup mechanism; the retained nonlinearity must remain comparable to the second-strain-derivative scale.

---

## 1. Define the saturation ratio

Let

\[
A=\|S\|_2,
\qquad
B=\|\Delta S\|_2,
\qquad
K=\|u\|_2.
\]

Define

\[
\boxed{
\mathfrak R_H
=
\frac{
\left\|P_{st}\left((u\cdot\nabla)S+S^2+\frac34\omega\otimes\omega\right)\right\|_2
}{B}.
}
\]

The strain projection is an `L2` contraction, so it is enough to estimate the unprojected terms.

---

## 2. Advection estimate

By Holder,

\[
\|(u\cdot\nabla)S\|_2
\le
\|u\|_\infty\|\nabla S\|_2.
\]

The three-dimensional Gagliardo--Nirenberg estimate and the Fourier equivalence of `nabla^2 u` with `nabla S` give

\[
\|u\|_\infty
\lesssim
K^{1/4}\|\nabla S\|_2^{3/4}.
\]

Also

\[
\|\nabla S\|_2
\le
A^{1/2}B^{1/2}.
\]

Therefore

\[
\boxed{
\|(u\cdot\nabla)S\|_2
\lesssim
K^{1/4}A^{7/8}B^{7/8}.
}
\]

After division by `B`,

\[
\boxed{
\frac{\|(u\cdot\nabla)S\|_2}{B}
\lesssim
K^{1/4}A^{7/8}B^{-1/8}.
}
\]

Thus, at fixed kinetic energy and fixed strain `L2` size, advection becomes perturbative relative to `-Delta S` if the second derivative is sent arbitrarily high.

---

## 3. Quadratic strain/vorticity estimate

Using

\[
\|S^2\|_2\le\|S\|_4^2
\]

and interpolation between `L2` and `H2`,

\[
\|S\|_4
\lesssim
A^{5/8}B^{3/8}.
\]

Hence

\[
\boxed{
\|S^2\|_2
\lesssim
A^{5/4}B^{3/4}.
}
\]

Since strain and vorticity are related by order-zero Fourier multipliers, the same estimate holds schematically for `omega tensor omega`:

\[
\boxed{
\|\omega\otimes\omega\|_2
\lesssim
A^{5/4}B^{3/4}.
}
\]

Therefore

\[
\boxed{
\frac{
\|S^2\|_2+\|\omega\otimes\omega\|_2
}{B}
\lesssim
A^{5/4}B^{-1/4}.
}
\]

---

## 4. Total H-ratio bound

Combining the estimates,

\[
\boxed{
\mathfrak R_H
\lesssim
K^{1/4}A^{7/8}B^{-1/8}
+
A^{5/4}B^{-1/4}.
}
\]

Consequently, if the blowup-required saturation `mathfrak R_H >= c0` holds along a sequence, then at least one term on the right is non-negligible. Hence

\[
\boxed{
B
\lesssim_{c_0}
K^2A^7+A^5.
}
\]

Because kinetic energy `K` is globally bounded for the physical Navier--Stokes solution, an admissible `H` blowup sequence cannot send `||Delta S||_2` to infinity arbitrarily faster than a fixed algebraic power of `||S||_2`.

Equivalently,

\[
\boxed{
B\gg K^2A^7+A^5
\Longrightarrow
\mathfrak R_H\ll1,
}
\]

which is incompatible with the Miller 2024 blowup saturation criterion if this perturbative regime persists toward the endpoint.

---

## 5. Interpretation for the DSD branch tree

The `H` branch should therefore no longer mean merely

\[
\text{palinstrophy or higher derivative becomes large}.
\]

The dangerous branch is the stricter condition

\[
\boxed{
\text{higher derivative growth}
+\text{nonlinear saturation at the same derivative scale}.
}
\]

This is a derivative-order analogue of the `M` saturation problem.

The late-frontier target can therefore be rewritten as a competition between two saturation ratios:

1. `M`: positive-middle-strain production remains critically efficient;
2. `H`: derivative nonlinearity remains comparable to viscous second-strain differentiation.

Transport `T` supplies the mechanism by which either ratio can be fed from adjacent physical scales.

---

## 6. External-anchor correction

The repository previously treated higher-derivative sparseness / asymptotic criticality as a strong external gate. This must be stated conservatively.

Grujic--Xu (arXiv:1911.00974) developed the higher-derivative sparseness framework and interpreted the regularity/a-priori sparseness scales as asymptotically critical.

Albritton--Bradshaw, *Remarks on sparseness and regularity of Navier-Stokes solutions*, arXiv:2110.02187, gave a different interpretation and argued that, in a reasonable homogeneity sense and in concrete blowup scenarios, the claimed scaling-gap improvement need not go beyond what is already supplied by the energy class.

Therefore this project will retain higher-derivative sparseness as a useful conditional regularity diagnostic, but **not** as an assumed near-closure of the Millennium problem.

Status: **H REFINED TO A NONLINEAR/SECOND-DERIVATIVE SATURATION RATIO; ARBITRARILY FAST DERIVATIVE-ONLY ESCAPE EXCLUDED CONDITIONALLY; CRITICAL H SATURATION REMAINS OPEN**.
