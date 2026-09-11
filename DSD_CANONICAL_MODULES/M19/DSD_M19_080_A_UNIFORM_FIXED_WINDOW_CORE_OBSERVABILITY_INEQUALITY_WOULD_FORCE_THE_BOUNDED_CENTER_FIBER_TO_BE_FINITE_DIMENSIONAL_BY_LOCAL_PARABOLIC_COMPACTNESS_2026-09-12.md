# DSD M19-080 — A uniform fixed-window core observability inequality would force the bounded center fiber to be finite-dimensional by local parabolic compactness

**Date:** 2026-09-12  
**Status:** CONDITIONAL FINITE-DIMENSIONAL CENTER THEOREM / M19-079 IDENTIFIES THE RIGHT SPATIAL OBSERVATION REGION, BUT A TIME-UNIFORM FIXED-WINDOW OBSERVABILITY BRIDGE IS STILL MISSING / GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED

## 1. Purpose

M19-079 proved that every bounded nonzero neutral linearized trajectory carries a positive **long-time average** fraction of its weighted energy in one fixed finite core.

That statement alone does not imply that the center space is finite-dimensional.

The present module proves the exact conditional statement needed for such a conclusion:

\[
\boxed{
\text{fixed-window finite-core observability}
+\text{local parabolic smoothing}
\Longrightarrow
\text{finite-dimensional bounded center fiber}.
}
\]

This turns the vague phrase ``the center should be controlled by the core'' into one precise missing inequality.

## 2. Phase space and bounded center fiber

Use the pressure-compatible weighted Hilbert space

\[
X:=L^2_\sigma(\mathbb R^3,w\,dy),
\]

where

\[
w(y)=(1+\kappa|y|^2)^{-a/2}
\]

lies in the M19-063 \(A_2\) corridor.

Fix a recurrent base trajectory \(Y_0\) and its linearized cocycle

\[
\Phi(\theta,s;Y_0).
\]

Define the bounded complete center fiber at time \(0\) by

\[
\boxed{
\mathcal C_b(Y_0)
:=
\left\{
W_0\in X:
\begin{array}{l}
\text{there exists a complete linearized solution }W(\theta),\\
W(0)=W_0,\\
\sup_{\theta\in\mathbb R}\|W(\theta)\|_X<\infty
\end{array}
\right\}.
}
\]

Because the linearized equation is linear, \(\mathcal C_b(Y_0)\) is a linear subspace whenever complete bounded continuation is unique.

For the compactness argument we assume a uniform center propagation bound

\[
\boxed{
\sup_{|\theta|\le T}
\|W(\theta)\|_X
\le
M_T\|W(0)\|_X
\qquad
\forall W_0\in\mathcal C_b(Y_0)
}
\]

for each fixed \(T>0\).

This is automatic if the bounded center bundle is a continuous finite-codimension spectral bundle, but here it is listed explicitly rather than assumed silently.

## 3. Desired fixed-window observability

Suppose there exist

\[
R<\infty,
\qquad
\tau>0,
\qquad
C_{obs}<\infty
\]

such that every \(W_0\in\mathcal C_b(Y_0)\) obeys

\[
\boxed{
\|W(0)\|_X^2
\le
C_{obs}
\int_{-\tau/2}^{\tau/2}
\int_{B_R}|W(y,\theta)|^2w(y)\,dy\,d\theta.
}
\tag{OBS}
\]

The constants must be uniform over the entire bounded center fiber.

Because \(\mathcal C_b\) is linear, the same inequality automatically applies to differences of two center trajectories.

That difference property is essential for compactness.

## 4. Local parabolic regularization from an earlier bounded time

Take the larger interval

\[
[-\tau,\tau].
\]

A unit-bounded sequence

\[
W_{0,n}\in\mathcal C_b,
\qquad
\|W_{0,n}\|_X\le1
\]

has, by the center propagation bound,

\[
\sup_n\|W_n(-\tau)\|_X
\le M_\tau.
\]

Evolve forward from \(-\tau\).

On the finite cylinder

\[
Q_{2R}:=B_{2R}\times[-3\tau/4,3\tau/4],
\]

the recurrent base coefficients \(U,\nabla U\) are uniformly smooth and bounded by the retained compact-corridor hypotheses.

The weighted norm \(X\) controls ordinary \(L^2\) on every fixed ball because \(w\) is bounded above and below there.

Standard interior parabolic estimates for the linearized incompressible system therefore give, after shrinking away from the initial time,

\[
\boxed{
\sup_n
\left[
\|W_n\|_{L^2(-3\tau/4,3\tau/4;H^1(B_{2R}))}
+
\|\partial_\theta W_n\|_{L^2(-3\tau/4,3\tau/4;H^{-1}(B_{2R}))}
\right]
<\infty.
}
\]

The pressure is not an uncontrolled local source: the global \(A_2\) estimate from M19-064 controls the linearized pressure in \(L^2(w)\), and hence locally in \(L^2\) on \(B_{2R}\).

Thus the usual local parabolic compactness mechanism is available on the observation cylinder.

## 5. Compactness of the observation map

Define

\[
\mathcal O_{R,\tau}:
\mathcal C_b(Y_0)
\to
L^2\bigl((-\tau/2,\tau/2)\times B_R\bigr)
\]

