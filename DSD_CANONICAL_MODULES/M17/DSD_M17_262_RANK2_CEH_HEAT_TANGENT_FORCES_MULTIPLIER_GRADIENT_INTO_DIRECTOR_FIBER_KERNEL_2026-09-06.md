# DSD M17-262 — Rank-2 CE-H heat tangent forces the multiplier gradient into the director-fiber kernel

Date: 2026-09-06  
Canonical ID: **M17-262**

Status: **RAW-TANGENT GEOMETRIC RIGIDITY / M17-260 SHOWS THAT A RAW NON-SPIKING CE-H HEAT TANGENT SATISFIES BOTH `partial_tau V=Delta V` AND `Delta V=K V`, SO ITS UNIT DIRECTION `xi=V/|V|` IS TIME-INDEPENDENT. WRITING `V=a xi` AND PROJECTING THE HEAT EQUATION PERPENDICULAR TO `xi` GIVES THE EXACT STATIC DIRECTOR CONSTRAINT `2 D_{grad log a} xi + P_xi^perp Delta xi = 0`. DIFFERENTIATING IN TIME AND USING `partial_tau log a=K` YIELDS `D_{grad K} xi=0`. ON THE RANK-2 DIRECTOR BRANCH, `ker D xi` IS ONE-DIMENSIONAL, SO `grad K` MUST LIE ALONG THE DIRECTOR-FIBER TANGENT. THUS THE SCALED MULTIPLIER IS CONSTANT IN BOTH TRANSVERSE DIRECTOR-CHANGING DIRECTIONS AND CAN VARY ONLY ALONG THE ONE-DIMENSIONAL FIBER. THIS REDUCES THE RAW CALORIC CE-H SURVIVOR TO A FIBERWISE COEFFICIENT GEOMETRY; RANK LOSS REMAINS AN EXPLICIT EXIT. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M17-260

On the raw mass-compact non-spike tangent branch,

\[
\boxed{
\partial_\tau V=\Delta V=K V.
}
\]

On the active set `V!=0`, write

\[
\boxed{
V(z,\tau)=a(z,\tau)\xi(z),
\qquad
|\xi|=1.
}
\]

M17-260 gives

\[
\boxed{\partial_\tau\xi=0.}
\]

The sign of `a` may be absorbed locally into `xi`; the identities below are applied on one active sign component.

---

## 2. Expand the heat equation

Because `xi` is independent of `tau`,

\[
\partial_\tau V=(\partial_\tau a)\xi.
\]

Spatially,

\[
\Delta(a\xi)
=(\Delta a)\xi
+2\sum_i(\partial_i a)(\partial_i\xi)
+a\Delta\xi.
\]

Therefore

\[
\boxed{
(\partial_\tau a)\xi
=(\Delta a)\xi
+2D_{\nabla a}\xi
+a\Delta\xi.
}
\]

---

## 3. Perpendicular director equation

Project perpendicular to `xi`.

Since

\[
P_\xi^\perp\xi=0,
\]

we obtain

\[
\boxed{
2D_{\nabla a}\xi
+aP_\xi^\perp\Delta\xi=0.
}
\]

On `a!=0`, divide by `a`:

\[
\boxed{
2D_{\nabla\log|a|}\xi
+P_\xi^\perp\Delta\xi=0.
}
\]

The second term depends only on the static spatial director `xi` and is therefore independent of time.

---

## 4. Time differentiation gives the kernel law

Differentiate the perpendicular equation in `tau`.

Because

\[
\partial_\tau\xi=0,
\]

all director coefficients are time independent. Thus

\[
2D_{\nabla(\partial_\tau\log|a|)}\xi=0.
\]

But

\[
\partial_\tau V=KV
\]

gives

\[
\boxed{
\partial_\tau\log|a|=K.
}
\]

Hence

\[
\boxed{
D_{\nabla K}\xi=0.
}
\]

Equivalently,

\[
\boxed{
\nabla K\in\ker D\xi.
}
\]

