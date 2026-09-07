# Final External-Paper Citation Role Registry — 3D Navier–Stokes

Date: 2026-09-07  
Repository: `dominicus9708/Navier_Stokes`  
Scope: the 16-family deep-audit batch of 2026-09-06 plus the second-pass formula-level audit and current public-version recheck.

## Status of this registry

This file closes the **citation-role decision** for the currently audited external claim families.

It does **not** declare that every inaccessible manuscript is mathematically false.
Instead, it answers the question needed by the DSD/Navier–Stokes program:

> What evidentiary role, if any, may each external paper/version play in the repository after analysis and audit?

The allowed roles are:

- `SUPPORTED_EXTERNAL_ANCHOR` — a rigorous external theorem/result may be used positively within its exact hypotheses.
- `CONDITIONAL_SURVIVOR` — useful theorem, architecture, or lemma survives only under named unproved hypotheses.
- `REFERENCE_ONLY` — insufficient public formula-level access for positive proof weight; may be cited descriptively but not used as a theorem.
- `ANTI_LESSON` — a failed/superseded hinge is preserved as a counterexample to an invalid proof move.
- `SCOPE_ONLY` — result concerns a modified representation/model unless exact equivalence to classical NSE is proved.
- `REJECTED_AS_GLOBAL_PROOF` — the audited version may not be cited as an unconditional proof of classical 3D NSE global regularity.

A family may receive more than one role because a failed global claim can still contain useful local lemmas or methodological lessons.

---

# 1. Final role table

| # | Family / version | Final audit status | Citation role in DSD/NSE | Positive use allowed | Anti-lesson / firewall |
|---|---|---|---|---|---|
| 1 | Onodera — constructive closure / public implementation | implementation `FAIL`; analytical PDF not recertified here | `ANTI_LESSON` + `REFERENCE_ONLY` | architecture may be described; no computational-proof weight | monitoring scalar surrogates or unchanged Fourier data is not time advancement of NSE; Riccati `C'=K C^(3/2)` with positive `K` is growth, not damping |
| 2 | SAPZ — v4.3r1 -> Route-T/v6 | earlier completion wording superseded; latest Route-T remains quantifier-gated | `CONDITIONAL_SURVIVOR` + `ANTI_LESSON` | versioned target ledger, scale-last discipline, approximate-identity strategy | selected scale is not all-finer-scale control; endpoint Gate A needs uniform sufficiently-small-scale control on the same window |
| 3 | Hall — DCC June conditional / July internal-QED | June survives conditionally; July closure unverified | `CONDITIONAL_SURVIVOR` | finite branch-reduction architecture and explicit terminal obligations | finite bookkeeping is not proof of exhaustive PDE coverage; carrier-edge and record-conservation completeness must be theorems |
| 4 | Peterson — Xi regularization | classical-NSE scope not established | `SCOPE_ONLY` + `ANTI_LESSON` | may be studied as a modified/control formulation | auxiliary stabilizing field is not classical NSE unless exact bidirectional equivalence is proved |
| 5 | Zhang — mollifier/Galerkin double-limit | `FAIL_ROOT` at high-order regularity upgrade | `ANTI_LESSON`; weak/Galerkin portion `CONDITIONAL_SURVIVOR` | standard weak compactness / Galerkin organization only | `L^2_t H^1_x` does not provide the `L^∞_t H^1_x` induction base; weak forcing does not supply arbitrary derivatives |
| 6 | Stough — phi-resonant decomposition | formula access insufficient for verdict | `REFERENCE_ONLY` | possible spectral-cancellation inspiration only after independent rederivation | never suppress low-high or high-high->low leakage without a symbol theorem |
| 7 | One-Scale Robustness / porosity | open at weight-to-critical and terminal-uniformity gates | `CONDITIONAL_SURVIVOR` | matched pressure subtraction, local-energy organization, BV/IMS ideas if independently checked | small `r^beta Phi(r)` is not epsilon-smallness of critical `Phi(r)`; a good scale must be usable uniformly near terminal time |
| 8 | Scale-K / VACM / Restricted-Carleson | early unconditional claim superseded; conditional analytic pieces survive; latest H1 gate open | `CONDITIONAL_SURVIVOR` + `ANTI_LESSON` | conic/microlocal decomposition, H2-H4 type conditional lemmas | smoothed eigen-axis costs inverse gap; analyticity does not give solution-independent eigen-gap transversality |
| 9 | Graah — thick/tube/fragmented trichotomy | architecture survives conditionally; physical summability bridge open | `CONDITIONAL_SURVIVOR` | geometric trichotomy and packing architecture | normalized dissipation quantum is not a fixed physical budget quantum; must prove nonsummable physical weights or multiplicity compensation |
| 10 | eigen-gap directional packets | predecessor endpoint `FAIL_ROOT`; latest version open | `ANTI_LESSON` + `REFERENCE_ONLY` | latest packet ledger may inspire independent constructions | spacetime `L^1_x` vorticity is not the continuation endpoint; small-gap/frame leakage must be included |
| 11 | IG-Morse / Crofton proof pack | amplitude-free topology-to-dissipation bridge `FAIL_ROOT` | `ANTI_LESSON`; geometry-only pieces `CONDITIONAL_SURVIVOR` | topology/Crofton/director geometry only when amplitude is kept separate | director topology is invariant under amplitude rescaling while physical dissipation is not; requires a PDE amplitude floor |
| 12 | Shoji — Logical Cost Functional | depth-only embedding `FAIL_ROOT` | `ANTI_LESSON` | bookkeeping analogy only, not PDE evidence | frequency-decomposition depth is amplitude-blind; proof-calculus resource cost is not physical dissipation without an analytic inequality |
| 13 | Global Bridge / Projection API | exact classical equivalence not established | `SCOPE_ONLY` + `ANTI_LESSON` | representation methodology only | a contractive scheduler/projection cannot prune classical NSE trajectories unless exact two-way conjugacy is proved |
| 14 | Polozov — emergent nonlinear vorticity dissipation | universal superquadratic-damping reading `FAIL_ROOT` by amplitude scaling | `ANTI_LESSON`; local identities only if independently verified | directional/spectral decompositions may be rederived | the quadratic viscous budget cannot provide an amplitude-independent superquadratic physical damping quantum for arbitrary rescaling |
| 15 | pressure–vorticity weighted enstrophy | global closure unverified; exact weight ledger mandatory | `REFERENCE_ONLY`; exact weighted-energy identity is an internal audit anchor | state-dependent weighted multipliers only with full derivative terms | every weight retains `(D_t + nu Delta) w`; positive/increasing weight is not free extra viscosity |
| 16 | finite-carrier / finite-information ledgers beyond DCC | methodology only absent a coverage theorem | `CONDITIONAL_SURVIVOR` | branch bookkeeping and audit architecture | enumeration is not exhaustiveness; every compactness/interface/scale/ancestry residual needs a priced export |

