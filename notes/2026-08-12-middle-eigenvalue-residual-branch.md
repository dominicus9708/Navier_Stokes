# Middle-eigenvalue / extensional-alignment branch of the residual singular class

Date: 2026-08-12

Status: **EXTERNAL NECESSARY BLOW-UP CONDITION + DERIVED BRANCH DECOMPOSITION + OPEN CO-LOCATION ESTIMATE**.

This note combines Evan Miller's scale-critical middle-strain criterion with the repository's vorticity-direction/strain competition identity.

No new middle-eigenvalue regularity theorem is claimed.

## 1. External middle-eigenvalue criterion

Let

\[
\lambda_1\le\lambda_2\le\lambda_3,
\qquad
\lambda_2^+=\max\{\lambda_2,0\},
\]

be the ordered eigenvalues of the strain tensor.

Miller proves that if

\[
\frac2p+\frac3q=2,
\qquad
\frac32<q\le\infty,
\]

then a mild solution obeys an `Hdot^1` estimate controlled exponentially by

\[
\int_0^T\|\lambda_2^+(t)\|_{L^q}^pdt.
\]

Consequently a finite maximal smooth time `T*` requires

\[
\boxed{
\int_0^{T^*}
\|\lambda_2^+(t)\|_{L^q}^pdt
=\infty.
}
\]

In particular the endpoint `q=infinity, p=1` gives

\[
\boxed{
\int_0^{T^*}
\|\lambda_2^+(t)\|_\infty dt
=\infty.
}
\]

External source: Evan Miller, *A regularity criterion for the Navier-Stokes equation involving only the middle eigenvalue of the strain tensor*, arXiv:1710.05569 / Arch. Rational Mech. Anal. 235 (2020).

## 2. Maximum-vorticity competition channel

Where `omega != 0`, define

\[
\rho=|\omega|,
\qquad
\xi=\omega/|\omega|,
\qquad
\gamma=\xi^TS\xi.
\]

The repository already derived

\[
(\partial_t+u\cdot\nabla-\nu\Delta)\rho
=
\rho(\gamma-\nu|\nabla\xi|^2).
\]

Let

\[
W(t)=\|\omega(t)\|_\infty,
\qquad
\mathcal M(t)=\{x:|\omega(x,t)|=W(t)\},
\]

and

\[
\mathcal G(t)
=
\sup_{x\in\mathcal M(t)}
(\gamma-\nu|\nabla\xi|^2)_+.
\]

Finite-time growth of `W` to infinity requires

\[
\int^{T^*}\mathcal G(t)dt=\infty.
\]

## 3. Pointwise branch decomposition

Write

\[
a_i^2=(\xi\cdot e_i)^2,
\qquad
\sum_i a_i^2=1.
\]

The eigenframe bound is

\[
\gamma
\le
\lambda_2^+(1-a_3^2)
+
\lambda_3a_3^2.
\]

At a point where

\[
g=\gamma-\nu|\nabla\xi|^2>0,
\]

set

\[
A=\lambda_2^+(1-a_3^2),
\]

\[
B=\lambda_3a_3^2-
u|\nabla\xi|^2.
\]

Then

\[
g\le A+B.
\]

Therefore at least one of

\[
\boxed{
A\ge \frac g2
}
\]

or

\[
\boxed{
B\ge \frac g2
}
\]

must hold.

Since `A <= lambda_2^+`, positive maximum-vorticity growth has the exact either/or consequence

\[
\boxed{
\lambda_2^+\ge\frac g2
\quad\text{or}\quad
\lambda_3a_3^2-
u|\nabla\xi|^2\ge\frac g2.
}
\]

The second branch requires extensional alignment strong enough not merely to be positive, but to overcome the direction-gradient diffusion penalty.

## 4. Time-level branch channels

Define

\[
\Lambda_{2,M}(t)
=
\sup_{x\in\mathcal M(t)}\lambda_2^+(x,t),
\]

\[
\Lambda_{2,\infty}(t)
=
\|\lambda_2^+(t)\|_\infty,
\]

and

