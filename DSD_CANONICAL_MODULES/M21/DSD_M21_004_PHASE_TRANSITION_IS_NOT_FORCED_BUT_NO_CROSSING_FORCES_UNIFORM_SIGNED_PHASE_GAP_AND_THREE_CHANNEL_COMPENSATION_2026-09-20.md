# M21-004 — A longitudinal/transverse phase transition is not forced by the two finite-depth witnesses; absence of crossing forces a uniform signed phase gap and an exact three-channel compensation

Date: 2026-09-20  
Canonical ID: **M21-004**  
Status: **PHASE-TRANSITION AUDIT / THE ENSTROPHY-PRODUCTION WITNESS AND THE PROJECTIVE-COMPENSATION WITNESS DO NOT DETERMINE OPPOSITE SIGNS OF 6A-B / THEREFORE A CROSSING 6A=B IS NOT AUTOMATIC / ON THE COMPACT M21 CORRIDOR, IF NO CROSSING OCCURS THEN CONTINUITY GIVES A UNIFORM LONGITUDINAL- OR TRANSVERSE-DOMINATED PHASE GAP / THE M21-003 MIXED-MOMENT ODE CONVERTS THAT GAP INTO AN EXACT THREE-CHANNEL COMPENSATION BY ENDPOINT-TRANSPORT CURRENT, PRESSURE-DIFFUSION CORRELATION, OR SIGNED EXTENSION/COMPRESSION SEGREGATION / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Phase discriminant

Recall from M21-003

\[
\mathscr A(z)
=
\left\langle
\Gamma^2 E K
\right\rangle
\ge0,
\]

and

\[
\mathscr B(z)
=
\left\langle
E K^2
\right\rangle
\ge0.
\]

Define the finite-depth phase discriminant

\[
\boxed{
\mathscr H(z)
:=
6\mathscr A(z)-\mathscr B(z).
}
\]

Then:

- \(\mathscr H>0\): longitudinal-square dominated;
- \(\mathscr H<0\): transverse-projective-quartic dominated;
- \(\mathscr H=0\): internal strain transition.

The M21-003 ODE becomes

\[
\boxed{
\mathscr M'
+
2z\mathscr F_M'
+
9\mathscr F_M
=
\frac12\mathscr H
-
\mathscr C
-
\mathscr D.
}
\]

## 2. The two forced witnesses do not fix the sign of H

At the scalar enstrophy-production witness \(z_\omega\),

\[
\mathscr Q_\omega(z_\omega)
-
\mathscr P_\omega(z_\omega)
>0.
\]

Hence

\[
\mathscr Q_\omega(z_\omega)>0.
\]

This fixes a positive enstrophy-weighted mean axial stretching.

It does **not** determine the relative size of

\[
6\langle\Gamma^2EK\rangle
\]

and

\[
\langle EK^2\rangle.
\]

Therefore

\[
\boxed{
\operatorname{sign}\mathscr H(z_\omega)
\text{ is currently undetermined.}
}
\]

At the projective compensation witness \(z_{EK}\),

\[
\mathscr Z(z_{EK})>0,
\]

and

\[
\mathscr R(z_{EK})-2\mathscr G(z_{EK})>0.
\]

This fixes nontrivial transverse projective activity and a positive joint compensation gap.

It does **not** determine whether

\[
K
\]

is above or below the threshold \(6\Gamma^2\) in the weighted mean.

Therefore

\[
\boxed{
\operatorname{sign}\mathscr H(z_{EK})
\text{ is also currently undetermined.}
}
\]

## 3. No intermediate-value theorem is available yet

M21-001 places

\[
z_\omega,z_{EK}\in[a_{21},b_{21}].
\]

But because neither endpoint witness fixes the sign of \(\mathscr H\), the data do not provide

\[
\mathscr H(z_\omega)\mathscr H(z_{EK})<0.
\]

Therefore one cannot invoke continuity to conclude a crossing.

Hence

\[
\boxed{
\text{the existing two witnesses do not force }
\exists z_*:\mathscr H(z_*)=0.
}
\]

This is the principal M21-004 audit correction.

## 4. Exact dichotomy on the compact corridor

