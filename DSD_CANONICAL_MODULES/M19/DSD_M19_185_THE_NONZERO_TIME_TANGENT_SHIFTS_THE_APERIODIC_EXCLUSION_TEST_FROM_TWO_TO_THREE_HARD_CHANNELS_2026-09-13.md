# M19-185 — The nonzero time tangent shifts the aperiodic exclusion test from two to three hard channels

**Date:** 2026-09-13  
**Status:** ACTIVE CALCULATION / STRICT IMPROVEMENT OF DIMENSION-ONE THRESHOLD

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Quotient dimension versus actual hard-family dimension

M19-173 uses

\[
N:=\dim E_q^{hard}
\]

after quotienting the exact time/rotation symmetries.

A genuinely aperiodic quotient recurrent component requires

\[
N\ge2.
\]

However the collective vorticity trace estimate need not discard symmetry modes. Every nonzero complete neutral hard mode consumes damping compensation.

## 2. The time tangent is an exact nonzero hard mode

Because the similarity Navier--Stokes equation is autonomous,

\[
W_t:=\partial_sU
\]

solves the exact linearized equation.

Inside the certified singular hard corridor, M19-146 gives the one-slice/scattering speed floor

\[
\boxed{
\|\partial_sU\|_{hard}\ge c_t>0.
}
\]

Equivalently,

\[
D\mathscr S_U(\partial_sU)
=-\frac12\partial_qA
\]

is nonzero.

Thus the time tangent contributes one genuine hard channel before quotienting.

## 3. Aperiodicity requires at least three observable hard channels

If the quotient hard dimension satisfies `N>=2`, then the unquotiented observable hard family has dimension at least

\[
\boxed{
M\ge N+1\ge3.
}
\]

The M19-180--182 collective trace estimate applies to an orthonormal frame of this full observable hard family.

## 4. Three-channel criterion

For a total hard-family dimension `M`, the normalized mean-activity inequality is

\[
\frac14+\nu x
\le
\mathfrak A M^{-2/5}x^{3/5}
+
\mathfrak B_a M^{d(a)-1}x^{q(a)}.
\]

Both powers of `M` on the right are negative.

Therefore to exclude quotient `N>=2`, it is enough to exclude the smallest possible total dimension `M=3`.

The sharpened sufficient condition is

\[
\boxed{
\sup_{x\ge0}
\left[
\mathfrak A3^{-2/5}x^{3/5}
+
\mathfrak B_a3^{d(a)-1}x^{q(a)}
-\nu x
\right]
<\frac14.
}
\]

If this holds for one `a in (3/2,3)`, then

\[
\boxed{N\le1.}
\]

## 5. Clean a=2 specialization

For `a=2`,

\[
q=\frac14,
\qquad
d-1=-\frac16.
\]

Set

\[
A_3:=3^{-2/5}\mathfrak A,
\qquad
B_3:=3^{-1/6}\mathfrak B_2.
\]

Then

\[
\Psi_3(x)=A_3x^{3/5}+B_3x^{1/4}-\nu x.
\]

If `y=x_*^{1/20}`, the unique maximizer satisfies

\[
\boxed{
\nu y^{15}
-\frac35A_3y^7
-\frac14B_3=0,
}
\]

and

\[
\boxed{
\Psi_3^{max}
=\frac25A_3y^{12}
+\frac34B_3y^5.
}
\]

Thus

\[
\boxed{
\Psi_3^{max}<\frac14
\Longrightarrow
N\le1.
}
\]

## 6. Comparison with M19-183

Because

\[
3^{-2/5}<2^{-2/5},
\qquad
3^{-1/6}<2^{-1/6},
\]

the admissible mean-activity region is strictly larger than the provisional two-mode region.

Hence M19-183 remains correct as a sufficient test, but M19-185 is the stronger universal aperiodic-exclusion test once the certified nonzero time tangent is counted.

## 7. Rotation-symmetry bonus

If the background has additional nonzero rotation-orbit tangents, those exact neutral modes can also be included in the collective trace family. On a stratum with rotation-orbit dimension `r_rot`, quotient `N>=2` implies

\[
M\ge3+r_{rot}.
\]

This gives still stronger stratum-specific thresholds. The universal statement uses only the always-available nonzero time tangent.

## 8. Firewall

\[
\boxed{
\text{quotient dimension}
\neq
\text{number of channels paying the collective damping budget}.
}
\]

Exact symmetry modes are removed for dynamical classification but remain legitimate compensation-consuming channels in the trace estimate.

---

\[
\boxed{\text{M19-185: APERIODICITY MUST PAY AT LEAST THREE HARD COMPENSATION CHANNELS.}}
\]
