# DSD Deep Audit Batch — Remaining 16 Claimed 3D Navier–Stokes Resolution Families

Date: 2026-09-06
Scope: version-aware, argument-focused audit of the 16 remaining deep-audit families in the external-claims registry.

## Audit rule

Each family is decomposed as

CLAIM -> HYPOTHESES -> HINGE -> EXPORT.

Statuses:
- FAIL_ROOT: a central public hinge has a direct mathematical/logical failure.
- CONDITIONAL: useful theorem/program survives under a named unproved hypothesis.
- SCOPE: modified/controlled model unless exact two-way equivalence to classical NSE is proved.
- OPEN_DEEP: no final failure established from currently accessible formula-level material.
- SUPERSEDED: an earlier unconditional claim is withdrawn/corrected by a later version.
- SURVIVOR: a useful partial result survives the audit and should be preserved/cited.

No status is a judgment of an author. It applies only to the specified argument/version.

---

## 1. Onodera — Fully Constructive Closure, Version 4.2

Public source: Zenodo 15605345 / 15605346; public implementation repository `hironodera/navier-stokes-global-regularity-proof`.

CLAIM: high-order energy induction + Riccati concentration control + constructive hierarchy closure gives unconditional global smoothness.

AUDIT:
1. The public implementation does not time-advance the NSE velocity. `u0_hat_proj` is constructed once and the loop repeatedly evaluates derivative norms of that unchanged array while scalar surrogate variables are advanced.
2. The public concentration surrogate uses `C' = K C^(3/2)` with positive `K`; this differential equation is blow-up producing, not suppressive, unless an additional negative/damping term changes the analytic theorem.
3. This does NOT by itself refute the analytical PDF, because the code may be only a schematic implementation.

STATUS: IMPLEMENTATION_FAIL already established; analytical proof remains OPEN_DEEP.

DECISIVE REMAINING HINGE: parameter- and order-uniform high-Sobolev estimates for the actual NSE solution, not a monitored scalar surrogate.

M17 lesson: numerical/algorithmic monitoring is not a PDE continuation theorem.

---

## 2. SAPZ — latest Route–T / v6 line

Version history matters.
- Earlier complete-resolution versions claimed closure.
- v4.3r1 explicitly identified CT3-(A3) as the remaining Clay-level target.
- Later Route–T/v5 and v6 records claim to discharge that target via a positive transport-residual contradiction.

CLAIM: epsilon-uniform Riccati normal form + CT2/CT3 persistence + Route–T positive transport residual + approximate-identity Gate A + CKN Gate B exclude blow-up.

AUDIT:
- The later self-identification of CT3-(A3) proves that earlier complete-claim versions were incomplete/superseded at that time.
- No direct contradiction has yet been established in the newest Route–T step from public summaries alone.
- The decisive quantifiers are: epsilon-uniform RNF coefficients; scale-last selection; persistence over the same physical horizon; positive transport-residual extraction without assuming the target concentration; and a fixed CKN bridge independent of the chosen mollifier scale.

STATUS: earlier complete claims SUPERSEDED; latest Route–T/v6 OPEN_DEEP.

SURVIVOR: the explicit hypothesis/target ledger and versioned self-audit are useful and should be cited as a model of correction discipline.

M17 lesson: growing-lag/scale-last quantifiers must be audited before an apparently closed local contradiction is globalized.

---

## 3. Hall — Dynamic Certificate Closure (DCC)

Version history:
- June 2026 paper explicitly presents a CONDITIONAL branch-reduction framework and leaves terminal regimes.
- July 2026 internal-QED version claims a finite carrier ledger closes terminal obstructions.

CLAIM: every possible singularity genealogy enters a finite list of carrier/record classes, each of which must pay a terminal obstruction.

