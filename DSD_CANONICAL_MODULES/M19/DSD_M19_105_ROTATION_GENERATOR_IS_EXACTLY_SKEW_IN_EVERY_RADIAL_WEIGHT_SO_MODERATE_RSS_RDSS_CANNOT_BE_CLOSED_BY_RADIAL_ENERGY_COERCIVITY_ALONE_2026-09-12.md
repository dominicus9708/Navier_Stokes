# DSD M19-105 — Rotation generator is exactly skew in every radial weight, so moderate RSS/RDSS cannot be closed by radial energy coercivity alone

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / EXACT ROTATING-FRAME ENERGY IDENTITY / THE ROTATION RATE DROPS OUT OF THE SYMMETRIC PART OF EVERY RADIAL WEIGHTED L2 ENERGY / THIS EXPLAINS WHY A PARAMETER-INDEPENDENT MODERATE-ROTATION CLOSURE CANNOT COME FROM THE SAME RADIAL COERCIVITY ALONE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Rotation generator

Let

\[
A\in\mathfrak{so}(3),
\qquad
A^T=-A.
\]

The infinitesimal action of spatial rotation on a vector field `F` is

\[
\boxed{
\mathcal J_AF
:=
AF-(Ay)\cdot\nabla F.
}
\]

For an RSS profile with angular rate `alpha`, passing to the co-rotating similarity frame adds the linear term

\[
\alpha\mathcal J_A
\]

to the stationary/similarity generator.

For RDSS the same generator appears after choosing a rotating frame whose one-period holonomy equals the discrete rotation.

---

## 2. Radial weighted inner product

Let

\[
w(y)=w(|y|)>0
\]

be any radial weight for which the integrations below are justified.

Define

\[
\langle F,G\rangle_w
:=
\int_{\mathbb R^3}F\cdot G\,w\,dy.
\]

Since `A` is skew,

\[
F\cdot AF=0.
\]

Also

\[
(Ay)\cdot\nabla w(|y|)=0
\]

because `Ay` is tangent to spheres centered at the origin.

Moreover

\[
\nabla\cdot(Ay)=\operatorname{tr}A=0.
\]

Therefore

\[
\begin{aligned}
\langle F,\mathcal J_AF\rangle_w
&=
-\int F\cdot((Ay)\cdot\nabla F)w\,dy\\
&=-\frac12\int (Ay)\cdot\nabla(|F|^2)w\,dy\\
&=\frac12\int |F|^2\nabla\cdot(Ayw)\,dy\\
&=0.
\end{aligned}
\]

Hence

\[
\boxed{
\langle F,\mathcal J_AF\rangle_w=0
}
\]

for every radial weight.

By polarization,

\[
\boxed{
\mathcal J_A^*=-\mathcal J_A
\quad\text{in }L^2(w).
}
\]

---

## 3. Consequence for RSS weighted energy

Write the co-rotating linearized operator schematically as

\[
\mathcal L_{\alpha}
=
\mathcal L_{base}
+\alpha\mathcal J_A.
\]

Its symmetric part in the radial weighted space is

\[
\boxed{
\frac12(\mathcal L_\alpha+\mathcal L_\alpha^*)
=
\frac12(\mathcal L_{base}+\mathcal L_{base}^*).
}
\]

Therefore the direct radial weighted energy identity is exactly independent of the angular speed:

\[
\boxed{
\frac d{ds}\|W\|_{L^2(w)}^2
\text{ contains no direct signed contribution proportional to }\alpha.
}
\]

The same statement holds for the vorticity energy under a radial weight, with the appropriate vector rotation action.

---

## 4. Why this matters for M19-104

Pineau--Vicol obtain Liouville theorems for extreme rotation regimes using a robust weighted framework, but the elementary symmetric-part energy identity itself cannot distinguish

\[
|\alpha|\ll1,
\qquad
|\alpha|\sim1,
\qquad
|\alpha|\gg1.
\]

The dependence on `alpha` must enter through additional structure such as:

- the resolvent/transport geometry of the rotating operator;
- averaging along rapid rotation;
- perturbation from the nonrotating problem for small rate;
- parameter-dependent pressure/commutator estimates;
- or other non-energy identities.

Thus a hypothetical proof of the moderate-rotation regime cannot consist only of improving the numerical constant in the same radial energy estimate.

---

## 5. RDSS interpretation

For a relative-periodic orbit

\[
U(s+S)=Q_*\cdot U(s),
\]

choose an axis-angle logarithm

\[
Q_*=e^{S\alpha A}.
\]

After passing to the co-rotating frame, the orbit becomes `S`-periodic and the equation contains

\[
\alpha\mathcal J_A.
\]

Since this term is radial-energy skew,

\[
\boxed{
\text{the basic one-period radial energy balance is also independent of the rotation rate.}
}
\]

Hence moderate RDSS is not separated from ordinary DSS at the level of the symmetric radial energy trace.

---

## 6. New firewall

\[
\boxed{
\text{rotation parameter appears in the generator}
\not\Rightarrow
\text{rotation parameter appears in radial energy coercivity}.
}
\]

Therefore

\[
\boxed{
\text{moderate RSS/RDSS closure}
\text{ requires a genuinely non-symmetric or nonradial mechanism.}
}
\]

---

## 7. Next target

A natural next question is whether one can deliberately break radial symmetry in the multiplier/weight so that the rotation generator contributes a sign.

This must be audited carefully because rotation orbits are closed: an angular derivative of any single-valued positive weight has zero mean around a full orbit, suggesting a strong obstruction to obtaining a uniform sign from a stationary anisotropic weight.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
