# M19-250 — Critical radial transport is subleading in physical shell coordinates and cannot rescue a regular sublinear shell

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / GAUSSIAN-TO-PHYSICAL-SHELL AUDIT + BRANCH REDUCTION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-242 identified the critical radial coefficient through the Gaussian-weighted defect

\[
-\frac1{4\nu}\int\rho(U\cdot y)|w|^2,
\]

where \(U\cdot y=A_r+\cdots=O(1)\) for a critical \(r^{-1}\) background. M19-244--249 therefore first isolated the radial-free branch.

The physical shell scaling reveals an important refinement: **order one in the Gaussian weighted energy does not mean leading order in the local boundary-shell PDE**. In shell coordinates, the similarity normal drift has coefficient \(R/2\), while the critical radial background velocity has coefficient only \(O(R^{-1})\).

This module removes the radial-free restriction from the regular sublinear-shell rigidity theorem.

## 2. General critical background at a remote shell

Let the retained critical background satisfy

\[
U(r,\omega,s)
=
\frac1r A(q,\omega,s)+O(r^{-3}),
\qquad
q=\log r-\frac s2,
\]

with

\[
A=A_r\omega+A_T.
\]

On a shell

\[
r=R-d,
\qquad d=o(R),
\]

we have

\[
U_r=\frac{A_r}{R}+o(R^{-1}),
\qquad
U_T=O(R^{-1}),
\qquad
\nabla U=O(R^{-2}).
\]

No assumption \(A_r=0\) is made.

## 3. Direct coefficient comparison in physical shell coordinates

Because \(\partial_r=-\partial_d\), the similarity normal transport is

\[
-\frac r2\partial_rw
=
\frac{R-d}{2}\partial_dw.
\]

The radial background transport is

\[
-U_r\partial_rw
=
U_r\partial_dw.
\]

Therefore, whenever \(\partial_dw\neq0\),

\[
\boxed{
\frac{|U_r\partial_dw|}
{|(R-d)\partial_dw/2|}
=O(R^{-2}).
}
\]

This ratio is independent of the shell thickness and of the size of the radial derivative itself. Even in the inner \(\nu/R\) layer, both terms see the same large \(\partial_dw\), so the relative factor remains \(O(R^{-2})\).

Thus

\[
\boxed{
\text{critical radial background transport is two powers of }R\text{ below the similarity normal drift in the physical shell PDE.}
}
\]

## 4. General D=o(R) scaling

Use the M19-249 sublinear scale

\[
\xi=\frac dD,
\qquad
w_T=\frac1{R\sqrt D}V_T,
\qquad
w_r=\frac{\sqrt D}{R^2}V_r,
\qquad
\pi=\frac{R}{D^{3/2}}P,
\]

where

\[
D=o(R).
\]

The leading tangential similarity drift is

\[
\frac1{2D^{3/2}}\partial_\xi V_T.
\]

The radial background transport is

\[
U_r\partial_dw_T
=
O\left(\frac1R\right)
O\left(\frac1{RD^{3/2}}\right)
=
O\left(\frac1{R^2D^{3/2}}\right).
\]

Hence its relative size is

\[
\boxed{O(R^{-2}).}
\]

The tangential background transport is even smaller:

\[
U_T\cdot\nabla_Tw_T
=
O\left(\frac1R\right)
O\left(\frac1R\right)
O\left(\frac1{R\sqrt D}\right)
=
O\left(\frac1{R^3\sqrt D}\right)
\]

under bounded scaled angular frequency.

The stretching term satisfies

\[
(w\cdot\nabla)U
=O(R^{-2})|w|
=O\left(\frac1{R^3\sqrt D}\right)
\]

for the leading tangential component.

Relative to \(D^{-3/2}\), these terms vanish whenever \(D=o(R)\).

## 5. The universal shell normal form is background-independent at leading order

Therefore the M19-249 leading equations remain unchanged for a general critical \(r^{-1}\) background:

\[
\boxed{
\partial_\xi P_0=0,
}
\]

\[
\boxed{
\frac12\partial_\xi V_T
=\nabla_{S^2}P_0,
}
\]

with the H1/inner-impedance matching condition

\[
\boxed{V_T(0)=0.}
\]

Thus

\[
\boxed{
V_T(\xi)=2\xi\nabla_{S^2}P_0.
}
\]

A scale-tight half-line \(L^2\) limit again forces

\[
\boxed{
\nabla_{S^2}P_0=0,
\qquad
V_T=V_r=0.
}
\]

Hence the regular single-scale sublinear shell is excluded **without** assuming \(A_r=0\).

## 6. Why M19-242 and M19-250 are not contradictory

M19-242 uses the Gaussian weight

\[
\rho=e^{-r^2/(4\nu)}.
\]

Its logarithmic radial derivative has size

\[
|\partial_r\log\rho|
=\frac r{2\nu}
\sim\frac R{2\nu}.
\]

Integration by parts therefore amplifies the small critical radial velocity

\[
U_r=O(R^{-1})
\]

into

\[
U_r\,\partial_r\log\rho=O(1/\nu).
\]

That is exactly why \(U\cdot y\) survives as an order-one Gaussian energy defect.

By contrast, the local physical shell PDE compares \(U_r\partial_d\) directly against \((R/2)\partial_d\), producing the ratio \(O(R^{-2})\).

Therefore the correct firewall is

\[
\boxed{
U\cdot y=O(1)\text{ in Gaussian energy}
\neq
U_r\partial_r\text{ is leading in physical shell dynamics}.
}
\]

This also explains why the Gaussian metric is structurally useful for the bare spectral calculation but is not uniformly equivalent to the escaping shell norm as \(R\to\infty\).

## 7. Strengthened shell branch reduction

M19-249 can now be strengthened from the radial-free statement to

\[
\boxed{
\text{general critical background}
+\text{ regular single-scale }D=o(R)\text{ shell}
\Longrightarrow
\text{zero leading shell}.
}
\]

Thus any nonzero escaping cavity unit mode must use at least one of:

\[
\boxed{
\begin{array}{l}
\text{scaled radial/angular/time-frequency decompactification},\\
\text{pressure/profile decompactification},\\
\text{genuinely multiscale boundary-distance mass with no compact median-scale profile},\\
\text{or the macroscopic }D\asymp R\text{ regime.}
\end{array}}
\]

The regular macroscopic weak limit is already zero by M19-238--239. Therefore any surviving escape branch is now a **decompactification branch**, not a regular pressure-supported shell branch.

## 8. Refined bounded-period target

The regular shell target \(\mathcal T_{shell}^{rad-pol}\) is no longer independent. Its surviving content is absorbed into

\[
\boxed{
\mathcal T_{cav}^{decomp}:
\text{exclude/control the scaled derivative, frequency, pressure, or profile decompactification required by an escaping cavity unit mode.}
}
\]

The core-tight branch remains separately open:

\[
\boxed{
\mathcal T_{cav}^{core}.
}
\]

Thus, at the theorem-obligation level,

\[
\boxed{
\mathcal T_{cav}^{comp}
\subset
\mathcal T_{cav}^{core}
\cup
\mathcal T_{cav}^{decomp}.
}
\]

## 9. Scope firewall

This reduction does not yet control the decompactification branch. In particular, the proof has not established the compactness needed to extract every shell limit.

Therefore

\[
\boxed{
\text{no regular shell survivor}
\neq
\text{no cavity escape survivor}.
}
\]

The next calculation should use the already fixed H1/vorticity currency to determine which scaled derivative or frequency can actually decompactify, and whether such growth is compatible with the compact finite hard/scattering hypotheses upstream.
