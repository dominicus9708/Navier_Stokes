# DSD M5-322 — Huang Atomic Rigidity Torus-to-R3 Transfer Ledger and Infinity-Tightness Gate

Date: 2026-08-30

Parent: `DSD_M5_321_R3_FULL_TIME_ENDPOINT_ENERGY_MEASURE_AND_SHRINKING_BALL_ATOM_EXTRACTION_2026-08-30.md`

Status: **CURRENT-LITERATURE TRANSFER AUDIT / SEVERAL TORUS INPUTS IN HUANG 2026 HAVE DIRECT R3 ANALOGUES, INCLUDING LERAY PROJECTION, PRESSURE RIESZ TRANSFORMS, LOCAL HODGE PACKETS, AND NOW THE FULL-TIME ENDPOINT ENERGY MEASURE / THE NONTRIVIAL TRANSFER GATES ARE THE TIGHTNESS OF THE SINGLE BACKWARD ADJOINT AGAINST SPATIAL ESCAPE AND GLOBAL DELAYED OSEEN SECOND-ORDER ESTIMATES WITHOUT A COMPACT-DOMAIN SPECTRAL GAP / NO R3 VERSION IS CLAIMED PROVED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-320 identified Huang 2026 atomic full-tail rigidity as a potentially decisive result for the screened-affine energy-atom branch.

M5-321 closed the first missing bridge by proving the full-time endpoint kinetic-energy measure and atom extraction in `R^3`.

This note decomposes the remaining `T^3 -> R^3` transfer problem.

---

## 2. Input A: Leray projection

On the torus Huang uses the periodic Leray projection.

On `R^3` the standard Fourier Leray projection is

\[
\widehat{\mathbb Pf}(\xi)
=\left(I-\frac{\xi\otimes\xi}{|\xi|^2}\right)\hat f(\xi).
\]

It is bounded on `L^2` and the usual `L^p`, `1<p<infty`, classes.

Thus the mere existence of the divergence-free projection is not a transfer obstruction.

Status: **GREEN at the functional-analytic level.**

---

## 3. Input B: pressure representation

The torus proof uses periodic Riesz transforms.

In `R^3`,

\[
p=\mathcal R_i\mathcal R_j(u_i u_j)
\]

with the standard Calderon--Zygmund bounds.

M5-321 already used this representation to construct the full-time endpoint energy measure.

Status: **GREEN.**

---

## 4. Input C: endpoint energy measure

Huang starts from a unique full-time endpoint energy measure.

M5-321 proves in the present whole-space finite-energy smooth-preterminal setting that

\[
|u(t)|^2dx\stackrel{*}{\rightharpoonup}\mu_*
\]

along the full time variable against compactly supported tests.

Moreover the saturated screened rotor gives

\[
\mu_*(\{a\})>0
\]

on the no-center-turnover branch.

Status: **GREEN.**

---

## 5. Input D: nested local Hodge packets

Huang's atom-selected packets are produced by local Hodge projections on nested balls.

The repository already uses Bogovskii/local-Hodge constructions on Euclidean balls and annuli.

Such constructions are local and scale invariant. They do not require global periodicity.

The packet orthogonality/frozen-ball ordering from Huang still needs to be reproduced exactly, but the underlying local projection machinery exists in `R^3`.

Status: **GREEN/YELLOW: local operator available; exact full-tail catalogue not yet rederived.**

---

## 6. Input E: Oseen evolution family

The relevant linearized divergence-free equation is

\[
\partial_t z
-\nu\Delta z
+\mathbb P[(u\cdot\nabla)z+(z\cdot\nabla)u]
=0.
\]

For every compact preterminal interval with smooth parent `u`, standard whole-space parabolic theory gives a well-defined Oseen evolution.

The transfer issue is not local existence.

The issue is obtaining the **uniform terminal-tail estimates** used by Huang as the parent approaches `T_*`.

Status: **YELLOW.**

---

## 7. First genuine R3 danger: adjoint escape to infinity

On the compact torus every `L^2`-bounded sequence is automatically spatially tight.

On `R^3`, weak `L^2` compactness alone allows mass to escape to spatial infinity.

Huang extracts one backward adjoint from the entire atom-selected packet tail and then uses terminal concentration plus Cauchy saturation to lock that adjoint to all late packets.

For the same argument in `R^3`, one must show that the normalized adjoint sequence does not lose its mass at infinity.

The atom strongly localizes its terminal pairing near `a`, suggesting tightness, but this requires an explicit estimate.

