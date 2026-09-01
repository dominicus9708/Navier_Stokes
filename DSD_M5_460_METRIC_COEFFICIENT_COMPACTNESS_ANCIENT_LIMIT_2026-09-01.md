# DSD M5-460 — Coefficient compactness and ancient metric limit

Date: 2026-09-01

Status: **ON THE BOUNDED OUTER-ENSTROPHY / BOUNDED-DEFORMATION BRANCH, THE REMOTE AFFINE STRAIN MATRIX IS A SMOOTH-KERNEL FUNCTIONAL OF THE OUTER VORTICITY AND IS UNIFORMLY LIPSCHITZ IN NORMALIZED TIME ON COMPACT BACKWARD INTERVALS / CONSEQUENTLY `A_j`, `F_j`, `C_j`, AND `G_j` ARE PRECOMPACT TOGETHER WITH THE INNER FIRST-HITTING STATES / A NONTRIVIAL COMPLETE ANCIENT TIME-DEPENDENT METRIC COVECTOR SOLUTION CAN BE EXTRACTED / THE REMAINING GAP IS ITS CRITICAL LIouVILLE/RIGIDITY CLASSIFICATION / GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. Affine strain is a smooth outer-vorticity functional

In M5-449 the remote source is separated from the inner target by a fixed positive distance in outer Euler coordinates. Each component of the harmonic strain matrix at the target can therefore be written schematically as

\[
A_j^{ab}(\tau)
=
\int K_A^{ab}(y)\,\Omega_j(y,\tau)\,dy,
\]

where `K_A` is a fixed smooth kernel on the retained source annulus, after the standard cutoff separating the selected source cluster.

## 2. Time derivative bound

The outer vorticity equation is

\[
\partial_\tau\Omega_j
+\nabla\cdot(V_j\otimes\Omega_j-\Omega_j\otimes V_j)
=K_j^{-2}\Delta\Omega_j.
\]

Differentiate the smooth pairing and integrate by parts:

\[
\begin{aligned}
\frac d{d\tau}A_j^{ab}
&=
\int \nabla K_A^{ab}:
(V_j\otimes\Omega_j-\Omega_j\otimes V_j)\,dy\\
&\quad
+K_j^{-2}\int (\Delta K_A^{ab})\Omega_j\,dy.
\end{aligned}
\]

On every compact backward interval M5-448 gives

\[
\|\Omega_j\|_\infty\le1,
\qquad
\|\Omega_j\|_2\le B_A,
\qquad
\|V_j\|_\infty\le C_A.
\]

Since `K_A` has fixed compact support,

\[
\boxed{
\sup_j\sup_{\tau\in[-T,0]}
|A_j'(\tau)|
\le C_T.
}
\]

The harmonic derivative estimates also give a uniform bound on `A_j` itself.

Thus `A_j` is equi-Lipschitz on every compact backward interval.

## 3. Deformation and metric coefficient compactness

Let

\[
F_j'=A_jF_j,
\qquad F_j(0)=I
\]

in the chosen stage gauge. On the bounded-deformation branch assume

\[
\|F_j\|+\|F_j^{-1}\|\le K_F
\]

on each retained compact backward interval, uniformly in `j`.

Then `F_j'` is uniformly bounded. Therefore Arzela--Ascoli gives, after a diagonal subsequence,

\[
A_j\to A,
\qquad
F_j\to F
\]

locally uniformly in time, with

\[
F'=AF,
\qquad
\det F=1.
\]

Define

\[
C_j=F_j^TF_j,
\qquad
G_j=C_j^{-1}.
\]

Then

\[
\boxed{
C_j\to C,
\qquad
G_j\to G
}
\]

locally uniformly, and the limit remains uniformly elliptic with

\[
C=F^TF,
\qquad
G=F^{-1}F^{-T},
\qquad
\det C=\det G=1.
\]

## 4. Inner-state compactness

The original first-hitting analyticity bounds, bounded linear distortion, and M5-452 metric div-curl estimates give local spatial compactness for the pulled-back inner states `(eta_j,w_j)` on every fixed cylinder, outside the already typed strong derivative/remote exits.

The vorticity equation

\[
\partial_t\eta_j
+\nabla\cdot(w_j\otimes\eta_j-\eta_j\otimes w_j)
=\nabla\cdot(G_j\nabla\eta_j)
\]

then gives time equicontinuity against compact smooth test functions. Together with `G_j -> G`, pass to a diagonal subsequence and obtain a complete ancient metric solution

\[
(\eta,w,C,G)
\]

on

\[
\mathbb R^3\times(-\infty,0].
\]

It satisfies

\[
\boxed{
\partial_t\eta+(w\cdot\nabla)\eta
=(\nabla w)\eta+\nabla\cdot(G\nabla\eta),
}
\]

\[
\boxed{
\eta=\nabla\times(Cw),
\qquad
\nabla\cdot w=0.
}
\]

The marked first-hitting core/dual-source construction prevents the limit from being identically zero.

## 5. Updated compact branch

The bounded-deformation/bounded-source branch is therefore no longer merely a formal variable-coefficient possibility. It produces an actual nontrivial ancient object:

\[
\boxed{
M_{ancient}^{metric}(C(t),G(t)).
}
\]

This object has:

- uniform spatial ellipticity;
- determinant-one metric;
- locally Lipschitz coefficient history;
- standard Gaussian parabolic scaling;
- uniform metric Biot--Savart bounds;
- inherited first-hitting/dual-source geometry.

## 6. Remaining theorem gap

M5-459 explains why standard Albritton--Barker Theorem 4.1 cannot yet be invoked verbatim. The next split should be the metric analogue of

\[
W_1^{metric}:\sup_k\|w(t_k)\|_{L^{3,\infty}}<\infty
\]

versus

\[
W_2^{metric}:\|w(t_k)\|_{L^{3,\infty}}\to\infty.
\]

The `W2` lane is strong critical-mass/frequency throughput. The `W1` lane requires a metric weak-`L^{3,\infty}` stability and terminal regularity theorem.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]