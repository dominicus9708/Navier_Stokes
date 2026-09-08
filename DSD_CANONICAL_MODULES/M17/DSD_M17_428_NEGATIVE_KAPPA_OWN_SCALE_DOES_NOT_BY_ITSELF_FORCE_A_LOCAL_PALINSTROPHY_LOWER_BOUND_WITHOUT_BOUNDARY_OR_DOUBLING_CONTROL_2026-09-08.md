# DSD M17-428 — Negative-kappa own scale does not by itself force a local palinstrophy lower bound without boundary or doubling control

Date: 2026-09-08  
Canonical ID: **M17-428**

Status: **ACTIVE PALINSTROPHY-SHORTCUT AUDIT / LOCAL BOUNDARY FIREWALL / M17-383 RETURN**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Motivation

After M17-425--427, the material-label concentration route remains tied to the cubic `R_m^{-3}` firewall.

Because the certified ancestral palinstrophy ledger has the more favorable weight

\[
R_m^{-1},
\]

it is natural to ask whether a negative-coefficient exact CE-H own-scale packet automatically forces local palinstrophy.

The tempting heuristic is

\[
\Delta\Omega=\kappa\Omega,
\qquad
\kappa\sim-r^{-2}<0,
\]

so perhaps

\[
\int_{B_r}|\nabla\Omega|^2
\gtrsim
r^{-2}\int_{B_r}|\Omega|^2.
\]

This lower bound is **not automatic on a local ball**.

## 2. Cutoff identity

Let `eta` be a smooth cutoff supported in `B_{2r}` and equal to one on `B_r`.

Multiply

\[
\Delta\Omega=\kappa\Omega
\]

by `eta^2 Omega` and integrate. Componentwise integration by parts gives

\[
-\int\eta^2|\nabla\Omega|^2
-2\int\eta\,\Omega\cdot(\nabla\eta\cdot\nabla\Omega)
=
\int\kappa\eta^2|\Omega|^2.
\]

Hence

\[
\boxed{
\int\eta^2|\nabla\Omega|^2
=
\int(-\kappa)\eta^2|\Omega|^2
-2\int\eta\,\Omega\cdot(\nabla\eta\cdot\nabla\Omega).
}
\]

On a negative own-scale coefficient cell,

\[
-\kappa\asymp r^{-2}.
\]

The first term is the desired positive scale term.

## 3. Boundary-annulus term is of the same scale

Since

\[
|\nabla\eta|\lesssim r^{-1},
\]

the cutoff term satisfies

\[
\left|
2\int\eta\Omega\cdot(\nabla\eta\cdot\nabla\Omega)
\right|
\lesssim
r^{-1}
\|\Omega\|_{L^2(A_r)}
\|\nabla\Omega\|_{L^2(A_r)},
\]

where

\[
A_r=B_{2r}\setminus B_r.
\]

Young's inequality gives only

\[
\lesssim
\varepsilon\|\nabla\Omega\|_{L^2(A_r)}^2
+C_\varepsilon r^{-2}\|\Omega\|_{L^2(A_r)}^2.
\]

These are exactly own-scale boundary terms. Without control of annular mass/gradient relative to the inner packet, they may cancel the desired lower bound.

## 4. What Caccioppoli actually gives

The standard cutoff argument naturally yields an **upper** estimate of Caccioppoli type,

\[
\int_{B_r}|\nabla\Omega|^2
\lesssim
r^{-2}\int_{B_{2r}}|\Omega|^2
\]

under `|kappa|lesssim r^{-2}`.

That estimate is useful for compactness and was already part of the M17-382/387 architecture.

It does not reverse to a lower bound without additional information.

## 5. Required extra information

A lower bound

\[
\int_{B_r}|\nabla\Omega|^2
\gtrsim
r^{-2}\int_{B_r}|\Omega|^2
\]

can become available if one additionally controls, for example,

- boundary/annulus mass leakage;
- local doubling/frequency;
- a suitable Dirichlet/Neumann or flux boundary condition;
- a global sign-definite coefficient identity with vanishing boundary at infinity;
- a recurrent loop covariance/gradient payer such as M17-361.

None is supplied solely by `kappa ~ -r^{-2}` on a local own-scale cell.

## 6. Return to M17-383

M17-383 already proved that coefficient-scale spatial thickness does not imply solution-mass retention: exact constant-coefficient Helmholtz modes may have arbitrarily high local vanishing order.

The present audit is the gradient version of the same obstruction.

Without a local frequency/doubling or boundary input, coefficient scale alone cannot force a uniform local palinstrophy payment.

Therefore

\[
\boxed{
H_{negative\ kappa\ own\text{-}scale}
\not\Rightarrow
H_{uniform\ local\ palinstrophy\ payer}
}
\]

by the local elliptic equation alone.

## 7. Consequence for the cubic material-core branch

The M17-426--427 zero-volume material-core survivor cannot be upgraded from the raw-`H2` cubic ancestry weight to the palinstrophy `R_m^{-1}` weight merely by noting that the active coefficient is negative.

A genuine palinstrophy bridge must independently control frequency/boundary leakage or use the recurrent loop gradient mechanism.

Thus the hoped-for shortcut

\[
R_m^{-3}\to R_m^{-1}
\]

is not certified.

## 8. Global identity is not a local substitute

If exact CE-H held globally with sufficient decay, integration over all of `R^3` would give

\[
\int|\nabla\Omega|^2
=-\int\kappa|\Omega|^2.
\]

But the right side is signed when `kappa` changes sign, and a local negative region may be offset by positive-coefficient regions.

Therefore this global identity does not supply the desired local negative-cell lower bound either without further sign/support structure.

## 9. Revised payer frontier

The material-core branch remains

\[
\boxed{
G_{zero\text{-}volume\ material\ core}
\to
G_{cubic\ raw\text{-}H2/volume\ firewall}
\lor
G_{frequency/boundary\ control\ needed}
\lor
G_{interface/genealogy\ exit}.
}
\]

## 10. Next target

The more promising use of the `R_m^{-1}` ledger is not a local negative-`kappa` elliptic shortcut, but a **genuine recurrent/turnover gradient payer** with controlled material-label occupancy.

The next audit should therefore compare M17-361's loop palinstrophy payer with the M17-420 empirical occupation mechanism after reach/tube decompactification, and determine exactly which geometric hypothesis is lost before the `R_m^{-1}` payer can be multiplied by record-linear spatial occupancy.

This is M17-429.

## 11. DSD audit

The DSD role is to prevent a coefficient sign from being mistaken for an integral coercivity theorem. The derivation is ordinary cutoff integration by parts.

## 12. Audit verdict

**PASS-NO-GO.**

Negative own-scale `kappa` gives the correct positive bulk term, but local boundary-annulus terms prevent an unconditional palinstrophy lower bound. The branch returns to the M17-383 frequency/boundary debt rather than bypassing it.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
