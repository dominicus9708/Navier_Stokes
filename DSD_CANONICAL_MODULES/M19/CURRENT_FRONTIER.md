# M19 Current Frontier

**Date:** 2026-09-13  
**Current tip:** **M19-191**  
**Status:** ACTIVE CALCULATION / FIVE-CHANNEL APERIODIC THRESHOLD + LARGE-BUT-FINITE W1 AMPLITUDE/FREQUENCY HARD BRANCH / RELATIVE-PERIODIC HARD CORE / FINAL ROOT-PROOF CERTIFICATION STILL OPEN

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Phase policy

M18 remains frozen as the analysis/audit family. M19 is the active calculation/closure family.

\[
\boxed{\text{M18 certified analysis}\Longrightarrow\text{M19 new analysis + calculation}\Longrightarrow\text{closure or explicit theorem frontier}.}
\]

M19 is not merely a summary of M18. Its working loop is

\[
\boxed{\text{accumulated calculation}\to\text{new structural analysis}\to\text{new calculation}\to\text{new frontier}.}
\]

## 2. Retained hard-cocycle reduction through M19-179

The recurrent weak-critical scattering problem has been reduced, on its certified smooth passive-spectator corridor, to a finite-dimensional interior hard cocycle.

For linearized vorticity `eta`,

\[
\frac12\frac d{ds}\|\eta\|_2^2
+\nu\|\nabla\eta\|_2^2
+\frac14\|\eta\|_2^2
=\mathcal C_U[W].
\]

The critical tail is a relatively compact perturbation of the bare similarity-vorticity generator, so

\[
\boxed{\lambda_{ess}\le-1/4<0.}
\]

Differentiated scattering covariance plus uniform hard observability exclude positive hard Lyapunov exponents. The remaining complete hard dynamics is finite-dimensional and zero/unit-growth after exact time/rotation symmetry bookkeeping.

The collective compensation trace is sublinear in hard-family dimension. For `3/2<a<3`,

\[
|T_{str}|\lesssim\|S_U\|_{5/2}P_N^{3/5},
\]

\[
|T_{nl}|\lesssim
\|\nabla\Omega\|_a
Z_N^{\,11/6-5/(2a)}
P_N^{\,3/(2a)-1/2},
\]

with total degree

\[
\boxed{d(a)=\frac43-\frac1a<1.}
\]

For a general compact recurrent component,

\[
\boxed{
\langle T_N\rangle
=\nu\langle P_N\rangle+\frac14\langle Z_N\rangle.
}
\]

## 3. Exponential-memory metric removes occupation distortion — M19-180--181

Define

\[
G_\lambda(s)
=\lambda\int_0^\infty e^{-\lambda r}H(s-r)\,dr,
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
\boxed{\langle\operatorname{tr}X_\lambda\rangle=N.}
\]

The moving-metric connection term is

\[
R_\lambda
=\frac\lambda2\operatorname{tr}(X_\lambda-X_\lambda^2).
\]

Matrix Cauchy plus Jensen yields

\[
\boxed{\langle R_\lambda\rangle\le0.}
\]

Therefore the provisional `lambda/8` damping loss from M19-179 disappears:

\[
\boxed{
\nu\langle P_\lambda\rangle+\frac14N
\le\langle T_\lambda\rangle.
}
\]

The only occupation distortion is

\[
\kappa_\lambda=1+\frac{L_+}{\lambda},
\]

and since the averaged connection term is favorable one may take

\[
\boxed{\lambda\to\infty,\qquad \kappa_\lambda\downarrow1.}
\]

Thus the old unknown `kappa_occ` is removed as an independent constant.

## 4. Mean-activity scalar hard-dimension criterion — M19-181--183

After generalized Lieb--Thirring/HLS and temporal Holder, define

\[
\mathfrak A
=C_{LT}^{3/5}\left\langle\|S_U\|_{5/2}^{5/2}\right\rangle^{2/5},
\]

\[
\mathfrak B_a
=C_a\left\langle
\|\nabla\Omega\|_a^{1/(1-q(a))}
\right\rangle^{1-q(a)},
\]

