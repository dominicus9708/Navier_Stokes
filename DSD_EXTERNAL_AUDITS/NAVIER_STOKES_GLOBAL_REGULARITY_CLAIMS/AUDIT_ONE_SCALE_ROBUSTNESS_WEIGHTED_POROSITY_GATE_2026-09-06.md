# DSD Deep Audit Gate — One-Scale Robustness / Weighted Porosity / Terminal Transfer

Date: 2026-09-06
Source family: *A One-Scale Robustness Framework for 3D Navier–Stokes: Pressure-Free epsilon-Regularity, Porosity, and Terminal Transfer* (2025 versions around Zenodo 16993830 / 17162443 / 17163225).

## Current status

**OPEN_DEEP, but reduced to two exact quantitative gates.**

No final failure is asserted without the formula-level slope-gap and terminal-transfer text.

---

## Public proof chain

The public description organizes the proof as:

1. one-cylinder pressure-free epsilon-regularity for a critical diagnostic
   \[
   \Phi(r)=E(r)+\kappa C(r)^{2/3};
   \]
2. introduce
   \[
   \widetilde\Phi_\beta(r)=r^\beta\Phi(r),\qquad \beta>2;
   \]
3. a slope-gap finite-difference inequality on bad radii + BV-on-bands + IMS shell-overlap + flux absolute continuity forces **uniform porosity** of bad scales;
4. matched-cutoff local-energy subtraction transfers interior smallness to the terminal time;
5. Vitali selection at a uniform scale floor excludes a first singular time.

---

# Gate 1 — weighted slope must create holes in the *unweighted critical* bad set

The epsilon-regularity gate is triggered by smallness of the scale-critical quantity \(\Phi\), not merely the weighted diagnostic \(r^\beta\Phi\).

There is an immediate firewall:

Take an abstract scale profile

\[
\Phi(r)\equiv\varepsilon_*>0
\]

for all sufficiently small \(r\), with \(\varepsilon_*\) at or above the bad-scale threshold.

Then **every small scale is bad** in the critical sense, but

\[
\widetilde\Phi_\beta(r)
=\varepsilon_*r^\beta\to0.
\]

Hence

\[
\boxed{
\widetilde\Phi_\beta(r)\to0
\not\Rightarrow
\Phi(r)\to0
}
\]

and, more generally, smallness or BV control of the weighted diagnostic does not by itself create porosity of the unweighted bad set.

### What the manuscript must prove

The advertised slope-gap theorem must contain an **unweighted quantitative consequence**, schematically:

\[
\Phi(r)\ge\varepsilon_*
\quad\Longrightarrow\quad
\text{a fixed weighted slope/variation cost that cannot occur at all nearby radii}.
\]

The constants must remain uniform as \(r\downarrow0\).

If the proof only shows decay/smallness of \(r^\beta\Phi(r)\), the porosity export does not reach the critical epsilon-regularity hypothesis.

This is the same DSD firewall as "normalization cannot manufacture epsilon-smallness."

---

# Gate 2 — compact-slab porosity must survive to the terminal time with a uniform scale floor

Porosity for every compact slab \([0,T-\delta]\) is not yet enough to exclude a first singularity at \(T\).

The final Vitali/terminal step requires a radius

\[
r_* >0
\]

or an equivalent quantitative selection rule that remains usable as \(\delta\downarrow0\).

If the available good radius satisfies

\[
r_*(\delta)\downarrow0
\]

without a uniform terminal modulus, then the proof has not produced a certificate at time \(T\); it has only regularized times strictly before \(T\), which is already known for a first-singular-time argument.

Therefore the terminal bridge must prove, without assuming endpoint regularity,

\[
\boxed{
\text{porosity + data-only flux modulus}
\Longrightarrow
\text{terminal good cylinder with scale-independent epsilon certificate}.
}
\]

The public description explicitly advertises a "data-only terminal slab modulus" and a "uniform scale floor". Those are therefore the exact formula-level objects that must be checked.

---

# Pressure-free issue

A pressure-free criterion can be legitimate if the harmonic/far-field pressure terms have been eliminated by an exact identity or bounded by velocity-only quantities with scale-uniform constants.

The public summary claims an exact far-field cancellation in a renormalized defect. The audit must distinguish:

\[
\text{exact cancellation of one pressure contribution}
\]

from

\[
\text{complete removal of all harmonic-tail information needed by the LEI}.
\]

No failure is asserted here until the displayed subtraction identity is available.

---

# Survivor value

Potentially valuable even if the global assembly fails:

- matched-cutoff subtraction of local energy inequalities;
- pressure near/far decomposition;
- BV-on-dyadic-bands organization;
- IMS overlap accounting;
- a genuinely unweighted slope-gap theorem, if verified;
- a terminal-time transfer lemma with data-only modulus, if verified.

These would be directly relevant to M17-301 growing-lag/terminal genealogy.

---

# M17 regression

For every weighted scale diagnostic \(r^\beta X(r)\):

\[
\boxed{
\text{small weighted diagnostic}
\neq
\text{small critical diagnostic}.
}
\]

The proof must export back to the unweighted quantity consumed by the continuation theorem.

Likewise, every fixed-lag/fixed-slab certificate used near a terminal singular time must have a **uniform terminal quantifier** before it can close a first-singular-time contradiction.

GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.
