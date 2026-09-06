# DSD External Audit Registry — Claimed 3D Navier–Stokes Global-Regularity Resolutions (2025–2026)

Date: 2026-09-06
Repository: dominicus9708/Navier_Stokes
Scope: external manuscripts/preprints/repositories explicitly claiming a complete proof, unconditional global regularity, or an equivalent resolution/independence result for the classical 3D incompressible Navier–Stokes Millennium Problem.

## Audit rule

This registry evaluates arguments, not authors. Academic rank, affiliation, publication venue, tone, and numerical evidence are not proof currencies. Every family is separated into:

- CLAIM: what the manuscript says it proves.
- HINGE: the step on which the global conclusion depends.
- AUDIT: whether that hinge is derived from prior hypotheses.
- SURVIVOR: any conditional theorem, calculation, numerical observation, or structural lemma that remains potentially useful even if the global claim fails.
- STATUS: `CORE_HINGE_FAIL`, `CONDITIONAL_ONLY`, `SCOPE_MISMATCH`, `OPEN_DEEP_AUDIT`, or `SURVIVES_CURRENT_AUDIT`.

A failed global closure does **not** imply that every lemma in a manuscript is false.

The external reference baseline remains that the Clay Mathematics Institute lists Navier–Stokes as unsolved as of 2026-09-06.

---

## A. Deep-audited / decisive hinge identified

### A1. Joseph Thomas Cox — Critical-endpoint/APMS minimal-element rigidity
Source family: *Resolving Global Regularity for the 3D Navier–Stokes Equations at the Critical Endpoint*, DOI family including 10.5281/zenodo.17503936.

Claim: unconditional global regularity through a Kenig–Merle-style minimal ancient precompact L3 element (APMS), followed by Type-I/Carleman rigidity.

Decisive hinge: Theorem G.5 defines

\[
M_*:=\inf\{M>0:\exists u\text{ suitable with }\sup_{t<T(u)}\|u(t)\|_3>M\}
\]

and then selects finite-time sequences whose L3 suprema decrease to a positive `M_*`, extracting a nonzero APMS.

DSD audit: as written, this set does not define a positive minimal blow-up threshold. If arbitrary suitable solutions are admitted, any nontrivial solution makes the condition true for all sufficiently small positive M, hence the infimum is 0. If `T(u)` is intended to be a finite singular time, the critical L3 regularity theorem implies a hypothetical singular solution cannot have a finite uniform L3 bound; again the displayed threshold does not produce a finite positive minimal element. The subsequent APMS extraction therefore consumes a property not established by the definition.

Status: **CORE_HINGE_FAIL at KL-1/minimal-element construction.** Later pressure, Carleman, and constants-ledger modules are not thereby individually refuted, but they do not close global regularity without a valid nonzero critical element.

### A2. Luca Eliseo Pavesi — Geometric frustration / helical quasi-trapping
Source family: *Global Regularity ... via Geometric Frustration and Helical Quasi-Trapping*, Zenodo 21158572/21172740/21194906; conditional predecessor Zenodo 21113042.

Claimed unconditional hinge:

\[
|\Pi(K,t)|\le C_*\,E_{>K}(t)^{1/2}E(t)^{1/2}/K
\]

for every smooth solution and every K, with absolute `C_*` independent of the data.

DSD audit 1 — homogeneity: replacing smooth divergence-free initial data by `A u_0` at the same instant scales the nonlinear energy flux cubically (`A^3`) whereas the displayed right-hand side scales quadratically (`A^2`). For any datum/configuration with nonzero flux, an absolute data-independent constant cannot make the estimate valid for arbitrarily large A.

DSD audit 2 — Fourier support: the proof states that fields supported above K are essentially cross-closed because dominant triads are comparable and leakage below K is `O(1/K)`. High frequencies are not support-closed under convolution: p and q can both be arbitrarily large with q approximately `-p+k`, producing arbitrarily small output k. Support geometry alone supplies no universal `1/K` suppression. Statistical/angular averaging is also not deterministic cancellation for arbitrary Fourier phases.

