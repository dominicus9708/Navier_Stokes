# DSD Audit — Permana / Ibrahim / Lathief Geometric Depletion and Third Topological Invariant

Date: 2026-09-06
Source family: SSRN 6557718; Zenodo 19632058 and associated revisions.
Audit status: **CONDITIONAL FRAMEWORK; UNCONDITIONAL CLOSURE NOT DERIVED**

## 1. Why this family is treated differently

The manuscript contains explicit labels identifying several decisive statements as hypotheses. This is a positive feature for auditability. The correct DSD classification is therefore not “all mathematics false,” but rather:

\[
\boxed{\text{the framework remains conditional on strong unresolved gates}.}
\]

## 2. TAH — Turbulence Alignment Hypothesis

The text assumes, on the high-vorticity extensional domain, a globally dominant damping relation of the form

\[
\int 2\alpha\kappa^p\,dx
\ge C_{damp}\int |\omega|\kappa^p\,dx,
\]

where `α=<ξ,Sξ>` and `κ` encodes directional curvature.

The paper itself says this hypothesis is necessary to uniformly close the Lp energy estimate and motivates it by turbulence phenomenology.

DSD status: **not an unconditional NSE theorem.** A geometric-alignment tendency observed in turbulence cannot be promoted to an all-smooth-data inequality without proof, especially because the sign of `α` can vary spatially.

## 3. DGMICH — degenerate Moser iteration

The manuscript assumes that the weight

\[
\frac{\nu}{|\omega|}
\]

belongs to a Muckenhoupt `A_2` class on the active domain and therefore supports the required Moser iteration.

This is exactly a nontrivial regularity/geometric condition in high-vorticity regions. As `|ω|` increases the coefficient degenerates. Standard uniformly elliptic De Giorgi–Nash–Moser theory cannot simply be invoked without the stated weighted hypotheses and uniform constants.

DSD status: **CONDITIONAL_ONLY** unless the A2 property is derived from NSE data independently of the desired conclusion.

## 4. TICH — nonlinear cancellation in the Third Topological Invariant

The later revision defines

\[
T^3(t)=\int_{\mathbb T^3}|\nabla\times(\omega\times u)|^2dx
\]

and assumes that nonlinear convective/stretching contributions to `dT^3/dt` combine into an exact spatial divergence on the torus.

The paper explicitly states that the cubic and pressure residual cancellation is a highly nontrivial open conjecture and that the exponential damping lemma is conditional on this assumption.

Under TICH, the paper derives a spectral-gap decay

\[
T^3(t)\le T^3(0)e^{-2\nu\Lambda t}.
\]

But this conclusion cannot be used to prove the hypothesis which produced it.

DSD dependency:

\[
\boxed{
TICH\Rightarrow T^3\text{ damping},
\quad
T^3\text{ damping}\not\Rightarrow TICH.
}
\]

## 5. Topological Damping Link

The manuscript additionally postulates a bound linking the curvature constant/higher Sobolev control to `T^3` and energy. This is another bridge from the introduced invariant to the classical regularity norm and requires an independent proof.

## 6. Transport-strain calculation

The manuscript writes a formal curvature equation whose diffusive part has coefficient `ν/|ω|`, then closes Lp estimates using TAH and DGMICH. Even accepting the formal differentiation, the estimate is therefore explicitly conditional.

One version also states that intense vorticity alignment with an extensive/intermediate strain eigenvector makes the positive damping integral dominate. Such a dominance is not a deterministic consequence of `tr S=0`.

## 7. Version-history significance

Some revisions describe a conditional pathway, while related records use stronger “quantitative resolution/global smoothness” language. For audit purposes, the most explicit mathematical version controls the classification: the presence of TAH, DGMICH, TICH, and the Topological Damping Link means the chain is conditional until those gates are discharged.

## 8. Surviving value

This family contributes a useful explicit hypothesis ledger:

- high-vorticity direction-domain isolation;
- weighted degenerate curvature evolution;
- a proposed topological current;
- spectral-gap damping conditional on exact nonlinear cancellation;
- a Kato/Fujita-style bootstrap after a global H1 bound.

Those can be tested individually without accepting the global claim.

## 9. DSD verdict

\[
\boxed{
\text{Conditional sufficient-structure program, not an unconditional resolution.}
}
\]

The most valuable next external test would be a standalone proof or counterexample for TICH and the A2 property of `ν/|ω|`.

Global regularity remains unproved.
