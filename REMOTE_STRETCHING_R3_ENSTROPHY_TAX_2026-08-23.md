# Remote Stretching `R^3` Enstrophy Tax — 2026-08-23

Status: **S-LEVEL SOURCE-ACTION LOWER BOUND / GLOBAL REGULARITY NOT PROVED.**

This note continues `REMOTE_STRAIN_SOURCE_EVOLUTION_IDENTITY_2026-08-23.md`. That exact identity reduced the remaining large-radius source-maintenance mechanism to the remote vorticity-stretching term

\[
\mathcal X_{stretch}(s)
=\int K(y)\psi_R(y,s)(\Sigma\Omega)(y,s)dy.
\]

The purpose here is to show that a fixed positive amount of this action pays the same `R^3` normalized-enstrophy-time cost as a fixed positive remote-strain action.

## 1. Exact L2 relation between strain and vorticity

For a smooth rapidly decaying divergence-free field in `R^3`,

\[
\int |\nabla U|^2dy
=\int |\Omega|^2dy,
\]

and with

\[
\nabla U=\Sigma+A,
\]

where `Sigma` is symmetric and `A` antisymmetric,

\[
\boxed{
\|\Sigma\|_2^2
=\frac12\|\Omega\|_2^2
=\frac12Z.
}
\]

At first-hitting normalized times,

\[
\|\Omega\|_\infty\le1.
\]

Hence

\[
\boxed{
\|\Sigma\Omega\|_2
\le
\|\Omega\|_\infty\|\Sigma\|_2
\le
\frac1{\sqrt2}Z^{1/2}.
}
\]

## 2. Remote kernel L2 bound

The strain kernel satisfies

\[
|K(y)|\le C_K|y|^{-3}.
\]

For a smooth remote cutoff `psi_R` supported outside radius comparable to `R`,

\[
\|K\psi_R\|_2
\le
C_{K,2}R^{-3/2}.
\]

Therefore

\[
\boxed{
|\mathcal X_{stretch}(s)|
\le
C_XR^{-3/2}Z(s)^{1/2},
}
\]

with a fixed kernel/cutoff constant `C_X>0`.

If the cutoff radius varies with time but obeys

\[
R(s)\ge R_->0
\]

throughout the stage, then

\[
\boxed{
|\mathcal X_{stretch}(s)|
\le
C_XR_-^{-3/2}Z(s)^{1/2}.
}
\]

## 3. Fixed stretching action forces R^3 occupancy

Let one normalized stage have length

\[
L_j=|I_j|.
\]

Suppose the remote stretching action satisfies

\[
\boxed{
\mathcal X_j
:=
\int_{I_j}|\mathcal X_{stretch}(s)|ds
\ge x_0>0.
}
\]

Then Cauchy--Schwarz in time gives

\[
x_0
\le
C_XR_-^{-3/2}
L_j^{1/2}
\left(\int_{I_j}Z(s)ds\right)^{1/2}.
\]

Therefore

\[
\boxed{
\int_{I_j}Z(s)ds
\ge
C_X^{-2}
R_-^3
\frac{x_0^2}{L_j}.
}
\]

If `L_j<=L_+`,

\[
\boxed{
\int_{I_j}Z(s)ds
\ge
C_X^{-2}L_+^{-1}
R_-^3x_0^2.
}
\]

Thus an order-one remote stretching action at normalized radius `R` costs `O(R^3)` normalized enstrophy-time occupancy.

## 4. Global physical energy consequence

The physical kinetic-energy dissipation packing on the geometric first-hitting stages gives

\[
\sum_jW_j^{-1/2}
\int_{I_j}Z(s)ds<\infty.
\]

Hence on an infinite sequence of stages with

\[
\mathcal X_j\ge x_0>0,
\qquad
R_{j,-}\to\infty,
\]

one must have

\[
\boxed{
\sum_jW_j^{-1/2}R_{j,-}^3<\infty.
}
\]

In particular,

\[
\boxed{
R_{j,-}=o(W_j^{1/6}).
}
\]

The corresponding physical radius

\[
\ell_{j,-}=W_j^{-1/2}R_{j,-}
\]

must satisfy

\[
\boxed{
\ell_{j,-}=o(W_j^{-1/3}).
}
\]

This is exactly the same contraction exponent found from the direct active-remote-strain estimate.

## 5. Vorticity-tight corollary

If the stage also satisfies the uniform vorticity-tight upper bound

\[
Z(s)\le Z_+
\]

throughout, then directly

\[
\mathcal X_j
\le
C_XR^{-3/2}Z_+^{1/2}L_+.
\]

Thus any fixed stretching action threshold `x0>0` forces a finite normalized radius

\[
\boxed{
R
\le
R_{X,\max}
:=
\left(
\frac{C_XL_+Z_+^{1/2}}{x_0}
\right)^{2/3}.
}
\]

So neither remote strain itself nor its remote stretching maintenance term can remain order-one at `R->infinity` inside a vorticity-tight corridor.

## 6. Combination with the exact source evolution identity

The remote-source evolution identity decomposes the payer into

\[
\mathcal T_{bulk},
\quad
\mathcal T_{cut},
\quad
\mathcal X_{stretch},
\quad
\mathcal V_{ann}.
\]

At large `R`, under the existing Morrey corridor:

- bulk advection and material cutoff crossing are `O(R^-2)`;
- fixed viscous annular action pays an `R^7` enstrophy-time tax;
- fixed remote stretching action pays an `R^3` enstrophy-time tax;
- physical-radius sweep is scale-critical and equals the logarithmic source-radius turnover action.

Thus no unidentified order-one source-replacement term remains in the evolution law.

## 7. Updated branch interpretation

For a genuinely remote active source on infinitely many late stages:

\[
\boxed{
\text{source maintenance}
\Longrightarrow
\begin{cases}
\text{physical radius sweep / source turnover},\\
R^3\text{ stretching occupancy tax},\\
R^7\text{ viscous occupancy tax},\\
\text{Morrey/local-energy failure}.
\end{cases}
}
\]

The last three routes either force the active physical radius to collapse rapidly toward the first-hitting point or enter an already typed local-energy/derivative exit. The source-radius sweep then becomes the natural remaining turnover quantity.

This does not yet prove that every such sweep is bounded by an existing global `T` budget; it identifies the exact scale-critical action that the `T` closure must control.

Status: **THE REMOTE VORTICITY-STRETCHING PAYER IS NOT A NEW COST-FREE ESCAPE. FIXED STRETCHING ACTION AT NORMALIZED RADIUS `R` PAYS AN `R^3` ENSTROPHY-TIME TAX, AND UNDER VORTICITY TIGHTNESS IT HAS A FINITE ACTIVE-RADIUS CEILING. THE REMAINING SCALE-CRITICAL SOURCE-REPLACEMENT QUANTITY IS LOGARITHMIC PHYSICAL-RADIUS SWEEP. GLOBAL REGULARITY IS NOT PROVED.**
