# M19-192 — Optimizing the W1 core-tail split replaces additive enstrophy control by a sharp multiplicative severity parameter

**Date:** 2026-09-13  
**Status:** ACTIVE CALCULATION / QUANTITATIVE SHARPENING OF M19-191

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. M19-191 used a nonoptimized unit split

M19-191 obtained

\[
Z\le C_Z\left(K_I^2+\Gamma_*^2W_*^2\right)
\]

by splitting the similarity domain at radius `R=1`.

The W1 shell-frequency and weak-L3 bounds hold at every retained shell scale, so the split radius can be chosen freely.

## 2. Core estimate at arbitrary radius R0

Type-I gives

\[
\|\Omega\|_\infty\le K_I.
\]

Therefore for every `R0>0`,

\[
\boxed{
\int_{|y|\le R_0}|\Omega|^2dy
\le C_0K_I^2R_0^3.
}
\]

## 3. Tail estimate beginning at R0

On a shell `A_R^*`, weak-L3 and shell-frequency control give

\[
\|U-m_R\|_2\le C R^{1/2}W_*,
\]

\[
\|\nabla U\|_2^2(A_R^*)
\le C\Gamma_*^2W_*^2R^{-1}.
\]

Choose dyadic radii

\[
R_k=2^kR_0,
\qquad k\ge0.
\]

Bounded overlap gives

\[
\int_{|y|\ge R_0}|\Omega|^2dy
\le
C_1\Gamma_*^2W_*^2
\sum_{k\ge0}(2^kR_0)^{-1}.
\]

Hence

\[
\boxed{
\int_{|y|\ge R_0}|\Omega|^2dy
\le C_2\Gamma_*^2W_*^2R_0^{-1}.
}
\]

## 4. Optimize the split

Set

\[
A:=C_0K_I^2,
\qquad
B:=C_2\Gamma_*^2W_*^2.
\]

Then

\[
Z\le AR_0^3+BR_0^{-1}.
\]

For `A,B>0`, the unique minimizer satisfies

\[
3AR_0^2-BR_0^{-2}=0,
\]

so

\[
\boxed{
R_0^4=\frac{B}{3A}.
}
\]

At this radius,

\[
\min_{R_0>0}(AR_0^3+BR_0^{-1})
=4\,3^{-3/4}A^{1/4}B^{3/4}.
\]

Therefore

\[
\boxed{
Z_+
\le
C_{opt}\,
K_I^{1/2}
(\Gamma_*W_*)^{3/2}.
}
\]

The degenerate cases `A=0` or `B=0` are obtained by limit and correspond to a much more rigid/vanishing situation.

## 5. Five-channel aperiodic criterion

M19-190 excludes genuinely aperiodic quotient recurrence if

\[
K_*^{(5)}\frac{Z_+^2}{\nu^3}<\frac14.
\]

Using the optimized W1 bound,

\[
Z_+^2
\le
C_{opt}^2
K_I(\Gamma_*W_*)^3.
\]

Hence a sufficient exclusion criterion is

\[
\boxed{
C_{opt}^2K_*^{(5)}
\frac{K_I(\Gamma_*W_*)^3}{\nu^3}
<\frac14.
}
\]

Define the current W1 severity parameter

\[
\boxed{
\Xi_{W1}
:=
\frac{K_I(\Gamma_*W_*)^3}{\nu^3}.
}
\]

Then

\[
\boxed{
\Xi_{W1}<\Xi_c
\Longrightarrow
\text{no genuinely aperiodic recurrent hard component},
}
\]

where

\[
\Xi_c=(4C_{opt}^2K_*^{(5)})^{-1}.
\]

## 6. Complementary hard branch

Every genuinely aperiodic survivor must satisfy

\[
\boxed{
\Xi_{W1}\ge\Xi_c.
}
\]

This is stronger than the additive M19-191 statement. In particular, a large value of only one factor is not enough if another factor is sufficiently small.

The surviving branch requires a joint amplitude--frequency--critical-size burden.

## 7. Generic rotational stratum

Replacing `K_*^(5)` by the smaller generic `K_*^(6)` gives the stronger threshold

\[
\boxed{
C_{opt}^2K_*^{(6)}\Xi_{W1}<\frac14
}
\]

on discrete-rotation-isotropy strata.

## 8. Firewall

\[
\boxed{
\text{large additive W1 ceiling}
\neq
\text{large optimized multiplicative severity}.
}
\]

The optimized parameter should be used in subsequent aperiodic-branch audits.

---

\[
\boxed{\text{M19-192: APERIODICITY REQUIRES A LARGE MULTIPLICATIVE W1 SEVERITY }\Xi_{W1}.}
\]
