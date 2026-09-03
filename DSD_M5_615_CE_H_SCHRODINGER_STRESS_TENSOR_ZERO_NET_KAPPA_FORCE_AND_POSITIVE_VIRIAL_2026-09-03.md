# DSD M5-615 — CE-H Schrödinger stress tensor gives zero net kappa force and positive virial moment

Date: 2026-09-03

Status: **LOCAL CONSERVATION LAW / THE CE-H EIGENVALUE EQUATION `-Delta W + kappa W=0` HAS A SYMMETRIC STRESS TENSOR `T_ij=partial_iW·partial_jW - 1/2(|nabla W|^2+kappa|W|^2)delta_ij` WHOSE DIVERGENCE IS EXACTLY `-(1/2)|W|^2 nabla kappa` / TERMINAL-TAIL DECAY MAKES THE TRACTION AT INFINITY VANISH, SO THE ENSTROPHY-WEIGHTED KAPPA-GRADIENT HAS ZERO TOTAL VECTOR FORCE / THE TRACE/VIRIAL MOMENT OF THE SAME LAW RECOVERS M5-607: `int y·(|W|^2 nabla kappa)=2P>0` / THUS THE CE-H KAPPA LANDSCAPE IS AN INTERNAL ZERO-NET-FORCE DIPOLE/STRESS SYSTEM WITH STRICTLY POSITIVE DILATION MOMENT / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. CE-H as a vector Schrödinger equation

The global CE-H equation is

\[
\Delta W=\kappa W,
\]

or equivalently

\[
\boxed{-\Delta W+\kappa W=0.}
\]

Define

\[
\rho=|W|.
\]

---

## 2. Stress tensor

Set

\[
\boxed{
\mathbb T_{ij}
:=
\partial_iW\cdot\partial_jW
-
\frac12
\left(
|\nabla W|^2+\kappa|W|^2
\right)\delta_{ij}.
}
\]

This tensor is symmetric.

Differentiate:

\[
\partial_i(\partial_iW\cdot\partial_jW)
=
\Delta W\cdot\partial_jW
+
\partial_iW\cdot\partial_{ij}W.
\]

The second term cancels

\[
\frac12\partial_j|\nabla W|^2.
\]

Using

\[
\Delta W=\kappa W,
\]

the remaining `kappa W·partial_j W` cancels the derivative of the `kappa|W|^2/2` term except for the derivative of `kappa` itself.

Hence

\[
\boxed{
\partial_i\mathbb T_{ij}
=
-\frac12|W|^2\partial_j\kappa.
}
\]

Vectorially,

\[
\boxed{
\nabla\cdot\mathbb T
=
-\frac12|W|^2\nabla\kappa.
}
\]

---

## 3. Define the kappa-force density

Define

\[
\boxed{
F_\kappa
:=
|W|^2\nabla\kappa.
}
\]

Then

\[
\boxed{
F_\kappa=-2\nabla\cdot\mathbb T.
}
\]

M5-600 gives

\[
W\cdot\nabla\kappa=0,
\]

so

\[
\boxed{F_\kappa\perp W}
\]

on the active set.

Thus this is a purely vortex-line-transverse force density.

---

## 4. Zero total force

Integrate over `B_R`:

\[
\int_{B_R}F_\kappa dy
=
-2\int_{S_R}\mathbb T n\,dS.
\]

The terminal-tail expansion gives

\[
W=O(r^{-2}),
\qquad
\nabla W=O(r^{-3}),
\qquad
\kappa|W|^2=W\cdot\Delta W=O(r^{-6}).
\]

Therefore

\[
\mathbb T=O(r^{-6}),
\]

and

\[
\int_{S_R}\mathbb T n\,dS=O(R^{-4})\to0.
\]

Hence

\[
\boxed{
\int_{\mathbb R^3}|W|^2\nabla\kappa\,dy=0.
}
\]

The internal kappa force has zero net vector resultant.

---

## 5. Zero torque

Because `T` is symmetric, the same stress law has zero total torque.

Indeed, after the same boundary audit,

\[
\boxed{
\int y\times F_\kappa\,dy=0.
}
\]

This is supplementary and is not needed for the main virial argument.

---

## 6. Positive dilation moment

Contract the stress law with the position vector `y`.

Integration by parts gives

\[
\int y\cdot F_\kappa
=
2\int\operatorname{tr}\mathbb T.
\]

Now

\[
\operatorname{tr}\mathbb T
=
-\frac12|\nabla W|^2
-\frac32\kappa|W|^2.
\]

Using

\[
\int\kappa|W|^2=-P,
\]

we obtain

\[
\int\operatorname{tr}\mathbb T
=
-\frac12P+rac32P
=P.
\]

Therefore

\[
\boxed{
\int y\cdot F_\kappa dy
=2P>0.
}
\]

This is exactly M5-607's Pohozaev identity.

---

## 7. Internal-dipole interpretation

The pair of exact laws is

\[
\boxed{
\int F_\kappa=0,
\qquad
\int y\cdot F_\kappa=2P>0.
}
\]

Thus the force field is not a monopole.

It must have internally compensating vector contributions whose spatial separation carries a strictly positive first moment.

The CE-H survivor therefore requires a genuine transverse kappa-force dipole/multipole architecture inside the finite active region.

---

## 8. Uniform lower virial on the marked hull

Earlier compactness arguments give

\[
P\ge p_0>0
\]

on the nonzero marked component.

Hence

\[
\boxed{
\int y\cdot F_\kappa\ge2p_0>0.
}
\]

This virial cannot collapse to zero along the recurrent hard component.

---

## 9. Next target

M5-604 localizes all fixed CE-H kappa budget to a finite core, and the all-order compact bounds give a uniform `L1` cap on `F_kappa=-2 div T`.

Together with

\[
\int F_\kappa=0,
\qquad
\int y\cdot F_\kappa\ge2p_0,
\]

this should force a quantitative separated positive/negative dipole in at least one Cartesian projection of `F_kappa`.

The next audit will extract that separation and determine whether its two lobes must be represented by distinct persistent lineages or by a multi-center source shape inside one lineage.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
