# Exact H1 Covariance Identity for the P_V Branch — 2026-08-20

Overall status: **NEW DERIVATIVE-GEOMETRY IDENTITY — GLOBAL REGULARITY NOT PROVED.**

This note connects the remaining projective `P_V` branch directly to the evolution of strain palinstrophy. The key is to use the strain--vorticity residual

\[
\mathcal R_{VI}
=P_{st}\left((u\cdot\nabla)S+S^2+\frac34\omega\otimes\omega\right)
=\mathcal A+3\mathcal V,
\]

for which the explicit vorticity term is orthogonal to `-Delta S`.

---

## 1. Exact H1 evolution

Let

\[
P_S=\|\nabla S\|_2^2,
\qquad
H_S=\|\Delta S\|_2^2.
\]

Taking the `L^2` inner product of the strain equation written relative to the strain--vorticity interaction model with `-Delta S` gives

\[
\boxed{
\frac12\frac{d}{dt}P_S
+\nu H_S
+\langle\mathcal R_{VI},-\Delta S\rangle
=0.
}
\]

The identity

\[
\langle-\Delta S,\omega\otimes\omega\rangle=0
\]

is essential here.

In dynamic first-hitting variables, where physical `P_S=W^{3/2}P_\Sigma`, the normalized form is

\[
\boxed{
\frac12P_\Sigma'
+\frac32aP_\Sigma
+\nu H_\Sigma
+\langle\mathcal R_{VI}^{norm},-\Delta\Sigma\rangle
=0.
}
\]

Thus a recurrent derivative-controlled profile must repeatedly make the final contraction sufficiently negative to overcome both viscous hyperdissipation and the positive scale damping `3aP/2`.

---

## 2. Spatial gradient covariance from advection

For each spatial derivative direction define

\[
G_k=\partial_kS.
\]

Set the `spatial-index` covariance

\[
(M_{sp})_{k\ell}=\langle G_k,G_\ell\rangle_F.
\]

It is symmetric positive semidefinite and

\[
\operatorname{tr}M_{sp}=|\nabla S|^2.
\]

Integration by parts gives

\[
\begin{aligned}
\langle(u\cdot\nabla)S,-\Delta S\rangle
&=\sum_{k,\ell}\int(\partial_ku_\ell)
\langle G_\ell,G_k\rangle_F\\
&=\int S:M_{sp}.
\end{aligned}
\]

The antisymmetric part of `grad u` drops out because `M_sp` is symmetric. Hence

\[
\boxed{
\langle\mathcal A,-\Delta S\rangle
=\int S:M_{sp}.
}
\]

This is the exact `H1` advection contraction in terms of the spatial covariance of the strain gradient.

---

## 3. Range gradient covariance from S^2

Define the `range-index` covariance

\[
M_{rg}=\sum_kG_k^2.
\]

Because each `G_k` is symmetric, `M_rg` is positive semidefinite, and

\[
\operatorname{tr}M_{rg}=|\nabla S|^2.
\]

Also

\[
\begin{aligned}
\langle S^2,-\Delta S\rangle
&=\sum_k\int \partial_k(S^2):G_k\\
&=2\sum_k\int\operatorname{tr}(S G_k^2)\\
&=2\int S:M_{rg}.
\end{aligned}
\]

Since the vorticity tensor is orthogonal to `-Delta S`, this gives

\[
\boxed{
\langle3\mathcal V,-\Delta S\rangle
=2\int S:M_{rg}.
}
\]

---

## 4. Exact combined covariance identity

Adding the two terms,

\[
\boxed{
\langle\mathcal R_{VI},-\Delta S\rangle
=\int S:(M_{sp}+2M_{rg}).
}
\]

At points where `|grad S| != 0`, define

\[
C_{sp}=\frac{M_{sp}}{|\nabla S|^2},
\qquad
C_{rg}=\frac{M_{rg}}{|\nabla S|^2},
\]

and

\[
\overline C=\frac{C_{sp}+2C_{rg}}{3}.
\]

Then all three matrices are positive semidefinite with trace one, and

\[
\boxed{
\langle\mathcal R_{VI},-\Delta S\rangle
=3\int|\nabla S|^2\,S:\overline C.
}
\]

Thus derivative growth is governed by the alignment of the strain with a combined spatial/range covariance of its own gradient.

---

## 5. Trace-free range cap

