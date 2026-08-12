# Local covariance equals a smoothed pairwise projective vorticity spectrum

Date: 2026-08-13

Status: **DERIVED EXACT LOCAL-TO-PAIRWISE IDENTITY / OPEN SINGULAR-KERNEL DEPLETION ESTIMATE**.

This note connects the local vorticity covariance block directly to the pairwise angular geometry that underlies classical geometric depletion of vortex stretching.

External context: Constantin--Fefferman (Indiana Univ. Math. J. 42 (1993), 775--789) initiated the Navier--Stokes regularity route based on vorticity direction. The identity below is elementary covariance algebra and is not presented as a novelty claim without a separate literature audit.

## 1. Local covariance block

Let `eta_r` be the positive normalized smooth kernel already used in the local covariance-axis lemma:

\[
\eta_r(z)=r^{-3}\eta(z/r),
\qquad
\int\eta_r=1.
\]

Define

\[
E_r(z)
=\int\eta_r(z-x)|\omega(x)|^2dx,
\]

\[
N_r(z)
=\int\eta_r(z-x)\omega(x)\otimes\omega(x)dx,
\]

\[
C_r(z)=N_r(z)/E_r(z)
\]

when `E_r(z)>0`, and

\[
J_r(z)=1-\operatorname{tr}(C_r(z)^2).
\]

## 2. Exact pointwise pair identity

We have

\[
E_r(z)^2J_r(z)
=E_r(z)^2-\operatorname{tr}(N_r(z)^2).
\]

The first term is

\[
E_r(z)^2
=
\iint
\eta_r(z-x)\eta_r(z-y)
|\omega(x)|^2|\omega(y)|^2dxdy.
\]

The second is

\[
\operatorname{tr}(N_r(z)^2)
=
\iint
\eta_r(z-x)\eta_r(z-y)
(\omega(x)\cdot\omega(y))^2dxdy.
\]

Using

\[
|a\times b|^2
=|a|^2|b|^2-(a\cdot b)^2,
\]

we obtain

\[
\boxed{
E_r(z)^2J_r(z)
=
\iint
\eta_r(z-x)\eta_r(z-y)
|\omega(x)\times\omega(y)|^2dxdy.
}
\]

Thus the local covariance defect is exactly the local enstrophy-weighted mean squared projective mismatch of pairs of vorticity vectors seen through the same observation kernel.

## 3. Integrate over all observation centers

Integrating in `z` and using Fubini,

\[
\begin{aligned}
\int E_r(z)^2J_r(z)dz
&=
\iint
\left[
\int\eta_r(z-x)\eta_r(z-y)dz
\right]
|\omega(x)\times\omega(y)|^2dxdy.
\end{aligned}
\]

For a radial/even kernel,

\[
\int\eta_r(z-x)\eta_r(z-y)dz
=(\eta_r*\eta_r)(x-y).
\]

Hence

\[
\boxed{
\mathcal P_r
:=
\int E_r(z)^2J_r(z)dz
=
\iint
K_r(x-y)
|\omega(x)\times\omega(y)|^2dxdy,
}
\]

where

\[
\boxed{K_r=\eta_r*\eta_r.}
\]

The kernel `K_r` is positive, radial, normalized, and has physical scale `r`.

## 4. Projective scale spectrum

Define

\[
\boxed{
\mathcal P_r
=
\int E_r^2J_r.
}
\]

Interpretation:

- `E_r^2`: local pairwise enstrophy weight;
- `J_r`: local multi-axis/projective defect;
- `P_r`: total pairwise cross-axis content visible at physical scale `r`.

If all vorticity vectors sampled at scale `r` lie on one unoriented axis, then

\[
\mathcal P_r=0.
\]

If they populate several axes, `P_r` is positive.

This is sign-invariant because `omega` and `-omega` determine the same projective axis.

## 5. Navier--Stokes scaling

Under

\[
\omega_\lambda(x,t)
=\lambda^2\omega(\lambda x,\lambda^2t),
\]

with the observation scale transformed as

\[
r\mapsto r/\lambda,
\]

one has

\[
E_r\mapsto\lambda^4E_{\lambda r},
\]

so

\[
\boxed{
\mathcal P_r
\mapsto
\lambda^5\mathcal P_{\lambda r}.
}
\]

Therefore

\[
\boxed{
\mathcal P_r^{1/2}
\mapsto
\lambda^{5/2}\mathcal P_{\lambda r}^{1/2},
}
\]

which is the same scaling as

\[
\|S\omega\|_2.
\]

This makes `P_r^(1/2)` a dimensionally natural candidate for geometric depletion of the base projective forcing norm.

## 6. Why the singular kernel still matters

The strain is a singular integral of vorticity, and the geometric vortex-stretching kernel has the borderline three-dimensional spatial homogeneity `|x-y|^-3` together with an angular cancellation factor.

The smooth pair kernel

\[
K_r=\eta_r*\eta_r
\]

is bounded at separation zero and therefore does **not** by itself dominate the full singular stretching kernel.

Thus one must not claim

\[
\|S\omega\|_2
\lesssim\mathcal P_r^{1/2}
\]

for a single fixed `r` without an additional argument.

The correct next step is a dyadic physical-scale decomposition.

## 7. Dyadic criticality

Let

\[
r_j=2^{-j}r_0.
\]

On a shell

\[
|x-y|\sim r_j,
\]

the singular strain kernel has size

\[
r_j^{-3},
\]

while shell volume is of order

\[
r_j^3.
\]

Thus the geometric size and volume cancel at leading order: there is no automatic dyadic decay.

This explains why the vorticity-direction channel is scale-critical and why angular/projective depletion must itself improve at small scales.

A suitable shell projective channel should therefore measure

\[
|\omega(x)\times\omega(y)|
\]

at each `r_j`, rather than relying only on one aggregate global covariance.

## 8. Connection to the DSD three-index route

The active proof architecture now has an exact relation among its indices:

\[
\boxed{
\text{physical scale }j
\longleftrightarrow
\text{pairwise projective covariance at scale }r_j,
}
\]

while derivative order `k` remains the independent regularity-resolution index.

Thus the earlier schematic object

\[
\mathcal K_{j,k}
\]

can be refined to retain a direction-covariance component

\[
\boxed{
\mathcal K_{j,k}
\supset
(E_{j,k},J_{j,k},\mathcal P_{j,k}).
}
\]

This does not introduce a new spatial dimension; it is a typed multiscale descriptor of the same 3D field.

## 9. Open target

The next proof-producing estimate would compare the near-field part of

\[
\|S\omega\|_2
\]

with a summable or otherwise controllable dyadic family built from

\[
\mathcal P_{r_j}^{1/2},
\]

or from a point-centered version of the same projective defect.

Because the kernel is borderline, a simple geometric series is not expected; a Dini/logarithmic/BMO-type summability mechanism is consistent with the established direction-coherence literature.

Status: **OPEN DYADIC PROJECTIVE DEPLETION OF VORTEX STRETCHING**.
