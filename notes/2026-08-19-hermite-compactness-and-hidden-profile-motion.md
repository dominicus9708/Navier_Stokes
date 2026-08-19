# Hermite compactness and covariance-invisible profile motion

Date: 2026-08-19

Status: **DERIVED FINITE-HERMITE COMPACTNESS GATE + DYNAMIC ENSTROPHY SCALE-DAMPING LEDGER / GLOBAL REGULARITY NOT PROVED**.

This note addresses a loophole left after the projective covariance analysis: a normalized profile can move while its low-order covariance stays nearly fixed.

---

## 1. Gaussian Hermite decomposition

Let

\[
d\gamma(y)=(2\pi)^{-3/2}e^{-|y|^2/2}dy
\]

and let `Pi_n` denote projection onto total Hermite degree `n` in `L^2(gamma)`.

For a scalar or vector field `f`, write

\[
f=\sum_{n\ge0}f_n,
\qquad f_n=\Pi_nf.
\]

The Ornstein--Uhlenbeck number operator has eigenvalue `n` on degree `n`, so the Gaussian Dirichlet form gives

\[
\boxed{
\|\nabla f\|_{L^2_\gamma}^2
=\sum_{n\ge1}n\|f_n\|_{L^2_\gamma}^2.
}
\]

Consequently, for every integer `N>=1`,

\[
\boxed{
\|\Pi_{\ge N}f\|_{L^2_\gamma}^2
\le
\frac1N\|\nabla f\|_{L^2_\gamma}^2.
}
\]

Thus the high-Hermite tail has an exact `1/N` compactness gain.

If a second Hermite/derivative energy is bounded, one similarly obtains an `H^1_gamma` tail gain of order `1/N` from the weighted sum `n(n-1)||f_n||^2`.

---

## 2. Finite-dimensional low-mode compactness

Suppose a normalized sequence `f_j` has

\[
\sup_j\|f_j\|_{L^2_\gamma}<\infty,
\qquad
\sup_j\|\nabla f_j\|_{L^2_\gamma}\le M.
\]

For fixed `N`, the space

\[
\Pi_{<N}L^2_\gamma
\]

is finite dimensional. Hence any bounded sequence has a subsequence on which all coefficients of degrees `<N` converge.

For two elements of that subsequence,

\[
\|f_j-f_k\|_{L^2_\gamma}
\le
\|\Pi_{<N}(f_j-f_k)\|_{L^2_\gamma}
+\frac{2M}{\sqrt N}.
\]

Taking first `j,k -> infinity` and then `N -> infinity` yields strong `L^2_gamma` compactness.

Therefore covariance-invisible oscillation of a tight sequence cannot destroy all profile compactness unless the Gaussian derivative/Hermite tail loses control.

This is simply an explicit Hermite realization of Rellich compactness, but it matches the repository's existing high-chaos bookkeeping.

---

## 3. Consequence for the reduced proof tree

A first-hitting sequence avoiding both:

- high-Hermite / derivative escape `H`, and
- spatial non-tightness `T`,

cannot use arbitrarily high hidden modes to keep changing shape while every fixed finite set of low Hermite coefficients settles.

After a diagonal subsequence, either:

1. the normalized profile is strongly compact in the Gaussian core;
2. some finite set of low modes keeps moving by an O(1) amount;
3. the high-Hermite tail loses its uniform derivative bound.

The third case is `H`. The first feeds the frozen/recurrent-profile compactness route. The second is a finite-dimensional phase/turnover channel rather than an untyped covariance loophole.

---

## 4. Low-mode shape action

For normalized vorticity `Omega(s)`, define the finite mode vector

\[
Z_N(s)=\Pi_{<N}\Omega(s).
\]

Its total variation on an interval `I` is

\[
\boxed{
\mathcal A_N(I)
=\int_I\|\partial_s Z_N(s)\|_{L^2_\gamma}ds.
}
\]

Then

\[
\boxed{
\|Z_N(s_1)-Z_N(s_0)\|_{L^2_\gamma}
\le\mathcal A_N([s_0,s_1]).
}
\]

Thus an O(1) covariance-invisible phase change in any fixed finite Hermite sector requires an O(1) low-mode shape action.

