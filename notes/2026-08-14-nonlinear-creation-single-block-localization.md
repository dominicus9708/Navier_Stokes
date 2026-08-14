# Nonlinear creation localizes to one matched heat block

Date: 2026-08-14

Status: **EXACT ON THE ISOTROPIC MATCHED HEAT CHAIN / BOUNDED-AFFINE VERSION REQUIRES ONLY A UNIFORM CONTRACTION FACTOR BELOW ONE**.

This note closes one specific loophole in the current bounded-affine first-hitting analysis: a required nonlinear Duhamel contribution cannot be hidden by distributing an arbitrarily small amount of creation over arbitrarily many geometric scale-time blocks.

## 1. Matched geometric heat chain

Fix `0<c<1` and consider isotropic Gaussian covariances

\[
\Sigma_{j+1}=c\Sigma_j.
\]

Choose successive times so that

\[
2\nu(t_{j+1}-t_j)=(1-c)\Sigma_j.
\]

Let

\[
B_j=\mathcal B_{\Sigma_j}[g(t_j)],
\qquad
A_j:=\sqrt{B_j},
\]

where `g=grad U` after removal of the Gaussian affine mean.

Write the exact mild step as

\[
g(t_{j+1})
=P_{(1-c)\Sigma_j}g(t_j)+Q_j.
\]

The matched heat-contraction identity gives

\[
\mathcal B_{\Sigma_{j+1}}
[P_{(1-c)\Sigma_j}g(t_j)]
\le c B_j.
\]

Since the square root of Gaussian variance is an `L2` seminorm,

\[
\boxed{
A_{j+1}
\le \rho A_j+q_j,
\qquad
\rho=\sqrt c<1,
\qquad
q_j:=\sqrt{\mathcal B_{\Sigma_{j+1}}[Q_j]}.
}
\]

## 2. Iteration

Iterating from block `0` to block `N` gives

\[
A_N
\le
\rho^N A_0
+
\sum_{j=0}^{N-1}
\rho^{N-1-j}q_j.
\]

Let

\[
q_*:=\max_{0\le j<N}q_j.
\]

Then

\[
A_N
\le
\rho^N A_0
+
q_*\sum_{k=0}^{N-1}\rho^k
\le
\rho^N A_0
+
\frac{q_*}{1-\rho}.
\]

Therefore, if the final pulse obeys

\[
A_N\ge \kappa\sqrt m
\]

for some fixed `kappa>0`, while the inherited initial part satisfies

\[
\rho^N A_0=o(\sqrt m),
\]

then necessarily

\[
\boxed{
q_*
\ge
(1-\rho)(\kappa-o(1))\sqrt m.
}
\]

Equivalently, at at least one matched heat block,

\[
\boxed{
\mathcal B_{\Sigma_{j+1}}[Q_j]
\ge c_{c,\kappa}\,m
}
\]

for all sufficiently large first-hitting levels.

## 3. Consequence for the adaptive precursor result

The previous-checkpoint inheritance estimate already gives

\[
B_{\rm inh}=o(m)
\]

on a surviving intermediate branch.

The present lemma strengthens the interpretation of

\[
B_Q\ge(1-o(1))m.
\]

The required nonlinear creation cannot be realized solely as a sum of vanishingly small commutators over an arbitrarily long scale chain. Because linear heat propagation contracts variance by a fixed factor at every matched step, geometric memory is summable.

Hence there exists at least one **single matched parabolic block** carrying order-`m` nonlinear variance creation.

This reduces the remaining nonlinear-packing problem from an arbitrary long Duhamel history to a local block question.

## 4. Bounded-affine extension

In a co-deforming bounded-condition affine frame, the same proof works provided the homogeneous affine Gaussian propagator satisfies a uniform variance contraction

\[
\sqrt{B_{j+1}^{\rm hom}}
\le \rho_K\sqrt{B_j},
\qquad
\rho_K<1,
\]

on the chosen fixed covariance ratio.

Then

\[
\boxed{
\max_j\sqrt{B_{Q_j}}
\ge
(1-\rho_K-o(1))\sqrt m.
}
\]

The isotropic statement is exact. The remaining affine task is only to write the corresponding Gaussian Markov propagator and verify a uniform `rho_K<1` under the already assumed condition-number and accumulated-affine bounds.

Status: **MULTISCALE-DILUTION LOOPHOLE CLOSED IN THE ISOTROPIC CHAIN / ACTIVE LOCAL QUESTION = WHAT AN ORDER-m NONLINEAR CREATION BLOCK MUST COST OR FORCE.**
