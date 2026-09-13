# M19-233 — Localized vorticity identity excludes intermediate-radius escape and forces escaping cavity vorticity to the cavity scale

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / ESCAPE-BRANCH RADIAL LOCALIZATION RIGIDITY

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-232 proves that every normalized cavity unit mode in the M19-231 escape branch carries the asymptotically exact one-period vorticity currency

\[
\boxed{
\int_0^{S_j}\|\eta_j\|_2^2\,ds
\to\frac1{4\nu},
\qquad
\eta_j:=\nabla\times w_j.
}
\]

The velocity energy cannot exclude escape because the bare similarity velocity balance contains a positive \(+\frac14\|w\|_2^2\) production.

The vorticity balance has the opposite similarity sign. This module uses that sign with a slowly varying logarithmic radial cutoff and proves that the fixed vorticity currency cannot remain at radii

\[
1\ll r\ll R_j.
\]

Hence any escaping cavity obstruction must move all the way to the cavity scale \(r\asymp R_j\).

## 2. Linearized vorticity equation

Let

\[
\Omega_j:=\nabla\times U_j.
\]

Curling the primal linearized similarity equation gives

\[
\boxed{
\begin{aligned}
\partial_s\eta_j
={}&\nu\Delta\eta_j
-\eta_j
-\frac12(y\cdot\nabla)\eta_j
-(U_j\cdot\nabla)\eta_j
-(w_j\cdot\nabla)\Omega_j\\
&+(\eta_j\cdot\nabla)U_j
+(\Omega_j\cdot\nabla)w_j.
\end{aligned}}
\]

There is no pressure term.

On the retained remote corridor,

\[
|U_j|=O(r^{-1}),
\qquad
|\nabla U_j|+|\Omega_j|=O(r^{-2}),
\qquad
|\nabla\Omega_j|=O(r^{-3})
\]

uniformly in the retained background family.

## 3. Exact weighted vorticity identity

Let \(a(y)\) be a smooth radial weight compactly supported away from the cavity boundary. Multiply the vorticity equation by \(a\eta_j\) and integrate over \(B_{R_j}\).

The diffusion term gives

\[
-\nu\int a|\nabla\eta_j|^2
+\frac\nu2\int(\Delta a)|\eta_j|^2.
\]

The amplitude and similarity drift combine as

\[
-\int a|\eta_j|^2
-\frac12\int a\eta_j\cdot(y\cdot\nabla)\eta_j
=
-\frac14\int a|\eta_j|^2
+\frac14\int(y\cdot\nabla a)|\eta_j|^2.
\]

The background transport gives

\[
\frac12\int(U_j\cdot\nabla a)|\eta_j|^2.
\]

The stretching term reduces to the symmetric strain:

\[
\int a\eta_j^TS_{U_j}\eta_j.
\]

Thus

\[
\boxed{
\begin{aligned}
\frac12\frac d{ds}\int a|\eta_j|^2
={}&-\nu\int a|\nabla\eta_j|^2
-\frac14\int a|\eta_j|^2\\
&+\frac\nu2\int(\Delta a)|\eta_j|^2
+\frac14\int(y\cdot\nabla a)|\eta_j|^2\\
&+\frac12\int(U_j\cdot\nabla a)|\eta_j|^2
+\int a\eta_j^TS_{U_j}\eta_j\\
&-\int a\eta_j\cdot((w_j\cdot\nabla)\Omega_j)
+\int a\eta_j\cdot((\Omega_j\cdot\nabla)w_j).
\end{aligned}}
\]

This is the pressure-free localized identity needed for the escape branch.

## 4. Slowly varying logarithmic cutoff

Take sequences

\[
a_j\to\infty,
\qquad
b_j\le \frac{R_j}{4},
\qquad
\frac{b_j}{R_j}\to0,
\]

with \(a_j\le b_j\).

Fix a large radius \(r_0\) independent of \(j\). Construct a radial cutoff \(\chi_j(r)\) such that

\[
0\le\chi_j\le1,
\]

\[
\chi_j=0\quad(r\le r_0),
\]

\[
\chi_j=1\quad(a_j\le r\le b_j),
\]

and \(\chi_j=0\) before \(r=R_j/2\).

Choose both transitions affine after smoothing in the logarithmic variable \(\log r\). Then

\[
L_j^{in}:=\log(a_j/r_0)\to\infty,
\]

and

\[
L_j^{out}:=\log\!\left(\frac{R_j}{2b_j}\right)\to\infty.
\]

Consequently

\[
\boxed{
\|y\cdot\nabla\chi_j\|_\infty
\lesssim
\frac1{L_j^{in}}+\frac1{L_j^{out}}
\to0.
}
\]

Also, because the inner transition starts at fixed \(r_0>0\) and the outer transition moves to infinity,

\[
\boxed{
\|\Delta\chi_j\|_\infty
\lesssim
\frac{C}{r_0^2L_j^{in}}
+o_j(1).
}
\]

Set

\[
a=\chi_j.
\]

The cutoff is radial, so the relative rotation preserves the weighted vorticity norm at the two period endpoints.

## 5. Period integration and remote coefficient errors

Integrate the weighted identity over one period. The time derivative vanishes because of relative periodicity and radiality of \(\chi_j\).

Move the two coercive terms to the left and discard the nonnegative gradient contribution when seeking a lower bound:

\[
\frac14
\int_0^{S_j}\int\chi_j|\eta_j|^2
\le
\text{cutoff errors}
+\text{background errors}.
\]

