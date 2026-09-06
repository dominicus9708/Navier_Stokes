# M17 frontier addendum — M17-257 coherent-mean projected dynamics

Date: 2026-09-06  
Scope: additive correction after `INDEX_M17_250_256_FRONTIER.md`.

This addendum does not replace earlier indices.

---

## 1. Why M17-256 needed a dynamic refinement

M17-256 isolates the quiet normalized-mass-decompactification branch as an almost constant ambient mean

\[
W=c_j+f_j,
\qquad
|c_j|/a_j\to\infty.
\]

The first diagnostic

\[
\beta_j=r_j^2|c_j|
\]

is useful physically but is not sufficient in the packet-normalized fluctuation equation because the normalized mean itself diverges.

---

## 2. Projected fluctuation equation

In own-scale variables

\[
\partial_\tau V_j-\Delta V_j
=-A_j\cdot\nabla V_j+C_jV_j,
\]

define on a fixed rescaled ball

\[
\bar V_j=\fint V_j,
\qquad
F_j=V_j-\bar V_j.
\]

Testing only against mean-zero test functions removes

1. the time derivative of the chosen spatial mean;
2. every spatially constant zero-order term acting on that mean;
3. in particular the constant linear reaction part `-r_j^2 I`.

The divergent mean returns only through

\[
\boxed{
(C_j-\bar C_j)\bar V_j.
}
\]

---

## 3. Correct mean-background coupling

The relevant dimensionless coupling is

\[
\boxed{
\Gamma_j(K,T)
=
\sup_{-T\le\tau\le0}
|\bar V_j(\tau)|
\,
\|C_j-\bar C_j\|_{L^\infty(B_K)}.
}
\]

Since

\[
C_j=r_j^2\Sigma_j-r_j^2I,
\]

this becomes

\[
\boxed{
\Gamma_j
\sim
\frac{|c_j|}{a_j}
\,
r_j^2\operatorname{osc}\Sigma_j.
}
\]

Thus

\[
\boxed{
\beta_j\to0
\not\Rightarrow
\Gamma_j\to0.
}
\]

Future frontier bookkeeping should use `Gamma_j`, not `beta_j`, as the sufficient coherent-mean decoupling criterion.

---

## 4. New coherent-mean gate

On a normalized-palinstrophy-quiet branch, Poincare bounds the mean-zero fluctuation locally in `L2` even when the raw normalized field decompactifies by constants.

Therefore

\[
\boxed{
G_{coherent\ ambient\ mean}
\Longrightarrow
H_{projected\ fluctuation\ compactness}
\lor
G_{mean\text{-}shear\ coupling}.
}
\]

If, on every fixed cylinder,

\[
A_j\to0,
\qquad
C_j\to0,
\qquad
\Gamma_j\to0,
\]

the projected fluctuation limit is caloric.

If `Gamma_j` does not vanish, the mean background is dynamically active through coefficient inhomogeneity and returns to the ambient/coefficient payer branch.

---

## 5. Current narrow frontier

The payer-free intrinsic line is now compressed to

\[
\boxed{
G_{nodal/subscale}
\lor H_{normalized\ palinstrophy}
\lor G_{scaled\ ambient/coefficient}
\lor G_{mean\text{-}shear\ coupling}
\lor H_{projected\ ancient\ caloric\ fluctuation}.
}
\]

The next useful calculation is not another raw mass estimate.

It is to determine whether the projected caloric fluctuation can inherit a global gradient/derivative growth condition strong enough for a Liouville theorem modulo spatial constants, or whether failure necessarily returns to normalized palinstrophy/ambient action.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
