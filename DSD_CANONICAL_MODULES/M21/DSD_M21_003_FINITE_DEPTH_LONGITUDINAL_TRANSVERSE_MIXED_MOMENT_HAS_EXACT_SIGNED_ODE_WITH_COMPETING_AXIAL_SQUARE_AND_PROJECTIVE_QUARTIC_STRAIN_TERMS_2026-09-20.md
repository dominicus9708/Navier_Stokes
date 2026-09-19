# M21-003 — The finite-depth longitudinal-transverse mixed moment obeys an exact signed ODE with competing axial-square and projective-quartic strain terms

Date: 2026-09-20  
Canonical ID: **M21-003**  
Status: **MIXED-MOMENT EVOLUTION / THE ENSTROPHY-WEIGHTED MIXED MOMENT E Gamma K IS THE FINITE-DEPTH CONTINUATION OF THE M20 gamma-K SIGNED COUPLING / USING THE COMMON HOMOGENEITY GENERATOR, ITS MATERIAL EVOLUTION CONTAINS AN EXACT INTERNAL COMPETITION -3 Gamma^2 EK + (1/2) E K^2 BEFORE PRESSURE AND DIFFUSION REMAINDERS / q-AVERAGING PRODUCES A CLOSED FINITE-DEPTH TRANSPORT ODE WITH EXPLICIT NONNEGATIVE LONGITUDINAL-SQUARE AND TRANSVERSE-QUARTIC TERMS OF OPPOSITE SIGN / NO UNIVERSAL SIGN FOLLOWS, BUT THE PHASE-SEGREGATION PROBLEM IS NOW A TYPED PDE BALANCE / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Finite-depth variables

Use the M21 variables

\[
E:=|G|^2,
\]

\[
\Gamma:=\xi^T\Sigma_F\xi,
\]

\[
K:=\|[\Sigma_F,Q]\|_F^2
=
2|s_\perp|^2,
\]

and

\[
J:=EK.
\]

Define the mixed signed density

\[
\boxed{
M:=\Gamma J
=
E\Gamma K.
}
\]

This is the unnormalized finite-depth version of the M20-011 enstrophy-weighted \(\gamma K\) moment.

## 2. Homogeneities

The physical quantities scale as

\[
E_{\rm phys}=r^{-4}E,
\]

\[
\Gamma_{\rm phys}=r^{-2}\Gamma,
\]

and

\[
K_{\rm phys}=r^{-4}K.
\]

Therefore

\[
J_{\rm phys}=r^{-8}J,
\]

and

\[
\boxed{
M_{\rm phys}=r^{-10}M.
}
\]

Thus M is governed by the homogeneity-ten material generator

\[
\mathcal M_{10}.
\]

## 3. Joint-density material equation

M20-012 gives

\[
\boxed{
\mathcal M_8J
=
-2\Gamma J
+
\mathcal R_J,
}
\]

where

\[
\mathcal R_J
=
K\mathcal R_E
+
4E\mathcal R_K.
\]

This contains scalar diffusion, direction-gradient damping, transverse pressure-Hessian forcing, strain diffusion, and viscous projective coupling.

## 4. Axial stretching material equation

The physical directional stretching law from M20-005 is

\[
D_t\gamma_{\rm phys}
=
-\gamma_{\rm phys}^2
+
|s_{\perp,\rm phys}|^2
+
\text{pressure/diffusion remainder}.
\]

In finite-depth normalized variables this becomes

\[
\boxed{
\mathcal M_2\Gamma
=
-\Gamma^2
+
\frac12K
+
\mathcal R_\Gamma,
}
\]

where

\[
\boxed{
\mathcal R_\Gamma
:=
-
H_\parallel
+
\nu\,\xi^T(\mathcal L_S\Sigma_F)\xi
+
2v_\perp\cdot s_\perp,
}
\]

and

\[
H_\parallel
:=
\xi^TH\xi
\]

is the normalized longitudinal pressure-Hessian component.

## 5. Product rule for M=Gamma J

