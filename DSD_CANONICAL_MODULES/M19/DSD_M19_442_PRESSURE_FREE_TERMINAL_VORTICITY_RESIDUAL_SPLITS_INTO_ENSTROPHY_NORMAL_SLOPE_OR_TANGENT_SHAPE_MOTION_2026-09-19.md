# M19-442 — The pressure-free terminal vorticity residual splits into enstrophy-normal slope or enstrophy-tangent shape motion

Date: 2026-09-19  
Canonical ID: **M19-442**  
Status: **PRESSURE-FREE CURL-RESIDUAL GEOMETRY / A NONZERO TERMINAL VORTICITY-TIME DERIVATIVE NEED NOT CHANGE THE q-AVERAGED TERMINAL ENSTROPHY TO FIRST ORDER / THE CURL-VISIBLE BRANCH DECOMPOSES ORTHOGONALLY INTO AN ENSTROPHY-NORMAL SCALAR SLOPE AND AN ENSTROPHY-TANGENT SHAPE/DIRECTION MOTION / THE TERMINAL ENSTROPHY ODE HAS NO SIGN THAT ELIMINATES EITHER CHANNEL / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Curl-visible residual

On the non-dipole branch of M19-441 define

\[
\boxed{
D_\omega
:=
\mathcal K_3C.
}
\]

Then

\[
\partial_s\omega(x,0^-)
=
-r^{-4}D_\omega.
\]

Let

\[
B
=
B_A
\]

be the terminal vorticity coefficient,

\[
\omega(x,0^-)
=
r^{-2}B(q,\omega).
\]

The hard terminal component has

\[
\boxed{
b_2
:=
\left\langle
\|B\|_2^2
\right\rangle
>0.
}
\]

Assume the selected curl-visible branch has

\[
\boxed{
d_\omega
:=
\left\langle
\|D_\omega\|_2^2
\right\rangle
>0.
}
\]

## 2. Hilbert-space projection onto the vorticity state

Use the invariant-q sphere Hilbert inner product

\[
\langle X,Y\rangle_H
:=
\left\langle
\int_{S^2}
X\cdot Y,d\omega
\right\rangle_q.
\]

Define

\[
\boxed{
\chi_\omega
:=
\langle B,D_\omega\rangle_H.
}
\]

Let

\[
\alpha
:=
\frac{\chi_\omega}{b_2}.
\]

Decompose

\[
\boxed{
D_\omega
=
\alpha B
+
D_\omega^\perp,
}
\]

with

\[
\boxed{
\langle B,D_\omega^\perp\rangle_H=0.
}
\]

Then exactly

\[
\boxed{
d_\omega
=
\frac{\chi_\omega^2}{b_2}
+
\|D_\omega^\perp\|_H^2.
}
\]

## 3. Quantitative fork

Since

\[
d_\omega>0,
\]

at least one of

\[
\boxed{
|\chi_\omega|
\ge
\frac12
\sqrt{b_2d_\omega}
}
\]

or

\[
\boxed{
\|D_\omega^\perp\|_H^2
\ge
\frac34d_\omega
}
\]

holds after a harmless fixed choice of threshold.

Thus

\[
\boxed{
V_{res}^{curl}
\Longrightarrow
V_{norm}
\lor
V_{tan}.
}
\]

## 4. Normal branch is exactly a terminal enstrophy slope

The exact wedge vorticity coefficient satisfies

\[
G(0,q,\omega)=B(q,\omega).
\]

Differentiate the wedge curl formula at z=0.

Because

\[
F_z(0)=C
\]

and the \(-2z\partial_z\) term in \(\mathfrak D\) contributes the homogeneity shift needed for degree minus three,

\[
\boxed{
G_z(0)
=
\mathcal K_3C
=
D_\omega.
}
\]

Therefore

\[
\mathscr K_\omega(z)
=
\frac12
\left\langle
\|G(z)\|_2^2
\right\rangle
\]

satisfies

\[
\boxed{
\mathscr K_\omega'(0)
=
\chi_\omega.
}
\]

Hence \(V_{norm}\) is precisely a nonzero signed terminal enstrophy slope.

## 5. Tangent branch changes shape without first-order enstrophy change

On \(V_{tan}\), the large part of \(D_\omega\) is orthogonal to B in the invariant Hilbert metric.

Therefore it changes the vorticity state while contributing no first-order change to the scalar terminal enstrophy.

This is the vorticity analogue of the tangent-motion firewall found for F in M19-431--432.

Thus

