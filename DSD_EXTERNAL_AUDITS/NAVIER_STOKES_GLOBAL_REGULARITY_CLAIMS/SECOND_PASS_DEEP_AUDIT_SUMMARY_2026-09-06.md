# Second-Pass DSD Deep Audit Summary — Claimed 3D Navier–Stokes Resolutions

Date: 2026-09-06
Scope: continuation after `DEEP_AUDIT_BATCH_16_2026-09-06.md`.

This report records only additional conclusions that could be justified from accessible full text, public source code, or exact mathematical necessity tests. It deliberately stops where the source formulae are not accessible enough for a responsible verdict.

## 1. Zhang — status upgraded from OPEN_DEEP to FAIL_ROOT

Full-text audit of *Global Smooth Solutions to the 3D Incompressible Navier-Stokes Equations: Weakly Regular Framework and Multi-Scenario Adaptation* (Preprints 202601.0992.v1; DOI 10.20944/preprints202601.0992.v1) found two root gaps in the smoothness upgrade.

The paper reaches the Leray-level class

\[
u\in L^\infty_tL^2_x\cap L^2_tH^1_x.
\]

Its high-order double induction then requires as the `k=1` base

\[
\nabla u\in L^\infty([\delta,T];L^2),
\]

but cites only the previously established time-integrated bound

\[
\nabla u\in L^2([0,T];L^2).
\]

Hence

\[
\boxed{L^2_tH^1_x\not\Rightarrow L^\infty_tH^1_x.}
\]

The same induction differentiates the equation by `partial_t^M nabla^K` while the weak-force hypothesis is only `f in L^2_tL^2_x`; derivatives of `f` are unavailable for `M+K>0`.

Verdict: `FAIL_ROOT` at the high-order regularity upgrade. The energy/Galerkin compactness portion survives as a weak-solution framework.

Detailed file: `AUDIT_ZHANG_MOLLIFIER_GALERKIN_DOUBLE_LIMIT_2026-09-06.md`.

## 2. Onodera — public implementation failure strengthened

The public repository `hironodera/navier-stokes-global-regularity-proof` was inspected at source-code level.

The concentration surrogate is

\[
C_{n+1}=C_n+\Delta t\,K C_n^{3/2},
\]

so for positive `K` the continuous analogue is Riccati growth, not suppression.

The high-order recurrence uses

\[
C_k^\sharp=\frac{k}{4}\frac{2^k}{\nu}+2,
\]

which worsens exponentially in derivative order.

The driver fixes `max_order=3`, and every time step computes derivative norms from the unchanged initial Fourier state `u0_hat_proj`; no NSE velocity state is advanced.

Verdict: the public package is not a computational proof certificate for NSE global regularity. The separate analytical PDF remains a distinct object requiring direct full-text audit.

Detailed file: `AUDIT_ONODERA_CONSTRUCTIVE_CLOSURE_IMPLEMENTATION_2026-09-06.md`.

## 3. Graah trichotomy — physical dissipation summability gate

For a parabolic cylinder of radius `r`, the globally budgeted physical dissipation

\[
D(Q_r)=\iint_{Q_r}|\nabla u|^2
\]

scales as `r`. Therefore a scale-invariant lower bound

\[
r^{-1}D(Q_r)\ge c
\]

yields only

\[
D(Q_r)\ge cr.
\]

Infinitely many disjoint intervals/cylinders do not by themselves contradict finite total dissipation because the radii may be summable. The final packing contradiction therefore requires one of:

- a fixed scale-independent **physical** dissipation quantum;
- a theorem forcing `sum r_j = infinity`;
- multiplicity compensation making the total scale-by-scale physical cost nonsummable;
- another globally finite budget with the correct zero scaling dimension.

Current status: `OPEN_DEEP`. Public searchable material does not expose whether this nonsummability theorem is actually present.

Detailed file: `AUDIT_GRAAH_TRICHOTOMY_DISSIPATION_SUMMABILITY_2026-09-06.md`.

## 4. Pressure-weighted enstrophy — exact multiplier ledger

For any smooth positive state-dependent weight `w`, the exact vorticity identity is

\[
\frac12\frac d{dt}\int w|\omega|^2
=
\int w\,\omega\cdot S\omega
-\nu\int w|\nabla\omega|^2
+\frac12\int(D_tw+\nu\Delta w)|\omega|^2.
\]

Thus `w=w(|nabla p|)` does not supply free additional damping. The proof must control the full material/diffusive derivative of the pressure-dependent weight and then recover an unweighted continuation norm.

Current status: `OPEN_DEEP`. Omission or unjustified favorable sign of the last term would be a root failure.

Detailed file: `AUDIT_PRESSURE_WEIGHTED_ENSTROPHY_EXACT_WEIGHT_DERIVATIVE_GATE_2026-09-06.md`.

## 5. IG–Morse/Crofton — amplitude firewall

For `omega=rho xi`,

\[
|\nabla\omega|^2=|\nabla\rho|^2+\rho^2|\nabla\xi|^2.
\]

Under `omega -> epsilon omega`, director topology and unweighted director Fisher/Crofton quantities remain unchanged while the physical weighted director cost scales as `epsilon^2`.

Therefore any inference

\[
\text{fixed director-topology/Fisher quantum}
\Rightarrow
\text{fixed physical NSE dissipation quantum}
\]

fails unless a PDE-derived amplitude floor or equivalent weighted bridge is proved.

Status: `FAIL_ROOT` for the amplitude-free bridge; the global family remains open only if the manuscript contains an independent amplitude bridge.

Detailed file: `AUDIT_IG_MORSE_CROFTON_DIRECTOR_TOPOLOGY_AMPLITUDE_FIREWALL_2026-09-06.md`.