Because Gamma has homogeneity two and J has homogeneity eight,

\[
\boxed{
\mathcal M_{10}M
=
\Gamma\mathcal M_8J
+
J\mathcal M_2\Gamma.
}
\]

Insert Sections 3 and 4:

\[
\begin{aligned}
\mathcal M_{10}M
={}&
\Gamma(-2\Gamma J+\mathcal R_J)
\\
&+
J
\left(
-\Gamma^2+\frac12K+\mathcal R_\Gamma
\right).
\end{aligned}
\]

Therefore

\[
\boxed{
\mathcal M_{10}M
=
-3\Gamma^2J
+
\frac12JK
+
\Gamma\mathcal R_J
+
J\mathcal R_\Gamma.
}
\]

Since

\[
J=EK,
\]

the positive transverse term is

\[
\boxed{
\frac12JK
=
\frac12EK^2
\ge0.
}
\]

## 6. Internal strain competition

Ignoring the typed pressure/diffusion remainders for one moment, the mixed density has material source

\[
\boxed{
-3\Gamma^2EK
+
\frac12EK^2.
}
\]

Factor:

\[
\boxed{
E K
\left(
\frac12K-3\Gamma^2
\right).
}
\]

Thus the internal longitudinal/transverse strain geometry has a sharp algebraic threshold:

\[
\boxed{
K
\gtrless
6\Gamma^2.
}
\]

- if \(K>6\Gamma^2\), the transverse projective-quartic term dominates;
- if \(K<6\Gamma^2\), the longitudinal axial-square term dominates.

This is a local signed competition, not a global branch claim.

## 7. Eigenframe interpretation of the threshold

Recall

\[
K=2|s_\perp|^2.
\]

Therefore

\[
K>6\Gamma^2
\]

is equivalent to

\[
\boxed{
|s_\perp|^2>3\Gamma^2.
}
\]

In the strain eigenframe,

\[
|s_\perp|^2
=
\sum_{i<j}
a_i a_j(\lambda_i-\lambda_j)^2,
\]

while

\[
\Gamma
=
\sum_i a_i\lambda_i.
\]

Thus the threshold compares:

- strain-eigenvalue variance sampled by the vorticity direction;
- squared mean strain eigenvalue sampled by that direction.

It is a projective coefficient-of-variation criterion for the strain seen by vorticity.

## 8. Conservation-form finite-depth equation

The physical mixed density is

\[
r^{-10}M.
\]

Its advective flux is

\[
r^{-11}MF.
\]

A degree-eleven vector flux has divergence coefficient

\[
\mathfrak D-9.
\]

Therefore

\[
\boxed{
-\partial_zM
+
(\mathfrak D-9)(MF_r)
+
\operatorname{div}_S(MF_T)
=
\mathcal S_M,
}
\]

where

\[
\boxed{
\mathcal S_M
=
-3\Gamma^2J
+
\frac12EK^2
+
\Gamma\mathcal R_J
+
J\mathcal R_\Gamma.
}
\]

## 9. q-averaged mixed-moment ODE

Define

\[
\boxed{
\mathscr M(z)
:=
\left\langle
\int M\,d\omega
\right\rangle_q,
}
\]

and mixed radial flux

\[
\boxed{
\mathscr F_M(z)
:=
\left\langle
\int MF_r\,d\omega
\right\rangle_q.
}
\]

Also define the nonnegative moments

\[
\boxed{
\mathscr A(z)
:=
\left\langle
\int
\Gamma^2J\,d\omega
\right\rangle_q
\ge0,
}
\]

\[
\boxed{
\mathscr B(z)
:=
\left\langle
\int
EK^2\,d\omega
\right\rangle_q
\ge0.
}
\]

Finally define

\[
\boxed{
\mathscr C(z)
:=
\left\langle
\int
\Gamma\mathcal R_J\,d\omega
\right\rangle_q,
}
\]

and

\[
\boxed{
\mathscr D(z)
:=
\left\langle
\int
J\mathcal R_\Gamma\,d\omega
\right\rangle_q.
}
\]

