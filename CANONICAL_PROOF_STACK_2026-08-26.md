# Canonical proof stack — DSD Navier–Stokes

Date: 2026-08-26

Purpose: compress the current proof attempt into the smallest live theorem stack. Dated branch notes remain evidence/audit records, but future work should identify which module below it strengthens.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]

---

## M0. Upstream singularity reduction

**Claim type:** W1-CONDITIONAL / FINAL AUDIT REQUIRED.

Starting from a candidate finite-time singularity, the repository routes a major retained corridor into a recurrent W1 Leray dynamics class.

The final project still requires a complete upstream audit proving that no admissible singular branch escapes this reduction.

This module is therefore not marked globally complete.

---

## M1. Recurrent W1 critical endpoint

**Claim type:** DERIVED INSIDE W1.

The nontrivial recurrent W1 endpoint carries a positive critical cubic residue

\[
\boxed{\mathscr R_3>0.}
\]

The general robust interpretation is Abel/Mellin, not automatically a pointwise weak-`L3` distribution limit.

This module absorbs the former periodic/aperiodic, coherent/oscillatory, strain/contact, turnover/export and Bernoulli/vorticity subbranches as diagnostics of the same endpoint class.

---

## M2. Exact critical boundary coordinate

**Claim type:** DERIVED IDENTITY / DERIVED W1 ENDPOINT.

Define

\[
\mathcal E_\lambda(U)
=
\frac12\int (|U|^2-\lambda^2)_+dY,
\]

\[
\boxed{K(U;\lambda)=\lambda\mathcal E_\lambda(U).}
\]

Then invariant W1 averaging gives

\[
\boxed{
\lim_{\lambda\downarrow0}
\langle K(U;\lambda)\rangle_\mu
=
\frac{\mathscr R_3}{3}>0.
}
\]

The exact amplitude-state transport is

\[
\boxed{
\partial_sK
-\frac\lambda2\partial_\lambda K
=
\lambda(J_P-\nu D_\lambda).
}
\]

This is the canonical DSD interior-to-boundary relation.

---

## M3. Physical high-amplitude tail correspondence

**Claim type:** DERIVED IDENTITY / COMPARISON LEMMA.

For a physical threshold `L`, define

\[
K_L^{phys}(t)
=
\frac L2\int(|u|^2-L^2)_+dx.
\]

Under the Leray transform,

\[
\boxed{
K(U(s);L\sqrt{T_*-t})
=K_L^{phys}(t).
}
\]

The `K` tail is quantitatively comparable to the high-amplitude weak-`L3` tail.

Thus the DSD boundary defect is not an extra nonstandard observable; it is a standard critical high-amplitude concentration coordinate written in state-boundary form.

---

## M4. High-tail absorption / continuation

**Claim type:** COMPLETED DERIVED LEMMA.

There is a viscosity-dependent `epsilon_nu>0` such that if, for one finite `L`,

\[
\boxed{
\sup_{t_0<t<T_*}
\|u(t)\mathbf1_{|u(t)|>L}\|_{L^{3,\infty}}
<\varepsilon_\nu,
}
\]

then the high-amplitude nonlinear term is absorbed by viscosity in the `H1` estimate and

\[
\sup_{t_0<t<T_*}\|\nabla u(t)\|_2<\infty.
\]

Hence the solution continues past `T*`.

Therefore

\[
\boxed{
\text{critical high-tail smallness}
\Longrightarrow
\text{no blow-up at }T_*.
}
\]

Reference: `DSD_W1_CRITICAL_HIGH_AMPLITUDE_TAIL_ABSORPTION_LEMMA_2026-08-26.md`.

---

## M5. Single open theorem

**Claim type:** OPEN MILLENNIUM-LEVEL BRIDGE.

The only live endpoint implication is to force the hypothesis of M4 from the retained finite-energy/W1 structure.

A sufficient canonical form is

\[
\boxed{
\lim_{L\to\infty}
\sup_{t_0<t<T_*}
K_L^{phys}(t)=0.
}
\]

Equivalent or sufficient substitutes include:

- high-amplitude weak-`L3` tail eventually below the M4 threshold;
- defect-aware compactness controlling `K`;
- pressure-pump absorption on the strict interior amplitude band;
- strong-critical upgrade to an established continuation class;
- direct exclusion of the large weak-critical recurrent W1 ancient class.

This is tracked in GitHub Issue #2.

---

# Dependency graph

\[
\boxed{
M0
\Longrightarrow
M1
\Longrightarrow
M2
\Longleftrightarrow
M3
\stackrel{\mathbf{M5\ OPEN}}{\Longrightarrow}
M4
\Longrightarrow
\text{continuation}.
}
\]

The project cannot skip M5 by renaming it as a DSD axiom.
Doing so would merely hide the missing standard-mathematics theorem.

---

# What is no longer a top-level module

The following are historical/diagnostic submodules and should not be reopened as separate terminal branches unless new mathematics makes them necessary:

- periodic vs aperiodic W1;
- `H2` coherence vs derivative escalation;
- strain eigenvalue and maximum-vorticity contact branches;
- Bernoulli surplus and pressure-free weighted-vorticity current;
- Lamb/Hodge commutator and BMO witnesses;
- turnover/export and finite-parent pressure routes;
- amplitude-level pressure-pump/two-sector geometry;
- terminal `1/r` trace constructions.

Their role is to constrain or realize M1–M3, not to replace M5.

---

# Audit locks

Do not use the following without new hypotheses:

1. similarity-radial current = material flux;
2. `R3/6` = new physical power source;
3. Mellin residue = pointwise `lim lambda^3 N(lambda)`;
4. large `H2` capacity = actual reformation;
5. periodic omega-limit tail automatically inherited on fixed physical annuli;
6. pointwise pressure sign as a gauge-invariant certificate;
7. infinitely many normalized events = infinite physical energy cost;
8. weak-`L3` upper bound contradicts logarithmic cubic concentration.

---

# Definition of proof completion

A global-regularity claim requires all of:

1. prove M5;
2. use it to close M1–M4 and eliminate the W1 endpoint;
3. complete the M0 upstream branch-completeness audit from arbitrary admissible blow-up;
4. independently recheck all external theorem hypotheses and every limiting argument;
5. only then promote the result beyond a conditional DSD closure.

Until then, this file is a compact research ledger, not a claimed solution to the Millennium Problem.