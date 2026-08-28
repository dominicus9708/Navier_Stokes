# DSD M5-194G — Tangential Skewness and Spherical Killing-Subclass Audit

Date: 2026-08-29

Parent: `DSD_M5_194F_CARLEMAN_CURVATURE_BUDGET_FIREWALL_2026-08-29.md`

Status: **POSITIVE CONDITIONAL SUBCLASS / `Phi_r=0` PLUS SPHERICAL DIVERGENCE-FREE MAKES THE TANGENTIAL DRIFT SKEW-ADJOINT ON EACH SPHERE, BUT THIS ALONE DOES NOT MAKE IT COMMUTE WITH THE CONJUGATED HEAT OPERATOR / LOG-RADIAL VARIATION PRODUCES MIXED COMMUTATORS AND ANGULAR DEFORMATION IS MEASURED BY THE SPHERICAL SYMMETRIC GRADIENT / THE EXACTLY FAVORABLE SCALAR SUBCLASS IS LOG-RADIUS-INDEPENDENT SPHERICAL KILLING TRANSPORT (AND TIME-INDEPENDENT IF THE FULL TIME COMMUTATOR IS TO VANISH) / THE ROTATIONAL TEST TAIL IS OF THIS FAVORABLE TYPE / GENERIC TANGENTIAL TAILS REMAIN OPEN / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-194E and M5-194F show that a generic critical first-order drift cannot be made perturbative merely by taking the Carleman parameter large or by globally increasing scalar weight curvature.

The most economical surviving scalar branch is therefore structural:

\[
\Phi_r=0.
\]

For such a tail a radial Carleman weight is constant along the drift. The question is whether spherical incompressibility is enough to make the angular drift harmless in the complete conjugated heat operator.

The answer is:

\[
\boxed{
\text{spherical divergence-free gives skewness, but not full commutation.}
}
\]

A smaller Killing-field subclass is exactly favorable.

---

## 2. Purely tangential incompressibility

Write

\[
B_T
=
\frac1r\Phi_\tau(y,\theta,t),
\qquad
\Phi_r=0.
\]

The full divergence identity from M5-194E is

\[
\Phi_r-\partial_y\Phi_r
+
\operatorname{div}_{S^2}\Phi_\tau=0.
\]

Hence

\[
\boxed{
\Phi_r=0
\quad\Longrightarrow\quad
\operatorname{div}_{S^2}\Phi_\tau=0.
}
\]

Define the angular transport operator

\[
T:=\Phi_\tau\cdot\nabla_{S^2}.
\]

For scalar functions on `S^2`, spherical integration by parts gives

\[
\langle Tf,g\rangle_{L^2(S^2)}
=-\langle f,Tg\rangle_{L^2(S^2)}.
\]

Thus

\[
\boxed{T^*=-T.}
\]

This is the first positive structural gain.

---

## 3. Radial weight does not break this skewness

Let

\[
\varphi=e^{\psi(y)}.
\]

Because `psi` depends only on `y`,

\[
T\psi=0.
\]

Therefore

\[
\boxed{
 e^{\psi}Te^{-\psi}=T.
}
\]

No `beta Phi_r`-type scalar potential is recreated.

This confirms the favorable status of the purely tangential branch identified in M5-194A.

However, skewness of `T` alone does not imply that `T` commutes with the rest of the conjugated operator.

---

## 4. Log-radial commutator

If `Phi_tau` depends on `y`, then

\[
\boxed{
[\partial_y,T]
=
(\partial_y\Phi_\tau)\cdot\nabla_{S^2}.
}
\]

Consequently,

\[
\boxed{
[\partial_{yy},T]
=
(\partial_{yy}\Phi_\tau)\cdot\nabla_{S^2}
+
2(\partial_y\Phi_\tau)\cdot\nabla_{S^2}\partial_y.
}
\]

The conjugated radial heat operator contains

