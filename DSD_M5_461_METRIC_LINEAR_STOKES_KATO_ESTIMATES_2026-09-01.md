# DSD M5-461 — Metric linear Stokes/Kato smoothing estimates

Date: 2026-09-01

Status: **THE LINEARIZED UNIFORMLY ELLIPTIC METRIC SYSTEM HAS AN EXPLICIT VELOCITY PROPAGATOR OBTAINED BY `METRIC BIOT-SAVART o ANISOTROPIC HEAT o METRIC CURL`; THE ORDER `-1/+1` OPERATORS CANCEL AND THE REMAINING GAUSSIAN PROPAGATOR HAS THE STANDARD STOKES `Lp-Lq` AND CRITICAL LORENTZ SCALING / THUS THE LINEAR PART OF A METRIC WEAK-`L3` THEORY IS AVAILABLE WITH UNIFORM CONSTANTS / GLOBAL REGULARITY REMAINS UNPROVED.**

Let `B_C` denote the M5-452 inverse of

\[
\eta=\nabla\times(Cw),
\qquad \nabla\cdot w=0.
\]

Thus

\[
w=\mathcal B_C\eta
\]

and `B_C` is a spatial Fourier multiplier homogeneous of degree `-1`, uniformly in a bounded ellipticity class.

For the linearized metric vorticity equation

\[
\partial_t\eta=\nabla\cdot(G(t)\nabla\eta),
\]

M5-457 gives the propagator `P_G(t,s)`.

Given initial velocity `w_s`, define

\[
\eta_s=\nabla\times(C(s)w_s).
\]

Then the corresponding linear metric velocity evolution is

\[
\boxed{
\mathcal S_C(t,s)w_s
:=
\mathcal B_{C(t)}
P_G(t,s)
\nabla\times(C(s)w_s).
}
\]

The outer operators have orders `-1` and `+1`; their composition around the Gaussian heat multiplier is an order-zero uniformly Mikhlin multiplier. Therefore, if

\[
\lambda I\le G(t),C(t)\le\Lambda I,
\]

then for `1<p<=q<infinity`,

\[
\boxed{
\|\mathcal S_C(t,s)f\|_{L^q}
\le
C_{p,q,\lambda,\Lambda}
(t-s)^{-\frac32(1/p-1/q)}
\|f\|_{L^p}.
}
\]

With one derivative,

\[
\boxed{
\|\nabla\mathcal S_C(t,s)f\|_{L^q}
\le
C
(t-s)^{-\frac12-\frac32(1/p-1/q)}
\|f\|_{L^p}.
}
\]

Real interpolation gives the corresponding Lorentz estimates. In particular,

\[
\boxed{
\|\mathcal S_C(t,s)f\|_{L^{3,\infty}}
\le C\|f\|_{L^{3,\infty}},
}
\]

and for `q>3`,

\[
\boxed{
(t-s)^{\frac12-\frac{3}{2q}}
\|\mathcal S_C(t,s)f\|_{L^q}
\le C_q\|f\|_{L^{3,\infty}}.
}
\]

Likewise the standard `L3 -> L-infinity` Kato weight survives:

\[
\boxed{
(t-s)^{1/2}
\|\mathcal S_C(t,s)f\|_\infty
\le C\|f\|_{L^3}.
}
\]

Thus the metric coefficient history does not alter the scale-critical linear smoothing exponents.

What remains for the metric weak-`L^{3,infinity}` package is nonlinear:

1. formulate the metric bilinear Duhamel operator in a velocity/covector space;
2. prove uniform critical bilinear bounds under coefficient convergence;
3. construct the large-data weak-`L^{3,infinity}` stability class used by the Albritton--Barker argument.

The present note completes only the linear step.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]