\[
\boxed{
\|D_\omega\|>0
\not\Rightarrow
|\mathscr K_\omega'(0)|>0.
}
\]

A pressure-free vorticity residual can be predominantly projective.

## 6. Exact terminal enstrophy ODE

M5-585 gives

\[
\mathscr K_\omega'
+
2z\mathscr J_\omega'
+
3\mathscr J_\omega
=
\mathscr P_\omega
-
\mathscr Q_\omega.
\]

At z=0,

\[
\boxed{
\chi_\omega
+
3\mathscr J_\omega(0)
=
\mathscr P_\omega(0)
-
\mathscr Q_\omega(0).
}
\]

Therefore even on the normal branch, the sign of \(\chi_\omega\) is not determined by diffusion minus stretching alone.

The signed enstrophy flux can compensate it.

## 7. Direct operator decomposition

Since

\[
C
=
-\Delta v
+
(v\cdot\nabla)v
+
\nabla p,
\]

curl gives

\[
D_\omega
=
r^4
\operatorname{curl}
\left[
-\Delta v
+
(v\cdot\nabla)v
\right].
\]

Equivalently, in terminal vorticity variables,

\[
\boxed{
D_\omega
=
-\mathcal L_2B
+
\mathcal A(A,B)
-
\mathcal S(B,A),
}
\]

where

- \(\mathcal L_2B\) is viscous vorticity diffusion;
- \(\mathcal A\) is vorticity advection;
- \(\mathcal S\) is vortex stretching.

Pressure is absent.

## 8. Conservative and nonconservative pieces

The advection pairing is conservative:

\[
B\cdot\mathcal A(A,B)
=
\text{divergence of the vorticity-energy flux}.
\]

The diffusion pairing produces the usual positive derivative terms plus the homogeneity correction.

The stretching pairing

\[
\boxed{
B\cdot\mathcal S(B,A)
}
\]

is the genuinely nonconservative part.

However the exact terminal enstrophy identity shows that transport and homogeneity corrections can still compensate its sign.

Therefore pressure removal alone does not produce a one-way scalar law.

## 9. Normal branch consequences

If

\[
\chi_\omega>0,
\]

then terminal q-averaged vorticity enstrophy initially rises with wedge depth.

Since

\[
\mathscr K_\omega(z)\to0
\qquad
(z\to\infty),
\]

an interior enstrophy maximum is forced.

If

\[
\chi_\omega<0,
\]

the terminal enstrophy initially decreases, and no analogous new maximum is forced beyond the already existing M5-587 functional maximum.

Thus even the normal branch retains a sign fork.

## 10. Tangent branch is the harder pressure-free survivor

The tangent branch satisfies

\[
\boxed{
\langle B,D_\omega^\perp\rangle_H=0,
\qquad
\|D_\omega^\perp\|_H>0.
}
\]

It is invisible to scalar enstrophy at first order.

Any closure must therefore use projective information such as

- vorticity direction change;
- strain-eigenframe change;
- helicity-type coupling;
- higher tensor moments;
- or a second-order curvature of the enstrophy trajectory.

Another scalar enstrophy payer calculation will not see this branch.

## 11. Current corrected residual frontier

Combining M19-441--442,

\[
\boxed{
C^\perp_{mandatory}
\Longrightarrow
D_{dip}^{crit,cons}
\lor
V_{norm}^{curl}
\lor
V_{tan}^{curl}.
}
\]

The first is the classified pressure-harmonic firewall.

The second is a signed terminal enstrophy-slope branch.

The third is a pressure-free projective vorticity-motion branch.

All remain open.

## 12. Next target

The highest-value new object is now the tangent branch.

Define the normalized vorticity direction where \(|B|\neq0\),

\[
\xi_B
=
\frac{B}{|B|}.
\]

The orthogonal component of \(D_\omega\) controls the first wedge-depth change of \(\xi_B\):

\[
\partial_z\xi_B
=
\frac{
P_{\xi_B}^\perp D_\omega
}{|B|}
\quad
\text{at }z=0.
\]

The next calculation should quantify this relation on a robust high-vorticity subset and determine whether mandatory tangent curl residual forces a finite-depth vorticity-direction turnover that can be compared with the existing CE-H/projective geometry.

\[
\boxed{\text{M19-442 COMPLETE; THE PRESSURE-FREE CURL RESIDUAL SPLITS INTO ENSTROPHY-NORMAL SLOPE OR ENSTROPHY-TANGENT SHAPE MOTION.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
