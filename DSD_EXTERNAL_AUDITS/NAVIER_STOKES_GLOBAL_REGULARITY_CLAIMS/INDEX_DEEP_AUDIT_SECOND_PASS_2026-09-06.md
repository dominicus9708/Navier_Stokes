# DSD External Navier–Stokes Claims — Deep Audit Second-Pass Index

Date: 2026-09-06
Scope: continuation after `DEEP_AUDIT_BATCH_16_2026-09-06.md`, excluding already finalized families unless a later version materially changes scope.

## One-line status

The previous 11 formula-level open families have been reduced to **8 still-open families**.

New closures in this pass:

1. Feinstein restricted-Carleson / VACM latest public closure: **FAIL_ROOT**.
2. Petenchia pressure-frequency latest published line: **SCOPE / CONDITIONAL SURVIVOR**.
3. Zhang weak-regularity / mollifier–Galerkin double limit: **FAIL_ROOT**.

Further narrowed but not finalized:

4. Graah trichotomy: exact **physical-dissipation quantum** gate isolated.
5. One-scale robustness: exact **weighted-to-unweighted porosity** and **terminal-uniformity** gates isolated.
6. SAPZ v6: exact **CT3 persistence -> positive Route–T transport residual with same scale/window and epsilon-independent constants** gate isolated.
7. Eigen-gap directional packets: exact **new endpoint inequality to BKM** remains unavailable in indexed public material.
8. IG–Morse/Crofton: exact **direction/topology-to-absolute-amplitude** bridge isolated.
9. DCC: latest internal-QED version itself lists external validation targets; remains conditional/open rather than refuted.

---

# A. Finalized this pass

## A1. Feinstein — Restricted NSE-native Carleson / VACM

File:
`AUDIT_FEINSTEIN_RESTRICTED_CARLESON_VACM_2026-09-06.md`

Status: **FAIL_ROOT**.

Two independent displayed failures:

### Endpoint derivative count

The public ledger uses

\[
\mathcal F=\sum_j2^{3j/2}\|U_j\|_2,
\qquad U_j=P_{e,j}\Delta_j u,
\]

and exports it as a vorticity \(B^0_{\infty,1}\)/BKM norm.

But

\[
\|\Delta_j\omega\|_\infty
\lesssim 2^{3j/2}\|\Delta_j\omega\|_2
\asymp 2^{5j/2}\|\Delta_j u\|_2.
\]

One dyadic derivative \(2^j\) is missing.

### Transport-commutator absorption

From

\[
\|[u\cdot\nabla,P_{e,j}]f\|_2
\le C\varepsilon_j\|\nabla u\|_{BMO}\|f\|_2,
\]

viscous absorption requires

\[
C\varepsilon_j\|\nabla u\|_{BMO}
\lesssim \nu2^{2j},
\]

not merely \(C\varepsilon_j\le\nu/2\).

Commit: `056010c5c04112953f7f757f98751b09b5a10c10`.

---

## A2. Petenchia — Pressure-frequency / internal-frequency latest published line

File:
`AUDIT_PETENCHIA_PRESSURE_FREQUENCY_LATEST_SCOPE_2026-09-06.md`

Status: **SCOPE / CONDITIONAL SURVIVOR**.

Latest paper explicitly adds effective viscosity and anisotropic stresses coupled to an internal frequency field. Its vanishing-regularization theorem assumes a regularization-independent BKM bound

\[
\sup_n\int_0^T\|\omega^n(t)\|_\infty dt<\infty,
\]

and identifies this as the remaining analytic obstacle.

Thus fixed-parameter regularity does not constitute unconditional regularity of classical NSE.

Commit: `c462b6e7a6d52dd31c57453c382ed2553d7210ed`.

---

## A3. Zhang — Weakly regular / double-limit framework

File:
`AUDIT_ZHANG_WEAK_REGULARITY_DOUBLE_LIMIT_FINAL_2026-09-06.md`

