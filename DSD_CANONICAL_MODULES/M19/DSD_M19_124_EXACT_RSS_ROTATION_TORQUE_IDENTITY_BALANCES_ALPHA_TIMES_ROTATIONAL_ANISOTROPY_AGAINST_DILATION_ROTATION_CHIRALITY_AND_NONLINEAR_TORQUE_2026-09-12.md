# DSD M19-124 — Exact RSS rotation-torque identity balances alpha times rotational anisotropy against dilation-rotation chirality and nonlinear torque

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / NEW SIGNED IDENTITY FOR THE MODERATE-RSS HARD CORE / UNLIKE RADIAL ENERGY, PAIRING THE CO-ROTATING PROFILE EQUATION WITH THE ROTATION GENERATOR EXPOSES ALPHA EXPLICITLY / THE PRICE IS TWO SIGNED TORQUE TERMS WITH NO PRESENT DEFINITE SIGN / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Co-rotating RSS profile equation

Write the RSS profile equation as

\[
\boxed{
\alpha\mathcal R U
+\mathcal D U
-\nu\Delta U
+(U\cdot\nabla)U
+\nabla P
=0,
}
\]

where

\[
\mathcal R U
:=AU-(Ay)\cdot\nabla U,
\qquad A^T=-A,
\]

and

\[
\mathcal D
:=\frac12I+\frac12y\cdot\nabla.
\]

Assume the retained RSS profile has sufficient decay/smoothness for the integrations by parts below.

---

## 2. Split the dilation operator into symmetric and skew parts

On unweighted `L2(R3)`,

\[
(y\cdot\nabla)^*
=-y\cdot\nabla-3.
\]

Hence

\[
\mathcal D
=-\frac14I+\mathcal K,
\]

where

\[
\boxed{
\mathcal K
:=\frac34I+\frac12y\cdot\nabla
}
\]

is skew-adjoint:

\[
\mathcal K^*=-\mathcal K.
\]

Dilation and rotation commute:

\[
\boxed{[\mathcal K,\mathcal R]=0.}
\]

The scalar symmetric part `-1/4 I` is orthogonal to the rotation tangent because

\[
\langle U,\mathcal R U\rangle=0.
\]

Therefore

\[
\boxed{
\langle\mathcal D U,\mathcal R U\rangle
=
\langle\mathcal K U,\mathcal R U\rangle.
}
\]

This term need not vanish: two commuting skew generators can have a nonzero self-adjoint product.

---

## 3. Viscous and pressure terms vanish in the rotation pairing

The Laplacian is self-adjoint and rotationally invariant:

\[
[\Delta,\mathcal R]=0.
\]

Thus

\[
\begin{aligned}
\langle-\nu\Delta U,\mathcal R U\rangle
&=\nu\langle\nabla U,\nabla\mathcal R U\rangle\\
&=0,
\end{aligned}
\]

because the Dirichlet energy is rotation-invariant and `R U` is its infinitesimal rotation tangent.

Also `R U` is divergence-free whenever `U` is, so

\[
\boxed{
\langle\nabla P,\mathcal R U\rangle=0.
}
\]

---

## 4. Exact torque identity

Take the `L2` pairing of the RSS equation with

\[
\mathcal R U.
\]

Using Sections 2--3 gives

\[
\boxed{
\alpha\|\mathcal R U\|_2^2
+
\langle\mathcal K U,\mathcal R U\rangle
+
\int_{\mathbb R^3}
(U\cdot\nabla)U\cdot\mathcal R U\,dy
=0.
}
\]

Define the signed dilation-rotation chirality

\[
\boxed{
\mathfrak C_{DR}(U)
:=
\langle\mathcal K U,\mathcal R U\rangle
}
\]

and nonlinear rotational torque

\[
\boxed{
\mathfrak T_{NL}(U)
:=
\int(U\cdot\nabla)U\cdot\mathcal R U\,dy.
}
\]