where

\[
q(a)=\frac{3-a}{2a},
\qquad
d(a)=\frac43-\frac1a.
\]

For a total hard-family dimension `M`, the mean trace test is

\[
\boxed{
\frac14+\nu x
\le
\mathfrak A M^{-2/5}x^{3/5}
+\mathfrak B_a M^{d(a)-1}x^{q(a)}.
}
\]

The clean choice `a=2` gives

\[
q=1/4,
\qquad d=5/6,
\]

and

\[
\mathfrak B_2\lesssim\langle P_U\rangle^{1/2},
\qquad
\mathfrak A\lesssim Z_+^{7/20}\langle P_U\rangle^{3/20}.
\]

For fixed `M`, the exact scalar maximizer of

\[
A_Mx^{3/5}+B_Mx^{1/4}-\nu x
\]

is characterized by a unique positive root `y=x^{1/20}` of

\[
\boxed{
\nu y^{15}-\frac35A_My^7-\frac14B_M=0.
}
\]

## 5. Aperiodic recurrence pays positive derivative activity — M19-184--187

Let

\[
\Pi:=\langle P_U\rangle.
\]

Low enough `Pi` forces quotient hard dimension at most one, hence relative-periodic dynamics after at most a two-fold quotient return.

The recurrent background enstrophy identity gives

\[
\frac14\overline Z_U+\nu\Pi
=\left\langle\int\Omega\cdot S_U\Omega\right\rangle.
\]

Using Calderon--Zygmund and interpolation,

\[
\left|\int\Omega\cdot S_U\Omega\right|
\le C_EZ_U^{3/4}P_U^{3/4}.
\]

Therefore, if `Z_U<=Z_+`,

\[
\boxed{
\Pi\le C_E^4\nu^{-4}Z_+^3.
}
\]

The dimension-one test can thus be reduced to a dimensionless small-enstrophy condition of the form

\[
\boxed{
K_*\frac{Z_+^2}{\nu^3}<\frac14.
}
\]

This is a sufficient condition, not an unconditional theorem.

## 6. Exact symmetry channels strengthen the aperiodic test — M19-185, M19-189--190

A genuinely aperiodic quotient component needs at least two extra quotient directions.

A nonzero smooth decaying divergence-free whole-space state cannot be invariant under all of `SO(3)`, so

\[
\boxed{\dim(SO(3)\cdot U)\ge2.}
\]

Off the RSS branch, the exact time tangent `partial_s U` is independent of the rotation tangents. Thus genuine aperiodicity requires at least

\[
\boxed{M\ge2\text{ extra}+2\text{ rotation}+1\text{ time}=5}
\]

observable hard channels.

On the generic discrete-isotropy stratum,

\[
\boxed{M\ge6.}
\]

For general `M`, the Young-reduced coefficients scale as

\[
K_1^{(M)}\propto M^{-1},
\qquad
K_2^{(M)}\propto M^{-2/9}.
\]

Define

\[
K_*^{(M)}
=K_1^{(M)}C_E^{3/2}+K_2^{(M)}C_E^{8/3}.
\]

The universal aperiodic exclusion criterion is therefore

\[
\boxed{
K_*^{(5)}\frac{Z_+^2}{\nu^3}<\frac14
\Longrightarrow
\text{no genuine aperiodic recurrent hard component}.
}
\]

Any genuinely aperiodic survivor must pay

\[
\boxed{
\frac{Z_+^2}{\nu^3}
\ge\frac1{4K_*^{(5)}}.
}
\]

## 7. W1 hypothesis refinement — M19-188, M19-191

M18-042 correctly records that bounded normalized enstrophy is not globally certified from arbitrary upstream data and that its complement remains part of ROOT-CERT.

However, inside the **simultaneous final W1 lane**, bounded `Z` is quantitatively redundant once Type-I amplitude, weak-L3, and bounded shell frequency all hold.

Let

\[
(T_*-t)\|\omega(t)\|_\infty\le K_I,
\qquad
W_*:=\sup_s\|U(s)\|_{L^{3,\infty}},
\qquad
\Gamma_R\le\Gamma_*.
\]

