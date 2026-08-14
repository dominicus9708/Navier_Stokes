# Exact polar dynamics of the Gaussian mean vorticity

Date: 2026-08-14

Status: **EXACT AMPLITUDE/AXIS DYNAMICS IN THE SELF-CONSISTENT GAUSSIAN AFFINE FRAME**.

The mean-vorticity-axis routing can be made dynamical rather than purely static.  The Gaussian mean vorticity obeys an exact vector ODE, and its polar decomposition separates amplitude growth from axis rotation without approximation.

---

## 1. Mean-vorticity equation

In the self-consistent Gaussian affine frame,

\[
\bar\Omega
:=\int\gamma\Omega
\]

obeys

\[
\boxed{
\bar\Omega'
=L\bar\Omega+J,
}
\]

where

\[
J:=\int\gamma f_r
=J_{\rm str}+J_{\rm drift}.
\]

Write

\[
L=\bar S+\bar A,
\]

with symmetric `bar S` and antisymmetric `bar A`.

The antisymmetric part corresponds to the Gaussian mean vorticity itself.  Hence if

\[
\bar\Omega=Me,
\qquad
M=|\bar\Omega|>0,
\qquad
|e|=1,
\]

then

\[
\boxed{
\bar A e=0.
}
\]

---

## 2. Exact amplitude equation

Differentiate

\[
M=|\bar\Omega|.
\]

Then

\[
M'
=e\cdot\bar\Omega'
=M e^TL e+e\cdot J.
\]

Since `e^T bar A e=0`,

\[
\boxed{
M'
=M e^T\bar S e
+e\cdot J.
}
\]

Thus Gaussian mean-vorticity amplitude changes only through

1. affine directional strain along the current mean axis;
2. the longitudinal component of the residual source.

No separate rotational or pressure term appears at this level.

---

## 3. Exact axis equation

Differentiate

\[
e=\bar\Omega/M.
\]

Using the orthogonal projector

\[
P_e^\perp=I-e\otimes e,
\]

we obtain

\[
M e'
=P_e^\perp\bar\Omega'.
\]

Therefore

\[
M e'
=M P_e^\perp L e
+P_e^\perp J.
\]

Since `bar A e=0`,

\[
\boxed{
M e'
=M P_e^\perp\bar S e
+P_e^\perp J.
}
\]

Equivalently,

\[
\boxed{
e'
=P_e^\perp\bar S e
+\frac{P_e^\perp J}{M}.
}
\]

Thus mean-axis rotation is produced only by

1. affine strain axis conversion;
2. transverse residual source.

---

## 4. Four exact polar channels

The mean-vorticity vector dynamics therefore closes into four geometrically typed channels:

\[
\boxed{
\begin{array}{c|c}
\text{effect} & \text{source}\\
\hline
\text{mean amplitude growth/decay}
& M e^T\bar S e\\
\text{residual amplitude injection}
& e\cdot J\\
\text{affine mean-axis conversion}
& M P_e^\perp\bar S e\\
\text{residual mean-axis rotation}
& P_e^\perp J
\end{array}
}
\]

There is no fifth untyped local mechanism in the Gaussian mean equation.

---

## 5. Relation to the bounded-affine branch

If

\[
\int_I|\bar S|ds\le K,
\]

then affine amplitude exposure and affine axis rotation satisfy

\[
\left|
\int_I e^T\bar S e\,ds
\right|
\le K,
\]

and

\[
\int_I|P_e^\perp\bar S e|ds
\le K.
\]

Thus any mean-amplitude or mean-axis change beyond a bounded affine amount must be supplied by the residual source `J`.

Conversely, if repeated residual geometry attempts to cancel into the affine mean, the earlier `m^(-1/2)` cancellation estimate forces this accumulated affine budget to diverge and leaves the bounded-affine branch.

---

## 6. Mean-small versus mean-dominant regimes

The polar representation requires `M>0`, but the apparent singularity of the axis equation at small `M` is geometrically harmless.

### Mean-small regime

If

\[
M^2\lesssim V_\omega,
\]

then the Gaussian vorticity is not concentrated around a dominant nonzero mean.  The fluctuation `delta Omega` is already comparable to the total vorticity in mean square, so the direct fluctuating-vorticity geometry is the natural representation.

### Mean-dominant regime

If

\[
M^2\gg V_\omega,
\]

then the total vorticity is concentrated around the mean vector except for the separately measured projective/line defects.  Moreover

\[
\frac{|J|}{M}
\lesssim_K
\frac{\sqrt{V_\omega B}}{M},
\]

so residual-induced mean-axis rotation is suppressed by the fluctuation-to-mean ratio unless the residual source or projective defect becomes large.

Thus the `1/M` term does not create a new escape channel: small `M` selects the fluctuation representation, while large `M` stabilizes the mean-axis representation.

---

## 7. Direct link to Cauchy-type amplification bookkeeping

The exact amplitude identity may be written, where `M>0`, as

\[
\boxed{
\frac{d}{ds}\log M
=e^T\bar S e
+\frac{e\cdot J}{M}.
}
\]

Hence a large change of Gaussian mean-vorticity magnitude requires either

\[
\boxed{
\text{large accumulated affine directional strain}
}
\]

or

\[
\boxed{
\text{large longitudinal residual-source exposure}.
}
\]

This is the Gaussian-mean analogue of the material Cauchy stretch ledger.  The difference is explicit: the residual-source term records non-affine viscous/transport rewriting that a purely material formula separates into its viscous contribution.

Similarly, the axis equation is the Gaussian-mean analogue of the projective/eigenframe conversion ledger.

---

## 8. Current use

Combined with the preceding source-typing notes:

- `J_str` becomes projective defect or mean-axis stretch/conversion, modulo an excluded affine-cancellation route;
- `J_drift` becomes gap-two Hermite transfer and curvature surplus;
- the longitudinal part of total `J` changes mean-vorticity amplitude;
- the transverse part rotates the mean axis.

Thus both the magnitude and direction of the Gaussian mean vorticity now have explicit causal ledgers compatible with the existing Cauchy/projective organization.

Status: **GAUSSIAN MEAN-VORTICITY TIME TRACKING CLOSED EXACTLY / REMAINING FRONTIER IS CROSS-SCALE PACKING OR SIMULTANEOUS-SATURATION RIGIDITY**.
