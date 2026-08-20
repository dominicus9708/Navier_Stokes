# Coherence/Compatibility Covariance Gap — 2026-08-20

Overall status: **QUANTITATIVE CLASS-LEVEL GAP FOR THE FINAL P_V BRANCH — GLOBAL REGULARITY NOT PROVED.**

This note combines two results already established:

1. the exact global fixed-axis compatibility cap

\[
n_0^T\mathbb C n_0\le\frac23;
\]

2. near `7/9` covariance saturation forces the local compressive eigenaxis `n(x)` to bend only weakly when the compressive spectral gap is positive.

The result is an explicit positive covariance-defect lower bound on any precompact coherent-axis class.

---

## 1. Moving-axis weighted alignment

Let

\[
P=\int|\nabla S|^2dx.
\]

Let `n(x)` be the local simple compressive eigenaxis on the active positive-middle sector and define

\[
A_{mov}
=\frac1P\int
|\nabla S|^2
n(x)^T\overline C(x)n(x)dx.
\]

Define the derivative-weighted mean covariance defect

\[
\boxed{
\overline\varepsilon
=\frac79-A_{mov}.
}
\]

Near local covariance saturation means `epsbar << 1`.

---

## 2. Compatibility forces axis dispersion when alignment exceeds 2/3

For any fixed unit vector `n0`,

\[
\frac1P\int
|\nabla S|^2
n_0^T\overline Cn_0dx
\le\frac23
\]

by `PV_GLOBAL_COMPATIBILITY_COVARIANCE_CAP_2026-08-20.md`.

Since `Cbar` is positive semidefinite with trace one,

\[
|n^T\overline Cn-n_0^T\overline Cn_0|
\le2|n-n_0|.
\]

Set

\[
D(n_0)
=
\left(
\frac1P\int
|\nabla S|^2|n(x)-n_0|^2dx
\right)^{1/2}.
\]

Then

\[
A_{mov}
\le
\frac23+2D(n_0).
\]

Taking the best constant axis,

\[
D_*:=\inf_{|n_0|=1}D(n_0),
\]

we obtain

\[
\boxed{
D_*
\ge
\frac12
\left(
\frac19-\overline\varepsilon
\right)
}
\]

whenever `epsbar <= 1/9`.

Thus approaching the old `7/9` ceiling forces a definite departure from every constant axis.

---

## 3. Near saturation simultaneously suppresses eigenaxis bending

Let

\[
g(x)=s_2(x)-s_1(x)
\]

be the compressive spectral gap. The eigenvector derivative identity gives

\[
|\nabla n|^2
\le
\frac1{g(x)^2}
\sum_k
|P_{n^\perp}(\partial_kS)n|^2.
\]

From the exact range-covariance defect calculation,

\[
\sum_k
|P_{n^\perp}(\partial_kS)n|^2
\le
\frac92
\varepsilon(x)|\nabla S|^2.
\]

Hence on a class with

\[
g(x)\ge g_->0
\]

through the active region,

\[
\boxed{
\int|\nabla n|^2
\le
\frac9{2g_-^2}
\overline\varepsilon P.
}
\]

On a bounded precompact active class, Poincare/analytic control converts this bending estimate into closeness to a constant axis.

---

## 4. Define the class coherence constant

For an admissible precompact class `K`, define `C_coh,K` to be any finite constant for which

\[
\boxed{
D_*^2
\le
C_{coh,K}\overline\varepsilon
}
\]

holds on the active positive-middle sector.

Such a finite constant follows from the preceding eigenaxis-bending estimate together with the bounded-radius/analytic compactness assumptions already required on the non-H/T class. Schematically,

\[
C_{coh,K}
\lesssim
\frac{R_K^2}{g_-^2}
\times
(\text{weighted/unweighted Poincare conversion factor}).
\]

The exact numerical value should be audited separately for each normalized compact class.

---

## 5. Explicit covariance gap

Combining

\[
D_*
\ge
\frac12\left(\frac19-\overline\varepsilon\right)
\]

with

\[
D_*^2\le C_{coh,K}\overline\varepsilon
\]

gives

\[
\left(\frac19-\overline\varepsilon\right)^2
\le
4C_{coh,K}\overline\varepsilon.
\]

Solving the quadratic inequality yields the lower root

\[
\boxed{
\overline\varepsilon
\ge
\delta_{cov,K}
:=
\left(
\sqrt{C_{coh,K}+\frac19}
-
\sqrt{C_{coh,K}}
\right)^2.
}
\]

Thus every finite-coherence precompact class carries a strictly positive covariance tax.

Asymptotically,

\[
\delta_{cov,K}
\sim
\frac1{324C_{coh,K}}
\qquad(C_{coh,K}\to\infty),
\]

while

\[
\delta_{cov,K}\to\frac19
\qquad(C_{coh,K}\to0).
\]

---

## 6. Insert the gap into the exact H1 covariance tax

The exact pointwise density decomposition contains

\[
-3S:\overline C
=
\text{ceiling}
-3\left(\frac79-c_1\right)(s_2-s_1)
-3c_3(s_3-s_2).
\]

If the active class also has

\[
s_2-s_1\ge g_->0,
\]

then after derivative-energy weighting,

\[
\boxed{
N
\le
N_{ceiling}
-3g_-\delta_{cov,K}P
}
\]

before the additional strongest-extensional leakage tax is even used.

Thus strain compatibility produces an additive positive H1 loss proportional to `P`.

---

## 7. Strengthened Leray recurrence tax

The Leray H1 identity is

\[
\frac12P_s+rac34P+\nu H=N.
\]

If the covariance ceiling is used as the comparison production, recurrence now requires it to overcome

\[
\boxed{
\left(
\frac34
+3g_-\delta_{cov,K}
\right)P
+\nu H.
}
\]

Therefore the previous similarity tax `3P/4` is strengthened on a coherent positive-gap compact class to

\[
\boxed{
\frac34P
\quad\longrightarrow\quad
\left(
\frac34+3g_-\delta_{cov,K}
\right)P.
}
\]

The compatibility tax is additive and strictly positive whenever `C_coh,K < infinity` and `g_->0`.

---

## 8. New quantitative target

The remaining task is no longer to prove an unspecified `delta_K>0`. It is to bound the finite list of compact-class quantities entering

\[
C_{coh,K},
\qquad g_-,
\qquad \kappa_K=P/H,
\qquad \kappa_K^+=\sup P/H.
\]

Once `C_coh,K` is bounded, the covariance defect is explicit:

\[
\delta_{cov,K}
=
\left(
\sqrt{C_{coh,K}+1/9}
-
\sqrt{C_{coh,K}}
\right)^2.
\]

This can be inserted directly into the recurrent threshold ledger.

Status: **THE NEW `2/3` FOURIER COMPATIBILITY CAP AND THE OLD NEAR-SATURATION EIGENAXIS LOCKING FORM A CLOSED QUANTITATIVE LOOP. ANY PRECOMPACT CLASS WITH FINITE AXIS-COHERENCE CONSTANT HAS AN EXPLICIT POSITIVE COVARIANCE DEFECT AND AN ADDITIONAL LERAY H1 TAX.**