Then

\[
\boxed{
\alpha\|\mathcal R U\|_2^2
=
-\mathfrak C_{DR}(U)
-\mathfrak T_{NL}(U).
}
\]

This is an exact signed RSS identity.

---

## 5. Interpretation of the chirality term

Because

\[
\mathcal K^*=-\mathcal K,
\qquad
\mathcal R^*=-\mathcal R,
\qquad
[\mathcal K,\mathcal R]=0,
\]

the product

\[
\mathcal K\mathcal R
\]

is self-adjoint.

Indeed

\[
\mathfrak C_{DR}(U)
=-\langle U,\mathcal K\mathcal R U\rangle.
\]

Thus `C_DR` is a genuine signed quadratic observable measuring correlation between radial dilation phase and angular rotation phase.

It vanishes for profiles whose radial dependence and angular orientation are separated in a way that carries no dilation-rotation phase correlation, but it need not vanish for a spiral/chiral profile.

---

## 6. Nonlinear torque has no automatic zero identity

The Navier--Stokes nonlinearity is rotation-equivariant and energy conserving, but these facts do **not** imply

\[
\mathfrak T_{NL}(U)=0.
\]

The trilinear identity

\[
b(U,U,U)=0
\]

only yields a tautological cancellation after differentiating by rotation; it does not force

\[
b(U,U,\mathcal R U)
\]

to vanish.

Hence the nonlinear torque must be retained as an independent signed term.

---

## 7. Necessary balance for moderate RSS

Every nontrivial RSS with

\[
\mathcal R U\ne0
\]

must satisfy

\[
\boxed{
|\alpha|\|\mathcal R U\|_2^2
\le
|\mathfrak C_{DR}(U)|
+|\mathfrak T_{NL}(U)|.
}
\]

Conversely, if one could prove on the Type-I corridor that

\[
\mathfrak C_{DR}(U)+\mathfrak T_{NL}(U)
\]

has a sign incompatible with `alpha`, or is strictly smaller than the left side in the moderate compensation band of M19-115, the RSS branch would close.

No such sign theorem is currently established.

---

## 8. Relation to M19-105--107

M19-105 showed that direct radial energy is blind to rotation.

M19-106 showed static anisotropic weighting cannot turn rotation itself into uniformly signed damping.

M19-107 showed the bare OU/diffusion generator commutes with rotation.

M19-124 explains where a usable `alpha`-dependent signed identity can nevertheless arise:

\[
\boxed{
\text{not from rotation alone, but from rotation paired against dilation phase and nonlinear torque.}
}
\]

This is a genuinely different mechanism from one-multiplier coercivity.

---

## 9. RDSS analogue

In a co-rotating frame for an RDSS orbit with constant chosen angular rate representative, the same pointwise-in-time identity acquires a time derivative/storage term.

After integration over one full periodic co-rotating cycle, the storage term cancels.

Thus a period-averaged analogue of

\[
\alpha\|\mathcal R U\|^2
+
\mathfrak C_{DR}
+
\mathfrak T_{NL}=0
\]

is expected, subject to the precise rotating-frame representation and integrability bookkeeping.

Because raw `alpha` has the winding ambiguity of M19-117, the RDSS use of this identity must be representation-aware.

---

## 10. New moderate-RSS theorem target

The moderate RSS Liouville problem can now be restated as a signed torque problem:

\[
\boxed{
\mathcal T_{torque}:
\text{exclude a Type-I profile satisfying simultaneously}
\begin{cases}
0<c_0\le|\alpha|\|\mathcal R U\|_{L^2_\mu}\le C_1,\\
\alpha\|\mathcal R U\|_2^2+\mathfrak C_{DR}(U)+\mathfrak T_{NL}(U)=0.
\end{cases}
}
\]

The next calculation should determine whether either signed torque term is an exact radial boundary flux and therefore can be evaluated from the known critical `1/r` tail.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
