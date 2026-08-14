# Second-chaos trace telescoping barrier

Date: 2026-08-14

Status: **DERIVED FOR THE QUADRATIC-CORE DEGREE-TWO TRACE SOURCE ON THE BOUNDED-CONDITION, BOUNDED-ACCUMULATED-STRAIN AFFINE-GAUSSIAN BRANCH. A FIXED STRICT-MESOSCOPIC TRACE ACTION IS EXCLUDED FOR LARGE FIRST-HITTING LEVELS. HIGH-HERMITE CORRECTIONS AND THE PROJECTIVE `Ab` LANE REMAIN. GLOBAL REGULARITY NOT PROVED.**

## 1. Quadratic-core split

The quadratic-core Gaussian mean-vorticity source is

\[
J_{\rm core}=J_{\rm tr}+J_{Ab},
\]

where `J_tr` is a finite-dimensional trace functional of the centered degree-two vorticity source and `J_Ab=Ab` is the projective constant-shift contribution.

The key point is that degree-two states at adjacent matched blocks are the same physical state expressed in compatible co-affine Gaussian bases. Their internal boundary terms therefore telescope.

## 2. Moving degree-two equation and audited coefficient variation

Let `Y_2(t)` be the actual degree-two residual-vorticity coefficient vector in the co-affine Gaussian basis matched to the affine heat covariance. Pure affine kinematics plus viscosity preserves Hermite degree, so

\[
\boxed{
Y_2'+\mathcal A_2(t)Y_2=F_2,
}
\]

where `F_2` contains the genuine degree-two nonlinear forcing.

On a geometric block of Gaussian radius `R(t)`, covariance normalization contributes

\[
\|\mathcal A_{2,\rm cov}(t)\|\lesssim_KR(t)^{-2}.
\]

Affine strain can also change the finite-dimensional coefficient representation. After rigid rotations are factored out, this gives the audited bound

\[
\boxed{
\|\mathcal A_2(t)\|
\lesssim_K
R(t)^{-2}+|S(t)|.
}
\]

Let `ell_t` recover the quadratic-core trace source from `F_2`:

\[
\boxed{J_{\rm tr}(t)=\ell_tF_2(t).}
\]

The same covariance/affine decomposition gives

\[
\boxed{
\|\ell_t\|\lesssim_K1,
\qquad
\|\ell_t'\|
\lesssim_K
R(t)^{-2}+|S(t)|.
}
\]

The antisymmetric affine part acts by rigid tensor rotation and does not create a norm-growth term in these estimates.

## 3. Exact telescoping identity

Using `F_2=Y_2'+A_2Y_2`,

\[
\boxed{
\int_IJ_{\rm tr}(t)dt
=
[\ell_tY_2(t)]_{\partial I}
+
\int_I
(\ell_t\mathcal A_2(t)-\ell_t')Y_2(t)dt.
}
\]

Thus all internal degree-two survival boundary terms cancel exactly.

## 4. Boundary and accumulated-strain terms vanish with the pulse height

On the intermediate branch,

\[
B(t)\le m,
\qquad
m=W^{-1/3}\Lambda\to0,
\]

and `Y_2` is part of the residual-vorticity variance, so

\[
|Y_2(t)|\lesssim\sqrt m.
\]

Hence

\[
|[\ell_tY_2]_{\partial I}|
\lesssim_K\sqrt m\to0.
\]

The audited affine-strain contribution satisfies

\[
\int_I |S(t)|\,|Y_2(t)|dt
\le
\sqrt m\int_I|S(t)|dt.
\]

On the bounded accumulated-strain branch,

\[
\int_I|S(t)|dt\le K,
\]

therefore

\[
\boxed{
\int_I |S|\,|Y_2|dt
\lesssim_K\sqrt m\to0.
}
\]

Thus neither moving-basis strain nor endpoint survival can carry a fixed positive trace action as `m -> 0`.

If `J_tr` carries a fixed signed action `rho>0`, then for sufficiently large `W`,

\[
\boxed{
\rho
\lesssim_K
\int_I R(t)^{-2}|Y_2(t)|dt.
}
\]

This is the scale term that must pay the remaining action.

## 5. Geometric-block lower bound

Partition the strict mesoscopic interval into geometric matched blocks `I_j` with

\[
|I_j|\asymp_KR_j^2,
\qquad
N_W\lesssim_K\log W.
\]

Define

\[
b_j:=\int_{I_j}R_j^{-2}|Y_2(t)|dt.
\]

Then

\[
\sum_jb_j\gtrsim_{K,\rho}1.
\]

Cauchy--Schwarz gives

\[
\boxed{
\int_{I_j}|Y_2(t)|^2dt
\gtrsim_K
R_j^2b_j^2.
}
\]

## 6. Physical dissipation price

Since

\[
B(t)\gtrsim|Y_2(t)|^2
\]

and a bounded-condition Gaussian of radius `R_j` satisfies

\[
\|\nabla U(t)\|_2^2
\gtrsim_KR_j^3B(t),
\]

we obtain

\[
D_{\rm phys}^{\rm tr}
\gtrsim_K
W^{-1/2}\sum_jR_j^5b_j^2.
\]

If

\[
R_j\ge R_*=W^{1/10+\varepsilon},
\]

then

\[
D_{\rm phys}^{\rm tr}
\gtrsim_K
W^{-1/2}R_*^5\sum_jb_j^2.
\]

Using `sum b_j >= c` and `N_W <= C log W`,

\[
\sum_jb_j^2\gtrsim\frac1{\log W}.
\]

Therefore

\[
\boxed{
D_{\rm phys}^{\rm tr}
\gtrsim_{K,\rho}
\frac{W^{5\varepsilon}}{\log W}
\to\infty.
}
\]

A fixed positive quadratic-core trace action is therefore impossible on the strict mesoscopic band for sufficiently large first-hitting level.

## 7. Revised quadratic-core routing

On the strict mesoscopic band:

1. a fixed `J_tr` action is excluded by telescoping plus physical dissipation;
2. the moving affine-strain contribution to the trace functional is `O_K(sqrt(m))` and cannot replace it;
3. the remaining low-Hermite quadratic-core source is the projective `J_Ab` lane, whose surviving infinite cascade requires

\[
\Lambda^{3/5}\Theta\to\infty;
\]

4. failure of quadratic-core dominance is charged to higher Hermite curvature/chaos.

## 8. Scope boundary

This result concerns the quadratic-core degree-two trace identity. Arbitrary high-Hermite nonlinear interactions are not asserted to reduce to this trace and remain in the high-Hermite nonlinear-cascade ledger.

Likewise the full transverse stretching source

\[
J_\perp=\int\gamma\,\delta S\,\beta
\]

is broader than `J_Ab`; only the quadratic-core projective constant-shift sublane has the stronger `Theta B` bound.

Status: **AUDITED TRACE TELESCOPING BARRIER HOLDS AFTER ROUTING MOVING-BASIS AFFINE STRAIN INTO THE BOUNDED ACCUMULATED-STRAIN LEDGER / STRICT-MESOSCOPIC QUADRATIC-CORE TRACE LANE EXCLUDED / REMAINING LOW-HERMITE CORE ESCAPE = PROJECTIVE `Ab` / GLOBAL REGULARITY NOT PROVED.**
