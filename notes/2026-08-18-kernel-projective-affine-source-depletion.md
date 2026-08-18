# Kernel projective covariance: affine-source depletion plus angular damping

Date: 2026-08-18

Status: **EXACT AFFINE/RESIDUAL SOURCE DECOMPOSITION + CONDITIONAL THICK-CELL PROJECTIVE POINCARE CLOSURE. PROJECTIVE DISPERSION BOTH REDUCES AFFINE STRETCHING CAPACITY AND INCREASES ANGULAR VISCOUS LOSS. GLOBAL REGULARITY NOT PROVED.**

## 1. Kernel-weighted vorticity covariance

For the exact terminal adjoint kernel `K`, define

\[
E_K=\int K|\Omega|^2,
\]

\[
M_K=\int K\,\Omega\otimes\Omega,
\qquad
C_K=M_K/E_K
\]

when `E_K>0`.

Then `C_K` is positive semidefinite and

\[
\operatorname{tr}C_K=1.
\]

Define the projective dispersion

\[
\boxed{
J_K=1-\operatorname{tr}(C_K^2),
\qquad
0\le J_K\le\frac23.
}
\]

Rank-one directional coherence has `J_K=0`; projective isotropy has `C_K=I/3` and `J_K=2/3`.

## 2. Exact affine/residual strain split

Let

\[
\bar S_K=\int KS,
\qquad
\delta S=S-\bar S_K,
\]

and

\[
V_{S,K}=\int K|\delta S|^2.
\]

The kernel stretching source is

\[
Q_K=\int K\Omega\cdot S\Omega.
\]

Exactly,

\[
Q_K
=E_K\operatorname{tr}(\bar S_KC_K)
+\int K\Omega\cdot\delta S\,\Omega.
\]

Because incompressibility gives `tr S=0`, also

\[
\operatorname{tr}\bar S_K=0,
\]

and therefore

\[
\operatorname{tr}(\bar S_KC_K)
=
\operatorname{tr}\left[
\bar S_K\left(C_K-\frac13I\right)
\right].
\]

Moreover

\[
\left\|C_K-\frac13I\right\|_F^2
=\operatorname{tr}(C_K^2)-\frac13
=\frac23-J_K.
\]

Hence

\[
\boxed{
|Q_{K,\mathrm{aff}}|
\le
E_K|\bar S_K|_F
\sqrt{\frac23-J_K}.
}
\]

This is an exact finite-dimensional source-depletion factor.

## 3. Residual strain source under first hitting

On the normalized first-hitting past,

\[
|\Omega|\le1.
\]

Thus

\[
\begin{aligned}
|Q_{K,\mathrm{res}}|
&\le
\left(\int K|\delta S|^2\right)^{1/2}
\left(\int K|\Omega|^4\right)^{1/2}\\
&\le
\sqrt{V_{S,K}}\,\sqrt{E_K}.
\end{aligned}
\]

Therefore

\[
\boxed{
Q_K
\le
E_K|\bar S_K|_F
\sqrt{\frac23-J_K}
+\sqrt{E_KV_{S,K}}.
}
\]

Consequences:

- if `J_K -> 2/3`, affine production vanishes;
- a projectively isotropic cell can grow only through non-affine strain variance;
- if residual strain is small, a source-active cell must retain a quantitatively anisotropic vorticity covariance.

## 4. Combine with exact angular damping

The exact adjoint-kernel magnitude identity is

\[
\frac12E_K'
+\nu P_{\rm mag,K}
+\nu P_{\rm ang,K}
=Q_K.
\]

Dropping only the nonnegative magnitude-gradient dissipation gives

\[
\boxed{
\frac12E_K'
+\nu P_{\rm ang,K}
\le
E_K|\bar S_K|_F
\sqrt{\frac23-J_K}
+\sqrt{E_KV_{S,K}}.
}
\]

Thus projective disorder hurts twice:

1. it decreases the affine source through `sqrt(2/3-J_K)`;
2. spatial realization of that disorder contributes angular palinstrophy and therefore direct viscous damping.

## 5. Thick-cell projective Poincare bridge

On a buffered intense cell where

\[
|\Omega|\ge a>0
\]