Status: **CORE_HINGE_FAIL for unconditional Theorem 6.1.** The earlier helicity-dominance result remains a **CONDITIONAL_ONLY** statement and should not be discarded merely because the unconditional upgrade fails.

### A3. Mikhail/Michael Aksman — Discrete vorticity-vorton / Uniform Spectral Closure
Source family: *Discrete Vorticity–Vorton Dynamics, Uniform Spectral Closure, and Continuum Regularity* (Aug 2026).

Claim: finite discrete spectrum plus uniformly stable reconstruction yields continuum L-infinity vorticity control and BKM continuation.

Displayed theorem explicitly assumes, among other items:
1. uniform discrete energy;
2. a uniform discrete L2-to-L∞ vorticity estimate;
3. uniformly stable reconstruction;
4. reconstruction error vanishing in the Sobolev topology strong enough to control the L∞ difference;
5. nonlinear consistency.

DSD audit: the conclusion

\[
\sup_{t\le T}\|\omega(t)\|_{\infty}<\infty
\]

is obtained precisely by assuming the uniform discrete/reconstruction estimates that must survive `h→0`. In three dimensions, ordinary shape-regular finite-element/Whitney inverse estimates have mesh factors of the form `h^{-3/2}` for L2-to-L∞ control; finite dimensionality at each h does not provide an h-uniform continuum bound. Shape regularity does not remove this dimensional scaling. Likewise, convergence in a generic Sobolev topology is insufficient for L∞ error unless the topology and constants are strong enough, which again encodes the needed continuum regularity.

Status: **CONDITIONAL_ONLY / CIRCULAR_CONTINUUM_BRIDGE.** The theorem is a valid implication if its uniform hypotheses are proved independently; the manuscript's claim that finite discrete topology itself proves them is not established by the displayed theorem.

### A4. Mikhail/Michael Aksman — Exact vorton decomposition / Uniform Core Exclusion
Source family: *A Rigorous Proof via Exact Vorton Decomposition, Uniform Core Exclusion, and the Fredholm Boundary Anchor*, Zenodo family 21070611/21084689/21132549/21169188.

Claim: exact vorton representation establishes a fixed positive UV cutoff at the Kolmogorov microscale `δ_K`, prevents vorton collision, and yields a uniform H1 bound on a punctured domain, then continuum regularity.

DSD audit: a fixed strictly positive `δ_K` is not a known invariant lower bound of arbitrary classical Navier–Stokes solutions. If retained during refinement it prevents the representation from resolving structures below that scale, so density in the full classical solution space is not automatic. If `δ_K→0` is allowed to recover arbitrary continuum scales, estimates whose constants depend on the puncture/core radius can diverge. A uniform H1 bound only on the punctured domain does not by itself control the excluded cores. Treating turbulence-scale phenomenology as a universal lower-scale theorem changes the hypothesis class.

Status: **CORE_HINGE_FAIL / SCALE-LIMIT INCOMPATIBILITY** unless a data-independent continuum theorem establishing the positive cutoff is supplied.

### A5. Amarachukwu Nwankpa — Coherence Manifold / Logic of Fluids
Source: *The Logic of Fluids: Coherence and Regularity in the Navier–Stokes System*, Preprints.org 202506.2259 v4.

Claim: Leray–Hopf energy plus interpolation preserves `L^2∩L^3`, provides a uniform-in-time critical L3 bound, then ESS regularity/uniqueness.

Decisive hinge: the proof derives the L3 differential inequality by testing the momentum equation with the L3 multiplier and states that the pressure term vanishes by incompressibility.

DSD audit: for the natural L3 test `|u|u`,

\[
\int \nabla p\cdot |u|u
=-\int p\,\nabla\cdot(|u|u),
\]

and `div u=0` does not imply `div(|u|u)=0`. The pressure term therefore does not vanish on that ground. In addition, time-integrated L3-type control obtained by interpolation does not imply a uniform `L_t^∞L_x^3` bound.

Status: **CORE_HINGE_FAIL.** The functional-space observations may remain descriptive, but the rigidity lemma needed for ESS is not established.

