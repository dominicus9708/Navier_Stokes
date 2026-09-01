# DSD M5-452 — Uniform metric div-curl / Biot-Savart estimates

Date: 2026-09-01

Status: **THE M5-451 METRIC CURL LAW REMAINS A CONSTANT-COEFFICIENT FIRST-ORDER ELLIPTIC SYSTEM AT EACH TIME / IF `C` AND `C^-1` ARE UNIFORMLY BOUNDED, THE VELOCITY IS RECOVERED FROM `eta` BY AN ORDER `-1` FOURIER MULTIPLIER WITH UNIFORM CALDERON-ZYGMUND CONSTANTS / THUS THE UNIFORMLY ELLIPTIC BRANCH HAS NO NEW SPATIAL BIOT-SAVART LOSS; ITS ONLY GENUINE NEW DEGREE OF FREEDOM IS THE TIME-DEPENDENT METRIC / GLOBAL REGULARITY REMAINS UNPROVED.**

Assume the M5-451 system

\[
\eta=\nabla\times(Cw),\qquad \nabla\cdot w=0,
\]

where `C=C(t)` is symmetric positive definite, spatially constant, and

\[
\kappa^{-1}I\le C(t)\le \kappa I.
\]

Set

\[
m:=Cw.
\]

Then

\[
\boxed{
\nabla\times m=\eta,
\qquad
\nabla\cdot(C^{-1}m)=0.
}
\]

In Fourier variables this is

\[
i\xi\times\widehat m=\widehat\eta,
\qquad
\xi\cdot C^{-1}\widehat m=0.
\]

For `xi != 0` this is a uniformly elliptic algebraic system on the divergence-free data subspace `xi dot eta_hat=0`. Uniform ellipticity of `C` gives an inverse symbol homogeneous of degree `-1` with angular derivatives bounded by constants depending only on `kappa`.

Therefore

\[
\boxed{
\|\nabla w\|_{L^p}
\le C_{p,\kappa}\|\eta\|_{L^p},
\qquad 1<p<\infty,
}
\]

and conversely

\[
\boxed{
\|\eta\|_{L^p}
\le C_{p,\kappa}\|\nabla w\|_{L^p}.
}
\]

More generally, for every real `s` for which the homogeneous norms are defined,

\[
\boxed{
\|w\|_{\dot H^{s+1}}
\asymp_\kappa
\|\eta\|_{\dot H^s}.
}
\]

In particular the critical correspondence survives:

\[
\boxed{
\|w\|_{\dot H^{1/2}}
\asymp_\kappa
\|\eta\|_{\dot H^{-1/2}}.
}
\]

Thus bounded metric anisotropy does not create a new spatial low-frequency or Calderon-Zygmund escape.

The remaining possibilities are:

1. the metric condition number degenerates, already typed as strong affine/metric throughput;
2. the metric stays uniformly elliptic but varies in time, producing a genuinely time-dependent critical system.

The second branch is the next target.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]