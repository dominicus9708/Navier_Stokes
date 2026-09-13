# M19-202 — Continuous scattering-translation representation rules out a one-dimensional minus-one hard block

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / HARD-REPRESENTATION REFINEMENT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Exact differentiated scattering covariance

On the certified hard bundle,

\[
D\mathscr S_{\sigma_tU}\,\Phi_t(U)
=
T_{-t/2}\,D\mathscr S_U,
\]

where \(T_a\) is q-translation on scattering signatures.

Uniform observability makes \(D\mathscr S\) injective on each finite-dimensional hard fiber. Pulling back the translation-invariant scattering norm makes the hard cocycle isometric.

## 2. Continuous one-parameter orthogonal action

After identifying a retained finite-dimensional hard scattering subspace, the time action is a continuous homomorphism

\[
\boxed{
\rho:\mathbb R\to O(N),
\qquad
\rho(t+t')=\rho(t)\rho(t').
}
\]

Continuity and \(\rho(0)=I\) imply

\[
\det\rho(t)=1
\]

for all \(t\), hence

\[
\boxed{\rho(t)\in SO(N).}
\]

Equivalently,

\[
\rho(t)=e^{tA}
\]

for a real skew-symmetric generator \(A\).

## 3. Real block decomposition

A real skew-symmetric matrix decomposes orthogonally into

- zero one-dimensional blocks, generating the constant multiplier \(+1\);
- two-dimensional rotation blocks
\[
\begin{pmatrix}0&-\kappa\\ \kappa&0\end{pmatrix},
\]
with time action by angle \(\kappa t\).

Therefore every nontrivial unit phase, including \(-1\) at a particular return time, belongs to a two-dimensional real block.

## 4. Consequence for dimension one

If the symmetry-quotient hard dimension satisfies

\[
N\le1,
\]

then no nontrivial rotation block exists. The only possible hard action is

\[
\boxed{\rho(t)\equiv1.}
\]

In particular a one-dimensional hard return cannot have multiplier \(-1\).

Thus the M19-173 conditional reduction can be sharpened on the certified scattering-representable hard bundle:

\[
\boxed{
N\le1
\Longrightarrow
\text{no irrational elliptic block, no }(-1)\text{ block, and the residual hard direction is a }(+1)\text{ kernel direction}.
}
\]

## 5. Interpretation

The previous period-two allowance came from treating the quotient return as an arbitrary one-dimensional homeomorphism. The actual Navier--Stokes hard cocycle is more rigid: it is the restriction of a continuous translation representation.

## 6. Firewall

This result is conditional on the certified finite-dimensional scattering-observable hard bundle. It does not prove \(N\le1\); it sharpens what follows if that dimension threshold is reached.