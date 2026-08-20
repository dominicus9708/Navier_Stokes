# Localized Compatibility Covariance Cap — 2026-08-20

Overall status: **LOCAL CORE/ANNULUS COMPATIBILITY BRIDGE — GLOBAL REGULARITY NOT PROVED.**

This note repairs the locality gap identified in `PV_BALL_COHERENCE_SCOPE_CORRECTION_2026-08-20.md`.

The global fixed-axis cap

\[
n^T\mathbb Cn\le\frac23
\]

can be transferred to a core ball by localizing the **velocity** rather than cutting off the strain directly.

---

## 1. Divergence-free velocity localization

Choose a smooth cutoff `chi_R` such that

\[
\chi_R=1\quad\text{on }B_R,
\qquad
\chi_R=0\quad\text{outside }B_{2R},
\]

with

\[
|\nabla\chi_R|\lesssim R^{-1},
\qquad
|\nabla^2\chi_R|\lesssim R^{-2}.
\]

Let

\[
A_R=B_{2R}\setminus B_R.
\]

Since `div u=0`,

\[
\operatorname{div}(\chi_Ru)
=\nabla\chi_R\cdot u
\]

is supported in `A_R` and has zero mean. Let `b_R` be an annular Bogovskii correction satisfying

\[
\operatorname{div}b_R
=\nabla\chi_R\cdot u.
\]

Set

\[
\boxed{
u_R=\chi_Ru-b_R.}
\]

Then

\[
\operatorname{div}u_R=0,
\qquad
u_R=u\text{ on }B_R,
\qquad
\operatorname{supp}u_R\subset B_{2R}.
\]

Define

\[
S_R=\operatorname{sym}\nabla u_R.
\]

Therefore

\[
S_R=S,
\qquad
\nabla S_R=\nabla S
\quad\text{on }B_R.
\]

---

## 2. Apply the exact global compatibility cap to the localized field

For a fixed unit vector `n`, define the core covariance numerator

\[
I_{n,B_R}
=
\|\partial_nS\|_{L^2(B_R)}^2
+2\sum_k\|(\partial_kS)n\|_{L^2(B_R)}^2.
\]

Let

\[
P_R=\|\nabla S\|_{L^2(B_R)}^2.
\]

Because `S_R` is a globally compatible incompressible strain field,

\[
I_n[S_R]
\le
2\|\nabla S_R\|_2^2.
\]

All terms in `I_n` are nonnegative, and `S_R=S` on the core, so

\[
I_{n,B_R}
\le
I_n[S_R]
\le
2P_R
+2\|\nabla S_R\|_{L^2(A_R)}^2.
\]

Define the corrected annular compatibility leakage

\[
\boxed{
\mathcal E_A(R)
=
\frac{\|\nabla S_R\|_{L^2(A_R)}^2}{P_R}.
}
\]

Then the localized fixed-axis covariance satisfies

\[
\boxed{
\frac{I_{n,B_R}}{3P_R}
\le
\frac23
+\frac23\mathcal E_A(R).
}
\]

This is the local replacement for the global `2/3` cap.

---

## 3. Annular error in original variables

The Bogovskii `W^{2,2}` estimate and the cutoff product rule give

\[
\boxed{
\|\nabla S_R\|_{L^2(A_R)}
\le
C_{comp}
\left[
\|\nabla S\|_{L^2(A_R)}
+R^{-1}\|\nabla u\|_{L^2(A_R)}
+R^{-2}\|u\|_{L^2(A_R)}
\right]
}
\]

for one scale-invariant annular localization constant `C_comp`.

Consequently

\[
\boxed{
\mathcal E_A(R)
\le
C_{comp}^2
\frac{
\left[
\|\nabla S\|_{A_R}
+R^{-1}\|\nabla u\|_{A_R}
+R^{-2}\|u\|_{A_R}
\right]^2
}{P_R}.
}
\]

Thus failure of local compatibility transfer is itself an annular derivative/material leakage event.

---

## 4. The `1/6` leakage threshold

The old pointwise covariance ceiling is `7/9`. The localized compatibility cap improves it whenever

\[
\frac23+\frac23\mathcal E_A
<\frac79.
\]

This is equivalent to

\[
\boxed{
\mathcal E_A<\frac16.
}
\]

Therefore the local branch splits sharply:

### Large annular compatibility leakage

If