Status: **FAIL_ROOT**.

Independent failures:

1. claims uniform \(H^1\) approximate initial-data bound independent of \(N,\varepsilon\) while allowing \(u_0\in L^2\setminus H^1\); this would force the limit datum into \(H^1\);
2. arbitrary high-order differentiation of the PDE while forcing is assumed only \(L^2_{t,x}\);
3. uses an \(L^2_tH^1_x\) energy bound as the \(L^\infty_tH^1_x\) base of a high-order induction;
4. uses a homogeneous linear Stokes-semigroup estimate to export global regularity of the nonlinear NSE without controlling the nonlinear Duhamel term;
5. states the false embedding \(H^s(\mathbb R^3)\subset C^\infty\) for a fixed \(s>3/2\);
6. displays the pressure-Poisson sign opposite to that obtained from its own NSE convention.

The Galerkin/Aubin–Lions weak-solution construction portion may survive separately.

Commit: `7d4b573a7f4585d25ea3e37f7edbbdac282aa4ea`.

---

# B. Narrowed this pass

## B1. Graah — thick / tube / fragmented

File:
`AUDIT_GRAAH_TRICHOTOMY_DISSIPATION_PACKING_2026-09-06.md`

Status: **OPEN_DEEP narrowed**.

If the per-scale theorem is only a standard scale-invariant lower bound

\[
E(r)=r^{-1}\int_{Q_r}|\nabla u|^2\ge c,
\]

then physical payment is only

\[
\int_{Q_r}|\nabla u|^2\ge cr.
\]

For dyadic \(r_n\), \(\sum r_n<\infty\), so infinitely many disjoint events do not contradict finite energy.

Needed repair: radius-independent physical quantum, non-summable payment, or positive-density-time mechanism.

Commit: `634be46d0b0b0b36050d66bd80ad7ae4fc0ada9b`.

---

## B2. One-scale robustness

File:
`AUDIT_ONE_SCALE_ROBUSTNESS_WEIGHTED_POROSITY_GATE_2026-09-06.md`

Status: **OPEN_DEEP narrowed**.

Exact remaining gates:

### weighted -> unweighted bad-scale porosity

\[
\widetilde\Phi_\beta(r)=r^\beta\Phi(r),\quad \beta>2
\]

can tend to zero even if the scale-critical \(\Phi(r)\) remains uniformly bad. The slope-gap theorem must export a quantitative hole in the **unweighted** bad set.

### terminal uniformity

Porosity on every compact slab before \(T\) must yield a good cylinder/scale certificate that remains effective as the slab approaches a first singular time. A scale floor that collapses with \(T-t\) does not close the terminal point.

Commit: `67bddca4df7a3b245059d06e70446b031a64f3ba`.

---

## B3. SAPZ v6

Status: **OPEN_DEEP**.

Version history is already informative:
- v4.3r1 explicitly isolated CT3-(A3) as the only remaining Clay-level PDE target;
- v5/v6 claim Route–T discharges it.

The exact remaining audit theorem is therefore

\[
\boxed{
\text{CT3 persistence at selected scale/window}
\Longrightarrow
\text{strictly positive transport residual}
}
\]

with:
- the same selected scale;
- the same physical contradiction window;
- constants uniform in the mollification/approximation parameter;
- no use of the target concentration as an assumption;
- residual lower bound quantitatively larger than the RNF residual upper budget.

Indexed public summaries do not expose this inequality sufficiently for a verdict.

---

## B4. Eigen-gap directional packet, Nov. 7 version

Status: **OPEN_DEEP**.

The preceding Nov. 2/3 directional-ledger draft publicly exports a spacetime \(L^1_x\) vorticity quantity to smoothness, which is not a BKM endpoint.

The Nov. 7 eigen-gap version instead states that a separate "classical endpoint inequality" converts the final ledger to maximum vorticity. The indexed record does not display that inequality.

