# Coherent mean rotation: turnover-scale Coriolis rigidity on the tight branch

Date: 2026-08-14

Status: **EXACT CORIOLIS KERNEL IDENTITY + CONDITIONAL TIGHT-COMPACTNESS RIGIDITY / COHERENT-ROTATION SUBBRANCH ONLY**.

## 1. Mean affine rotation

In the self-consistent Gaussian affine frame write

\[
L=\bar S+A,
\qquad
A=\frac12(L-L^T).
\]

Let

\[
\bar\Omega_\gamma
=\int\gamma\,\Omega.
\]

Because averaging commutes with taking the antisymmetric part of the gradient,

\[
\boxed{
A v
=\frac12\bar\Omega_\gamma\times v.
}
\]

Thus the antisymmetric affine part is coherent solid-body rotation, not strain.

This corrects any bookkeeping that would charge the full matrix `L` to accumulated affine deformation: only `sym L` deforms; `A` is removed by an orthogonal change of coordinates.

## 2. Co-rotating perturbation equation

First freeze the covariance and suppress the already typed affine-forcing projection to display the principal structure. For

\[
V(y,t)=Ly+r(y,t)
\]

with constant skew part `A`, the perturbation equation contains

\[
\partial_t r
+(Ay\cdot\nabla)r
+A r
+(r\cdot\nabla)r
+\cdots.
\]

Let `Q'=AQ` and set

\[
y=Q(t)z,
\qquad
w(z,t)=Q(t)^Tr(Q(t)z,t).
\]

The coordinate derivative supplies one additional `A w`. Consequently the coherent rotation becomes the Coriolis-type term

\[
\boxed{
2Aw
=\bar\Omega_\gamma\times w.
}
\]

The symmetric affine strain remains as a separate deformation channel. Time-dependent covariance/affine commutators are also kept separate and are not silently absorbed into the Coriolis term.

## 3. Turnover normalization

For a pulse height `m`, normalize residual velocity and time by

\[
\widehat w=\frac{w}{R\sqrt m},
\qquad
\tau=\sqrt m\,(t-t_R).
\]

The Coriolis coefficient is

\[
\boxed{
\Gamma
=\frac{|\bar\Omega_\gamma|}{\sqrt m}.
}
\]

Hence the coherent-rotation branch

\[
|\bar\Omega_\gamma|\gg\sqrt m
\]

has

\[
\Gamma\to\infty.
\]

This is a subbranch, not an automatic consequence of the terminal pointwise normalization: the mean vorticity on a large Gaussian may be small because of cancellation or spatial concentration.

## 4. Exact whole-space Coriolis kernel identity

Fix a unit vector `e` and define on divergence-free fields

\[
\mathcal C_e w
:=\mathbb P(e\times w),
\]

where `mathbb P` is the Leray projector.

For `xi !=0`, put `n=xi/|xi|`. Since `hat w(xi)` lies in `n^perp`, a direct two-dimensional calculation in that plane gives

\[
\boxed{
|P_n(e\times\widehat w)|^2
=|e\cdot n|^2|\widehat w|^2.
}
\]

Therefore

\[
\boxed{
\|\mathcal C_e w\|_2^2
=
\int_{\mathbb R^3}
\frac{(\xi\cdot e)^2}{|\xi|^2}
|\widehat w(\xi)|^2d\xi.
}
\]

In particular,

\[
\mathcal C_e w=0
\]

implies that `hat w` is supported on the plane

\[
\xi\cdot e=0.
\]

This plane has three-dimensional Lebesgue measure zero. Hence

\[
\boxed{
\ker_{L^2_\sigma(\mathbb R^3)}\mathcal C_e
=\{0\}.
}
\]

The familiar nonzero exactly columnar fields are not in global `L2(R3)` unless they vanish, because they are independent of the coordinate parallel to `e`.

## 5. Tight compactness rigidity lemma

Consider a sequence of turnover-normalized residuals `w_j` on a fixed time interval with

\[
\Gamma_j\to\infty,
\qquad
|e_j|=1,
\qquad
e_j\to e.
\]

Suppose their equations can be written distributionally as

\[
\partial_\tau w_j
+\Gamma_j\mathcal C_{e_j}w_j
=F_j,
\]

where

- `w_j` is bounded in global `L2` and strongly precompact in the topology needed to pass to the limit;
- `F_j` is uniformly bounded as a distribution on compact time intervals after all separately typed strain, covariance, high-curvature, and transport branches have been excluded.

Divide by `Gamma_j` and test against a compactly supported smooth spacetime function. Integration by parts in time makes the `Gamma_j^{-1} partial_tau w_j` term vanish, while `Gamma_j^{-1}F_j` vanishes by the assumed bound. Thus

\[
\mathcal C_e w=0
\]

for every strong limit `w`.

The kernel identity yields

\[
\boxed{w=0.}
\]

Therefore a normalized nonzero residual cannot have all of

1. coherent mean rotation `Gamma_j -> infinity`;
2. whole-space/spatial tightness;
3. low-curvature compactness;
4. bounded non-Coriolis forcing after the already typed channels are removed.

## 6. Escape alternatives

A surviving coherent-rotation pulse must therefore lose at least one hypothesis above. It must produce

\[
\boxed{
\text{higher-chaos/frequency loss of compactness}
\quad\text{or}\quad
\text{spatial non-tightness / shell transport}
\quad\text{or}\quad
\text{large symmetric-affine/frame forcing}
\quad\text{or}\quad
\text{mean rotation not dominant}.
}
\]

This is a genuine branch reduction on the coherent-mean-rotation subcase.

## 7. Approximate kernel and columnar concentration

The exact identity also shows

\[
\|\mathcal C_e w\|_2^2
=
\int \cos^2\theta_\xi\,|\widehat w|^2d\xi.
\]

Thus approximate Coriolis kernel states concentrate Fourier energy in a thin slab around

\[
\xi\cdot e=0.
\]

Such concentration corresponds to increasingly long physical coherence in the `e` direction. If global spatial tightness is retained, that concentration cannot persist under strong `L2` compactness; if tightness is lost, it is naturally routed to the existing shell/critical-mass transport branch.

## 8. Relation to rotating-fluid literature

The algebra above is derived directly and does not invoke an external rotating-fluid regularity theorem. Published rotating Navier--Stokes/Euler results generally assume an externally imposed, spatially uniform Coriolis force and use dispersive or Strichartz estimates. The present mean rotation is self-generated and local, so those theorems are structural comparison points only, not proof imports.

Status: **COHERENT-ROTATION + TIGHT LOW-CURVATURE SURVIVOR EXCLUDED CONDITIONALLY; NONCOHERENT ROTATION, HIGHER CHAOS, OR TRANSPORT REMAINS**.
