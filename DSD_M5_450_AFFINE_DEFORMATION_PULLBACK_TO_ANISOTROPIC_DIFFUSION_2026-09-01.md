# DSD M5-450 — Pullback of the matched affine strain to a time-dependent anisotropic diffusion metric

Date: 2026-09-01

Status: **EXACT STRUCTURAL REDUCTION OF THE M5-449 INNER HARD EQUATION / LET `F'=AF`, `det F=1`, AND PULL BACK BOTH SPACE AND VECTOR COMPONENTS BY THE OUTER AFFINE DEFORMATION / IN VORTICITY FORM THE EXPLICIT AFFINE TRANSPORT `Az.grad Omega` AND AFFINE STRETCH `A Omega` CANCEL EXACTLY / THE MATCHED INNER EQUATION BECOMES THE ORDINARY VORTICITY-STRETCHING EQUATION WITH A SPATIALLY HOMOGENEOUS TIME-DEPENDENT DIFFUSION TENSOR `G=F^-1 F^-T`, `det G=1` / THUS THE REMOTE AFFINE SOURCE IS EQUIVALENT TO AN ANISOTROPIC DIFFUSION METRIC: BOUNDED AFFINE DEFORMATION GIVES UNIFORMLY ELLIPTIC ANISOTROPIC NAVIER--STOKES, WHILE UNBOUNDED DEFORMATION GIVES METRIC DEGENERACY AND AN EXPLICIT STRONG AFFINE-DEFORMATION BRANCH / THIS DOES NOT SOLVE EITHER 3D NONLINEAR HARD CORE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Matched strained inner equation

M5-449 derives the inner vorticity equation

\[
\boxed{
\partial_\tau\Omega
+(v+Az)\cdot\nabla_z\Omega
=(\nabla_zv+A)\Omega
+\Delta_z\Omega,
}
\]

where

\[
A(\tau)=A(\tau)^T,
\qquad
\operatorname{tr}A(\tau)=0.
\]

The matrix `A` is the leading affine strain induced on the inner first-hitting core by the bounded outer Euler source.

---

## 2. Affine deformation matrix

Let `F(tau)` solve

\[
\boxed{
F'=AF,
\qquad
F(0)=I.
}
\]

Jacobi's determinant identity gives

\[
\frac d{d\tau}\det F
=\operatorname{tr}(A)\det F=0.
\]

Hence

\[
\boxed{\det F(\tau)=1.}
\]

Thus the outer affine coordinate deformation is volume preserving.

---

## 3. Pull back space and velocity

Define

\[
\boxed{
z=F(\tau)y}
\]

and the pulled-back perturbation velocity

\[
\boxed{
v(z,\tau)=F(\tau)\widetilde v(y,\tau).}
\]

Since `F` is spatially constant and `det F=1`,

\[
\nabla_z\cdot v=0
\quad\Longleftrightarrow\quad
\nabla_y\cdot\widetilde v=0.
\]

The curl transformation under a volume-preserving linear map is

\[
\boxed{
\Omega(z,\tau)
=F(\tau)\eta(y,\tau),
\qquad
\eta=\nabla_y\times\widetilde v.
}
\]

---

## 4. Exact cancellation of affine transport and affine stretching

At fixed physical `z`,

\[
y=F^{-1}z
\]

satisfies

\[
\partial_\tau y
=-F^{-1}F'y
=-F^{-1}AFy.
\]

For

\[
\Omega=F\eta,
\]

the time derivative is

\[
\partial_\tau\Omega
=AF\eta
+F\partial_\tau\eta
-F\left[
(F^{-1}AFy)\cdot\nabla_y\eta
\right].
\]

The affine transport term is

\[
(Az\cdot\nabla_z)\Omega
=F\left[
(F^{-1}AFy)\cdot\nabla_y\eta
\right].
\]

Therefore

\[
\boxed{
\partial_\tau\Omega
+(Az\cdot\nabla_z)\Omega
=AF\eta+F\partial_\tau\eta.
}
\]

The first term on the right is exactly

\[
A\Omega=AF\eta,
\]

which appears as the affine stretching term on the right side of the original vorticity equation.

Hence the affine transport and affine stretch cancel from the pulled-back equation.

---

## 5. Nonlinear terms transform covariantly

Because

\[
v=F\widetilde v,
\]

and

\[
\nabla_z\Omega
=F(\nabla_y\eta)F^{-1},
\]

one has

\[
\boxed{
(v\cdot\nabla_z)\Omega
=F(\widetilde v\cdot\nabla_y)\eta.
}
\]

Also

\[
\nabla_zv
=F(\nabla_y\widetilde v)F^{-1},
\]

so

\[
\boxed{
(\nabla_zv)\Omega
=F(\nabla_y\widetilde v)\eta.
}
\]

Thus the nonlinear vortex-advection/stretching pair retains exactly its standard algebraic form.

---

## 6. Diffusion becomes anisotropic

Let

\[
\boxed{
G(\tau)
:=F^{-1}(\tau)F^{-T}(\tau).
}
\]

Since `F` is spatially homogeneous,

\[
\boxed{
\Delta_z(F\eta)
=F\nabla_y\cdot(G\nabla_y\eta).
}
\]

Therefore dividing the pulled-back equation by `F` gives