---

# 2. Paper-by-paper final analysis

## 2.1 Onodera

The public implementation is not a computational certificate for the NSE evolution.
The code-level audit found that the displayed monitoring loop evaluates derivative norms from a fixed projected initial Fourier state while scalar surrogate variables evolve.
Thus the package may not be cited as numerical verification of global regularity.

The separate analytical manuscript is logically distinct.
Because the present audit did not recertify all of its full formula chain, it receives `REFERENCE_ONLY`, not `FAIL_ROOT` by inheritance from the code.

**Use:** anti-lesson for the rule `algorithmic monitor != PDE trajectory`.

## 2.2 SAPZ

Version history is itself evidentiary.
The v4.3r1 record explicitly isolated CT3-(A3) as a remaining Clay-level PDE target, so earlier full-resolution language is superseded.
Later Route-T/v6 claims to discharge it.
The remaining audited gate is quantifier order at the approximate-identity endpoint: a selected mollifier scale cannot by itself recover a pointwise `L^infinity` bound; one needs uniform control for all sufficiently small scales, or an independent theorem exporting the selected scale to all finer scales on the same physical window.

**Use:** preserve versioned target-ledger discipline and scale-last selection as positive methodology; cite the earlier/later transition as an anti-lesson against treating a criterion as a completed global proof.

## 2.3 Hall DCC

The June framework is correctly conditional and therefore survives as a legitimate branch-reduction/audit architecture.
The July internal-QED version strengthens the claim, but the exact exhaustive-coverage theorem, record conservation and carrier-edge completeness remain the decisive verification points.

**Use:** direct methodological comparator for DSD branch coverage.

## 2.4 Peterson Xi

Any Xi field that acts as an independent stabilizer/controller changes the dynamical problem unless the manuscript proves exact bidirectional equivalence with every classical NSE trajectory.

