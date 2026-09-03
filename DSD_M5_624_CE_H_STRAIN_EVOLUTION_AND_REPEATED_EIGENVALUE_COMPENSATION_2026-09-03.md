# DSD M5-624 — CE-H strain evolution and repeated-eigenvalue compensation

Date: 2026-09-03

Status: **INTERNAL EXACT TENSOR COMPATIBILITY / THE SIMILARITY STRAIN EQUATION IS `D_B Sigma + Sigma^2 + R^2 + Sigma + Hess P = Delta Sigma`, WITH `R v=(1/2)W x v` / MATERIAL PRESERVATION OF THE CE-H VORTICITY EIGENLINE FORCES THE OFF-DIAGONAL PRESSURE-VISCOUS STRAIN CONDITION `P_perp(Delta Sigma-Hess P)xi=0` / AT A REPEATED STRAIN EIGENVALUE `spec Sigma={sigma,sigma,-2sigma}`, THE ROTATIONAL TERM `R^2` SPLITS THE TWO-DIMENSIONAL REPEATED EIGENSPACE BY EXACTLY `rho^2/4`; PERSISTENCE OF THE COLLISION THEREFORE REQUIRES AN EQUAL AND OPPOSITE PRESSURE-VISCOUS STRAIN ANISOTROPY OF SIZE `rho^2/4` / THUS EIGENVALUE COLLISION IS NOT A FREE DEGENERACY BUT A QUANTITATIVELY PAID TENSOR BRANCH / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Similarity velocity equation

Use

\[
\partial_\theta U
+\frac12U
+\frac12(y\cdot\nabla)U
+(U\cdot\nabla)U
=-\nabla P+\Delta U.
\]

With

\[
B=U+\frac12y,
\qquad
D_B=\partial_\theta+B\cdot\nabla,
\]

this is

\[
\boxed{
D_BU+\frac12U
=-\nabla P+\Delta U.
}
\]

---

## 2. Velocity-gradient equation

Let

\[
A:=\nabla U.
\]

For a transported gradient,

\[
D_B(\nabla U)
=\nabla(D_BU)-(\nabla U)(\nabla B)
\]

in matrix notation with the standard component convention.

Since

\[
\nabla B=A+\frac12I,
\]

one obtains

\[
\boxed{
D_BA+A^2+A+\nabla^2P=\Delta A.
}
\]

---

## 3. Symmetric strain equation

Decompose

\[
A=\Sigma+\mathcal R,
\]

where `Sigma` is symmetric and `R` antisymmetric.

The symmetric part of `A^2` is

\[
\operatorname{Sym}(A^2)=\Sigma^2+\mathcal R^2.
\]

Therefore

\[
\boxed{
D_B\Sigma
+\Sigma^2
+\mathcal R^2
+\Sigma
+\nabla^2P
=\Delta\Sigma.
}
\]

For incompressible three-dimensional flow,

\[
\mathcal Rv=\frac12W\times v,
\]

so

\[
\boxed{
\mathcal R^2
=\frac14\left(W\otimes W-|W|^2I\right).
}
\]

Define the pressure-viscous strain forcing

\[
\boxed{
\mathcal F_S:=\Delta\Sigma-\nabla^2P.
}
\]

Then

\[
\boxed{
D_B\Sigma
=\mathcal F_S-\Sigma^2-\Sigma-\mathcal R^2.
}
\]

---

## 4. Material preservation of the vorticity strain eigenline

On CE-H,

\[
\Sigma\xi=\sigma\xi,
\qquad
D_B\xi=0.
\]

Materially differentiate the eigenline:

\[
(D_B\Sigma)\xi
=(D_B\sigma)\xi.
\]

Hence

\[
\boxed{
P_\xi^\perp(D_B\Sigma)\xi=0.
}
\]

Now

\[
\Sigma^2\xi=\sigma^2\xi,
\qquad
\Sigma\xi=\sigma\xi.
\]

Also, because `W=rho xi`,

\[
\mathcal R^2\xi
=\frac14(\rho^2\xi-\rho^2\xi)=0.
\]

Therefore all algebraic terms are parallel to `xi`, and the transverse condition reduces exactly to

\[
\boxed{
P_\xi^\perp\mathcal F_S\xi=0.
}
\]

Equivalently,

\[
\boxed{
P_\xi^\perp(\Delta\Sigma-\nabla^2P)\xi=0.
}
\]

Thus the pressure Hessian and viscous strain Laplacian must cancel their transverse action on the material vorticity eigenline at every CE-H point.

---

## 5. Axial strain eigenvalue equation

Taking the `xi` component gives

\[
D_B\sigma
=\xi\cdot\mathcal F_S\xi
-\sigma^2-\sigma.
\]

Hence

\[
\boxed{
D_B\sigma+\sigma^2+\sigma
=\xi\cdot(\Delta\Sigma-\nabla^2P)\xi.
}
\]

This is the exact material scalar equation for the axial strain eigenvalue on CE-H.

---

## 6. Exact repeated-eigenvalue frame

Consider the exact collision branch from M5-623:

