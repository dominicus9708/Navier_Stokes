# Leray Non-Normality Strain Floor — 2026-08-20

Status: **RECURRENT-ORBIT AMPLITUDE NECESSITY — GLOBAL REGULARITY NOT PROVED.**

This note combines the exact vorticity-gradient non-normality identity with `LERAY_H1_RECURRENCE_TAX_2026-08-20.md`.

Let

\[
G=\nabla_Y\widetilde\Omega.
\]

The exact production identity is

\[
N_L
=\frac12\int
\Sigma:(G^TG-GG^T)dY.
\]

## 1. Böttcher--Wenzel non-normality cap

The Frobenius commutator inequality gives

\[
\|G^TG-GG^T\|_F
\le\sqrt2\,\|G\|_F^2.
\]

Therefore

\[
N_L
\le
\frac1{\sqrt2}
\|\Sigma\|_\infty
\|\nabla\widetilde\Omega\|_2^2.
\]

The strain--vorticity derivative isometry gives

\[
\|\nabla\widetilde\Omega\|_2^2
=2\|\nabla\Sigma\|_2^2=2P.
\]

Hence

\[
\boxed{
N_L
\le
\sqrt2\,\|\Sigma\|_\infty P.
}
\]

Equality at the matrix level requires maximally non-normal, rank-one shear-type gradient geometry; for example a rank-one matrix `G=a tensor b` with `a dot b=0` saturates the commutator factor.

## 2. Insert into the exact Leray H1 ledger

The Leray identity is

\[
\frac12P_s+\frac34P+\nu H=N_L.
\]

Thus

\[
\boxed{
\frac12P_s
+\left(\frac34-\sqrt2\|\Sigma\|_\infty\right)P
+\nu H
\le0.
}
\]

In particular, if

\[
\|\Sigma\|_\infty<\frac3{4\sqrt2}
\approx0.530330086
\]

uniformly, `P` cannot support a nonzero recurrent orbit.

## 3. Quantitative recurrent compact-class floor

Let `K` be the nonzero precompact recurrent class and define

\[
B_K=\sup_{\Sigma\in K}\|\Sigma\|_\infty,
\]

\[
\kappa_K^+
=\sup_{\Sigma\in K}\frac{P}{H}<\infty.
\]

Then

\[
H\ge\frac1{\kappa_K^+}P.
\]

Integrate the previous differential inequality between recurrent return pairs whose `H^2` endpoint difference tends to zero. The endpoint `P` difference vanishes asymptotically, and the return interval carries positive `P` mass. Therefore recurrence requires

\[
\sqrt2 B_K
\ge
\frac34+rac{\nu}{\kappa_K^+}.
\]

Hence

\[
\boxed{
B_K
\ge
\frac1{\sqrt2}
\left(
\frac34+rac{\nu}{\kappa_K^+}
\right).
}
\]

Even after discarding the positive viscosity contribution,

\[
\boxed{
B_K\ge\frac3{4\sqrt2}\approx0.530330086.
}
\]

## 4. Spectral interpretation

For every trace-free symmetric `3x3` strain matrix,

\[
\lambda_{max}(\Sigma)
\ge\frac{|\Sigma|}{\sqrt6}.
\]

Therefore a recurrent class satisfying the amplitude floor must contain points/times with positive extensional eigenvalue at least

\[
\boxed{
\lambda_3
\ge
\frac{B_K}{\sqrt6}
\ge
\frac1{\sqrt{12}}
\left(
\frac34+rac{\nu}{\kappa_K^+}
\right).
}
\]

Ignoring the viscosity improvement gives the universal recurrent floor

\[
\lambda_3\gtrsim0.21650635
\]

at some point/time in the normalized Leray class.

This does not yet imply that the vorticity direction is aligned with that eigenvector. It is therefore a strain-amplitude necessity, not by itself a vortex-stretching contradiction.

## 5. New combined survivor geometry

A non-H/T recurrent `P_V` survivor must now simultaneously have:

1. a nonvanishing compact H2 profile;
2. the strict Leray threshold `Lambda_K >= nu + 3 kappa_K/4`;
3. strain amplitude at least `3/(4 sqrt(2))`, with a larger floor when `nu/kappa_K^+` is retained;
4. sufficiently non-normal vorticity-gradient geometry to supply the commutator production;
5. the previously derived near-max-mid/covariance constraints whenever H1 production approaches its algebraic ceiling.

The next rigidity target is to quantify the incompatibility between the rank-one shear-type gradient geometry needed for near Böttcher--Wenzel saturation and the near-max-mid derivative geometry needed for near strain-H1 saturation.

Status: **A NONZERO RECURRENT LERAY `P_V` ORBIT MUST REACH NORMALIZED STRAIN AMPLITUDE AT LEAST `0.530330086`, AND MORE PRECISELY `B_K >= (3/4 + nu/kappa_K^+)/sqrt(2)`. RECURRENCE THEREFORE REQUIRES BOTH STRONG STRAIN AND STRONG VORTICITY-GRADIENT NON-NORMALITY.**