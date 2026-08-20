# Compatibility/Covariance Endgame Frontier — 2026-08-20

Overall status: **ACTIVE 3D NAVIER--STOKES PROOF ATTEMPT — GLOBAL REGULARITY NOT PROVED.**

This frontier continues `FRONTIER_SOLENOIDAL_LERAY_ENDGAME_2026-08-20.md` after the full incompressible-strain compatibility constraint is inserted into the final `P_V` covariance geometry.

---

## 1. Old pointwise ceiling versus true compatible whole-profile ceiling

The pointwise trace-free calculation gave

\[
\lambda_{max}(\overline C(x))\le\frac79.
\]

For the derivative-energy-weighted integrated covariance of an actual incompressible strain field,

\[
\mathbb C
=\frac1P\int|\nabla S|^2\overline C(x)dx,
\]

Fourier compatibility gives the stronger exact bound

\[
\boxed{
\lambda_{max}(\mathbb C)\le\frac23.
}
\]

Every single compatible Fourier strain mode has combined covariance eigenvalues

\[
\boxed{
\left\{\frac23,\frac13,0\right\}.
}
\]

Thus a coherent whole profile cannot indefinitely approach the pointwise `7/9` ceiling.

---

## 2. Exact global covariance deficit

For every fixed unit axis `n`, define

\[
I_n
=\|\partial_nS\|_2^2
+2\sum_k\|(\partial_kS)n\|_2^2.
\]

Then

\[
\boxed{
2P-I_n
=
\frac12\|\Delta(u\cdot n)\|_2^2
+\|\nabla(\omega\cdot n)\|_2^2.
}
\]

Hence

\[
\boxed{
\frac23-n^T\mathbb Cn
=
\frac{\|\Delta(u\cdot n)\|_2^2}{6P}
+
\frac{\|\nabla(\omega\cdot n)\|_2^2}{3P}.
}
\]

Near `2/3` saturation therefore requires simultaneous depletion of axial velocity curvature and axial vorticity-gradient energy.

---

## 3. Static max-mid saturation is Fourier-incompatible

Let

\[
Q_n=\frac{I-3n\otimes n}{\sqrt6}.
\]

For every compatible Fourier strain subspace `V_k`,

\[
\boxed{
\|P_{V_k}Q_n\|
=\sqrt3|\sin\theta\cos\theta|
\le\frac{\sqrt3}{2},
}
\]

so

\[
\boxed{
\operatorname{dist}(Q_n,V_k)\ge\frac12.
}
\]

If `k parallel n`, which is the exact one-dimensional derivative direction required by static H1 saturation,

\[
\boxed{P_{V_k}Q_n=0.}
\]

Thus the exact static one-dimensional max-mid derivative geometry is orthogonal to the incompressible strain space in its limiting Fourier direction.

---

## 4. Max-mid versus non-normality spectral tradeoff

On

\[
(s_1,s_2,s_3)=(-2m,m-d,m+d),
\qquad x=d/m\in[0,1],
\]

the static H1 efficiency factor is

\[
\Theta_{st}(x)
=\frac12+
\frac1{2\sqrt{1+x^2/3}},
\]

while the non-normality range efficiency is

\[
\Theta_{NN}(x)
=\frac{3+x}{2\sqrt{3+x^2}}.
\]

They cross at

\[
\boxed{
x_*=\frac{3(\sqrt3-1)}4
\approx0.549038106
}
\]

with

\[
\boxed{
\Theta_*
=\frac{15+6\sqrt3}{26}
\approx0.9766271094.
}
\]

Therefore every positive-middle spectrum pays at least

\[
\boxed{
1-\Theta_*
\approx0.0233728906
}
\]

in at least one of the two algebraic saturation channels.

This is a spectral tradeoff, not yet by itself a global H1 constant reduction, because the two local density representations differ by divergence transfer.

---

## 5. Localized compatibility cap

Localize the **velocity** with an annular Bogovskii correction:

\[
u_R=\chi_Ru-b_R,
\qquad
\operatorname{div}u_R=0,
\]

and set

\[
S_R=\operatorname{sym}\nabla u_R.
\]

Then `S_R=S` on `B_R` and the global `2/3` cap applies to `S_R`.

Let

\[
P_R=\|\nabla S\|_{L^2(B_R)}^2
\]

and define corrected annular compatibility leakage

\[
\mathcal E_A(R)
=\frac{\|\nabla S_R\|_{L^2(A_R)}^2}{P_R}.
\]

Then

\[
\boxed{
\frac{I_{n,B_R}}{3P_R}
\le
\frac23+rac23\mathcal E_A(R).
}
\]

The annular error obeys

\[
\mathcal E_A
\lesssim
\frac{
[\|\nabla S\|_{A_R}
+R^{-1}\|\nabla u\|_{A_R}
+R^{-2}\|u\|_{A_R}]^2
}{P_R}.
\]

