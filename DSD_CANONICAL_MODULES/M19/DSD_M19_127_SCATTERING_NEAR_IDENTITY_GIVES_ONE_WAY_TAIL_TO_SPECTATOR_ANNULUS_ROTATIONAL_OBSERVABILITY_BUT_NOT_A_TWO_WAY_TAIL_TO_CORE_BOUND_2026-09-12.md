# DSD M19-127 — Scattering near identity gives one-way tail-to-spectator-annulus rotational observability but not a two-way tail-to-core bound

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / M19-069 SCATTERING LINEARIZATION APPLIED TO THE ROTATION GENERATOR / NONZERO FAR-FIELD ROTATIONAL ANISOTROPY FORCES NONZERO ANISOTROPY AT A FINITE SPECTATOR ANNULUS, BUT THE REVERSE CONTROL OF THE WHOLE GAUSSIAN CORE BY THE TAIL IS NOT CURRENTLY CERTIFIED / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Spectator scattering map

At a fixed large spectator radius `R_spec`, write the critical annular profile

\[
V_{spec}(\xi)
:=
R_{spec}U(R_{spec}\xi,s_{spec})
\]

on a fixed reference annulus.

M5-563/567 and M19-069 give the scattering relation

\[
\boxed{
A
=
V_{spec}
+\mathcal E_{spec},
}
\]

with

\[
\|\mathcal E_{spec}\|_X
\le C R_{spec}^{-2}
\]

in the retained strong spectator norm `X`.

At the linearized level,

\[
D\mathscr S_{R_{spec}}
=I+O(R_{spec}^{-2}).
\]

---

## 2. Rotation commutes with scaling and scattering

Let

\[
\mathcal R
]

be the physical/vector rotation generator and

\[
\mathcal R_\omega
\]

its induced action on the angular scattering datum.

Scaling commutes with rotation, so

\[
\boxed{
\mathcal R_\xi V_{spec}(\xi)
=
R_{spec}\,
(\mathcal R U)(R_{spec}\xi,s_{spec}).
}
\]

Rotation equivariance of the scattering construction gives, in the same strong corridor,

\[
\boxed{
\mathcal R_\omega A
=
\mathcal R_\xi V_{spec}
+\mathcal E_{rot},
}
\]

where the differentiated Duhamel/scattering error obeys schematically

\[
\|\mathcal E_{rot}\|_X
\le C_{rot}R_{spec}^{-2}
\]

provided the corresponding rotational derivative of the spectator residual is uniformly bounded.

This is exactly the same strong-norm certification required for the `I+O(R^-2)` scattering derivative in M19-069.

---

## 3. Tail-to-annulus lower observability

Therefore

\[
\boxed{
\|\mathcal R_\xi V_{spec}\|_X
\ge
\|\mathcal R_\omega A\|_X
-C_{rot}R_{spec}^{-2}.
}
\]

If the RSS tail has a fixed rotational defect

\[
\|\mathcal R_\omega A\|_X
\ge a_*>0,
\]

choose the spectator radius so large that

\[
C_{rot}R_{spec}^{-2}\le a_*/2.
\]

Then

\[
\boxed{
\|\mathcal R_\xi V_{spec}\|_X
\ge a_*/2.
}
\]

Thus a genuinely nonaxisymmetric critical RSS tail cannot be produced from an asymptotically axisymmetric spectator boundary profile.

---

## 4. Convert to physical annulus norm

For example, in `L2` on the reference annulus,

\[
\begin{aligned}
\|\mathcal R_\xi V_{spec}\|_{L^2(A_1)}^2
&=
R_{spec}^{-1}
\int_{A_{R_{spec}}}
|\mathcal R U(y,s_{spec})|^2dy.
\end{aligned}
\]

Hence

\[
\boxed{
\int_{A_{R_{spec}}}
|\mathcal R U|^2dy
\gtrsim
R_{spec}
\left(
\|\mathcal R_\omega A\|_{L^2(S^2)}
-O(R_{spec}^{-2})
\right)^2
}
\]

up to the fixed-annulus/radial-phase norm convention.

Because the Gaussian weight is strictly positive on every fixed finite annulus, this also gives a positive, though potentially exponentially small in `R_spec`, contribution to the Pineau--Vicol Gaussian rotational-defect norm.

---

## 5. One-way comparison with the Gaussian core norm

Let

\[
\mu(y)=e^{-|y|^2/4}.
\]

On the annulus

\[
R_{spec}<|y|<2R_{spec},
\]

\[
\mu(y)
\ge e^{-R_{spec}^2}
\]

up to an inessential fixed constant in the exponent.

Therefore

\[
\boxed{
\|\mathcal RU\|_{L^2_\mu}
\ge
c(R_{spec})
\|\mathcal R_\omega A\|_{L^2(S^2)}
-O(R_{spec}^{-2}),
}
\]

for a positive but very small constant

\[
c(R_{spec})>0.
\]

Thus a nonzero tail defect forces a nonzero global Gaussian rotational defect.

---

## 6. Why the reverse estimate is not certified

The desired converse would be something like

\[
\boxed{
\|\mathcal RU\|_{L^2_\mu}
\le
C\|\mathcal R_\omega A\|_X.
}
\]

Nothing currently proved implies this.

The Gaussian norm strongly weights the compact core. A profile may in principle have substantial nonaxisymmetric rotational defect in a bounded region while its leading critical tail is much closer to axisymmetric.

The scattering map describes outward propagation from a finite spectator boundary to infinity; it does not by itself reconstruct all compact-core anisotropy from the leading tail coefficient.

Hence

\[
\boxed{
\text{tail anisotropy controls one finite annulus}
\not\Rightarrow
\text{tail anisotropy controls the whole core}.
}
\]

---

## 7. What would be needed for two-way observability

A reverse estimate would require an additional theorem, for example:

1. a unique-continuation estimate for the rotational symmetry tangent
   \[
   Z=\mathcal RU;
   \]
2. a Carleman/three-sphere inequality propagating rotational anisotropy from infinity into the Gaussian core;
3. a stationary RSS elliptic resolvent estimate ruling out a localized nonaxisymmetric kernel with vanishing leading scattering data.

No such theorem is currently certified in M19.

---

## 8. Consequence for M19-115 and M19-126

M19-115 gives the interior compensation floor

\[
|\alpha|\|\mathcal RU\|_{L^2_\mu}
\ge c_0.
\]

M19-126 gives a far-field shell charge containing

\[
4\alpha^2\|\mathcal R_\omega A\|_2^2.
\]

M19-127 connects these only in the **tail-to-interior lower direction**.

That is not enough to turn the two inequalities into a contradiction.

Therefore the tail/core matching problem remains genuine.

---

## 9. Revised moderate-RSS target

The most concrete new bridge is

\[
\boxed{
\mathcal T_{obs}:
\text{prove a quantitative reverse observability/unique-continuation estimate for }Z=\mathcal RU.
}
\]

If successful, the interior compensation band and the spiral shell-charge law would become a single global constraint.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
