# DSD Audit — Harbeck Equilibrium Depletion / Universal Frequency Envelopes

Date: 2026-09-06
Source: William Harbeck, *Global Regularity for the Three-Dimensional Navier–Stokes Equations via Equilibrium Depletion and Universal Frequency Envelopes*, DOI 10.31224/5814, Nov 2025.
Audit status: **CORE SCALE/NORMALIZATION HINGE FAIL IDENTIFIED; OTHER MODULES REQUIRE SEPARATE AUDIT**

## 1. Claimed architecture

The manuscript develops a large framework using:

- a local geometric depletion ratio;
- a normalized universal cap `\widetilde D≤1`;
- a deterministic frequency-envelope ODE supersolution;
- CKN epsilon-regularity;
- integrated monotonicity and an Osgood inequality;
- whole-space extension.

Because the manuscript is modular and long, this audit records one decisive issue rather than declaring every later module false.

## 2. Definition and scale audit

The manuscript describes a raw depletion functional schematically as

\[
D_{raw}(Q_r)
=
\frac{\iint_{Q_r}|\omega\cdot S\omega|\,dxdt}
{\iint_{Q_r}|\nabla\omega|^2\,dxdt},
\]

up to mollification/cutoff details.

Under the standard Navier–Stokes scaling

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\]

we have

\[
\omega_\lambda=\lambda^2\omega,
\qquad
S_\lambda=\lambda^2S,
\qquad
\nabla\omega_\lambda=\lambda^3\nabla\omega.
\]

Therefore

\[
|\omega\cdot S\omega|\mapsto\lambda^6|\omega\cdot S\omega|,
\]

and

\[
|\nabla\omega|^2\mapsto\lambda^6|\nabla\omega|^2.
\]

Space-time measure scales as `λ^{-5}`, so both numerator and denominator scale as `λ`; their ratio is dimensionless/scale-invariant.

The manuscript contains a displayed scaling discussion in which the numerator is assigned a different power, producing

\[
D_{raw}\sim 1/r,
\]

then states that because the normalization constant is r-independent the r-dependence “exactly cancels” when the Calderón–Zygmund bound is applied.

A constant independent of r cannot algebraically convert `1/r` into a scale-invariant quantity. Either the preceding scaling exponent is wrong (as the standard NSE scaling calculation indicates), or the asserted cancellation is wrong. The manuscript cannot consistently use both statements.

## 3. Normalization versus CKN threshold

The manuscript normalizes a geometric kernel/function so its universal cap becomes a convenient numerical constant such as 1 and elsewhere discusses choosing/renormalizing universal multiplicative factors relative to a CKN epsilon threshold.

DSD rule:

\[
X\le C
\]

can always be rewritten as

\[
\widetilde X:=\alpha X\le\alpha C.
\]

But a regularity criterion is formulated for a **specific physical/scale-invariant quantity** `Y`, not for arbitrary names assigned to a surrogate diagnostic. To infer

\[
Y<\varepsilon_{CKN}
\]

from `\widetilde X≤1`, one needs a fixed bridge

\[
Y\le C_{bridge}\widetilde X.
\]

If `\widetilde X` is rescaled by `α`, the bridge constant rescales by `1/α`. Therefore arbitrary normalization cannot manufacture CKN smallness.

In short:

\[
\boxed{
\text{renaming/rescaling a dimensionless diagnostic does not create epsilon-regularity.}
}
\]

Any threshold comparison must be invariant under such reparameterization.

## 4. Universal-cap audit

A spherical integral or normalized kernel cap can establish a geometric operator constant. But a bound such as

\[
0\le \widetilde D\le1
\]

is only useful for regularity if `1` is quantitatively below a **fixed** critical coupling threshold in the original physical inequality. If saturation at `\widetilde D=1` is allowed, a universal cap of 1 is not by itself a strict depletion margin.

Thus the nondegeneracy/strict-margin theorem is a separate hinge from the existence of a normalized cap.

## 5. Whole-space and envelope modules

The deterministic frequency-envelope system may contain independent useful estimates. It should be audited separately for:

- whether the envelope is an a priori supersolution with constants independent of unknown higher norms;
- whether the claimed exponential tail is stronger than what the NSE energy inequality supplies;
- whether the R3 extension hides a Poincaré/far-field compactness assumption;
- whether weak lower semicontinuity applies to every nonlinear normalized ratio used.

This file does not prejudge those modules.

## 6. DSD verdict

A decisive inconsistency is present in the scale/normalization bridge used to connect the geometric diagnostic to the regularity mechanism.

\[
\boxed{
\text{Scale-dependent raw ratio + scale-independent constant cannot become scale-invariant by normalization.}
}
\]

Furthermore, arbitrary normalization cannot be used to cross a fixed CKN epsilon threshold without tracking the inverse change in the bridge constant.

Therefore the current global closure is not established even if later frequency-envelope calculations are provisionally accepted.

Global regularity remains unproved.
