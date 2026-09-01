# DSD M5-459 — Scope audit for transferring ancient weak-L3 Liouville machinery to the metric system

Date: 2026-09-01

Status: **THE EXISTING ALBRITTON--BARKER THEOREM 4.1 CANNOT BE APPLIED VERBATIM TO THE M5-451 METRIC COVECTOR SYSTEM / HOWEVER THE PRINCIPAL-PART OBSTACLES ARE SUBSTANTIALLY REDUCED: THE METRIC HEAT PROPAGATOR IS EXPLICIT WITH STANDARD CRITICAL SMOOTHING, AND GENERAL BACKWARD-UNIQUENESS THEORY COVERS UNIFORMLY PARABOLIC VARIABLE PRINCIPAL COEFFICIENTS UNDER APPROPRIATE TIME REGULARITY / THE GENUINE MISSING THEOREM IS A METRIC ANALOGUE OF THE WEAK-`L^{3,INFINITY}` STABILITY + TERMINAL BESOV PERTURBATION PACKAGE / GLOBAL REGULARITY REMAINS UNPROVED.**

## 1. External theorem actually used in the isotropic branch

Albritton--Barker, *On local Type I singularities of the Navier-Stokes equations and Liouville theorems*, Theorem 4.1, assumes a mild ancient **standard Navier--Stokes** solution `v` with

\[
\|v(t_k)\|_{L^{3,\infty}}\le M
\]

along `t_k -> -infinity` and terminal datum sufficiently close in `dot B^{-1}_{infinity,infinity}` to their subspace `B`. The proof uses their weak-`L^{3,infinity}` solution stability and a terminal regularity proposition, itself based on the standard Navier--Stokes weak/Besov theory and backward uniqueness.

Therefore M5-276/388 may invoke that theorem only for a genuine standard-NS ancient orbit.

## 2. Why direct invocation fails after M5-451

The bounded-metric pullback obeys

\[
\partial_t\eta-\nabla\cdot(G(t)\nabla\eta)
=\nabla\cdot(\eta\otimes w-w\otimes\eta),
\]

\[
\eta=\nabla\times(C(t)w),
\qquad C=G^{-1}.
\]

Even when `G,C` are uniformly elliptic, this is not literally the standard Navier--Stokes system. In particular:

- the velocity-vorticity law depends on time through `C(t)`;
- the natural linear propagator is `P_G(t,s)`, not the standard Stokes semigroup;
- a Navier scaling of an ancient solution also rescales/translates the coefficient history `G(t)`;
- the weak-`L^{3,infinity}` stability theory quoted in Albritton--Barker is stated for standard NS.

Hence the theorem cannot be imported by notation change.

## 3. What does transfer automatically

M5-457 gives

\[
\widehat{P_G(t,s)f}(\xi)
=
\exp\left[-\int_s^t\xi^TG(\tau)\xi d\tau\right]\widehat f(\xi).
\]

Uniform ellipticity gives all standard heat/Stokes scaling exponents. M5-452 gives a uniform metric Biot--Savart/CZ inverse. Thus the small-data and mild-bilinear estimates in critical Lorentz/Besov spaces have the same dimensional exponents, with constants depending on the ellipticity ratio and coefficient regularity.

General backward-uniqueness theory for uniformly parabolic operators also allows variable principal coefficients under suitable time regularity (for example the Del Santo--Prizzi line of results). Since our principal matrix is spatially constant, it lies in a substantially more rigid class than general variable-coefficient operators.

Therefore the principal heat operator itself is not the main gap.

## 4. Genuine missing package

To reproduce Albritton--Barker's contradiction one still needs a theorem containing all of the following in one compatible metric class:

1. weak-`L^{3,infinity}` initial-value solutions for the metric covector system;
2. stability under weak-* initial-data convergence and coefficient convergence `G_k -> G_infinity`;
3. critical Besov splitting/perturbation with the metric propagator `P_G`;
4. local compactness strong enough to preserve singularity/nontriviality under rescaling;
5. terminal regularity from a small `dot B^{-1}_{infinity,infinity}` metric datum;
6. backward uniqueness for the resulting vorticity equation.

Items 3 and 6 have strong existing analogues/ingredients; items 1--2--4--5 are not established in the repository for the time-dependent metric system.

## 5. Correct branch status

Thus the uniformly elliptic recurrent lane is best typed as

\[
\boxed{
L_{metric}^{ancient}
}
\]

with an explicit finite theorem gap, rather than as an already closed `W1` Liouville branch.

The external theorem remains a model/target and must be cited, but not silently extended.

## 6. Highest-value internal next step

Because the metric coefficients are finite-dimensional and spatially constant, the most efficient next step is to prove coefficient compactness under ancient time translations and then establish a metric mild-solution stability lemma using the explicit `P_G` kernel.

That would reduce the missing package to the terminal Besov regularity/backward-uniqueness stage.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]