AUDIT:
- The June conditional theorem is not refuted; its conditional scope is correctly stated.
- The July upgrade requires a theorem of EXHAUSTIVE PDE COVERAGE: every defect measure, loss of compactness, interface leak, scale escape, ancestry change, and carrier-edge event must enter the finite ledger with no unpriced residual.
- Finite bookkeeping by definition does not prove completeness.

STATUS: June CONDITIONAL/SURVIVOR; July UNVERIFIED INTERNAL-QED / OPEN_DEEP.

DECISIVE HINGE: terminalization completeness + record-conservation theorem + carrier-edge completeness.

M17 lesson: DSD's own branch tree has the same obligation. No global closure may be claimed until coverage is proved, not merely enumerated.

---

## 4. Peterson — Xi-Regularization

Public claim introduces a dynamically oscillating phase-pressure feedback field Xi that stabilizes vorticity.

AUDIT:
- If Xi is an additional feedback/controller term, the equation is modified and the result is outside the classical Clay problem.
- To remain classical NSE, the manuscript must prove an exact bidirectional equivalence: every classical solution determines Xi and every Xi-formulation solution maps back to the same classical NSE solution, with no additional admissibility constraint.
- Describing an added stabilizing field as not disrupting turbulence is not an equivalence theorem.

STATUS: SCOPE unless exact two-way equivalence is proved. No claim that the modified-model regularity mathematics is false.

M17 lesson: never confuse an auxiliary analytic variable with an added dynamical degree of freedom.

---

## 5. Zhang — mollifier/Galerkin double-limit framework

CLAIM: compactly supported mollification + uniform double-limit energy estimates + Galerkin iteration produce global smooth solutions, including very weak initial classes.

AUDIT:
- Standard uniform energy control gives compactness sufficient for Leray weak solutions, not global smoothness.
- Passing to C^infinity/H^infinity for t>0 requires approximation-parameter-uniform critical or higher-Sobolev bounds on every positive-time slab.
- Mollified approximants are individually smooth; this fact alone does not survive the limit strongly enough to exclude 3D singularities.

STATUS: OPEN_DEEP / UNIFORMITY HINGE.

DECISIVE HINGE: explicit estimates of the form `sup_{epsilon,N} ||u_{epsilon,N}||_{X(tau,T)} < infinity` in a regularity-continuation space X, for every tau>0, with no hidden epsilon or Galerkin-dimension loss.

M17 lesson: compactness is not regularity unless the norm controlling regularity is compactly inherited.

---

## 6. Stough — phi-resonant decomposition

CLAIM: a phi-resonant harmonic decomposition enforces dynamic cancellations and yields uniform higher-Sobolev control.

AUDIT:
- Accessible summaries do not expose enough formulae for a valid root-failure verdict.
- Required checks are exact completeness of resonant/nonresonant splitting, arbitrary phase configurations, Bony low-high interactions, high-high near-cancellation to low output, and amplitude homogeneity of the multiplier estimate.
- A similar named kernel appearing in another Millennium-problem manuscript is not itself evidence for or against the NSE proof.

STATUS: OPEN_DEEP.

M17 lesson: any spectral cancellation must keep low-high and high-high->low leakage explicit unless a true symbol theorem removes it.

---

## 7. One-Scale Robustness — pressure-free epsilon-regularity, porosity, terminal transfer

Public chain:
P1 single-cylinder velocity-only epsilon regularity for `Phi = E + kappa C^(2/3)`;
P2 weighted `Phi_beta(r)=r^beta Phi(r)`, beta>2, slope-gap + BV-on-bands + IMS overlap -> porosity;
P3 terminal-time transfer via matched local-energy inequalities and Vitali selection;
P4 weak-strong continuation.

AUDIT:
- No direct public root contradiction has been established.
- Main quantitative danger: `r^beta Phi(r)` becomes small as r->0 even when the unweighted critical quantity Phi does not. Every use of weighted smallness must be audited before it is exported as genuine epsilon-smallness.
- A terminal-time `uniform scale floor` must be derived without importing endpoint regularity or compactness that the proof is trying to obtain.
- Exact cancellation of a renormalized far-field pressure defect is useful only if all remaining harmonic-tail terms are controlled uniformly.

