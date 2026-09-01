# DSD M5-454 — Uniform metric angular-depletion lemma by Fourier div-curl

Date: 2026-09-01

Status: **THE BOUNDED-METRIC DIV-CURL LAW RETAINS A QUANTITATIVE ANGULAR DEPLETION MECHANISM WITHOUT REQUIRING THE STANDARD ISOTROPIC BIOT-SAVART KERNEL FORMULA / FOR EVERY FIXED AXIS `e`, THE LONGITUDINAL STRAIN `e^T S_w e` IS CONTROLLED IN `L2` BY THE VORTICITY COMPONENT TRANSVERSE TO `e` / THUS REPEATED FIRST-HITTING STRETCHING IN THE UNIFORMLY ELLIPTIC BRANCH CANNOT BE SUPPLIED BY A PERFECTLY ALIGNED VORTICITY FIELD / GLOBAL REGULARITY REMAINS UNPROVED.**

Assume

\[
\eta=\nabla\times(Cw),\qquad \nabla\cdot w=0,
\]

with

\[
\kappa^{-1}I\le C\le\kappa I.
\]

Let

\[
S_w=\frac12(\nabla w+\nabla w^T)
\]

and fix a unit vector `e`. Define

\[
\gamma_e:=e^TS_we.
\]

In Fourier variables,

\[
\boxed{
\widehat{\gamma_e}(\xi)
=i(e\cdot\xi)(e\cdot\widehat w(\xi)).
}
\]

By M5-452, the metric div-curl inverse is an order `-1` multiplier, hence

\[
|\widehat w(\xi)|
\le C_\kappa |\xi|^{-1}|\widehat\eta(\xi)|.
\]

Decompose

\[
\widehat\eta=a e+b,
\qquad b\perp e.
\]

Since `div eta=0`,

\[
a(e\cdot\xi)+\xi\cdot b=0.
\]

Therefore

\[
|e\cdot\xi|\,|a|
\le |\xi|\,|b|.
\]

Also `|e dot xi|<=|xi|`, so

\[
\frac{|e\cdot\xi|}{|\xi|}|\widehat\eta|
\le
\frac{|e\cdot\xi|}{|\xi|}(|a|+|b|)
\le 2|b|.
\]

Thus

\[
|\widehat{\gamma_e}(\xi)|
\le
2C_\kappa |b|
=
2C_\kappa |(I-e\otimes e)\widehat\eta(\xi)|.
\]

Plancherel gives the exact metric-uniform angular depletion estimate

\[
\boxed{
\|e^TS_we\|_{L^2}
\le
C_\kappa
\|(I-e\otimes e)\eta\|_{L^2}.
}
\]

Consequences:

1. if `eta` is everywhere parallel to one fixed direction `e`, then `e^T S_w e=0` identically;
2. order-one longitudinal strain requires a nonzero transverse vorticity reservoir;
3. on the first-hitting corridor, the existing M5-377/M5-392 analyticity-thickening audit can be reused after a bounded linear distortion to convert persistent longitudinal stretching into either local transverse occupancy or remote/delocalized transverse mass.

Firewall: the estimate is global `L2`. A pointwise strain value alone does not automatically yield a fixed `L2` lower bound without the already audited first-hitting thickness/analyticity input. No such silent step is taken here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]