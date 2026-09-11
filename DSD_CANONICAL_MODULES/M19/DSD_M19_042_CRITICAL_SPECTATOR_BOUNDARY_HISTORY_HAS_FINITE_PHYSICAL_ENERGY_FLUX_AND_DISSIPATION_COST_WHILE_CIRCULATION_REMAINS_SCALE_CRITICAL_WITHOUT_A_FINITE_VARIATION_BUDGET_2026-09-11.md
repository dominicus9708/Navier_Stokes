# M19-042 — Critical spectator-boundary history has finite physical energy-flux and dissipation cost, while circulation remains scale critical without a finite variation budget

**Date:** 2026-09-11  
**Status:** CALCULATION / R-CRITICAL BUDGET AUDIT / PHYSICAL SIMILARITY-JACOBIAN FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-041 exhibits a nonzero bounded aperiodic toroidal scattering datum satisfying all currently certified leading critical-tail constraints.

A natural possible closure route is to argue that persistent critical activity on a fixed similarity spectator sphere must spend infinite physical kinetic energy, energy flux, or viscous dissipation near the singular time.

The present module computes the physical scaling of those budgets. They are integrable.

## 2. Similarity-to-physical scaling

Let

\[
\tau=T_*-t\downarrow0.
\]

Suppressing harmless viscosity constants, the parabolic similarity scaling is

\[
y=\frac{x-x_*}{\sqrt\tau},
\qquad
u(x,t)=\tau^{-1/2}U(y,\theta),
\qquad
p(x,t)=\tau^{-1}P(y,\theta),
\]

with

\[
\theta=-\log\tau.
\]

Fix a spectator radius \(|y|=R_0\). Its physical radius is

\[
\boxed{r_b(t)=R_0\sqrt\tau.}
\]

For a critical tail \(U\sim R_0^{-1}A(q,\omega)\), with bounded nonzero \(A\),

\[
|u|\sim \tau^{-1/2}R_0^{-1},
\qquad
|p|\sim \tau^{-1}R_0^{-2},
\qquad
|\nabla_xu|\sim \tau^{-1}R_0^{-2}.
\]

Also

\[
|\partial B_{r_b}|\sim \tau R_0^2.
\]

## 3. Kinetic energy in a fixed similarity annulus vanishes

For \(R_0<|y|<2R_0\), the physical volume is \(\sim\tau^{3/2}R_0^3\). Hence

\[
E_{ann}(t)
\sim
\tau^{-1}R_0^{-2}\cdot\tau^{3/2}R_0^3
=
\boxed{O(\tau^{1/2}R_0)}.
\]

Thus \(E_{ann}(t)\to0\).

## 4. Convective and pressure energy flux are time integrable

The convective energy flux satisfies

\[
|\Phi_{conv}(t)|
\lesssim C\tau^{-1/2}R_0^{-1}.
\]

The pressure-energy flux has the same scaling. Therefore

\[
\boxed{
\int_{T_*-\varepsilon}^{T_*}
(|\Phi_{conv}|+|\Phi_{press}|)dt
\lesssim C R_0^{-1}\varepsilon^{1/2}<\infty.
}
\]

## 5. Viscous energy flux is also integrable

The viscous energy-flux scale is

\[
\nu |u||\nabla u||\partial B_{r_b}|,
\]

which gives

\[
\boxed{|\Phi_{visc}(t)|\lesssim C\tau^{-1/2}R_0^{-1}}
\]

and hence

\[
\boxed{\int^{T_*}|\Phi_{visc}(t)|dt<\infty.}
\]

## 6. Local viscous dissipation is integrable

On the fixed similarity annulus,

\[
|\nabla u|^2\sim\tau^{-2}R_0^{-4}.
\]

Multiplying by physical volume gives

\[
\int_{ann}|\nabla u|^2dx
\sim
\tau^{-2}R_0^{-4}\cdot\tau^{3/2}R_0^3
=
\boxed{O(\tau^{-1/2}R_0^{-1})}.
\]

Therefore

\[
\boxed{
\int_{T_*-\varepsilon}^{T_*}
\int_{ann(t)}|\nabla u|^2dxdt<\infty.
}
\]

## 7. Angular-momentum-type moments are even cheaper

Adding one physical radius factor \(r_b\sim\tau^{1/2}R_0\) improves the terminal power of \(\tau\). Thus elementary angular-momentum moments do not create a stronger terminal divergence than energy flux.

## 8. Circulation is scale critical but lacks a finite-variation budget

For a fixed-shape similarity loop at radius \(R_0\),

\[
dl_{phys}\sim\sqrt\tau R_0.
\]

Since \(|u|\sim\tau^{-1/2}R_0^{-1}\),

\[
\boxed{\Gamma(t)=\oint u\cdot dl=O(1).}
\]

But a similarity-time-dependent circulation has natural rate

\[
\left|\frac{d\Gamma}{dt}\right|
\sim\tau^{-1}|\partial_\theta\Gamma|,
\]

and

\[
\int\tau^{-1}dt=\int d\theta
\]

need not be finite on an infinite similarity-time interval. Hence

\[
\boxed{\text{scale-critical circulation}\not\Rightarrow\text{finite total variation}.}
\]

## 9. Boundary-history form in q

At fixed spectator radius \(R_0=e^{\rho_0}\),

\[
q=\rho_0-\frac\theta2,
\qquad d\theta=-2dq.
\]

The physical energy-flux Jacobian has an exponential historical weight, whereas the weak-critical obstruction is an unweighted translation problem in \(q\). This is the same structural mismatch as finite enstrophy versus strong \(L^3\) in M5-567.

## 10. Consequence for the toroidal anti-model

The quasiperiodic toroidal datum of M19-041 can remain order one for arbitrarily long \(q\)-history while elementary physical energy/dissipation costs remain integrable. Therefore

\[
\boxed{
\text{persistent aperiodic critical boundary history}
\not\Rightarrow
\text{infinite physical energy/dissipation/energy-flux cost}.
}
\]

## 11. Sharpened R-critical frontier

The remaining observables divide into:

1. subcritical physical budgets, which are terminally integrable;
2. scale-critical signed observables such as circulation, which lack a certified finite-total-variation or one-sign budget;
3. a genuinely global recurrent-hull/cocycle rigidity theorem.

Hence the target remains

\[
\boxed{
\mathcal T_{critical}^{global}:
\text{exclude globally realizable nonzero aperiodic toroidal/radial scattering cocycles}
}
\]

rather than another unsigned local-energy estimate.

---

\[
\boxed{\text{M19-042 COMPLETE; ELEMENTARY PHYSICAL ENERGY AND FLUX BUDGETS DO NOT CLOSE APERIODIC CRITICAL SCATTERING.}}
\]