**Use:** scope firewall for auxiliary variables.

## 2.5 Zhang

The energy/Galerkin portion supports a weak-solution compactness framework, but not the claimed smoothness upgrade.
The public text states a high-order double induction whose `k=1` base is supplied only by a time-integrated gradient estimate; this does not give the required uniform-in-time `H1` control.
The differentiated equation also needs derivatives of the forcing that are absent under merely `f in L2_t L2_x`.

**Use:** strong anti-lesson for `smooth approximants + weak compactness != smooth limiting solution` and for derivative-budget bookkeeping.

## 2.6 Stough phi-resonant

Accessible formulae remain insufficient to verify the resonant/nonresonant partition, arbitrary-phase cancellation and spectral leakage terms.
A negative verdict would be speculative.

**Use:** reference-only until independently reconstructed.

## 2.7 One-Scale Robustness

The central useful idea is to seek a real scale at which the unweighted critical epsilon quantity is small.
The dangerous shortcut is to infer that from a weighted diagnostic `r^beta Phi(r)` with `beta>2`, which may become small even when `Phi(r)` stays order one.

**Use:** pressure/local-energy organization as conditional method; R26 anti-shortcut remains mandatory.

## 2.8 Scale-K / VACM

The program's self-correction is useful evidence about its internal auditability: an early unconditional record was followed by a formulation identifying Axis Carleson H1 as the remaining barrier.
The later restricted-Carleson approach is mathematically interesting but must price the derivative of the moving top-eigenvector projector through the inverse gap.

For a simple eigenvalue one expects schematically

`|grad P1| <= C |grad S|/(lambda1-lambda2)`.

**Use:** conditional microlocal tools; R24 inverse-gap firewall.

## 2.9 Graah trichotomy

The thick/tube/fragmented trichotomy is potentially useful as a geometric carrier classification.
The global contradiction, however, requires the local normalized payment to become a nonsummable **physical** budget.
If the physical cost of a radius-`r` event is only `c r`, an infinite collection with summable radii is compatible with finite total dissipation.

**Use:** direct architectural input to M17 genealogy/packing, but never as a completed dissipation contradiction without physical weights.

## 2.10 Eigen-gap directional packets

The predecessor endpoint based on spacetime `L1_x` vorticity does not control the maximum-vorticity continuation endpoint and is rejected.
The newer eigen-gap packet version is judged separately and remains unverified until the endpoint inequality and small-gap/frame leakage are explicit.

**Use:** R27 endpoint and frame-degeneracy regression test.

## 2.11 IG-Morse / Crofton

For `omega=rho xi`, the exact decomposition

`|grad omega|^2 = |grad rho|^2 + rho^2 |grad xi|^2`

shows the amplitude firewall.
Under `omega -> epsilon omega`, the director geometry/topology is unchanged while physical weighted director cost scales by `epsilon^2`.

**Use:** director-topology geometry may be useful, but only as geometry; any topology-to-dissipation claim needs an independently proved amplitude bridge.

## 2.12 Shoji logical cost

Scaling a fixed smooth profile `u` to `A u` preserves frequency-decomposition depth while multiplying maximum vorticity by `A`.
Therefore a universal depth-only upper bound on maximum vorticity cannot hold.
A proof-calculus restriction is also not automatically a Navier–Stokes dissipation inequality.

**Use:** category-error anti-lesson.

## 2.13 Global Bridge / Projection API

A representation/lift may be useful, but if a scheduler selects contractive trajectories then the proof has changed the admissible dynamics unless every classical NSE trajectory is exactly and bidirectionally represented.

**Use:** equivalence firewall.

## 2.14 Emergent nonlinear vorticity dissipation

The classical viscous term has quadratic amplitude scaling.
A claimed universal physical damping `c ||omega||_p^p`, `p>2`, with amplitude-independent `c`, scales superquadratically and cannot be additional free dissipation extracted from the same quadratic budget for arbitrary amplitude rescaling.

Local directional quotient identities may still exist, but they must retain every normalization denominator.

**Use:** direct external analogue of the M17 amplitude-scaling firewall.

## 2.15 Pressure-vorticity weighted enstrophy

For a smooth positive state-dependent weight `w`, the correct exact ledger contains the full derivative of the weight:

`(1/2) d/dt ∫ w |omega|^2 = ∫ w omega·S omega - nu ∫ w |grad omega|^2 + (1/2) ∫ (D_t w + nu Delta w) |omega|^2`.