The wedge coefficients are smooth on the fixed corridor, so

\[
\mathscr H\in C([a_{21},b_{21}]).
\]

Therefore exactly one of the following occurs:

### Transition branch

\[
\boxed{
\exists z_*\in[a_{21},b_{21}]
:
\mathscr H(z_*)=0.
}
\]

### No-crossing branch

\[
\boxed{
\mathscr H(z)\neq0
\qquad
\forall z\in[a_{21},b_{21}].
}
\]

In the no-crossing branch, connectedness implies one fixed sign throughout the corridor.

Compactness then gives a uniform gap

\[
\boxed{
|\mathscr H(z)|
\ge
\delta_H>0
\qquad
\forall z\in[a_{21},b_{21}].
}
\]

Thus no crossing is much stronger than merely saying the sign happens not to change.

It forces a uniformly longitudinal-dominated or uniformly transverse-dominated finite-depth phase.

## 5. Natural weighted mixed current

Define

\[
\boxed{
\mathscr Y_M(z)
:=
z^{7/2}\mathscr M(z)
+
2z^{9/2}\mathscr F_M(z).
}
\]

Differentiate:

\[
\begin{aligned}
\mathscr Y_M'
={}&
\frac72 z^{5/2}\mathscr M
\\
&+
z^{7/2}
\left(
\mathscr M'
+
2z\mathscr F_M'
+
9\mathscr F_M
\right).
\end{aligned}
\]

Using the M21-003 ODE,

\[
\boxed{
\mathscr Y_M'
=
\frac12z^{7/2}\mathscr H
-
z^{7/2}(\mathscr C+\mathscr D)
+
\frac72z^{5/2}\mathscr M.
}
\]

This is the correct phase-current identity.

## 6. Integrated corridor identity

Let

\[
a:=a_{21},
\qquad
b:=b_{21}.
\]

Integrating Section 5 gives

\[
\boxed{
\begin{aligned}
\frac12
\int_a^b
z^{7/2}\mathscr H(z)\,dz
={}&
\mathscr Y_M(b)-\mathscr Y_M(a)
\\
&+
\int_a^b
z^{7/2}
(\mathscr C+\mathscr D)\,dz
\\
&-
\frac72
\int_a^b
z^{5/2}\mathscr M(z)\,dz.
\end{aligned}
}
\]

Define

\[
\boxed{
\Delta Y_M
:=
\mathscr Y_M(b)-\mathscr Y_M(a),
}
\]

\[
\boxed{
R_{PD}
:=
\int_a^b
z^{7/2}
(\mathscr C+\mathscr D)\,dz,
}
\]

and

\[
\boxed{
R_{\Gamma K}
:=
\frac72
\int_a^b
z^{5/2}\mathscr M(z)\,dz.
}
\]

Then

\[
\boxed{
\frac12
\int_a^b
z^{7/2}\mathscr H\,dz
=
\Delta Y_M+R_{PD}-R_{\Gamma K}.
}
\]

## 7. Uniform longitudinal phase compensation

Assume the no-crossing branch is longitudinal:

\[
\mathscr H(z)\ge\delta_H>0.
\]

Then

\[
\frac12
\int_a^b
z^{7/2}\mathscr H\,dz
\ge
L_H,
\]

where

\[
\boxed{
L_H
:=
\frac{\delta_H}{2}
\int_a^b z^{7/2}dz
>0.
}
\]

Hence

\[
\Delta Y_M+R_{PD}-R_{\Gamma K}
\ge
L_H.
\]

Therefore at least one of

\[
\boxed{
\Delta Y_M
\ge
\frac13L_H,
}
\]

\[
\boxed{
R_{PD}
\ge
\frac13L_H,
}
\]

or

\[
\boxed{
-R_{\Gamma K}
\ge
\frac13L_H
}
\]

must hold.

The third alternative means

\[
\boxed{
\int_a^b
z^{5/2}
\mathscr M(z)\,dz
<0.
}
\]

Since

\[
\mathscr M
=
\langle E\Gamma K\rangle,
\]

this is an integrated compressive/projective-segregation payment:

projective noncommutation is preferentially weighted toward \(\Gamma<0\) strongly enough to offset a uniformly longitudinal internal phase.