on a fixed positive fraction of the kernel mass and the kernel has a bounded-condition Poincare constant at radius `r`, the projective map

\[
A(x)=\xi(x)\otimes\xi(x)
\]

satisfies

\[
|\nabla A|^2=2|\nabla\xi|^2.
\]

The projective covariance variance is

\[
\operatorname{Var}(A)
=1-\operatorname{tr}(C_K^2)
=J_K
\]

up to the fixed thick-core amplitude/comparability constants.  Hence the weighted Poincare inequality gives schematically

\[
\boxed{
P_{\rm ang,K}
\gtrsim
\frac{E_K}{r^2}J_K.
}
\]

This step is conditional on the thick-cell/kernel-comparability hypotheses; failure of thickness or Poincare comparability remains an occupancy/kernel-deformation branch rather than being discarded.

At the natural unit-cell scale `r~1`, this becomes

\[
P_{\rm ang,K}\gtrsim E_KJ_K.
\]

Therefore

\[
\boxed{
\frac12E_K'
+c\nu E_KJ_K
\lesssim
E_K|\bar S_K|_F
\sqrt{\frac23-J_K}
+\sqrt{E_KV_{S,K}}.
}
\]

## 6. Monotone projective efficiency function

For fixed affine strain amplitude `A`, define

\[
\mathcal G_A(J)
=A\sqrt{\frac23-J}-c\nu J.
\]

Then

\[
\mathcal G_A'(J)
=-\frac{A}{2\sqrt{2/3-J}}-c\nu<0.
\]

Thus, among states with the same affine strain budget and small residual strain, the most efficient projective state for magnitude production is always the coherent endpoint

\[
\boxed{J=0.}
\]

Every fixed `J>=j_0>0` carries a strict coefficient deficit relative to the rank-one state:

\[
\boxed{
\delta(A,\nu,j_0)
=
A\left[
\sqrt{\frac23}
-\sqrt{\frac23-j_0}
\right]
+c\nu j_0
>0.
}
\]

This does not by itself prove viscosity dominates the source, but it shows that a scalar-minimal surviving unit cell is driven toward projective coherence unless it pays residual-strain or kernel/thickness escape costs.

## 7. Source-active anisotropy gate

Suppose on a normalized repopulation interval of length at most `T_0`,

\[
E_K(T)-E_K(t_0)\ge d_0>0,
\]

\[
|\bar S_K|\le M,
\]

and

\[
\int_{t_0}^{T}\sqrt{E_KV_{S,K}}\,dt\le\varepsilon<d_0/2.
\]

If

\[
\frac23-J_K(t)\le a
\]

throughout the interval, then after dropping angular damping,

\[
\frac{d_0}{2}
\le
MT_0\sqrt a+\varepsilon.
\]

Hence for sufficiently small `a` this is impossible.  Therefore there exists a source-active time at which

\[
\boxed{
\frac23-J_K
\ge
\left(
\frac{d_0/2-\varepsilon}{MT_0}
\right)^2.
}
\]

Equivalently,

\[
\operatorname{tr}(C_K^2)
\ge
\frac13+a_0
\]

for a fixed `a_0>0`.  Since

\[
\lambda_{\max}(C_K)
\ge
\operatorname{tr}(C_K^2),
\]

the cell carries a quantitatively preferred projective axis.

## 8. Updated unit-cell trichotomy

A newly source-active same-scale unit cell must therefore choose among

\[
\boxed{
\text{preferred projective axis / coherence}
}
\]

or

\[
\boxed{
\text{order-one residual strain variance}
}
\]

or

\[
\boxed{
\text{angular palinstrophy / kernel-thickness deformation}.
}
\]

The first branch should be compared across neighboring packets; the second is already the scale-mixing/non-affine branch; the third is directly viscously damped or returns to derivative/kernel deformation.

Status: **SAME-SCALE NONCOHERENT CELL CANNOT BE AN EFFICIENT PURE-AFFINE AMPLIFIER / NEXT TARGET = INTER-PACKET PROJECTIVE-AXIS ORGANIZATION VERSUS RESIDUAL HIGH-HIGH INTERACTION.**