### A6. Felipe Gaspar Gomes de Carvalho — NTG algebra
Source: *An Algebraic Reformulation ... via the NTG Algebra*, Aug 2026, DOI 10.13140/RG.2.2.29020.55689.

Definition used:

\[
A\star B=AB-\frac13\operatorname{tr}(AB)I.
\]

For `G=∇u`, the exact gradient equation is

\[
D_tG+G^2=-\nabla^2p+\nu\Delta G,
\qquad \Delta p=-\operatorname{tr}(G^2).
\]

Writing

\[
G^2=G\star G+\frac13\operatorname{tr}(G^2)I,
\]

and decomposing the pressure Hessian into deviatoric plus isotropic parts cancels the isotropic pieces and leaves coefficient **1** in front of `G⋆G`:

\[
D_tG+G\star G=-P_{dev}+\nu\Delta G.
\]

The manuscript's downstream cubic evolution displays the coefficient corresponding to `3/2 G⋆G` (the term `-9/2 ∫ tr(G^2(G⋆G))`). Under the stated star-product definition this coefficient is inconsistent with the exact differentiated Navier–Stokes equation.

Status: **CORE ALGEBRA HINGE FAIL.** Downstream sharp-correlation/dissipativity constants must be recomputed from the correct base equation before the regularity conclusion can be assessed.

### A7. Bryan P. Permana, Sage A. Ibrahim, Hanif A. Lathief — geometric depletion / Third Topological Invariant
Source family: SSRN 6557718; Zenodo 19632058 and revisions.

The later full text explicitly introduces:
- TAH (Turbulence Alignment Hypothesis), needed to dominate the curvature energy;
- DGMICH, assuming the degenerate weight `ν/|ω|` lies in Muckenhoupt `A_2` and supports the required Moser iteration;
- Topological Damping Link, assumed to connect higher Sobolev control to `T^3`;
- TICH, assuming all nonlinear terms in the `T^3` evolution are exact spatial divergences and hence vanish globally.

The paper itself states that verification of TICH is contingent on the assumption and that the required cubic/pressure cancellation is a nontrivial open conjecture. Therefore an unconditional global-regularity conclusion cannot consume TICH/TAH/DGMICH as already-proved facts.

A separate warning: the displayed curvature equation uses the degenerate coefficient `ν/|ω|`; standard De Giorgi–Nash–Moser iteration is not automatically uniformly elliptic in precisely the high-vorticity regime unless the stated weighted hypotheses are proved.

Status: **CONDITIONAL_ONLY, not unconditional resolution.** This family is useful as an explicit map of sufficient hypotheses; those hypotheses are themselves substantial open gates.

### A8. Rollo Dicks — Exhaustion of Continuations
Source: Zenodo 18963533, *Global Regularity ... via Exhaustion of Continuations*.

Claim: assuming a finite singular time, all post-singularity continuations are incompatible with enstrophy nonnegativity, Leray energy inequality, deterministic selection, or alignment/adjoint constraints; therefore the singularity cannot occur.

DSD audit: the classical smoothness problem does not require a hypothetical singular solution to possess a unique deterministic classical continuation beyond its first singular time. Failure, nonuniqueness, or underdetermination of a post-singular continuation is not a contradiction with the existence of a singularity at the endpoint of the classical interval. To turn continuation exhaustion into a blow-up exclusion theorem, one must first prove that a singularity necessarily admits one of the postulated continuation classes and that uniqueness/deterministic selection is a theorem of the original problem rather than an added axiom.

Status: **SCOPE / LOGICAL NON-SEQUITUR at continuation-to-regularity gate.**

### A9. Christopher Pompetzki — claimed ZFC independence
Source family: Zenodo 18292041/18292042, Jan 2026.

Claim: regularity is independent of ZFC because existing energy methods fail to close, while a blow-up proof would relativize to hyperdissipative equations and contradict their known regularity.

DSD audit: failure of a class of analytic methods does not imply formal unprovability in ZFC. Independence requires a metamathematical relative-consistency/model-theoretic argument, not a barrier analogy. There is also no theorem that any proof of blow-up for the standard exponent `α=1` must transfer to nearby or larger hyperdissipation exponents. The manuscript additionally treats 3D Euler singularity as settled in the motivating analogy, whereas general smooth 3D Euler finite-time blow-up remains open.

