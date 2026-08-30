# DSD M5-335 — Near-Planar Strain / Neutral-Axis Locking Fork

Date: 2026-08-30

Status: **DETERMINANT-DEGENERATE LARGE STRAIN REDUCED TO VORTICITY STRETCH/TILT OR NEUTRAL-AXIS LOCKING / EXACT AFFINE ANTI-MODEL LIES ONLY IN THE LOCKED SECTOR / GLOBAL REGULARITY UNPROVED.**

## 1. Planar spectral corridor

Work on the near-planar sector from M5-334:

\[
|\lambda_2|<\delta|S|,
\qquad 0<\delta\ll1.
\]

Let `e_1,e_2,e_3` be the orthonormal eigenframe of `S`, ordered by

\[
\lambda_1\ge\lambda_2\ge\lambda_3.
\]

Trace-freeness gives, uniformly for sufficiently small fixed `delta`,

\[
\boxed{
\lambda_1\ge c_\delta|S|,
\qquad
-\lambda_3\ge c_\delta|S|,
}
\]

while `e_2` is the unique approximately neutral strain axis.

## 2. Vorticity-axis decomposition

On the active set `|omega|>0`, let

\[
\xi=\frac\omega{|\omega|}.
\]

Write

\[
S\xi=\gamma\xi+\tau,
\qquad
\tau\perp\xi.
\]

Then

\[
\boxed{
|S\xi|^2=\gamma^2+|\tau|^2.
}
\]

Expand

\[
\xi=\xi_1e_1+\xi_2e_2+\xi_3e_3.
\]

Since `S` is diagonal in this frame,

\[
|S\xi|^2
=\lambda_1^2\xi_1^2+\lambda_2^2\xi_2^2+\lambda_3^2\xi_3^2.
\]

Hence

\[
\boxed{
\gamma^2+|\tau|^2
\ge
c_\delta^2|S|^2(\xi_1^2+\xi_3^2).
}
\]

Define the angle to the neutral axis by

\[
\sin\theta_2
:=\sqrt{1-(\xi\cdot e_2)^2}
=\sqrt{\xi_1^2+\xi_3^2}.
\]

Then

\[
\boxed{
\sqrt{\gamma^2+|\tau|^2}
\ge c_\delta|S|\sin\theta_2.
}
\]

## 3. Unlocked sector

Fix an angular threshold `epsilon>0` and define

\[
\mathcal P_{un}(\delta,\varepsilon)
=\{|\lambda_2|<\delta|S|,\ \sin\theta_2\ge\varepsilon\}.
\]

On this set,

\[
\boxed{
\gamma^2+|\tau|^2
\ge c_{\delta,\varepsilon}|S|^2.
}
\]

Therefore any nonsummable atom-compressive `L_t^2L_x^3` action carried by this set forces

\[
\boxed{
\int^{T_*}\|\gamma\mathbf1_{\mathcal P_{un}}\|_3^2dt=\infty
\quad\text{or}\quad
\int^{T_*}\|\tau\mathbf1_{\mathcal P_{un}}\|_3^2dt=\infty.
}
\]

Thus determinant-degenerate strain is not a separate obstruction whenever the vorticity axis is not locked to the neutral strain axis.

## 4. Locked sector

The only remaining planar sector is

\[
\boxed{
\mathcal P_{lock}(\delta,\varepsilon)
=\{|\lambda_2|<\delta|S|,\ \sin\theta_2<\varepsilon\}.
}
\]

Here

\[
\xi\approx\pm e_2,
\]

and a large transverse hyperbolic strain can be almost invisible to both vorticity stretching and vorticity-axis turning.

The exact affine model

\[
S=\operatorname{diag}(a,0,-a)
\]

with vorticity parallel to `e_2` lies precisely in this branch.

Hence this is the unique axis geometry preserving the previously identified affine anti-model.

## 5. Dynamic equations on the locked branch

The vorticity-direction equation is

\[
(\partial_t+u\cdot\nabla)\xi
=\tau
+\frac\nu{|\omega|}
(I-\xi\otimes\xi)\Delta\omega.
\]

For a simple eigenvalue `lambda_2`, the material derivative of its eigenvector is

\[
\boxed{
D_te_2
=\sum_{k\ne2}
\frac{e_k^T(D_tS)e_2}{\lambda_2-\lambda_k}e_k.
}
\]

In the planar corridor the spectral gaps satisfy

\[
|\lambda_2-\lambda_1|
+|\lambda_2-\lambda_3|
\gtrsim_\delta |S|.
\]

Thus neutral-axis locking over time requires the projective velocities `D_t xi` and `D_t e_2` to remain matched up to the small angular error.

This gives the next structural fork:

\[
\boxed{
\mathcal P_{lock}
\Longrightarrow
\text{projective mismatch/turnover}
\ \lor\
\text{matched neutral-axis transport}.
}
\]

## 6. Formation/axis interpretation

The planar branch is now no longer described merely by a large number `|D_perp|`.
Its minimal descriptor contains

\[
(|S|,\lambda_2/|S|,\xi\cdot e_2,D_t\xi,D_te_2).
\]

At the present resolution the only hard planar object is

\[
\boxed{
\text{large planar compression}
+\text{neutral-axis vorticity lock}
+\text{matched projective transport}.
}
\]

The next standard-mathematical target is the equation maintaining `lambda_2\approx0` itself.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
