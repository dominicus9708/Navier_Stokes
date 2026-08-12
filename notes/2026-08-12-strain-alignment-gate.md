# Strain-eigenvalue / vorticity-alignment gate

Date: 2026-08-12

Status: **DERIVED LINEAR-ALGEBRA BOUND + DSD CRITICAL-CHANNEL TARGET**.

## 1. Pointwise setup

At a point with `|omega|>0`, let

\[
S e_i=\lambda_i e_i,
\qquad
\lambda_1\le\lambda_2\le\lambda_3,
\]

and

\[
\xi=\frac{\omega}{|\omega|},
\qquad
a_i=(\xi\cdot e_i)^2,
\qquad
a_1+a_2+a_3=1.
\]

Incompressibility gives

\[
\lambda_1+\lambda_2+\lambda_3=0.
\]

The directional stretching rate is

\[
\gamma=\xi^TS\xi
=\lambda_1a_1+\lambda_2a_2+\lambda_3a_3.
\]

## 2. Exact upper gate

Because `lambda_1 <= lambda_2`,

\[
\gamma
\le
\lambda_2(a_1+a_2)+\lambda_3a_3.
\]

Therefore

\[
\boxed{
\gamma
\le
\lambda_2+(\lambda_3-\lambda_2)a_3.
}
\]

The difference is exactly

\[
\left[\lambda_2+(\lambda_3-\lambda_2)a_3\right]-\gamma
=(\lambda_2-\lambda_1)a_1\ge0.
\]

Hence

\[
\boxed{
\gamma_+
\le
U_{\rm align}
:=
\left[\lambda_2+(\lambda_3-\lambda_2)a_3\right]_+.
}
\]

Multiplying by the vorticity magnitude gives

\[
\boxed{
\sigma_+
\le
|\omega|^2U_{\rm align}.
}
\]

This is elementary spectral linear algebra, not a new Navier–Stokes regularity theorem.

## 3. Alignment threshold when the middle eigenvalue is negative

If

\[
\lambda_2<0,
\]

then `lambda_3>0` and

\[
\theta
=
\frac{-\lambda_2}{\lambda_3-\lambda_2}
\in(0,1).
\]

The upper gate becomes

\[
U_{\rm align}
=(\lambda_3-\lambda_2)
(a_3-\theta)_+.
\]

Consequently, in a region with negative middle strain eigenvalue, positive vorticity stretching requires at least the **necessary alignment condition**

\[
\boxed{
a_3>\theta}
\]

with the most extensional strain eigenvector.

This divides the local danger mechanism into two typed cases:

1. `lambda_2 >= 0`: the middle strain direction is already noncompressive/extensional;
2. `lambda_2 < 0`: positive stretching can occur only if maximal-axis alignment exceeds the threshold `theta`.

## 4. DSD channel interpretation

Retain separately:

\[
\lambda_2^+,
\qquad
\lambda_3-\lambda_2,
\qquad
a_3,
\qquad
\theta,
\qquad
(a_3-\theta)_+.
\]

Do not store only `gamma` or `sigma`, because the same positive stretching value can arise from different eigenvalue/alignment mechanisms.

At `|omega|=0`, `a_3` and the vorticity-direction gate are **undefined/inapplicable**. The stretching density itself is still defined and equals zero there.

## 5. Scale-local critical channel

Under Navier–Stokes scaling, both the strain eigenvalues and `U_align` scale like `lambda^2`, while `|omega|^2` scales like `lambda^4`.

Therefore the parabolic-cylinder quantity

\[
\boxed{
C_{\rm align}(z_0,r)
=
r\int_{Q_r(z_0)}
|\omega|^2U_{\rm align}\,dxdt
}
\]

is dimensionless.

Likewise

\[
C_{\sigma+}(z_0,r)
=
r\int_{Q_r(z_0)}\sigma_+\,dxdt
\]

is dimensionless and satisfies

\[
C_{\sigma+}\le C_{\rm align}.
\]

These are **BRIDGE DEFINITIONS / TARGET CHANNELS**. No epsilon threshold or global bound has been established.

## 6. Relation to external regularity theory

Regularity criteria based on vorticity direction and on the positive part of the middle strain eigenvalue already exist in the Navier–Stokes literature. The present gate is therefore not presented as discovering that geometry matters.

Its DSD role is to place the two established geometric themes into one typed local channel system:

- middle-eigenvalue status;
- maximal-axis alignment;
- vorticity magnitude;
- applicability at zero vorticity;
- scale localization;
- off-diagonal interaction channels.

## 7. Benchmark role

For the single Gaussian benchmark, the vorticity direction aligns exactly with the middle strain eigenvector wherever `|omega|>0`:

\[
a_2=1,
\qquad
a_1=a_3=0,
\qquad
\gamma=\lambda_2.
\]

It is therefore a clean control case but does not exercise the `a_3` danger channel. The translated/superposed benchmark should be used next to test the nontrivial alignment gate.

## 8. Open proof obligation

A useful proof route would need to show, for arbitrary admissible data, that the scale-local positive channel

\[
C_{\rm align}(z_0,r)
\]

cannot remain large in the pattern required by a finite-time singularity, or that it forces an already-established regularity gate to activate.

No such estimate is currently proved.

## External anchors

- Peter Constantin and Charles Fefferman, *Direction of Vorticity and the Problem of Global Regularity for the Navier-Stokes Equations*, Indiana Univ. Math. J. 42 (1993), 775–789.
- Evan Miller, *A Regularity Criterion for the Navier–Stokes Equation Involving Only the Middle Eigenvalue of the Strain Tensor*, Arch. Rational Mech. Anal. 235 (2020), 99–139, DOI `10.1007/s00205-019-01419-z`.