Status: **CORE LOGIC CATEGORY ERROR / NOT AN INDEPENDENCE PROOF.**

---

## B. High-risk first-pass audits; full-text hinge audit still required

### B1. Brad Bledsoe — Coherence Functional
Source: SSRN 5575415 / 6393402.
Abstract states a universal discount of the form

\[
\int ((\omega\cdot\nabla u)\cdot\omega)|\omega|\,dx
\le (1-\delta)\|\omega\|_3^3.
\]

As written, the left-hand side is homogeneous of degree four in the amplitude of u whereas the right-hand side is degree three. A data-independent positive `δ` cannot support this exact unnormalized inequality under `u→Au`. **Status: HIGH-RISK SCALING FAILURE IN ABSTRACTED FORM; verify the manuscript's exact normalization before a final verdict.**

### B2. SAPZ Singularity Principle / spectral trace-energy family
Source family includes Zenodo 15846589 and numerous later revisions.
Historical audit flag: early versions claim complete unconditional resolution; later versions in the same program explicitly isolate a remaining PDE completion target before still later versions claim to discharge it. This version history is important evidence that the early “complete” closure was not stable under self-audit. **Status: OPEN_DEEP_AUDIT of the latest Route-T/closure theorem; older complete-claim versions should be tagged superseded/incomplete where the authors later acknowledge a missing hinge.**

### B3. Hiroaki Onodera — Fully Constructive Closure
Source: Zenodo 15605345 and associated repository.
Abstract-level hinge includes high-order induction, Riccati concentration control, and “real-time stability monitoring.” The audit must determine whether the monitoring rule is an a priori theorem of every classical NSE trajectory or an adaptive/control procedure not present in the original PDE. **Status: OPEN_DEEP_AUDIT.**

### B4. Stough 2025 — φ-resonant decomposition
Source: Zenodo 15335698/15335699.
Claimed universal cancellations and uniform high-Sobolev bounds. Required audit: amplitude/scaling of nonlinear multiplier estimates, completeness of resonant/nonresonant decomposition, and whether the key cancellation is deterministic for arbitrary phase configurations. **Status: OPEN_DEEP_AUDIT.**

### B5. Global Bridge / projection-API family
Source: Zenodo 16784408 and related Global Bridge records.
Claim uses an inductive-limit holomorphic host space, projection architecture, and scheduler contractivity. Required audit: prove exact equivalence to the original classical NSE and that contractive scheduling is a consequence of the PDE, not an externally chosen regularization/projection procedure. **Status: OPEN_DEEP_AUDIT / MODEL-EQUIVALENCE GATE.**

### B6. Hannes Graah — thick/tube/fragmented trichotomy
Source family: Zenodo 18132364/18132365.
Claim: every possible blow-up scale belongs to a complete geometric trichotomy and every branch pays scale-invariant dissipation; packing disjoint intervals contradicts energy. Required audit: completeness of the trichotomy, uniform positive time fraction, and non-overcounting/disjointness of the dissipation ledger. **Status: OPEN_DEEP_AUDIT; potentially close in philosophy to the current M17 branch-pruning work and therefore high comparison priority.**

### B7. Emergent Nonlinear Vorticity Dissipation family
Source: Zenodo 15801527/15801528.
Claim: directional decomposition creates an intrinsic nonlinear damping mechanism suppressing stretching. Required audit: exact sign/coercivity identity, amplitude/scaling, and whether a conditional alignment assumption is silently promoted to universal. **Status: OPEN_DEEP_AUDIT.**

### B8. Pressure–Vorticity Coupling family
Source: Zenodo 17340233.
Claim introduces a positive weight depending on pressure gradient and infers enhanced dissipation/BKM. Required audit: whether the weighted equation is algebraically equivalent to classical NSE or changes the dynamics/energy identity, and whether pressure curvature can be assigned a sign-definite damping role. **Status: OPEN_DEEP_AUDIT / POSSIBLE MODEL MODIFICATION.**

