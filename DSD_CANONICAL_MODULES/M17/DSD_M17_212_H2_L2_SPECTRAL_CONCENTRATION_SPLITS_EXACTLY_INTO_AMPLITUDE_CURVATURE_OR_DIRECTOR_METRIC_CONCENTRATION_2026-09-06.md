# DSD M17-212 — H2/L2 spectral concentration splits exactly into amplitude curvature or director-metric concentration

Date: 2026-09-06  
Canonical ID: **M17-212**

Status: **SPECTRAL-GEOMETRIC SPLIT / WRITING `W=rho xi` IN THE CE-H EIGEN-RELATION AND PROJECTING PARALLEL/PERPENDICULAR TO `xi` GIVES THE EXACT SCALAR LAW `kappa = Delta rho/rho - |grad xi|^2` AND THE DIRECTOR EQUATION `Delta xi + 2 grad log rho dot grad xi + |grad xi|^2 xi = 0`. CONSEQUENTLY `kappa^2 rho^2 = (Delta rho - rho |grad xi|^2)^2`. THE M17-210/211 HARD SPECTRAL EXIT `Lambda_R -> infinity` CAN THEREFORE OCCUR ONLY THROUGH LARGE NORMALIZED AMPLITUDE CURVATURE OR LARGE DIRECTOR METRIC, UP TO THEIR SIGNED CANCELLATION. POSITIVE LARGE KAPPA NECESSARILY REQUIRES POSITIVE AMPLITUDE CURVATURE STRONG ENOUGH TO OVERCOME THE NONNEGATIVE DIRECTOR METRIC. NEGATIVE LARGE KAPPA MAY BE PAID BY DIRECTOR-METRIC GROWTH OR NEGATIVE AMPLITUDE CURVATURE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Parallel/perpendicular decomposition

Write

\[
W=\rho\xi,
\qquad
|\xi|=1.
\]

Then

\[
\Delta W
=(\Delta\rho)\xi
+2\partial_i\rho\,\partial_i\xi
+\rho\Delta\xi.
\]

Since

\[
\xi\cdot\partial_i\xi=0
\]

and

\[
\xi\cdot\Delta\xi=-|\nabla\xi|^2,
\]

the parallel projection of

\[
\Delta W=\kappa\rho\xi
\]

gives

\[
\boxed{
\Delta\rho-\rho|\nabla\xi|^2
=\kappa\rho.
}
\]

Thus

\[
\boxed{
\kappa=\frac{\Delta\rho}{\rho}-|\nabla\xi|^2
}
\]

on the active set.

---

## 2. Perpendicular director equation

Subtract the parallel part from the vector equation:

\[
2\nabla\rho\cdot\nabla\xi
+\rho\left(\Delta\xi+|\nabla\xi|^2\xi\right)=0.
\]

Dividing by `rho>0`,

\[
\boxed{
\Delta\xi
+2\nabla\log\rho\cdot\nabla\xi
+|\nabla\xi|^2\xi
=0.
}
\]

Thus the perpendicular second derivative is not an independent free jet; it is locked to amplitude gradient and the director metric.

---

## 3. Exact spectral-density formula

M17-210 gives

\[
|\Delta W|^2=\kappa^2\rho^2.
\]

Using the scalar law,

\[
\boxed{
\kappa^2\rho^2
=\left(\Delta\rho-\rho|\nabla\xi|^2\right)^2.
}
\]

Hence the shell spectral ratio is

\[
\boxed{
\Lambda_R^2
=\frac{
\int_{C_R}(\Delta\rho-\rho|\nabla\xi|^2)^2dy
}{
\int_{C_R}\rho^2dy
}.
}
\]

---

## 4. Quantitative two-channel upper decomposition

Elementary algebra gives

\[
(a-b)^2\le2a^2+2b^2.
\]

Therefore

\[
\boxed{
\int\kappa^2\rho^2
\le
2\int|\Delta\rho|^2
+2\int\rho^2|\nabla\xi|^4.
}
\]

Consequently, if `Lambda_R -> infinity`, at least one normalized charge must diverge along a subsequence:

\[
\boxed{
\frac{\int_{C_R}|\Delta\rho|^2}{E_R}
\to\infty
}
\]

or

\[
\boxed{
\frac{\int_{C_R}\rho^2|\nabla\xi|^4}{E_R}
\to\infty.
}
\]

Otherwise the right-hand side would keep `Lambda_R` bounded.

Thus

\[
\boxed{
G_{H2/L2\ spectral}
\Longrightarrow
G_{amplitude\ curvature}
\lor
G_{director\ metric^2}.
}
\]

---

## 5. Pointwise sign split

If

\[
\kappa(x)=K>0,
\]

then

\[
\boxed{
\frac{\Delta\rho}{\rho}
=K+|\nabla\xi|^2
\ge K.
}
\]

So positive high kappa necessarily comes from positive normalized amplitude curvature; director geometry can only increase the required curvature.

If

\[
\kappa(x)=-K<0,
\]

then

\[
\boxed{
|\nabla\xi|^2-\frac{\Delta\rho}{\rho}=K.
}
\]

Hence at least one of

\[
\boxed{|\nabla\xi|^2\ge K/2}
\]

or

\[
\boxed{-\Delta\rho/\rho\ge K/2}
\]

must hold.

This gives a sign-sensitive refinement of the RMS split.

---

## 6. Relation to Rank-2 director area

For the director map in three dimensions, if its two nonzero singular values are `s1,s2`,

\[
|J_\xi|=s_1s_2,
\qquad
|\nabla\xi|^2=s_1^2+s_2^2,
\]

so

\[
\boxed{2|J_\xi|\le|\nabla\xi|^2.}
\]

A lower bound on director-area current therefore gives a baseline director metric, but **large** `|grad xi|^2` can still occur through anisotropy (`s1>>s2`) without a corresponding large product.

Thus the director-metric spectral branch is naturally routed to an anisotropy/rank-degeneration audit rather than being identified with large director-area flux.

---

## 7. DSD audit

- The split is exact on `rho>0`; no scalar kappa formula is extended through nodes.
- Large director metric and large amplitude curvature can partially cancel in kappa; the implication used is only that large `|kappa|` forces at least one to be large.
- `|grad xi|^4` occupancy is not yet a finite cumulative cost.
- The positive and negative kappa mechanisms are structurally different and should not be merged.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