\[
\boxed{
\partial_\tau\eta
+(\widetilde v\cdot\nabla_y)\eta
=(\nabla_y\widetilde v)\eta
+\nabla_y\cdot(G(\tau)\nabla_y\eta).
}
\]

This is the standard 3D vorticity advection/stretching equation with a time-dependent, spatially homogeneous anisotropic viscosity tensor.

Moreover

\[
\boxed{
G=G^T>0,
\qquad
\det G=(\det F)^{-2}=1.
}
\]

---

## 7. Enstrophy identity in the pulled-back frame

Because `div tilde v=0`, multiplying by `eta` gives

\[
\boxed{
\frac12\frac d{d\tau}\|\eta\|_2^2
+
\int
(\nabla\eta)^TG(\tau)(\nabla\eta)dy
=
\int
\eta\cdot(\nabla\widetilde v)\eta\,dy.
}
\]

The explicit outer affine stretching has disappeared.

Its only direct trace is the anisotropic diffusion metric `G`.

Thus the outer source does not add a fundamentally new vorticity-stretching algebra; it changes the geometry in which viscosity acts.

---

## 8. Bounded-deformation branch

Let the singular values of `F` be

\[
\sigma_1\ge\sigma_2\ge\sigma_3>0,
\qquad
\sigma_1\sigma_2\sigma_3=1.
\]

The eigenvalues of `G` are

\[
\sigma_1^{-2},
\quad
\sigma_2^{-2},
\quad
\sigma_3^{-2}.
\]

If the affine deformation condition number remains bounded on the relevant ancient/stage intervals,

\[
\boxed{
\kappa(F)=\sigma_1/\sigma_3\le K_F<\infty,
}
\]

then, since `det F=1`, all singular values stay between fixed positive constants.

Consequently

\[
\boxed{
c_FI\le G(\tau)\le C_FI.}
\]

The pulled-back system has uniformly elliptic anisotropic diffusion.

This is still a genuinely three-dimensional Navier--Stokes-type critical problem; uniform ellipticity alone does not prove global regularity.

The gain is that bounded remote affine strain no longer needs a separate geometric branch.

---

## 9. Unbounded-deformation branch

If

\[
\boxed{
\kappa(F(\tau_j))\to\infty,
}
\]

then `G` becomes increasingly anisotropic:

\[
\lambda_{min}(G)\to0
\quad\text{or}\quad
\lambda_{max}(G)\to\infty
\]

while

\[
\det G=1.
\]

This is a precise metric-degeneracy manifestation of accumulated affine deformation.

It belongs to a strong deformation/axis branch rather than an unformed remote-source branch:

\[
\boxed{
H_{affine\ deformation}^{strong}.
}
\]

No contradiction is claimed: anisotropic degeneracy may be compatible with a hypothetical singular tower.

---

## 10. New hard split for the bounded outer-Euler branch

Combining M5-449 and M5-450,

\[
\boxed{
E_{outer}^{bounded\ Euler}
\Longrightarrow
\begin{cases}
H_{affine\ deformation}^{strong},
&\kappa(F)\to\infty,\\[1mm]
N_{uniform\ elliptic}^{anisotropic},
&\sup\kappa(F)<\infty.
\end{cases}
}
\]

The second object is not a new physical equation class in the sense of source formation; it is the original nonlinear vortex-stretching problem expressed in a bounded time-dependent volume-preserving metric.

---

## 11. DSD interpretation

The remote outer source has now been separated into two roles:

1. **formation/source role** — create the affine matrix `A(tau)`;
2. **metric role** — after following the affine flow, `A` is encoded entirely in `G=F^-1F^-T`.

This prevents counting outer strain both as explicit stretching and as deformation of the diffusive geometry.

It also makes clear where the remaining difficulty lives: nonlinear self-stretching of the inner vorticity under critical 3D dynamics, possibly with a degenerating anisotropic metric.

---

## 12. Firewall

Uniformly elliptic anisotropic viscosity does **not** solve the 3D Navier--Stokes global regularity problem.

Unbounded `kappa(F)` is also not automatically impossible.

No theorem has been proved that converts the fixed positive first-hitting `A`-action into monotone growth of `kappa(F)`; time-dependent strain axes can partially undo earlier deformation.

Therefore do not infer

\[
\text{remote affine source}\Rightarrow\text{contradiction}.
\]

---

## 13. Current value of the reduction

The M5-449 matched hard equation is no longer an opaque coupled outer/inner object.

After the exact affine pullback, its inner core is either:

\[
\boxed{
\text{standard vortex stretching with uniformly elliptic anisotropic diffusion}
}
\]

or

\[
\boxed{
\text{strong metric/deformation degeneracy}.
}
\]

This is the correct point for the next critical-element/rigidity audit.

---

## 14. Audit verdict

### Exact derived identity

\[
\boxed{
\partial_\tau\eta
+(\widetilde v\cdot\nabla)\eta
=(\nabla\widetilde v)\eta
+\nabla\cdot(G\nabla\eta),
\quad
G=F^{-1}F^{-T},
\quad
\det G=1.
}
\]

### Remaining split

\[
\boxed{
H_{affine\ deformation}^{strong}
\lor
N_{uniform\ elliptic}^{anisotropic}.
}
\]

### Still open

- rigidity of the uniformly elliptic anisotropic critical element;
- exclusion of metric degeneracy;
- strong multiscale source-scale enstrophy branch;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
