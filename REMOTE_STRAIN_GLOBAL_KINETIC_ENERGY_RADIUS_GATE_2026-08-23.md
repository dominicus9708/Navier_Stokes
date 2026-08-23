# Remote Strain Global-Kinetic-Energy Radius Gate — 2026-08-23

Status: **S-LEVEL POINTWISE/FINITE-STAGE ACTIVE-RADIUS BOUND — GLOBAL REGULARITY NOT PROVED.**

This note strengthens the active `H_remote` radius restriction again. Instead of estimating remote strain through normalized enstrophy, integrate the remote Biot--Savart strain formula by parts and estimate it directly by the globally bounded physical kinetic energy.

The resulting normalized active-radius ceiling is

\[
R\lesssim W^{1/10},
\]

hence the physical active radius satisfies

\[
\ell\lesssim W^{-2/5}.
\]

This is stronger than the previous `o(W^(-1/3))` consequence obtained by time-integrating the `R^3` enstrophy tax.

## 1. Smooth remote strain functional

At one first-hitting normalized time let

\[
U(y)=W^{-1/2}u(X_*+W^{-1/2}y),
\qquad
\Omega=\nabla_y\times U.
\]

Let `K` be the degree `-3` strain-from-vorticity kernel and choose a smooth radial remote cutoff

\[
\psi_R=0\quad(|y|\le R),
\qquad
\psi_R=1\quad(|y|\ge2R),
\]

with the standard derivative bounds

\[
|\nabla^m\psi_R|\lesssim R^{-m}.
\]

Define

\[
\boxed{
\mathcal S_R
:=\int K(y)\psi_R(y)\Omega(y)dy.
}
\]

This differs from a sharp exterior cutoff only by a controlled annular transition and is the natural smooth remote-source quantity used in `REMOTE_STRAIN_SOURCE_EVOLUTION_IDENTITY_2026-08-23.md`.

## 2. Integrate vorticity by parts

Since

\[
\Omega=\nabla\times U,
\]

and the fields decay rapidly, integration by parts gives schematically

\[
\mathcal S_R
=
-\int \nabla(K\psi_R)\,\mathcal R(U)\,dy,
\]

where `mathcal R` here denotes only the fixed index permutation/contraction from the curl; it introduces no derivative or scale factor.

The derivative of the cutoff kernel obeys

\[
|\nabla(K\psi_R)|
\lesssim
|y|^{-4}\mathbf 1_{|y|\ge R}
+R^{-4}\mathbf 1_{R<|y|<2R}.
\]

Consequently

\[
\begin{aligned}
\|\nabla(K\psi_R)\|_2^2
&\lesssim
\int_R^\infty r^{-8}r^2dr
+R^{-8}|A_R|\\
&\lesssim R^{-5},
\end{aligned}
\]

and therefore

\[
\boxed{
\|\nabla(K\psi_R)\|_2
\le C_{KE}R^{-5/2}.
}
\]

By Cauchy--Schwarz,

\[
\boxed{
|\mathcal S_R|
\le
C_{KE}R^{-5/2}\|U\|_2.
}
\]

## 3. Convert normalized velocity energy to physical kinetic energy

The first-hitting scaling gives

\[
U(y)=W^{-1/2}u(x),
\qquad
 dy=W^{3/2}dx.
\]

Hence

\[
\boxed{
\|U\|_2^2
=W^{1/2}\|u\|_2^2,
}
\]

or

\[
\boxed{
\|U\|_2
=W^{1/4}\|u\|_2.
}
\]

For a smooth Navier--Stokes solution the physical kinetic-energy identity gives

\[
\|u(t)\|_2\le\|u_0\|_2.
\]

Therefore

\[
\boxed{
|\mathcal S_R|
\le
C_{KE}\|u_0\|_2
W^{1/4}R^{-5/2}.
}
\]

This estimate requires no vorticity-tightness and no normalized derivative bound.

## 4. Pointwise active normalized-radius ceiling

Suppose

\[
|\mathcal S_R|\ge s_0>0.
\]

Then

\[
s_0
\le
C_{KE}\|u_0\|_2W^{1/4}R^{-5/2}.
\]

Solving for `R`,

\[
\boxed{
R
\le
R_{KE,\max}(W;s_0)
:=
\left(
\frac{C_{KE}\|u_0\|_2}{s_0}
\right)^{2/5}
W^{1/10}.
}
\]

Thus an order-one dynamically active remote strain may move to infinity in normalized variables only at most like `W^(1/10)`.

## 5. Physical-radius ceiling

The physical radius associated with normalized radius `R` is

\[
\ell=RW^{-1/2}.
\]

Therefore