STATUS: OPEN_DEEP / WEIGHT-TO-UNWEIGHT + TERMINAL-UNIFORMITY HINGES.

SURVIVOR: pressure decomposition, matched-cutoff subtraction, BV/IMS organization may be independently useful if formulae check out.

M17 lesson: do not manufacture smallness by scale weights; distinguish a diagnostic's slope from the actual critical quantity.

---

## 8. Scale-K / variable-axis conic / resonant-budget family

Version evidence is decisive.

- 2025-09-07 record claims unconditional global regularity.
- 2025-09-12/13 record states H2-H4 are proved but H1 (Axis Carleson) is the remaining analytic barrier and regularity follows IF H1 holds.
- Later Restricted-Carleson/VACM records attempt to discharge active-scale Carleson through spectral-gap sublevel estimates.

AUDIT:
- The later H1 statement supersedes the earlier unconditional wording: the earlier record cannot be treated as a completed proof if the same program later identifies H1 as unproved.
- H2-H4 may remain valuable conditional harmonic-analysis results.
- The later restricted-Carleson discharge must still be checked for eigen-axis degeneracy, mollification-scale dependence, Carleson constants, and low-high/high-high spectral leakage.

STATUS: 2025-09-07 unconditional claim SUPERSEDED; H2-H4 CONDITIONAL/SURVIVOR; latest restricted-Carleson H1 discharge OPEN_DEEP.

M17 lesson: explicit self-correction is positive evidence of auditability. Preserve surviving lemmas rather than treating the family as all-or-nothing.

---

## 9. Graah — thick / tube-like / fragmented trichotomy

CLAIM: every blow-up scale falls into a complete geometric trichotomy; each regime forces a scale-invariant dissipation lower bound on a comparable time interval; infinitely many disjoint intervals contradict finite total dissipation.

AUDIT:
- Logical skeleton is valid IF four quantitative statements hold: trichotomy exhaustiveness; definite time fraction; fixed positive PHYSICAL dissipation cost; genuinely disjoint/non-overcounted time intervals.
- Critical DSD firewall: a normalized/scale-invariant lower bound is not automatically an amplitude-independent lower bound on the physical quantity `int |grad u|^2`. The cost may shrink with packet amplitude or scale.
- This is exactly the failure mode already exposed internally by M17-235/237/242.

STATUS: OPEN_DEEP, high priority.

DECISIVE HINGE: demonstrate a scale-independent positive lower bound in the actual globally budgeted dissipation, not only a normalized local functional.

SURVIVOR: the trichotomy/packing architecture is highly relevant to M17 if that physical-cost bridge survives.

---

## 10. Eigen-gap Carleson / directional packet analysis

Latest family: scale-localized directional packets, smoothed strain eigenvectors, spectral-gap sublevel estimates, Carleson tents, global ledger.

Important earlier directional-microlocal draft publicly states a bound of the form
`int_0^infty ||omega(t)||_{L^1_x} dt <= C(nu,E0)`
and then claims smoothness.

AUDIT:
- `L^1_x` vorticity is not the Beale-Kato-Majda endpoint. Spatial concentration can keep L1 bounded while L-infinity diverges. Hence the earlier L1 -> max-vorticity endpoint bridge is a FAIL_ROOT unless substantial additional regularity is supplied.
- The Nov. 7 eigen-gap version speaks of a separate 'classical endpoint inequality' converting the ledger to maximum vorticity. That newer bridge must be audited separately and is not automatically refuted by the earlier draft.
- Near eigenvalue degeneracy, a principal strain direction is unstable; any moving-frame estimate needs a gap-weighted commutator that remains integrable across the small-gap set.