\[
(2\psi'+1)\partial_y.
\]

Since the coefficient `2 psi' + 1` depends only on `y`,

\[
\boxed{
[(2\psi'+1)\partial_y,T]
=
(2\psi'+1)
(\partial_y\Phi_\tau)\cdot\nabla_{S^2}.
}
\]

When `psi' ~ beta`, this channel has coefficient size

\[
O(\beta\,\partial_y\Phi_\tau).
\]

Thus a log-radius-dependent tangential drift can recreate a large mixed commutator even though it is skew on every individual sphere.

---

## 5. Angular Laplacian commutator

Let

\[
A:=-\Delta_{S^2}.
\]

Because `A` is self-adjoint and `T` is skew-adjoint,

\[
[A,T]
\]

is self-adjoint.

Let

\[
S^{S^2}_{\Phi}
:=
\frac12
\left(
\nabla^{S^2}\Phi_\tau
+
(\nabla^{S^2}\Phi_\tau)^T
\right)
\]

be the spherical symmetric gradient.

For a smooth scalar test function `f`, direct integration by parts gives

\[
\boxed{
\langle[A,T]f,f\rangle
=
2\int_{S^2}
S^{S^2}_{\Phi}
(\nabla_{S^2}f,\nabla_{S^2}f)\,dS.
}
\]

Therefore the obstruction to commuting with the angular Laplacian is precisely the **spherical deformation tensor**.

If

\[
S^{S^2}_{\Phi}\ne0,
\]

then the angular transport is skew as an `L^2` operator but still generates a symmetric second-order commutator with the Laplacian.

Thus

\[
\boxed{
\operatorname{div}_{S^2}\Phi_\tau=0
\quad\not\Rightarrow\quad
[\Delta_{S^2},T]=0.
}
\]

---

## 6. Killing fields are the exact angular-commuting subclass

A tangent vector field on `S^2` is Killing precisely when

\[
\boxed{
S^{S^2}_{\Phi}=0.
}
\]

Killing fields generate isometries of the round sphere. Because the Laplace--Beltrami operator is invariant under those isometries,

\[
\boxed{
[\Delta_{S^2},T]=0
}
\]

for a spherical Killing transport.

Every Killing field on the round two-sphere is a rotational generator. It can be written as

\[
\boxed{
\Phi_\tau(\theta)
=a\times\hat x,
\qquad a\in\mathbb R^3,
}
\]

where `hat x=x/|x|`.

This is a three-dimensional Lie algebra of rotations.

---

## 7. Exact favorable stationary subclass

Suppose

\[
\boxed{
\Phi_r=0,
\qquad
\partial_y\Phi_\tau=0,
\qquad
S^{S^2}_{\Phi}=0.
}
\]

Then

\[
[T,\psi(y)]=0,
\]

\[
[T,\partial_y]=0,
\]

and

\[
[T,\Delta_{S^2}]=0.
\]

Therefore the angular first-order drift commutes with every spatial part of the radial conjugated log-cylinder heat operator.

If in addition

\[
\partial_t\Phi_\tau=0,
\]

then it also commutes with the time derivative, modulo the harmless scalar factor `r^2=e^{-2y}` which is independent of angle.

Hence, for this stationary spherical-Killing subclass,

\[
\boxed{
\text{the critical first-order drift can be retained as a commuting skew transport rather than estimated as an error.}
}
\]

This removes the generic `C|Phi|^2 < 1+psi''` smallness requirement for that drift channel at the formal operator level.

---

## 8. Relation to the M5-191 rotational test tail

The rotational critical tail used in M5-191 is of the form

\[
B_{\rm rot}(x)
\sim
\frac{a\times x}{|x|^2}
=
\frac1r(a\times\hat x).
\]

Thus

\[
\Phi_r=0,
\qquad
\Phi_\tau=a\times\hat x,
\]

which is exactly a spherical Killing field independent of log-radius.

Therefore M5-191 should now be classified more precisely:

\[
\boxed{
\text{M5-191 is not merely tangential; it lies in the maximally favorable rotational/Killing first-order subclass.}
}
\]

Its physical `1/r` radial dependence can still generate a nonzero three-dimensional strain matrix. But M5-194E shows that bounded critical strain is a zeroth-order channel with a favorable `beta^2` absorption margin at the coefficient-ledger level.

Hence the M5-191 test does **not** expose the generic first-order endpoint obstruction.

---

## 9. Time-dependent tangential tail

If

\[
\Phi_\tau=\Phi_\tau(y,\theta,t),
\]

then

\[
\boxed{
[\partial_t,T]
=
(\partial_t\Phi_\tau)\cdot\nabla_{S^2}.
}
\]

In the dimensionless heat operator the time derivative appears as

\[
r^2\partial_t.
\]

Hence time variation of the angular drift generates

\[
r^2(\partial_t\Phi_\tau)\cdot\nabla_{S^2}.
\]

Whether this is subcritical, critical, or small depends on the actual Type-I rescaled-time normalization and is not decided by the present purely spatial audit.

This must be kept separate from the stationary Killing conclusion.

---

## 10. DSD verdict

### POSITIVE CONDITIONAL RESULT

The critical first-order transport is formally harmless to a radial scalar Carleman architecture if it belongs to the stationary log-radius-independent spherical Killing subclass:

\[
\boxed{
\Phi_r=0,
\quad
\partial_y\Phi_\tau=0,
\quad
S^{S^2}_{\Phi}=0,
\quad
\partial_t\Phi_\tau=0.
}
\]

In that case the angular drift is skew and commutes with the spatial conjugated heat operator.

### FIREWALL

The weaker condition

\[
\Phi_r=0,
\qquad
\operatorname{div}_{S^2}\Phi_\tau=0
\]

is **not sufficient**.

Generic tangential tails can still generate

- log-radial mixed commutators through `partial_y Phi_tau`;
- symmetric angular commutators through `S^{S^2}_Phi`;
- temporal commutators through `partial_t Phi_tau`.

### REMAINS OPEN

- whether the canonical Type-I common tail is forced into or approaches the spherical Killing subclass;
- whether non-Killing commutators can be absorbed by a refined endpoint estimate;
- whether a time-dependent rotational generator can be removed by a rotating frame without recreating equally bad terms;
- matrix/symmetrizer treatment of generic non-small critical drift;
- complete backward uniqueness and global regularity.

---

## 11. Next audit target

There are now two sharply separated routes.

### Route K — rigidity route

Determine whether the Navier--Stokes/common-tail equations themselves constrain a critical purely tangential tail toward

\[
\Phi_\tau=a\times\hat x
\]

or another finite-dimensional structured family.

### Route M — generic matrix route

Assume no such rigidity and construct the first-order log-cylinder symbol for a generic `Phi`, then test whether a matrix symmetrizer can control the non-small drift without demanding scalar smallness.

The next economical calculation is Route K first: insert a `1/r` stationary tail ansatz into the stationary leading-order Navier--Stokes equations and determine what equations the spherical profile `Phi(theta)` must satisfy.