Using the dynamic normalized vorticity equation,

\[
\partial_s\Omega
=S_U\Omega-(U-c)\cdot\nabla\Omega+\nu\Delta\Omega
-a(2\Omega+y\cdot\nabla\Omega),
\]

this action is supplied only by:

- stretching/derivative source;
- material advection/turnover;
- viscous mode transfer;
- the scale generator `a(2+y dot grad)`.

Therefore low-mode motion is a typed channel and cannot be treated as an invisible reorganization.

A global summability estimate for `A_N` is not yet proved.

---

## 5. Dynamic normalized enstrophy equation

Let

\[
E=\|\Omega\|_2^2,
\qquad
P=\|\nabla\Omega\|_2^2.
\]

The dynamic scaling gives the exact enstrophy identity

\[
\boxed{
\frac12E'
+\frac a2E
+\nu P
=\int S_U\Omega\cdot\Omega\,dy.
}
\]

The extra term

\[
\boxed{\frac a2E}
\]

is the dissipation-like cost created by continuously renormalizing the vorticity maximum to one.

---

## 6. Middle-strain defect in dynamic variables

Let `Lambda_2^+` be the positive middle eigenvalue of the normalized strain `S_U`. The exact determinant defect and Sobolev estimate give

\[
\boxed{
\frac12E'
+\frac a2E
+4\|\Lambda_2^+\|_3^3
\le
\left(C_S\|\Lambda_2^+\|_{3/2}-\nu\right)P.
}
\]

On a geometric scale-growth stage `I_j`,

\[
\int_{I_j}a(s)ds=\frac12\log q.
\]

If the normalized enstrophy satisfies `E>=e0>0`, then

\[
\boxed{
\frac12\int_{I_j}aE\,ds
\ge
\frac{e_0}{4}\log q.
}
\]

Hence every geometric scale increase requires a fixed amount of middle-strain excess/palinstrophy production even if the normalized profile returns to the same enstrophy at the end of the stage.

This scale-damping cost is absent from a fixed-terminal-scale normalization and is therefore a useful new ledger for the packing problem.

---

## 7. Integrated stage form

Let

\[
\mathfrak E_M(s)=C_S\|\Lambda_2^+(s)\|_{3/2}-\nu.
\]

For a stage `I=[s_0,s_1]`,

\[
\boxed{
\frac12(E(s_1)-E(s_0))
+\frac12\int_IaE\,ds
+4\int_I\|\Lambda_2^+\|_3^3ds
\le
\int_I\mathfrak E_M P\,ds.
}
\]

If `E(s_1)` and `E(s_0)` are comparable and `E>=e0`, the right-hand side must pay a fixed positive amount per scale step.

Therefore a recurrent normalized profile cannot be maintained by exact scale repetition without repeatedly activating the critical middle-strain/palinstrophy channel.

This is a scale-critical action statement, not yet a contradiction with an a-priori finite global budget.

---

## 8. Compact recurrent limit versus stationary limit

Hermite compactness at terminal snapshots does not by itself prove that the limiting normalized evolution is stationary. A compact survivor may converge, after shifts in rescaled time, to:

- a stationary profile;
- a periodic/discretely self-similar orbit;
- a rotated orbit;
- a more general compact recurrent trajectory.

The stationary positive-scale-rate and zero-scale-rate limits are routed to existing backward-self-similar and steady Liouville theorems under their hypotheses.

The genuinely new unresolved compact object is therefore a nonstationary recurrent orbit in dynamic first-hitting variables.

The next target is to determine whether the fixed scale-damping action, finite-Hermite shape action, and projective covariance action can provide a Lyapunov/packing obstruction to such recurrent compact trajectories.

Status: **HIGH-HERMITE HIDDEN MOTION REDUCED BY 1/N TAIL; LOW-MODE MOTION TYPED AS FINITE-DIMENSIONAL ACTION; DYNAMIC SCALE NORMALIZATION ADDS A FIXED MIDDLE-STRAIN PRODUCTION COST PER GEOMETRIC SCALE STEP; COMPACT NONSTATIONARY RECURRENT ORBIT IS THE REMAINING SHAPE-PERSISTENCE LOophole.**