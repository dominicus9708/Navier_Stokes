# M19-242 — The full Gaussian-weighted linearized energy identifies critical radial transport and pressure as the bare-gap defects

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / FULL WEIGHTED-ENERGY AUDIT + GAP-DEFECT IDENTIFICATION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-241 proves an exact R-independent negative spectral gap for the bare toroidal similarity-Stokes cavity. The actual cavity mode, however, is linearized around a nonzero critical background U and carries a pressure.

This module derives the exact Gaussian-weighted L2 identity for the full linearized equation. The calculation shows precisely why the bare gap does not automatically extend: the defect is not mainly the small remote strain. It is the critical radial transport term U·y together with the loss of pressure orthogonality in the Gaussian metric.

## 2. Full primal linearized equation

On B_R with no-slip boundary condition,

\[
\boxed{
\partial_sw
=\nu\Delta w
-\left(\frac y2+U\right)\cdot\nabla w
-\frac12w
-(w\cdot\nabla)U
-\nabla\pi,
}
\]

\[
\nabla\cdot w=0,
\qquad
w|_{S_R}=0.
\]

Use the Gaussian weight naturally associated with the M19-241 conjugation:

\[
\boxed{
\rho(y):=e^{-|y|^2/(4\nu)}.
}
\]

Then

\[
\nabla\rho=-\frac y{2\nu}\rho,
\]

\[
\Delta\rho
=\left(-\frac3{2\nu}+\frac{|y|^2}{4\nu^2}\right)\rho.
\]

Define

\[
E_\rho(s):=\int_{B_R}\rho|w|^2dy.
\]

## 3. Bare diffusion and similarity drift cancel exactly to the gap form

The viscous term gives

\[
\begin{aligned}
\nu\int\rho w\cdot\Delta w
&=-\nu\int\rho|\nabla w|^2
-\nu\int (\nabla\rho\cdot\nabla w)\cdot w\\
&=-\nu\int\rho|\nabla w|^2
+\frac\nu2\int(\Delta\rho)|w|^2.
\end{aligned}
\]

Hence

\[
\nu\int\rho w\cdot\Delta w
=-\nu\int\rho|\nabla w|^2
-\frac34E_\rho
+\int\frac{|y|^2}{8\nu}\rho|w|^2.
\]

The similarity drift gives

\[
\begin{aligned}
-\int\rho w\cdot\frac y2\cdot\nabla w
&=-\frac14\int\rho y\cdot\nabla|w|^2\\
&=\frac14\int\operatorname{div}(\rho y)|w|^2\\
&=\frac34E_\rho
-\int\frac{|y|^2}{8\nu}\rho|w|^2.
\end{aligned}
\]

Thus the potential terms cancel exactly. Including the explicit amplitude term -w/2 gives

\[
\boxed{
\text{bare contribution}
=-\nu\int\rho|\nabla w|^2
-\frac12E_\rho.
}
\]

This is the weighted-energy form of the M19-241 Gaussian-conjugated spectral gap.

## 4. Background transport defect

The incompressible background transport gives

\[
\begin{aligned}
-\int\rho w\cdot(U\cdot\nabla)w
&=-\frac12\int\rho U\cdot\nabla|w|^2\\
&=\frac12\int\operatorname{div}(\rho U)|w|^2.
\end{aligned}
\]

Since div U=0,

\[
\boxed{
-\int\rho w\cdot(U\cdot\nabla)w
=-\frac1{4\nu}\int\rho(U\cdot y)|w|^2.
}
\]

This is the first critical defect.

Remote critical scaling gives

\[
U=O(r^{-1}),
\]

but therefore only

\[
\boxed{U\cdot y=O(1),}
\]

not o(1). The radial critical scattering channel survives at order one in the Gaussian energy.

Hence remote coefficient smallness in the ordinary pointwise norm does not make this defect small relative to E_rho.

## 5. Background strain defect

The linearized stretching term is

\[
-\int\rho w^T(\nabla U)w.
\]

The antisymmetric part drops from the quadratic form, leaving

\[
\boxed{
-\int\rho w^TS_Uw.
}
\]

Unlike U·y, the remote critical estimate

\[
S_U=O(r^{-2})
\]

makes this term genuinely small on a remote shell.

Thus strain is not the leading obstruction to transferring the M19-241 bare gap.

## 6. Pressure is no longer orthogonal in the Gaussian metric

In ordinary unweighted L2, pressure is orthogonal to divergence-free no-slip fields. In the weighted metric,

\[
-\int\rho w\cdot\nabla\pi
=
\int\pi\nabla\cdot(\rho w).
\]