\[
\boxed{
\mathcal E_A\ge\frac16,
}
\]

then the corrected annulus carries at least one-sixth of the core strain-gradient energy. This is a definite derivative/material leakage packet and belongs naturally to the existing `H/T` routing.

### Small annular compatibility leakage

If

\[
\boxed{
\mathcal E_A<\frac16,
}
\]

then the local fixed-axis covariance ceiling is strictly below `7/9`, so a positive compatibility gap survives inside the core.

---

## 5. Moving-axis local compatibility loop

Let `n(x)` be the local compressive eigenaxis in `B_R`. Define

\[
A_{mov,R}
=
\frac1{P_R}
\int_{B_R}
|\nabla S|^2
n(x)^T\overline C(x)n(x)dx,
\]

and

\[
\overline\varepsilon_R
=\frac79-A_{mov,R}.
\]

For a fixed unit vector `n0`, the localized cap gives

\[
\frac1{P_R}
\int_{B_R}
|\nabla S|^2
n_0^T\overline Cn_0dx
\le
\frac23+rac23\mathcal E_A.
\]

As before,

\[
|n^T\overline Cn-n_0^T\overline Cn_0|
\le2|n-n_0|.
\]

Hence the weighted axis dispersion

\[
D_*^2
=
\inf_{|n_0|=1}
\frac1{P_R}
\int_{B_R}
|\nabla S|^2|n-n_0|^2dx
\]

must satisfy

\[
\boxed{
D_*
\ge
\frac12
\left[
\frac19
-\frac23\mathcal E_A
-\overline\varepsilon_R
\right]_+.
}
\]

---

## 6. Combine with the ball coherence estimate

On a positive-gap active ball, `PV_EXPLICIT_BALL_COHERENCE_CONSTANT_2026-08-20.md` gives

\[
D_*^2
\le
C_{coh}^{ball}\overline\varepsilon_R,
\]

where

\[
C_{coh}^{ball}
=\frac{36}{\pi^2}
\frac{R^2P_\infty}{g_-^2}.
\]

Define

\[
\boxed{
a_R
=\left[
\frac19-rac23\mathcal E_A(R)
\right]_+.
}
\]

Then

\[
(a_R-\overline\varepsilon_R)^2
\le
4C_{coh}^{ball}\overline\varepsilon_R.
\]

Therefore

\[
\boxed{
\overline\varepsilon_R
\ge
\delta_{cov,R}
:=
\left(
\sqrt{C_{coh}^{ball}+a_R}
-\sqrt{C_{coh}^{ball}}
\right)^2.
}
\]

This is the corrected fully local covariance-gap formula.

---

## 7. Local H1 compatibility tax

If

\[
s_2-s_1\ge g_->0
\]

on the active ball, the exact covariance density decomposition gives

\[
\boxed{
N_R
\le
N_{ceiling,R}
-3g_-\delta_{cov,R}P_R
}
\]

before strongest-extensional leakage is included.

Thus the local recurrent branch obeys the dichotomy

\[
\boxed{
\mathcal E_A\ge\frac16
\quad\Rightarrow\quad H/T\text{-scale annular leakage},
}

or

\[
\boxed{
\mathcal E_A<\frac16
\quad\Rightarrow\quad
\text{strict positive compatibility covariance tax}.
}
\]

---

## 8. Updated proof target

The compatibility/localization problem is now reduced to quantitative control of

\[
\mathcal E_A(R),
\qquad
P_\infty,
\qquad
g_-,
\qquad R.
\]

If the annular error is not small, it is already a noncompact leakage event. If it is small, the covariance gap is explicit through

\[
\delta_{cov,R}
=
\left(
\sqrt{
\frac{36}{\pi^2}\frac{R^2P_\infty}{g_-^2}
+
\frac19-rac23\mathcal E_A
}
-
\sqrt{
\frac{36}{\pi^2}\frac{R^2P_\infty}{g_-^2}
}
\right)^2.
\]

Status: **THE GLOBAL `2/3` STRAIN-COMPATIBILITY CAP HAS BEEN LOCALIZED TO AN ACTIVE CORE WITH A SINGLE ANNULAR ERROR. IF THAT ERROR REACHES `1/6`, IT IS ALREADY A DEFINITE H/T LEAKAGE EVENT; BELOW `1/6`, A STRICT EXPLICIT LOCAL COVARIANCE GAP SURVIVES.**