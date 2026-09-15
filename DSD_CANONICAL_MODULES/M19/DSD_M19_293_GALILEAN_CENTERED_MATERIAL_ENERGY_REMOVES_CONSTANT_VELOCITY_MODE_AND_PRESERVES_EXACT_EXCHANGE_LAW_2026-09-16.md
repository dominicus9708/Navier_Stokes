# M19-293 — Galilean-centered material energy removes the constant-velocity mode and preserves an exact exchange law

**Date:** 2026-09-16  
**Status:** CALCULATION / GALILEAN FIREWALL / CENTERED MATERIAL ENERGY

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-292 reduces the gauge-invariant closed-core production-conditioned lag balance to

\[
\nu D_{core}-\frac12E_{core}
\]

plus possible external/background exchange.

However the vorticity-production event is Galilean invariant, while the uncentered kinetic energy \(E_{core}\) is not. Therefore no canonical sign transfer from vorticity production to the uncentered kinetic surplus is possible without fixing a frame.

This module removes the constant-velocity mode by deriving the exact material law for mean-subtracted kinetic energy.

## 2. Material population mass and momentum

Let \(\eta\) be a smooth material cutoff:

\[
D_B\eta=0,
\qquad
B=U+\frac12y,
\qquad
\nabla\cdot B=\frac32.
\]

Define

\[
M_\eta:=\int\eta\,dy,
\]

and the vector momentum

\[
\mathbf P_\eta:=\int\eta U\,dy.
\]

The material transport formula gives

\[
\boxed{M_\eta'=\frac32M_\eta.}
\]

Define the population mean velocity

\[
\boxed{\bar U_\eta:=\frac{\mathbf P_\eta}{M_\eta}.}
\]

## 3. Material momentum law

The similarity momentum equation in material form is

\[
D_BU
+\frac12U
+\nabla P
=\nu\Delta U.
\]

Hence

\[
\begin{aligned}
\mathbf P_\eta'
&=
\int\eta\left(D_BU+\frac32U\right)dy\\
&=
\mathbf P_\eta
+\int P\nabla\eta\,dy
-\nu\int \nabla\eta\cdot\nabla U\,dy.
\end{aligned}
\]

Define the vector material-momentum exchange

\[
\boxed{
\mathbf X_M[\eta]
:=
\int P\nabla\eta\,dy
-\nu\int \nabla\eta\cdot\nabla U\,dy.
}
\]

Then

\[
\boxed{\mathbf P_\eta'=\mathbf P_\eta+\mathbf X_M[\eta].}
\]

## 4. Galilean-centered kinetic energy

Define

\[
\boxed{
K_\eta
:=
\frac12\int\eta|U-\bar U_\eta|^2dy.
}
\]

Equivalently,

\[
\boxed{
K_\eta
=E_\eta-rac{|\mathbf P_\eta|^2}{2M_\eta},
}
\]

where

\[
E_\eta=\frac12\int\eta|U|^2dy.
\]

Under a constant Galilean velocity shift

\[
U\mapsto U+V,
\]

one has

\[
\bar U_\eta\mapsto\bar U_\eta+V,
\]

so

\[
\boxed{K_\eta\text{ is Galilean invariant}.}
\]

## 5. Derivative of the mean-mode energy

Let

\[
C_\eta:=\frac{|\mathbf P_\eta|^2}{2M_\eta}.
\]

Using

\[
M_\eta'=\frac32M_\eta,
\qquad
\mathbf P_\eta'=\mathbf P_\eta+\mathbf X_M,
\]

gives

\[
\boxed{
C_\eta'
=
\frac14M_\eta|\bar U_\eta|^2
+\bar U_\eta\cdot\mathbf X_M[\eta].
}
\]

## 6. Exact centered-energy law

M19-284 gives

\[
E_\eta'
=
\frac12E_\eta
+X_P[\eta]
+X_\nu[\eta]
-\nu D_U[\eta].
\]

Subtracting the mean-mode law and using

\[
E_\eta
=K_\eta+rac12M_\eta|\bar U_\eta|^2
\]

cancels the mean-mode similarity term exactly. We obtain

\[
\boxed{
K_\eta'
=
\frac12K_\eta
+X_P^\circ[\eta]
+X_\nu^\circ[\eta]
-\nu D_U[\eta],
}
\]

where

\[
\boxed{
X_P^\circ[\eta]
:=
\int P\,(U-\bar U_\eta)\cdot\nabla\eta\,dy,
}
\]

and

\[
\boxed{
X_\nu^\circ[\eta]
:=
-\nu\int
\nabla\eta\cdot
\nabla\left(\frac12|U-\bar U_\eta|^2\right)dy.
}
\]

Because \(\bar U_\eta\) is spatially constant,

\[
D_U[\eta]
=
\int\eta|\nabla(U-\bar U_\eta)|^2dy.
\]

Thus the centered law has exactly the same structural form as the uncentered material-energy law.

## 7. Pressure-gauge invariance

Under

\[
P\mapsto P+C(\theta),
\]

the centered pressure exchange changes by

\[
C\int(U-\bar U_\eta)\cdot\nabla\eta\,dy.
\]

But

\[
\int(U-\bar U_\eta)\cdot\nabla\eta
=-\int\eta\nabla\cdot(U-\bar U_\eta)=0.
\]

Hence

\[
\boxed{X_P^\circ[\eta]\text{ is pressure-gauge invariant}.}
\]

All terms in the centered law are therefore both pressure-gauge safe and Galilean safe.

## 8. Production-conditioned centered-energy identity

With the same lagged production marker \(m_h\), invariant integration by parts gives

\[
\boxed{
\begin{aligned}
\langle m_h'K_\eta\rangle
={}&
-\frac12\langle m_hK_\eta\rangle\\
&-\langle m_h(X_P^\circ+X_\nu^\circ)\rangle
+\nu\langle m_hD_U\rangle.
\end{aligned}
}
\]

This is the correct local material quantity to compare with the Galilean-invariant M5-589 vorticity-production event.

## 9. New firewall

At a purely kinematic level, adding a constant velocity component changes uncentered kinetic energy but leaves

\[
W,
\quad
\Sigma,
\quad
W\cdot\Sigma W,
\quad
|\nabla W|^2
\]

unchanged. Therefore no theorem of the form

\[
\text{positive vorticity production}
\Rightarrow
\nu D-\frac12E>c
\]

can be frame-independent when \(E\) is uncentered.

The canonical quantity must instead use \(K_\eta\) or an explicitly fixed Galilean frame.

## 10. Next target

On a bounded nondegenerate material population, a Poincare-type inequality may relate

\[
K_\eta
\quad\text{to}\quad
D_U[\eta].
\]

If one can prove a uniform population Poincare constant \(C_P\), then

\[
K_\eta\le C_PD_U
\]

and

\[
\nu D_U-\frac12K_\eta
\ge
\left(\nu-\frac{C_P}{2}\right)D_U.
\]

This has a sign only if the dimensionless geometry satisfies a genuine spectral-gap condition such as \(C_P<2\nu\). It is not automatic.

Therefore the next audit should determine whether the persistent production-paying material populations have a certified uniform Poincare/spectral gap, or whether geometry/decompactification allows \(C_P\) to remain too large.

---

\[
\boxed{\text{M19-293 COMPLETE; GALILEAN CENTERING REMOVES THE CONSTANT-VELOCITY LOW-FREQUENCY FIREWALL AND IS REQUIRED BEFORE COMPARING KINETIC DISSIPATION SURPLUS WITH VORTICITY PRODUCTION.}}
\]
