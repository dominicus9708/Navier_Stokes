# Smooth Near-Floor Record Rigidity — 2026-08-20

Status: **SMOOTH-ONLY NEAR-FLOOR RIGIDITY / GLOBAL REGULARITY NOT PROVED.**

This note sharpens the common-core floor by quantifying what happens when a surviving core lies only slightly above the minimum radius forced by finite-stage record growth.

## 1. Record-growth lower rate and strain ceiling

On a persistent low-turnover smooth stage,

\[
L_I\le \Pi_V\frac{R_C^2}{\nu}
\]

when the moving variance core is contained in the common radius `R_C`. Hence some actual record-growth time satisfies

\[
\boxed{
 b\ge b_-(R_C):=
\frac{\nu\log q}{\Pi_VR_C^2}.
}
\]

Derivative quantile tightness and the analytic derivative bounds give

\[
Q\le
\frac{4\pi}{3(1-\varepsilon_Q)}K_1^2R_C^3.
\]

The Hardy--Biot--Savart strain estimate therefore gives

\[
\boxed{
\|\Sigma\|_\infty
\le
B_+(R_C)
:=
C_BK_2^{1/5}
\left[
\frac{4\pi}{3(1-\varepsilon_Q)}K_1^2R_C^3
\right]^{2/5},
}
\]

where

\[
C_B=\frac{15\sqrt2}{8}\pi^{-2/5}.
\]

Thus `B_+(R)` scales like `R^(6/5)`, while `b_-(R)` scales like `R^(-2)`.

## 2. Define the exact record-growth floor

Let `R_*` be the radius solving

\[
\boxed{B_+(R_*)=b_-(R_*).}
\]

This is exactly the eighth-power floor derived in `SMOOTH_RECORD_GROWTH_COMMON_CORE_FLOOR_2026-08-20.md`.

For

\[
\zeta=R_C/R_*\ge1,
\]

homogeneity gives the exact ratio

\[
\boxed{
\frac{B_+(R_C)}{b_-(R_C)}
=\zeta^{16/5}.
}
\]

## 3. Record-point headroom identity

At the selected actual record point `y_*`, let

\[
\xi=\Omega(y_*),
\qquad |\xi|=1,
\]

and let `s_3` be the largest eigenvalue of `Sigma(y_*)`. The smooth maximum-vorticity equation gives

\[
 b+\nu|\nabla\Omega(y_*)|^2
\le
\xi^T\Sigma(y_*)\xi.
\]

Define the alignment defect

\[
\boxed{
\delta_{align}
:=s_3-\xi^T\Sigma\xi\ge0.
}
\]

Since

\[
s_3\le\|\Sigma\|_\infty\le B_+(R_C)
\]

and `b>=b_-(R_C)`, one obtains

\[
\boxed{
\nu|\nabla\Omega(y_*)|^2
+\delta_{align}
\le
B_+(R_C)-b_-(R_C).
}
\]

Using the exact floor ratio,

\[
\boxed{
\nu|\nabla\Omega(y_*)|^2
+\delta_{align}
\le
b_-(R_C)
\left(\zeta^{16/5}-1\right).
}
\]

This is the near-floor rigidity law.

## 4. Separate consequences

Immediately,

\[
\boxed{
|\nabla\Omega(y_*)|^2
\le
\frac{\log q}{\Pi_VR_C^2}
\left(\zeta^{16/5}-1\right),
}
\]

and

\[
\boxed{
\delta_{align}
\le
b_-(R_C)
\left(\zeta^{16/5}-1\right).
}
\]

Relative to the maximal possible strain,

\[
\boxed{
\frac{\delta_{align}}{s_3}
\le
1-\zeta^{-16/5}
}
\]

whenever `s_3>=b_-`, as holds at the record point.

Thus the alignment defect vanishes linearly in `zeta-1` near the floor.

## 5. Extensional-axis angle on the middle-zero side

Suppose `s_3>s_2` and write the positive-middle spectrum as

\[
(-2m,m-d,m+d),
\qquad x=d/m.
\]

If `theta` is the angle between `xi` and the strongest extensional eigenvector `e_3`, then

\[
\delta_{align}
\ge
(s_3-s_2)\sin^2\theta.
\]

For the middle-zero-side sector `x>=x_*`,

\[
x_*=
\frac{3(\sqrt3-1)}4,
\]

we have

\[
\frac{s_3-s_2}{s_3}
=\frac{2x}{1+x}
\ge
\gamma_*
:=\frac{30-12\sqrt3}{13}
\approx0.7088761776.
\]

Hence

\[
\boxed{
\sin^2\theta
\le
\frac{1-\zeta^{-16/5}}{\gamma_*}.
}
\]

Thus the previously heuristic vorticity/extensional-axis alignment becomes quantitatively forced on a near-floor middle-zero record core.

## 6. Record-point H1 production density without exact alignment

Let

\[
G=\nabla\Omega.
\]

At a maximum of `|Omega|`,

\[
G\xi=0.
\]

In an eigenbasis of `Sigma`, the local H1 production density is

\[
n
=\frac12\sum_{k,i}(s_i-s_k)G_{ki}^2.
\]

For each row of `G`, the constraint `G xi=0` restricts that row to `xi^perp`. If

\[
\mu_\perp
=\max_{v\perp\xi,|v|=1}v^T\Sigma v,
\]

then

\[
n\le\frac12(\mu_\perp-s_1)|G|^2.
\]

Moreover,

\[
\mu_\perp
\le s_2+\delta_{align}.
\]

Therefore the exact useful upper bound is

\[
\boxed{
n^+
\le
\frac12
\left[(s_2-s_1)+\delta_{align}\right]
|\nabla\Omega|^2.
}
\]

For exact alignment this reduces to the previously derived `(s2-s1)/2` coefficient.

## 7. Meaning for the smooth external line

A core only slightly above `R_*` cannot independently choose

- a large record-point vorticity gradient;
- a large vorticity/strain misalignment;
- and unrestricted local H1 production geometry.

All three consume the same headroom `B_+-b_-`.

If the global H1 production is instead carried far from this rigid record core, that is a spatial separation of the record-growth and derivative-production cores and returns to the already typed turnover/remote-derivative lane.

Status: **THE COMMON-CORE FLOOR IS A RIGIDITY WALL, NOT MERELY A SIZE WALL. AS `R_C/R_* -> 1`, RECORD-POINT GRADIENT, ALIGNMENT DEFECT, AND THE ADMISSIBLE LOCAL H1 PRODUCTION GEOMETRY COLLAPSE TO A HIGHLY CONSTRAINED STATE.**