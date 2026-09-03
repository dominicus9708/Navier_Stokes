# DSD M16-024 — Collapse axial strain PDE channels to same-tube direction geometry

Date: 2026-09-03
Canonical ID: **M16-024**

Status: **INTERNAL GEOMETRIC COLLAPSE / THE TWO SAME-TUBE PDE CHANNELS OF M16-023 ARE NOT INDEPENDENT ONCE `W = rho xi` AND `div W = 0` ARE USED. THE AXIAL STRAIN DERIVATIVE SATISFIES AN EXACT DIRECTOR-FIELD IDENTITY, SO POSITIVE-DENSITY SAME-TUBE STRAIN HETEROGENEITY FORCES A POSITIVE-DENSITY DIRECTION-GRADIENT EVENT ON THAT SAME MATERIAL TUBE. THIS SPLITS INTO VORTEX-LINE CURVATURE, WHICH RECONNECTS TO THE M13 CURVATURE/FLUX REPLACEMENT MECHANISM, OR TRANSVERSE DIRECTOR DEFORMATION, WHICH IS THE NEW RESIDUAL SAME-TUBE GEOMETRIC BRANCH / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Start from M16-023

M16-023 gives

\[
\boxed{
W\cdot\nabla\sigma
=
\Sigma:\nabla W
-\frac12W\cdot(\nabla\times W).
}
\]

Write

\[
W=\rho\xi,
\qquad |\xi|=1.
\]

We now resolve both terms on the right using the director field `xi`.

---

## 2. Resolve the strain--derivative contraction

Since

\[
\partial_iW_j
=(\partial_i\rho)\xi_j
+\rho\partial_i\xi_j,
\]

and

\[
\Sigma\xi=\sigma\xi,
\]

we obtain

\[
\Sigma:\nabla W
=
\sigma\,\xi\cdot\nabla\rho
+\rho\,\Sigma:\nabla\xi.
\]

The divergence-free condition gives

\[
0=\nabla\cdot(\rho\xi)
=\xi\cdot\nabla\rho+\rho\nabla\cdot\xi,
\]

hence

\[
\frac{\xi\cdot\nabla\rho}{\rho}
=-\nabla\cdot\xi.
\]

Therefore

\[
\boxed{
\frac1\rho\Sigma:\nabla W
=
-\sigma\nabla\cdot\xi
+\Sigma:\nabla\xi.
}
\]

---

## 3. Resolve vorticity self-helicity

Because

\[
\nabla\times W
=\nabla\rho\times\xi
+\rho\nabla\times\xi,
\]

we have

\[
W\cdot\nabla\times W
=
\rho^2\xi\cdot\nabla\times\xi.
\]

Define the director twist

\[
\boxed{
\tau_\xi
:=\xi\cdot\nabla\times\xi.
}
\]

Then

\[
\boxed{
\frac1\rho W\cdot\nabla\times W
=\rho\tau_\xi.
}
\]

---

## 4. Exact axial-strain/director identity

Divide the M16-023 identity by `rho` and combine Sections 2--3:

\[
\xi\cdot\nabla\sigma
=
-\sigma\nabla\cdot\xi
+\Sigma:\nabla\xi
-\frac\rho2\tau_\xi.
\]

Equivalently,

\[
\boxed{
\xi\cdot\nabla\sigma
=
(\Sigma-\sigma I):\nabla\xi
-\frac\rho2\,\xi\cdot\nabla\times\xi.
}
\]

This is the canonical same-tube strain-heterogeneity identity.

---

## 5. Direction-gradient floor

On the fixed active core,

\[
|\Sigma|\le S_*,
\qquad
0<\rho\le M_*.
\]

Also

\[
|\xi\cdot\nabla\times\xi|
\le C|\nabla\xi|.
\]

Therefore

\[
|\xi\cdot\nabla\sigma|
\le
C_{dir}|\nabla\xi|,
\]

where `C_dir` depends only on the compact-hull upper caps.

M16-022 gives a positive-density linewise axial strain-variation charge. Hence on that same tube family one obtains a positive-density event with

\[
\boxed{
|\nabla\xi|\ge d_\xi>0.
}
\]

After the usual smooth thickening this yields a coherent same-tube direction-gradient packet.

Thus

\[
\boxed{
P_1^{\rm axial\ het}
\Longrightarrow
P_{dir}^{\rm same\ tube}.
}
\]

---

## 6. Curvature versus transverse director deformation

Choose an orthonormal frame with first vector `xi`. Then

\[
|\nabla\xi|^2
=
|(\xi\cdot\nabla)\xi|^2
+
|\nabla_{\xi^\perp}\xi|^2.
\]

Define vortex-line curvature

\[
\mathcal K=(\xi\cdot\nabla)\xi.
\]

Therefore a same-tube direction-gradient floor implies

\[
\boxed{
|\mathcal K|\ge\frac{d_\xi}{\sqrt2}
\quad\lor\quad
|\nabla_{\xi^\perp}\xi|
\ge\frac{d_\xi}{\sqrt2}.
}
\]

Call the branches

\[
\boxed{B_{curv}^{same}}
\]

and

\[
\boxed{B_{trans-dir}^{same}}.
\]

---

## 7. Curvature branch reconnects to M13/M16-001--003

For a persistent material vortex line, M13 / M16-001--003 gives the exact curvature/flux similarity law. In particular a fixed material flux label cannot carry a fixed-strength curvature packet indefinitely without label renewal/turnover; the physical-variable audit prevents interpreting the similarity factor as artificial dissipation but retains the finite-label recurrence obstruction.

Hence

\[
\boxed{
B_{curv}^{same}
\Longrightarrow
T_{curv/label}
}

within the already audited finite-genealogy framework.

The only genuinely new same-tube geometric survivor is therefore

\[
\boxed{B_{trans-dir}^{same}}.
\]

---

## 8. Updated canonical branch tree

Combining M16-021--024,

\[
\boxed{
\text{negative enstrophy-weighted `kappa`}
\Longrightarrow
B_{\rm flux}^{-}
\ \lor\ 
T_{\rm marker/sheath}
\ \lor\ 
T_{curv/label}
\ \lor\ 
B_{trans-dir}^{same}.
}
\]

Three of the four branches are already signed material-resource / turnover mechanisms.

The final same-tube no-turnover geometric branch is now specifically

\[
\boxed{
B_{trans-dir}^{same}:
\quad
|\nabla_{\xi^\perp}\xi|\ge d_*>0
}
\]

on a positive-density family of recurrent material tubes.

The next target is to derive the material evolution of the transverse director-gradient tensor and determine whether it admits a flux-neutral recurrent cycle or instead forces strain-sheet deformation / replacement.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
