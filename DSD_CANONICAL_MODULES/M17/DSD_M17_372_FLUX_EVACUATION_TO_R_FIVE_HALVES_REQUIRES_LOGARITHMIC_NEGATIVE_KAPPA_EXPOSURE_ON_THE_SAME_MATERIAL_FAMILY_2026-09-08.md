# DSD M17-372 — Flux evacuation to `O(r^{5/2})` requires logarithmic negative-`kappa` exposure on the same material family

Date: 2026-09-08  
Canonical ID: **M17-372**

Status: **ACTIVE SAME-GENEALOGY FLUX-EXPOSURE LEDGER / FIXED SIMILARITY REPRESENTATION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Scope

This module works inside **one fixed similarity representation** and one material flux-family genealogy.

It does not compare the same numerical `kappa` threshold across record generations. The M17-338 physical/similarity dictionary remains mandatory for any such cross-generation use.

Let `F(theta)` be one retained positively oriented material-flux family whose infinitesimal flux weights obey the M5-684 law

\[
\boxed{
\frac d{d\theta}d\Phi_\lambda
=\kappa_\lambda d\Phi_\lambda.
}
\]

Assume the family identity is preserved on the interval under consideration. If labels enter or leave through cutoff, nodal, rank, or interface changes, record the corresponding genealogy/interface exit instead of applying the present formula silently.

## 2. Total family flux law

Define

\[
\Phi_F(\theta)
:=
\int_{F(\theta)}d\Phi.
\]

For a fixed material family,

\[
\frac d{d\theta}\Phi_F
=
\int_F\kappa\,d\Phi.
\]

Hence

\[
\boxed{
\frac d{d\theta}\log\Phi_F
=
\bar\kappa_{\Phi,F},
}
\]

where

\[
\boxed{
\bar\kappa_{\Phi,F}
:=
\frac{1}{\Phi_F}
\int_F\kappa\,d\Phi.
}
\]

This is the family-level analogue of the single-label flux law.

## 3. Input from M17-371

Suppose at an earlier reference time `theta_0` the same family carries

\[
\boxed{
\Phi_F(\theta_0)\ge\Phi_0>0.
}
\]

At a later strict-subscale event of intrinsic size `r`, M17-371 gives on the compact coefficient-mass/local-H2 branch

\[
\boxed{
\Phi_F(\theta_r)
\le C_*r^{5/2}.
}
\]

Integrating the total flux law,

\[
\log\frac{\Phi_F(\theta_r)}{\Phi_F(\theta_0)}
=
\int_{\theta_0}^{\theta_r}
\bar\kappa_{\Phi,F}(\theta)d\theta.
\]

Therefore

\[
\boxed{
\int_{\theta_0}^{\theta_r}
\bar\kappa_{\Phi,F}d\theta
\le
-\frac52\log\frac1r
+C_0,
}
\]

with

\[
C_0=\log(C_*/\Phi_0).
\]

## 4. Negative exposure lower bound

Write

\[
\bar\kappa_{\Phi,F}
=(\bar\kappa_{\Phi,F})_+
-(\bar\kappa_{\Phi,F})_-.
\]

The preceding inequality implies

\[
\boxed{
\int_{\theta_0}^{\theta_r}
(\bar\kappa_{\Phi,F})_-d\theta
\ge
\frac52\log\frac1r-C_0.
}
\]

By convexity of the negative-part function,

\[
(\bar\kappa_{\Phi,F})_-
\le
\overline{\kappa_-}_{\Phi,F},
\]

where

\[
\overline{\kappa_-}_{\Phi,F}
:=
\frac1{\Phi_F}
\int_F\kappa_-d\Phi.
\]

Hence the stronger usable statement is

\[
\boxed{
\int_{\theta_0}^{\theta_r}
\overline{\kappa_-}_{\Phi,F}d\theta
\ge
\frac52\log\frac1r-C_0.
}
\]

Thus strict-subscale flux evacuation requires a logarithmically divergent negative coefficient exposure along the same retained material family.

## 5. If the same family later recovers its flux

Suppose at a later time `theta_1>theta_r`

\[
\Phi_F(\theta_1)\ge\Phi_0.
\]

Then

\[
\int_{\theta_r}^{\theta_1}
\bar\kappa_{\Phi,F}d\theta
\ge
\frac52\log\frac1r-C_0.
\]

Therefore

\[
\boxed{
\int_{\theta_r}^{\theta_1}
\overline{\kappa_+}_{\Phi,F}d\theta
\ge
\frac52\log\frac1r-C_0.
}
\]

A lineage that repeatedly descends to scale `r` and then returns to comparable flux must therefore carry both large negative and large positive coefficient exposure.

This creates a genuine turnover/residence problem; the loss and recovery cannot both be hidden in a signed average.

## 6. Residence versus repeated turnover

The logarithmic exposure does not by itself determine how many sign crossings occur.

For example, the negative exposure may be supplied by

1. a long residence in a negative critical-coefficient phase;
2. many shorter negative episodes separated by returns;
3. a mixture of both.

Without an upper bound on exposure per episode, one may not conclude

\[
N_{cross}\gtrsim\log(1/r).
\]

Thus the exact safe split is

\[
\boxed{
H_{flux\ evacuation/recovery}
\Longrightarrow
H_{long\ signed\ coefficient\ residence}
\lor
H_{repeated\ coefficient\ turnover}
\lor
G_{family/interface/genealogy\ change}.
}
\]

## 7. Relation to the existing zero-current branch

M17-314/323 already force a positive-density directed zero-`kappa` current on the retained high-amplitude material branch.

The present result is different: it shows that a strict-subscale **flux-poor nodal bubble**, if it belongs to the same material family that previously carried order-one flux, must accumulate a logarithmically large signed exposure before reaching that bubble.

Hence the high-amplitude zero-current branch and the nodal flux-evacuation branch are not unrelated populations once same-family genealogy is established.

The remaining bridge is quantitative control of exposure per residence/turnover episode.

## 8. Audit verdict

**PASS as a same-genealogy logarithmic exposure theorem.**

The key result is

\[
\boxed{
\int
\overline{\kappa_-}_{\Phi,F}d\theta
\gtrsim
\frac52\log\frac1r
}
\]

for evacuation from fixed positive flux to the M17-371 `r^{5/2}` scale.

No crossing-count lower bound is claimed without an additional per-episode exposure bound.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]