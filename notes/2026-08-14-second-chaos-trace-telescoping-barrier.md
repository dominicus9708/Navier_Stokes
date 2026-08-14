# Second-chaos trace telescoping barrier

Date: 2026-08-14

Status: **DERIVED FOR THE QUADRATIC-CORE DEGREE-TWO TRACE SOURCE ON THE BOUNDED-CONDITION AFFINE-GAUSSIAN HEAT STRUCTURE. A FIXED MESOSCOPIC TRACE ACTION IS EXCLUDED FOR LARGE FIRST-HITTING LEVELS. HIGH-HERMITE CORRECTIONS AND THE PROJECTIVE `Ab` LANE REMAIN. GLOBAL REGULARITY NOT PROVED.**

## 1. Why the earlier survival/erasure split can be strengthened

The quadratic-core identity writes the Gaussian mean-vorticity source as

\[
J_{\rm core}
=J_{\rm tr}+J_{Ab},
\]

where

\[
J_{\rm tr}=E_\gamma P
\]

is a fixed finite-dimensional trace functional of the degree-two centered vorticity source and

\[
J_{Ab}=Ab
\]

is the projective constant-shift term.

The previous heat-erasure note treated each matched block separately. But degree-two states at adjacent block boundaries are the same physical state written in compatible moving Gaussian bases. Therefore the surviving boundary contributions telescope when the full mesoscopic interval is considered at once.

## 2. Moving degree-two coefficient equation

Let `Y_2(t)` denote the actual degree-two residual-vorticity coefficient vector in the Gaussian basis matched to the bounded-affine heat covariance.

Pure affine+heat evolution preserves Hermite degree. Hence, after putting all genuinely nonlinear degree-two forcing into `F_2`, we may write

\[
\boxed{
Y_2'+\mathcal A_2(t)Y_2=F_2.
}
\]

On a bounded-condition geometric block of radius `R(t)`,

\[
\|\mathcal A_2(t)\|
\lesssim_K R(t)^{-2}.
\]

Let `ell_t` be the bounded linear functional recovering the quadratic-core trace contribution from the centered degree-two source:

\[
\boxed{
J_{\rm tr}(t)=\ell_tF_2(t).
}
\]

Because the only time dependence of this finite-dimensional identification comes from the bounded-condition affine/Gaussian normalization,

\[
\|\ell_t\|
\lesssim_K1,
\qquad
\|\ell_t'\|
\lesssim_KR(t)^{-2}.
\]

These are the natural scale bounds for the moving covariance basis.

## 3. Exact telescoping identity

Using

\[
F_2=Y_2'+\mathcal A_2Y_2,
\]

we obtain