Therefore the exact remaining question is:

\[
\boxed{
\text{what norm does the packet ledger control, and by what derivative-correct inequality does it reach }\|\omega\|_\infty?
}
\]

No verdict is exported from the earlier version to the later one without this formula.

---

## B5. IG–Morse / Crofton Proof Pack

Status: **OPEN_DEEP narrowed**.

Director geometry

\[
\xi=\omega/|\omega|
\]

and any topology/Fisher/Crofton quantity built solely from \(\xi\) is invariant under

\[
\omega\mapsto A\omega,
\]

while

\[
\|\omega\|_\infty\mapsto A\|\omega\|_\infty.
\]

Therefore the advertised Campanato->Morrey / \(C_r\to X\) bridge must contain an actual **absolute-amplitude currency**, not only direction topology.

Also \(\xi\) is undefined on the nodal set, so handle birth/death must be audited against zero-vorticity topology changes and cannot automatically be priced as a physical singular event.

---

## B6. Hall DCC

Status: **CONDITIONAL / OPEN_DEEP, scope confirmed by latest public description**.

The June version explicitly says it is conditional and retains two terminal profile regimes.

The July internal-QED version explicitly says external validation remains directed to:
- relative log-shell estimate;
- collar routing;
- record conservation;
- carrier-edge completeness;
- exact PDE inputs.

Therefore these bridges should be treated as unverified obligations rather than silently inherited as theorems.

---

# C. Still open because formula-level public material was not recovered

## C1. Onodera analytical manuscript

Status: **OPEN_DEEP**.

Implementation failure is already proved separately. The analytical PDF still requires actual parameter/order-uniform high-Sobolev closure.

## C2. Stough phi-resonant manuscript

Status: **OPEN_DEEP**.

Indexed abstracts expose no multiplier formula. Required audit remains:
- completeness of resonance split;
- arbitrary phase cancellation;
- low-high and high-high->low interactions;
- amplitude homogeneity;
- no circular dependence of high-Sobolev bound on itself.

---

# Current formula-level open count

After this pass:

\[
\boxed{8\ \text{families remain formula-level open}}
\]

namely:

1. Onodera analytical manuscript;
2. SAPZ v6 Route–T;
3. Hall DCC latest internal closure;
4. Stough phi-resonant;
5. One-scale robustness;
6. Graah trichotomy;
7. Nov. 7 eigen-gap directional packet;
8. IG–Morse/Crofton.

The pressure-frequency and Zhang families have left OPEN_DEEP status, and the latest publicly accessible restricted-Carleson Scale-K/VACM closure has a direct FAIL_ROOT verdict.

---

# New M17 regression rules from this pass

### R21 — Approximation strong-norm inheritance

A parameter-uniform stronger norm on approximants may force the limiting datum into that stronger space. Check this before accepting the bound.

### R22 — Differentiated forcing regularity

Never differentiate the PDE beyond the regularity actually assumed for forcing/coefficient data without an explicit maximal-regularity argument.

### R23 — Derivative count at endpoint

When exporting a velocity packet to a vorticity endpoint, retain

\[
\omega_j\sim 2^j u_j.
\]

### R24 — Commutator coefficient amplitude

Small geometry parameter alone does not absorb

\[
\varepsilon_j M_j E_j
\]

unless \(\varepsilon_j M_j\) is compared with the actual viscous scale.

### R25 — Infinite-event packing requires divergent physical cost

Infinitely many normalized events can have summable unnormalized physical payments.

### R26 — Direction topology cannot control absolute amplitude by itself

Any \(\xi=\omega/|\omega|\) geometry-to-BKM theorem must explicitly import magnitude.

### R27 — Version correction is evidence, not embarrassment

If a later manuscript explicitly isolates a missing theorem, earlier unconditional wording is superseded while surviving partial results remain citable.

---

GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.
