# M19-013 — Critical 1/R velocity tail is exactly nonvanishing physical kinetic Morrey density under blowup rescaling

**Date:** 2026-09-11  
**Status:** CALCULATION / R-CRITICAL ENTRY / EXACT MORREY RESCALING IDENTITY / CRITICAL-TAIL NORMAL FORM

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-005--012 exposes the present R-AC frontier and identifies the genuinely new theorem required there. The active calculation now moves to

\[
\boxed{\mathcal R_{critical}}.
\]

M18 identifies the main critical endpoint as a bounded weak-\(L^3\)-compatible velocity tail of order

\[
U(y)\sim |y|^{-1},
\qquad
\Omega(y)\sim |y|^{-2},
\]

together with low-frequency \(\dot H^{-1}\) and terminal/global-realization issues.

The first task is to express this tail in the original physical parent without representation ambiguity.

The result is exact: the normalized critical tail is equivalent to nonvanishing scale-invariant local kinetic Morrey density

\[
\boxed{
\mathcal M_u(x,r,t)
:=
\frac1r\int_{B_r(x)}|u(z,t)|^2dz.
}
\]

## 2. Blowup rescaling

Let \(r_j\downarrow0\) and centers \((x_j,t_j)\) define the standard parabolic rescaling

\[
\boxed{
U_j(y,s)
:=
r_j u(x_j+r_jy,t_j+r_j^2s).
}
\]

Then

\[
\Omega_j(y,s)
=
 r_j^2\omega(x_j+r_jy,t_j+r_j^2s).
\]

Fix one rescaled time \(s\), and let

\[
t=t_j+r_j^2s.
\]

## 3. Exact local kinetic-energy scaling

For every \(R>0\),

\[
\begin{aligned}
\int_{B_R}|U_j(y,s)|^2dy
&=
\int_{B_R}
 r_j^2
 |u(x_j+r_jy,t)|^2dy\\
&=
 r_j^{-1}
 \int_{B_{r_jR}(x_j)}|u(x,t)|^2dx.
\end{aligned}
\]

Divide by \(R\):

\[
\boxed{
\frac1R
\int_{B_R}|U_j|^2dy
=
\frac1{r_jR}
\int_{B_{r_jR}(x_j)}|u|^2dx.
}
\]

Set

\[
\ell:=r_jR.
\]

Then

\[
\boxed{
\mathcal M_{U_j}(0,R,s)
=
\mathcal M_u(x_j,\ell,t).
}
\]

Thus the kinetic Morrey density is exactly invariant under the blowup change of representation.

## 4. Critical 1/R tail gives nonzero Morrey density

Suppose a limiting or approximate normalized profile has

\[
|U(y)|\sim\frac{|A(\widehat y)|}{|y|}
\]

on large radii, with nontrivial angular amplitude \(A\).

Then

\[
\int_{1<|y|<R}|U(y)|^2dy
\sim
\left(
\int_{S^2}|A(\omega)|^2d\omega
\right)R
\]

up to lower-order terms.

Therefore

\[
\boxed{
\liminf_{R\to\infty}
\frac1R\int_{B_R}|U|^2dy
>0
}
\]

for a genuinely nontrivial \(1/R\) tail.

By Section 3 this is equivalent, along the corresponding physical scales, to

\[
\boxed{
\liminf
\frac1\ell
\int_{B_\ell(x_j)}|u(x,t)|^2dx
>0.
}
\]

This is the parent form of the critical tail.

## 5. Weak-L3 gives the natural upper bound

On a finite ball, the Lorentz embedding gives

\[
\|f\|_{L^2(B_R)}
\le
C|B_R|^{1/6}
\|f\|_{L^{3,\infty}}
\sim
CR^{1/2}\|f\|_{L^{3,\infty}}.
\]

Hence

\[
\boxed{
\frac1R\int_{B_R}|f|^2
\le
C\|f\|_{L^{3,\infty}}^2.
}
\]

Thus the W1 weak-\(L^3\) bound is exactly consistent with a bounded kinetic Morrey density.

Conversely, if

\[
\frac1R\int_{B_R}|f|^2\ge m_*>0,
\]

then the same inequality implies

\[
\boxed{
\|f\|_{L^{3,\infty}}
\ge c m_*^{1/2}.
}
\]

So a nonvanishing critical Morrey tail carries a nonzero weak-\(L^3\) amplitude, but bounded weak-\(L^3\) does not force the Morrey density to vanish.

## 6. Finite physical kinetic energy does not force Morrey vanishing

Finite energy gives

\[
\int_{\mathbb R^3}|u|^2dx<\infty.
\]

Therefore

\[
\int_{B_\ell(x)}|u|^2dx\to0
\qquad(\ell\downarrow0)
\]

for every fixed time and center by absolute continuity of the integral.

But this does **not** imply

\[
\frac1\ell\int_{B_\ell(x)}|u|^2dx\to0.
\]

The model scaling

\[
|u(x)|\sim\frac1{|x|}
\]

has

\[
\int_{B_\ell}|u|^2dx
\sim C\ell,
\]

so the energy tends to zero while the Morrey density stays order one.

Thus

\[
\boxed{
L^2\text{ absolute continuity}
\not\Rightarrow
\mathcal M_u(r)\to0.
}
\]

This is the exact criticality of the \(1/R\) tail.

## 7. Annular version

Define the dyadic annular Morrey charge

\[
\boxed{
\mathcal A_u(x,r,t)
:=
\frac1r
\int_{r<|z-x|<2r}|u(z,t)|^2dz.
}
\]

Under the same blowup scaling,

\[
\boxed{
\mathcal A_{U_j}(0,R,s)
=
\mathcal A_u(x_j,r_jR,t).
}
\]

A persistent normalized \(1/R\) tail is therefore equivalently a sequence of physical dyadic annuli carrying order-one \(\mathcal A_u\).

This is often more useful than ball Morrey density because annuli separate scales and avoid repeated counting of the inner core.

## 8. R-critical normal form

The escaping critical-tail subroot can now be represented by the exact parent statement

\[
\boxed{
G_{critical\ tail}
:
\exists\,(x_j,t_j,\ell_j),\ \ell_j\downarrow0,
\quad
\mathcal A_u(x_j,\ell_j,t_j)\ge a_*>0,
}
\]

or the corresponding nonvanishing ball-Morrey form, together with the existing weak-\(L^3\)/compactness conditions.

This is a representation-safe target.

## 9. What this gains

The phrase `1/R tail` can refer to pointwise, averaged, angular, or subsequential behavior.

The Morrey formulation removes that ambiguity.

It also puts the critical root directly in the original finite-energy solution rather than only in a normalized ancient limit.

Any future contradiction or rigidity theorem may now target

\[
\mathcal A_u(x,r,t)
\]

without first reconstructing a pointwise asymptotic tail.

## 10. What is not proved

This module does not prove that \(\mathcal A_u\to0\).

Finite energy alone is insufficient.

It also does not identify the angular profile of the tail, control low-frequency \(\dot H^{-1}\) tightness, or close the terminal realization problem.

## 11. Next calculation

M19-014 should calculate the exact energy economics of a persistent dyadic critical tail.

If

\[
\mathcal A_u(x,r_n,t_n)\ge a_*
\]

across geometrically nested scales, determine whether the corresponding physical energy costs are additive or geometrically summable.

This will show whether standard finite energy can exclude repeated critical Morrey shells or whether a different rigidity mechanism is required.

---

\[
\boxed{\text{M19-013 COMPLETE; R-CRITICAL IS NOW EXPRESSED AS A PHYSICAL MORREY-ENERGY ROOT.}}
\]
