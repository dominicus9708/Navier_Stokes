# DSD Deep Audit — One-Scale Robustness / Porosity: Weight-to-Critical-Smallness Gate

Date: 2026-09-06
Target: *A One-Scale Robustness Framework for 3D Navier-Stokes: Pressure-Free epsilon-Regularity, Porosity, and Terminal Transfer* (2025 family around Zenodo 16993830 / 17162443 / 17163225).
Status: **OPEN_DEEP / WEIGHT-TO-CRITICAL + TERMINAL-SCALE UNIFORMITY GATES**

## 1. Public chain

The public description organizes the argument as:

1. pressure-free one-cylinder epsilon-regularity for a critical diagnostic `Phi`;
2. weighted diagnostic

\[
\widetilde\Phi_\beta(r)=r^\beta\Phi(r),\qquad \beta>2,
\]

with a slope-gap inequality, BV-on-bands and IMS overlap;
3. porosity of bad radii;
4. terminal-time transfer with a uniform scale floor;
5. weak-strong continuation.

The present audit isolates the two export steps most likely to carry a hidden quantifier change.

## 2. Weight-to-critical firewall

If `Phi(r)` is the actual scale-critical regularity quantity, then multiplying by `r^beta` deliberately destroys scale invariance:

\[
\widetilde\Phi_\beta(r)=r^\beta\Phi(r).
\]

As `r->0`, weighted smallness may occur even when `Phi(r)` is not small.

For example, if

\[
\Phi(r)\equiv1,
\]

then

\[
\widetilde\Phi_\beta(r)=r^\beta\to0,
\]

while the critical quantity never enters any small epsilon threshold.

More generally,

\[
\widetilde\Phi_\beta(r)\ll1
\not\Rightarrow
\Phi(r)\ll1.
\]

Therefore slope/porosity information in the weighted variable can activate a one-scale epsilon criterion only through an explicit theorem returning to the **unweighted critical** quantity.

## 3. What porosity must actually produce

Let the bad critical scales be

\[
\mathcal B=\{r:\Phi(r)\ge\varepsilon_*\}.
\]

A useful porosity theorem must imply that near every putative singular point there exists a scale `r` in the admissible terminal window with

\[
\boxed{\Phi(r)<\varepsilon_*}.
\]

It is insufficient to show merely that

\[
\widetilde\Phi_\beta(r)<\widetilde\varepsilon
\]

or that weighted bad radii occupy less logarithmic measure.

The export theorem should display the dependence of the chosen `r` on:

- the terminal slab;
- the distance to the putative first singular time;
- the BV/IMS constants;
- far-field pressure/harmonic-tail terms.

## 4. Terminal uniform scale-floor firewall

At a first potential singular time `T`, regularity may hold on every preterminal compact slab while the admissible regularity scale shrinks to zero as `t upward T`.

Thus the statement

\[
\forall t<T\ \exists r(t)>0:\Phi(r(t);t)<\varepsilon_*
\]

does not imply a terminal scale floor

\[
\inf_{t\uparrow T}r(t)>0.
\]

But a Vitali/finite-cover terminal argument that uses a uniform positive scale floor must prove precisely such uniformity or use a scale-free alternative.

The danger is circular:

\[
\text{uniform terminal scale}
\]

can be nearly equivalent to excluding the concentration one is trying to rule out.

## 5. Pressure-free criterion audit

Eliminating pressure from the displayed diagnostic is acceptable only if the harmonic/far-field pressure information has been completely exported into controlled remainder terms.

An exact cancellation in a *renormalized defect* is useful, but it must not remove pressure from one formula while leaving uncontrolled harmonic-tail data in the terminal transfer.

Therefore the pressure-free criterion must be accompanied by a uniform estimate for all residual pressure/harmonic contributions on the same scale selected by porosity.

## 6. DSD verdict

No direct contradiction with the currently accessible public description has been established. The decisive obligations are now exact:

\[
\boxed{
\begin{aligned}
&\text{weighted porosity}\Rightarrow\text{actual unweighted critical epsilon-smallness},\\
&\text{preterminal good scales}\Rightarrow\text{terminally usable scale with uniform constants}.
\end{aligned}}
}
\]

Status:

\[
\boxed{\text{OPEN_DEEP — WEIGHT-TO-CRITICAL AND TERMINAL-UNIFORMITY GATES.}}
\]

Survivors worth preserving if formulas check:

- matched-cutoff pressure cancellation;
- BV-on-dyadic-band organization;
- IMS shell-overlap estimate;
- a genuine pressure-free one-scale criterion if its hypotheses are exactly verified.

New regression test:

\[
\boxed{
R26:\ \text{porosity/slope of a weighted diagnostic cannot replace epsilon-smallness of the critical diagnostic.}
}
\]

GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.
