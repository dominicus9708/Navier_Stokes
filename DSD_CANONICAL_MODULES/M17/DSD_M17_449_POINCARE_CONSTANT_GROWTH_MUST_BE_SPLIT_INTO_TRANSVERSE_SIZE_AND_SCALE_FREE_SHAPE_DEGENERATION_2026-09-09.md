# DSD M17-449 — Poincare growth must be split into transverse size growth and scale-free shape/spectral degeneration

Date: 2026-09-09  
Canonical ID: **M17-449**

Status: **ACTIVE REPRESENTATION CORRECTION / M17-448 SCALE-NORMALIZATION REFINEMENT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Correction target

M17-448 correctly derived the bottleneck palinstrophy ancestry estimate

\[
\mathcal P_{anc,m}
\gtrsim
\beta_m\frac{R_m}{C_{P,m}},
\]

and correctly observed that unbounded `C_P` is a loss of compact transverse geometry relative to one fixed reference chart.

However the interpretation `large C_P = thin-neck/spectral-shape degeneration` is too narrow because `C_P` has dimensions of length squared in the normalized transverse plane.

Pure isotropic enlargement already makes `C_P` large.

## 2. Exact transverse dilation law

For a two-dimensional cross-section `A` and scalar dilation

\[
A_\lambda:=\lambda A,
\]

the optimal Poincare constant satisfies

\[
\boxed{
C_P(A_\lambda)=\lambda^2C_P(A).
}
\]

At the same time

\[
|A_\lambda|=\lambda^2|A|.
\]

Therefore the ratio

\[
\boxed{
\Pi(A):=\frac{C_P(A)}{|A|}
}
\]

is invariant under isotropic transverse dilation.

`Pi` is the appropriate dimensionless shape/spectral descriptor when area is already tracked separately.

## 3. Size and shape factorization

Use the M17-439 normalized transverse area

\[
\mathfrak A_m:=|A_m|.
\]

Then define

\[
\boxed{
\Pi_m:=\frac{C_{P,m}}{\mathfrak A_m}.
}
\]

Hence

\[
\boxed{
C_{P,m}=\mathfrak A_m\Pi_m.
}
\]

The two mechanisms are now distinct:

1. `mathfrak A_m -> infinity`: transverse support/size decompactification;
2. `Pi_m -> infinity`: scale-free neck/eccentricity/spectral-shape degeneration.

A round disk whose radius tends to infinity has `C_P -> infinity` but `Pi ~ constant`; it is size decompactification, not a thin-neck instability.

## 4. Corrected M17-448 bottleneck ancestry

M17-448 gives

\[
\mathcal P_{anc,m}
\gtrsim
\beta_m\frac{R_m}{C_{P,m}}.
\]

Substitute the factorization:

\[
\boxed{
\mathcal P_{anc,m}
\gtrsim
\beta_m
\frac{R_m}{\mathfrak A_m}
\frac1{\Pi_m}.
}
\]

Define the transverse size factor relative to the record-linear baseline

\[
\boxed{
S_m:=\frac{\mathfrak A_m}{R_m}.
}
\]

Then

\[
\boxed{
\mathcal P_{anc,m}
\gtrsim
\frac{\beta_m}{S_m\Pi_m}.
}
\]

Thus the exact survival condition for this bottleneck currency is

\[
\boxed{
\sum_m\frac{\beta_m}{S_m\Pi_m}<\infty.
}
\]

This is the canonical replacement for interpreting `C_P,m >= R_m` as necessarily record-linear neck degeneration.

## 5. Consequences

If `beta_m >= beta_* > 0` and both `S_m` and `Pi_m` remain bounded, then

\[
\sum_m\mathcal P_{anc,m}=\infty,
\]

contradicting M17-307.

Therefore a persistent bottleneck must have at least one of

\[
S_m\to\infty,
\qquad
\Pi_m\to\infty,
\qquad
\beta_m\to0
\]

strongly enough that

\[
\sum_m(S_m\Pi_m)^{-1}<\infty
\]

when `beta_m` has a positive lower bound.

For a record-index power model

\[
S_m\Pi_m\sim m^p,
\]

the harmonic borderline is

\[
\boxed{p=1,}
\]

and power-law survival requires `p>1`.

## 6. Correction to the deformation interpretation

M17-448 proved, for a material image of one fixed reference cross-section,

\[
C_P(A_m)\le C_{P,0}e^{6K_m}.
\]

That estimate remains valid.

But

\[
K_m\gtrsim \log C_{P,m}
\]

contains both ordinary transverse size dilation and scale-free shape distortion.

It must not be read as a pure neck-formation lower bound unless `mathfrak A_m` is separately normalized or bounded.

True shape degeneration is measured by `Pi_m`, not by `C_P,m` alone.

## 7. Updated split

\[
\boxed{
\begin{aligned}
G_{low\text{-}amplitude\ separator}
\Longrightarrow{}&
G_{palinstrophy\ payer}\\
&\lor G_{transverse\ size\ decompactification}\;(S_m\to\infty)\\
&\lor G_{scale\text{-}free\ neck/spectral\ degeneration}\;(\Pi_m\to\infty)\\
&\lor G_{separator\ time\ thinning}\\
&\lor G_{high\text{-}amplitude\ flux\ participation\ loss}\\
&\lor G_{chart/topology/genealogy\ loss}.
\end{aligned}
}
\]

## 8. Audit verdict

**PASS as a correction/refinement of M17-448.**

The M17-448 palinstrophy formula remains certified. The interpretation is sharpened: record-linear `C_P` growth can arise from ordinary transverse area dilation and is not by itself evidence of thin-neck shape degeneration.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
