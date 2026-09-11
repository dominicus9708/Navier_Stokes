# DSD M19-076 — Rotation quotient commutes with log-scattering translation but must retain a relative-periodic screw branch

**Date:** 2026-09-12  
**Status:** SYMMETRY-SAFE FACTOR REDUCTION WITH RELATIVE-PERIOD FIREWALL / ROTATIONAL ZERO MODES MAY BE QUOTIENTED, BUT TIME SHIFT COMPENSATED BY ROTATION MUST REMAIN AN EXPLICIT BRANCH / GLOBAL REGULARITY REMAINS UNPROVED

## 1. Purpose

M19-075 showed that a generic recurrent similarity trajectory carries rotation-generated zero modes in addition to the orbit tangent.

The next question is whether those neutral directions can be removed without erasing the log-radius translation factor whose rigidity is the active M19 target.

The answer is:

\[
\boxed{
SO(3)\text{ quotient is dynamically compatible with }q\text{-translation},
}
\]

but with one necessary firewall:

\[
\boxed{
\text{relative time-periodicity modulo rotation must remain separately visible.}
}
\]

## 2. Rotation action on the similarity solution

For \(R\in SO(3)\),

\[
(R\cdot U)(y,\theta)
:=R\,U(R^{-1}y,\theta).
\]

The same action on the scattering datum is

\[
\boxed{
(\mathcal R_R A)(q,\omega)
:=R\,A(q,R^{-1}\omega).
}
\]

This follows directly from

\[
U(y,\theta)
=\frac1rA\left(\log r-\frac\theta2,\omega\right)+O(r^{-3})
\]

because rotations preserve \(r=|y|\) and act only on \(\omega\).

Hence the scattering map is rotation-equivariant:

\[
\boxed{
\mathscr S(R\cdot Y)
=\mathcal R_R\mathscr S(Y).
}
\]

## 3. Rotation and q-translation commute exactly

Let

\[
(T_sA)(q,\omega):=A(q-s,\omega).
\]

Then

\[
\begin{aligned}
T_s(\mathcal R_RA)(q,\omega)
&=R A(q-s,R^{-1}\omega),\\
\mathcal R_R(T_sA)(q,\omega)
&=R A(q-s,R^{-1}\omega).
\end{aligned}
\]

Therefore

\[
\boxed{
T_s\mathcal R_R
=\mathcal R_RT_s.
}
\]

This is the central compatibility missing from a time-orbit quotient.

Time quotienting identifies the very q-translations to be studied. Rotation quotienting does not generically do so because it changes only angular orientation.

## 4. Induced translation dynamics on the rotation quotient

Let

\[
[A]_{rot}:=\{\mathcal R_RA:R\in SO(3)\}.
\]

Because the two actions commute,

\[
\boxed{
\widetilde T_s[A]_{rot}
:=[T_sA]_{rot}
}
\]

is well defined.

Similarly, the recurrent hull quotient

\[
\widetilde{\mathcal H}:=\mathcal H/SO(3)
\]

inherits the similarity flow.

The scattering factor descends to

\[
\boxed{
\widetilde{\mathscr S}:
\widetilde{\mathcal H}
\to
\mathcal A/SO(3)
}
\]

with covariance

\[
\boxed{
\widetilde{\mathscr S}(\widetilde\sigma_t[Y])
=
\widetilde T_{t/2}\widetilde{\mathscr S}([Y])
}
\]

up to the sign convention already fixed by

\[
A_{\sigma_tY}(q)=A_Y(q-t/2).
\]

Thus rotation-generated center directions can be removed without destroying the existence of an induced q-translation factor.

## 5. The relative-period firewall

Suppose the full similarity trajectory is not exactly periodic but satisfies

\[
\boxed{
\sigma_TY=R\cdot Y
}
\]

for some \(T>0\) and \(R\in SO(3)\).

Then in the quotient

\[
\widetilde\sigma_T[Y]=[Y],
\]

so the quotient trajectory is periodic.

The scattering covariance gives

\[
\boxed{
T_{T/2}A
=\mathcal R_{R^{-1}}A
}
\]

with the precise sign determined by the chosen \(T_sA(q)=A(q-s)\) convention.

Equivalently, in direct variables,

\[
\boxed{
A(q-T/2,\omega)
=R\,A(q,R^{-1}\omega).
}
\]

This is a **relative-periodic screw relation** between log-radius translation and angular rotation.

