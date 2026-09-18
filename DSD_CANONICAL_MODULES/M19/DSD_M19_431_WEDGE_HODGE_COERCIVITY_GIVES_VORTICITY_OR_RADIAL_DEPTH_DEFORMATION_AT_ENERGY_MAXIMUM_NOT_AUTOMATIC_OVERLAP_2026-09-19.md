# M19-431 — Wedge Hodge coercivity gives vorticity-or-radial/depth deformation at the energy maximum, not automatic energy–enstrophy overlap

Date: 2026-09-19  
Canonical ID: **M19-431**  
Status: **WEDGE-ADAPTED HODGE COERCIVITY / EXACT M5-8 TRANSFER WITH D=∂q-2z∂z / THE RESIDUAL-SLOPE ENERGY MAXIMUM FORCES EITHER SAME-DEPTH VORTICITY MASS OR A FIXED RADIAL/DEPTH DEFORMATION FLOOR / THEREFORE ENERGY MAXIMUM DOES NOT AUTOMATICALLY COINCIDE WITH THE M5-587 STRETCHING-DOMINANT SHELL / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-430

On the residual-slope master branch, M19-269 and M19-430 provide an energy maximum

\[
z_E\in[a_*,b_*],
\qquad
0<a_*<b_*<\infty,
\]

such that

\[
\boxed{
\mathscr E'(z_E)=0,
\qquad
\mathscr E(z_E)\ge e_*>0.
}
\]

Independently, M5-587 provides an enstrophy-production maximum

\[
z_\omega\in[a_*,b_*]
\]

with

\[
\boxed{
\mathscr Q_\omega(z_\omega)
-
\mathscr P_\omega(z_\omega)
=
\frac{\mathscr K_\omega(z_\omega)}
{2z_\omega}
>0.
}
\]

M19-430 traps both witnesses in one compact corridor, but does not prove overlap.

The first natural test is whether the energy maximum itself must carry vorticity.

## 2. Exact wedge incompressibility

M5-582 gives

\[
\boxed{
(\mathfrak D+1)F_r
+
\operatorname{div}_{S^2}F_T
=
0,
}
\]

where

\[
\boxed{
\mathfrak D
=
\partial_q-2z\partial_z.
}
\]

The operator \(\mathfrak D\) is the normalized radial derivative at fixed physical time:

\[
r\partial_rF\big|_s
=
\mathfrak DF.
\]

Thus the ordinary cross-radius Hodge calculation of M5-8 transfers to each fixed wedge depth with \(\partial_\rho\) replaced by \(\mathfrak D\).

## 3. Exact wedge vorticity formula

The physical vorticity has the form

\[
\omega
=
r^{-2}G(z,q,\omega).
\]

The normalized coefficient is

\[
\boxed{
G
=
\left(
\operatorname{curl}_{S^2}F_T
\right)e_r
+
e_r\times
\left(
\mathfrak DF_T
-
\nabla_{S^2}F_r
\right),
}
\]

up to the fixed orientation convention of the sphere curl.

Therefore

\[
\boxed{
\|G\|_2^2
=
\|
\operatorname{curl}_{S^2}F_T
\|_2^2
+
\|
\mathfrak DF_T
-
\nabla_{S^2}F_r
\|_2^2.
}
\]

This is the exact wedge analogue of M5-8.

## 4. Fixed-depth spherical Hodge coercivity

The physical flux through every sphere is zero, so

\[
\boxed{
\int_{S^2}F_r,d\omega=0.
}
\]

Scalar Poincare gives

\[
\|F_r\|_2
\le
C
\|\nabla_{S^2}F_r\|_2.
\]

From the vorticity formula,

\[
\|\nabla_SF_r\|_2
\le
\|\mathfrak DF_T\|_2
+
\|G\|_2.
\]

For tangential fields, the Hodge--Poincare estimate on \(S^2\) gives

\[
\|F_T\|_2
\le
C
\left(
\|\operatorname{div}_SF_T\|_2
+
\|\operatorname{curl}_SF_T\|_2
\right).
\]

Using incompressibility,

\[
\operatorname{div}_SF_T
=
-(\mathfrak D+1)F_r,
\]

and absorbing the zeroth-order radial term with the preceding scalar estimate yields

\[
\boxed{
\|F\|_{L^2(S^2)}^2
\le
C_H
\left[
\|\mathfrak DF\|_{L^2(S^2)}^2
+
\|G\|_{L^2(S^2)}^2
\right].
}
\]

Equivalently,

\[
\boxed{
\|\mathfrak DF\|_2^2
+
\|G\|_2^2
\ge
c_H\|F\|_2^2,
}
\]

for one universal spherical Hodge constant \(c_H>0\).

## 5. q-averaged wedge form

Take the invariant q-mean at one fixed depth z.

Define

\[
\boxed{
\mathscr X(z)
:=
\left\langle
\|\mathfrak DF(z)\|_2^2
\right\rangle_q,
}
\]

and recall

\[
\boxed{
\mathscr K_\omega(z)
=
\frac12
\left\langle
\|G(z)\|_2^2
\right\rangle_q,
}
\]

\[
\boxed{
\mathscr E(z)
=
\frac12
\left\langle
\|F(z)\|_2^2
\right\rangle_q.
}
\]

Then