By M19-232,

\[
\int_0^{S_j}\|\eta_j\|_2^2ds=O(1),
\qquad
\int_0^{S_j}\|\nabla w_j\|_2^2ds=O(1),
\qquad
\int_0^{S_j}\|w_j\|_2^2ds=1.
\]

Therefore the \(\Delta\chi_j\) and \(y\cdot\nabla\chi_j\) errors tend to zero after first choosing \(r_0\) large and then letting \(j\to\infty\).

The transport-cutoff term obeys

\[
\left|\int(U_j\cdot\nabla\chi_j)|\eta_j|^2\right|
\le
\sup_{r\ge r_0}|U_j|\,\|\nabla\chi_j\|_\infty
\|\eta_j\|_2^2
=o(1).
\]

The strain term is bounded by

\[
\sup_{r\ge r_0}|S_{U_j}|
\int\chi_j|\eta_j|^2
\]

and is made arbitrarily small by taking \(r_0\) large.

The two remaining linearized coupling terms satisfy, schematically,

\[
\left|
\int\chi_j\eta_j\cdot((w_j\cdot\nabla)\Omega_j)
\right|
\lesssim
\sup_{r\ge r_0}|\nabla\Omega_j|
\|\eta_j\|_2\|w_j\|_2,
\]

and

\[
\left|
\int\chi_j\eta_j\cdot((\Omega_j\cdot\nabla)w_j)
\right|
\lesssim
\sup_{r\ge r_0}|\Omega_j|
\|\eta_j\|_2\|\nabla w_j\|_2.
\]

Their period integrals tend to zero uniformly as \(r_0\to\infty\).

Hence

\[
\boxed{
\int_0^{S_j}\int\chi_j|\eta_j|^2\,dy\,ds
\to0.
}
\]

Since \(\chi_j=1\) on \(a_j\le r\le b_j\),

\[
\boxed{
\int_0^{S_j}\int_{a_j\le|y|\le b_j}|\eta_j|^2\,dy\,ds
\to0
}
\]

whenever

\[
a_j\to\infty,
\qquad
\frac{b_j}{R_j}\to0.
\]

This excludes every multiplicatively interior remote vorticity packet.

## 6. Local vorticity also vanishes in the escape branch

M19-231 gives

\[
w_j\to0
\quad\text{strongly in }L^2_{loc}
\]

on the escape branch. The same interior parabolic estimates used in the compactness proof upgrade this, after shrinking compact cylinders, to strong local first-derivative convergence. Hence for each fixed \(r\),

\[
\boxed{
\int_0^{S_j}\int_{B_r}|\eta_j|^2\,dy\,ds\to0.
}
\]

Thus the fixed vorticity currency from M19-232 is genuinely escaping as well.

## 7. Cavity-scale localization theorem

Combine local vanishing with the intermediate-radius exclusion.

Let \(c_j\downarrow0\). If \(c_jR_j\) remains bounded, local vorticity vanishing gives

\[
\int_{|y|\le c_jR_j}|\eta_j|^2\to0.
\]

If \(c_jR_j\to\infty\), choose by a diagonal argument \(a_j\to\infty\) so slowly that

\[
\int_0^{S_j}\int_{|y|\le a_j}|\eta_j|^2\to0.
\]

Apply the preceding intermediate-radius result with

\[
b_j=c_jR_j.
\]

Then

\[
\boxed{
\int_0^{S_j}\int_{|y|\le c_jR_j}|\eta_j|^2\,dy\,ds
\to0
\qquad
\text{for every }c_j\downarrow0.
}
\]

Equivalently,

\[
\boxed{
\lim_{c\downarrow0}
\limsup_{j\to\infty}
\int_0^{S_j}\int_{|y|\le cR_j}|\eta_j|^2\,dy\,ds
=0.
}
\]

Since the total vorticity currency tends to \(1/(4\nu)\), all of it is forced to radii comparable to the cavity radius.

## 8. What has and has not been proved

The valid conclusion is

\[
\boxed{
\text{escape-to-infinity cavity unit mode}
\Longrightarrow
\text{its nonzero vorticity currency lives at }|y|\asymp R_j.
}
\]

This does **not** yet imply concentration in an \(O(1)\)-thick physical boundary layer \(R_j-|y|=O(1)\). The mode may occupy any fixed fractional-radius annulus

\[
cR_j\lesssim |y|<R_j.
\]

Therefore

\[
\boxed{
\text{cavity-scale localization}
\neq
\text{thin boundary-layer localization}.
}
\]

## 9. New frontier

The M19-231 escape branch is reduced to

\[
\boxed{
\mathcal T_{cav}^{esc,bdry-scale}:
\begin{array}{l}
\text{exclude or classify unit-multiplier cavity modes whose fixed vorticity currency}\\
\text{is supported at the expanding scale }|y|\asymp R_j.
\end{array}}
\]

At this scale the background terms vanish, but the similarity drift has magnitude \(O(R_j)\). Thus the next calculation should rescale

\[
y=R_jx
\]

and determine the limiting equation on the unit ball/shell. The viscosity coefficient becomes \(\nu/R_j^2\), while the similarity drift remains order one after radial rescaling, indicating a singular transport-dominated boundary-scale limit rather than an elliptic/parabolic interior limit.

---

\[
\boxed{\text{M19-233 COMPLETE: INTERMEDIATE-RADIUS ESCAPE IS CLOSED; ONLY CAVITY-SCALE VORTICITY ESCAPE REMAINS.}}
\]
