# DSD M5-194H — Stationary (-1)-Homogeneous Tail Rigidity Audit

Date: 2026-08-29

Parent: `DSD_M5_194G_TANGENTIAL_SKEWNESS_AND_SPHERICAL_KILLING_SUBCLASS_AUDIT_2026-08-29.md`

Status: **POSITIVE PDE-RIGIDITY / FOR A NONTRIVIAL SMOOTH STATIONARY EXACTLY `(-1)`-HOMOGENEOUS 3D NAVIER--STOKES PROFILE ON `R^3\{0}`, A PURELY TANGENTIAL COMMON TAIL IS IMPOSSIBLE / THE SPHERICAL EQUATIONS FORCE ITS TANGENTIAL FIELD TO BE BOTH DIVERGENCE-FREE AND CURL-FREE, HENCE ZERO ON `S^2` / SV̌ERÁK'S CLASSIFICATION THEN IDENTIFIES EVERY NONTRIVIAL SMOOTH PROFILE AS A LANDAU SOLUTION / THEREFORE THE FAVORABLE NONZERO SPHERICAL-KILLING DRIFT FROM M5-194G IS AN OPERATOR-LEVEL TEST SUBCLASS BUT NOT AN EXACT STATIONARY `(-1)`-HOMOGENEOUS NS PROFILE / DYNAMIC, ASYMPTOTIC, OR NONSTATIONARY TYPE-I TAILS ARE NOT CLASSIFIED BY THIS RESULT / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-194G isolated a formally favorable first-order drift subclass:

\[
\Phi_r=0,
\qquad
\Phi_\tau=a\times\hat x,
\]

with no log-radial or temporal dependence.

Such a field is a spherical Killing transport, is skew-adjoint on each sphere, and commutes with the radial scalar conjugated heat operator at the spatial operator level.

The present audit asks a stronger PDE question:

> Can a nonzero field of this favorable type actually occur as an exact stationary `(-1)`-homogeneous Navier--Stokes solution smooth on the full sphere?

The answer is **no**.

---

## 2. External classification theorem used

Reference:

Vladimir Šverák, *On Landau's Solutions of the Navier--Stokes Equations*, Journal of Mathematical Sciences 179 (2011), 208--228; preprint arXiv:math/0604550.

Theorem 1 states that every nontrivial smooth solution

\[
u:\mathbb R^3\setminus\{0\}\to\mathbb R^3
\]

of the stationary Navier--Stokes equations satisfying the scale invariance

\[
\lambda u(\lambda x)=u(x)
\qquad\forall\lambda>0
\]

is a Landau solution.

The proof writes the profile intrinsically on `S^2`; that sphere system is particularly useful for the present DSD audit because it gives a direct no-go for the purely tangential branch before invoking the full classification.

---

## 3. Sphere decomposition of a `(-1)`-homogeneous stationary profile

Write

\[
u(x)=\frac1r\bigl(v(\theta)+f(\theta)e_r\bigr),
\qquad
p(x)=\frac1{r^2}p_S(\theta),
\]

where `v` is tangent to `S^2` and `f` is the radial coefficient.

Šverák derives the sphere equations

\[
\boxed{
-\Delta_H v
+v\cdot\nabla v
+\nabla(p_S-2f)=0,
}
\]

\[
\boxed{
-\Delta f
+v\cdot\nabla f
-f^2-|v|^2-2p_S=0,
}
\]

and

\[
\boxed{
\operatorname{div}_{S^2}v+f=0.
}
\]

Here `Delta_H` is the Hodge Laplacian on tangent one-forms/vector fields on the round sphere.

In the notation of the preceding DSD tail audits,

\[
\Phi_\tau=v,
\qquad
\Phi_r=f.
\]

---

## 4. Spherical-vorticity equation

Let the scalar spherical vorticity `omega_S` be defined by

\[
dv=\omega_S\,\Omega_{S^2}.
\]

Taking the exterior derivative of the tangential momentum equation yields

\[
\boxed{
-\Delta\omega_S
+
\operatorname{div}_{S^2}(v\,\omega_S)=0.
}
\]

Šverák's maximum-principle/Fredholm argument shows that a smooth solution on the full sphere satisfies

\[
\boxed{\omega_S\equiv0.}
\]

Thus

\[
\boxed{dv=0.}
\]

This is the key rigidity input.

---

## 5. Direct no-go for a nonzero purely tangential stationary tail

Assume

\[
\boxed{f=\Phi_r=0.}
\]

Then the incompressibility equation gives

\[
\boxed{
\operatorname{div}_{S^2}v=0.
}
\]

The spherical-vorticity rigidity gives independently

\[
\boxed{dv=0.}
\]

Therefore the one-form dual to `v` is both co-closed and closed, hence harmonic.

But

\[
H^1(S^2)=0.
\]

The round two-sphere has no nonzero harmonic one-forms. Consequently

