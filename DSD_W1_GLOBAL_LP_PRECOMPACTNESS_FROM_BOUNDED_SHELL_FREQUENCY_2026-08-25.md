# DSD W1: Global Lp Precompactness from Bounded Shell Frequency

Date: 2026-08-25

Status: **W1 FUNCTION-SPACE UPGRADE PROVED FOR EVERY 3<p<=6 / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

After the direct routing

\[
W_2:\ \|U\|_{L^{3,\infty}}\uparrow
\Longrightarrow H_{freq}
\]

on the bounded-Campanato corridor, the genuine endpoint survivor is the bounded-frequency class `W1`:

\[
\sup_s\|U(s)\|_{L^{3,\infty}}<\infty,
\qquad
\sup_{R,s}\Gamma_R(s)\le \Gamma_*<\infty,
\]

with bounded normalized enstrophy and a nonzero recurrent core.

This note proves that `W1` is substantially stronger than a generic weak-L3 class. It is uniformly bounded and tight in every global `L^p`, `3<p<=6`, and therefore its Leray orbit is precompact in each such `L^p` once the already available local analytic compactness is inserted.

---

## 2. Annular setup

Let

\[
A_R=\{R<|Y|<2R\}
\]

and let `A_R^*` be a fixed enlargement.

Write

\[
m_R=(U)_{A_R^*},
\qquad
f_R=U-m_R
\]

on the retained annulus, with the standard divergence-free cutoff/Bogovskii localization when an exact compact packet is needed.

The bounded relative-Campanato corridor gives

\[
\boxed{
R^{-1}\|f_R\|_{L^2(A_R^*)}^2\le C_0.
}
\]

Hence

\[
\boxed{
\|f_R\|_2\le C_0^{1/2}R^{1/2}.
}
\]

The non-H derivative-frequency condition is

\[
\boxed{
\Gamma_R:=\frac{R\|\nabla f_R\|_2}{\|f_R\|_2}\le\Gamma_*.
}
\]

Therefore

\[
\boxed{
\|\nabla f_R\|_2
\le
\Gamma_*C_0^{1/2}R^{-1/2}.
}
\]

All constants below absorb fixed enlargement/cutoff factors.

---

## 3. Annular L6 bound

Scale the standard Sobolev-Poincare estimate from a unit annulus:

\[
\|f_R\|_{L^6(A_R)}
\le C\|\nabla f_R\|_{L^2(A_R^*)}.
\]

Thus

\[
\boxed{
\|f_R\|_{L^6(A_R)}
\le
C(C_0,\Gamma_*)R^{-1/2}.
}
\]

This is exactly the critical `1/R` shell scaling in L6 form.

---

## 4. Interpolation to every 3<p<=6

For `2<=p<=6`, choose `theta` from

\[
\frac1p=\frac{1-\theta}{2}+\frac\theta6,
\qquad
\theta=\frac32-\frac3p.
\]

Interpolation gives

\[
\|f_R\|_p
\le
\|f_R\|_2^{1-\theta}
\|f_R\|_6^\theta.
\]

Using the preceding shell estimates,

\[
\|f_R\|_p
\le
C R^{(1-\theta)/2}R^{-\theta/2}
=C R^{1/2-\theta}.
\]

Since

\[
\frac12-\theta
=\frac3p-1,
\]

we obtain

\[
\boxed{
\|U-m_R\|_{L^p(A_R)}
\le
C_p R^{3/p-1},
\qquad 3<p\le6.
}
\]

Equivalently,

\[
\boxed{
\int_{A_R}|U-m_R|^p
\le
C_p R^{3-p}.
}
\]

---

## 5. Mean term has the same critical decay

The finite-energy/relative-Campanato mean telescope already used in
`FINITE_ENERGY_RELATIVE_CAMPANATO_TO_MORREY_2026-08-24.md`
gives, under uniform Campanato control,

\[
R|m_R|
\le
C\sum_{k\ge0}2^{-k}\mathcal C_{2^kR}^{1/2}
\le C(C_0).
\]

Hence

\[
\boxed{|m_R|\le C R^{-1}.}
\]

Since `|A_R|~R^3`,

\[
\boxed{
\int_{A_R}|m_R|^p
\le C_pR^{3-p}.
}
\]

Combining mean and mean-free terms,

\[
\boxed{
\int_{A_R}|U|^p
\le C_pR^{3-p},
\qquad 3<p\le6.
}
\]

---

## 6. Dyadic summability and global Lp bound

Let `R_k=2^kR_0`. For every `p>3`,

\[
\sum_{k\ge0}R_k^{3-p}<\infty.
\]

Therefore

\[
\boxed{
\sup_s\|U(s)\|_{L^p(\mathbb R^3)}<\infty,
\qquad 3<p\le6.
}
\]

More strongly, the tail obeys

\[
\boxed{
\sup_s
\int_{|Y|>R}|U(Y,s)|^p\,dY
\le
C_pR^{3-p}
\to0
\quad(R\to\infty).
}
\]

Thus the W1 orbit is uniformly `L^p`-tight for every `p>3`.

The endpoint `p=3` is exactly critical: the dyadic bound becomes order one per logarithmic shell and need not be summable. This preserves the genuine weak-L3 obstruction rather than hiding it.

---

## 7. Global Lp precompactness of the Leray orbit

On every fixed ball, the recurrent first-hitting/ancient corridor already has uniform local analytic derivative bounds. Hence any time sequence `s_n` has a subsequence converging strongly on compact sets in `C^m` for each fixed finite `m`.

Fix `p in (3,6]` and `epsilon>0`. Choose `R` so large that

\[
\sup_s\|U(s)\|_{L^p(|Y|>R)}<\epsilon.
\]

On `B_R`, local analytic compactness gives a subsequence converging strongly in `L^p(B_R)`. The two uniform tails contribute at most `2epsilon`.

Therefore

\[
\boxed{
\{U(s):s\ge s_0\}
\text{ is precompact in }L^p(\mathbb R^3)
\quad\forall\,3<p\le6.
}
\]

The same argument applies to omega-limit trajectories extracted by time translation.

---

## 8. Consequences for the final rigidity problem

The final W1 survivor is not an arbitrary bounded ancient weak-L3 solution. It is a much narrower class:

\[
\boxed{
\begin{aligned}
&U\in L_s^\infty L_Y^{3,\infty},\\
&U\in L_s^\infty L_Y^p\quad\forall 3<p\le6,\\
&\sup_s\|\Omega(s)\|_2<\infty,\\
&\text{the orbit is precompact in every }L^p,\ p>3,\\
&\text{the local recurrent core is nonzero},\\
&\text{and the shell derivative ratio is uniformly bounded.}
\end{aligned}
}
\]

Therefore any remaining rigidity theorem only needs to exclude a nonzero recurrent/precompact Leray trajectory in this endpoint class, rather than all bounded ancient three-dimensional Navier-Stokes solutions.

Stationary/self-similar omega-limit points can be tested against the existing backward-self-similar Liouville theorems; the genuinely new issue is a nonstationary recurrent orbit.

---

## 9. Audit verdict

### PROVED

- bounded shell Campanato plus bounded derivative ratio gives the critical annular estimate
  \[
  \|U\|_{L^p(A_R)}\lesssim R^{3/p-1};
  \]
- for every `p>3` the dyadic tail is summable;
- W1 is uniformly bounded and tight in global `L^p`, `3<p<=6`;
- local analyticity plus tail tightness makes the Leray orbit globally `L^p`-precompact.

### OPEN

- exclusion of a genuinely nonstationary recurrent/precompact W1 Leray trajectory;
- final integration of all H/T/D/R branches;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
