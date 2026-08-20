# Exact Three-Axis H1 Covariance Tax — 2026-08-20

Overall status: **SHARPENED P_V DERIVATIVE-GEOMETRY REDUCTION — GLOBAL REGULARITY NOT PROVED.**

This note sharpens `PV_H1_EFFICIENCY_TAX_2026-08-20.md`. The deficit from the theoretical `7/9` H1 production cap splits exactly into two nonnegative geometric losses: compressive-axis underfill and leakage into the strongest extensional axis.

---

## 1. Strain eigenframe weights

Let

\[
s_1\le s_2\le s_3,
\qquad s_1+s_2+s_3=0,
\]

with orthonormal eigenvectors `e_1,e_2,e_3`. Define the diagonal weights of the combined gradient covariance

\[
c_i=e_i^T\overline C e_i.
\]

Since `Cbar` is positive semidefinite and trace one,

\[
c_i\ge0,
\qquad
c_1+c_2+c_3=1.
\]

Moreover

\[
c_i\le\lambda_{max}(\overline C)\le\frac79.
\]

The nonlinear H1 density is

\[
-3S:\overline C
=-3(s_1c_1+s_2c_2+s_3c_3).
\]

Off-diagonal entries of `Cbar` do not enter this contraction in the strain eigenframe.

---

## 2. Exact deficit decomposition

Set

\[
\delta_1=\frac79-c_1\ge0.
\]

Since

\[
c_2=1-c_1-c_3
=\frac29+\delta_1-c_3,
\]

we obtain

\[
\begin{aligned}
S:\overline C
={}&
\frac79s_1+rac29s_2
+\delta_1(s_2-s_1)
+c_3(s_3-s_2).
\end{aligned}
\]

Therefore

\[
\boxed{
-3S:\overline C
=
\frac13(5s_2+7s_3)
-3\delta_1(s_2-s_1)
-3c_3(s_3-s_2).
}
\]

This is an **exact identity**, not merely an upper bound.

---

## 3. The two positive taxes

Define

\[
\boxed{
\mathcal T_- 
=3\left(\frac79-c_1\right)(s_2-s_1)|\nabla S|^2
}
\]

and

\[
\boxed{
\mathcal T_+
=3c_3(s_3-s_2)|\nabla S|^2.
}
\]

Both are nonnegative. Hence the theoretical pointwise cap

\[
\frac13(5s_2+7s_3)|\nabla S|^2
\]

is attained only if all active taxes vanish.

The physical meaning is:

1. `T_-`: the derivative covariance fails to load the compressive eigendirection up to its universal `7/9` maximum;
2. `T_+`: derivative covariance leaks into the strongest extensional eigendirection rather than the middle eigendirection.

---

## 4. Strictly non-max-mid consequence

If

\[
s_3-s_2\ge g_+>0
\]

on a derivative-active region, near-maximal H1 production forces

\[
c_3\ll1.
\]

Thus in a fixed-gap positive-eigenvalue geometry the covariance must simultaneously satisfy

\[
\boxed{
c_1\approx\frac79,
\qquad
c_2\approx\frac29,
\qquad
c_3\approx0.
}
\]

The H1-efficient state is therefore not merely `compressively anisotropic`; it is a nearly rank-two, three-axis-locked covariance state.

This is stronger than the previous single-axis `7/9` requirement.

---

## 5. Max-mid specialization

For

\[
(s_1,s_2,s_3)=(-2m,m,m),
\]

the positive eigengap vanishes, so `T_+` vanishes identically. The exact density reduces to

\[
\boxed{
-3S:\overline C
=(4-9\delta_1)m.
}
\]

Thus the max-mid branch needs only the compressive covariance lock. This is consistent with the earlier max-mid rigidity/projection calculations, which separately constrain that geometry.

---

## 6. Exact saturation rigidity

If `s_2<s_3`, exact saturation of the theoretical H1 cap requires

\[
\boxed{
c_1=\frac79,
\qquad c_3=0,
\qquad c_2=\frac29.
}
\]

But `c_1=7/9` already forces saturation of the combined covariance cap. The previous rigidity theorem shows that exact `7/9` saturation forces a fixed-axis, effectively one-dimensional axisymmetric derivative geometry, incompatible with a nonzero whole-space finite-energy strain field.

Therefore the theoretical H1 cap is not attained by a nontrivial finite-energy tight core.

---

## 7. Integrated ledger

Define

\[
\mathcal D_-
=3\int
\left(\frac79-c_1\right)(s_2-s_1)|\nabla S|^2dx,
\]

\[
\mathcal D_+
=3\int
c_3(s_3-s_2)|\nabla S|^2dx.
\]

Then

\[
\boxed{
-\langle\mathcal R_{VI},-\Delta S\rangle
+\mathcal D_-+\mathcal D_+
=
\frac13\int(5s_2+7s_3)|\nabla S|^2dx.
}
\]

Thus the normalized first-hitting H1 ledger may be written schematically as

\[
\frac12P_\Sigma'
+\frac32aP_\Sigma
+\nu H_\Sigma
+\mathcal D_-+\mathcal D_+
=
\frac13\int(5s_2+7s_3)|\nabla\Sigma|^2dy.
\]

The two covariance defects therefore behave as explicit positive damping terms in the derivative budget.

---

## 8. New reduced alternatives

For a recurrent non-H/T P_V core, efficient H1 replenishment now requires one of two highly constrained geometries:

1. **near-max-mid:** `s_3-s_2` is small, so the extensional leakage tax is weak; this branch is already constrained by the max-mid projection-kernel/defect results;
2. **fixed positive eigengap:** `s_3-s_2 >= g_+`, forcing the full covariance lock `(7/9,2/9,0)` in the strain eigenframe if production is near maximal.

Failure of that three-axis lock creates a definite positive H1 tax.

The next target is a quantitative rigidity theorem for the near `(7/9,2/9,0)` covariance state, including off-diagonal covariance and eigenframe motion. The expected exit channels remain derivative concentration `H`, spatial turnover/non-tightness `T`, or projective eigenframe reorganization.

Status: **THE H1 EFFICIENCY DEFICIT HAS AN EXACT TWO-TAX DECOMPOSITION. NON-MAX-MID EFFICIENT P_V RECURRENCE REQUIRES A NEARLY RANK-TWO `(7/9,2/9,0)` COVARIANCE LOCK IN THE STRAIN EIGENFRAME. GLOBAL REGULARITY REMAINS UNPROVED.**