Since div w=0,

\[
\nabla\cdot(\rho w)=\nabla\rho\cdot w
=-\frac1{2\nu}\rho y\cdot w.
\]

Therefore

\[
\boxed{
-\int\rho w\cdot\nabla\pi
=-\frac1{2\nu}\int\rho\pi(y\cdot w).
}
\]

This is the second leading structural defect.

It vanishes for a purely tangential/toroidal field with y·w=0, but the actual background can couple toroidal and poloidal/radial components. Thus the pressure defect is exactly one way in which the full system escapes the bare toroidal gap.

## 7. Exact full Gaussian energy identity

Combining the previous terms gives

\[
\boxed{
\begin{aligned}
\frac12\frac d{ds}E_\rho
+\nu\int\rho|\nabla w|^2
+\frac12E_\rho
={}&-\frac1{4\nu}\int\rho(U\cdot y)|w|^2\\
&-\int\rho w^TS_Uw\\
&-\frac1{2\nu}\int\rho\pi(y\cdot w).
\end{aligned}}
\]

For a relative-periodic mode, the radial weight is rotation invariant, so E_rho has identical endpoint values over one period. Therefore

\[
\boxed{
\begin{aligned}
\nu\int_0^S\int\rho|\nabla w|^2
+\frac12\int_0^S E_\rho\,ds
={}&-\frac1{4\nu}\int_0^S\int\rho(U\cdot y)|w|^2\\
&-\int_0^S\int\rho w^TS_Uw\\
&-\frac1{2\nu}\int_0^S\int\rho\pi(y\cdot w).
\end{aligned}}
\]

Thus every full cavity unit mode must pay the entire bare Gaussian coercivity through these three defects.

## 8. The radial critical channel is the leading coefficient defect

Write the remote critical background schematically as

\[
U(r\omega,s)
=r^{-1}A(q,\omega)+O(r^{-3}).
\]

Then

\[
\boxed{
U\cdot y=A_r(q,\omega)+O(r^{-2}).
}
\]

Hence the Gaussian transport defect has leading form

\[
-\frac1{4\nu}\int\rho A_r|w|^2.
\]

The toroidal part of the background does not enter U·y directly. Therefore the full-gap instability is naturally separated into

1. a critical radial-background scalar A_r;
2. pressure/poloidal coupling through y·w;
3. lower-order strain.

This is a sharper decomposition than generic nonnormality language.

## 9. Why the Gaussian identity is blind to the unweighted escape shell

M19-234--240 place the escaping unweighted mode near r≈R with a velocity-carrying shell and an inner nu/R no-slip sublayer.

But

\[
\rho(R)=e^{-R^2/(4\nu)}.
\]

Therefore an unweighted O(1)-mass boundary shell may have exponentially tiny E_rho.

Consequently even a strong weighted coercive estimate does not by itself control the unweighted cavity normalization.

Permanent firewall:

\[
\boxed{
\text{Gaussian weighted spectral gap}
\neq
\text{unweighted boundary-shell exclusion}.
}
\]

This is independent of the pressure/coupling defects.

## 10. Conditional toroidal extension

If a cavity mode stays exactly toroidal and the background has no radial/poloidal coupling into that sector, then

\[
y\cdot w=0
\]

and the pressure defect vanishes. If additionally A_r=0 in the support relevant to the weighted mode, then the radial transport defect vanishes as well, while the remote strain is small.

In that restricted invariant situation, the M19-241 gap is stable and a unit multiplier is excluded for sufficiently remote support.

The actual hard corridor does not currently certify these decoupling hypotheses, so this remains a conditional subclosure only.

## 11. Updated shell-return target

A surviving boundary-shell unit mode must exploit at least one of the following:

\[
\boxed{
\begin{array}{l}
\text{critical radial transport }U\cdot y\sim A_r,\\
\text{pressure/radial-poloidal coupling }\pi\,y\cdot w,\\
\text{Gaussian-weight degeneracy on the unweighted boundary shell},\\
\text{or scaled-derivative/nonnormal concentration.}
\end{array}}
\]

Thus the next useful calculation is not another generic spectral gap. It is to determine whether the radial transport and pressure defects have an exact cancellation/current structure in the remote critical variables, or whether their required magnitude forces an already typed radial/poloidal hard channel.

---

\[
\boxed{\text{M19-242 COMPLETE: THE FULL GAUSSIAN ENERGY LOCATES THE BARE-GAP FAILURE IN CRITICAL RADIAL TRANSPORT, PRESSURE/POLoidal COUPLING, AND WEIGHT DEGENERACY.}}
\]