### B9. Scale-K Barrier family
Source: Zenodo 16898814.
Claim: above a fixed small scale nonlinear input is a strict fraction of viscous dissipation, yielding spectral tail/analyticity. Required audit: derivation of the strict fraction uniformly for arbitrary smooth data, moving-axis commutator control, and scale-packing closure. **Status: OPEN_DEEP_AUDIT; technically relevant to M17-298–300.**

### B10. One-scale robustness / pressure-free epsilon-regularity family
Source family: Zenodo 16993830/17162443/17163225.
Claim: one-cylinder pressure-free criterion + porosity + terminal transfer implies global regularity. Required audit: whether the one-scale criterion is truly pressure-free without hidden harmonic-tail hypotheses, whether porosity of bad radii follows with uniform constants, and whether terminal transfer is noncircular. **Status: OPEN_DEEP_AUDIT.**

### B11. Harbeck — equilibrium depletion / universal frequency envelopes
Required audit: derivation of a universal strict depletion/nondegeneracy constant and transition from an envelope criterion to unconditional regularity. **Status: OPEN_DEEP_AUDIT.**

### B12. Science World Journal quantum-force/quantized-fluid proof family
First-pass DSD flag: if the proof imposes quantum numbers/minimum-force/discrete fluid-particle postulates not shown to be exactly equivalent to the classical continuum NSE, it solves a modified model rather than the Clay statement. **Status: SCOPE_MISMATCH unless a two-way equivalence theorem is supplied.**

### B13. Aksman — Spectral Saturation / Heegner-resolution family
First-pass DSD flag: any transfer from vorticity/spectral dynamics to arithmetic/Heegner objects must include an exact, invertible or sufficiently faithful correspondence preserving the PDE, norms, and singularity question. **Status: OPEN_DEEP_AUDIT / EQUIVALENCE GATE.**

---

## C. Cross-family recurring failure modes

The audit to date identifies recurrent patterns that should be checked first in every new claimed proof:

1. **Critical property assumed in the bridge** — e.g. uniform L∞ reconstruction, alignment floor, A2 weight, UV cutoff.
2. **Amplitude homogeneity mismatch** — proposed nonlinear estimates have the wrong degree under `u→Au`.
3. **Fourier support fallacy** — high×high interactions can produce low frequencies through near-cancellation.
4. **Integrated-to-uniform upgrade** — finite time integral is promoted to a time supremum without a valid differential inequality.
5. **Pressure cancellation error** — incompressibility cancels pressure only against divergence-free tests, not arbitrary nonlinear multipliers.
6. **Finite-dimensional-to-continuum leakage** — constants depending on mesh/core scale are silently treated as uniform.
7. **Physical phenomenology promoted to universal theorem** — Kolmogorov/core/alignment assumptions used for arbitrary smooth data.
8. **Modified-model equivalence gap** — new algebra/quantization/projection replaces rather than proves an equivalent form of the classical PDE.
9. **Continuation non sequitur** — impossibility/nonuniqueness after a hypothetical singularity is treated as contradiction before singular time.
10. **Minimal-element definition failure** — the minimization set does not actually isolate a positive critical threshold.
11. **Conditional theorem relabeled unconditional** — hypotheses remain open while the conclusion is advertised as the full Clay result.

---

## D. Current comparison value for the internal M17 project

The external audits are not to be imported as authority. They serve as adversarial test cases for the current M17 argument. Every failure mode above should be run against our own chain, especially:

- amplitude/scaling of M17 shell and packet inequalities;
- exact inheritance of CE-H under rescaling/cutoff;
- growing-lag `T_j~log R_j` constants;
- high×high→low spectral leakage in M17-300;
- packet-family coverage/packing versus selected representative;
- any use of phenomenological quietness or material genealogy;
- any step converting a conditional corridor into an exhaustive global branch.

The purpose of this registry is therefore two-sided: evaluate external claims fairly, and use every identified failure as a regression test against our own proof attempt.

\[
\boxed{\text{3D NAVIER–STOKES GLOBAL REGULARITY REMAINS UNPROVED IN THIS REPOSITORY.}}
\]
