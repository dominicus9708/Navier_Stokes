# Exact strain-gradient covariance / Fourier-angle bridge

Date: 2026-08-19

Status: **DERIVED EXACT PROJECTIVE IDENTITY + ADVECTION DEPLETION GATE / GLOBAL REGULARITY NOT PROVED**.

This note continues the reduced advection-saturated `H` branch.

---

## 1. Global strain-gradient covariance

For each strain component define

\[
g^{ab}(x)=\nabla S_{ab}(x).
\]

Let

\[
P_S=\int_{\mathbb R^3}|\nabla S|^2dx
=\sum_{a,b}\int|g^{ab}|^2dx,
\]

and

\[
\mathsf G_S
=\sum_{a,b}\int g^{ab}\otimes g^{ab}\,dx.
\]

Normalize by

\[
\boxed{
\mathsf C_{\nabla S}
=\frac{\mathsf G_S}{P_S}.
}
\]

Then `C_{nabla S}` is positive semidefinite with trace one.

Define the projective dispersion

\[
\boxed{
\mathcal J_{\nabla S}
=1-\operatorname{tr}(\mathsf C_{\nabla S}^2).
}
\]

In three dimensions,

\[
0\le \mathcal J_{\nabla S}\le\frac23.
\]

---

## 2. Exact physical-space pairwise identity

Using

\[
|a\times b|^2=|a|^2|b|^2-(a\cdot b)^2,
\]

one obtains exactly

\[
\boxed{
\mathcal J_{\nabla S}
=
\frac{
\sum_{a,b,c,d}
\iint
|\nabla S_{ab}(x)\times\nabla S_{cd}(y)|^2\,dxdy
}{
P_S^2
}.
}
\]

Thus `J_{nabla S}` is the pairwise projective angular dispersion of all strain-gradient vectors, with no preferred axis chosen in advance.

---

## 3. The same matrix in Fourier space

By Plancherel,

\[
\mathsf G_S
=\int_{\mathbb R^3}
 k\otimes k\,|\widehat S(k)|_F^2\,dk,
\]

and

\[
P_S
=\int|k|^2|\widehat S(k)|_F^2\,dk.
\]

Define the probability measure

\[
\boxed{
d\mu_S(k)
=
\frac{|k|^2|\widehat S(k)|_F^2}{P_S}\,dk.
}
\]

Then

\[
\boxed{
\mathsf C_{\nabla S}
=\int \widehat k\otimes\widehat k\,d\mu_S(k),
\qquad
\widehat k=k/|k|.
}
\]

Consequently

\[
\boxed{
\mathcal J_{\nabla S}
=
\iint
\left[1-(\widehat k\cdot\widehat q)^2\right]
\,d\mu_S(k)d\mu_S(q).
}
\]

Equivalently,

\[
\boxed{
\mathcal J_{\nabla S}
=
\iint
\sin^2\theta_{kq}
\,d\mu_S(k)d\mu_S(q).
}
\]

Therefore the global physical-space strain-gradient covariance and the Fourier angular dispersion are not merely comparable: they are the same projective state written in two representations.

---

## 4. Principal spectral-axis consequence

Let the eigenvalues of `C_{nabla S}` be

\[
\mu_1\ge\mu_2\ge\mu_3,
\qquad
\sum_i\mu_i=1,
\]

and define

\[
\Pi_{\nabla S}=1-\mu_1.
\]

The same trace-one matrix algebra as for the vorticity projective covariance gives

\[
\boxed{
\frac12\mathcal J_{\nabla S}
\le
\Pi_{\nabla S}
\le
\frac32\mathcal J_{\nabla S}.
}
\]

Hence small `J_{nabla S}` means that most strain-gradient Fourier energy is projectively concentrated near a single axis `+-n`.

Since the advection Fourier symbol contains an angular factor because `p dot uhat(p)=0`, exactly collinear derivative-energy configurations are kinematically depleted. A complete global null-form estimate still requires control of low-frequency sweeping and the third triad factor; this note does not claim such a theorem.

---

## 5. Local covariance and exact anisotropy action

Pointwise where

\[
p(x)=|\nabla S(x)|^2>0,
\]

define

\[
\mathsf C(x)
=
\frac{
\sum_{a,b}\nabla S_{ab}(x)\otimes\nabla S_{ab}(x)
}{p(x)}.
\]

Then `C(x)` is positive semidefinite with trace one and

\[
\mathsf C_{\nabla S}
=
\frac1{P_S}\int p(x)\mathsf C(x)dx.
\]

Define the weighted covariance variance

\[
\boxed{
\mathcal V_C
=
\frac1{P_S}
\int p(x)
|\mathsf C(x)-\mathsf C_{\nabla S}|_F^2dx.
}
\]

