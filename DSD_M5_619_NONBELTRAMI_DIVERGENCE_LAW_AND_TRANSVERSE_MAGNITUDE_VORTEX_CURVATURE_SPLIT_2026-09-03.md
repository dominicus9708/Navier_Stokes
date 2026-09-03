# DSD M5-619 — Non-Beltrami divergence law and transverse-magnitude / vortex-curvature split

Date: 2026-09-03

Status: **INTERNAL GEOMETRIC DECOMPOSITION / THE M5-618 NON-BELTRAMI VECTOR `J_B=W x curl W` OBEYS THE EXACT SIGNED DIVERGENCE LAW `div J_B = |curl W|^2 + W·Delta W`, WHICH ON CE-H IS `|curl W|^2 + kappa|W|^2` AND GLOBALLY REPRODUCES THE RAYLEIGH IDENTITY / WRITING `W=rho xi` GIVES `J_B = rho P_perp nabla rho - rho^2 (xi·nabla)xi`, SO THE UNIFORM NON-BELTRAMI GAP FORCES EITHER A TRANSVERSE MAGNITUDE-GRADIENT CHARGE OR A VORTEX-LINE CURVATURE CHARGE / THE EXACT BELTRAMI ESCAPE IS THEREFORE REPLACED BY A MANDATORY FINITE GEOMETRIC BENDING/TRANSVERSE-AMPLITUDE CHANNEL / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Non-Beltrami vector

Let

\[
C:=\nabla\times W,
\]

and

\[
\boxed{J_B:=W\times C.}
\]

M5-618 gives a uniform compact-hull lower bound

\[
\boxed{\|J_B\|_2\ge b_*>0.}
\]

---

## 2. Exact divergence identity

Use

\[
\nabla\cdot(A\times B)
=B\cdot(\nabla\times A)-A\cdot(\nabla\times B).
\]

With `A=W`, `B=C=curl W`,

\[
\nabla\cdot J_B
=|C|^2-W\cdot(\nabla\times C).
\]

Since

\[
\nabla\times C
=\nabla\times\nabla\times W
=\nabla(\nabla\cdot W)-\Delta W
=-\Delta W,
\]

we obtain

\[
\boxed{
\nabla\cdot J_B
=|\nabla\times W|^2+W\cdot\Delta W.
}
\]

On the CE-H active set,

\[
W\cdot\Delta W=\kappa|W|^2,
\]

so

\[
\boxed{
\nabla\cdot J_B
=|C|^2+\kappa|W|^2.
}
\]

The product form is globally meaningful across the nodal set.

---

## 3. Whole-space audit

The terminal tail gives

\[
W=O(r^{-2}),
\qquad
C=O(r^{-3}),
\]

hence

\[
J_B=O(r^{-5}).
\]

Therefore the flux at infinity vanishes:

\[
\int_{S_R}J_B\cdot n\,dS=O(R^{-3})\to0.
\]

Integrating the divergence identity gives

\[
\int|C|^2dy
+
\int W\cdot\Delta Wdy
=0.
\]

For divergence-free whole-space `W`,

\[
\|C\|_2^2=\|\nabla W\|_2^2=P,
\]

while

\[
\int W\cdot\Delta W=-P.
\]

Thus the law is exactly consistent with the CE-H Rayleigh balance.

No new global contradiction is obtained by integrating it over all space.

---

## 4. Magnitude-direction decomposition

Write

\[
W=\rho\xi,
\qquad |\xi|=1.
\]

Then

\[
C
=\nabla\rho\times\xi
+
\rho\,\nabla\times\xi.
\]

Hence

\[
J_B
=\rho\xi\times(\nabla\rho\times\xi)
+
\rho^2\xi\times(\nabla\times\xi).
\]

The first term is

\[
\xi\times(\nabla\rho\times\xi)
=
\nabla\rho-(\xi\cdot\nabla\rho)\xi
=P_\xi^\perp\nabla\rho.
\]

For a unit vector field,

\[
(\xi\cdot\nabla)\xi
=
-\xi\times(\nabla\times\xi).
\]

Therefore

\[
\boxed{
J_B
=
\rho P_\xi^\perp\nabla\rho
-
\rho^2(\xi\cdot\nabla)\xi.
}
\]

---

## 5. Vortex-line curvature interpretation

Where the vortex line is parametrized by arclength with unit tangent `xi`,

\[
\boxed{
\mathcal K_\xi
:=(\xi\cdot\nabla)\xi
}
\]

is its curvature vector.

It is perpendicular to `xi`.

Thus

\[
\boxed{
J_B
=
\text{transverse magnitude force}
-
\text{vortex-line curvature force}.
}
\]

---

## 6. Uniform channel split

By the triangle inequality,

\[
b_*
\le
\|\rho P_\xi^\perp\nabla\rho\|_2
+
\|\rho^2\mathcal K_\xi\|_2.
\]

Therefore every marked CE-H state satisfies at least one of

\[
\boxed{
\|\rho P_\xi^\perp\nabla\rho\|_2
\ge\frac12b_*,
}
\]

or

\[
\boxed{
\|\rho^2\mathcal K_\xi\|_2
\ge\frac12b_*.
}
\]

These are stronger weighted subchannels than the unweighted statements `P_mag>0` and `P_dir>0`.

---

## 7. Relation to existing derivative charges

Using the compact vorticity amplitude cap `rho<=M0`,

\[
\|\rho P_\xi^\perp\nabla\rho\|_2
\le
M_0 P_{mag}^{1/2},
\]

and

\[
\|\rho^2\mathcal K_\xi\|_2
\le
M_0 P_{dir}^{1/2}.
\]

Thus the M5-618 gap is compatible with M5-613--614, but it says more: at least one derivative channel must be genuinely transverse to the vortex-line foliation.

A field with purely along-line magnitude variation and zero vortex curvature would fall into the excluded Beltrami class.

---

## 8. Local signed form

For every bounded domain `Omega`,

\[
\boxed{
\int_\Omega
\left(
|C|^2+W\cdot\Delta W
\right)dy
=
\int_{\partial\Omega}J_B\cdot n\,dS.
}
\]

Thus local mismatch between curl energy and viscous Rayleigh density is transported by the non-Beltrami vector through the boundary.

This gives a signed spatial flux law that can be localized to the finite persistent core.

---

## 9. Updated CE-H geometry

A surviving CE-H state must now carry simultaneously:

1. negative enstrophy-weighted kappa mean;
2. positive radial kappa virial;
3. zero-net generalized kappa force with a separated force dipole;
4. both magnitude and direction Dirichlet floors;
5. a uniform non-Beltrami defect;
6. therefore a fixed transverse-magnitude or vortex-curvature charge.

The next calculation should test the material evolution of the curvature/transverse-magnitude split, because vortex lines themselves are material on CE-H.

---

## 10. Firewall

The two terms in the decomposition of `J_B` are not orthogonal in general, so no exact Pythagorean split is claimed.

The conclusion is the robust dichotomy obtained from the triangle inequality only.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