\[
\boxed{v\equiv0.}
\]

and therefore

\[
\boxed{u\equiv0.}
\]

within this purely tangential exact stationary `(-1)`-homogeneous branch.

Hence

\[
\boxed{
\text{nonzero + stationary + exact `(-1)` homogeneity + smooth full sphere}
\Longrightarrow
\Phi_r\not\equiv0.
}
\]

---

## 6. Consequence for the M5-194G Killing branch

The rotational Killing profile

\[
\Phi_\tau=a\times\hat x
\]

is nonzero, tangential, divergence-free, and has nonzero spherical curl.

M5-194G correctly found that its transport operator is especially favorable to a radial scalar Carleman weight.

But the present PDE audit shows

\[
\boxed{
\frac1r(a\times\hat x)
\text{ is not a nonzero exact stationary smooth `(-1)`-homogeneous NS solution in }\mathbb R^3\setminus\{0\}.
}
\]

Thus M5-191's rotational tail remains a valid **kinematic/operator test field**, but it cannot be promoted to an exact stationary critical Navier--Stokes profile under the assumptions of this audit.

---

## 7. Full classification: the nonzero branch is Landau

Once `dv=0`, the sphere equations imply

\[
v=\nabla_{S^2}\phi
\]

and reduce to a Liouville/conformal-geometry equation on `S^2`.

Šverák solves this system and proves that every nontrivial smooth scale-invariant stationary profile is a Landau solution.

In suitable spherical coordinates the tangential component is meridional rather than swirl:

\[
v
=
-\frac{2\sin\theta}{\coth\kappa-\cos\theta}
\,e_\theta,
\]

while the radial component is

\[
f
=
\frac{2}{(\cosh\kappa-\sinh\kappa\cos\theta)^2}-2.
\]

Thus the exact nonzero stationary class is not the favorable pure rotational/Killing branch.

---

## 8. Stronger very-weak corollary and its scope

Šverák further notes that Landau solutions do not satisfy the unforced stationary Navier--Stokes equations across the origin; distributionally they carry a point-force term.

Consequently, if a `(-1)`-homogeneous very weak solution of the unforced Navier--Stokes equations is defined on all of `R^3`, is smooth away from the origin, and satisfies the equation across the origin in the required weak sense, then

\[
\boxed{u\equiv0.}
\]

for dimension three.

This is potentially relevant to blow-up limits, but it can only be used if the limiting object really has all of the required properties:

- exact `(-1)` homogeneity;
- stationarity;
- smoothness away from the origin;
- the correct unforced distributional equation across the origin.

None of those limiting upgrades is established by this note.

---

## 9. DSD branch update

### CLOSED under the stationary exact-homogeneous assumptions

The nonzero branch

\[
\Phi_r=0
\]

is closed.

Therefore the exact stationary critical profile cannot use the M5-194G pure-tangential/Killing mechanism unless it is the zero profile.

### CLASSIFIED under the same assumptions

Every nonzero smooth exact stationary `(-1)`-homogeneous profile is Landau.

### NOT CLOSED for the actual Type-I endpoint

The Type-I canonical common tail may be

- only asymptotically `(-1)`-homogeneous;
- nonstationary in physical or rescaled time;
- dependent on log-radius;
- a coefficient field extracted from a solution difference rather than an autonomous stationary solution;
- defined only on a continuation/exterior region rather than all of `R^3\setminus\{0\}`.

Therefore the classification cannot simply be substituted for the missing endpoint proof.

---

## 10. Updated route priority

The result changes the route order.

### Route K1 — exact stationary profile

This branch is essentially classified:

\[
\boxed{0\quad\text{or Landau}.}
\]

The favorable nonzero Killing drift is excluded.

### Route K2 — asymptotic rigidity

The next useful question is whether the actual Type-I common tail has a blow-down/blow-up subsequence converging strongly enough to an exact stationary `(-1)`-homogeneous sphere-smooth profile.

If yes, the limit is forced into `0/Landau`, and if the limit also satisfies the unforced very-weak equation across the origin, only zero remains.

### Route M — generic dynamic endpoint

If no such stationary limiting rigidity can be justified, the calculation returns to the generic non-small first-order drift and requires a critical backward-uniqueness estimate or matrix/symmetrizer structure.

---

## 11. Next audit target

Before attempting a matrix symmetrizer, audit Route K2:

\[
\boxed{
\text{Which properties of the current Type-I compactness/canonical-tail construction are strong enough to pass to a stationary `(-1)`-homogeneous limit?}
}
\]

The required ledger is:

1. spatial scaling compactness;
2. time-translation or rescaled-time compactness;
3. exact homogeneity of the limit versus only a pointwise `1/r` bound;
4. smoothness on the full sphere;
5. pressure convergence;
6. whether the limit solves the unforced equation across the origin.

Only properties actually established earlier in the repository may be checked as `YES`; all others must remain explicit gaps.
