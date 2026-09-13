# M19-247 — The poloidal outer-shell normal form exactly saturates the linear pressure-work currency

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / OUTER-SHELL NORMAL FORM + PRESSURE-WORK NO-GO

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-246 shows that a radial-free shell carrying positive mass in a sublinear distance-to-wall layer requires

\[
\mathcal W_{P,D}(R)=\Omega(R)
\]

of signed poloidal pressure work.

This module tests whether that requirement is itself impossible. The answer is **no**: at fixed physical distance \(d=R-r=O(1)\), the bare similarity-pressure system has a canonical poloidal outer-shell normal form that produces exactly the required order-\(R\) work.

Thus M19-246 is not a closure theorem. It identifies the correct shell scaling and the leading pressure-supported mode.

## 2. Fixed-thickness outer-shell scaling

Let

\[
d=R-r=O(1),
\qquad R\to\infty.
\]

A normalized velocity shell of volume \(O(R^2)\) naturally has tangential amplitude \(O(R^{-1})\). Introduce

\[
\boxed{
w_T=R^{-1}v_T(d,\omega,s),}
\]

and use incompressibility to anticipate the smaller radial scale

\[
\boxed{
w_r=R^{-2}v_r(d,\omega,s).}
\]

To balance the order-one tangential similarity drift, take pressure

\[
\boxed{
\pi=R\,p(d,\omega,s).
}
\]

The background is assumed in the M19-244 leading radial-free critical branch, so its order-one radial transport is absent; \(\nabla U=O(R^{-2})\) is lower order in this outer-shell scaling.

## 3. Radial momentum forces the leading pressure to be independent of d

Because \(\partial_r=-\partial_d\), the radial pressure force is

\[
-\partial_r\pi
=R\,\partial_dp.
\]

All radial velocity terms under the scaling \(w_r=R^{-2}v_r\) are at most order \(R^{-1}\) at fixed bounded derivatives in \(d,s,\omega\). Therefore absence of an unmatched order-\(R\) radial force requires

\[
\boxed{
\partial_dp_0=0.
}
\]

Hence the leading pressure is constant across the fixed-thickness outer shell:

\[
\boxed{
p_0=p_0(\omega,s).}
\]

This is a shell pressure mode, not a radial pressure layer.

## 4. Leading tangential momentum

For the tangential component,

\[
-\frac r2\partial_rw_T
=
\frac{R-d}{2}\partial_d(R^{-1}v_T)
=
\frac12\partial_dv_T+O(R^{-1}).
\]

The physical tangential pressure gradient is

\[
-\frac1r\nabla_{S^2}\pi
=-\nabla_{S^2}p_0+O(R^{-1}).
\]

Time differentiation, viscosity on the fixed \(d\)-scale, the explicit \(-w/2\) term, angular diffusion, and the radial-free background coefficients are all \(O(R^{-1})\) or smaller under the retained bounded-frequency/angular-mode assumptions.

Therefore the order-one tangential equation is

\[
\boxed{
\frac12\partial_dv_T-\nabla_{S^2}p_0=0.
}
\]

Thus

\[
\boxed{
\partial_dv_T=2\nabla_{S^2}p_0.
}
\]

## 5. Fixed H1 currency forces zero leading outer trace at d=0

Let \(a_T\) be the outer tangential amplitude matched to the inner \(\nu/R\) no-slip layer. M19-245 gives the leading layer dissipation

\[
\mathcal D_{BL}^{(0)}
=
\frac R4\int_{S_R}|a_T|^2dS.
\]

The total one-period viscous currency from M19-232 is only

\[
\nu\int_0^S\|\nabla w\|_2^2ds\to\frac14.
\]

Hence a retained sequence must satisfy

\[
R\int_0^S\int_{S_R}|a_T|^2dSds=O(1).
\]

If

\[
a_T=R^{-1}b_T(\omega,s),
\]

then \(dS=R^2d\omega\), so

\[
\int_0^S\|b_T\|_{L^2(S^2)}^2ds=O(R^{-1})\to0.
\]

Therefore the fixed-thickness outer scaling inherits the leading matching condition

\[
\boxed{
v_T(0,\omega,s)=0.}
\]

This is stronger than merely imposing the exact wall condition inside the thinner \(\nu/R\) layer: the fixed H1 budget suppresses an \(O(R^{-1})\) nonzero outer trace.

## 6. Canonical tangential profile

Integrating the leading tangential equation with \(v_T(0)=0\),

\[
\boxed{
v_T(d,\omega,s)
=2d\,\nabla_{S^2}p_0(\omega,s).
}
\]

Thus the leading fixed-thickness shell is necessarily poloidal. A toroidal component has zero right-hand side in the leading equation and, with zero leading trace, vanishes at this order. This is consistent with the M19-241 bare toroidal gap.

## 7. Incompressibility determines the radial component

In spherical variables,

