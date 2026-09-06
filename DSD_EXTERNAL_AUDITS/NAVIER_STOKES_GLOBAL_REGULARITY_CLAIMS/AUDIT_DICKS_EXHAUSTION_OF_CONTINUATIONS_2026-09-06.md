# DSD Audit — Dicks Exhaustion of Continuations

Date: 2026-09-06
Source: Rollo Stanley Dicks, *Global Regularity of the Three-Dimensional Incompressible Navier-Stokes Equations via Exhaustion of Continuations*, Zenodo 18963533, Mar 2026.
Audit status: **POST-SINGULAR CONTINUATION NON-SEQUITUR**

## 1. Claimed contradiction architecture

The paper assumes a finite first singular time `T_*`, then studies possible post-singularity enstrophy/weak continuations. It argues that a post-singularity state cannot be uniquely selected without violating nonnegative enstrophy, the Leray energy inequality, deterministic selection, adjoint structure, or directional-alignment constraints. The asserted conclusion is that the singular time cannot occur.

## 2. DSD timeline separation

The Clay regularity question asks whether a classical/smooth solution can cease to be smooth at finite time.

A hypothetical singular solution may have:

\[
\text{smooth evolution on }[0,T_*)
\]

and fail to possess a classical continuation through `T_*`.

There is no requirement in the problem statement that a singularity must be followed by:

- a unique classical continuation;
- a deterministic branch selection;
- a continuation preserving a chosen enstrophy topology;
- a well-posed adjoint across the singular point.

Therefore

\[
\boxed{
\text{post-singular continuation failure/nonuniqueness}
\not\Rightarrow
\text{pre-singular regularity}.
}
\]

## 3. Weak-solution distinction

Leray–Hopf weak solutions exist globally, but global weak existence does not supply uniqueness or smoothness. A first singular time of a strong solution can in principle be followed by one or more weak continuations, or by a weak state whose fine variables are not classically defined.

Showing that a desired strong continuation cannot be selected uniquely is therefore compatible with, rather than contradictory to, finite-time breakdown of the strong solution.

## 4. Deterministic-selection audit

“Deterministic selection” is an additional requirement unless derived from the classical NSE in the relevant weak class. Weak-solution nonuniqueness phenomena are precisely a warning that determinism of arbitrary post-singular weak continuation cannot be assumed as a regularity axiom.

To use deterministic selection as a contradiction, the proof would first need a theorem:

\[
\text{every finite-time singularity necessarily admits a unique admissible post-singular state}.
\]

Such a theorem would itself be a major well-posedness result and is not supplied merely by energy/enstrophy nonnegativity.

## 5. Adjoint failure audit

Failure of an adjoint equation or dual representation at a singular time can diagnose loss of regularity. It does not reverse the implication automatically. The logic

\[
\text{singularity}\Rightarrow\text{adjoint failure}
\]

is fully compatible with a singularity. One needs an independent theorem saying the adjoint must remain valid across `T_*` for every admissible NSE evolution to derive a contradiction.

## 6. Surviving value

Continuation classification can still be useful for:

- weak-solution selection problems;
- admissibility criteria;
- enstrophy branching after loss of smoothness;
- identifying which structural quantities fail at a hypothetical singularity.

Those are meaningful questions distinct from proving that the singularity is impossible.

## 7. DSD verdict

The proof changes the obligation from

\[
\text{can smoothness fail at }T_*?
\]

to

\[
\text{can a uniquely deterministic post-}T_*\text{ continuation be chosen?}
\]

without proving equivalence of those questions.

\[
\boxed{
\text{The continuation-exhaustion contradiction is therefore not established.}
}
\]

Global regularity remains unproved.
