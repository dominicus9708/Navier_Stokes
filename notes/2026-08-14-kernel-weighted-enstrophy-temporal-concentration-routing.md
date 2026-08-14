# Kernel weighted-enstrophy action: mesoscopic cost or terminal middle-strain escalation

Date: 2026-08-14

Status: **DERIVED ABSTRACT TIME-WEIGHT DICHOTOMY + ROUTING TO THE EXISTING GLOBAL ENSTROPHY / POSITIVE-MIDDLE-STRAIN BRANCH. KERNEL NON-GAUSSIANITY NO LONGER REQUIRES A SEPARATE TEMPORAL ESCAPE LABEL. GLOBAL REGULARITY NOT PROVED.**

## 1. Critical kernel-deformation action

The exact-kernel regression/Girsanov/Sobolev estimate gives

\[
\mathfrak D_K(\tau)
\le
C\nu^{-3/2}
\mathfrak Z_K(\tau),
\]

where

\[
\boxed{
\mathfrak Z_K(\tau)
:=
\int_0^\tau s^{-1/2}E_\omega(s)ds,
\qquad
E_\omega(s)=\|\Omega(s)\|_2^2.
}
\]

Thus a fixed kernel shape defect

\[
\mathfrak D_K(\tau)\ge d_0>0
\]

forces

\[
\boxed{
\mathfrak Z_K(\tau)
\ge c_{d_0,\nu}>0.
}
\]

The question is where in backward age this weighted action sits.

## 2. Mesoscopic-versus-terminal split

Fix

\[
0<\eta<1.
\]

Split

\[
\mathfrak Z_K
=
\int_0^{\eta\tau}s^{-1/2}E_\omega(s)ds
+
\int_{\eta\tau}^{\tau}s^{-1/2}E_\omega(s)ds.
\]

If the later/mesoscopic part carries at least half the action,

\[
\int_{\eta\tau}^{\tau}s^{-1/2}E_\omega ds
\ge\frac{c_0}{2},
\]

then, because `s^-1/2 <= (eta tau)^-1/2` on this interval,

\[
\boxed{
\int_{\eta\tau}^{\tau}E_\omega(s)ds
\ge
\frac{c_0}{2}\sqrt{\eta\tau}.
}
\]

Thus non-Gaussian kernel deformation occurring at a fixed positive fraction of the scale time pays an explicit ordinary enstrophy-time / kinetic-dissipation occupancy cost.

## 3. Terminal concentration alternative

Otherwise the terminal layer carries at least half the weighted action:

\[
\boxed{
\int_0^{\eta\tau}s^{-1/2}E_\omega(s)ds
\ge\frac{c_0}{2}.
}
\]

More generally, if for some terminal width `ell`

\[
\int_0^\ell s^{-1/2}E_\omega(s)ds
\ge\delta,
\]

then

\[
\int_0^\ell s^{-1/2}ds=2\sqrt\ell
\]

implies the sharp elementary lower bound

\[
\boxed{
\sup_{0<s<\ell}E_\omega(s)
\ge
\frac{\delta}{2\sqrt\ell}.
}
\]

Therefore if a fixed weighted action is pushed into widths

\[
\ell_j\to0,
\]

then

\[
\boxed{
\sup_{0<s<\ell_j}E_{\omega,j}(s)
\to\infty
}
\]

at least as fast as `ell_j^-1/2`.

Thus cheap kernel deformation is necessarily a global temporal-enstrophy concentration event.

## 4. Dyadic formulation

Let

\[
I_k=(2^{-k-1}\tau,2^{-k}\tau].
\]

On `I_k`,

\[
s^{-1/2}\asymp(2^{-k}\tau)^{-1/2}.
\]

Hence

\[
\mathfrak Z_K
\asymp
\sum_{k\ge0}
\frac{
\int_{I_k}E_\omega(s)ds
}{
\sqrt{2^{-k}\tau}
}.
\]

If the ordinary enstrophy mass on every fixed finite collection of outer dyadic blocks tends to zero, a fixed `Z_K` action must move to indices `k_j->infinity`. On those blocks the average enstrophy obeys

\[
\boxed{
\operatorname*{avg}_{I_{k_j}}E_\omega
\gtrsim
(2^{-k_j}\tau)^{-1/2}
}
\]

up to the fraction of action assigned to the selected block.

This makes the temporal-concentration mechanism explicit in scale-time language.

## 5. Route to the far-checkpoint enstrophy reset

The adaptive proof already uses a farther first-hitting checkpoint at which normalized global enstrophy is small relative to the later dangerous scale. In particular the recorded `q_far=W^(2/3)` checkpoint gives

\[
E_-\lesssim W^{-1/6}
\]

in terminal normalization.

If the kernel-deformation action is concentrated into a shrinking terminal layer and forces

\[
E_{\max}\gtrsim\ell^{-1/2},
\]

then the ratio

\[
E_{\max}/E_-
\]

necessarily diverges whenever the terminal width is driven to zero along the singular sequence.

Thus the terminal kernel-deformation lane is a fresh global enstrophy-escalation lane.

## 6. Exact routing to positive middle strain

The whole-space strain identity already gives, for an enstrophy rise `E0 -> E1`,

\[
\boxed{
\int\!\!\int\lambda_2^+|S|^2dxdt
\gtrsim
E_1-E_0.
}
\]

Therefore a fixed kernel shape defect has only two temporal realizations:

\[
\boxed{
\text{K-meso: ordinary enstrophy-time occupancy},
}
\]

or

\[
\boxed{
\text{K-terminal: global enstrophy escalation}
\Rightarrow
\text{positive-middle-strain action}.
}
\]

Kernel deformation is no longer a third independent physical source branch.

## 7. Claim boundary

The mesoscopic ordinary enstrophy-time lower bound may shrink after conversion back to physical variables as the first-hitting level grows; it is not by itself a contradiction on an infinite geometric sequence.

Likewise, routing the terminal alternative to `lambda_2^+` identifies the established scale-critical blow-up channel but does not yet prove that its required action is globally impossible.

The result is a branch reduction, not a regularity theorem.

Status: **KERNEL NON-GAUSSIANITY ROUTED TO ORDINARY DISSIPATION OCCUPANCY OR POSITIVE-MIDDLE-STRAIN ESCALATION / NO INDEPENDENT TERMINAL KERNEL-DEFORMATION ESCAPE REMAINS / GLOBAL REGULARITY NOT PROVED.**
