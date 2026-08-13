# Finite shell escalation under bounded normalized enstrophy

Date: 2026-08-13

Status: **DERIVED FINITE-SCALE SHELL SELECTOR / DSD ADAPTIVE LOCALIZATION LEMMA**.

A local dangerous core may try to avoid an interior source-gap argument because the cutoff transport term is large on the first observation shell.  The DSD route need not inspect every radius.  It can move outward through parent shells until a low-enstrophy buffer is found.  Bounded normalized global enstrophy makes the number of such scale hops finite.

---

## 1. Unit-width normalized annuli

After natural-window renormalization, let

\[
A_k
=B_{k+1}\setminus B_k,
\qquad
k=1,2,\ldots.
\]

Assume the normalized global enstrophy satisfies

\[
\boxed{
\|\Omega\|_{L^2(\mathbb R^3)}^2
\le M_E.
}
\]

The annuli are disjoint, so

\[
\sum_{k=1}^{N}
\int_{A_k}|\Omega|^2dy
\le M_E.
\]

---

## 2. Pigeonhole shell selector

For any `epsilon>0`, if

\[
N>\frac{M_E}{\varepsilon},
\]

then not every shell can have enstrophy mass at least `epsilon`.  Therefore

\[
\boxed{
\exists k\le N:\quad
\int_{A_k}|\Omega|^2dy
<\varepsilon.
}
\]

More quantitatively,

\[
\boxed{
\min_{1\le k\le N}
\int_{A_k}|\Omega|^2dy
\le
\frac{M_E}{N}.
}
\]

Thus the outward shell search terminates after finitely many normalized scale hops on every bounded-`M_E` state.

---

## 3. Cutoff on the selected shell

Choose `chi_k` such that

\[
\chi_k=1\text{ on }B_k,
\qquad
\chi_k=0\text{ outside }B_{k+1},
\]

with

\[
|\nabla\chi_k|+|\Delta\chi_k|\le C
\]

because the transition width is one in normalized units.

The local vorticity-enstrophy budget contains the transport shell term

\[
T_{\chi_k}
=\frac12\int
|\Omega|^2U\cdot\nabla(\chi_k^2)dy
\]

and cutoff diffusion term

\[
B_{\chi_k}
=\frac\nu2\int
|\Omega|^2\Delta(\chi_k^2)dy.
\]

Both are supported in `A_k`.

---

## 4. Low shell mass suppresses cutoff transport under bounded local `H1` channels

Assume on the selected annulus/buffer

\[
\|U\|_{H^1}\le M_U,
\qquad
\|\Omega\|_{H^1}\le M_\Omega.
\]

Sobolev gives

\[
\|U\|_6\le C M_U,
\qquad
\|\Omega\|_6\le C M_\Omega.
\]

Interpolate

\[
\|\Omega\|_{12/5}
\le
\|\Omega\|_2^{3/4}
\|\Omega\|_6^{1/4}.
\]

Hence on `A_k`, if

\[
\int_{A_k}|\Omega|^2\le\varepsilon,
\]

then

\[
\boxed{
|T_{\chi_k}|
\le
C M_U M_\Omega^{1/2}
\varepsilon^{3/4}.
}
\]

Also

\[
\boxed{
|B_{\chi_k}|
\le
C\nu\varepsilon.
}
\]

Thus the artificial/localization shell terms become arbitrarily small once a low-enstrophy shell is found, provided the local `H1` block stays bounded.

---

## 5. Adaptive-scale interpretation

The proof search does not need to preselect one globally optimal cutoff radius.

Start from the unit dangerous core:

1. test the first shell;
2. if its transport channel is small, localize there;
3. if its vorticity mass is large, move to the next parent shell;
4. repeat.

On the bounded normalized-enstrophy branch, at most

\[
O(M_E/\varepsilon)
\]

large-mass shell hops can occur before a low-mass shell must appear.

This is exactly a DSD-style adaptive search: only the scale lineage actually carrying danger is inspected.

---

## 6. Complementary concentration branches

The shell selector fails to give a small cutoff contribution only if at least one of the assumed bounded channels fails:

1. normalized global enstrophy `M_E` becomes unbounded;
2. the buffered velocity `H1` channel becomes unbounded;
3. the buffered vorticity `H1`/palinstrophy channel becomes unbounded.

All three are already typed concentration branches.

Therefore localization-shell escape is closed on the fully bounded state block.

---

## 7. Important limitation

Choosing a farther shell enlarges the interior region on which the local enstrophy budget is written.  The present lemma suppresses the **cutoff shell contribution**, but it does not assert that every interior point shares the projective geometry of the original unit dangerous core.

The interior nonlinear source must still be decomposed into

- the original dangerous core/source-gap region;
- any additional active parent-scale regions;
- and regions already controlled by regularity/depletion channels.

Thus the shell selector closes localization leakage, not the full multi-core source interaction.

Status: **FINITE SHELL LEAKAGE CLOSED / INTERIOR MULTI-CORE SOURCE ACCOUNTING REMAINS**.