Averaging Section 8 yields

\[
\boxed{
\mathscr M'
+
2z\mathscr F_M'
+
9\mathscr F_M
=
3\mathscr A
-
\frac12\mathscr B
-
\mathscr C
-
\mathscr D.
}
\]

This is the main M21-003 finite-depth signed mixed-moment equation.

## 10. Relation to longitudinal/transverse covariance

Normalize by

\[
W(z)=\langle E\rangle.
\]

Then

\[
\frac{\mathscr M}{W}
=
\mathbb E_{\pi_z}[\Gamma K].
\]

Since

\[
K=2|s_\perp|^2,
\]

we have

\[
\boxed{
\frac{\mathscr M}{2W}
=
\mathbb E_{\pi_z}
[
\Gamma|s_\perp|^2
].
}
\]

Therefore

\[
\boxed{
\frac{\mathscr M}{2W}
=
\bar\Gamma\,
\mathbb E_{\pi_z}|s_\perp|^2
+
C_{\Gamma T}(z).
}
\]

Thus M21-003 is exactly the evolution equation for the signed overlap variable proposed in M21-002.

## 11. Neutral mixed moment means phase segregation

If

\[
\mathscr M(z)\approx0
\]

while

\[
\bar\Gamma(z)>0
\]

and

\[
\mathbb E|s_\perp|^2>0,
\]

then necessarily

\[
\boxed{
C_{\Gamma T}(z)<0
}
\]

with matching magnitude.

That is, projective misalignment must preferentially occupy below-average stretching or compressive regions.

This is the finite-depth version of the M20-011 gamma--K phase-segregation condition.

## 12. Internal neutral threshold

Suppose the pressure/diffusion correlations are negligible at one depth and the transport derivative is also small.

Then the ODE requires approximately

\[
3\mathscr A
\approx
\frac12\mathscr B.
\]

Equivalently,

\[
\boxed{
\mathscr B
\approx
6\mathscr A.
}
\]

Thus neutral internal strain dynamics requires an exact balance between:

- longitudinal-square weighted projective activity;
- transverse-quartic weighted activity.

This is the averaged analogue of the pointwise threshold \(K=6\Gamma^2\).

## 13. No universal sign

Neither

\[
3\mathscr A-\frac12\mathscr B
\]

nor

\[
-\mathscr C-\mathscr D
\]

has a universal sign.

Therefore the mixed moment is not a Lyapunov function.

A recurrent hard solution may alternate between:

- longitudinal-dominated phases;
- transverse-dominated phases;
- pressure/diffusion compensation phases.

M21-003 types these phases but does not exclude them.

## 14. Criticality

All terms in the finite-depth normalized ODE are order one on the M21 compact corridor.

Returning to physical variables, the mixed density has degree ten.

Repeated normalized activity still carries scale-decaying ancestry weight.

Thus the new mixed ODE is a coupling/observability tool, not yet a noncritical accumulation theorem.

## 15. Next target

The M21 compact corridor makes all coefficients uniformly bounded.

M21-004 should use the two nonnegative moments

\[
\mathscr A
\]

and

\[
\mathscr B
\]

to define longitudinal-dominated and transverse-dominated depth sets:

\[
\mathcal L
=
\{6\mathscr A>\mathscr B\},
\]

\[
\mathcal T
=
\{6\mathscr A<\mathscr B\}.
\]

The question is whether the forced scalar enstrophy-production shell and the forced projective compensation shell must cross a transition depth where

\[
\boxed{
6\mathscr A=\mathscr B
}
\]

or whether pressure/diffusion correlations can keep the two witness structures permanently segregated.

This converts the vague overlap problem into a finite-depth phase-transition problem.

\[
\boxed{\text{M21-003 COMPLETE; THE LONGITUDINAL-TRANSVERSE MIXED MOMENT HAS AN EXACT SIGNED ODE WITH COMPETING AXIAL-SQUARE AND PROJECTIVE-QUARTIC TERMS.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