---

## 6. Exact `1/6` local branch split

The localized compatibility ceiling improves the old `7/9` ceiling precisely when

\[
\mathcal E_A<\frac16.
\]

Therefore

\[
\boxed{
\mathcal E_A\ge\frac16
\Rightarrow
\text{definite annular derivative/material leakage }(H/T),
}
\]

while

\[
\boxed{
\mathcal E_A<\frac16
\Rightarrow
\text{strict positive local compatibility gap}.
}
\]

---

## 7. Explicit local covariance gap

On a positive-gap active ball assume

\[
s_2-s_1\ge g_->0,
\qquad
|\nabla S|^2\le P_\infty.
\]

The eigenaxis-bending/Poincare estimate gives

\[
C_{coh}^{ball}
=\frac{36}{\pi^2}
\frac{R^2P_\infty}{g_-^2}.
\]

Define

\[
a_R
=\left[
\frac19-rac23\mathcal E_A
\right]_+.
\]

Then the derivative-weighted covariance defect satisfies

\[
\boxed{
\overline\varepsilon_R
\ge
\delta_{cov,R}
=
\left(
\sqrt{C_{coh}^{ball}+a_R}
-
\sqrt{C_{coh}^{ball}}
\right)^2.
}
\]

Hence

\[
\boxed{
N_R
\le
N_{ceiling,R}
-3g_-\delta_{cov,R}P_R.
}
\]

The strongest-extensional covariance leakage tax remains additional and nonnegative.

---

## 8. Quantitative non-T compact class

Fix a non-turnover annulus threshold

\[
0\le e_T<\frac16
\]

and suppose

\[
\mathcal E_A\le e_T.
\]

Define the compact-class shape parameter

\[
\boxed{
\chi_K
=\sup_K\frac{R^2P_\infty}{g_-^2}<\infty.
}
\]

Then uniformly on the non-T class,

\[
\boxed{
\delta_{cov,K}^{comp}
\ge
\left[
\sqrt{
\frac{36}{\pi^2}\chi_K
+
\frac19-rac23e_T
}
-
\sqrt{
\frac{36}{\pi^2}\chi_K
}
\right]^2
>0.
}
\]

Thus the former qualitative compactness statement `some delta_K > 0` has been reduced to an explicit function of two quantitative class parameters: `chi_K` and `e_T`.

---

## 9. Strengthened Leray recurrence ledger

The exact Leray H1 identity is

\[
\frac12P_s+rac34P+\nu H=N.
\]

On the positive-gap coherent active core, compatibility adds

\[
3g_-\delta_{cov,K}^{comp}P_R
\]

to the production cost.

Thus the recurrent survivor must pay simultaneously:

1. the similarity tax `3P/4`;
2. viscous hyperdissipation `nu H`;
3. the positive compatibility covariance tax;
4. strongest-extensional covariance leakage;
5. annular localization leakage unless `E_A` is small;
6. the max-mid/non-normality double-saturation tradeoff.

---

## 10. Current branch structure

A hypothetical recurrent non-H/T `P_V` survivor must now choose among:

### Branch C1 — annular compatibility leakage

\[
\mathcal E_A\ge1/6.
\]

This is routed to `H/T`.

### Branch C2 — positive-gap coherent core

\[
\mathcal E_A<1/6,
\qquad
g_->0.
\]

Then a strict explicit covariance tax `delta_cov,R` is mandatory.

### Branch C3 — loss of positive-middle compressive gap

If `g_-` degenerates, the profile leaves the coherent max-mid sector and must be analyzed through the middle-zero/non-normality spectral branch, where `Theta_st` loses efficiency and the double-saturation tradeoff applies.

Thus the old single `P_V` survivor has split again into a leakage branch, a quantitatively taxed coherent branch, and a middle-zero/non-normality branch.

---

## 11. Principal next target

The remaining quantitative target is to compare the explicitly taxed coherent-core ceiling with

\[
\nu+\frac34\kappa
\]

in the Leray threshold quotient, while separately routing the middle-zero branch through the non-normality geometry.

The key remaining normalized inputs are

\[
\chi_K,
\qquad
e_T,
\qquad
g_-,
\qquad
\kappa=P/H,
\qquad
B_K=\|S\|_\infty.
\]

Status: **FULL STRAIN COMPATIBILITY HAS LOWERED THE COHERENT COVARIANCE CEILING FROM THE POINTWISE `7/9` GEOMETRY TO A LOCALIZED `2/3 + ANNULUS ERROR` LAW. THE ERROR HAS A SHARP `1/6` BRANCH THRESHOLD, AND BELOW IT THE PRECOMPACT POSITIVE-GAP CORE PAYS AN EXPLICIT COMPATIBILITY TAX IN THE LERAY H1 LEDGER. GLOBAL REGULARITY REMAINS UNPROVED.**