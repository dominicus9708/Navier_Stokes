# DSD M5-189 — First-Order Div–Curl Carleman Repairs the Elliptic Derivative Loss

Date: 2026-08-28

Status: **P1_B COUPLED CARLEMAN REPAIR / THE SECOND-ORDER IDENTITY `-Delta Z = curl eta` INTRODUCES AN ARTIFICIAL DERIVATIVE LOSS BECAUSE ITS CARLEMAN RHS CONTAINS `nabla eta`; THE ACTUAL RECONSTRUCTION IS THE FIRST-ORDER HODGE SYSTEM `curl Z=eta`, `div Z=0`; A SHIFTED FIRST-ORDER DIV–CURL/DIRAC CARLEMAN MATCHES THE CRITICAL COUPLING `rho^-3 Z`, `rho^-2 nabla Z`, `rho^-2 eta` WITHOUT DIFFERENTIATING ETA / THIS REPLACES THE M5-188 SECOND-ORDER ELLIPTIC TARGET / GLOBAL REGULARITY UNPROVED.**

---

## 1. Why the second-order reconstruction is inefficient

M5-183/M5-188 used

\[
-\Delta Z=\nabla\times\eta.
\]

A second-order elliptic Carleman estimate then produces a source norm containing

\[
|\nabla\eta|.
\]

This is one derivative stronger than the relative-vorticity equation naturally exports and risks forcing an unnecessary derivative hierarchy.

This loss is not intrinsic.

---

## 2. Exact first-order Hodge system

Because

\[
\eta=\nabla\times Z,
\qquad
\nabla\cdot Z=0,
\]

the actual reconstruction is

\[
\boxed{
\mathcal D Z
:=
(\nabla\times Z,\nabla\cdot Z)
=
(\eta,0).
}
\]

`mathcal D` is a first-order elliptic Hodge/Dirac-type operator.

Thus the correct companion to the parabolic Carleman estimate is a first-order Carleman inequality for `mathcal D`, not a Laplacian estimate.

---

## 3. Critical scaling target

For a power-type singular Carleman weight at exponent `tau`, the first-order elliptic scaling is schematically

\[
\boxed{
\tau^2
\int r^{-2\tau-2}|Z|^2
+
\int r^{-2\tau}|\nabla Z|^2
\lesssim
\int r^{-2\tau}|\mathcal D Z|^2.
}
\]

Since

\[
\mathcal D Z=(\eta,0),
\]
this becomes

\[
\tau^2
\int r^{-2\tau-2}|Z|^2
+
\int r^{-2\tau}|\nabla Z|^2
\lesssim
\int r^{-2\tau}|\eta|^2.
\]

The exact allowed sequence of `tau` must avoid the discrete Hodge/spherical spectrum, just as the scalar Hardy–Carleman parameter avoids spherical resonances.

This spectral-gap issue is the next technical sublemma.

---

## 4. Shift by two powers gives the needed W1 coupling

Apply the same first-order estimate with exponent `tau+2`.

Then, schematically,

\[
\boxed{
\tau^2
\int r^{-2\tau-6}|Z|^2
+
\int r^{-2\tau-4}|\nabla Z|^2
\lesssim
\int r^{-2\tau-4}|\eta|^2.
}
\]

This matches exactly the squared critical coupling terms in the vorticity equation:

\[
|\nabla\omega^W|^2|Z|^2
\lesssim
r^{-6}|Z|^2,
\]

\[
|\omega^W|^2|\nabla Z|^2
\lesssim
r^{-4}|\nabla Z|^2,
\]

while the vorticity matrix-potential term has

\[
|\nabla u^V|^2|\eta|^2
\lesssim
r^{-4}|\eta|^2.
\]

Thus all three are now on the same weighted scale.

---

## 5. Consequence

If the first-order div–curl Carleman is proved with a constant independent of large `tau` along a nonresonant sequence, then

\[
\boxed{
\int W_\tau
\left(
 r^{-6}|Z|^2
+r^{-4}|\nabla Z|^2
\right)
\lesssim
\tau^{-c}
\int W_\tau r^{-4}|\eta|^2
}
\]

for some positive Carleman gain `tau^-c` after retaining the exact parameter powers.

That gain would permit the two velocity-reconstruction terms in the vorticity equation to be absorbed together with the inverse-square stretching term.

No derivative of `eta` is needed.

---

## 6. Relation to the refined parabolic Hardy estimate

The Banerjee–Garofalo–Manna proof contains positive conjugated radial/angular derivative terms before they are discarded in the final theorem statement.

Therefore the desired coupled architecture is now

\[
\boxed{
\text{refined parabolic Hardy Carleman for }\eta
+
\text{first-order div–curl Carleman for }Z.
}
\]

This is better aligned than

\[
\text{parabolic }\eta
+
\text{second-order elliptic }Z,
\]

which unnecessarily differentiated `eta`.

---

## 7. DSD audit

### Formation — GREEN

`curl Z=eta` and `div Z=0` are exact identities of the same-tail difference.

### Axis — GREEN

Parabolic vorticity evolution and elliptic velocity reconstruction remain separate but matched at the same differential order.

### Static aggregation — GREEN

No derivative of `eta` is manufactured merely by rewriting the reconstruction through `-Delta`.

### Dynamics — YELLOW

The first-order Hodge Carleman spectral gap and exact parameter gain still have to be proved.

### Cross-audit — GREEN

This explicitly supersedes the M5-188 second-order shifted elliptic target; M5-188's drift cancellation remains valid.

---

## 8. Next calculation

Prove the first-order div–curl Carleman on `R^3\{0}` by spherical Hodge decomposition/conjugation, determine its resonance set, and retain the exact `tau` gain.

If the gain is at least one positive power of `tau`, combine it with the refined parabolic Hardy estimate to attempt absorption of all relative-vorticity lower-order channels.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
