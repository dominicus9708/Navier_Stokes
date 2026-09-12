# DSD M19-108 — One-slice regularity speed floor forces a nonzero RSS to have a quantitative rotation-rate or rotational-anisotropy floor

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / M19-096 SPEED FLOOR SPECIALIZED TO EXACT RSS / SMALL ROTATION CAN SURVIVE ONLY IF THE ROTATIONAL ANISOTROPY NORM BLOWS UP, WHICH IS FORBIDDEN ON A COMPACT SMOOTH TYPE-I CORRIDOR / LARGE ROTATION FORCES THE PROFILE TOWARD AXISYMMETRY IF THE SIMILARITY SPEED IS UNIFORMLY BOUNDED / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Exact RSS kinematics

For an RSS orbit about axis generator

\[
A\in\mathfrak{so}(3),
\]

write

\[
U(s)=e^{s\alpha A}\cdot U_0.
\]

Then

\[
\boxed{
\partial_sU
=\alpha\mathcal J_AU,
}
\]

where

\[
\mathcal J_AU
=AU-(Ay)\cdot\nabla U.
\]

---

## 2. Gaussian one-slice speed floor

On the certified Pineau--Vicol application lane used in M19-096, a singular survivor must satisfy for every sufficiently late `s`

\[
\boxed{
\mathcal V_G(s)
:=
\int_{\mathbb R^3}
|\partial_sU(y,s)|
(1+|y|)e^{-|y|^2/8}\,dy
\ge v_*>0.
}
\]

For RSS this becomes

\[
\mathcal V_G(s)
=|\alpha|\,\mathcal J_G(U_0),
\]

where

\[
\boxed{
\mathcal J_G(U_0)
:=
\int
|\mathcal J_AU_0|
(1+|y|)e^{-|y|^2/8}\,dy.
}
\]

Hence every nonregular RSS survivor on this lane obeys

\[
\boxed{
|\alpha|\,\mathcal J_G(U_0)
\ge v_*.
}
\]

This is an exact kinematic consequence of the external one-slice criterion once its hypotheses are certified.

---

## 3. Axisymmetric degeneration

If

\[
\mathcal J_G(U_0)=0,
\]

then

\[
\mathcal J_AU_0=0
\]

in the retained smooth class, so `U_0` is invariant under rotation about the chosen axis.

The apparent RSS time dependence then disappears:

\[
\partial_sU=0.
\]

Thus the orbit reduces to ordinary backward self-similarity rather than a genuinely rotated orbit.

Therefore a genuinely nontrivial RSS must have

\[
\boxed{
\mathcal J_G(U_0)>0.
}
\]

---

## 4. Compact-corridor upper bound gives an internal small-alpha exclusion

Suppose the retained smooth Type-I compact corridor provides a uniform rotational-anisotropy bound

\[
\boxed{
\mathcal J_G(U_0)
\le C_J<\infty.
}
\]

Then the speed floor yields

\[
\boxed{
|\alpha|
\ge
\frac{v_*}{C_J}.
}
\]

Hence sufficiently small rotation rate is impossible on this certified singular lane even before invoking the separate rotated Liouville theorem.

This does not produce a universal numerical threshold: `v_*` and `C_J` depend on the certified corridor and external theorem constants.

---

## 5. Large-alpha axisymmetry pressure

Assume in addition that compact smooth recurrence supplies a uniform upper bound on the same Gaussian similarity speed,

\[
\boxed{
\mathcal V_G(s)\le V_*<\infty.
}
\]

Then

\[
\boxed{
\frac{v_*}{|\alpha|}
\le
\mathcal J_G(U_0)
\le
\frac{V_*}{|\alpha|}.
}
\]

Therefore along a hypothetical sequence

\[
|\alpha_n|\to\infty,
\]

we must have

\[
\boxed{
\mathcal J_G(U_{0,n})\to0.
}
\]

Thus large rotation forces the profile toward axisymmetry in the Gaussian rotational-anisotropy metric.

This is consistent with, but does not replace, the Pineau--Vicol large-rotation Liouville theorem.

The product

\[
\alpha_n\mathcal J_AU_{0,n}
\]

may remain order one, so one must not conclude triviality merely from

\[
\mathcal J_AU_{0,n}\to0.
\]

---

## 6. Parameter geometry of a surviving RSS

On the combined certified lane, a surviving genuine RSS must satisfy

\[
\boxed{
|\alpha|\ge\alpha_*
:=\frac{v_*}{C_J}>0
}
\]

and, if `|alpha|` is very large, must lie very close to the axisymmetric subspace.

Therefore the rotation-rate problem is naturally divided into

\[
\boxed{
\text{small alpha: internally excluded}
\quad|\quad
\text{moderate alpha: genuine hard core}
\quad|\quad
\text{large alpha: axisymmetry-singular perturbation regime}.
}
\]

This aligns with the external extreme-rotation theorem without claiming identical thresholds.

---

## 7. Firewall

The estimate

\[
|\alpha|\mathcal J_G\ge v_*
\]

is conditional on the M19-096 external regularity criterion being applicable to the branch under consideration.

It does not establish that the whole original singularity tree satisfies the required Type-I and pressure-annulus hypotheses.

Also,

\[
\mathcal J_G\to0
\]

at large `alpha` is not by itself a contradiction.

---

## 8. Next target

The moderate RSS hard core can now be expressed in a compact parameter region if the external large-rotation threshold and the internal small-rate floor are both available.

The next useful calculation is to ask whether the co-rotating stationary equation admits a Pohozaev/virial identity in which the rotation term cancels but the nonlinear profile terms have a definite sign or a finite-radius boundary defect that can be matched to the known `1/r` critical tail.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
