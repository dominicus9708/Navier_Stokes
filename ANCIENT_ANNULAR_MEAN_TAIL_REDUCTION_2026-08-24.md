# Ancient Annular-Mean Tail Reduction — 2026-08-24

Status: **FULL L3 TAIL REDUCED TO THE SAME WEIGHTED DIRICHLET STACK / GLOBAL REGULARITY NOT PROVED.**

This note closes the annular-mean caveat left in `ANCIENT_CRITICAL_TAIL_SHELL_NECESSITY_2026-08-24.md`.

The conclusion is that both the mean-free shell variation and the slowly varying annular means are controlled by the same weighted Dirichlet sequence.  Hence failure of global `L3` requires

\[
\sum_k(R_ke_k)^{3/2}=\infty
\]

for the **full velocity tail**, not merely its mean-free part.

---

## 1. Dyadic annular means

Let

\[
R_k=2^kR_0,
\qquad
A_k=\{R_k<|y|<2R_k\},
\]

and

\[
a_k=(U)_{A_k}.
\]

Let `C_k` be a connected enlarged annulus containing both `A_k` and `A_{k+1}`, for example

\[
C_k=\{R_k<|y|<4R_k\}.
\]

Set

\[
\widetilde e_k
=\int_{C_k}|\nabla U|^2dy.
\]

The family `C_k` has uniformly bounded overlap.

---

## 2. Adjacent means are controlled by shell gradient energy

Let

\[
b_k=(U)_{C_k}.
\]

Then

\[
|a_k-b_k|
\le
|A_k|^{-1/2}
\|U-b_k\|_{L^2(A_k)}.
\]

Poincare on `C_k` gives

\[
\|U-b_k\|_{L^2(C_k)}
\le C R_k\|\nabla U\|_{L^2(C_k)}.
\]

Since `|A_k|~R_k^3`,

\[
|a_k-b_k|
\le
C R_k^{-1/2}\widetilde e_k^{1/2}.
\]

The same estimate holds for `a_{k+1}-b_k`, hence

\[
\boxed{
|a_{k+1}-a_k|
\le
C R_k^{-1/2}\widetilde e_k^{1/2}.
}
\]

Define the weighted shell Dirichlet number

\[
\boxed{
x_k:=R_k\widetilde e_k.}
\]

Then

\[
\boxed{
|a_{k+1}-a_k|
\le
C\frac{x_k^{1/2}}{R_k}.
}
\]

---

## 3. The annular means vanish at infinity

The ancient limit lies in global `L6`.  Therefore

\[
|a_k|
\le
|A_k|^{-1/6}\|U\|_{L^6(A_k)}
\le
C R_k^{-1/2}\|U\|_6.
\]

Hence

\[
\boxed{a_k\to0\qquad(k\to\infty).}
\]

Thus one may telescope from infinity:

\[
a_k
=-\sum_{\ell=k}^{\infty}(a_{\ell+1}-a_\ell).
\]

Using the adjacent-mean estimate and `R_{k+n}=2^nR_k`,

\[
\boxed{
R_k|a_k|
\le
C\sum_{n=0}^{\infty}
2^{-n}x_{k+n}^{1/2}.
}
\]

---

## 4. Discrete Young inequality

Let

\[
y_k=x_k^{1/2}
\]

and let

\[
h_n=2^{-n}\mathbf 1_{n\ge0}.
\]

Then the preceding estimate is

\[
R_k|a_k|
\le C(h*y)_k.
\]

Since

\[
h\in\ell^1,
\]

discrete Young gives

\[
\|h*y\|_{\ell^3}
\le
\|h\|_{\ell^1}\|y\|_{\ell^3}.
\]

Therefore

\[
\boxed{
\sum_k(R_k|a_k|)^3
\le
C\sum_kx_k^{3/2}.
}
\]

But

\[
|A_k||a_k|^3
\asymp
R_k^3|a_k|^3
=(R_k|a_k|)^3.
\]

Hence the total cubic mass carried by the annular means satisfies

\[
\boxed{
\sum_k\int_{A_k}|a_k|^3dy
\le
C\sum_k(R_k\widetilde e_k)^{3/2}.
}
\]

---

## 5. Combine with the mean-free shell estimate

The previous note established

\[
\int_{A_k}|U-a_k|^3dy
\le
C(R_ke_k)^{3/2}.
\]

Because the enlarged-annulus energies `tilde e_k` have bounded overlap and are comparable to a finite sum of neighboring shell energies, one obtains

\[
\boxed{
\sum_k\int_{A_k}|U|^3dy
\le
C\sum_k(R_k\widetilde e_k)^{3/2}.
}
\]

Consequently,

\[
\boxed{
\sum_k(R_k\widetilde e_k)^{3/2}<\infty
\quad\Longrightarrow\quad
U\in L^3(\{|y|>R_0\}).
}
\]

Taking the contrapositive,

\[
\boxed{
U\notin L^3\text{ at spatial infinity}
\quad\Longrightarrow\quad
\sum_k(R_k\widetilde e_k)^{3/2}=\infty.
}
\]

Thus the same weighted Dirichlet stack controls the **entire** critical tail.

---

## 6. Significance for the ancient Liouville obstruction

Albritton-Barker's backward-sequence `L3` Liouville theorem can only be evaded by the restricted ancient survivor if its velocity fails the global `L3` condition at remote backward times.

The present estimate shows that this failure is equivalent, at the shell-obstruction level, to a non-summable weighted Dirichlet stack:

\[
\boxed{
\sum_k(R_ke_k)^{3/2}=\infty.
}
\]

A nearly constant or slowly drifting annular mean cannot evade this conclusion without paying gradient energy in the transitions between shells.

Therefore the final low-frequency obstruction is genuinely vortical/Dirichlet even when it is represented in velocity variables.

---

## 7. Critical model

For

\[
|U|\sim R^{-1},
\qquad
|\nabla U|\sim R^{-2},
\]

one has on a dyadic shell

\[
e_R\sim R^{-1}
\]

and therefore

\[
R e_R\sim1.
\]

Hence

\[
\sum_k(R_ke_{R_k})^{3/2}=\infty,
\]

while

\[
\sum_ke_{R_k}<\infty.
\]

This again shows that the `1/r` tail is exactly the sharp survivor of the current estimates.

---

## 8. Updated final tail statement

The remaining ancient low-frequency obstruction is now completely shell-typed:

\[
\boxed{
\begin{gathered}
\|\Omega(\tau)\|_2^2\lesssim|\tau|^{-1/2},\\
\|\Omega(\tau)\|_\infty\lesssim|\tau|^{-1},\\
U(\tau)\notin L^3
\Longrightarrow
\sum_k(R_ke_k)^{3/2}=\infty,\\
\sum_ke_k<\infty.
\end{gathered}
}
\]

Thus the final survivor must carry an infinite sequence of energy-cheap but **scale-critical weighted-Dirichlet shells**.

Status: **ANNULAR MEANS DO NOT PROVIDE A SEPARATE LOW-FREQUENCY ESCAPE. BOTH MEAN-FREE AND MEAN PARTS OF THE GLOBAL `L3` TAIL ARE CONTROLLED BY THE SAME DYADIC WEIGHTED DIRICHLET STACK. THE FINAL OBSTRUCTION IS PRECISELY `sum (R e_R)^(3/2)=infinity` WITH `sum e_R<infinity`, SATURATED BY `U~1/r`. GLOBAL REGULARITY REMAINS UNPROVED.**