STATUS: earlier directional-ledger endpoint FAIL_ROOT; latest eigen-gap version OPEN_DEEP at endpoint + small-gap bridge.

M17 lesson: geometric/Carleson control must terminate in a norm that actually controls continuation; L1-type geometry cannot silently inherit L-infinity amplitude control.

---

## 11. IG-Morse / Crofton Navier-Stokes Proof Pack

CLAIM: vorticity-direction topology on S^2, Fisher-information jumps at handle birth, Crofton integral geometry, Campanato/Morrey bridges and BKM close regularity.

AUDIT:
- `xi=omega/|omega|` is undefined at omega=0; nodal-set creation/motion can change direction-field topology without a singularity of the physical vorticity.
- Topological complexity controls geometry, not vorticity amplitude. An independent amplitude-to-BKM bridge is required.
- A claimed Fisher-information quantum at every topology change must be derived from the PDE and shown to be paid in a globally summable physical budget.

STATUS: OPEN_DEEP / GEOMETRY-TO-AMPLITUDE HINGE.

M17 lesson: nodal interfaces and director topology must remain separated from absolute amplitude budgets.

---

## 12. Shoji — Logical Cost Functional / Resource-Constrained Analysis

Public central claim: maximum vorticity is bounded by a function (reported as square-root/logarithmic type) of logical depth of a frequency decomposition, and maintaining high logical depth requires exponentially large physical dissipation.

DIRECT AMPLITUDE TEST:
Take a fixed nonzero smooth divergence-free profile u and replace it by A u at a fixed time. The frequency support/decomposition depth is unchanged by scalar amplitude A, while `||omega||_infinity` scales as A. Therefore no universal inequality
`||omega||_infinity <= F(logical depth)`
can hold if logical depth contains no amplitude information.

Even if amplitude is inserted into the cost, a second bridge is required: a restriction on contraction/duplication in a proof calculus is not itself an analytic lower bound on NSE dissipation.

STATUS: FAIL_ROOT for the public depth-only embedding; CATEGORY-BRIDGE failure remains independently.

M17 lesson: bookkeeping complexity is not physical energy unless an explicit analytic inequality proves the conversion.

---

## 13. Global Bridge / Projection API

Public architecture: embed NSE into an inductive-limit holomorphic host, use a projection API/analytic lift, and a scheduler that ensures contractivity; collapse of the projection correspondence is said to imply global smoothness.

AUDIT:
- A contractive scheduler is an algorithmic control unless it is proved to be forced by, and exactly equivalent to, every classical NSE trajectory.
- Required theorem: two-way conjugacy/equivalence preserving time evolution, divergence-free constraint, norms relevant to blow-up, and all nonlinear interactions.
- If contractivity is chosen by the scheduler and then exported back as PDE contractivity, the desired conclusion has been inserted at the representation layer.

STATUS: CONDITIONAL/SCOPE; Clay upgrade FAILS unless exact bidirectional equivalence is supplied.

M17 lesson: representation changes cannot add admissibility conditions that prune genuine NSE trajectories.

---

## 14. Emergent nonlinear vorticity dissipation

Public claim: the classical linear viscous term, after directional decomposition/spectral analysis, generates an effective nonlinear damping strong enough to dominate vortex stretching.

AMPLITUDE FIREWALL:
For a fixed spatial profile omega, replacing omega by A omega makes standard viscous quadratic dissipation scale as A^2. Any proposed universal coercive superquadratic damping term `c ||omega||_p^p`, p>2, scales as A^p. A fixed positive c cannot be supplied by the same quadratic viscous budget for arbitrary A.

A directional projection of the linear Laplacian can generate useful identities and normalized quotient terms, but any amplitude-independent nonlinear damping must pay a denominator/normalization cost; it is not additional physical dissipation for free.

STATUS: FAIL_ROOT for any universal superquadratic-damping interpretation of the unmodified viscous budget; local/directional identities may survive separately.

