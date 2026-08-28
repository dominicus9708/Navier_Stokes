# DSD M5-190 — Hodge Resonance Kills the First-Order Large-Parameter Gain

Date: 2026-08-28

Status: **CORRECTION TO M5-189 / THE FIRST-ORDER DIV–CURL OPERATOR HAS NONTRIVIAL HOMOGENEOUS CURL-FREE/DIVERGENCE-FREE MODES AT AN UNBOUNDED DISCRETE SET OF RADIAL EXPONENTS; CONSEQUENTLY A CARLEMAN EXPONENT `tau` CAN BE KEPT ONLY A FIXED DISTANCE FROM THE HODGE SPECTRUM, SO A FIRST-ORDER ESTIMATE HAS AT MOST O(1) SPECTRAL-GAP COERCIVITY AND CANNOT EXPORT THE `tau` OR `tau^2` GAIN NEEDED TO ABSORB AN ARBITRARILY LARGE CRITICAL COUPLING / THE M5-189 LARGE-PARAMETER TARGET IS RED; SECOND-ORDER FACTORIZATION MUST BE RESTORED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Exact homogeneous kernel of div–curl

Let `Y_ell` be a spherical harmonic of degree `ell`.

The scalar harmonic functions

\[
h_\ell^+(x)=r^\ell Y_\ell(\theta),
\qquad
h_\ell^-(x)=r^{-\ell-1}Y_\ell(\theta)
\]

satisfy

\[
\Delta h_\ell^\pm=0
\qquad (r>0).
\]

Therefore

\[
Z_\ell^\pm:=\nabla h_\ell^\pm
\]

satisfy

\[
\boxed{
\nabla\times Z_\ell^\pm=0,
\qquad
\nabla\cdot Z_\ell^\pm=0.
}
\]

Their homogeneities are

\[
Z_\ell^+\sim r^{\ell-1},
\qquad
Z_\ell^-\sim r^{-\ell-2}.
\]

Thus the first-order Hodge operator

\[
\mathcal D=(\operatorname{curl},\operatorname{div})
\]

has an unbounded discrete radial resonance set containing

\[
\boxed{
\{\ell-1:\ell\ge1\}
\cup
\{-\ell-2:\ell\ge0\}.
}
\]

---

## 2. Consequence for a power Carleman weight

A power weight `r^-tau` shifts the radial logarithmic derivative by `tau`.

For a first-order operator, after spherical decomposition the normal factors are of schematic form

\[
\partial_{\log r}+\lambda_j-\tau,
\]

where `lambda_j` ranges over the Hodge spherical spectrum.

Since the spectrum is unbounded with O(1) spacing, one can choose a nonresonant sequence `tau` such that

\[
\operatorname{dist}(\tau,\sigma_{Hodge})\ge c_0>0,
\]

but this distance cannot grow like `tau`.

Therefore the best uniform first-order spectral coercivity is only

\[
\boxed{
\|r^{-\tau-1}Z\|
\lesssim
\|r^{-\tau}\mathcal DZ\|
}
\]

up to fixed constants and the appropriate nonresonant sequence.

It does **not** have the form

\[
\tau\|r^{-\tau-1}Z\|
\lesssim
\|r^{-\tau}\mathcal DZ\|.
\]

---

## 3. Why the derivative estimate also cannot have a large gain

Near a resonance with angular degree `ell~tau`, a homogeneous Hodge mode has

\[
|\nabla Z|\sim \tau r^{-1}|Z|
\]

while

\[
|\mathcal DZ|
\sim
\operatorname{dist}(\tau,\sigma_{Hodge})r^{-1}|Z|
=O(r^{-1}|Z|).
\]

Hence no uniform estimate of the form

\[
\|r^{-\tau}\nabla Z\|
\lesssim
\|r^{-\tau}\mathcal DZ\|
\]

can hold with a `tau`-independent constant across the large-parameter sequence.

This is an explicit resonance obstruction, not a technical gap.

---

## 4. Why second order is different

For the scalar Laplacian, spherical factorization contains two radial factors.  For a mode `k`, the coefficient is schematically

\[
(\beta-k)(\beta+k+n-2).
\]

Choosing `beta` a fixed distance from the integer spectrum keeps

\[
|\beta-k|\ge c_0,
\]

while the second factor is of size

\[
\beta+k+n-2\gtrsim \tau.
\]

Thus the **second-order product retains one large factor `~tau`** even at the nearest resonance.

This is exactly the mechanism behind the scalar Hardy–Carleman critical coercivity.

Therefore the large Carleman parameter gain needed for arbitrary critical coupling is intrinsically second-order.

---

## 5. Correction to M5-189

The M5-189 target

\[
\tau^2\int r^{-2\tau-2}|Z|^2
+
\int r^{-2\tau}|\nabla Z|^2
\lesssim
\int r^{-2\tau}|\mathcal DZ|^2
\]

with a large-`tau` gain is **RED**.

The exact identities

\[
\operatorname{curl}Z=\eta,
\qquad
\operatorname{div}Z=0
\]

remain useful structurally, but they cannot by themselves supply the coercive Carleman parameter needed to absorb a general large Type-I coupling.

---

## 6. Restored coupled route

The correct route returns to a second-order elliptic factor, but must avoid the derivative-loss problem by exploiting the derivative coercivity already present in the refined parabolic Hardy proof.

The required architecture is now

\[
\boxed{
\text{gradient-retaining parabolic Hardy Carleman for }\eta
+
\text{shifted second-order elliptic Carleman for }Z.
}
\]

The Banerjee–Garofalo–Manna intermediate estimate contains positive conjugated radial and angular derivative terms before these are discarded in the published final theorem.

Those derivative terms are the resource needed to pay for

\[
\Delta Z=-\nabla\times\eta.
\]

---

## 7. DSD audit

### Formation — GREEN

The obstruction is witnessed by exact harmonic gradients.

### Axis — GREEN

First-order Hodge and second-order Laplacian coercivity are no longer conflated.

### Static aggregation — GREEN

A fixed spectral gap is not multiplied into a fictitious large-parameter gain.

### Dynamics — GREEN correction

M5-189's proposed large-parameter first-order closure is pruned.

### Cross-audit — GREEN

This is the same anti-circular rule used throughout W1: a formal differential-order match cannot replace the actual spectral coercivity needed for absorption.

---

## 8. Next calculation

Extract a gradient-retaining version of the refined parabolic Hardy Carleman estimate from its pre-discarded positive terms, then pair it with a shifted second-order elliptic Carleman for

\[
-\Delta Z=\nabla\times\eta.
\]

The key question is whether the exact parameter powers close the one-derivative coupling without reintroducing a derivative hierarchy.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
