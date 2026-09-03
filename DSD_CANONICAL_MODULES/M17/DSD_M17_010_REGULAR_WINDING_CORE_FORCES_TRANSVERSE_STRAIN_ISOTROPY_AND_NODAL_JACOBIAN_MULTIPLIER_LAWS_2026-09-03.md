# DSD M17-010 — Regular winding core forces transverse strain isotropy and nodal-Jacobian multiplier laws

Date: 2026-09-03
Canonical ID: **M17-010**

Status: **INTERNAL REGULAR-NODAL DYNAMICS / AT A REGULAR CODIMENSION-TWO GREAT-CIRCLE WINDING ZERO, THE SURROUNDING VORTICITY DIRECTIONS APPROACH EVERY DIRECTION IN THE FIXED GREAT-CIRCLE PLANE. CONTINUITY OF THE CE-H STRAIN EIGENLINE THEREFORE FORCES THE NODAL-CORE STRAIN TO BE ISOTROPIC ON THAT PLANE, WITH SPECTRUM `(lambda,lambda,-2lambda)`. BECAUSE `W=0` ALSO KILLS THE ANTISYMMETRIC VELOCITY-GRADIENT PART, THE LINEARIZED VORTICITY JACOBIAN ALONG THE MATERIAL NODAL FILAMENT OBEYS EXACT COLUMN-WISE MULTIPLIER LAWS. A UNIFORMLY REGULAR RECURRENT FILAMENT WITH NONZERO HORIZONTAL JACOBIAN FORCES MEAN `kappa = 3/2`; IF A VERTICAL-DERIVATIVE COLUMN ALSO PERSISTS, IT FURTHER FORCES MEAN `lambda = 0`. THESE ARE NEW SIGNED RECURRENCE CONSTRAINTS, NOT YET A CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Regular winding zero and surjective direction limit

Work in the global great-circle frame of M17-003--009:

\[
W=(W_1,W_2,0),
\qquad n=e_3.
\]

Let `p` be a regular nodal point:

\[
W(p)=0,
\qquad
\operatorname{rank}(\nabla W_1(p),\nabla W_2(p))=2.
\]

The linear map

\[
G(p):=\nabla W(p):\mathbb R^3\to n^\perp
\]

has rank two. Hence its image is the entire great-circle plane `n^perp`.

Approaching `p` along suitable transverse directions therefore produces vorticity directions converging to **every** unit vector `e in n^perp`.

---

## 2. Strain isotropy on the great-circle plane

On the punctured active neighborhood,

\[
\Sigma W=\sigma W.
\]

Take a sequence approaching `p` along which

\[
\xi\to e,
\qquad e\in n^\perp,
\qquad |e|=1.
\]

By smoothness of `Sigma`, after passing to the limit,

\[
\Sigma(p)e=\lambda_e e.
\]

Because **every** direction in the two-dimensional plane is obtained this way, every direction in `n^perp` is an eigenvector of the symmetric matrix `Sigma(p)`.

The only symmetric linear map on a two-dimensional plane with every direction an eigenvector is a scalar multiple of the identity. Therefore

\[
\boxed{
\Sigma(p)|_{n^\perp}=\lambda I_2.
}
\]

Since

\[
\operatorname{tr}\Sigma=0,
\]

we also have

\[
\boxed{
\Sigma(p)n=-2\lambda n.
}
\]

Thus

\[
\boxed{
\operatorname{spec}\Sigma(p)=\{\lambda,\lambda,-2\lambda\}.
}
\]

This is exactly the repeated-eigenvalue strain geometry familiar from the axisymmetric no-swirl model, but it has been derived here solely from regular great-circle winding plus CE-H.

---

## 3. Velocity gradient at the nodal core

The antisymmetric part of the velocity gradient is determined by vorticity:

\[
\mathcal R_{ij}
=-\frac12\varepsilon_{ijk}W_k.
\]

At the nodal point,

\[
W(p)=0,
\]

so

\[
\boxed{\mathcal R(p)=0.}
\]

Hence

\[
\boxed{
\nabla U(p)=\Sigma(p)
=\operatorname{diag}(\lambda,\lambda,-2\lambda)
}
\]

in the great-circle frame.

For the similarity material velocity

\[
B=U+\frac12y,
\]

we have

\[
\boxed{
\nabla B(p)
=\operatorname{diag}
\left(
\lambda+\frac12,
\lambda+\frac12,
-2\lambda+\frac12
\right).
}
\]

---