\[
\partial_rw_r+rac2r w_r+rac1r\operatorname{div}_{S^2}w_T=0.
\]

Under

\[
w_r=R^{-2}v_r,
\qquad
w_T=R^{-1}v_T,
\]

the order \(R^{-2}\) equation is

\[
\boxed{
\partial_dv_r
=
\operatorname{div}_{S^2}v_T.
}
\]

The exact no-penetration condition and the inner matching give \(v_r(0)=0\). Hence

\[
\begin{aligned}
v_r(d)
&=
\int_0^d\operatorname{div}_{S^2}
\left(2\delta\nabla_{S^2}p_0\right)d\delta\\
&=
d^2\Delta_{S^2}p_0.
\end{aligned}
\]

Therefore

\[
\boxed{
v_r=d^2\Delta_{S^2}p_0.}
\]

The radial velocity is one extra power of \(R^{-1}\) smaller than the tangential velocity, exactly as required by the shell geometry.

## 8. The leading pressure work exactly matches the M19-246 similarity loss

Recall

\[
\mathcal W_{P,D}
=-\int_0^S\int e^{-d/D}\pi w_r\,dy\,ds.
\]

Using

\[
\pi=Rp_0,
\qquad
w_r=R^{-2}d^2\Delta_{S^2}p_0,
\qquad
dy=R^2(1+O(D/R))\,dd\,d\omega,
\]

we obtain

\[
\begin{aligned}
\mathcal W_{P,D}
&=
-R\int_0^S\int_0^\infty d^2e^{-d/D}dd
\int_{S^2}p_0\Delta_{S^2}p_0d\omega\,ds
+o(R)\\
&=
2RD^3
\int_0^S\int_{S^2}|\nabla_{S^2}p_0|^2d\omega\,ds
+o(R),
\end{aligned}
\]

because

\[
\int_0^\infty d^2e^{-d/D}dd=2D^3.
\]

On the other hand the detected shell mass is, at leading order,

\[
\begin{aligned}
M_D(R)
&=
\int_0^S\int e^{-d/D}|w|^2dy\,ds\\
&=
4\int_0^S\int_0^\infty d^2e^{-d/D}dd
\int_{S^2}|\nabla_{S^2}p_0|^2d\omega\,ds
+o(1)\\
&=
8D^3
\int_0^S\int_{S^2}|\nabla_{S^2}p_0|^2d\omega\,ds
+o(1).
\end{aligned}
\]

Therefore

\[
\boxed{
\mathcal W_{P,D}(R)
=
\frac R4 M_D(R)+o(R).
}
\]

This is exactly the leading similarity-drift loss exposed in M19-246.

## 9. Main conclusion: the pressure-work lower bound is asymptotically sharp

M19-246 required

\[
\mathcal W_{P,D}
\gtrsim
\frac R4 M_D
\]

up to lower-order terms. The canonical poloidal shell gives precisely

\[
\boxed{
\mathcal W_{P,D}
=\frac R4M_D+o(R).
}
\]

Hence

\[
\boxed{
\text{linear-in-R pressure-work requirement}
\neq
\text{shell contradiction}.
}
\]

It is instead the exact leading balance law of the surviving poloidal shell.

## 10. Structural interpretation

The bounded-period escape branch has now acquired a three-scale canonical architecture:

\[
\boxed{
\begin{array}{c}
\text{fixed/sublinear outer poloidal velocity shell}\\
\downarrow\\
\pi\sim R p_0(\omega,s),\quad
w_T\sim 2R^{-1}d\nabla_{S^2}p_0,\quad
w_r\sim R^{-2}d^2\Delta_{S^2}p_0\\
\downarrow\\
\nu/R\text{ passive no-slip/vorticity sublayer.}
\end{array}}
\]

The leading outer pressure transfer exactly replenishes the first-moment similarity loss, while the inner layer dissipates.

The shell is therefore not closed at leading order. Its existence or nonexistence is decided by the **next order**, where time/Floquet return, viscosity, curvature, explicit amplitude damping, angular diffusion, and the lower-order background coupling first enter.

## 11. Refined theorem target

The previous shell target is replaced by

\[
\boxed{
\mathcal T_{shell}^{next}:
\text{derive the next-order solvability/evolution equation for }p_0(\omega,s)
\text{ and determine whether it admits a nonzero relative-periodic solution.}
}
\]

A failure of bounded angular/time derivatives while taking this limit belongs to \(\mathcal T_{scaled-deriv}\).

## 12. Scope firewall

The leading normal form is an asymptotic necessity inside the retained fixed-thickness, bounded-frequency radial-free shell regime. It is not yet an exact cavity eigenfunction.

Therefore

\[
\boxed{
\text{leading poloidal shell normal form}
\neq
\text{existence of a global relative-periodic unit mode}.
}

Conversely, because it exactly saturates M19-246, no contradiction may be claimed from the linear pressure-work currency alone.