Thus a pressure-dependent weight does not supply free damping.

**Use:** no positive proof weight for the global claim until this term is controlled and the result exports to an unweighted continuation norm.

## 2.16 Finite ledgers

A finite list of carriers proves global closure only after a separate coverage theorem shows that every loss of compactness, interface leak, scale escape, ancestry change and residual term belongs to the list with controlled overlap and no unpriced remainder.

**Use:** methodology and audit obligation, not a theorem.

---

# 3. Supported classical external anchors

The failed or conditional modern claim papers are **not** the repository's sole external basis.
The following classical results remain positive external anchors within their exact hypotheses:

1. **Caffarelli–Kohn–Nirenberg (1982)** — partial regularity / epsilon-regularity architecture for suitable weak solutions. Use as a genuine endpoint regularity anchor, not as proof that any arbitrary weighted diagnostic is epsilon-small.
2. **Kato (1984)** — strong `L^p` Navier–Stokes solution theory and local/continuation framework. Use for legitimate strong-solution interfaces only within the theorem's hypotheses.
3. **Escauriaza–Seregin–Sverak (2003)** — critical endpoint/backward-uniqueness regularity result. Use as a genuine critical endpoint rigidity anchor when the exact `L^infinity_t L^3_x`-type hypothesis has actually been reached.
4. Standard Leray energy/Galerkin theory — use for weak existence/energy compactness, never as an automatic smoothness upgrade.

These anchors are deliberately separated from claimed-resolution preprints.

---

# 4. Citation policy after this audit

## 4.1 Failed global claims

A `FAIL_ROOT` or superseded proof may be cited only in forms such as:

> This route illustrates why normalized payment counting is insufficient without physical-weight nonsummability.

or

> The failed high-order upgrade provides a counterexample to the inference that weak compactness of smooth approximants preserves the regularity norm.

It may **not** be cited as positive evidence for global regularity.

## 4.2 Partial survivors

When a family contains surviving material, cite the exact surviving object rather than the global claim.
Examples:

- Hall June: conditional branch-reduction framework.
- Scale-K: conditional conic/Carleson lemmas, not the superseded unconditional conclusion.
- Zhang: energy/Galerkin weak framework, not the smoothness theorem.
- IG-Morse: geometry/topology identities, not amplitude-independent dissipation.

## 4.3 Version pinning

Every citation to a rapidly revised proof program must include its exact version/date/record.
A later version that explicitly restores a missing hypothesis supersedes earlier unconditional wording for DSD evidentiary purposes.

## 4.4 Reference-only papers

If the exact hinge formula is not accessible, the paper is descriptive context only.
No theorem in M17 may depend on it.

---

# 5. M17 integration

The following existing regression tests remain externally reinforced:

- `R21` physicalize normalized payments and prove nonsummable weights.
- `R22` retain full state-dependent weight derivatives.
- `R23` keep amplitude separate from director topology.
- `R24` price inverse eigen-gap/frame derivatives.
- `R25` preserve selected-scale versus all-finer-scale quantifier order.
- `R26` do not replace critical epsilon-smallness by weighted porosity smallness.
- `R27` export geometric ledgers to a true continuation endpoint and include degeneracy leakage.

A companion file introduces `R28-R38` for citation-role and external-import discipline.

---

# 6. Final accounting

No audited modern claim family in this 16-family batch is accepted as an unconditional verified proof of classical 3D Navier–Stokes global regularity.

The completed citation-role allocation is:

- direct anti-lessons: Onodera implementation, Zhang smoothness upgrade, Shoji depth-only bridge, emergent superquadratic damping, predecessor directional endpoint, amplitude-free IG-Morse bridge;
- scope/equivalence firewalls: Peterson Xi, Global Bridge/Projection API;
- conditional survivors: Hall June, SAPZ method/ledger, One-Scale components, Scale-K conditional components, Graah architecture, IG-Morse geometry, finite-ledger methodology;
- reference-only pending formula access: Stough, latest directional packet bridge, pressure-weighted closure, unrecertified Onodera analytic PDF;
- positive theorem anchors: CKN, Kato, Escauriaza–Seregin–Sverak, and standard Leray weak theory within their exact scopes.

This completes the external-paper **analysis-to-citation-role** stage.
Future newly published versions re-enter the audit as new versioned objects rather than silently overwriting this registry.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
