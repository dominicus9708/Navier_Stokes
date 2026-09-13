# M19 Current Frontier

**Date:** 2026-09-13  
**Current tip:** **M19-193**  
**Status:** ACTIVE CALCULATION / FINITE-HIGH W1 SEVERITY APERIODIC FRONTIER + RELATIVE-PERIODIC HARD CORE / FINAL ROOT-PROOF CERTIFICATION STILL OPEN

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Phase policy

M18 remains frozen as the analysis/audit family. M19 is the active calculation/closure family.

\[
\boxed{\text{M18 certified analysis}\Longrightarrow\text{M19 new analysis + calculation}\Longrightarrow\text{closure or explicit theorem frontier}.}
\]

## 2. Retained recurrent hard-cocycle reduction

On the certified smooth passive-spectator critical corridor, linearized vorticity satisfies

\[
\frac12\frac d{ds}\|\eta\|_2^2
+\nu\|\nabla\eta\|_2^2
+\frac14\|\eta\|_2^2
=\mathcal C_U[W].
\]

The tail coupling is relatively compact with respect to the bare similarity-vorticity generator, so

\[
\lambda_{ess}\le-\frac14<0.
\]

Differentiated scattering covariance and uniform hard observability exclude positive hard Lyapunov growth. The remaining complete hard dynamics is finite-dimensional and zero/unit-growth after exact time/rotation symmetry bookkeeping.

For a recurrent hard family,

\[
\langle T_N\rangle
=\nu\langle P_N\rangle+\frac14\langle Z_N\rangle.
\]

Collective local and nonlocal compensation are sublinear in family dimension.

## 3. Exponential-memory metric removes occupation distortion — M19-180--181

Define

\[
G_\lambda(s)=\lambda\int_0^\infty e^{-\lambda r}H(s-r)\,dr,
\qquad
G_\lambda'=\lambda(H-G_\lambda),
\]

and

\[
X_\lambda=G_\lambda^{-1/2}HG_\lambda^{-1/2}.
\]

Then

\[
\frac d{ds}\log\det G_\lambda
=\lambda(\operatorname{tr}X_\lambda-N),
\]

so on a recurrent component

\[
\langle\operatorname{tr}X_\lambda\rangle=N.
\]

The moving-metric connection term

\[
R_\lambda=\frac\lambda2\operatorname{tr}(X_\lambda-X_\lambda^2)
\]

has

\[
\boxed{\langle R_\lambda\rangle\le0.}
\]

Therefore the provisional `lambda/8` loss disappears and

\[
\nu\langle P_\lambda\rangle+\frac14N
\le\langle T_\lambda\rangle.
\]

The Bessel distortion is

\[
\kappa_\lambda=1+\frac{L_+}{\lambda},
\]

and since there is no positive averaged connection penalty, one may take

\[
\lambda\to\infty,
\qquad
\kappa_\lambda\downarrow1.
\]

Thus the previous unknown occupation constant is removed.

## 4. Mean-activity dimension criterion — M19-182--183

For `3/2<a<3`, let

\[
q(a)=\frac{3-a}{2a},
\qquad
d(a)=\frac43-\frac1a<1.
\]

Define recurrent mean coefficients

\[
\mathfrak A
=C_{LT}^{3/5}\left\langle\|S_U\|_{5/2}^{5/2}\right\rangle^{2/5},
\]

\[
\mathfrak B_a
=C_a\left\langle
\|\nabla\Omega\|_a^{1/(1-q(a))}
\right\rangle^{1-q(a)}.
\]

For total observable hard-channel count `M`,

\[
\boxed{
\frac14+\nu x
\le
\mathfrak A M^{-2/5}x^{3/5}
+\mathfrak B_aM^{d(a)-1}x^{q(a)}.
}
\]

The clean choice `a=2` gives

\[
q=\frac14,
\qquad d=\frac56,
\]

with

\[
\mathfrak A\lesssim Z_+^{7/20}\Pi^{3/20},
\qquad
\mathfrak B_2\lesssim\Pi^{1/2},
\qquad
\Pi:=\langle P_U\rangle.
\]

## 5. Recurrent enstrophy bounds mean palinstrophy — M19-184--187

The background identity is

\[
\frac12Z_U'+\frac14Z_U+\nu P_U
=\int\Omega\cdot S_U\Omega.
\]

Using Calderon--Zygmund and interpolation,

\[
\left|\int\Omega\cdot S_U\Omega\right|
\le C_EZ_U^{3/4}P_U^{3/4}.
\]

Hence, under `Z_U<=Z_+`,

\[
\boxed{
\Pi\le C_E^4\nu^{-4}Z_+^3.
}
\]

This reduces the aperiodic dimension test to a small-enstrophy criterion of the form

\[
K_*^{(M)}\frac{Z_+^2}{\nu^3}<\frac14.
\]

Finite `Z_+` alone does not imply this smallness.

## 6. Genuine aperiodicity pays at least five exact hard channels — M19-185, M19-189--190

A genuinely aperiodic quotient component needs at least two extra quotient directions.

A nonzero smooth decaying divergence-free whole-space state cannot be invariant under all of `SO(3)`, so

\[
\boxed{\dim(SO(3)\cdot U)\ge2.}
\]

Off the RSS branch, the exact time tangent `partial_s U` is independent of the rotation tangents. Therefore genuine aperiodicity requires at least

\[
\boxed{M\ge2\text{ extra}+2\text{ rotation}+1\text{ time}=5}
\]

observable hard channels.