Then similarity Type-I gives

\[
\|\Omega\|_\infty\le K_I,
\]

so core enstrophy is `O(K_I^2)`.

On a shell `A_R^*`, Lorentz embedding gives

\[
\|U-m_R\|_2\lesssim R^{1/2}W_*,
\]

and the frequency ratio gives

\[
\|\nabla U\|_2^2(A_R^*)
\lesssim\Gamma_*^2W_*^2R^{-1}.
\]

Dyadic summation over `R>=1` yields

\[
\boxed{
Z_+
\le C_Z\left(K_I^2+\Gamma_*^2W_*^2\right).
}
\]

Therefore the current explicit W1-subcorridor aperiodic exclusion criterion is

\[
\boxed{
K_*^{(5)}C_Z^2
\frac{\left(K_I^2+\Gamma_*^2W_*^2\right)^2}{\nu^3}
<\frac14.
}
\]

This is an **internal W1 redundancy**, not yet a global deletion of the upstream `Z` root: existing entry routes for `H_F,H_W` can themselves use bounded-enstrophy/Campanato information.

## 8. Current live analytic branches

### A. Low-amplitude/frequency recurrent hard lane

If

\[
K_*^{(5)}C_Z^2
\frac{\left(K_I^2+\Gamma_*^2W_*^2\right)^2}{\nu^3}
<\frac14,
\]

then genuine aperiodic recurrent hard dynamics is excluded and the survivor reduces to RSS/RDSS after a finite quotient iterate.

### B. Large-but-finite recurrent W1 hard lane

The remaining genuinely aperiodic branch is quantitatively constrained by

\[
\boxed{
K_I^2+\Gamma_*^2W_*^2
\ge c_*\nu^{3/2}
}
\]

for a fixed current threshold constant `c_*`.

This is not the same as Type-II, frequency escalation, weak-L3 escalation, or `Z->infinity`. All three W1 ceilings can remain finite while lying above the threshold.

This large-but-finite amplitude/frequency branch is now the primary aperiodic analytic frontier.

### C. Relative-periodic hard core

Once the aperiodic branch is reduced, the remaining moderate finite-amplitude RSS/RDSS problem is finite-dimensional/low-mode. Fixed-moduli nonsymmetry kernel degeneracy and irrational elliptic unit blocks remain the local Fredholm obstructions; rational elliptic phases reduce to finite-iterate kernels.

### D. Long-period branch

`S->infinity` remains an invariant-measure/compactness limit problem. Its genuinely aperiodic limiting components are subject to the same five-channel threshold above.

## 9. Next analytic target

The next calculation should test whether the large-but-finite W1 combination

\[
K_I^2+\Gamma_*^2W_*^2
\]

can be routed to an already typed branch by a **quantitative** Type-I/frequency/weak-L3 threshold theorem, without replacing finite largeness by escalation to infinity.

If no such theorem exists, this combination should remain an explicit hard quantitative frontier rather than being hidden under the old bounded-W1 label.

## 10. Final proof-chain certification remains open

Even if the active analytic branches close, global regularity still requires:

1. arbitrary-singularity entry certification;
2. historical branch completeness and remaining alignment/nonreuse checks;
3. full beginning-to-end independent audit.

## 11. Permanent firewalls

\[
\boxed{\text{bounded W1 constants}\neq\text{small W1 constants}},
\]

\[
\boxed{\text{internal W1 hypothesis redundancy}\neq\text{global ROOT-CERT closure}},
\]

\[
\boxed{\text{positive recurrent palinstrophy floor}\neq\text{finite-energy contradiction}},
\]

\[
\boxed{\text{quotienting symmetry}\neq\text{removing symmetry-channel damping cost}},
\]

\[
\boxed{\text{relative periodicity}\neq\text{relative-periodic nonexistence}},
\]

\[
\boxed{\text{root-class merger}\neq\text{analytic closure}}.
\]

---

\[
\boxed{\text{M19 ACTIVE TIP = M19-191.}}
\]
