# DSD M5-457 — Metric covector formulation and explicit heat propagator

Date: 2026-09-01

Status: **THE UNIFORMLY ELLIPTIC AFFINE-PULLBACK SYSTEM HAS A NATURAL MOMENTUM COVECTOR `m=Cw` WITH `eta=curl m`; ITS VORTICITY DIFFUSION HAS AN EXPLICIT TIME-DEPENDENT GAUSSIAN PROPAGATOR BECAUSE `G(t)` IS SPATIALLY CONSTANT / ALL STANDARD PARABOLIC SMOOTHING EXPONENTS SURVIVE WITH CONSTANTS DEPENDING ONLY ON THE ELLIPTICITY RATIO / THE REMAINING OBSTRUCTION IS NONLINEAR/ANCIENT RIGIDITY, NOT LOSS OF HEAT-KERNEL CONTROL / GLOBAL REGULARITY REMAINS UNPROVED.**

Let

\[
m:=C(t)w,
\qquad
C=G^{-1}.
\]

Then M5-451 gives

\[
\boxed{\eta=\nabla\times m.}
\]

The affine-pulled velocity equation obtained from the M5-449 strained perturbation equation can be written first as

\[
\partial_t m+(w\cdot\nabla)m
=-\nabla p+\nabla\cdot(G\nabla m).
\]

Since `C` is symmetric and spatially constant,

\[
(\nabla w)^Tm
=\nabla\left(\frac12 w\cdot Cw\right).
\]

Absorbing this gradient into pressure gives the geometric covector form

\[
\boxed{
\partial_t m
+(w\cdot\nabla)m
+(\nabla w)^Tm
=-\nabla\Pi
+\nabla\cdot(G\nabla m),
\qquad w=Gm.
}
\]

Taking curl recovers the M5-451 vorticity equation

\[
\boxed{
\partial_t\eta
+(w\cdot\nabla)\eta
-(\eta\cdot\nabla)w
=\nabla\cdot(G\nabla\eta).
}
\]

Equivalently, using `div w=div eta=0`,

\[
\boxed{
\partial_t\eta-\nabla\cdot(G\nabla\eta)
=\nabla\cdot(\eta\otimes w-w\otimes\eta).
}
\]

For the linear equation

\[
\partial_t f=\nabla\cdot(G(t)\nabla f),
\]

Fourier transformation gives

\[
\widehat f(\xi,t)
=
\exp\left[-\int_s^t\xi^TG(\tau)\xi\,d\tau\right]
\widehat f(\xi,s).
\]

Thus the propagator is

\[
\boxed{
\widehat{P_G(t,s)f}(\xi)
=
e^{-\xi^TQ(t,s)\xi}\widehat f(\xi),
\qquad
Q(t,s):=\int_s^tG(\tau)d\tau.
}
\]

If

\[
\lambda I\le G(t)\le\Lambda I,
\]

then

\[
\lambda(t-s)I\le Q(t,s)\le\Lambda(t-s)I.
\]

Hence the kernel is Gaussian with covariance comparable to `(t-s)I` and the standard smoothing bounds hold:

\[
\boxed{
\|\nabla^kP_G(t,s)f\|_{L^q}
\le
C_{k,p,q,\lambda,\Lambda}
(t-s)^{-k/2-\frac32(1/p-1/q)}
\|f\|_{L^p}.
}
\]

The vorticity mild form is therefore

\[
\boxed{
\eta(t)
=P_G(t,s)\eta(s)
+\int_s^t
P_G(t,\tau)
\nabla\cdot(\eta\otimes w-w\otimes\eta)(\tau)d\tau.
}
\]

This supplies the same critical parabolic smoothing exponents as the standard Navier-Stokes heat semigroup.

Firewall: the time-dependent metric Leray/covector system is not thereby covered by an existing standard Navier-Stokes Liouville theorem. The heat-kernel part transfers; the nonlinear ancient rigidity still needs its own theorem or a justified stability extension.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]