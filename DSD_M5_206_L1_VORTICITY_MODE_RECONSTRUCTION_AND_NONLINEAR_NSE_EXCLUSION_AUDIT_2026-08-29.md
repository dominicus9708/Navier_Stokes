# DSD M5-206 — `l=1` Critical Vorticity Reconstruction and Nonlinear NSE Exclusion

Date: 2026-08-29

Parent: `DSD_M5_205_DEGREE_MINUS_TWO_VORTICITY_CYLINDER_MATRIX_DIFFUSION_IDENTITY_AUDIT_2026-08-29.md`

Status: **POSITIVE SPECTRAL-BRANCH CLOSURE / THE APPARENT CONSTANT-METRIC `l=1` DEGREE-`-2` VORTICITY BALANCE CAN BE CLASSIFIED EXACTLY / DIVERGENCE-FREE PLUS GLOBAL-CURL ZERO-FLUX REDUCES EVERY COMPONENTWISE `l=1` MODE TO `W=a×theta` / THERE IS A UNIQUE SMOOTH DIVERGENCE-FREE DEGREE-`-1` VELOCITY PRODUCING IT, `B_a=(2r)^-1[a+(a·theta)theta]`, WHICH IS EXACTLY THE ROTATED M5-194A TEST FAMILY / ITS VORTICITY IS HARMONIC AWAY FROM THE ORIGIN, BUT ITS NONLINEAR STATIONARY VORTICITY RESIDUAL IS `-3(a·theta)(a×theta)/r^4`, SO IT CANNOT SOLVE THE UNFORCED STATIONARY NSE FOR ANY NONZERO `a` / THIS AGREES WITH SVERAK'S HOMOGENEOUS LANDAU CLASSIFICATION / THE FREE `l=1` SPECTRAL ESCAPE IS CLOSED, THOUGH VARIABLE-METRIC AND DYNAMIC CRITICAL TAILS REMAIN OPEN / GLOBAL REGULARITY UNPROVED.**

---

## 1. The apparent spectral branch from M5-205

For a constant matrix metric and a `y`-independent degree-`-2` vorticity coefficient, the post-symmetrization diffusion balance can reduce to

\[
\int_{S^2}|\nabla_SW|^2
=2\int_{S^2}|W|^2.
\]

Hence each Cartesian component lies in the first nonzero scalar spherical-harmonic eigenspace:

\[
\boxed{-\Delta_{S^2}W=2W.}
\]

The question is whether such a vector coefficient can actually be a critical Navier--Stokes vorticity.

---

## 2. General vector-valued `l=1` mode

Every scalar `l=1` harmonic is linear in `theta`.

Therefore every `R^3`-valued componentwise `l=1` field has the form

\[
\boxed{W(\theta)=M\theta}
\]

for one constant real `3 x 3` matrix `M`.

The corresponding physical vorticity is

\[
\boxed{\omega(x)=r^{-2}M\theta=r^{-3}Mx.}
\]

---

## 3. Divergence-free condition

Differentiate

\[
\omega_i=r^{-3}M_{ij}x_j.
\]

Then

\[
\nabla\cdot\omega
=
r^{-3}
\left[
\operatorname{tr}M
-3\theta^TM\theta
\right].
\]

Only the symmetric part of `M` contributes to the quadratic form. Write

\[
M=S+A,
\qquad
S^T=S,
\qquad
A^T=-A.
\]

The identity

\[
\operatorname{tr}M
-3\theta^TS\theta
=0
\]

for every unit `theta` implies

\[
\boxed{S=cI}
\]

for one scalar `c`.

Thus

\[
\boxed{M=cI+A.}
\]

---

## 4. Curl flux removes the radial monopole part

If `omega=curl B` for one globally defined smooth degree-`-1` velocity field on `R^3\setminus{0}`, then the flux of `omega` through each sphere must vanish.

Indeed the flux 2-form is the exterior derivative of the velocity 1-form restricted to the closed sphere, so its integral is zero.

But

\[
\begin{aligned}
\int_{S^2}W\cdot\theta\,dS
&=
\int_{S^2}\theta^T(cI+A)\theta\,dS\\
&=
4\pi c,
\end{aligned}
\]

because

\[
\theta^TA\theta=0.
\]

