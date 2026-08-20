# Solenoidal/Leray Endgame Frontier — 2026-08-20

Overall status: **ACTIVE 3D NAVIER--STOKES PROOF ATTEMPT — GLOBAL REGULARITY NOT PROVED.**

This frontier consolidates the deductions after the vorticity-Hessian reformulation, the solenoidal uncertainty audit, the localization correction, and the Leray recurrence calculation.

## 1. Exact H1 production is vorticity-gradient non-normality

With `G=grad omega`,

\[
\boxed{
N
=\frac12\int S:(G^TG-GG^T)dx.
}
\]

Equivalently,

\[
\boxed{
2N
=\int S_{ab}
(\omega_i\partial_{ab}\omega_i-\omega_a\Delta\omega_b)dx.
}
\]

This yields

\[
\boxed{
\eta_{VI}
\le
\sqrt{\frac32}\|\omega\|_\infty\sqrt{Z/D}.
}
\]

Thus `P_V` production requires non-normal vorticity-gradient geometry, not merely large gradient magnitude.

## 2. Whole-field finite-moment branch

The sharp first-order solenoidal uncertainty constant `25/4` improves the whole-field radius bound. A direct second-order radial spectral reduction improves it further.

The rigorous Temple estimate gives

\[
\mathcal C_{2,sol}
\ge6.7199874273
\]

for

\[
M\sqrt D\ge\mathcal C_{2,sol}Z^{3/2}.
\]

Hence a whole-space finite-second-moment first-hitting threshold satisfies

\[
\boxed{
R_{\omega,global}
\ge2.3424019207\sqrt\nu.
}
\]

This is **not** an active-core radius statement. A weak remote tail may inflate the global moment.

## 3. Scope correction

The direct comparison of the global rms radius with the non-T active-core upper radius is withdrawn unless a core-tail moment comparison is proved.

The ancient global second moment may also be infinite. Therefore the correct local route uses cutoff or divergence-free localization.

## 4. Bogovskii-localized second-order solenoidal gate

For the divergence-free corrected field supported in `B_{2R}`,

\[
\boxed{
\|\Delta v_R\|_2
\ge
\frac{1.6799968568}{R^2}
\|\omega\|_{L^2(B_R)}.
}
\]

Returning to the original vorticity gives a local dichotomy between second-derivative cost and annular leakage.

## 5. Fully explicit cutoff gate

Without Bogovskii correction, use the explicit quintic radial cutoff. Then

\[
\boxed{
\begin{aligned}
&R^2\frac{\|\Delta\Omega\|_{B_{2R}}}{\|\Omega\|_{B_R}}
+\frac{15}{4}R\frac{\|\nabla\Omega\|_{A_R}}{\|\Omega\|_{B_R}}\\
&\quad+
\left(\frac{10}{\sqrt3}+\frac{15}{4}\right)
\frac{\|\Omega\|_{A_R}}{\|\Omega\|_{B_R}}
\ge\frac9{16}.
\end{aligned}
}
\]

All localization constants here are explicit.

## 6. First-hitting analyticity converts the cutoff gate into an exclusion scale

If

\[
|\Omega(y_*)|=1,
\qquad
\sup_{|Im y|<\rho_0}|\Omega|\le M_0,
\]

Cauchy estimates give a local enstrophy mass floor and a local `Delta Omega` upper bound.

For

\[
R\le
R_{ex}^{explicit}
=
\min\left\{
\frac{\rho_0}{12M_0},
0.03458381\frac{\rho_0}{\sqrt{M_0}}
\right\},
\]

one must have at least one of

\[
\boxed{
R\frac{\|\nabla\Omega\|_{A_R}}{\|\Omega\|_{B_R}}
\ge0.0375
}
\]

or

\[
\boxed{
\frac{\|\Omega\|_{A_R}}{\|\Omega\|_{B_R}}
\ge0.01476610.
}
\]

