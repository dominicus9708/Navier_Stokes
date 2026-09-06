# Comparative DSD Frontier — Internal M17 vs external 3D Navier–Stokes regularity claims

Date: 2026-09-06  
Scope: current repository M17 chain compared with the external claimed-resolution manuscripts audited in this directory.  
Status: **COMPARATIVE AUDIT — NOT A CLAIM OF GLOBAL REGULARITY**

## 1. Executive verdict

The internal M17 chain is **not ahead of the established mathematical literature in theorem strength**: it has not proved global regularity, and the growing-lag ancestor/recharge gate remains open.

It is, however, ahead of several audited claimed-resolution manuscripts in a narrower and important sense:

\[
\boxed{
\text{nonlocal leakage, scale dependence, and conditional gates are kept explicit rather than silently closed.}
}
\]

The comparison must therefore distinguish:

- `THEOREM_STRENGTH`: still OPEN internally;
- `AUDIT / DEPENDENCY RESOLUTION`: internal M17 is stronger than the audited claimant chains at several decisive hinges;
- `NOVELTY PRIORITY`: not asserted without a separate literature-priority search.

## 2. Internal frontier: M17-299 / M17-300

### M17-299 — polynomial packet scale/amplitude floor

On an infinite shell-relevant subfamily, exponentially small packets carrying a fixed fraction of the nonsummable shell `H^2` numerator cannot remain arbitrarily tiny. The route yields schematically

\[
r_j\gtrsim (\log R_j)^{-1/2},
\]

and a shell-relevant packet amplitude floor of the form

\[
a_j\gtrsim R_j^{-2}(\log R_j)^{-4/3-\varepsilon/2}(\log\log R_j)^{-1/2}.
\]

This converts a beyond-all-orders tiny-carrier scenario into a polynomial/slow-log ancestor problem.

### M17-300 — fixed-annulus ancestor/recharge dichotomy

For a localized rescaled packet `f_j=chi V_j` on the no-subscale/higher-regularity branch, the repository has

\[
\|\Delta f_j(0)\|_2^2\ge h_0,
\qquad
\|f_j(0)\|_2\le C_0,
\qquad
\|f_j(0)\|_{H^3}\le C_3.
\]

Low and high Fourier tails cannot carry all Laplacian charge, so one obtains a **fixed annulus**

\[
\mathcal B=\{\lambda_-\le|\xi|\le\lambda_+\}
\]

with

\[
\|P_{\mathcal B}f_j(0)\|_2\ge c_B>0.
\]

The localized equation is retained as

\[
\partial_\tau f_j-\Delta f_j=F_j,
\]

with

\[
F_j=\chi\mathcal N_j
-2\nabla\chi\cdot\nabla V_j
-(\Delta\chi)V_j.
\]

Thus coefficient forcing and cutoff/interface leakage are not discarded.

For every **fixed** rescaled lag `T`, Duhamel yields the dichotomy

\[
\int_{-T}^0e^{-\lambda_-^2(-s)}
\|P_{\mathcal B}F_j(s)\|_2\,ds
\ge c_B/2,
\]

or

\[
\|P_{\mathcal B}f_j(-T)\|_2
\ge(c_B/2)e^{\lambda_-^2T}.
\]

The unresolved gate is the passage from fixed `T` to

\[
T_j\asymp\log R_j.
\]

No global theorem is claimed before that gate is closed.

## 3. Comparison with Pavesi

Pavesi's unconditional bridge uses a universal spectral-flux estimate with a claimed `1/K` gain.

The explicit six-mode certificate in this directory gives

\[
E=3,\qquad E_{>1}=1,\qquad \Pi(1)=-2,
\]

and amplitude scaling contradicts the data-independent estimate.

Appendix B also promotes geometric rarity of near-cancelling triads into deterministic `1/K` suppression without an operator estimate.

**M17 advantage:** M17-300 does not infer small spectral forcing from phase-space rarity. It retains

\[
P_{\mathcal B}F_j
\]

as an explicit recharge/leakage branch.

Status:

\[
\boxed{
\text{Pavesi universal flux closure: FALSE AS STATED; M17 analogous leakage gate: OPEN but honestly retained.}
}
\]

## 4. Comparison with Balawi

Balawi's core width-3 paraproduct lemma replaces the nonlinear output at shell `j` by a budget involving only neighboring shells `j±3`.

Standard Bony decomposition contains:

- low-high terms with the full low prefix `S_{j-1}u`;
- high-high near-cancellation producing much lower output.

Therefore output shell localization does not imply both inputs lie in `j±3`.

**M17 advantage:** the localized forcing ledger explicitly keeps nonlocal coefficient and interface leakage. The M17 chain is not allowed to replace this forcing by a nearest-neighbor band without a symbol-level estimate.

Status:

\[
\boxed{
\text{Balawi finite-width nonlinear closure: FALSE; M17 regression test passed so far.}
}
\]

## 5. Comparison with Nwankpa

Nwankpa attempts

\[
L^2\text{ energy}
\to L_t^pL_x^3\text{ control}
\to L_t^\infty L_x^3
\to \text{ESS regularity}.
\]

