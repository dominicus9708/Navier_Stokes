# Late Frontier — 2026-08-19

Overall status: **ACTIVE DSD-ASSISTED 3D NAVIER--STOKES PROOF ATTEMPT — GLOBAL REGULARITY NOT PROVED.**

This file continues `FRONTIER_2026-08-19.md` after the exact strain-gradient covariance/Fourier bridge, projective angular uncertainty, covariance-segregation gate, palinstrophy covariance decomposition, and divergence-free vortex-line tightness analysis.

---

## 1. Exact strain-gradient projective state

Define

\[
P_S=\|\nabla S\|_2^2,
\]

\[
\mathsf C_{\nabla S}
=
\frac{
\sum_{a,b}\int\nabla S_{ab}\otimes\nabla S_{ab}dx
}{P_S},
\]

and

\[
\mathcal J_{\nabla S}
=1-\operatorname{tr}(\mathsf C_{\nabla S}^2).
\]

Exactly,

\[
\boxed{
\mathcal J_{\nabla S}
=
\frac{
\sum_{a,b,c,d}\iint
|\nabla S_{ab}(x)\times\nabla S_{cd}(y)|^2dxdy
}{P_S^2}
}
\]

and, in Fourier space,

\[
\boxed{
\mathcal J_{\nabla S}
=
\iint\sin^2\theta_{kq}\,d\mu_S(k)d\mu_S(q),
}
\]

where

\[
d\mu_S(k)
=\frac{|k|^2|\widehat S(k)|_F^2}{P_S}dk.
\]

Thus the physical gradient-direction dispersion and Fourier angular dispersion are the same normalized projective state.

---

## 2. Advection saturation requires projective anisotropy

For the local gradient covariance `C(x)`, define

\[
\mathfrak A_{\nabla S}
=
\frac1{P_S}
\int|\nabla S|^2
\left|C(x)-\frac13I\right|_F^2dx.
\]

Then

\[
\boxed{
\mathfrak A_{\nabla S}
=
\mathcal V_C
+\frac23-\mathcal J_{\nabla S},
}
\]

where `V_C` is the weighted spatial variance of the local covariance field.

The exact advection `H1` contraction satisfies

\[
\boxed{
|I_{\rm adv}|
\lesssim
P_S^{5/4}
\|\Delta S\|_2^{1/2}
\mathfrak A_{\nabla S}^{1/2}.
}
\]

Hence an advection episode comparable to viscous `H1` dissipation requires

\[
\boxed{
\mathfrak A_{\nabla S}
\gtrsim
\nu^2
\frac{\|\Delta S\|_2^3}{P_S^{5/2}}.
}
\]

So dangerous derivative growth requires not merely large derivatives but a scale-critical amount of directional anisotropy.

---

## 3. The spectral-axis endpoint J -> 0 routes to H or T

Let `n` be the principal axis of `C_{nabla S}` and

\[
\Pi_{\nabla S}=1-\mu_1.
\]

For the transverse rms strain radius `R_perp`, the two-dimensional Heisenberg inequality gives

\[
\boxed{
R_\perp^2
\ge
\frac{\|S\|_2^2}{P_S\Pi_{\nabla S}}
\ge
\frac{2\|S\|_2^2}{3P_S\mathcal J_{\nabla S}}.
}
\]

Therefore

\[
\boxed{
\mathcal J_{\nabla S}\to0
\Longrightarrow
R_\perp^2\frac{P_S}{\|S\|_2^2}\to\infty.
}
\]

Thus extreme Fourier collimation forces either derivative concentration `H` or transverse spatial non-tightness `T`.

---

## 4. The isotropic endpoint J -> 2/3 routes to H or weak-connectivity T

Pointwise, the local covariance obeys

\[
\boxed{
|\nabla S|^2|\nabla C|_F^2
\le
16|\nabla^2S|^2.
}
\]

For the gradient-energy probability measure

\[
d\mu_C=|\nabla S|^2dx/P_S,
\]

if `L_C^2` denotes its weighted Poincare constant, then

\[
\boxed{
\mathcal V_C
\le
16L_C^2
\frac{\|\Delta S\|_2^2}{P_S}.
}
\]

Hence if

\[
\mathcal J_{\nabla S}\to2/3
\]

while advection remains saturated, the required covariance segregation forces either:

1. a higher-derivative `H` cost;
2. a large weighted Poincare length, i.e. weakly connected / multicore / spatially extended `T` geometry.

Thus both angular endpoints are removed from the genuinely new tight/nonconcentrating survivor.

---

## 5. The surviving angular state lies in the interior

A genuinely new tight advection-saturated survivor must therefore maintain

\[
\boxed{
\mathcal J_{\nabla S}
\in[j_-,j_+]\Subset(0,2/3)
}
\]

