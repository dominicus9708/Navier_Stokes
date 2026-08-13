# Compactness-rigidity gap for the canonical sharp Gagliardo--Nirenberg source step

Date: 2026-08-13

Status: **CANONICAL COMPACTNESS-RIGIDITY LEMMA FOR THE SHARP SCALAR SOURCE STEP**.

After the sharp-Gagliardo--Nirenberg audit correction, the canonical scalar source estimate no longer treats `L2-L3-L6` interpolation and critical Sobolev as two independently optimized steps.  The correct compactness-rigidity object is the single sharp GN ratio.

External anchors:

- Michael I. Weinstein, *Nonlinear Schrödinger equations and sharp interpolation estimates*, Communications in Mathematical Physics 87 (1983), 567--576;
- Jian-Guo Liu and Jinhuan Wang, *On the best constant for Gagliardo-Nirenberg interpolation inequalities* (2017), general sharp constants and optimizer structure.

---

## 1. Sharp GN ratio

For nonzero

\[
f\in H^1(\mathbb R^3),
\]

define

\[
\boxed{
\mathcal R_{\rm GN}[f]
=
\frac{\|f\|_3}
{C_{\rm GN}\|f\|_2^{1/2}\|\nabla f\|_2^{1/2}}
\le1,
}
\]

where `C_GN` is the best whole-space constant.

The equality cases are the variational ground-state optimizer family, modulo amplitude/translation/dilation symmetries.

In the present `d=3`, `L2`--gradient-`L2`--target-`L3` case, a nonzero optimizer solves the associated elliptic Euler--Lagrange ground-state equation after normalization.  Such a ground state is a noncompactly supported whole-space profile.

---

## 2. Fixed normalized cutoff family

Let

\[
\chi\in C_c^\infty(B_R)
\]

be fixed and define

\[
\boxed{
f_j=\chi|\Omega_j|\in H_0^1(B_R).}
\]

Assume

\[
\boxed{
f_j\to f_\infty
\quad\text{strongly in }H^1(B_R)}
\]

and

\[
\boxed{
\|f_j\|_2\ge c_0>0.
}
\]

Then

\[
f_\infty\not\equiv0.
\]

Zero-extend every `f_j` and `f_infty` to `R^3`.  Strong `H1` convergence is preserved under this fixed zero extension.

---

## 3. Sharp-GN saturation would produce a compactly supported optimizer

Suppose for contradiction

\[
\mathcal R_{\rm GN}[f_j]\to1.
\]

Strong `H1` convergence implies strong `L2` and `L3` convergence, and convergence of the gradient `L2` norm.  Therefore

\[
\boxed{
\mathcal R_{\rm GN}[f_\infty]=1.
}
\]

Thus the zero extension of `f_infty` is a nonzero whole-space sharp-GN optimizer.

But it has compact support inside `\overline{B_R}`.  This is incompatible with the noncompactly supported ground-state optimizer family.

Hence

\[
\boxed{
\limsup_{j\to\infty}
\mathcal R_{\rm GN}[f_j]<1.
}
\]

Equivalently, there exists a family-dependent

\[
\boxed{\delta_{\rm GN}>0}
\]

such that eventually

\[
\boxed{
\|f_j\|_3
\le
(1-\delta_{\rm GN})
C_{\rm GN}
\|f_j\|_2^{1/2}
\|\nabla f_j\|_2^{1/2}.
}
\]

Cubing,

\[
\boxed{
\|f_j\|_3^3
\le
(1-\delta_{\rm GN})^3
C_{\rm GN}^3
\|f_j\|_2^{3/2}
\|\nabla f_j\|_2^{3/2}.
}
\]

---

## 4. Bounded V2 supplies the required compactness

On the buffered normalized V2-bounded branch, the already-derived lemma gives

\[
\Omega_j
\to
\Omega_\infty
\quad\text{strongly in }L_s^2H_y^1
\]

on a smaller cylinder.

After selecting almost-everywhere persistent source-active times, one obtains strongly `H1`-convergent cutoff magnitude profiles.

The temporal-concentration gate supplies the complementary alternative: if no persistent time set exists, the local source/shell channel becomes unbounded.

Therefore, on the fully bounded persistent V2 branch, the sharp-GN gap is no longer an independent assumption.

---

## 5. Canonical local source consequence

The canonical near-source estimate uses

\[
\|f_j\|_3^3.
\]

On the compact nontrivial branch it therefore inherits the strict factor

\[
\boxed{
(1-\delta_{\rm GN})^3.
}
\]

Separately, the exact magnitude/direction gradient split gives

\[
\|\nabla|\Omega_j|\|_2^2
=P-P_{\rm ang}.
\]

Hence the compact local scalar source has the structural form

\[
\boxed{
Q_{\rm near}
\lesssim
C_R C_{\rm GN}^3
(1-\delta_{\rm GN})^3
E^{3/4}
(P-P_{\rm ang}+\text{cutoff reserve})^{3/4}.
}
\]

The precise buffered cutoff reserve is kept explicit in the localized source note.

---

## 6. Relation to the older auxiliary gaps

The previous

- magnitude-heterogeneity interpolation gap; and
- separate sharp-Sobolev compactness gap

remain valid diagnostic statements about a nonsharp factorization of the scalar estimate.

They should now be interpreted as **explanations of loss of sharpness**, not multiplied on top of the canonical sharp-GN constant.

The present `delta_GN` is the canonical compactness-rigidity coefficient used by the source estimate.

---

## 7. Concentration alternative

Sharp-GN near-extremizing sequences can evade fixed strong `H1` compactness through the inequality's translation/dilation noncompactness.

In the current proof map this is not hidden: if the normalized source tries to approach the sharp GN constant while the fixed-window cutoff family fails strong `H1` compactness, the sequence must leave the bounded V2/compactness state block or concentrate relative to the fixed normalized scale.

Thus

\[
\boxed{
\text{strong compactness}
\Rightarrow
\text{uniform GN gap},
}
\]

or

\[
\boxed{
\text{GN near saturation}
\Rightarrow
\text{typed concentration/modulation branch}.
}
\]

---

## 8. Current role

The canonical bounded-branch source analysis now needs only one scalar near-extremizer rigidity parameter `delta_GN`, plus

- angular palinstrophy;
- projective covariance;
- far strain/tail;
- shell transport;
- Cauchy I/V amplification.

This substantially reduces the number of artificial equality conditions introduced by the earlier factorized estimate.

Status: **CANONICAL SHARP-GN COMPACTNESS GAP DERIVED / MODULATION-OR-CONCENTRATION EXHAUSTION NEXT**.