On the generic discrete-isotropy stratum,

\[
M\ge6.
\]

For general `M`, the Young-reduced constants satisfy

\[
K_1^{(M)}\propto M^{-1},
\qquad
K_2^{(M)}\propto M^{-2/9},
\]

so define

\[
K_*^{(M)}
=K_1^{(M)}C_E^{3/2}+K_2^{(M)}C_E^{8/3}.
\]

The universal five-channel aperiodic exclusion criterion is

\[
\boxed{
K_*^{(5)}\frac{Z_+^2}{\nu^3}<\frac14.
}
\]

## 7. W1 internal enstrophy redundancy — M19-188, M19-191

M18-042 remains correct for global ROOT-CERT bookkeeping: bounded normalized enstrophy is not certified from arbitrary upstream data.

However, inside the simultaneous final W1 lane, Type-I amplitude, bounded weak-L3, and bounded shell frequency imply bounded normalized enstrophy quantitatively.

Let

\[
(T_*-t)\|\omega(t)\|_\infty\le K_I,
\qquad
W_*:=\sup_s\|U(s)\|_{L^{3,\infty}},
\qquad
\Gamma_R\le\Gamma_*.
\]

For any split radius `R_0>0`,

\[
\int_{|y|\le R_0}|\Omega|^2dy
\lesssim K_I^2R_0^3,
\]

while Lorentz embedding plus the shell-frequency ratio give

\[
\int_{|y|\ge R_0}|\Omega|^2dy
\lesssim\Gamma_*^2W_*^2R_0^{-1}.
\]

Thus bounded `Z` is internally redundant on this simultaneous lane.

This does **not** remove the upstream `Z` root globally because existing routes to `H_F,H_W` can themselves use bounded-enstrophy/Campanato information.

## 8. Optimized W1 severity parameter — M19-192

Optimize

\[
K_I^2R_0^3+\Gamma_*^2W_*^2R_0^{-1}
\]

over `R_0`. The minimizer satisfies

\[
R_0^4=\frac{\Gamma_*^2W_*^2}{3K_I^2},
\]

and gives

\[
\boxed{
Z_+
\lesssim
K_I^{1/2}(\Gamma_*W_*)^{3/2}.
}
\]

Therefore define the current optimized W1 severity

\[
\boxed{
\Xi_{W1}
:=
\frac{K_I(\Gamma_*W_*)^3}{\nu^3}.
}
\]

There is an explicit current threshold

\[
\Xi_c=(4C_{opt}^2K_*^{(5)})^{-1}
\]

such that

\[
\boxed{
\Xi_{W1}<\Xi_c
\Longrightarrow
\text{no genuinely aperiodic recurrent hard component}.
}
\]

Hence every genuinely aperiodic survivor must satisfy

\[
\boxed{\Xi_{W1}\ge\Xi_c.}
\]

## 9. Finite-high threshold strata — M19-193

Choose finite positive thresholds `k_0,gamma_0,w_0` satisfying

\[
k_0(\gamma_0w_0)^3<\nu^3\Xi_c.
\]

Then genuine aperiodicity implies

\[
\boxed{
K_I\ge k_0
\ \lor\ 
\Gamma_*\ge\gamma_0
\ \lor\ 
W_*\ge w_0.
}
\]

These are **finite-high threshold strata**, not the old escalation roots. All three ceilings may remain finite.

Therefore

\[
\boxed{
\text{finite-high threshold stratum}
\neq
\text{Type-II / frequency escalation / weak-L3 escalation}.
}
\]

## 10. Current live analytic branches

### A. Aperiodic W1 hard frontier

The primary aperiodic frontier is now

\[
\boxed{\Xi_{W1}\ge\Xi_c.}
\]

The next target is to determine whether any of the finite-high strata

\[
\mathcal H_{K_I}^{high},
\qquad
\mathcal H_{\Gamma}^{high},
\qquad
\mathcal H_W^{high}
\]

has an independent quantitative routing/regularity theorem.

### B. Relative-periodic hard core

Once the aperiodic branch is reduced, moderate finite-amplitude RSS/RDSS remains a finite-dimensional/low-mode problem. Fixed-moduli nonsymmetry kernel degeneracy and irrational elliptic unit blocks remain the principal local Fredholm obstructions; rational elliptic phases reduce to finite-iterate kernels.

### C. Long-period branch

`S->infinity` remains an invariant-measure/compactness limit problem. Any genuinely aperiodic limiting component is subject to the same five-channel severity threshold above.

## 11. Final proof-chain certification remains open

Even if the active analytic branches close, global regularity still requires:

1. arbitrary-singularity entry certification;
2. historical branch completeness and remaining alignment/nonreuse checks;
3. full beginning-to-end independent audit.

## 12. Permanent firewalls

\[
\boxed{\text{bounded W1 constants}\neq\text{small W1 constants}},
\]

\[
\boxed{\text{internal W1 hypothesis redundancy}\neq\text{global ROOT-CERT closure}},
\]

\[
\boxed{\text{finite-high W1 threshold}\neq\text{escalation to infinity}},
\]

\[
\boxed{\text{positive recurrent palinstrophy floor}\neq\text{finite-energy contradiction}},
\]

\[
\boxed{\text{quotienting symmetry}\neq\text{removing symmetry-channel damping cost}},
\]

\[
\boxed{\text{relative periodicity}\neq\text{relative-periodic nonexistence}}.
\]

---

\[
\boxed{\text{M19 ACTIVE TIP = M19-193.}}
\]