The variance decomposition is exact:

\[
\boxed{
\frac1{P_S}
\int p(x)
\left|\mathsf C(x)-\frac13I\right|_F^2dx
=
\mathcal V_C
+\frac23-\mathcal J_{\nabla S}.
}
\]

Define the total advection-anisotropy action

\[
\boxed{
\mathfrak A_{\nabla S}
=
\mathcal V_C
+\frac23-\mathcal J_{\nabla S}.
}
\]

Since every trace-one positive semidefinite `3 x 3` matrix satisfies

\[
0\le|C-I/3|_F^2\le2/3,
\]

one has

\[
\boxed{
0\le\mathfrak A_{\nabla S}\le\frac23.
}
\]

---

## 6. Exact advection H1 identity with anisotropy depletion

The already-derived transport identity is

\[
\langle(u\cdot\nabla)S,-\Delta S\rangle
=
\sum_{a,b}\int
(\nabla S_{ab})^TS(\nabla S_{ab})dx.
\]

Using `tr S=0`, this becomes

\[
\boxed{
I_{\rm adv}
=
\int p(x)
S(x):\left(\mathsf C(x)-\frac13I\right)dx.
}
\]

Weighted Cauchy--Schwarz therefore gives

\[
\boxed{
|I_{\rm adv}|
\le
\left(\int |S|^2|\nabla S|^2dx\right)^{1/2}
P_S^{1/2}
\mathfrak A_{\nabla S}^{1/2}.
}
\]

Thus advection `H1` growth is depleted whenever the strain-gradient covariance is locally close to isotropic on average.

In particular, if

\[
\mathcal V_C\to0,
\qquad
\mathcal J_{\nabla S}\to\frac23,
\]

then

\[
I_{\rm adv}\to0
\]

relative to the same non-angular envelope.

---

## 7. Scale-critical derivative bound

Using Sobolev and interpolation,

\[
\|S\|_6\lesssim\|\nabla S\|_2,
\]

and

\[
\|\nabla S\|_{12/5}
\lesssim
\|\nabla S\|_2^{3/4}
\|\nabla S\|_6^{1/4}
\lesssim
P_S^{3/8}\|\Delta S\|_2^{1/4}.
\]

Hence

\[
\int |S|^2|\nabla S|^2
\lesssim
P_S^{3/2}\|\Delta S\|_2.
\]

Therefore

\[
\boxed{
|I_{\rm adv}|
\lesssim
P_S^{5/4}
\|\Delta S\|_2^{1/2}
\mathfrak A_{\nabla S}^{1/2}.
}
\]

This estimate is Navier--Stokes scale consistent.

If an advection-driven `H1` episode satisfies

\[
|I_{\rm adv}|
\ge c\nu\|\Delta S\|_2^2
\]

for fixed `c>0`, then

\[
\boxed{
\|\Delta S\|_2
\lesssim_{c}
\nu^{-2/3}
P_S^{5/6}
\mathfrak A_{\nabla S}^{1/3}.
}
\]

Equivalently,

\[
\boxed{
\mathfrak A_{\nabla S}
\gtrsim_c
\nu^2
\frac{\|\Delta S\|_2^3}{P_S^{5/2}}.
}
\]

The ratio

\[
\boxed{
\mathfrak K_H
=
\nu^2
\frac{\|\Delta S\|_2^3}{P_S^{5/2}}
}
\]

is scale invariant. Therefore dangerous advection-derivative saturation requires a quantitatively non-small projective anisotropy action.

---

## 8. Remaining split inside advection H

Since

\[
\mathfrak A_{\nabla S}
=
\underbrace{\mathcal V_C}_{\text{spatial covariance segregation}}
+
\underbrace{\left(\frac23-\mathcal J_{\nabla S}\right)}_{\text{global spectral anisotropy}},
\]

a dangerous advection-saturated episode must activate at least one of:

1. **spectral-axis concentration**: `J_{nabla S}` stays away from `2/3`;
2. **spatial covariance segregation**: `V_C` is non-small;
3. lower/higher derivative ratios leave the advection-saturation regime.

The first branch is in tension with the exact Fourier triad angular factor because projectively collinear modes suppress advection. The second branch requires spatial changes of the gradient covariance and is naturally coupled to higher derivatives or multicore/material-turnover geometry.

A complete nonrepeatability theorem still requires a quantitative treatment of these two branches.

Status: **EXACT PHYSICAL/FOURIER PROJECTIVE BRIDGE + SCALE-CRITICAL ADVECTION ANISOTROPY GATE; FINAL SATURATION-RIGIDITY STEP OPEN**.
