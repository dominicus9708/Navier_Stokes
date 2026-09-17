# DSD M19-360 — Curvature renewal has exponentially discounted base-flux cost, so finite transverse flux alone cannot close the reset branch

Date: 2026-09-17  
Canonical ID: **M19-360**

Status: **ACTIVE RESET-RESOURCE AUDIT / M19-359 SCOPE CORRECTION / EXPONENTIAL BASE-FLUX DISCOUNT FIREWALL**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Correction target

M19-359 correctly proves

\[
\text{positive curvature frequency}
\Longrightarrow
\text{positive renewal frequency}
\Longrightarrow
\text{positive flux/projective discharge frequency}.
\]

It then names an absolute-flux resource as the next target.

The repository, however, already contains two facts that must be combined before using that target:

1. M5-647 constructs a finite total base-slice transverse-flux resource on a fixed compact reservoir;
2. M5-621 gives the exact same-label curvature-to-flux ratio law

\[
\boxed{
D_B X=-\frac32,
\qquad
X:=\log\frac{Z_{curv}}{|\phi|},
\qquad
Z_{curv}:=\rho|\mathcal K|.
}
\]

The second fact shows that a future curvature-active packet need not consume order-one flux on the fixed base slice.

## 2. Active packet thresholds

On the curvature-active fixed-flux genealogy retain

\[
Z_{curv}(\theta_j)\ge z_*>0,
\]

and

\[
0<\phi_-\le|\phi(\theta_j)|\le\phi_+<\infty.
\]

Hence at every active time

\[
\boxed{
R(\theta_j)
:=
\frac{Z_{curv}(\theta_j)}{|\phi(\theta_j)|}
\ge
r_*:=\frac{z_*}{\phi_+}>0.
}
\]

The compact CE-H hull also gives

\[
\boxed{Z_{curv}(\theta)\le M_1.}
\]

## 3. Pullback of the strict ratio

Fix one earlier reference time \(\theta_0<\theta_j\) on the same material label.

M5-621 integrates exactly to

\[
R(\theta_j)
=
R(\theta_0)
\exp\left[-\frac32(\theta_j-\theta_0)\right].
\]

Therefore

\[
\boxed{
R(\theta_0)
\ge
r_*
\exp\left[\frac32(\theta_j-\theta_0)\right].
}
\]

Since

\[
R(\theta_0)=\frac{Z_{curv}(\theta_0)}{|\phi(\theta_0)|}
\]

and \(Z_{curv}(\theta_0)\le M_1\), one obtains the base-flux upper bound

\[
\boxed{
|\phi_j(\theta_0)|
\le
\frac{M_1}{r_*}
\exp\left[-\frac32(\theta_j-\theta_0)\right].
}
\]

Equivalently,

\[
\boxed{
|\phi_j(\theta_0)|
\le
\frac{M_1\phi_+}{z_*}
 e^{-3(\theta_j-\theta_0)/2}.
}
\]

This is the main M19-360 estimate.

## 4. Positive renewal density is compatible with finite base flux

Suppose a separated curvature-active subsequence satisfies

\[
\theta_j-\theta_0\ge j\tau
\]

for some fixed \(\tau>0\), as is available after thinning a positive-density event sequence.

Then

\[
\sum_j|\phi_j(\theta_0)|
\le
\frac{M_1}{r_*}
\sum_j e^{-3j\tau/2}
<\infty.
\]

Thus even an infinite positive-density sequence of future order-one fixed-flux curvature packets can, in principle, pull back to a summable amount of base transverse flux.

Therefore

\[
\boxed{
\text{finite base absolute-flux resource}
\not\Rightarrow
\text{curvature-renewal contradiction}.
}
\]

## 5. Why this does not contradict M5-643--648

M5-643's non-discounted-flux argument applies to the strongly-negative relabeling lane, where

\[
\kappa<0
\]

is preserved and material flux is forward nonincreasing. There one has

\[
|\Phi(\theta_0)|\ge|\Phi(\theta_j)|\ge\phi_*.
\]

M5-647 then constructs a finite base transverse-flux resource, and M5-648 converts the negative-\(\kappa\) packet events into irreversible telescoping flux loss.

The curvature lane is different. No sign condition on \(\kappa\) is supplied by curvature activity alone. The exact ratio law permits the packet flux to have been exponentially smaller in the past and later to enter the fixed-flux window.

Hence the implication

\[
|\phi(\theta_j)|\ge\phi_*
\Longrightarrow
|\phi(\theta_0)|\gtrsim1
\]

is invalid on the generic curvature-renewal branch.

## 6. Correction to the M19-359 resource target

M19-359 Section 6 should be read conditionally:

\[
\boxed{
\mathcal T_{ren}^{abs-flux}
\text{ closes only if renewal also carries a non-discounted past-flux or irreversible-loss mechanism.}
}
\]

The finite transversal/current norm itself is not the missing object; M5-647 already provides it on the fixed analytic base slice.

The missing object is a lower bound of the form

\[
\boxed{
\text{reset event}
\Longrightarrow
\text{fixed nonrecyclable charge against a finite base resource},
}
\]

with no exponential generation discount.

## 7. Updated curvature-renewal normal form

The audited branch is now

\[
\boxed{
\begin{aligned}
\langle a^{curv}\rangle>0
&\Longrightarrow
\langle R_{ren}\rangle>0\\
&\Longrightarrow
\langle X_{visc\ flux}+X_{proj}\rangle>0\\
&\Longrightarrow
G_{projective/representation}
\lor
G_{recurrent\ flux\ turnover}^{discounted}.
\end{aligned}
}
\]

On the strict no-projective CE-H lane the surviving object is a recurrent viscous-flux turnover whose fixed-base flux cost can be exponentially discounted.

## 8. New theorem gate

Define

\[
\boxed{
\mathcal T_{ren}^{non\text{-}discounted}:
\text{construct a reset cost whose pullback to one finite resource has a generation-independent lower bound.}
}
\]

Possible sources must use information not canceled by the strict ratio law, for example a coupled curvature/magnitude/current quantity, a sheet-transfer invariant, or another genuinely irreversible material-lineage resource.

Merely reusing base flux, material volume, or the label-local strict ratio cannot work by themselves.

## 9. Audit verdict

**PASS-NO-GO / CORRECTION.**

M5-647 already supplies a finite transverse-flux resource, but M5-621 implies that generic curvature renewals may pull back to exponentially small base flux. Therefore finite absolute flux alone does not close the reset branch. M19-359's current resource target must be strengthened from existence of a finite flux norm to a non-discounted irreversible reset charge.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
