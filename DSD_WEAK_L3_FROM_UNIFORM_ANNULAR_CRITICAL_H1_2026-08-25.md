# DSD Weak-L3 Control from Uniform Annular Critical H1

Date: 2026-08-25

Status: **PROVED DYADIC ENDPOINT EMBEDDING / RESIDUAL WEAK-L3 ESCALATION REDUCED TO CRITICAL-H1 SHELL ESCALATION / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The current last residual-tail frontier is

\[
\|U_j\|_{L^{3,\infty}}\to\infty.
\]

This note proves that such escalation cannot occur if the critical first-derivative energy of every dyadic annulus remains uniformly bounded.

The key point is that weak-L3 requires only a distribution-function bound, not summability of annular L3 masses.

## 2. Dyadic annuli and critical H1 quantity

Fix `R0>0` and define

\[
R_k=2^kR_0,
\qquad
A_k=\{R_k<|Y|<2R_k\},
\]

with fixed enlargements `A_k^*` of uniformly bounded overlap.

Set

\[
\boxed{
E_k:=R_k\int_{A_k^*}|\nabla U|^2\,dY.
}
\]

Assume

\[
\boxed{
\sup_{k\ge0}E_k\le E_*<\infty.
}
\]

Let

\[
m_k=(U)_{A_k^*},
\qquad
f_k=U-m_k.
\]

## 3. L2 and L6 shell estimates

Poincare on a fixed-shape annulus, after scaling, gives

\[
\|f_k\|_2^2
\le C R_k^2\int_{A_k^*}|\nabla U|^2
\le C E_*R_k.
\]

Thus

\[
\boxed{
\|f_k\|_2^2\le C E_*R_k.
}
\]

Sobolev on the same enlarged annulus gives

\[
\|f_k\|_6
\le C\|\nabla U\|_{L^2(A_k^*)}
\le C E_*^{1/2}R_k^{-1/2}.
\]

Hence

\[
\boxed{
\|f_k\|_6^6\le C E_*^3R_k^{-3}.
}
\]

## 4. Distribution estimate for the mean-free part

For any `lambda>0`, Chebyshev gives two bounds:

\[
|\{|f_k|>\lambda\}\cap A_k|
\le C E_*R_k\lambda^{-2},
\]

and

\[
|\{|f_k|>\lambda\}\cap A_k|
\le C E_*^3R_k^{-3}\lambda^{-6}.
\]

Therefore

\[
|\{|f_k|>\lambda\}\cap A_k|
\le C\min\{
E_*R_k\lambda^{-2},
E_*^3R_k^{-3}\lambda^{-6}
\}.
\]

The two expressions balance at

\[
R_*\asymp E_*^{1/2}\lambda^{-1}.
\]

Sum the L2 bound over dyadic radii `R_k<=R_*`:

\[
\sum_{R_k\le R_*}
E_*R_k\lambda^{-2}
\le C E_*R_*\lambda^{-2}
\le C E_*^{3/2}\lambda^{-3}.
\]

Sum the L6 bound over `R_k>R_*`:

\[
\sum_{R_k>R_*}
E_*^3R_k^{-3}\lambda^{-6}
\le C E_*^3R_*^{-3}\lambda^{-6}
\le C E_*^{3/2}\lambda^{-3}.
\]

Thus

\[
\boxed{
\left|
\left\{Y:\ |U(Y)-m_{k(Y)}|>\lambda\right\}
\right|
\le C E_*^{3/2}\lambda^{-3}.
}
\]

## 5. Dyadic means

Finite physical energy fixes the velocity mean at spatial infinity. Neighboring annular means satisfy

\[
|m_{k+1}-m_k|
\le C R_k^{-3/2}\|U-m_k\|_{L^2(A_k^*)}
\le C E_*^{1/2}R_k^{-1}.
\]

Telescoping outward therefore gives

\[
\boxed{
|m_k|\le C E_*^{1/2}R_k^{-1}.
}
\]

For a fixed `lambda`, the mean can exceed `lambda/2` only on shells

\[
R_k\le C E_*^{1/2}\lambda^{-1}.
\]

The volume of their union is bounded by

\[
C E_*^{3/2}\lambda^{-3}.
\]

Hence the mean part obeys the same weak-L3 distribution law.

## 6. Exterior weak-L3 bound

Combining the mean and mean-free estimates,

\[
\boxed{
\sup_{\lambda>0}
\lambda^3
\left|
\{Y:\ |Y|>R_0,\ |U(Y)|>\lambda\}
\right|
\le C E_*^{3/2}.
}
\]

Equivalently,

\[
\boxed{
\|U\|_{L^{3,\infty}(|Y|>R_0)}
\le C E_*^{1/2}.
}
\]

A fixed inner ball is harmless on the recurrent analytic corridor because `U` is uniformly bounded there.

Therefore

\[
\boxed{
\sup_k
R_k\int_{A_k^*}|\nabla U|^2<\infty
\Longrightarrow
U\in L^{3,\infty}(\mathbb R^3).
}
\]

## 7. Contrapositive for the residual tail

For a sequence of recurrent first-hitting states whose fixed-core contribution is uniformly controlled,

\[
\boxed{
\|U_j\|_{L^{3,\infty}}\to\infty
\Longrightarrow
\sup_R
R\int_{A_R}|\nabla U_j|^2\to\infty
}
\]

along a subsequence.

Thus residual weak-L3 escalation is not a new zero-derivative tail mechanism. It necessarily creates critical-H1 shell escalation.

## 8. Combine with the existing H1 -> Campanato/H2 reduction

`CRITICAL_H1_TAIL_TO_CAMPANATO_OR_H2_2026-08-24.md` proves

\[
H_{1,crit}^{tail}
\Longrightarrow
\text{relative-Campanato escalation}
\lor
H_{2,crit}^{tail}.
\]

Therefore

\[
\boxed{
L^{3,\infty}\text{ residual escalation}
\Longrightarrow
\text{relative-Campanato escalation}
\lor
H_{2,crit}^{tail}.
}
\]

This is precisely the two-way bridge needed for the current DSD endgame.

## 9. Audit verdict

### PROVED

- uniform annular critical-H1 control implies global weak-L3 control;
- weak-L3 escalation forces critical-H1 shell escalation;
- using the previous interpolation lemma, weak-L3 escalation reduces to Campanato escalation or critical-H2 derivative escalation.

### NOT YET CLAIMED HERE

- Campanato escalation is impossible;
- critical-H2 escalation is globally contradictory;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
