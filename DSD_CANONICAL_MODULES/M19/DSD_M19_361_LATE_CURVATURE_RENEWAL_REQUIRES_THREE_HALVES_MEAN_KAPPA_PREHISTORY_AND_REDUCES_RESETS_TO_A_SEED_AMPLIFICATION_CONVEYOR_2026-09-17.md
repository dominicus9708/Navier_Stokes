# DSD M19-361 — Late curvature renewal requires asymptotic three-halves mean kappa prehistory and reduces resets to a seed-amplification conveyor

Date: 2026-09-17  
Canonical ID: **M19-361**

Status: **ACTIVE RESET-PREHISTORY REDUCTION / POSITIVE-KAPPA AMPLIFICATION THRESHOLD / SEED-CONVEYOR FORM**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-360

For a material label that becomes curvature-active at \(\theta_j\), M19-360 gives

\[
|\phi_j(\theta_0)|
\le
C_0 e^{-3(\theta_j-\theta_0)/2},
\]

where

\[
C_0=\frac{M_1\phi_+}{z_*}.
\]

At the active time the fixed-flux genealogy gives

\[
|\phi_j(\theta_j)|\ge\phi_->0.
\]

## 2. Exact material-flux law

On CE-H the infinitesimal material vortex-tube flux satisfies

\[
\boxed{
D_B\log|\phi|=\kappa.
}
\]

Therefore

\[
\log\frac{|\phi_j(\theta_j)|}{|\phi_j(\theta_0)|}
=
\int_{\theta_0}^{\theta_j}\kappa_{\lambda_j}(s)\,ds.
\]

Using the lower bound at activation and the M19-360 base-flux upper bound yields

\[
\boxed{
\int_{\theta_0}^{\theta_j}\kappa_{\lambda_j}(s)\,ds
\ge
\frac32(\theta_j-\theta_0)-C_*,
}
\]

with

\[
C_*:=\log\frac{C_0}{\phi_-}
=
\log\frac{M_1\phi_+}{z_*\phi_-}.
\]

## 3. Mean-coefficient threshold

Let

\[
T_j:=\theta_j-\theta_0.
\]

Then

\[
\boxed{
\frac1{T_j}
\int_{\theta_0}^{\theta_j}\kappa_{\lambda_j}(s)\,ds
\ge
\frac32-\frac{C_*}{T_j}.
}
\]

Hence every sequence of increasingly late renewed curvature labels satisfies

\[
\boxed{
\liminf_{j\to\infty}
\frac1{T_j}
\int_{\theta_0}^{\theta_j}\kappa_{\lambda_j}(s)\,ds
\ge\frac32.
}
\]

In particular

\[
\boxed{
\int_{\theta_0}^{\theta_j}(\kappa_{\lambda_j})_+(s)\,ds
\ge
\frac32T_j-C_*.
}
\]

Thus late renewal cannot be supplied by a neutral prehistory. It requires extensive positive multiplier exposure.

## 4. Equivalent curvature-amplitude form

M5-621 also gives

\[
D_B\log Z_{curv}
=
\kappa-\frac32,
\qquad
Z_{curv}=\rho|\mathcal K|.
\]

Integrating,

\[
\log\frac{Z_{curv}(\theta_j)}{Z_{curv}(\theta_0)}
=
\int_{\theta_0}^{\theta_j}
\left(\kappa-\frac32\right)ds.
\]

Since

\[
Z_{curv}(\theta_j)\ge z_*,
\qquad
Z_{curv}(\theta_0)\le M_1,
\]

one recovers the same threshold:

\[
\int_{\theta_0}^{\theta_j}\kappa ds
\ge
\frac32T_j-\log\frac{M_1}{z_*}.
\]

The three-halves value is therefore intrinsic to maintenance of order-one curvature amplitude in backward similarity variables, not an artifact of the flux estimate.

## 5. Reset interpretation

M19-358 describes renewal as an upward reset of the label-local potential

\[
X=\log\frac{Z_{curv}}{|\phi|}.
\]

M19-360 shows that late resets can be sourced by labels with exponentially small base flux.

M19-361 shows what those labels must do before activation:

\[
\boxed{
\text{exponentially small seed flux}
\xrightarrow{\ \overline\kappa\gtrsim3/2\ }
\text{order-one fixed-flux curvature carrier}.
}
\]

Thus the surviving reset mechanism is a **positive-kappa seed-amplification conveyor**.

## 6. Relation to the whole-space sign identity

At each time exact CE-H gives

\[
\int\kappa|W|^2dx=-\|\nabla W\|_2^2\le0.
\]

Therefore the extensive positive \(\kappa\) exposure required on selected future curvature labels cannot represent a globally positive enstrophy-weighted coefficient mean.

It must coexist with compensating negative-\(\kappa\) weighted population, low-amplitude selection, or other measure segregation.

This is consistent with the M17/M19 mixed-sign conveyor analysis and does not by itself give a contradiction.

## 7. Why the threshold is not yet a closure theorem

The coefficient \(\kappa\) is bounded on the compact all-order hull, but no certified bound

\[
\kappa<\frac32
\]

exists.

Nor does the global negative enstrophy-weighted mean control the unweighted time average of \(\kappa\) along a sparse family of material labels.

Hence

\[
\overline\kappa_\lambda\ge\frac32-o(1)
\]

is a strong structural requirement, but not presently impossible.

## 8. Updated reset theorem gate

The M19-360 non-discounted-resource target can now be sharpened to

\[
\boxed{
\mathcal T_{amp}^{3/2}:
\text{rule out positive-density production of new material labels with long-time mean }\kappa\ge3/2-o(1),
}
\]

or prove that such amplification necessarily pays one of the already typed mixed-sign, palinstrophy, high-jet, transverse-geometry, genealogy, or representation exits.

This is more precise than another absolute-flux counting argument.

## 9. Audit verdict

**PASS — every sufficiently late curvature reset requires an extensive positive-kappa amplification prehistory with asymptotic mean at least three-halves.**

The curvature reset problem is therefore reduced from finite absolute-flux counting to a seed-amplification conveyor. Whether that conveyor can persist inside the exact CE-H compact hard core remains open.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