The central nonlinear `L^3` test states that the pressure term vanishes by incompressibility. For the natural test `phi=|u|u`,

\[
\nabla\cdot(|u|u)=u\cdot\nabla|u|
\]

is generally nonzero. Thus

\[
\int\nabla p\cdot |u|u
=-\int p\,u\cdot\nabla|u|
\]

does not vanish merely from `div u=0`.

**M17 advantage:** no global `L_t^infty L_x^3` endpoint is manufactured from energy interpolation, and pressure/nonlocal forcing is not dropped by a false divergence-free test.

Status: **SAFE CORE-HINGE FAIL**.

## 6. Comparison with Cox

Cox defines a purported minimal blow-up threshold schematically by

\[
M_*=\inf\{M>0:\exists u\text{ suitable with }\sup_{t<T(u)}\|u(t)\|_3>M\}.
\]

Under the displayed quantifier this infimum is zero for any nonzero suitable solution; restricting to singular solutions does not repair it, since a finite-time singular solution cannot have a finite uniform endpoint `L^3` bound. Yet the subsequent APMS extraction uses `M_*>0`.

**M17 advantage:** the current packet route does not depend on a silently positive critical minimal element generated by this definition. It keeps its contradiction assumptions and packet extraction gates separately audited.

Status: **SAFE DEFINITION/QUANTIFIER HINGE FAIL**.

## 7. Comparison with Permana / Ibrahim / Lathief

The later geometric-depletion/T3 framework explicitly names decisive statements as hypotheses, including turbulence alignment, a degenerate weighted Moser condition, and a nonlinear cancellation/topological damping bridge.

These are not automatically false. The correct classification is

\[
\boxed{\text{CONDITIONAL SUFFICIENT-STRUCTURE PROGRAM}.}
\]

The error would be to promote those hypotheses to an unconditional theorem without proving them from NSE dynamics.

**M17 advantage:** analogous alignment/damping behavior is not installed as a universal law. Failed direct coercivity routes and payer/tail branches are retained as barriers.

## 8. Comparison with Aksman discrete-vorton continuum bridge

Finite-dimensional discrete regularity does not by itself produce a mesh-uniform continuum `L^infty` vorticity estimate. Uniform reconstruction stability, approximation error, and nonlinear consistency must survive `h->0` with constants independent of `h`.

The latest discrete-vorton formulation explicitly places several of these as hypotheses, so it should be classified as a **conditional continuum bridge**, not automatically as a false discrete theorem.

**M17 advantage:** the spectral band is extracted directly inside the continuum localized PDE from `H^2/H^3` information; it does not use a finite-dimensional norm-equivalence constant as a continuum regularity bound.

## 9. Comparison with Harbeck

The audited scale/normalization bridge contains a conflict between a claimed scale behavior of the raw depletion ratio and a subsequent scale-independent normalization, and a normalized universal cap cannot by itself manufacture CKN epsilon-smallness.

**M17 advantage:** rescaled packet quantities and their costs are tracked at the physical/intrinsic scale; numerical normalization is not used as a substitute for a strict critical smallness margin.

This comparison concerns the identified hinge only; the manuscript's many independent frequency-envelope modules require separate audits.

## 10. Comparison with Onodera implementation package

The public implementation audit found that the main driver repeatedly computes derivative norms from the same initial projected Fourier array while updating proxy scalar recurrences, rather than evolving the NSE velocity state.

Thus the code package cannot serve as an NSE trajectory certificate in that form.

**M17 advantage:** internal scripts/certificates are used only to verify finite algebraic or analytic subclaims; they are not promoted into PDE evolution proofs unless the evolved state and convergence bridge are present.

## 11. What is genuinely ahead now

Relative to the audited claimed-resolution manuscripts, the internal chain is ahead on four concrete methodological points:

1. **Leakage completeness** — low-high, high-high-to-low, coefficient, cutoff and interface payments are not deleted by locality slogans.
2. **Quantifier discipline** — fixed-lag statements are not upgraded to growing-lag statements; finite or conditional statements stay labeled.
3. **Scale discipline** — normalization and rescaling do not create smallness or uniform constants for free.
4. **Barrier conversion** — failed proof mechanisms are kept as regression tests for the next route rather than hidden.

The strongest current original-looking internal reduction is the M17-299 -> M17-300 chain:

\[
\text{shell H2 mass}
\to\text{polynomial carrier floor}
\to\text{fixed intrinsic Fourier band}
\to\text{ancestor growth OR recharge/leakage payment}.
\]

No literature-priority claim is made here.

## 12. What remains before the internal chain can surpass the external literature in theorem strength

The immediate open gate is:

\[
\boxed{
\text{upgrade fixed-lag M17-300 to a controlled }T_j\asymp\log R_j\text{ ancestor/recharge statement.}
}
\]

A valid closure must prove at least one of:

- growing-lag band persistence with constants uniform in `j`;
- a summable/contradictory lower bound on cumulative recharge/interface leakage;
- an alternative rigidity mechanism that closes the same genealogy branch.

Until then:

\[
\boxed{\text{GLOBAL REGULARITY = OPEN.}}
\]
