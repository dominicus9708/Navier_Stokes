# Restartable material parabolic tube

Date: 2026-08-12

Status: **DERIVED GEOMETRIC/SCALING BRIDGE + EXTERNAL REGULARITY ANCHOR + OPEN PROOF OBLIGATION**.

## 1. Why the material cell should be restarted at each scale

A material cell initialized at time `0` can accumulate deformation for a very long time before a candidate singular time.  That accumulated history is not the correct object for a local parabolic regularity test at scale `ell`.

For each restart time `t0`, initial label `a`, and scale `ell`, define a local flow map

\[
\partial_s\Phi_{s;t_0}(b)=u(\Phi_{s;t_0}(b),s),
\qquad
\Phi_{t_0;t_0}(b)=b,
\]

for

\[
s\in[t_0,t_0+\ell^2].
\]

The restartable material tube is

\[
\mathcal T(a,\ell,t_0)
=
\left\{
(\Phi_{s;t_0}(b),s):
 b\in B_\ell(a),
 s\in[t_0,t_0+\ell^2]
\right\}.
\]

This is matched to the Navier--Stokes parabolic scaling: spatial scale `ell` is paired with time scale `ell^2`.

## 2. Recent compression and extension channels

Let the ordered strain eigenvalues be

\[
\lambda_1\le\lambda_2\le\lambda_3,
\qquad
\lambda_1+\lambda_2+\lambda_3=0.
\]

Define recent material distortion channels

\[
K_-(a,\ell,t_0)
=
\int_{t_0}^{t_0+\ell^2}
\sup_{b\in B_\ell(a)}
[-\lambda_1(\Phi_{s;t_0}(b),s)]\,ds,
\]

\[
K_+(a,\ell,t_0)
=
\int_{t_0}^{t_0+\ell^2}
\sup_{b\in B_\ell(a)}
\lambda_3(\Phi_{s;t_0}(b),s)\,ds.
\]

Both are dimensionless and invariant under Navier--Stokes scaling.

For material tangent vectors,

\[
\frac{d}{ds}\log|Fv|
=\eta^TS\eta,
\]

so recent extension is bounded by `K_+`, while inverse-map / compression growth is bounded by `K_-`.

In an affine audit one obtains cell radii comparable to

\[
\ell e^{-K_-}
\quad\text{and}\quad
\ell e^{K_+}.
\]

For a general nonlinear cell, converting this to rigorous ball inclusions requires corresponding bi-Lipschitz control of the flow map throughout the reference ball.  That is a bridge obligation rather than an automatic consequence of one center-point value.

## 3. Mean-centered parabolic oscillation

Using the restartable material cell, define at each `s`

\[
C_{\rm osc}(a,\ell,s;t_0)
=
\ell^{-1}
\int_{B_\ell(a)}
|u(\Phi_{s;t_0}(b),s)-\bar U(s)|^2db,
\]

where `bar U(s)` is the material-cell mean.

The parabolic time average

\[
\boxed{
\mathfrak C_{\rm osc}(a,\ell,t_0)
=
\ell^{-2}
\int_{t_0}^{t_0+\ell^2}
C_{\rm osc}(a,\ell,s;t_0)\,ds
}
\]

is again Navier--Stokes scale invariant.

The corresponding pressure and viscous difference channels can be averaged in the same way.

## 4. Material path channel

A material tube is not centered at a fixed Eulerian point.  To compare it with an ordinary parabolic cylinder, define a scale-invariant path excursion after removing a constant Galilean velocity `c`:

\[
K_{\rm path}
=
\ell^{-1}
\sup_{s\in[t_0,t_0+\ell^2]}
\left|
X(s)-X(t_0)-c(s-t_0)
\right|,
\]

where

\[
X(s)=\Phi_{s;t_0}(a).
\]

A bounded `K_path` means that, after one constant Galilean shift, the moving center remains within an `O(ell)` spatial neighborhood during the parabolic window.

This channel is required if the material-tube quantities are to be transferred to a fixed-center Eulerian epsilon-regularity criterion.

## 5. Relation to the critical `L^2` Morrey scale

At a restart time, the flow map is the identity.  Therefore

\[
\ell^{-1}
\int_{B_\ell(a)}|u|^2dx
=
C_{\rm osc}
+
C_{\rm mean},
\]

where

\[
C_{\rm mean}
=
\ell^{-1}|B_\ell|\,|\bar U|^2.
\]

The left side is the basic local quantity underlying the critical velocity Morrey space `M^{2,1}`.

Existing Navier--Stokes theory already gives small-data regularity/global results in the critical `M^{2,1}` setting and local-energy regularity results based on small truncated Morrey quantities.  The DSD contribution here is **not** to rename that known quantity.  It is to keep its internal-oscillation and coherent-mean channels separate and then follow them through a moving material tube.

## 6. Current bridge to an Eulerian regularity gate

A prospective route now has three distinct obligations on a parabolic material tube:

1. **internal critical smallness/control** through `mathfrak C_osc` and pressure/viscous difference channels;
2. **recent shape control** through `K_-` and `K_+` so the material cell remains comparable to an ordinary ball;
3. **path control** through `K_path` so the moving cell can be covered by a fixed or Galilean-shifted Eulerian parabolic cylinder.

If these three can be bounded in a non-circular way at every candidate singular point and scale, the material description can be transferred to existing Eulerian local regularity machinery.

At present no such arbitrary-data a-priori bound has been proved.

Status: **OPEN PROOF OBLIGATION**.

## External anchor

Bradshaw and Tsai, *Global existence, regularity, and uniqueness of infinite energy solutions to the Navier-Stokes equations*, develop regularity results based on small truncated critical `L^2` Morrey quantities and identify `M^{2,1}` as a critical velocity space.  This is used only as an external anchor for the scale of the local energy channel; the restartable material-tube decomposition is an application-specific bridge in this repository.
