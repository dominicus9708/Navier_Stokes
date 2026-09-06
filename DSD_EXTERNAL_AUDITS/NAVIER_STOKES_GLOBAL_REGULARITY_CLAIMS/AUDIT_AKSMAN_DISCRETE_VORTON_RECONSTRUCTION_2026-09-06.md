# DSD Audit — Aksman Discrete Vorticity–Vorton / Uniform Spectral Closure

Date: 2026-09-06
Source: Mikhail I. Aksman, *GLOBAL REGULARITY OF THE 3D NAVIER–STOKES EQUATIONS — Discrete Vorticity–Vorton Dynamics, Uniform Spectral Closure, and Continuum Regularity*, Aug 2026.
Audit status: **CONDITIONAL THEOREM; CONTINUUM BRIDGE ASSUMES THE CRITICAL UNIFORM CONTROL**

## 1. Displayed theorem

The manuscript states a `Uniform Spectral Closure` theorem for shape-regular simplicial refinements `K_h`, under five explicit hypotheses:

1. uniform global discrete energy bound;
2. uniform discrete vorticity `L^2→L∞` estimate;
3. uniformly stable reconstruction operators `R_h`;
4. reconstruction error tends to zero in the required Sobolev topology;
5. nonlinear consistency with incompressible Navier–Stokes.

It then concludes

\[
\sup_{0\le t\le T}\|\omega(t)\|_{L^\infty}<\infty
\]

and invokes BKM.

## 2. Logical form

The proof uses

\[
\|\omega\|_\infty
\le
\|\omega-R_h\omega_h\|_\infty
+
\|R_h\omega_h\|_\infty.
\]

Hypotheses 2–3 supply a uniform bound for the second term; Hypothesis 4 is invoked to make the first term vanish.

As an implication, this is structurally correct:

\[
\boxed{
\text{uniform L∞ reconstruction + L∞ convergence}
\Rightarrow
\text{continuum L∞ bound}.
}
\]

The global-regularity problem is therefore displaced into proving those uniform hypotheses.

## 3. Mesh-scaling audit

For ordinary finite-element/Whitney-type spaces in three dimensions, inverse estimates carry mesh dependence. A localized shape function with support volume `~h^3` can have

\[
\|v_h\|_2\sim h^{3/2}\|v_h\|_\infty,
\]

so generally

\[
\|v_h\|_\infty
\lesssim h^{-3/2}\|v_h\|_2.
\]

Shape regularity controls distortion constants but does not eliminate the dimensional factor `h^{-3/2}`.

Thus

\[
\sup_h C_h<\infty
\]

for a general L2-to-L∞ reconstruction estimate is not a consequence of finite dimensionality or shape regularity.

## 4. Reconstruction-error topology audit

To send

\[
\|\omega-R_h\omega_h\|_\infty\to0,
\]

one needs a convergence topology embedding into L∞ with constants uniform in h, or a direct L∞ convergence theorem.

A generic `H^1` or energy convergence does not give this in 3D. A sufficiently strong uniform Sobolev convergence hypothesis is already a substantial continuum regularity statement.

Hence the phrase “reconstruction error converges to zero in the required Sobolev topology” must be expanded into explicit norms/constants before it can serve as a proof bridge.

## 5. Finite-spectrum audit

Every fixed discrete complex has finite spectrum and finite-dimensional norm equivalence. But

\[
\boxed{
\forall h:\ C_h<\infty
\not\Rightarrow
\sup_h C_h<\infty.
}
\]

The latter is exactly the refinement-uniform statement needed to pass to a smooth continuum solution.

## 6. DSD verdict

The displayed theorem is best classified as a **conditional transfer theorem**:

\[
\boxed{
(H2)+(H3)+(H4)\Rightarrow BKM.
}
\]

It is not by itself a derivation of `(H2)–(H4)` from discrete topology.

If the manuscript supplies an independent h-uniform proof avoiding the standard inverse-scaling obstruction, that proof is the true core and must be audited separately. Until then, “finite discrete spectrum ⇒ continuum L∞” is not established.

Global regularity remains unproved.