\[
\boxed{
\ell
\le
\left(
\frac{C_{KE}\|u_0\|_2}{s_0}
\right)^{2/5}
W^{-2/5}.
}
\]

This is a pointwise physical localization law for dynamically active remote strain.

In particular, a fixed positive physical radius `ell_*>0` cannot supply an order-one **normalized** strain as `W->infinity`.

## 6. Finite-stage action form

On one geometric first-hitting stage let

\[
W_j\le M(s)\le qW_j,
\qquad
L_j\le L_+.
\]

At each normalized time,

\[
\|U(s)\|_2
\le
(qW_j)^{1/4}\|u_0\|_2.
\]

For a fixed normalized remote cutoff radius `R`,

\[
\mathcal A_{R,j}
:=\int_{I_j}|\mathcal S_R(s)|ds
\]

therefore obeys

\[
\boxed{
\mathcal A_{R,j}
\le
C_{KE}q^{1/4}L_+\|u_0\|_2
W_j^{1/4}R^{-5/2}.
}
\]

If

\[
\mathcal A_{R,j}\ge a_0>0,
\]

then

\[
\boxed{
R
\le
\left(
\frac{C_{KE}q^{1/4}L_+\|u_0\|_2}{a_0}
\right)^{2/5}
W_j^{1/10}.
}
\]

Again the corresponding physical radius is `O(W_j^(-2/5))`.

## 7. Stronger contraction action on a consecutive active corridor

Suppose one chooses an effective active physical radius `ell_j` at each late stage and the active strain/action threshold is fixed below by `s0` or `a0` as above. Then

\[
\boxed{
\ell_j\lesssim W_j^{-2/5}.
}
\]

If the active radius is genuinely remote in normalized variables, `R_j->infinity`, then its physical radius still tends to zero.

For a consecutive geometric corridor `W_j=q^jW_0`, any path that asymptotically saturates or remains below this power law must carry an average inward logarithmic radius action at least

\[
\boxed{
\frac25\log q
}
\]

when the effective radius itself persists stage to stage.

A robust half-average threshold is

\[
\boxed{
\tau_{KE,*}:=\frac15\log q.
}
\]

Thus infinitely many stages must satisfy

\[
\boxed{
\ell_{j+1}\le q^{-1/5}\ell_j
}
\]

unless the effective source disappears/reappears through a distinct source-replacement event.

For `q=2`,

\[
1-2^{-1/5}\approx0.12944944,
\]

so this corresponds to about `12.94%` inward effective-radius contraction.

## 8. Same-material time floor

If one of these fixed contraction events is carried by the same coherent material structure, the exact material-line equation gives

\[
\log\frac{\ell_j}{\ell_{j+1}}
\le
\int_{I_j}\|\Sigma\|_\infty ds
\le B_+L_j.
\]

Hence

\[
\boxed{
L_j
\ge
L_{R,KE}^{mat}
:=
\frac{\log q}{5B_+}
=\frac15L_{def}.
}
\]

This strengthens the earlier `L_def/6` same-material threshold obtained from the `R^3` time-packing route.

## 9. Scope and remaining source-replacement issue

The kinetic-energy radius gate is pointwise and does not require vorticity tightness. It therefore applies even inside the new `V_remote` branch of vorticity/enstrophy non-tightness.

However, the estimate controls **where an active remote source may act**, not the identity of that source between stages. A nested family of distinct active sources can in principle replace one another while remaining inside the shrinking `W^(-2/5)` physical envelope.

That replacement is now the sharp turnover question. It is already represented in the exact remote-source evolution identity by physical-radius sweep and source-evolution terms, but a final global bound for that scale-critical turnover action has not been proved.

## 10. Updated hierarchy

For active remote strain, use the following hierarchy:

\[
\boxed{
|\mathcal S_R|
\lesssim
\min\left\{
R^{-3/2}Z^{1/2},
R^{-5/2}W^{1/4}\|u_0\|_2
\right\}.
}
\]

The first estimate is useful for vorticity-tight finite-radius closure and `R^3` enstrophy taxes. The second gives the unconditional kinetic-energy active-radius ceiling

\[
\boxed{
R=O(W^{1/10}),
\qquad
\ell=O(W^{-2/5}).
}
\]

Status: **GLOBAL KINETIC ENERGY LOCATES ANY ORDER-ONE ACTIVE REMOTE STRAIN INSIDE PHYSICAL RADIUS `O(W^(-2/5))`, WITHOUT VORTICITY TIGHTNESS. THIS STRENGTHENS THE REMOTE-H CONTRACTION ROUTE; DISTINCT SOURCE REPLACEMENT INSIDE THE SHRINKING ACTIVE ENVELOPE REMAINS THE TURNOVER BOTTLENECK. GLOBAL REGULARITY IS NOT PROVED.**