M17 lesson: this is a direct external confirmation of the M17-242 amplitude-scaling firewall.

---

## 15. Pressure-vorticity weighted enstrophy

Public claim: a positive weight w(|grad p|) yields stronger dissipation in high-pressure-gradient/curvature regions and closes a BKM integral while keeping classical NSE unchanged.

EXACT AUDIT REQUIREMENT:
For a state-dependent weight w(x,t), differentiating weighted enstrophy necessarily creates terms involving
`partial_t w`, `u dot grad w`, `Delta w`, and `grad w dot grad omega`.
Pressure is nonlocal and satisfies a Poisson equation, so these terms have no automatic favorable sign.

A positive/increasing weight does not increase the physical viscosity for free. Any apparent extra coercivity must be balanced against these commutator/transport terms. Also, converting weighted control back to unweighted BKM requires quantitative upper/lower bounds on the weight.

STATUS: OPEN_DEEP / HIGH-RISK WEIGHT-COMMUTATOR HINGE. If the derivative-of-weight terms are omitted or assumed favorable, that would be FAIL_ROOT; currently accessible summaries are insufficient for that final verdict.

M17 lesson: weighted multipliers must carry their full material-derivative ledger.

---

## 16. Finite-carrier / finite-information ledgers beyond DCC

This is a schema rather than one manuscript.

A finite obstruction ledger can prove global closure only if there is an independent COVERAGE THEOREM:
1. every blow-up/loss-of-compactness sequence produces at least one listed carrier;
2. transitions between carriers conserve or pay a quantified record;
3. interfaces, scale escape, frequency leakage, genealogy replacement and vanishing-amplitude carriers are included;
4. no new carrier appears under weak limits/rescaling;
5. the terminal payer is measured in an actual globally finite physical budget.

STATUS: CONDITIONAL SCHEMA. Enumeration is not completeness.

M17 lesson: this requirement applies equally to DSD/M17. The present branch tree is a research/audit structure, not yet a proof of exhaustive global regularity.

---

# Cross-family regression tests exported to M17

R11. Amplitude homogeneity: test every claimed universal inequality under amplitude rescaling before geometric interpretation.

R12. No scale-weight smallness inheritance: `r^beta X(r)` small does not imply critical `X(r)` small.

R13. Normalized local cost != globally budgeted physical cost. Every packing contradiction needs a fixed lower bound in the actual global budget.

R14. Endpoint correctness: L1, area, topology, entropy, logical depth, or packet count does not become L-infinity/BKM control without an explicit analytic bridge.

R15. Moving-axis/eigenvector estimates must price small eigen-gaps and axis variation; a principal direction is unstable at degeneracy.

R16. Finite ledgers require an exhaustive coverage theorem, including weak-limit and interface escape.

R17. State-dependent weights require the full derivative/commutator ledger.

R18. Representation/scheduler/regularization methods need exact two-way equivalence or a uniform zero-parameter limit before they can inherit the label 'classical NSE'.

R19. Low-high and high-high->low Fourier leakage remains explicit in M17-300/301.

R20. Version-aware audit: later self-correction supersedes earlier unconditional claims but does not erase valid intermediate lemmas.

---

# Batch conclusion

No member of this 16-family batch is accepted here as a verified unconditional proof of classical 3D Navier-Stokes global regularity.

However the audit does NOT reduce all families to 'false'. The batch separates:
- direct root failures (e.g. Shoji depth-only amplitude bridge; earlier directional-ledger L1 endpoint; superquadratic physical-damping interpretation),
- modified/equivalence-scope programs (Xi, Global Bridge),
- explicit conditional survivors (Scale-K H2-H4, June DCC),
- version-corrected programs (SAPZ, Scale-K), and
- genuinely open formula-level audits (Graah, one-scale porosity, latest eigen-gap packet, Stough, Zhang, pressure-weighted enstrophy, latest SAPZ/DCC).

GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.