## 4. Homogeneous vorticity equation through the regular zero

M17-007 gives an analytic extension of `kappa` through the regular nodal filament:

\[
\Delta W=\kappa W.
\]

Therefore locally

\[
D_BW
=\left(\nabla U+(\kappa-1)I\right)W.
\]

Set

\[
M:=\nabla U+(\kappa-1)I.
\]

At the nodal point, the action of `M` on the horizontal output plane is scalar:

\[
\boxed{
M|_{n^\perp}
=\left(\lambda+\kappa-1\right)I_2.
}
\]

---

## 5. Evolution of the nodal Jacobian

Let

\[
G_j:=\partial_jW
\]

be the three column vectors of the spatial Jacobian.

Differentiate the homogeneous equation. At `W=0`, the term `(partial_j M)W` vanishes, giving

\[
D_BG_j
=M G_j-\sum_k(\partial_jB_k)G_k.
\]

In the diagonal nodal-core frame of Section 3, this becomes column-wise.

For the two horizontal columns,

\[
\boxed{
D_BG_1
=\left(\kappa-\frac32\right)G_1,
}
\]

\[
\boxed{
D_BG_2
=\left(\kappa-\frac32\right)G_2.
}
\]

For the vertical derivative column,

\[
\boxed{
D_BG_3
=\left(3\lambda+\kappa-\frac32\right)G_3.
}
\]

These are exact at the regular material nodal filament.

---

## 6. Horizontal Jacobian determinant

Let `G_h` denote the `2 x 2` horizontal-output/horizontal-input block.

Then

\[
\boxed{
D_B G_h
=\left(\kappa-\frac32\right)G_h.
}
\]

Therefore

\[
\boxed{
D_B\log|\det G_h|
=2\kappa-3
}
\]

whenever `det G_h != 0`.

If the nodal filament is uniformly regular with

\[
0<c_G\le|\det G_h|\le C_G<\infty
\]

along a recurrent material branch, the mean logarithmic drift vanishes and

\[
\boxed{
\langle\kappa\rangle_{nodal}=\frac32.
}
\]

This reproduces, from a completely different nodal-Jacobian calculation, the critical `3/2` amplification rate that appeared earlier in the similarity replacement analysis.

---

## 7. Slanted-filament constraint

A regular nodal filament need not be parallel to `n=e_3`.

If its Jacobian uses a persistent nonzero vertical derivative column `G_3`, and if

\[
0<c_3\le|G_3|\le C_3
\]

along the recurrent branch, then

\[
\left\langle
3\lambda+\kappa-\frac32
\right\rangle=0.
\]

Together with

\[
\langle\kappa\rangle=\frac32
\]

from the horizontal regularity, this gives

\[
\boxed{
\langle\lambda\rangle_{nodal}=0.
}
\]

Thus a recurrent slanted regular nodal filament must have zero mean repeated-plane strain at its core.

By contrast, a purely vertical axisymmetric-style filament has `G_3=0` and need not satisfy this additional condition.

---

## 8. Branch classification

The regular material nodal branch therefore splits into

\[
\boxed{
R_{nodal}^{vertical-like}
\ \lor\ 
R_{nodal}^{slanted}.
}
\]

For every uniformly recurrent regular filament,

\[
\boxed{
\langle\kappa\rangle_{nodal}=\frac32.
}
\]

For the slanted class,

\[
\boxed{
\langle\lambda\rangle_{nodal}=0
}
\]

is additionally forced.

These are signed mean constraints on the zero-set skeleton, but the skeleton carries zero enstrophy weight. Therefore they do not contradict the global negative identity

\[
\int\kappa|W|^2=-P<0.
\]

They instead expose another sharp measure separation: the winding skeleton is a positive-`kappa` amplification structure while the enstrophy-weighted bulk remains dissipatively negative.

---

## 9. Next target

The new structural question is whether a compact recurrent CE-H field can sustain

\[
\boxed{
\langle\kappa\rangle_{nodal}=\frac32
}
\]

on every persistent winding filament while maintaining

\[
\boxed{
\int\kappa\rho^2=-P<0
}
\]

in the surrounding bulk.

This is a nodal-skeleton / bulk-sheath exchange problem analogous to, but sharper than, the earlier flux/enstrophy measure mismatch.

The axisymmetric no-swirl model shows that such a sign separation is not automatically contradictory; the missing step is to classify whether the non-axisymmetric recurrent geometry can realize it without nodal degeneracy or turnover.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