## 6. Scale-K / Restricted-Carleson VACM — inverse eigen-gap gate

The version history itself is relevant: the early unconditional statement was followed by a version explicitly identifying H1 Axis Carleson as the remaining barrier; later Restricted-Carleson work attempts to close H1.

For a simple top eigenvalue of the smoothed strain,

\[
|\nabla P_1|\lesssim\frac{|\nabla S|}{\lambda_1-\lambda_2}.
\]

Thus the latest proof must price the inverse eigen-gap. Heat analyticity alone does not imply universal, solution-independent eigen-gap transversality or Lojasiewicz sublevel constants.

Status: early unconditional claim `SUPERSEDED`; H2-H4 conditional survivor; latest H1 discharge `OPEN_DEEP`.

Detailed file: `AUDIT_SCALE_K_RESTRICTED_CARLESON_EIGENGAP_UNIFORMITY_2026-09-06.md`.

## 7. SAPZ v6 Route-T — all-small-scales quantifier gate

Gate A based on approximate identities is valid if the proof has

\[
\sup_{0<\varepsilon<\varepsilon_0}
\||u|^2*\varphi_\varepsilon\|_\infty\le C.
\]

But a bound at only one selected scale

\[
\exists\varepsilon_*:\
\||u|^2*\varphi_{\varepsilon_*}\|_\infty\le C
\]

cannot recover the pointwise `L^infinity` norm.

Hence the latest Route-T chain must prove all-sufficiently-small-scale control (or a monotonicity/coverage theorem exporting the selected scale to all finer scales), on the same physical window with uniform constants.

Status: v6 `OPEN_DEEP`; earlier criterion-stage versions are superseded by the author's later Route-T program rather than used as a refutation.

Detailed file: `AUDIT_SAPZ_V6_GATE_A_QUANTIFIER_ORDER_2026-09-06.md`.

## 8. One-scale robustness — weighted porosity is not critical smallness

With

\[
\widetilde\Phi_\beta(r)=r^\beta\Phi(r),\qquad\beta>2,
\]

smallness of the weighted quantity does not imply smallness of the scale-critical `Phi`. Example: `Phi(r)=1` gives `r^beta Phi(r)->0`.

The porosity theorem must therefore output a genuine scale with

\[
\Phi(r)<\varepsilon_*,
\]

not merely a weighted diagnostic below a threshold. The terminal transfer also needs a scale usable uniformly as `t upward T`, rather than good scales that shrink without control.

Status: `OPEN_DEEP` at the weight-to-critical and terminal-uniformity gates.

Detailed file: `AUDIT_ONE_SCALE_POROSITY_WEIGHT_TO_CRITICAL_SMALLNESS_GATE_2026-09-06.md`.

## 9. Latest eigen-gap directional packets — endpoint and frame-degeneracy gates

A predecessor directional-ledger formulation described finite spacetime `L^1_x` vorticity and a regularity conclusion. `L^1_x` is not the BKM endpoint, so that formulation fails at the endpoint bridge.

The latest eigen-gap packet version advertises a separate maximum-vorticity endpoint inequality and must be judged independently. It also must price the same inverse eigen-gap/frame variation as the Scale-K program and reconstruct all degenerate/interface residuals.

Status: predecessor endpoint `FAIL_ROOT`; latest version `OPEN_DEEP`.

Detailed file: `AUDIT_EIGENGAP_DIRECTIONAL_PACKET_ENDPOINT_AND_SMALL_GAP_2026-09-06.md`.

## 10. Stough phi-resonant — stopping point of responsible audit

Searchable public records expose the abstract and the claim of a phi-resonant decomposition/nonlinear multiplier cancellation, but not enough formulae to verify:

- completeness of the resonant/nonresonant split;
- arbitrary-phase cancellation;
- low-high interactions;
- high-high near-cancellation to low output;
- amplitude homogeneity of the multiplier estimate.

No further negative verdict is justified without the actual formulae. Status remains `OPEN_DEEP`.

## 11. Hall DCC — stopping point of responsible audit

The June version is explicitly conditional and should not be attacked as an unconditional proof. The July internal-QED version itself directs external validation toward relative log-shell estimates, collar routing, record conservation and carrier-edge completeness.

Without the exact bridge formulae, the correct status remains `OPEN_DEEP` for the July upgrade and `CONDITIONAL/SURVIVOR` for the June framework.

## 12. New M17 regression tests R21–R27

R21. Infinite count of normalized payments is not an infinite physical budget; prove their physical weights nonsummable.

R22. Every state-dependent weighted energy retains the full `(D_t+nu Delta)w` term.

R23. Director topology is amplitude-blind; topology-to-dissipation needs a PDE amplitude bridge.

R24. Analytic smoothing does not create universal eigen-gap transversality; inverse-gap costs must be paid.

R25. Selected-scale success does not imply all-finer-scale compactness/endpoint control.

R26. Porosity/slope of `r^beta Phi` cannot substitute for epsilon-smallness of critical `Phi`.

R27. Directional packet ledgers must export into a genuine continuation endpoint and include small-gap/frame leakage.

These are now mandatory regression tests for M17-300 -> M17-301 and subsequent growing-lag genealogy work.

## 13. Accounting after second pass

From the previous 16-family deep-audit batch:

- 6 families are now resolved/classified at root/scope level, including Zhang;
- 10 remain latest-version/formula dependent;
- several of those 10 now have only one or two explicitly named formula-level gates rather than an undefined 'needs more audit' status.

No external paper audited here is accepted as a verified unconditional solution of classical 3D Navier-Stokes global regularity.

GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.