Therefore

\[
\boxed{c=0.}
\]

Hence every admissible curl-type `l=1` vorticity coefficient is purely antisymmetric:

\[
\boxed{W=A\theta.}
\]

Every real antisymmetric `3 x 3` matrix is cross product with a vector, so after choosing the sign convention

\[
\boxed{W(\theta)=a\times\theta.}
\]

---

## 5. Reconstruct the degree-`-1` velocity

Define

\[
\boxed{
B_a(x)
:=
\frac1{2r}
\left[
 a+(a\cdot\theta)\theta
\right].
}
\]

Equivalently,

\[
B_a
=
\frac12
\left[
\frac a r
+
\frac{(a\cdot x)x}{r^3}
\right].
\]

The two vector fields inside the brackets have opposite divergence:

\[
\nabla\cdot\frac a r
=-\frac{a\cdot\theta}{r^2},
\]

\[
\nabla\cdot
\frac{(a\cdot x)x}{r^3}
=+rac{a\cdot\theta}{r^2}.
\]

Therefore

\[
\boxed{\nabla\cdot B_a=0.}
\]

Their curls are equal:

\[
\nabla\times\frac a r
=
\frac{a\times\theta}{r^2},
\]

and, because

\[
\frac{(a\cdot x)x}{r^3}
=
\frac a r
-
\nabla(a\cdot\theta),
\]

its curl is the same.

Thus

\[
\boxed{
\nabla\times B_a
=
\frac{a\times\theta}{r^2}
=\omega_a.
}
\]

---

## 6. Uniqueness of the reconstruction

Suppose another smooth divergence-free degree-`-1` field `B` has the same vorticity.

Then

\[
C:=B-B_a
\]

satisfies

\[
\nabla\times C=0,
\qquad
\nabla\cdot C=0,
\]

and is homogeneous of degree `-1`.

Since `R^3\setminus{0}` is simply connected,

\[
C=\nabla\varphi.
\]

Degree `-1` of `C` allows only a degree-zero angular potential plus a possible `log r` radial potential. Harmonicity

\[
\Delta\varphi=0
\]

eliminates the `log r` coefficient after spherical averaging, and the remaining degree-zero harmonic on `S^2` is constant.

Hence

\[
\boxed{C=0.}
\]

Therefore `B_a` is the unique smooth divergence-free degree-`-1` velocity with the admissible `l=1` vorticity.

---

## 7. Identification with the M5-194A test tail

Take

\[
a=e_z.
\]

On the sphere,

\[
e_z
=
\cos\theta\,e_r
-
\sin\theta\,e_\theta.
\]

Also

\[
(a\cdot\theta)\theta
=
\cos\theta\,e_r.
\]

Therefore

\[
\boxed{
B_a
=
\frac1r
\left[
\cos\theta\,e_r
-
\frac12\sin\theta\,e_\theta
\right].
}
\]

This is exactly the explicit divergence-free critical tail used in M5-194A to show failure of a universal scalar adapted Carleman weight.

Thus that counterexample is not arbitrary: it is the unique velocity reconstruction of the free `l=1` critical vorticity mode.

---

## 8. The vorticity is harmonic

Each component of

\[
\omega_a
=
\frac{a\times x}{r^3}
\]

is a derivative/rotation of the harmonic Newton kernel `1/r`.

Hence away from the origin

\[
\boxed{\Delta\omega_a=0.}
\]

Equivalently, the degree-`-2` radial homogeneity potential `2` cancels the spherical `l=1` eigenvalue `2` exactly.

This explains the M5-205 constant-metric viscous spectral balance.

---

## 9. Exact nonlinear vorticity residual

The stationary vorticity equation would require

\[
-\nu\Delta\omega_a
+
(B_a\cdot\nabla)\omega_a
-
(\omega_a\cdot\nabla)B_a
=0.
\]

The viscous term vanishes:

\[
\Delta\omega_a=0.
\]

Direct differentiation of the explicit fields gives

\[
\boxed{
(B_a\cdot\nabla)\omega_a
-
(\omega_a\cdot\nabla)B_a
=
-3
\frac{(a\cdot x)(a\times x)}{r^6}.
}
\]

In spherical variables,