\[
\operatorname{spec}\Sigma
=\{\sigma,\sigma,-2\sigma\}.
\]

Choose an orthonormal eigenframe

\[
e_1=\xi,
\qquad e_2\perp\xi,
\qquad e_3\perp\operatorname{span}\{e_1,e_2\},
\]

such that

\[
\Sigma e_1=\sigma e_1,
\qquad
\Sigma e_2=\sigma e_2,
\qquad
\Sigma e_3=-2\sigma e_3.
\]

The repeated eigenspace is

\[
E=\operatorname{span}\{e_1,e_2\}.
\]

---

## 7. Rotational term splits the repeated eigenspace

Because

\[
W=\rho e_1,
\]

we have

\[
\mathcal R^2e_1=0.
\]

For `e2` transverse to `W`,

\[
\mathcal R^2e_2
=-\frac{\rho^2}{4}e_2.
\]

Thus the contribution `-R^2` in `D_B Sigma` is

\[
0
\quad\text{on }e_1,
\]

but

\[
+\frac{\rho^2}{4}
\quad\text{on }e_2.
\]

Therefore the vorticity rotation tensor **intrinsically tries to split the repeated strain eigenvalue** at rate `rho^2/4`.

---

## 8. Necessary compensation for persistence of multiplicity

If the repeated eigenvalue remains repeated for a nonzero material-time interval, first-order perturbation theory for a symmetric matrix requires the restriction of `D_B Sigma` to the repeated eigenspace to be scalar:

\[
\boxed{
E(D_B\Sigma)E
=(D_B\sigma)E.
}
\]

The terms `-Sigma^2-Sigma` are already scalar on `E`.

Hence the anisotropy from `-R^2` must be canceled by `F_S`.

Comparing the diagonal entries along `e1` and `e2`,

\[
e_2\cdot D_B\Sigma e_2
-e_1\cdot D_B\Sigma e_1
=0.
\]

Therefore

\[
e_2\cdot\mathcal F_Se_2
-e_1\cdot\mathcal F_Se_1
+\frac{\rho^2}{4}=0.
\]

Equivalently,

\[
\boxed{
 e_1\cdot\mathcal F_Se_1
-e_2\cdot\mathcal F_Se_2
=\frac{\rho^2}{4}.
}
\]

This is the exact collision-compensation identity.

---

## 9. Off-diagonal condition inside the repeated plane

Persistence also requires no first-order splitting through an off-diagonal entry in `E`:

\[
e_1\cdot D_B\Sigma e_2=0.
\]

The algebraic terms and `R^2` have zero `e1-e2` entry, so

\[
\boxed{
 e_1\cdot\mathcal F_Se_2=0.
}
\]

This is already contained in the general CE-H condition

\[
P_\xi^\perp\mathcal F_S\xi=0.
\]

---

## 10. Quantitative consequence on a coherent carrier

On a production-linked coherent carrier,

\[
\rho\ge\rho_*>0.
\]

If the exact-collision condition persists there, then

\[
\boxed{
\left|
 e_1\cdot\mathcal F_Se_1
-e_2\cdot\mathcal F_Se_2
\right|
\ge\frac{\rho_*^2}{4}.
}
\]

Thus repeated strain eigenvalues cannot form a free low-cost degeneracy.

They require a fixed pressure-viscous strain anisotropy.

Smooth thickening converts this into a fixed spacetime tensor charge unless the collision exists only instantaneously.

---

## 11. Instantaneous collision versus persistent collision

An isolated instant at which `g=0` need not satisfy the multiplicity-preservation identity beyond that instant.

Therefore the exact branch splits into

\[
\boxed{
EC
\Longrightarrow
EC_{crossing}
\lor
EC_{persistent}.
}
\]

- `EC_crossing`: the two eigenvalues cross/separate; immediately nearby times enter the simple-gap branch of M5-623 and pay strain-derivative/eigenframe activity.
- `EC_persistent`: multiplicity persists over a time interval and must pay the exact `rho^2/4` pressure-viscous anisotropy derived above.

Thus eigenvalue collision does not remove the forced branch; it converts it into either a simple-gap crossing or a fixed tensor-compensation channel.

---

## 12. Updated CE-H frontier

Combining M5-621--624,

\[
\boxed{
E_{CEH}
\Longrightarrow
T_{viscous\ flux}^{curvature}
\lor
F_{\nabla\kappa}
\lor
SG_{\nabla\Sigma}^{gap}
\lor
EC_{PV\ compensation}
\lor
H_{Burgers-like}.
}
\]

Here `EC_PV compensation` denotes the pressure-viscous strain anisotropy required to keep a repeated strain eigenvalue.

---

## 13. Audit firewall

The identity

\[
 e_1\cdot\mathcal F_Se_1
-e_2\cdot\mathcal F_Se_2
=\rho^2/4
\]

requires multiplicity to persist in material time. It is not imposed on a merely instantaneous eigenvalue crossing.

No contradiction is claimed from the existence of pressure-Hessian compensation; the result only makes its required size explicit.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
