# Source-active Betchov dichotomy without an alignment hypothesis

Date: 2026-08-18

Status: **POINTWISE ALGEBRAIC SHARPENING OF THE LOCAL BETCHOV ROUTE. POSITIVE VORTEX STRETCHING REQUIRES EITHER POSITIVE MIDDLE STRAIN OR A STRICTLY POSITIVE BETCHOV MISMATCH, WITHOUT ASSUMING VORTICITY ALIGNMENT WITH A STRAIN EIGENVECTOR. GLOBAL REGULARITY NOT PROVED.**

## 1. Setup

Let the ordered eigenvalues of the symmetric trace-free strain be

\[
\lambda_1\ge\lambda_2\ge\lambda_3,
\qquad
\lambda_1+\lambda_2+\lambda_3=0.
\]

Let

\[
q(x,t)=\omega\cdot S\omega.
\]

The exact local Betchov divergence identity used in the repository is

\[
\boxed{
q+4\det S
=\frac43\nabla\cdot\mathcal F_A.
}
\]

## 2. Positive stretching point

Suppose

\[
q>0.
\]

There are only two eigenvalue cases.

### Case A: `lambda_2>0`

Then the point belongs directly to the positive-middle-strain branch.

### Case B: `lambda_2<=0`

Because `q>0`, the strain has a positive direction and hence `lambda_1>0`.  Trace-free ordering then gives `lambda_3<0`. Therefore

\[
\det S
=\lambda_1\lambda_2\lambda_3
\ge0.
\]

Consequently

\[
\boxed{
q+4\det S
\ge q>0.
}
\]

No assumption that `omega` is an eigenvector of `S` is used.

## 3. Pointwise source-active dichotomy

Every point with positive vortex stretching satisfies

\[
\boxed{
q>0
\Longrightarrow
\left[
\lambda_2^+>0
\right]
\quad\lor\quad
\left[
q+4\det S\ge q>0
\right].
}
\]

Thus arbitrary strain/vorticity misalignment does not create a third source-active lane.

## 4. Buffered cell consequence

Consider a natural-scale buffered cell in which a fixed core portion has

\[
q\ge q_0>0.
\]

If a fixed portion of that production occurs where `lambda_2>0`, the cell pays positive-middle-strain action.

Otherwise a fixed core portion satisfies `lambda_2<=0`, and hence carries strictly positive Betchov mismatch.  Applying the local cutoff Betchov identity routes this mismatch to the already derived alternatives

\[
\boxed{
\text{buffer strain-energy reservoir}
\quad\lor\quad
\text{buffer Hessian/palinstrophy}
\quad\lor\quad
\text{cubic residual-shape breakdown}.
}
\]

The local constant-shift/Poincare version prevents a remote whole-space enstrophy reservoir from paying this cost artificially.

## 5. Many-cell consequence

For a bounded-overlap family of separated source-active unit cells, the local buffer estimates may be summed without counting one shell arbitrarily many times.  Therefore a family of `N` cells cannot all use the `lambda_2<=0` route without producing a correspondingly large collection of local buffer/derivative costs.

If the cells merge into a dense connected cluster, summing the positive core mismatch before applying a single outer cutoff converts the problem into a bulk-to-boundary Betchov compensation problem at the cluster scale.

Hence the remaining same-scale high--high network has the structural alternatives

\[
\boxed{
\text{positive-middle-strain population}
}
\]

or

\[
\boxed{
\text{local/cluster Betchov compensation}
}
\]

or the previously typed residual/derivative/kernel-deformation channels.

## 6. Relation to the critical phase-space ridge

For `N` natural physical packets at frequency `K`, a source-active positive-middle-strain population of order `N` has the scale-critical size

\[
\int_{\text{one natural block}}
\|\lambda_2^+\|_3^2dt
\gtrsim
cN^{2/3}
\]

when the cells have bounded overlap and order-one normalized production.

The terminal kinetic-energy dissipation price remains

\[
D_{\rm kin}\gtrsim c\frac{N}{K}.
\]

Their product has the same phase-space exponent previously found from the I-lane occupancy--strain calculation:

\[
\boxed{
D_{\rm kin}\,
\mathcal S_{\lambda_2}
\gtrsim
c\frac{N^{5/3}}{K}.
}
\]

Thus the `N~K^(3/5)` ridge is reproduced without an axial-alignment assumption.

This still does not constitute a contradiction: a hypothetical singular solution is allowed to have divergent critical middle-strain action.  The value of the result is structural—misalignment no longer supplies an untyped local escape.

Status: **ALIGNMENT HYPOTHESIS REMOVED FROM THE SOURCE-ACTIVE BETCHOV SPLIT / SAME-SCALE NETWORK STILL REDUCES TO CRITICAL MIDDLE STRAIN, LOCAL BETCHOV COMPENSATION, OR DERIVATIVE/RESIDUAL REORGANIZATION.**