by

\[
\boxed{
\mathcal O_{R,\tau}W_0
:=W|_{(-\tau/2,\tau/2)\times B_R}.
}
\]

The estimates of Section 4 and Aubin--Lions/Rellich compactness yield

\[
\boxed{
\mathcal O_{R,\tau}
\text{ maps bounded subsets of }\mathcal C_b(Y_0)
\text{ to relatively compact subsets of the observation space.}
}
\]

Equivalently,

\[
\boxed{
\mathcal O_{R,\tau}
\text{ is a compact linear observation operator.}
}
\]

This does **not** say that the global cocycle on \(X\) is compact. M19-077 already disproved that shortcut.

Only the finite-core spacetime observation is compact.

## 6. Compact observation plus observability makes the center unit ball compact

Take any bounded sequence

\[
W_{0,n}\in\mathcal C_b,
\qquad
\|W_{0,n}\|_X\le1.
\]

By compactness of \(\mathcal O_{R,\tau}\), choose a subsequence, not relabeled, such that

\[
\mathcal O_{R,\tau}W_{0,n}
\]

is Cauchy in the observation space.

For two indices \(n,m\), the difference

\[
V_{n,m}:=W_n-W_m
\]

is again a bounded complete center trajectory.

Apply (OBS):

\[
\begin{aligned}
\|W_{0,n}-W_{0,m}\|_X^2
&\le
C_{obs}
\|\mathcal O_{R,\tau}(W_{0,n}-W_{0,m})\|_{L^2}^2.
\end{aligned}
\]

The right-hand side tends to zero as \(n,m\to\infty\).

Hence

\[
\boxed{
\{W_{0,n}\}
\text{ has a strongly convergent subsequence in }X.
}
\]

Therefore the closed unit ball of \(\mathcal C_b(Y_0)\) is relatively compact in its own norm.

## 7. Riesz lemma forces finite dimension

An infinite-dimensional normed linear space cannot have a compact closed unit ball.

Therefore

\[
\boxed{
(OBS)
\Longrightarrow
\dim\mathcal C_b(Y_0)<\infty.
}
\]

This is the desired conditional finite-dimensional center theorem.

No global compactness of the weighted phase space is required.

## 8. Why M19-079 is not yet enough

M19-079 gives

\[
\boxed{
\overline E_c
\ge
\delta_R\overline E
}
\]

for each bounded nonzero neutral trajectory.

This is a long-time average statement.

It permits the core visits to occur in bursts separated by arbitrarily long intervals.

By contrast, (OBS) requires one universal finite window centered at the reference time:

\[
[-\tau/2,\tau/2].
\]

Thus the missing implication is

\[
\boxed{
\text{positive long-time core occupation}
\not\stackrel{current\ results}{\Longrightarrow}
\text{uniform fixed-window observability}.
}
\]

This is now the exact temporal gap.

## 9. Relation to the symmetry center

M19-075 identified the certified symmetry-generated center

\[
E^c_{sym}
=
\operatorname{span}
\{\partial_\theta U,Z_A:A\in\mathfrak{so}(3)\}
\]

modulo the rotational stabilizer.

M19-080 does not prove

\[
\mathcal C_b=E^c_{sym}.
\]

It would only prove that \(\mathcal C_b\) is finite-dimensional under (OBS).

A finite-dimensional center may still contain additional neutral directions and may support quasiperiodic dynamics.

Therefore

\[
\boxed{
\text{finite-dimensional center}
\neq
\text{factor rigidity}.
}
\]

It is nevertheless a major structural reduction because the formal infinite-dimensional scattering center of M19-068 could no longer be realized independently by the interior cocycle.

## 10. Relative-periodic branch remains visible

The rotational quotient of M19-076 can be combined with this theorem because rotations commute with q-translation.

However a relative-periodic state

\[
\sigma_TY=R\cdot Y
\]

must remain an explicit branch.

Finite-dimensionality after rotational modulation does not itself exclude such rotating/screw recurrence.

## 11. What is certified

M19-080 certifies the implication:

\[
\boxed{
\begin{array}{c}
\text{uniform bounded-center propagation}\\
+\text{fixed-window finite-core observability}\\
+\text{local parabolic regularity}
\end{array}
\Longrightarrow
\dim\mathcal C_b<\infty.
}
\]

The proof uses only:

1. compactness of a **local observation operator**;
2. observability for differences;
3. Riesz lemma.

## 12. What remains unproved

M19-080 does not certify:

1. (OBS) for the Navier--Stokes recurrent center;
2. boundedness of every zero-Lyapunov representative;
3. a numerical upper bound on \(\dim\mathcal C_b\);
4. exhaustion by symmetry modes;
5. exclusion of aperiodic or relative-periodic recurrent factors;
6. global regularity.

## 13. Next target

The next question is now sharply temporal:

> Can recurrence plus the positive long-time core fraction from M19-079 force a bounded gap between core-observation episodes?

Abstract recurrence does not generally imply such syndetic return times.

The next audit should construct the exact countermodel or determine which additional property of the Navier--Stokes recurrent hull could upgrade positive density/mean occupation to a uniform fixed-window observation inequality.

---

\[
\boxed{\text{M19-080 COMPLETE.}}
\]