Thus an ultra-small isolated first-hitting core is impossible: it must carry a fixed annular derivative or vorticity-mass fraction.

On the smooth rapidly-decaying initial-data track, the standard vorticity analyticity theorem gives

\[
M_0=M,
\qquad
\rho_0=\frac{\sqrt{\sigma\nu}}{c(M)},
\quad M>1,\ 0<\sigma<1.
\]

For `M=2`,

\[
R_{ex}^{explicit}
\approx
\frac{0.02445445\sqrt{\sigma\nu}}{c(2)}.
\]

The theorem statement does not supply a numerical `c(2)`, so this scale is universal-symbolic rather than fully numerical.

## 7. Exact Leray H1 recurrence tax

In backward Leray variables,

\[
\boxed{
\frac12P_s+\frac34P+\nu H=N_L.
}
\]

For a nonzero precompact recurrent class `K`, define

\[
\kappa_K=\inf_K P/H>0.
\]

Recurrence therefore forces

\[
\boxed{
\Lambda_K
\ge
\nu+\frac34\kappa_K.
}
\]

The previous local target `Lambda_K<nu` was stronger than necessary. To eliminate recurrent survival it is enough to prove

\[
\boxed{
\Lambda_K
<
\nu+\frac34\kappa_K.
}
\]

The positive `3 kappa_K/4` is a genuinely dynamic similarity-recurrence gap.

## 8. Non-normality also forces a strain-amplitude floor

Bottcher--Wenzel gives

\[
N_L
\le
\sqrt2\|\Sigma\|_\infty P.
\]

If

\[
\kappa_K^+=\sup_K P/H,
\]

then recurrent survival requires

\[
\boxed{
\sup_K\|\Sigma\|_\infty
\ge
\frac1{\sqrt2}
\left(\frac34+\frac\nu{\kappa_K^+}\right).
}
\]

In particular,

\[
\boxed{
\sup_K\|\Sigma\|_\infty
\ge0.530330086.
}
\]

Thus the survivor must carry both strong normalized strain and strong vorticity-gradient non-normality.

## 9. Current restricted survivor

If repeated `H/T` does not occur, a hypothetical singularity is now forced into a recurrent Type-I `P_V` ancient class with all of the following:

- nonzero H2-precompact active profiles;
- first-hitting vorticity cap;
- dynamically passive but globally necessary critical tail;
- no active singular KKT contact reaction;
- local small-core exclusion unless fixed annular leakage occurs;
- `Lambda_K >= nu + 3 kappa_K/4`;
- normalized strain amplitude at least `0.530330086`, and larger when viscosity is retained;
- strongly non-normal vorticity-gradient geometry;
- near-max-mid/covariance rigidity whenever production approaches its static algebraic ceiling.

## 10. Principal next target

There are now two closely coupled rigidity problems.

1. **Double-saturation incompatibility:** near Böttcher--Wenzel saturation pushes `grad Omega` toward rank-one shear geometry, while near static H1 saturation pushes strain derivatives toward the previously derived max-mid/one-dimensional covariance geometry. Quantify whether both can occur in the same strain-compatible finite-energy profile.
2. **Recurrent threshold gap:** estimate `kappa_K`, `kappa_K^+`, `B_K`, and the static efficiency defect `delta_K` sufficiently to violate

\[
(1-\delta_K)\frac4{\sqrt6}B_K\kappa_K^+
\ge
\nu+\frac34\kappa_K.
\]

Status: **GLOBAL REGULARITY REMAINS UNPROVED. THE NON-H/T SURVIVOR IS NOW CONSTRAINED SIMULTANEOUSLY BY A LOCAL ANALYTIC/UNCERTAINTY LEAKAGE GATE AND A STRICT LERAY RECURRENCE TAX. THE NEXT TARGET IS THE INCOMPATIBILITY OF THE TWO REQUIRED NEAR-SATURATION GEOMETRIES.**