along the dangerous first-hitting subsequence, unless it already pays through `H` or `T`.

This is a substantial reduction from arbitrary strain-gradient anisotropy.

---

## 6. Exact identity with palinstrophy covariance

Axis-resolved Plancherel gives

\[
\boxed{
\int\partial_jS:\partial_kS
=
\frac12\int\partial_j\omega\cdot\partial_k\omega.
}
\]

Hence

\[
\boxed{
\mathsf C_{\nabla S}
=
\mathsf C_{\nabla\omega},
\qquad
\mathcal J_{\nabla S}
=
\mathcal J_{\nabla\omega}.
}
\]

Writing

\[
\omega=\rho\xi
\]

gives the exact covariance split

\[
\boxed{
\mathsf G_\omega
=
\nabla\rho\otimes\nabla\rho
+
\rho^2\sum_i\nabla\xi_i\otimes\nabla\xi_i.
}
\]

Let

\[
P_\rho=\|\nabla\rho\|_2^2,
\qquad
P_\xi=\int\rho^2|\nabla\xi|^2,
\qquad
\theta=P_\rho/(P_\rho+P_\xi).
\]

Then

\[
\boxed{
C_{\nabla S}
=
\theta C_\rho+(1-\theta)C_\xi
}
\]

and

\[
\boxed{
J_{\nabla S}
=
\theta J_\rho
+(1-\theta)J_\xi
+\theta(1-\theta)\|C_\rho-C_\xi\|_F^2.
}
\]

Thus the interior angular state is supplied by magnitude-interface geometry, direction variation, or covariance mismatch.

---

## 7. Divergence-free vortex-line tightness gate

Since

\[
\nabla\cdot(\rho\xi)=0,
\]

one has

\[
\boxed{
\xi\cdot\nabla\rho
=-\rho\nabla\cdot\xi.
}
\]

For any constant axis `n` and longitudinal rms radius `R_n`, define

\[
Q_n
=
\int|P_{\xi^\perp}n|^2|\nabla\rho|^2dx.
\]

A one-dimensional Heisenberg estimate gives

\[
\boxed{
3P_\xi+Q_n
\ge
\frac{\|\omega\|_2^2}{8R_n^2}.
}
\]

Therefore a nontrivial vortex core cannot be simultaneously:

- longitudinally tight;
- straight/projectively aligned with a fixed axis;
- small in magnitude-weighted direction variation;
- small in cross-axis magnitude-gradient leakage.

Exact constant direction forces longitudinal non-tightness.

---

## 8. Current reduced survivor

The bounded-affine fresh-pulse route is now reduced as follows.

### M* — non-negligibly non-saturated critical middle strain

The positive-middle-strain channel remains above the critical `L^(3/2)` threshold, with the exact cubic saturation defect preventing free approach to determinant equality.

### AH* — interior angular advection saturation

A genuinely new derivative survivor must keep

\[
J_{\nabla S}\in[j_-,j_+]\Subset(0,2/3)
\]

and sustain one or more of:

1. non-negligible magnitude-weighted direction variation `P_xi`;
2. multiaxial vorticity-magnitude interface geometry `J_rho`;
3. magnitude/direction covariance-axis mismatch;
4. repeated spatial covariance reorganization.

### T* — bounded-radius multicore/material turnover

Far-shell escape is already derivative/enstrophy expensive. The remaining transport branch is bounded-normalized-radius turnover, weak connectivity, repeated core replacement, or multicore exchange.

Straight coherent finite-length vortex cores are excluded by the divergence-free longitudinal gate, so `T*` must itself be geometrically reorganizing.

---

## 9. Principal next theorem target

The active endgame is no longer arbitrary `M/H/T` saturation.

It is the following much narrower packing problem:

\[
\boxed{
\begin{gathered}
\text{Can an infinite first-hitting sequence repeatedly regenerate a bounded-radius}\
\text{vorticity core whose strain-gradient/palinstrophy covariance remains in an}\
\text{interior projective angular window, while magnitude interfaces and vorticity}\
\text{directions co-reorganize so that all associated derivative, cubic-middle-strain,}\
\text{and multicore/material-turnover costs remain globally repeatable?}
\end{gathered}
}
\]

A final proof still requires a nonrepeatability/packing theorem for this co-reorganizing interior-angular state.

Status: **BOTH PROJECTIVE ANGULAR ENDPOINTS REDUCED; STRAIGHT COHERENT TIGHT CORE EXCLUDED; ACTIVE ENDGAME = INTERIOR PALINSTROPHY-ANGLE / MAGNITUDE-DIRECTION CO-REORGANIZATION PACKING — GLOBAL REGULARITY NOT PROVED.**
