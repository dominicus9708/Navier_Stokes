# Near-Saturation Rigidity of the H1 Covariance Cap — 2026-08-20

Overall status: **NEW RIGIDITY LEMMA FOR THE FINAL P_V BRANCH — GLOBAL REGULARITY NOT PROVED.**

This note quantifies what it means for the combined strain-gradient covariance to approach its maximal possible concentration on the compressive strain axis. It upgrades the universal `7/9` covariance cap into a rigidity statement: near saturation forces both spatial one-dimensionality and axisymmetric max-mid structure of every active derivative matrix.

---

## 1. Setup

Let

\[
G_k=\partial_kS,
\qquad
P=|\nabla S|^2=\sum_k|G_k|_F^2.
\]

Define

\[
(M_{sp})_{k\ell}=\langle G_k,G_\ell\rangle_F,
\qquad
M_{rg}=\sum_kG_k^2,
\]

and, on the set `P>0`,

\[
C_{sp}=M_{sp}/P,
\qquad
C_{rg}=M_{rg}/P,
\qquad
\overline C=(C_{sp}+2C_{rg})/3.
\]

All three covariance matrices are positive semidefinite and trace one. For every unit vector `n`, the trace-free range inequality gives

\[
n^TC_{rg}n\le\frac23,
\]

hence

\[
n^T\overline Cn\le\frac79.
\]

Define the combined saturation defect

\[
\boxed{
\varepsilon_n
=\frac79-n^T\overline Cn\ge0.
}
\]

---

## 2. The defect splits exactly into spatial and range defects

From the definition of `Cbar`,

\[
\boxed{
\varepsilon_n
=\frac13\left(1-n^TC_{sp}n\right)
+\frac23\left(\frac23-n^TC_{rg}n\right).
}
\]

Both terms are nonnegative. Therefore

\[
\boxed{
1-n^TC_{sp}n\le3\varepsilon_n,
}
\]

and