\[
\begin{aligned}
\int_IJ_{\rm tr}(t)dt
&=
\int_I\ell_tY_2'(t)dt
+
\int_I\ell_t\mathcal A_2(t)Y_2(t)dt\\
&=
\boxed{
[\ell_tY_2(t)]_{\partial I}
+
\int_I
(\ell_t\mathcal A_2(t)-\ell_t')Y_2(t)dt.
}
\end{aligned}
\]

Thus all internal degree-two survival terms cancel exactly. There is no need to decide block by block whether the second chaos survives or is erased.

## 4. Boundary terms vanish on the intermediate-pulse branch

Throughout the responsible branch,

\[
B(t)\le m,
\qquad
m=W^{-1/3}\Lambda,
\qquad
m\to0.
\]

The degree-two vorticity coefficient is part of the residual variance, so

\[
|Y_2(t)|
\lesssim\sqrt{B(t)}
\le\sqrt m.
\]

Therefore at the two boundaries of a mesoscopic subinterval,

\[
\boxed{
|[\ell_tY_2]_{\partial I}|
\lesssim_K\sqrt m
\to0.
}
\]

Suppose the quadratic-core trace lane carries a fixed positive signed endpoint action `rho>0` on this mesoscopic interval. For sufficiently large `W`, the boundary term is smaller than `rho/2`, so

\[
\rho
\lesssim_K
\int_I R(t)^{-2}|Y_2(t)|dt.
\]

## 5. Geometric block decomposition

Partition the strict mesoscopic interval into geometric matched blocks `I_j` with radii `R_j`, so

\[
|I_j|\asymp_KR_j^2
\]

and the number of blocks satisfies

\[
N_W\lesssim_K\log W.
\]

Define

\[
b_j
:=
\int_{I_j}R_j^{-2}|Y_2(t)|dt.
\]

The fixed trace action forces

\[
\sum_jb_j\gtrsim_{K,\rho}1.
\]

By Cauchy--Schwarz,

\[
\begin{aligned}
b_j^2
&\le
R_j^{-4}|I_j|
\int_{I_j}|Y_2(t)|^2dt\\
&\lesssim_K
R_j^{-2}
\int_{I_j}|Y_2(t)|^2dt.
\end{aligned}
\]

Hence

\[
\boxed{
\int_{I_j}|Y_2(t)|^2dt
\gtrsim_K
R_j^2b_j^2.
}
\]

## 6. Physical dissipation price

Since `Y_2` is part of the residual-vorticity variance,

\[
B(t)\gtrsim|Y_2(t)|^2.
\]

The Gaussian-volume inequality gives

\[
\|\nabla U(t)\|_2^2
\gtrsim_K
R_j^3B(t)
\]

on block `I_j`. Therefore

\[
\int_{I_j}\|\nabla U\|_2^2dt
\gtrsim_K
R_j^5b_j^2.
\]

Returning to physical variables,

\[
D_{\rm phys}^{\rm tr}
\gtrsim_K
W^{-1/2}\sum_jR_j^5b_j^2.
\]

If the entire responsible trace action lies in the strict mesoscopic band

\[
R_j\ge R_*
=W^{1/10+\varepsilon},
\]

then

\[
D_{\rm phys}^{\rm tr}
\gtrsim_K
W^{-1/2}R_*^5
\sum_jb_j^2.
\]

Because

\[
\sum_jb_j\gtrsim1,
\qquad
N_W\lesssim\log W,
\]

Cauchy gives

\[
\sum_jb_j^2
\gtrsim
\frac1{\log W}.
\]

Thus

\[
\boxed{
D_{\rm phys}^{\rm tr}
\gtrsim_{K,\rho}
\frac{W^{5\varepsilon}}{\log W}.
}
\]

The right-hand side diverges as `W -> infinity`.

Hence a fixed positive quadratic-core trace action cannot be carried by the strict mesoscopic band at sufficiently large first-hitting level.

## 7. Revised quadratic-core routing

The quadratic-core mean source obeys

\[
J_{\rm core}
=J_{\rm tr}+J_{Ab}.
\]

On the strict mesoscopic band:

1. `J_tr` carrying fixed endpoint action is excluded by the telescoping/dissipation barrier;
2. `J_Ab` is the projective constant-shift lane and, if it carries fixed action on an infinite cascade, it must satisfy

\[
\Lambda^{3/5}\Theta\to\infty
\]

(up to dyadic localization of `Theta`);
3. failure of the quadratic-core approximation is charged to higher Hermite curvature/chaos.

Therefore the low-Hermite quadratic-core source has no remaining non-projective mesoscopic fixed-action escape.

## 8. Scope boundary

This theorem concerns the **quadratic-core degree-two trace identity**. It does not assert that the full nonlinear mean-vorticity source, including arbitrary high-Hermite interactions, is a degree-two trace.

Those higher interactions remain in the Hermite-curvature / gap-two / nonlinear-cascade ledger.

Likewise, the full transverse stretching projective term

\[
J_\perp
=\int\gamma\,\delta S\,\beta
\]

is not identical to `J_Ab`; only the quadratic-core projective constant-shift sublane has the stronger `Theta B` estimate.

Status: **STRICT-MESOSCOPIC QUADRATIC-CORE SECOND-CHAOS TRACE LANE EXCLUDED BY GLOBAL TELESCOPING PLUS PHYSICAL DISSIPATION / REMAINING LOW-HERMITE CORE ESCAPE = PROJECTIVE `Ab`; OTHER ESCAPE = HIGH-HERMITE STRUCTURE / GLOBAL REGULARITY NOT PROVED.**