This is exact on every active smooth component of the raw CE-H heat tangent.

---

## 5. Rank-2 consequence

On the retained Rank-2 branch,

\[
\operatorname{rank}D\xi=2.
\]

Since the spatial domain is three-dimensional,

\[
\boxed{
\dim\ker D\xi=1.
}
\]

Let `t_f(z)` be a local unit vector spanning this kernel:

\[
D_{t_f}\xi=0.
\]

Then M17-262 gives

\[
\boxed{
\nabla K=\lambda_K(z,\tau)t_f(z)
}
\]

for some scalar `lambda_K`.

Thus for every vector `v` transverse to the fiber kernel,

\[
\boxed{
D_vK=0.
}
\]

The multiplier is constant across the two director-changing directions.

---

## 6. The transverse log-amplitude gradient is also frozen

The rank-2 map

\[
D\xi:T_z\mathbb R^3\to T_\xi S^2
\]

has a one-dimensional kernel and is invertible on any chosen two-dimensional complement.

The equation

\[
2D_{\nabla\log|a|}\xi
=-P_\xi^\perp\Delta\xi
\]

therefore determines the component of

\[
\nabla\log|a|
\]

transverse to the fiber uniquely from `xi`.

Hence that transverse component is time independent.

All temporal change in `grad log|a|` is confined to the fiber direction, consistently with

\[
\nabla K\parallel t_f.
\]

---

## 7. Scalar amplitude equation

Taking the dot product of the heat equation with `xi` and using

\[
\xi\cdot\partial_i\xi=0,
\qquad
\xi\cdot\Delta\xi=-|\nabla\xi|^2,
\]

gives

\[
\boxed{
\partial_\tau a
=\Delta a-|\nabla\xi|^2a.
}
\]

Thus the raw vector tangent reduces to a scalar heat equation with a static nonnegative geometric potential, coupled to the frozen-director constraint.

At the same time,

\[
\boxed{
K
=\frac{\partial_\tau a}{a}
=\frac{\Delta a}{a}-|\nabla\xi|^2.
}
\]

The coefficient is therefore not arbitrary even along the fiber.

---

## 8. Relation to the M17 director geometry

M17-213 identifies the Rank-2 director differential through its singular values and area/anisotropy factors.

M17-214/215/216 track the associated director-fiber and anisotropy geometry.

M17-262 adds a new tangent-level statement:

\[
\boxed{
\text{raw CE-H caloric limit}
+
\operatorname{rank}D\xi=2
\Longrightarrow
\text{all multiplier variation is fiberwise}.
}
\]

Thus a two-dimensional transverse `K` pattern is forbidden on the raw quiet tangent.

If such transverse multiplier variation persists in the prelimit, at least one assumption used to obtain the raw tangent must fail: coefficient compactness, heat decoupling, Rank-2 regularity, or strong tangent convergence.

---

## 9. New frontier

The raw caloric survivor is now reduced to

\[
\boxed{
V=a\xi,
\qquad
\partial_\tau\xi=0,
\qquad
\partial_\tau a=\Delta a-|\nabla\xi|^2a,
\qquad
\nabla K\parallel\ker D\xi.
}
\]

The next target is the fiberwise compatibility problem:

1. whether the one-dimensional multiplier variation can coexist with the M17-233/234 critical sign-balanced coefficient occupancy;
2. whether bounded director-flux/fiber geometry converts it to a one-dimensional coercive cost;
3. or whether failure returns to rank loss, fiber decompactification, nodal crossing, or coefficient spike.

---

## 10. DSD audit

1. The result is local on active sign components; nodal points remain explicit exits.
2. Rank-2 is used only after deriving the coordinate-free kernel law.
3. `ker Dxi` is a geometric fiber tangent, not a formal DSD axis.
4. No global fiber coordinate is assumed.
5. The scalar amplitude reduction is exact, but no one-dimensional global separation theorem is claimed yet.
6. The projected coherent-mean branch is not covered because homogeneous CE-H is not inherited there.
7. Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