\[
\boxed{
(B_a\cdot\nabla)\omega_a
-
(\omega_a\cdot\nabla)B_a
=
-\frac3{r^4}
(a\cdot\theta)(a\times\theta).
}
\]

For any

\[
a\ne0,
\]

this field is not identically zero.

Therefore

\[
\boxed{
a\ne0
\quad\Longrightarrow\quad
B_a\text{ is not a stationary unforced Navier--Stokes solution}.}
\]

The conclusion is viscosity-independent because the `l=1` vorticity is harmonic.

---

## 10. Nonlinear order interpretation

The family `B_a` is linear in `a`, while the residual is quadratic:

\[
\mathcal R_{NSE}[B_a]
=O(|a|^2).
\]

Thus the `l=1` mode is a legitimate **linearized neutral direction** around the zero homogeneous profile, but nonlinear self-interaction immediately leaves the pure `l=1` eigenspace.

A nonlinear completion, if one exists, must generate higher spherical harmonics.

This is consistent with the explicit Landau family: the small-amplitude homogeneous stationary branch is tangent to this axisymmetric `l=1` direction, while finite-amplitude Landau profiles contain nonlinear angular structure.

---

## 11. External homogeneous classification cross-check

Šverák's classification of smooth stationary degree-`-1` Navier--Stokes solutions on `R^3\setminus{0}` identifies the nontrivial smooth class with the Landau family.

The explicit pure `l=1` field above is not an exact finite-amplitude Landau profile; the direct residual calculation already proves this independently.

Thus the internal calculation and the external classification agree:

\[
\boxed{
\text{pure nonzero }l=1\text{ critical vorticity}
\notin
\text{exact stationary NSE class}.
}
\]

---

## 12. Consequence for M5-205

The apparent constant-metric spectral escape

\[
-\Delta_SW=2W
\]

is too large when `W` is treated as a free vector field.

After imposing

1. vorticity divergence-free;
2. global curl zero-flux;
3. existence of a smooth divergence-free degree-`-1` velocity reconstruction;
4. the nonlinear stationary vorticity equation,

only

\[
\boxed{W=0}
\]

remains inside the **pure `l=1` subspace**.

Hence that specific residual branch is closed.

---

## 13. What this does not close

This result does not exclude

- the full nonlinear Landau family, which contains higher angular harmonics;
- variable matrix metrics with nontrivial `Delta H` commutators;
- `y`-dependent critical log-cylinder profiles;
- time-dependent periodic/aperiodic similarity tails;
- forced/core-coupled critical tails;
- generic backward-uniqueness survivors.

The result closes only the free constant-metric `l=1` spectral loophole exposed in M5-205.

---

## 14. DSD verdict

### PROVED

- every componentwise vector `l=1` coefficient is `M theta`;
- divergence-free forces `sym M=cI`;
- curl zero-flux forces `c=0`;
- admissible `l=1` vorticity is exactly `a x theta`;
- unique smooth divergence-free degree-`-1` velocity reconstruction is `B_a=(2r)^-1[a+(a·theta)theta]`;
- this is the M5-194A critical-tail family;
- its vorticity is harmonic;
- its exact nonlinear stationary vorticity residual is `-3(a·theta)(a x theta)/r^4`;
- all nonzero pure `l=1` modes fail the stationary unforced NSE;
- the M5-205 free `l=1` constant-metric spectral branch is closed.

### OPEN

- nonlinear higher-harmonic homogeneous completions already represented by Landau;
- dynamic/core-coupled critical tails;
- variable-metric commutator control;
- generic critical backward uniqueness;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]

---

## 15. Next target

The next nonredundant matrix branch is no longer the free spherical `l=1` mode.

It is the variable-metric curvature term

\[
\frac12\int W^T(\Delta_cH)W.
\]

A useful next audit is to test whether the full-gradient symmetrizer equation plus incompressibility imposes any elliptic equation or trace identity on `Delta H` strong enough to bound this term.

If not, construct an explicit smooth bounded-ellipticity family with elliptic monodromy but arbitrarily large transverse `Delta H`, proving that characteristic Floquet control alone cannot support a PDE Carleman estimate. That would decide whether the local matrix route must be abandoned in favor of nonlocal/backward-uniqueness methods.