Define schematically the adjoint tightness defect

\[
\boxed{
\mathfrak T_{adj}(R)
:=\limsup_n
\int_{|x-a|>R}|\psi_n(x)|^2dx.
}
\]

The desired gate is

\[
\boxed{
\lim_{R\to\infty}\mathfrak T_{adj}(R)=0.
}
\]

Status: **OPEN TRANSFER LEMMA.**

---

## 8. Why the energy atom may help adjoint tightness

The local Hodge packets are supported on nested balls shrinking to `a`.

The common adjoint is normalized through pairings with these packets.

If an order-one portion of adjoint mass escaped to infinity while the terminal packet support shrank to `a`, Cauchy saturation would need to reconcile a localized pairing with a delocalized unit vector.

This suggests a concentration-compactness dichotomy:

\[
\boxed{
\text{localized saturated pairing}
\Longrightarrow
\text{adjoint tightness}
\lor
\text{loss in the Cauchy saturation constant}.
}
\]

Huang's torus proof gets tightness for free from compactness; in `R^3` this implication must be quantified.

---

## 9. Second genuine R3 danger: no spectral gap

On `T^3`, the Stokes operator has discrete spectrum modulo constants and a compact-domain spectral gap on the mean-free sector.

On `R^3`, low frequencies accumulate at zero.

The delayed second-order action

\[
\int\|\Delta U(t,s)q\|_2^2dt
\]

is designed to avoid the ordinary initial parabolic singularity, but low-frequency behavior can still differ between compact and whole-space settings.

Therefore one must check every step that uses

- Poincare inequality;
- compact resolvent;
- spectral gap;
- periodic mean decomposition;
- global elliptic inversion.

The whole-space replacements may use homogeneous Sobolev/Fourier splitting and the packet's compact localization/zero-mean properties.

Status: **OPEN/TECHNICAL.**

---

## 10. Potential low-frequency repair from existing packet structure

The repository has already proved for compact divergence-free localized packets that

\[
\int f=0
\]

and quantitatively suppresses frequencies `|xi| << 1/r`.

Thus Huang's atom-selected Euclidean Hodge packets may inherit a natural low-frequency cancellation replacing the torus Poincare gap.

A promising bridge is

\[
\boxed{
\text{compact solenoidal zero mean}
\Longrightarrow
\|P_{\le a/r}q\|_2\le C a^{5/2}\|q\|_2.
}
\]

This is exactly the type of estimate already recorded in the localized phase-space ledger.

Hence the absence of a global spectral gap may be reparable **on the selected packet class**, even though it cannot be repaired for arbitrary `L^2(R^3)` data.

---

## 11. Transfer ledger

Current status:

\[
\boxed{
\begin{array}{c|c}
\text{ingredient}&\text{R3 status}\\
\hline
\text{full-time endpoint measure}&\text{GREEN (M5-321)}\\
\text{energy atom extraction}&\text{GREEN (M5-321)}\\
\text{Leray projection}&\text{GREEN}\\
\text{pressure CZ/Riesz}&\text{GREEN}\\
\text{local Hodge packets}&\text{GREEN/YELLOW}\\
\text{Oseen evolution existence}&\text{GREEN on compact preterminal intervals}\\
\text{adjoint spatial tightness}&\text{OPEN}\\
\text{uniform full-tail Oseen estimates}&\text{OPEN}\\
\text{delayed H2 parent budget comparison}&\text{OPEN}
\end{array}
}
\]

---

## 12. Formation/DSD separation

The formation-level contribution here is the decomposition of the transfer problem into independently describable gates.

No new proof rule is introduced.

The DSD audit role is only to prevent the statement

\[
\text{torus theorem is local, therefore it holds on R3}
\]

from being accepted without the infinity and low-frequency checks.

---

## 13. Next high-value calculation

The most direct next calculation is to combine

1. atom-localized Hodge packets;
2. the existing zero-mean low-frequency suppression;
3. the backward Oseen energy identity;

and prove an `R^3` adjoint tightness/low-frequency lemma.

If successful, the remaining transfer gap would be primarily the delayed second-order regularity estimate.

---

## 14. Verdict

The torus-to-whole-space transfer is **plausible but not proved**.

The current work narrows the genuinely new issues to

\[
\boxed{
\text{adjoint infinity tightness}
\quad+\quad
\text{packet-class low-frequency/delayed Oseen H2 control}.
}
\]

This is significantly narrower than redoing the entire atomic-rigidity construction from scratch.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
