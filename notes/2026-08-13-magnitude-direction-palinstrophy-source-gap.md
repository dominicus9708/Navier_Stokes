# Magnitude-direction palinstrophy split and a strict Sobolev source-depletion factor

Date: 2026-08-13

Status: **DERIVED SOURCE-DEPLETION INEQUALITY / RELATED TO GEOMETRIC DEPLETION / OPEN LOCALIZED CLOSURE**.

This note refines the generic enstrophy-production estimate by observing that the scalar Sobolev inequality for the vorticity magnitude uses only the part of palinstrophy devoted to changing the **magnitude** of vorticity.  Palinstrophy spent rotating the vorticity direction cannot simultaneously be used in that Sobolev channel.

No novelty claim is made without a dedicated literature audit.  The inequality is used here as an internal strict-gap mechanism compatible with the established geometric-depletion theory.

---

## 1. Robust magnitude/angular decomposition

Let

\[
\rho=|\omega|.
\]

Define total palinstrophy

\[
\boxed{P=\int_{\mathbb R^3}|\nabla\omega|^2dx.}
\]

Define the magnitude part robustly by

\[
\boxed{P_{\rm mag}=\int_{\mathbb R^3}|\nabla|\omega||^2dx.}
\]

The Kato inequality gives

\[
P_{\rm mag}\le P.
\]

Define the complementary angular/projective reserve

\[
\boxed{P_{\rm ang}=P-P_{\rm mag}\ge0.}
\]

On the nonzero-vorticity set, writing

\[
\omega=\rho\xi,
\qquad |\xi|=1,
\]

we have pointwise

\[
\boxed{
|\nabla\omega|^2
=|\nabla\rho|^2
+\rho^2|\nabla\xi|^2.
}
\]

Hence, away from the zero-set issue in the directional representation,

\[
P_{\rm ang}
=\int\rho^2|\nabla\xi|^2dx.
\]

The difference definition `P_ang=P-P_mag` is retained as the globally robust one.

---

## 2. Scalar Sobolev uses only `P_mag`

Because

\[
\|\omega\|_6=\||\omega|\|_6=\|\rho\|_6,
\]

the scalar Sobolev inequality gives

\[
\boxed{
\|\omega\|_6
\le C_S\|\nabla\rho\|_2
=C_S P_{\rm mag}^{1/2}
=C_S(P-P_{\rm ang})^{1/2}.
}
\]

This is strictly sharper than replacing `P_mag` by the full `P` whenever `P_ang>0`.

---

## 3. Enstrophy-production source

Let

\[
E=\|\omega\|_2^2
\]

and

\[
Q=\int\omega\cdot S\omega\,dx.
\]

The strain is a zero-order singular-integral transform of vorticity, so

\[
\|S\|_3\le C_R\|\omega\|_3.
\]

Therefore

\[
|Q|
\le\|S\|_3\|\omega\|_3^2
\le C_R\|\omega\|_3^3.
\]

Interpolate

\[
\|\omega\|_3
\le
\|\omega\|_2^{1/2}
\|\omega\|_6^{1/2}.
\]

Using the magnitude-only Sobolev bound,

\[
\boxed{
|Q|
\le C_*
E^{3/4}
(P-P_{\rm ang})^{3/4}.
}
\]

This refines the generic estimate

\[
|Q|\lesssim E^{3/4}P^{3/4}.
\]

---

## 4. Dimensionless strict-gap factor

For `P>0`, define

\[
\boxed{
\eta_{\rm ang}
=\frac{P_{\rm ang}}{P}
\in[0,1].
}
\]

Then

\[
\boxed{
|Q|
\le
C_*E^{3/4}P^{3/4}
(1-\eta_{\rm ang})^{3/4}.
}
\]

Thus a positive angular fraction produces a strict multiplicative depletion relative to the generic Sobolev source.

Important: the exponent remains scale critical.  The gain is in the **dimensionless coefficient**, not a new power of the dangerous scale.

---

## 5. Connect to the thick projective-rough branch

On a thick intense ball, the projective Poincare lemma gives schematically

\[
P_{{\rm ang},B}
=\int_B|\omega|^2|\nabla\xi|^2
\ge
c a^6\frac{E_BJ_B}{r^2}.
\]

At the natural vorticity scale

\[
r\sim W^{-1/2},
\]

for a genuinely intense thick core,

\[
P_{{\rm ang},B}
\gtrsim
W^{3/2}J_B.
\]

Define the normalized local total palinstrophy

\[
\mathcal P_B
=r^3P_B.
\]

If a renormalized dangerous-window subsequence satisfies

\[
\mathcal P_B\le M_P
\]

and remains projectively rough,

\[
J_B\ge j_0>0,
\]

then the angular fraction cannot vanish:

\[
\boxed{
\eta_{{\rm ang},B}
\ge
c\frac{j_0}{M_P}
}
\]

up to the fixed intensity/thickness constants and localization bookkeeping.

Hence the rough + bounded-palinstrophy branch carries a **uniform strict source-depletion factor**.

---

## 6. Saturation incompatibility

The generic Sobolev estimate can be nearly saturated only if

\[
\eta_{\rm ang}\to0.
\]

But the thick projectively rough branch with bounded normalized palinstrophy forces

\[
\eta_{\rm ang}\ge\eta_0>0.
\]

Therefore these two saturation requirements are incompatible:

\[
\boxed{
\text{bounded normalized palinstrophy}
+\text{non-small projective roughness}
\Longrightarrow
\text{strict deficit from the generic Sobolev source}.
}
\]

This is the first explicit coefficient-level gap in the current simultaneous-saturation program.

It does **not** yet prove that viscosity dominates the nonlinear source; the Calderon--Zygmund/Sobolev constant and the remaining localized/far-field pieces still matter.

---

## 7. Localized version required for the proof route

The active proof route uses moving/adjoint localized windows.  On a cutoff window, applying scalar Sobolev to `chi rho` produces cutoff-error terms of the form

\[
r^{-2}\int_{B_{2r}}|\omega|^2.
\]

At the natural scale these are also critical and must remain typed as shell/localization channels.

Therefore the global inequality above is an exact structural guide, while the proof-producing next step is a localized buffered version:

\[
\boxed{
Q_{B_r}^{\rm near}
\lesssim
E_{B_{2r}}^{3/4}
\left(
P_{{\rm mag},B_{2r}}
+r^{-2}E_{B_{2r}}
\right)^{3/4}
+\text{remote strain term}.
}
\]

The remote strain term is already handled by the dyadic/projective and pressure-style localization machinery in separate notes; it must not be silently discarded.

---

## 8. New normalized rigidity target

On the naturally rescaled unit cylinder, a residual bounded-channel limit must now choose:

1. `J -> 0`, feeding the projective coherence/anisotropic branch; or
2. `J >= j0`, forcing a positive angular palinstrophy fraction and hence a strict Sobolev source deficit; or
3. normalized palinstrophy becomes unbounded, which is a typed concentration branch.

Schematically,

\[
\boxed{
\text{coherent}
\quad\text{or}\quad
\text{strict source deficit}
\quad\text{or}\quad
\text{palinstrophy concentration}.
}
\]

This trichotomy is more useful than comparing only critical exponents.

Status: **ACTIVE COEFFICIENT-GAP ROUTE / OPEN LOCAL SOURCE-DISSIPATION CLOSURE**.
