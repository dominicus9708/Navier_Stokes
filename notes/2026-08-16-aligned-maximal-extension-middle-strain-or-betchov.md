# Aligned maximal extension -> positive-middle strain or Betchov exterior compensation

Date: 2026-08-16

Status: **EXACT LOCAL EIGENVALUE DICHOTOMY FOR THE CRITICAL AFFINE FIXED-POINT SHAPE. ONCE THE COHERENT VORTICITY DIRECTION IS ALIGNED WITH A MAXIMALLY EXTENSIONAL STRAIN DIRECTION, EVERY TRACE-FREE STRAIN SHAPE IS EITHER DIRECTLY POSITIVE-MIDDLE-STRAIN PRODUCTIVE OR HAS A STRICTLY POSITIVE LOCAL BETCHOV MISMATCH THAT REQUIRES EXTERIOR/BOUNDARY COMPENSATION. GLOBAL REGULARITY NOT PROVED.**

## 1. Setup

Let `S` be a real symmetric trace-free `3x3` strain matrix with ordered eigenvalues

\[
\lambda_1\ge\lambda_2\ge\lambda_3,
\qquad
\lambda_1+\lambda_2+\lambda_3=0.
\]

Assume the coherent vorticity direction is aligned with the maximally extensional eigenvector `e1`:

\[
\boxed{
\omega=\Omega e_1,
\qquad
S e_1=\lambda_1e_1,
\qquad
\lambda_1>0.
}
\]

The local Betchov mismatch density is

\[
\boxed{
\mathcal D_B
:=
\omega\cdot S\omega+4\det S.
}
\]

In the aligned state,

\[
\boxed{
\mathcal D_B
=\lambda_1\Omega^2
+4\lambda_1\lambda_2\lambda_3.
}
\]

## 2. Case A: positive middle eigenvalue

If

\[
\boxed{\lambda_2>0,}
\]

then the state is already in the positive-middle-strain branch.

In particular the productive density used in the global enstrophy-growth ledger,

\[
\lambda_2^+|S|^2,
\]

is strictly positive wherever the aligned state is nontrivial.

No Betchov argument is needed to type this case:

\[
\boxed{
\lambda_2>0
\Longrightarrow
\text{direct positive-middle-strain production}.
}
\]

## 3. Case B: nonpositive middle eigenvalue

Suppose

\[
\boxed{\lambda_2\le0.}
\]

Since `lambda1>0` and the trace vanishes,

\[
\lambda_3=-\lambda_1-\lambda_2<0.
\]

Therefore

\[
\lambda_2\lambda_3\ge0
\]

and hence

\[
\boxed{\det S=\lambda_1\lambda_2\lambda_3\ge0.}
\]

Thus

\[
\boxed{
\mathcal D_B
\ge
\lambda_1\Omega^2>0
}
\]

whenever `Omega != 0`.

The exact local Betchov divergence identity

\[
\omega\cdot S\omega+4\det S
=\frac43\nabla\cdot\mathcal F_A
\]

then implies that the aligned core cannot be a closed internal state. Its positive mismatch must be balanced by boundary/exterior flux or by breakdown of the assumed aligned coherent shape.

Hence

\[
\boxed{
\lambda_2\le0
\Longrightarrow
\text{strict local Betchov mismatch}
\Longrightarrow
\text{exterior/boundary compensation or shape defect}.
}
\]

## 4. Complete aligned-shape dichotomy

Combining the two cases,

\[
\boxed{
\begin{gathered}
\omega\parallel e_1,\quad
\lambda_1>0
\end{gathered}
\Longrightarrow
\begin{cases}
\lambda_2^+>0,
&\text{productive middle strain},\\
\mathcal D_B>0,
&\text{Betchov exterior compensation}.
\end{cases}
}
\]

There is no third trace-free eigenvalue geometry.

This generalizes the earlier exactly axial shape

\[
(-a/2,-a/2,a)
\]

to arbitrary transverse eigenvalue ratios.

## 5. Stability under near alignment

Suppose

\[
\omega=\Omega e_1+\eta
\]

and `S` differs from an aligned eigenframe by a small shape/orientation error.

Because both

\[
\omega\cdot S\omega
\]

and

\[
\det S
\]

are continuous polynomial functions of the state variables, the dichotomy is stable away from the neutral transition `lambda2=0`:

- if `lambda2>=delta |S|` for a fixed `delta>0`, a definite positive-middle-strain density remains;
- if `lambda2<=-delta |S|`, the Betchov mismatch remains definitely positive when the coherent vorticity component is bounded below;
- if `|lambda2|<<|S|`, the shape is close to the uniaxial transition surface and may be treated as the axial-extension/Betchov branch plus an explicitly small shape error.

Thus small projective/coherence errors do not generate a qualitatively new escape.

## 6. Connection to affine-diffusion saturation

The critical `R^-2` residual-seed model forces

\[
q\sim R^2
\]

actual vorticity amplification and, near deformation--diffusion saturation, a hyperbolic `O(R)` affine ramp.

To realize the endpoint coherent vorticity with minimal source mass, the amplified source direction must be approximately aligned with a strong extensional direction of the affine transition. If the instantaneous strain maintains this alignment through the active ramp, the present eigenvalue dichotomy applies.

Therefore the critical affine-residual fixed point cannot hide in a special transverse eigenvalue ratio:

\[
\boxed{
\text{critical aligned affine ramp}
\Longrightarrow
\text{positive-middle strain}
\lor
\text{Betchov exterior compensation}.
}
\]

If the alignment itself fails rapidly, that is the complementary orientation/time-modulation/projective branch.

## 7. Remaining wall

The positive-middle-strain branch is necessary for global enstrophy growth but can diverge at a hypothetical singularity; its recurrence is not yet forbidden.

The Betchov-compensation branch has a local flux/palinstrophy estimate, but its exterior compensation may migrate to smaller/farther scales and can in principle have summable physical costs.

Thus the remaining theorem is no longer an affine-shape classification problem. It is a **scale-orthogonal exterior-compensation/nonrepeatability theorem** for the critical fixed-point sequence.

Status: **ALL ALIGNED MAXIMAL-EXTENSION STRAIN SHAPES TYPED / NO TRANSVERSE-EIGENVALUE ESCAPE REMAINS / FINAL OBSTRUCTION = REPEATED POSITIVE-MIDDLE-STRAIN OR BETCHOV EXTERIOR COMPENSATION ACROSS SHRINKING SCALES.**
