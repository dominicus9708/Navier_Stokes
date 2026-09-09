# DSD M17-451 — Uniform record enstrophy forces fixed-amplitude positive-flux arclength sparsity on parent-length loops

Date: 2026-09-09  
Canonical ID: **M17-451**

Status: **ACTIVE FLUX-PARTICIPATION SPARSITY THEOREM / M17-450 REFINEMENT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input

Use the retained positive-flux tube from M17-450.

On a fixed normalized record-time window,

\[
\|\Omega_R\|_2^2\le E_I,
\]

and the coherent parent-length loop satisfies

\[
\ell_R\ge c_\ell R,
\qquad
\Phi_R\ge\Phi_*>0.
\]

At cross-section `A_z`, write

\[
\rho_R=|\Omega_R|,
\qquad
Q_R(z)=\int_{A_z}\rho_R^2dA,
\qquad
\mathfrak a_\Phi(z)=\frac{Q_R(z)}{\Phi_R}.
\]

M17-450 gives

\[
\int_{\Gamma_R}Q_R(z)dz
\lesssim E_I.
\]

## 2. Fixed normalized amplitude threshold

Fix any `a>0` independent of `R`.

Define the fraction of positive vortex flux carried by normalized amplitudes at least `a`:

\[
\boxed{
\eta_a(z)
:=
\frac1{\Phi_R}
\int_{A_z\cap\{\rho_R\ge a\}}
\rho_R\,dA.
}
\]

Then

\[
0\le\eta_a(z)\le1.
\]

## 3. Pointwise participation bound

On the set `rho_R >= a`,

\[
\rho_R^2\ge a\rho_R.
\]

Therefore

\[
Q_R(z)
\ge
\int_{\rho_R\ge a}\rho_R^2dA
\ge
 a\int_{\rho_R\ge a}\rho_RdA.
\]

Hence

\[
\boxed{
\mathfrak a_\Phi(z)
=\frac{Q_R(z)}{\Phi_R}
\ge
 a\eta_a(z).
}
\]

This is the sectionwise M17-440 high-amplitude participation inequality.

## 4. Arclength sparsity

Integrate along the loop:

\[
a\Phi_R
\int_{\Gamma_R}\eta_a(z)dz
\le
\int_{\Gamma_R}Q_R(z)dz
\lesssim E_I.
\]

Using `Phi_R >= Phi_*`,

\[
\boxed{
\int_{\Gamma_R}\eta_a(z)dz
\le
\frac{C E_I}{a\Phi_*}.
}
\]

The right side is independent of `R`.

Since `ell_R >= c_l R`, the arclength average satisfies

\[
\boxed{
\frac1{\ell_R}
\int_{\Gamma_R}\eta_a(z)dz
\lesssim
\frac{C}{a\Phi_*R}.
}
\]

Thus every fixed normalized amplitude threshold carries only `O(R^{-1})` average flux fraction along a parent-length loop.

## 5. Good-section version

Fix also `eta_*>0` and define

\[
G_{a,\eta_*}
:=
\{z\in\Gamma_R:\eta_a(z)\ge\eta_*\}.
\]

Then

\[
\eta_*|G_{a,\eta_*}|
\le
\int_{\Gamma_R}\eta_a(z)dz.
\]

Therefore

\[
\boxed{
|G_{a,\eta_*}|
\lesssim
\frac{E_I}{a\eta_*\Phi_*}.
}
\]

So the total normalized arclength on which a fixed positive fraction of flux is carried at fixed normalized amplitude is uniformly `O(1)`, even though the whole loop has length `O(R)`.

## 6. Consequence for own-scale spatial multiplicity

A fixed-amplitude good arc of normalized own-scale length `O(1)` contains only `O(1)` own-scale spatial packets.

Since the total good arclength is uniformly bounded,

\[
\boxed{
N^{high\text{-}amp}_{space}(R)=O(1)
}
\]

for every fixed pair `(a,eta_*)`, rather than `O(R)`.

Hence the M17-413 record-linear spatial multiplicity cannot survive on a fixed-amplitude positive-flux subpopulation under the uniform record-enstrophy bound.

This is the quantitative mechanism behind the amplitude-dilution survivor.

## 7. Interpretation

The parent-length loop may remain geometrically long and may retain total positive flux, but almost all of that flux must be carried, in arclength average, at normalized amplitudes tending to zero.

Thus the previous qualitative branch

\[
G_{high\text{-}amplitude\ flux\ participation\ loss}
\]

can be sharpened on retained parent-length loops to

\[
\boxed{
\text{fixed-amplitude positive-flux arclength fraction}
=O(R^{-1}).
}
\]

This is not an independent mystery: it is forced by bounded record enstrophy.

## 8. Remaining survivor

What remains is a genuinely low-amplitude, transversely broadened positive-flux carrier.

Its unresolved mechanisms are:

1. transverse size growth beyond the M17-450 `A_H ~ R` baseline;
2. scale-free shape/spectral degeneration `Pi -> infinity`;
3. coefficient-action redistribution inside the low-amplitude flux population;
4. good-time thinning;
5. chart/topology/genealogy and parent-to-record scale-map loss.

## 9. Audit verdict

**PASS — fixed normalized amplitude positive-flux participation is arclength-sparse.**

For every fixed amplitude threshold and fixed positive flux fraction threshold, the good arclength is uniformly bounded while the parent-length loop grows like `R`.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
