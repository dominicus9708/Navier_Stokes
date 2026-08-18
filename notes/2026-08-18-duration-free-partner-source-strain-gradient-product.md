# Duration-free critical product for a bounded-geometry same-scale partner-source event

Date: 2026-08-18

Status: **DERIVED UNIT-SCALE EVENT PRODUCT. IF A BOUNDED-GEOMETRY PROJECTIVE/SIGNED PARTNER NETWORK SUPPLIES A FIXED FRACTION OF AN ORDER-ONE VORTICITY BIRTH, THEN THE KERNEL-WEIGHTED STRAIN-SQUARE ACTION TIMES THE TOTAL MAGNITUDE+ANGULAR GRADIENT ACTION HAS A FIXED POSITIVE LOWER BOUND, INDEPENDENT OF THE EVENT DURATION. A SHORT EVENT PAYS STRAIN; A LONG EVENT PAYS VISCOUS INTERFACE/DIRECTION GRADIENT. GLOBAL REGULARITY NOT PROVED.**

## 1. Normalized same-scale source event

Work in the natural terminal normalization of one compact critical cell, so

\[
\|\Omega\|_\infty\le1
\]

and the active packet scale is order one.  Let `K(x,s)` be the exact terminal adjoint advection--diffusion kernel.

Define

\[
E_K=\int K|\Omega|^2,
\qquad
Q_K=\int K\,\Omega\cdot S\Omega,
\]

and the robust total vorticity-gradient split

\[
P_{\rm grad,K}
=P_{\rm mag,K}+P_{\rm ang,K}
=\int K|\nabla\Omega|^2.
\]

Let `A` be the subset of normalized times on which a bounded-geometry same-scale projective/signed partner configuration is the source-active mechanism.

## 2. Partner variance forces total gradient content

The exact weighted variance split gives

\[
\operatorname{Var}_K(\Omega)
=D_{\rm proj,K}+D_{\rm line,K}.
\]

Gaussian/Poincare control on a bounded-condition unit window gives

\[
\operatorname{Var}_K(\Omega)
\lesssim
P_{\rm grad,K}.
\]

If the partner source has fixed nondegenerate angular/polarity geometry, then on the source-active set

\[
D_{\rm proj,K}+D_{\rm line,K}\ge d_0>0.
\]

Hence

\[
\boxed{
P_{\rm grad,K}(s)\ge c_0>0
\qquad(s\in A).
}
\]

This includes both possible realizations:

- thick directional change, paid by `P_ang`;
- low-magnitude interface between differently oriented packets, paid by `P_mag`.

## 3. Order-one source requires inverse-duration strain square

Suppose the partner mechanism supplies a fixed fraction of the order-one terminal vorticity birth:

\[
\int_A Q_K(s)\,ds\ge q_0>0.
\]

Because `|Omega|<=1` and `K` is a probability density,

\[
|Q_K|
\le
\left(\int K|S|^2\right)^{1/2}
\left(\int K|\Omega|^4\right)^{1/2}
\le
\left(\int K|S|^2\right)^{1/2}.
\]

Set

\[
S_{2,K}(s)=\int K|S|^2.
\]

Then Cauchy--Schwarz in time gives

\[
q_0
\le
\int_A S_{2,K}^{1/2}ds
\le
|A|^{1/2}
\left(\int_A S_{2,K}ds\right)^{1/2}.
\]

Therefore

\[
\boxed{
\int_A S_{2,K}ds
\ge
\frac{q_0^2}{|A|}.
}
\]

## 4. Duration-free product

The gradient lower bound gives

\[
\int_A P_{\rm grad,K}ds
\ge
c_0|A|.
\]

Multiplying by the strain lower bound eliminates the duration:

\[
\boxed{
\left(\int_A S_{2,K}ds\right)
\left(\int_A P_{\rm grad,K}ds\right)
\ge
c_0q_0^2
=:c_*>0.
}
\]

Thus a source-active same-scale partner event cannot be made cheap merely by compressing or dilating its normalized lifetime.

- If `|A|` is tiny, the strain-square action is large.
- If `|A|` is long, the magnitude/angular gradient action is large.

## 5. Multiple sequential partner events

For disjoint or sequentially selected source-active events `A_j`, write

\[
X_j=\int_{A_j}S_{2,K_j}ds,
\qquad
Y_j=\int_{A_j}P_{\rm grad,K_j}ds.
\]

Each genuine event satisfies

\[
X_jY_j\ge c_*.
\]

Therefore

\[
\sum_j\sqrt{X_jY_j}
\ge
\sqrt{c_*}\,N.
\]

Cauchy--Schwarz in the event index yields

\[
\boxed{
N
\lesssim
\left(\sum_jX_j\right)^{1/2}
\left(\sum_jY_j\right)^{1/2}.
}
\]

This is a critical-action event-count estimate whenever the chosen events have a legitimate non-overcounted scale-time packing.

## 6. Limitation

Neither cumulative strain-square action nor scale-critical total vorticity-gradient action is known to be globally finite near a hypothetical singular time.  Moreover arbitrary overlapping source events require a separate phase-space/Bessel pruning before the multi-event sum can be used.

Thus the event product sharpens the genealogy ledger but does not prove global regularity.

Status: **SAME-SCALE PARTNER SOURCE HAS A FIXED DURATION-FREE STRAIN-SQUARE x MAGNITUDE+ANGULAR-GRADIENT PRODUCT / MULTIPLE PRUNED EVENTS ARE COUNTED BY THE GEOMETRIC MEAN OF TWO CRITICAL ACTIONS / GLOBAL REGULARITY NOT PROVED.**