Therefore

\[
\boxed{
[A]\text{ periodic in }\mathcal A/SO(3)
\not\Rightarrow
A\text{ periodic in q without qualification.}
}
\]

## 6. Fourier-spherical harmonic representation of a relative period

Choose the rotation axis of \(R\) as the polar axis and let its rotation angle be \(\alpha\).

For an angular Fourier/spherical-harmonic mode with azimuthal number \(m\), rotation contributes phase

\[
e^{im\alpha}.
\]

A q-Fourier factor

\[
e^{ikq}
\]

under \(q\mapsto q-T/2\) contributes

\[
e^{-ikT/2}.
\]

The relative-period condition allows the resonance

\[
\boxed{
e^{-ikT/2}=e^{im\alpha}.}
\]

Hence

\[
\boxed{
k
= -\frac{2m\alpha}{T}
+\frac{4\pi n}{T},
\qquad n\in\mathbb Z.
}
\]

Different \((m,n)\) pairs can generate several q-frequencies. If \(\alpha/\pi\) is irrational, their ratios need not be rational.

Thus a full datum can have nontrivial or even quasiperiodic q-behavior while being periodic after quotienting by rotations.

This is why the relative-period branch cannot be discarded as gauge.

## 7. Continuous relative equilibrium is more rigid

A stronger condition is

\[
\boxed{
\sigma_tY=R_t\cdot Y
\qquad\forall t,
}
\]

with a continuous one-parameter rotation subgroup

\[
R_t=e^{tK},
\qquad K\in\mathfrak{so}(3).
\]

Then

\[
A(q-t/2,\omega)
=R_tA(q,R_t^{-1}\omega).
\]

Differentiating at \(t=0\),

\[
\boxed{
-\frac12\partial_qA
=K A-(K\omega)\cdot\nabla_{S^2}A.
}
\]

Define the angular rotation generator

\[
\mathfrak R_KA
:=K A-(K\omega)\cdot\nabla_{S^2}A.
\]

Then

\[
\boxed{
\partial_qA+2\mathfrak R_KA=0.
}
\]

Since every one-parameter subgroup of \(SO(3)\) is periodic in its rotation angle, a pure continuous rotating-wave q-dependence is periodic unless the generator vanishes on the datum.

This continuous relative-equilibrium class is therefore substantially more rigid than a merely discrete relative period.

## 8. Correct quotient branch tree

After removing rotation-generated zero modes, the scattering problem becomes

\[
\boxed{
\mathcal R_{critical}^{weak\text{-}scatt}
\Longrightarrow
\begin{cases}
\text{quotient-aperiodic translation factor},\\
\text{relative-periodic screw factor},\\
\text{quotient-stationary/continuous rotating factor},\\
\text{typed decompactification/export}.
\end{cases}
}
\]

The second and third branches are not generic gauge artifacts. They are dynamically structured realization classes requiring their own PDE audit.

## 9. Consequence for center dimension

The symmetry-correct target is not

\[
\dim E^c=1.
\]

It is

\[
\boxed{
E^c/E^c_{rot}
\text{ contains only the orbit tangent, unless a relative-rotation branch is realized.}
}
\]

Equivalently, after rotational modulation one seeks transverse contraction while retaining an explicit relative-period parameter whenever time evolution and rotation lock together.

## 10. What is certified

M19-076 certifies:

1. rotation equivariance of the scattering datum;
2. exact commutation of rotations with q-translations;
3. well-defined scattering dynamics on the rotation quotient;
4. the exact relative-period screw identity;
5. the spherical/Fourier resonance relation
   \[
   e^{-ikT/2}=e^{im\alpha};
   \]
6. the need to retain relative-periodic solutions as an explicit branch rather than quotient them away silently.

## 11. What remains open

M19-076 does not prove:

1. that relative-periodic rotating similarity solutions exist;
2. that they do not exist;
3. that the quotient center is one-dimensional;
4. transverse contraction;
5. global regularity.

## 12. Next target

Two possible shortcuts now need audit.

First, one may hope that positive-time parabolic smoothing makes the quotient linearized cocycle compact and hence forces a finite-dimensional center.

Second, one may hope to use a stronger Gaussian space after moving to vorticity and thereby remove the pressure obstruction.

Both claims must be tested against remote translated packets and nonlocal Biot--Savart recovery before being used.

---

\[
\boxed{\text{M19-076 COMPLETE.}}
\]