\[
\boxed{
\mathscr X(z)
+
2\mathscr K_\omega(z)
\ge
2c_H\mathscr E(z).
}
\]

At \(z=z_E\),

\[
\boxed{
\mathscr X(z_E)
+
2\mathscr K_\omega(z_E)
\ge
2c_He_*.
}
\]

Therefore at least one of

\[
\boxed{
\mathscr K_\omega(z_E)
\ge
\frac{c_He_*}{2}
}
\]

or

\[
\boxed{
\mathscr X(z_E)
\ge
c_He_*
}
\]

must hold.

## 6. First branch — same-depth vorticity floor

If

\[
\mathscr K_\omega(z_E)
\ge
\frac{c_He_*}{2},
\]

then the energy maximum itself lies on a sphere carrying a fixed positive q-averaged vorticity-enstrophy density.

This is a genuine energy–vorticity same-depth overlap:

\[
\boxed{
\mathscr E(z_E)>0,
\qquad
\mathscr K_\omega(z_E)>0.
}
\]

However it is still weaker than the M5-587 production-shell condition

\[
\mathscr Q_\omega
-
\mathscr P_\omega
>0.
\]

Positive vorticity mass does not determine the sign of stretching minus vorticity-gradient dissipation.

Thus even this branch does not yet prove

\[
z_E=z_\omega.
\]

## 7. Second branch — radial/depth deformation floor

If the vorticity floor is not large enough, then

\[
\boxed{
\mathscr X(z_E)
=
\left\langle
\|\mathfrak DF(z_E)\|_2^2
\right\rangle
\ge
c_He_*.
}
\]

This is a fixed scale-critical deformation in the direction

\[
\mathfrak D
=
\partial_q-2z\partial_z.
\]

It is not an angular-vorticity charge.

Hence the energy maximum can support its Hodge formation cost through fixed-time radial/depth deformation rather than through large vorticity.

This is the exact wedge version of the M5-8 radial-reformation escape.

## 8. Orthogonality at the energy maximum

At arbitrary depth,

\[
\begin{aligned}
\left\langle
\int F\cdot\mathfrak DF
\right\rangle_q
&=
\left\langle
\int F\cdot\partial_qF
\right\rangle_q
-
2z
\left\langle
\int F\cdot\partial_zF
\right\rangle_q
\\
&=
-2z\mathscr E'(z),
\end{aligned}
\]

because the q-derivative averages to zero.

Therefore at the energy maximum,

\[
\boxed{
\left\langle
\int F\cdot\mathfrak DF
\right\rangle_{z_E}
=
0.
}
\]

Thus the deformation branch is not simply amplitude growth or decay.

It is mean-orthogonal to the state itself at the maximum and can represent a phase/shape motion along the constant-energy surface.

This is precisely why the scalar condition \(\mathscr E'(z_E)=0\) cannot eliminate it.

## 9. Relation to the energy dissipation identity

M19-269 gives at the energy maximum

\[
\boxed{
\mathscr D(z_E)
=
2\mathscr E(z_E)
+
\mathscr X(z_E)
+
\left\langle
\|\nabla_{S^2}F(z_E)\|_2^2
\right\rangle.
}
\]

Hence

\[
\mathscr D(z_E)>0
\]

does not by itself imply a vorticity floor.

The positive dissipation can be carried by

- radial/depth deformation \(\mathscr X\);
- angular strain/gradient structure;
- vorticity;

with the Hodge relation only forcing the vorticity-or-deformation alternative above.

Therefore the shortcut

\[
\boxed{
\mathscr D(z_E)>0
\Longrightarrow
\mathscr K_\omega(z_E)>0\text{ quantitatively}
}
\]

is not certified.

## 10. Correct overlap frontier

M19-430's target

\[
\mathcal T_{overlap}^{E\omega}
\]

must therefore be refined to

\[
\boxed{
\mathcal T_{overlap}^{E\omega}
\quad\lor\quad
\mathcal R_{\mathfrak D}^{deform},
}
\]

where

\[
\boxed{
\mathcal R_{\mathfrak D}^{deform}:
\mathscr X(z_E)
\ge
c_He_*.
}
\]

On the first branch one still needs a sign theorem connecting vorticity mass to

\[
\mathscr Q_\omega-\mathscr P_\omega.
\]

On the second branch one must classify the radial/depth deformation itself.

## 11. Next calculation

The deformation is

\[
\mathfrak DF
=
\partial_qF-2z\partial_zF.
\]

On the compact corridor \(z\in[a_*,b_*]\), a quantitative lower bound on \(\mathfrak DF\) forces at least one of

\[
\partial_qF
\]

or

\[
\partial_zF
\]

to be large.

These are already typed objects:

- \(\partial_qF\): recurrent scale/log-phase motion;
- \(\partial_zF\): parabolic depth/time-jet activity, physically an acceleration channel.

The next step is to split \(\mathcal R_{\mathfrak D}^{deform}\) quantitatively into those two channels and compare each with the existing criticality firewalls.

\[
\boxed{\text{M19-431 COMPLETE; WEDGE HODGE COERCIVITY GIVES A VORTICITY-OR-DEFORMATION FORK, SO SAME-DEPTH ENERGY–ENSTROPHY OVERLAP IS NOT AUTOMATIC.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
