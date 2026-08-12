# Small-scale limit of local projective covariance: recovery of the vorticity-direction gradient

Date: 2026-08-13

Status: **DERIVED LOCAL ASYMPTOTIC IDENTITY / CONNECTS COVARIANCE TO CLASSICAL DIRECTION-GRADIENT GEOMETRY**.

This note identifies the infinitesimal meaning of the local projective covariance defect `J_r`.

At a smooth point where vorticity is nonzero, `J_r/r^2` converges to a kernel constant times `|grad xi|^2`, where

\[
\xi=\omega/|\omega|.
\]

Thus the local covariance channel is a sign-invariant finite-scale regularization of the classical vorticity-direction gradient.

## 1. Local enstrophy probability measure

Let

\[
\omega=\rho\xi,
\qquad
\rho=|\omega|>0,
\qquad
|\xi|=1.
\]

For a smooth positive radial normalized kernel

\[
\eta_r(h)=r^{-3}\eta(h/r),
\qquad
\int\eta=1,
\]

define at a fixed point `x`

\[
d\mu_{x,r}(y)
=
\frac{\eta_r(x-y)\rho(y)^2dy}{E_r(x)},
\]

where

\[
E_r(x)=\int\eta_r(x-y)\rho(y)^2dy.
\]

Then

\[
C_r(x)=\int\xi(y)\otimes\xi(y)d\mu_{x,r}(y),
\]

and

\[
\boxed{
J_r(x)
=
\iint
[1-(\xi(y)\cdot\xi(y'))^2]
\,d\mu_{x,r}(y)d\mu_{x,r}(y').
}
\]

## 2. Kernel covariance

Let

\[
M_{ab}
=
\int z_a z_b\eta(z)dz.
\]

For a radial kernel,

\[
\boxed{M_{ab}=m_\eta\delta_{ab}.}
\]

The total normalized second moment is

\[
\int|z|^2\eta(z)dz=3m_\eta.
\]

For the Student-type kernel used in the local covariance-axis lemma,

\[
\int|z|^2\eta(z)dz
=\frac{3}{2m-5},
\]

so

\[
\boxed{m_\eta=\frac1{2m-5}.}
\]

## 3. Taylor expansion of the direction field

Write

\[
y=x+rz,
\qquad
y'=x+rz'.
\]

Smoothness gives

\[
\xi(x+rz)
=
\xi_0+r(z\cdot\nabla)\xi_0+O(r^2),
\]

uniformly on compact `z` sets.

Because `|xi|=1`,

\[
\xi_0\cdot\partial_a\xi_0=0.
\]

Therefore

\[
\xi(x+rz)-\xi(x+rz')
=r[(z-z')\cdot\nabla]\xi_0+O(r^2).
\]

For two nearby unit vectors `a,b`,

\[
1-(a\cdot b)^2
=|a-b|^2+O(|a-b|^4).
\]

Hence

\[
1-(\xi(x+rz)\cdot\xi(x+rz'))^2
=
r^2
\left|
[(z-z')\cdot\nabla]\xi_0
\right|^2
+o(r^2).
\]

## 4. The enstrophy weight does not change the leading coefficient

Since `rho(x)>0`,

\[
\rho(x+rz)^2
=\rho(x)^2+O(r).
\]

The radial kernel has zero first moment, so after normalization the measure `mu_{x,r}` converges to `eta(z)dz`, and the `O(r)` density correction does not contribute to the leading `r^2` pair variance.

Therefore

\[
\frac{J_r(x)}{r^2}
\to
\iint
\left|
[(z-z')\cdot\nabla]\xi_0
\right|^2
\eta(z)\eta(z')dzdz'.
\]

## 5. Evaluate the pair covariance

Because the kernel mean is zero,

\[
\iint
(z-z')_a(z-z')_b
\eta(z)\eta(z')dzdz'
=2M_{ab}.
\]

Thus, for a general centered kernel,

\[
\boxed{
\lim_{r\to0}
\frac{J_r(x)}{r^2}
=
2\sum_{a,b}
M_{ab}
\partial_a\xi(x)\cdot\partial_b\xi(x).
}
\]

For a radial kernel,

\[
\boxed{
\lim_{r\to0}
\frac{J_r(x)}{r^2}
=2m_\eta|\nabla\xi(x)|^2.
}
\]

For the Student kernel,

\[
\boxed{
\lim_{r\to0}
\frac{J_r(x)}{r^2}
=
\frac{2}{2m-5}
|\nabla\xi(x)|^2.
}
\]

## 6. Define the renormalized finite-scale direction-gradient channel

For a radial kernel define

\[
\boxed{
\mathcal G_r(x)
=
\frac{J_r(x)}{2m_\eta r^2}.
}
\]

Then at every smooth nonzero-vorticity point,

\[
\boxed{
\mathcal G_r(x)
\longrightarrow
|\nabla\xi(x)|^2.
}
\]

Unlike the pointwise direction vector `xi`, `J_r` is projective and therefore invariant under the sign flip

\[
\xi\mapsto-\xi.
\]

This is appropriate for vortex-stretching geometry, where parallel and antiparallel directions both have zero cross product.

## 7. Relation to the local-axis gradient estimate

The local covariance-axis lemma gave

\[
r|\nabla n_r|
\lesssim
\sqrt{\Pi_r}
\]

in the small-defect regime.

Since

\[
\Pi_r\sim\frac12J_r
\]

when `J_r -> 0`, the infinitesimal limit gives

\[
|\nabla n_r|
=O(|\nabla\xi|)
\]

at smooth nonzero-vorticity points.

Thus the covariance-axis gluing estimate has the correct small-scale differential behavior.

## 8. Relation to logarithmic/BMO direction criteria

Classical geometric depletion conditions are commonly stated in terms of pointwise Hölder coherence or function-space control of the vorticity direction. A recent 2026 preprint studies a logarithmically weighted BMO-type direction condition in a critical-point setting.

The covariance quantity `J_r` is an `L^2` pairwise oscillation rather than a BMO seminorm. Therefore no equivalence with those hypotheses is claimed.

However the scale family

\[
\boxed{
\left\{
\frac{\sqrt{J_r(x)}}{r}
\right\}_{r>0}
}

is a natural projective square-oscillation analogue of a direction-gradient/coherence profile.

Possible borderline quantities include logarithmically weighted scale envelopes such as

\[
|\log r|\sqrt{J_r},
\]

but any regularity implication for such an averaged condition must be proved separately rather than imported from BMO by notation.

## 9. DSD interpretation

The physical-scale index `r` and the direction channel are not independent bookkeeping devices in the small-scale limit.

They satisfy

\[
\boxed{
J_r
\sim
2m_\eta r^2|\nabla\xi|^2.
}
\]

Thus the DSD multiscale covariance block is a finite-resolution description of the same geometric direction variation that appears in established Navier--Stokes depletion theory.

This makes the current three-index route

\[
(\text{physical scale }r,\ 
\text{derivative order }k,\ 
\text{projective covariance})
\]

internally consistent with the classical infinitesimal geometry.

Status: **BRIDGE ESTABLISHED — BORDERLINE MULTISCALE REGULARITY CONDITION STILL OPEN**.