\[
\mathcal E_3(t)
=
\sup_{x\in\mathcal M(t)}
(\lambda_3a_3^2-
u|\nabla\xi|^2)_+.
\]

Then

\[
\boxed{
\mathcal G(t)
\le
\Lambda_{2,M}(t)+\mathcal E_3(t)
\le
\Lambda_{2,\infty}(t)+\mathcal E_3(t).
}
\]

Hence

\[
\int^{T^*}\mathcal G=\infty
\]

forces at least one of

\[
\int^{T^*}\Lambda_{2,M}(t)dt=\infty
\]

or

\[
\int^{T^*}\mathcal E_3(t)dt=\infty.
\]

This is only a branch decomposition of the maximum-vorticity growth mechanism.

## 5. Co-location versus spatial-separation branches

Miller's theorem separately requires

\[
\int^{T^*}\Lambda_{2,\infty}(t)dt=\infty.
\]

This gives two qualitatively different residual scenarios.

### Branch C: co-located middle-strain growth

\[
\boxed{
\int^{T^*}\Lambda_{2,M}(t)dt=\infty.
}
\]

The positive middle-strain channel repeatedly reaches the maximum-vorticity set itself.

This is the natural branch on which vorticity occupancy and local strain-volume estimates may interact directly.

### Branch S: spatially separated middle-strain growth

Suppose instead

\[
\int^{T^*}\Lambda_{2,M}(t)dt<\infty.
\]

Then necessarily

\[
\boxed{
\int^{T^*}\mathcal E_3(t)dt=\infty
}
\]

in order to drive `W` to infinity, while Miller still requires

\[
\boxed{
\int^{T^*}\Lambda_{2,\infty}(t)dt=\infty.
}
\]

Thus the strongest positive-middle-strain events must occur substantially away from the maximum-vorticity growth mechanism often enough to keep the two integrals distinct.

This is a **spatial-separation residual branch**:

- global `lambda_2^+` must be critically nonintegrable somewhere;
- maximum vorticity is instead driven by most-extensional alignment beating direction diffusion.

## 6. Why this split is useful

Previously `G_dir^c` and `G_strain^c` were listed as separate residual requirements.  The present split shows that they cannot remain completely independent near maximum-vorticity growth.

A singular residual flow must choose, repeatedly in time, between

\[
\boxed{
\text{middle-strain / maximum-vorticity co-location}
}
\]

and

\[
\boxed{
\text{extensional-alignment growth at the vorticity maximum}
+
\text{middle-strain divergence elsewhere}.
}
\]

This is a genuine narrowing of the residual class, but not an exclusion.

## 7. Connection to occupancy

The existing vorticity occupancy gate says that a residual singularity must keep intense vorticity sufficiently non-sparse at the natural `W^{-1/2}` scale.

This suggests two different next estimates.

### Co-location target

If `lambda_2^+` is large at a maximum-vorticity point and intense vorticity occupies a non-sparse region nearby, prove that positive middle strain also occupies enough volume to create a lower bound on a scale-critical `L^q` channel.

No such propagation-of-strain estimate is yet established here.

### Separation target

If the `lambda_2^+` divergence stays spatially separated from the vorticity maximum while `mathcal E_3` drives the maximum, prove that the required spatial separation or off-diagonal coupling incurs a pressure/dissipation/higher-derivative cost.

No such estimate is yet established here.

## 8. DSD typed branch block

Retain

\[
\mathcal B_{\rm strain}(t)
=
\bigl(
\mathcal G,
\Lambda_{2,M},
\Lambda_{2,\infty},
\mathcal E_3,
W,
\rho_{\rm occ},
\text{separation-distance},
\text{cross-coupling}
\bigr).
\]

Do not collapse `Lambda_{2,M}` and `Lambda_{2,infinity}`: their difference is precisely the new co-location/separation information.

## 9. Open proof target

The next useful theorem would exclude at least one branch:

\[
\boxed{
\text{Branch C impossible}
\quad\text{or}\quad
\text{Branch S impossible}.
}
\]

A stronger result would show that both branches force one of the already established regularity gates.

Status: **OPEN CO-LOCATION / SEPARATION ESTIMATE**.
