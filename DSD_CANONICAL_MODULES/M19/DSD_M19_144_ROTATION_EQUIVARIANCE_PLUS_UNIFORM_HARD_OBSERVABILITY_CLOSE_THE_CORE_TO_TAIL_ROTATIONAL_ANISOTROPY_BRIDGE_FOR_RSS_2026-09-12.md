# DSD M19-144 — Rotation equivariance plus uniform hard observability close the core-to-tail rotational anisotropy bridge for RSS

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / THE ONE-WAY ANISOTROPY OBSERVATION GAP LEFT IN M19-127 IS CLOSED ON THE CERTIFIED UNIFORMLY OBSERVABLE HARD BUNDLE / ROTATION EQUIVARIANCE OF THE SCATTERING MAP IDENTIFIES THE INTERIOR ROTATION TANGENT WITH THE ROTATIONAL DERIVATIVE OF THE CRITICAL TAIL / MODERATE RSS COMPENSATION CAN THEREFORE BE EXPRESSED DIRECTLY IN FAR-TAIL VARIABLES / THIS SHARPENS BUT DOES NOT YET ELIMINATE THE MODERATE RSS HARD CORE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Rotation action

Let `Q in SO(3)` act on a divergence-free velocity field by

\[
(Q\cdot U)(y)
:=
Q\,U(Q^{-1}y).
\]

For a skew generator `J`, define

\[
\boxed{
\mathcal R_JU
:=
JU-(Jy)\cdot\nabla U.
}
\]

This is the exact tangent to the rotation orbit.

On the critical scattering datum define the corresponding angular rotation generator

\[
\boxed{
\mathcal R_{J,\omega}A
:=
JA-(J\omega)\cdot\nabla_{S^2}A.
}
\]

---

## 2. Scattering map is rotation equivariant

The Navier--Stokes equations, similarity rescaling, the radial spectator construction, and the outward characteristic are rotation covariant.
Hence

\[
\boxed{
\mathscr S(Q\cdot U)
=
Q\cdot\mathscr S(U).
}
\]

Differentiate at the identity rotation:

\[
\boxed{
D\mathscr S_U(\mathcal R_JU)
=
\mathcal R_{J,\omega}A.
}
\]

This is exact and requires no asymptotic approximation beyond the already-certified scattering map itself.

---

## 3. Rotation tangent is a hard neutral mode

M19-075 identifies rotation as an exact neutral symmetry direction.
On the quasi-compact M19-095 hard splitting it belongs to the discrete unit/zero-growth hard fiber rather than the negative essential spectrum.

Therefore the M19-131 uniform observability estimate applies before rotation quotient:

\[
 c_{obs}\|\mathcal R_JU\|_H
\le
\|D\mathscr S_U(\mathcal R_JU)\|_{X_{sc}}
\le
C_{obs}\|\mathcal R_JU\|_H.
\]

Using rotation equivariance,

\[
\boxed{
 c_{obs}\|\mathcal R_JU\|_H
\le
\|\mathcal R_{J,\omega}A\|_{X_{sc}}
\le
C_{obs}\|\mathcal R_JU\|_H.
}
\]

Thus compact-core rotational anisotropy and critical-tail rotational anisotropy are uniformly equivalent on the certified hard corridor.

---

## 4. Close the M19-127 reverse-observability gap

M19-127 had only the safe implication

\[
\text{tail anisotropy}
\Longrightarrow
\text{finite spectator anisotropy},
\]

and warned that a strongly nonaxisymmetric compact core might conceivably have an almost-axisymmetric leading tail.

M19-144 rules out that silent decoupling for the **exact rotation tangent hard mode**:

\[
\boxed{
\|\mathcal R_JU\|_H>0
\Longrightarrow
\|\mathcal R_{J,\omega}A\|_{X_{sc}}
\ge c_{obs}\|\mathcal R_JU\|_H>0.
}
\]

Conversely a large tail rotation derivative forces a comparable hard interior rotation mode.

This statement is specific to the hard rotation tangent and should not be generalized automatically to arbitrary nonlinear core features.

---

## 5. Transfer the RSS compensation band to the tail

M19-115/Pineau--Vicol give the necessary moderate-RSS compensation, schematically

\[
0<c_0
\le
|\alpha|\,\|\mathcal R_JU\|_H
\le C_0
\]

on the relevant Type-I weighted hard lane.

Uniform norm equivalence now gives

\[
\boxed{
0<c_1
\le
|\alpha|\,
\|\mathcal R_{J,\omega}A\|_{X_{sc}}
\le C_1.
}
\]

Hence a surviving RSS critical tail cannot become axisymmetric faster than `1/|alpha|`, and it cannot carry arbitrarily large rotation-weighted tail anisotropy.

---

## 6. Combine with the exact RSS spiral shell cost

M19-125--126 give

\[
\partial_qA=-2\alpha\mathcal R_{J,\omega}A
\]

and

\[
\|\partial_qA-A\|_2^2
=
\|A\|_2^2
+4\alpha^2\|\mathcal R_{J,\omega}A\|_2^2.
\]

Thus the transferred lower bound implies a positive rotation-generated shell charge:

\[
\boxed{
4\alpha^2\|\mathcal R_{J,\omega}A\|^2
\ge c_2>0
}
\]

in any scattering/shell norm for which the retained finite-dimensional norm equivalence has been certified.

The moderate RSS tail therefore has a quantitatively nonzero spiral component, not merely a nonzero critical amplitude.

---

## 7. What this does not prove

A fixed positive critical shell charge is compatible with finite ancient enstrophy because the physical/log-radius ancestry weight decays.
Therefore

\[
\boxed{
\text{positive spiral shell cost}
\neq
\text{RSS contradiction}.
}
\]

The module closes an observability gap and converts the RSS hard core into a fully visible finite-dimensional spiral mode, but an additional signed or nonlinear rigidity argument is still required to eliminate that mode.

---

## 8. Updated moderate-RSS hard core

A surviving moderate RSS must now satisfy simultaneously

\[
\boxed{
\begin{aligned}
&A(q)=e^{-2\alpha q\mathcal R_{J,\omega}}A(0),\\
&0<c_1\le |\alpha|\|\mathcal R_{J,\omega}A\|_{X_{sc}}\le C_1,\\
&\text{positive cubic-tail mean},\\
&\text{finite-dimensional low-mode tail support at the hard level},\\
&\text{discrete finite-dimensional interior Floquet spectrum}.
\end{aligned}
}
\]

The unknown is no longer whether the rotating core is visible at infinity; it is whether such a finite-amplitude visible spiral mode can solve the full nonlinear similarity equation.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
