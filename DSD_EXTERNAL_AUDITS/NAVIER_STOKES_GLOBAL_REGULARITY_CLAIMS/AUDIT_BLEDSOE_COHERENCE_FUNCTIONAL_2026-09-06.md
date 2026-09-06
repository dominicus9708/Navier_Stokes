# DSD Audit — Bledsoe Coherence Functional

Date: 2026-09-06
Source family: Brad Bledsoe, *A Constructive Framework for Global Regularity in the 3D Navier–Stokes Equations*, SSRN 5575415 / 6393402.
Audit status: **ABSTRACTED CORE INEQUALITY FAILS AMPLITUDE HOMOGENEITY AS STATED**

## 1. Claimed hinge

The abstract states that a scale-invariant angular coherence functional enforces a universal discount `δ>0` on vortex stretching, yielding

\[
\boxed{
\int_{\mathbb R^3} ((\omega\cdot\nabla u)\cdot\omega)|\omega|\,dx
\le (1-\delta)\|\omega\|_{L^3}^3.
}
\]

This inequality is presented as the decisive mechanism closing the critical L3 bootstrap for arbitrary smooth divergence-free H1 initial data.

## 2. Amplitude audit at initial time

The global theorem is claimed for arbitrary smooth divergence-free initial data. Therefore, if `u_0` is admissible, so is

\[
u_0^{(A)}:=A u_0
\]

for every finite `A>0`.

At the initial instant,

\[
\omega^{(A)}=A\omega,
\qquad
\nabla u^{(A)}=A\nabla u.
\]

Hence the displayed stretching integral scales as

\[
A^4
\int ((\omega\cdot\nabla u)\cdot\omega)|\omega|\,dx.
\]

The right side scales as

\[
(1-\delta)A^3\|\omega\|_3^3.
\]

For any datum for which the signed/positive stretching integral is nonzero in the relevant orientation, the estimate would require

\[
A\,C(u_0)\le (1-\delta)\|\omega_0\|_3^3
\]

for arbitrarily large `A`, impossible for one data-independent `δ` and one unscaled right-hand side.

Thus the displayed inequality has incompatible amplitude degree `4` versus `3`.

## 3. What could repair the dimensional mismatch

A corrected inequality might contain an additional quantity of velocity-gradient dimension, for example a norm/scale factor, or might normalize the stretching term by an amplitude-dependent denominator. But that would be a different estimate and must be stated and proved explicitly.

A purely angular functional is dimensionless and cannot alone repair one missing power of amplitude.

## 4. Geometry-persistence issue is downstream

The manuscript also claims that angular diffusion, geometric depletion, and heat-kernel localization produce a uniform positive misalignment floor before the discount is used. That is a separate deep gate. The present audit does not need to decide it because the displayed universal stretching estimate already fails homogeneity as written.

If the full manuscript contains a differently normalized theorem than the abstract, that exact theorem should supersede this audit and be rechecked. Until then, the public central formula cannot be the claimed universal closure inequality.

## 5. Surviving value

The following ideas remain potentially useful:

- a quantitative vorticity-direction coherence functional;
- propagation of angular misalignment;
- conditional regularity under a proven coherence floor;
- comparison with Constantin–Fefferman-type geometric depletion criteria.

## 6. DSD verdict

\[
\boxed{
\text{The public decisive discount inequality has amplitude degree }4\text{ on the left and }3\text{ on the right.}
}
\]

Therefore it cannot hold for arbitrary-amplitude smooth initial data with a universal data-independent discount in the stated form.

Global regularity remains unproved.
