# M19-207 — Any moderate RSS/RDSS nonsymmetry unit kernel must saturate the pressure-compatible weighted linear gap by order-one nonlinear compensation

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / NECESSARY KERNEL CONDITION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Weighted linear gap

For the radial A2 weight family of M19-063--064, the linearized velocity difference obeys an estimate of the form

\[
\frac12E_w'
+\frac\nu2G_w
+\bigl(c_{gap}-\Lambda_{NL}(s)\bigr)E_w
\le0,
\]

where

\[
E_w=\|W\|_{L^2(w)}^2,
\qquad
G_w=\|\nabla W\|_{L^2(w)}^2,
\]

and one may take

\[
\Lambda_{NL}
\le
\left(\frac12+2C_{CZ}\right)L_w M_U
+C_1\nu^{-1}M_S^2
+C_2L_wM_S.
\]

Here \(M_U\) and \(M_S\) denote the relevant instantaneous background velocity and strain sizes on the retained corridor.

## 2. Unit-return mode cannot lie below the gap

Let \(W\) be a nonsymmetry hard mode with unit Floquet return over period \(S\). The twisted rotation/phase return preserves the radial weighted norm, so

\[
E_w(S)=E_w(0).
\]

Integrating one period gives

\[
\frac\nu2\int_0^S G_w\,ds
+c_{gap}\int_0^S E_w\,ds
\le
\int_0^S\Lambda_{NL}(s)E_w(s)\,ds.
\]

Therefore every nonzero unit mode satisfies the exact necessary inequality

\[
\boxed{
\frac{\int_0^S\Lambda_{NL}(s)E_w(s)\,ds}
{\int_0^S E_w(s)\,ds}
\ge
c_{gap}
+\frac\nu2
\frac{\int_0^S G_w\,ds}
{\int_0^S E_w\,ds}
>
c_{gap}.
}
\]

Thus a unit kernel/elliptic mode requires order-one nonlinear compensation of the pressure-compatible linear gap.

## 3. RSS specialization

For an RSS state in the co-rotating frame, radial weighted norms are stationary because the rotation generator is skew-adjoint for radial weights. Hence the background sizes entering the estimate are time-independent in that frame.

A nonsymmetry stationary/co-rotating kernel therefore requires

\[
\boxed{
\left(\frac12+2C_{CZ}\right)L_w M_U
+C_1\nu^{-1}M_S^2
+C_2L_wM_S
\ge
c_{gap}+\frac\nu2\frac{G_w}{E_w}.
}
\]

In particular the weaker necessary condition

\[
\boxed{
\left(\frac12+2C_{CZ}\right)L_w M_U
+C_1\nu^{-1}M_S^2
+C_2L_wM_S
\ge c_{gap}
}
\]

must hold.

## 4. RDSS specialization

For a bounded-period RDSS state the same statement holds with the E-weighted period average of \(\Lambda_{NL}\). Compact hard-bundle norm equivalence converts this, at the cost of a finite condition number, to an ordinary period-mean nonlinear-activity floor.

## 5. Relation to the optimal A2 gap

M19-066 gives

\[
\sup c_{gap}=\frac15
\]

within the pressure-compatible radial A2 family (approached as \(a\to3^-\) with the corresponding optimal \(\beta\)). Therefore a kernel mode cannot survive in a corridor where the optimized nonlinear compensation remains uniformly below this order-one scale.

## 6. Verdict

The moderate RSS/RDSS kernel problem is now quantitatively localized:

\[
\boxed{
\text{nonsymmetry unit kernel}
\Longrightarrow
\text{order-one weighted velocity/strain compensation of the A2 gap}.
}
\]

This is a necessary activity floor, not yet a contradiction. The next question is whether the retained Type-I/scattering/torque constraints impose an upper bound below this floor on the moderate compact hard set.