A new purely algebraic fact is available because every `G_k=partial_k S` is symmetric and trace free.

For every symmetric trace-free `3x3` matrix `G` and every unit vector `n`,

\[
\boxed{
n^TG^2n\le\frac23|G|_F^2.}
\]

To verify it, rotate so `n=e_1` and write

\[
G=
\begin{pmatrix}
a&x&y\\x&b&z\\y&z&-a-b
\end{pmatrix}.
\]

Then

\[
\frac23|G|^2-e_1^TG^2e_1
=
\frac13\left[(a+2b)^2+x^2+y^2+4z^2\right]\ge0.
\]

Equality holds iff

\[
G=a\,\mathrm{diag}(1,-1/2,-1/2)
\]

in that axis frame.

Summing over `k` yields

\[
\boxed{
\lambda_{max}(C_{rg})\le\frac23.
}
\]

Consequently

\[
\boxed{
\lambda_{max}(\overline C)
\le
\frac{1+2(2/3)}{3}
=\frac79.
}
\]

---

## 6. Eigenvalue bound on the H1 nonlinear contraction

Let

\[
s_1\le s_2\le s_3,
\qquad s_1+s_2+s_3=0
\]

be the eigenvalues of `S`. For any positive semidefinite trace-one matrix `C` with `lambda_max(C)<=7/9`, the minimum of `S:C` is obtained by placing weight `7/9` on `s_1` and the remaining `2/9` on `s_2`. Therefore

\[
\boxed{
S:\overline C
\ge
\frac79s_1+\frac29s_2.
}
\]

Similarly,

\[
\boxed{
S:\overline C
\le
\frac79s_3+\frac29s_2.
}
\]

Hence pointwise

\[
\boxed{
\frac13(7s_1+2s_2)|\nabla S|^2
\le
\text{H1 residual density}
\le
\frac13(7s_3+2s_2)|\nabla S|^2.
}
\]

In particular,

\[
-\langle\mathcal R_{VI},-\Delta S\rangle
\le
\frac13\int(5s_2+7s_3)|\nabla S|^2,
\]

using `-s_1=s_2+s_3`.

---

## 7. Consequence for recurrent first-hitting stages

The normalized H1 ledger is

\[
\frac12P_\Sigma'
+\frac32aP_\Sigma
+\nu H_\Sigma
=-\langle\mathcal R_{VI}^{norm},-\Delta\Sigma\rangle.
\]

If `P_\Sigma` remains recurrent/bounded away from zero over a geometric stage, the right-hand side must pay not only viscous hyperdissipation but also the fixed positive scale-damping action

\[
\frac32\int aP_\Sigma ds.
\]

Thus the remaining `P_V` orbit requires a repeated **compressive alignment of the combined gradient covariance** `Cbar` with the negative strain eigenspace.

Because `C_rg` can place at most `2/3` of its mass on any one axis, perfect derivative-range alignment is impossible. Equality in the range cap forces every active derivative matrix into the axisymmetric trace-free pattern

\[
G_k\propto\mathrm{diag}(-2,1,1)
\]

(up to sign and axis convention), which is the differential analogue of the max-mid structure already heavily constrained in the main proof route.

---

## 8. New reduced target

The remaining projective branch must now satisfy two simultaneous requirements:

1. the advection/algebraic alignment parameter avoids the regularizing `alpha=3` lock often enough;
2. the `H1` residual must anti-align with `-Delta S` strongly enough that the combined gradient covariance repeatedly concentrates toward the compressive strain eigenspace, despite the universal `2/3` range cap.

The next target is a quantitative rigidity/packing theorem for near-saturation of this covariance bound. Near saturation should force a nearly one-dimensional, fixed-axis max-mid derivative geometry, which can then be tested against the strain compatibility constraint, aligned-tube turnover, or the previously derived max-mid projection inequalities.

Status: **P_V-DRIVEN H1 GROWTH HAS AN EXACT TWO-COVARIANCE GEOMETRY. THE RANGE COVARIANCE HAS A UNIVERSAL 2/3 AXIS CAP AND THE COMBINED COVARIANCE A 7/9 CAP. PERSISTENT TYPE-I RECURRENCE MUST REPEATEDLY APPROACH A HIGHLY COMPRESSIVE DERIVATIVE GEOMETRY OR PAY ADDITIONAL H/T/PROJECTIVE COST.**