## 8. Uniform transverse phase compensation

Assume instead

\[
\mathscr H(z)\le-\delta_H<0.
\]

Then

\[
\frac12
\int_a^b
z^{7/2}\mathscr H\,dz
\le
-L_H.
\]

Hence

\[
\Delta Y_M+R_{PD}-R_{\Gamma K}
\le
-L_H.
\]

Therefore at least one of

\[
\boxed{
-\Delta Y_M
\ge
\frac13L_H,
}
\]

\[
\boxed{
-R_{PD}
\ge
\frac13L_H,
}
\]

or

\[
\boxed{
R_{\Gamma K}
\ge
\frac13L_H
}
\]

must hold.

The third alternative is an integrated extensional/projective-segregation payment:

\[
\boxed{
\int_a^b
z^{5/2}
\mathscr M(z)\,dz
>0.
}
\]

Thus a uniformly transverse internal phase must be balanced by projective activity preferentially weighted toward \(\Gamma>0\), or by endpoint/transport or pressure/diffusion compensation.

## 9. Meaning of the three compensators

The no-crossing branch therefore cannot remain an untyped phase label.

It must pay through at least one of:

### P1. Mixed-current transport

\[
\boxed{
\Delta Y_M.
}
\]

This records net finite-depth transport of the longitudinal/transverse mixed moment.

### P2. Pressure/diffusion correlation

\[
\boxed{
R_{PD}.
}
\]

This contains the typed correlations inherited from

\[
\mathscr C+\mathscr D,
\]

including pressure-Hessian, scalar diffusion, strain diffusion, and viscous projective coupling.

### P3. Signed phase segregation

\[
\boxed{
R_{\Gamma K}.
}
\]

This is the depth-integrated enstrophy-weighted correlation between axial stretching and projective noncommutation.

## 10. The phase-transition problem is now a four-way theorem

The correct M21-004 frontier is

\[
\boxed{
\text{compact corridor}
\Longrightarrow
T_{\rm phase}
\lor
P_{\rm transport}
\lor
P_{\rm pressure/diffusion}
\lor
P_{\rm segregation}.
}
\]

Here

\[
T_{\rm phase}:
\exists z_*\in[a,b]
\text{ with }
6\mathscr A(z_*)=\mathscr B(z_*).
\]

If no transition occurs, the remaining phase has a uniform gap and must generate one of the three quantitative compensators above.

## 11. Why this is a real reduction

Before M21-004, “the witnesses may remain segregated” was only a qualitative firewall.

Now persistent segregation has a quantitative cost.

Because no-crossing gives

\[
|\mathscr H|\ge\delta_H,
\]

the total weighted phase charge

\[
\int_a^b z^{7/2}|\mathscr H|\,dz
\]

has a fixed positive lower bound.

That charge must appear in one of three explicitly typed signed ledgers.

Thus the branch cannot evade analysis merely by avoiding the transition surface.

## 12. What is not yet known

M21-004 does not establish that any compensator is noncritical or nonrecyclable.

In particular:

- \(\Delta Y_M\) may be ordinary finite-depth transport;
- \(R_{PD}\) may return to critical pressure/raw-H2 derivative channels;
- \(R_{\Gamma K}\) may be recurrent phase segregation without finite ancestral cost.

Therefore no global contradiction follows yet.

## 13. Next target

The most economical next audit is the mixed-current transport term

\[
\Delta Y_M.
\]

M21-005 should determine whether \(\mathscr Y_M\) is merely a conservative/coboundary current whose corridor endpoint difference can recycle freely, or whether its endpoint values are controlled by the already forced witness functionals in a way that reduces this branch.

In parallel, the pressure/diffusion term should not be split into new independent payers until the transport-current audit is complete.

\[
\boxed{\text{M21-004 COMPLETE; A PHASE TRANSITION IS NOT AUTOMATIC, BUT ANY NO-CROSSING PHASE MUST PAY A FIXED SIGNED CHARGE THROUGH TRANSPORT, PRESSURE/DIFFUSION, OR LONGITUDINAL-TRANSVERSE SEGREGATION.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