\[
\boxed{
\frac23-n^TC_{rg}n\le\frac32\varepsilon_n.
}

The first inequality says that the physical derivative index is almost entirely aligned with `n`.

Indeed, rotating coordinates so `n=e_1`,

\[
n^TM_{sp}n=|\partial_nS|^2,
\]

so

\[
\boxed{
\sum_{v\perp n}|\partial_vS|^2
=P-|\partial_nS|^2
\le3\varepsilon_nP.
}
\]

Thus near saturation forces near one-dimensionality in physical space.

---

## 3. Exact distance of a trace-free derivative matrix from the saturating subspace

Fix a unit vector `n`. Let

\[
\mathcal L_n
=\{a(I-\tfrac32P_{n^\perp})\}
=\{a\,\mathrm{diag}(1,-1/2,-1/2)\}
\]

in a frame with `n=e_1`. This is the one-dimensional axisymmetric trace-free subspace saturating the range inequality.

Write a symmetric trace-free matrix as

\[
G=
\begin{pmatrix}
a&x&y\\x&b&z\\y&z&-a-b
\end{pmatrix}.
\]

Define the range-cap defect

\[
\delta_n(G)=\frac23|G|_F^2-n^TG^2n.
\]

Direct calculation gives

\[
\boxed{
\delta_n(G)
=\frac13\left[(a+2b)^2+x^2+y^2+4z^2\right].
}
\]

The orthogonal projection of `G` onto `L_n` is `a diag(1,-1/2,-1/2)`, so

\[
\operatorname{dist}_F(G,\mathcal L_n)^2
=\frac12(a+2b)^2+2(x^2+y^2+z^2).
\]

Comparing coefficients yields

\[
\boxed{
\operatorname{dist}_F(G,\mathcal L_n)^2
\le6\delta_n(G).
}
\]

---

## 4. Near saturation controls all derivative matrices

Since

\[
\frac23-n^TC_{rg}n
=\frac1P\sum_k\delta_n(G_k),
\]

we obtain

\[
\sum_k\delta_n(G_k)
\le\frac32\varepsilon_nP.
\]

Using the distance estimate,

\[
\boxed{
\sum_k\operatorname{dist}_F(G_k,\mathcal L_n)^2
\le9\varepsilon_nP.
}
\]

Thus, if `Cbar` is within `epsilon` of the `7/9` cap on axis `n`, every active derivative matrix is collectively within `O(sqrt(epsilon))` of the same axisymmetric max-mid derivative line `L_n`.

Combining with the spatial estimate:

\[
\boxed{
\sum_{v\perp n}|\partial_vS|^2
+\frac13\sum_k\operatorname{dist}_F(\partial_kS,\mathcal L_n)^2
\le6\varepsilon_n|\nabla S|^2.
}
\]

(up to the displayed harmless numerical normalization).

This is the quantitative near-saturation rigidity statement.

---

## 5. Exact saturation

If

\[
\varepsilon_n=0,
\]

then exactly

\[
\partial_vS=0\qquad(v\perp n)
\]

and

\[
\partial_kS\in\mathcal L_n\qquad(k=1,2,3).
\]

Now take `n` to be the simple compressive eigenvector of `S` in a positive-middle-strain region. The spectral derivative formula gives

\[
\partial_kn
=\sum_{j=2,3}
\frac{e_j^T(\partial_kS)n}{s_1-s_j}e_j.
\]

But every `partial_k S in L_n` is diagonal in the frame `(n,e_2,e_3)`, hence

\[
e_j^T(\partial_kS)n=0.
\]

Therefore

\[
\boxed{\nabla n=0.}
\]

The compressive eigenaxis is fixed on every connected positive-middle active component.

With fixed `n`, exact spatial saturation also gives

\[
\boxed{
S(x)=S_0+\phi(n\cdot x)E_n,
\qquad
E_n=\mathrm{diag}(1,-1/2,-1/2)
}
\]

locally on the component.

Thus exact saturation is a one-dimensional fixed-axis strain profile.

---

## 6. Finite-energy consequence

A nonzero field depending only on the single coordinate `n dot x` is constant along two-dimensional transverse planes. Such a global field cannot belong to `L^2(R^3)` unless it vanishes (after eliminating any constant background, which is also not in `L^2`).

Hence a globally exact-saturating finite-energy positive-middle strain state cannot be a nontrivial whole-space survivor.

The remaining issue for the proof attempt is **quantitative stability**: a sequence may only approach saturation on weighted core regions rather than saturate globally. The estimates above show what such a sequence must look like: increasingly one-dimensional in physical derivative direction and increasingly axisymmetric in derivative range.

---

## 7. Routing of near saturation

Let `epsilon_bar` denote a weighted average of `epsilon_n` using `|grad S|^2` over the active core. If `epsilon_bar -> 0`, then the preceding estimates force:

1. transverse derivative energy `-> 0`;
2. derivative-matrix distance to the axisymmetric max-mid line `-> 0`;
3. on any region with a uniform compressive spectral gap, eigenaxis bending `-> 0`.

Therefore a tight bounded-radius core approaching saturation must either:

- become approximately one-dimensional and fixed-axis, which tends toward transverse non-tightness / aligned turnover geometry (`T`);
- create boundary/interface layers to remain spatially localized, which produces higher derivative cost (`H`);
- fail to approach saturation, leaving a definite covariance deficit that must be compensated by larger projective/derivative action in the H1 ledger.

This is not yet a complete quantitative no-saturation theorem, because turning approximate one-dimensionality into a sharp `H or T` lower bound requires a weighted Poincare/interface estimate. But the exact geometry and the coercive defect norm are now explicit.

Status: **NEAR SATURATION OF THE 7/9 H1 COVARIANCE CAP FORCES SIMULTANEOUS SPATIAL ONE-DIMENSIONALITY AND AXISYMMETRIC MAX-MID DERIVATIVE STRUCTURE. EXACT SATURATION WITH FINITE WHOLE-SPACE ENERGY IS TRIVIAL. THE REMAINING TASK IS A QUANTITATIVE LOCALIZATION COST FOR APPROXIMATE SATURATION.**