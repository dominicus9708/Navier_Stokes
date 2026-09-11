# M19-042 — Critical spectator-boundary history has finite physical energy-flux and dissipation cost, while circulation remains scale critical without a finite variation budget

**Date:** 2026-09-11  
**Status:** CALCULATION / R-CRITICAL BUDGET AUDIT / PHYSICAL SIMILARITY-JACOBIAN FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-041 exhibits a nonzero bounded aperiodic toroidal scattering datum satisfying all currently certified leading critical-tail constraints.

A natural possible closure route is to argue that persistent critical activity on a fixed similarity spectator sphere must spend infinite physical kinetic energy, energy flux, or viscous dissipation near the singular time.

The present module computes the physical scaling of those budgets.

They are integrable.

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

Fix a spectator radius

\[
|y|=R_0.
\]

Its physical radius is

\[
\boxed{
r_b(t)=R_0\sqrt\tau.
}
\]

For a critical tail

\[
U\sim R_0^{-1}A(q,\omega),
\]

with bounded nonzero \(A\), the physical sizes on the spectator sphere are

\[
|u|\sim \tau^{-1/2}R_0^{-1},
\]

\[
|p|\sim \tau^{-1}R_0^{-2},
\]

\[
|\nabla_xu|\sim \tau^{-1}R_0^{-2}.
\]

The physical boundary area satisfies

\[
|\partial B_{r_b}|\sim \tau R_0^2.
\]

## 3. Kinetic energy in a fixed similarity annulus vanishes

Take a fixed similarity annulus \(R_0<|y|<2R_0\). Its physical volume is

\[
\sim \tau^{3/2}R_0^3.
\]

Hence its kinetic energy is

\[
E_{ann}(t)
\sim
\tau^{-1}R_0^{-2}\cdot\tau^{3/2}R_0^3
=
\boxed{O(\tau^{1/2}R_0)}.
\]

Thus

\[
\boxed{E_{ann}(t)\to0.}
\]

Persistent order-one similarity amplitude does not create a fixed physical-energy atom on a fixed spectator annulus.

## 4. Convective and pressure energy flux are time integrable

The convective kinetic-energy flux density scales as \(|u|^3\). Through the spectator sphere,

\[
\Phi_{conv}(t)
\sim
|u|^3|\partial B_{r_b}|
\sim
\tau^{-3/2}R_0^{-3}\cdot\tau R_0^2.
\]

Therefore

\[
\boxed{
|\Phi_{conv}(t)|
\lesssim
C\tau^{-1/2}R_0^{-1}.
}
\]

Similarly the pressure-energy flux scales as

\[
|p||u||\partial B_{r_b}|
\sim
\tau^{-1}\tau^{-1/2}\tau
\,R_0^{-2}R_0^{-1}R_0^2
=
O(\tau^{-1/2}R_0^{-1}).
\]

Hence

\[
\boxed{
\int_{T_*-\varepsilon}^{T_*}
(|\Phi_{conv}|+|\Phi_{press}|)dt
\lesssim
C R_0^{-1}\varepsilon^{1/2}<\infty.
}
\]

A nondecaying recurrent boundary history is therefore compatible with finite cumulative physical energy transport near \(T_*\).

## 5. Viscous energy flux is also integrable

The viscous energy-flux scale is

\[
\nu |u||\nabla u||\partial B_{r_b}|.
\]

Using the similarity sizes,

\[
|u||\nabla u||\partial B_{r_b}|
\sim
\tau^{-1/2}R_0^{-1}\cdot
\tau^{-1}R_0^{-2}\cdot
\tau R_0^2.
\]

Thus

\[
\boxed{
|\Phi_{visc}(t)|
\lesssim
C\tau^{-1/2}R_0^{-1}
}
\]

and

\[
\boxed{
\int^{T_*}|\Phi_{visc}(t)|dt<\infty.
}
\]

## 6. Local viscous dissipation is integrable

On the fixed similarity annulus,

\[
|\nabla u|^2
\sim
\tau^{-2}R_0^{-4}.
\]

Multiplying by physical volume,

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
\int_{ann(t)}|\nabla u|^2dxdt
<\infty.
}
\]

Thus ordinary Leray dissipation does not exclude persistent aperiodic critical spectator activity.

## 7. Angular-momentum-type moments are even cheaper

Adding one physical radius factor \(r_b\sim\tau^{1/2}R_0\) to the above momentum/flux densities improves the terminal power of \(\tau\).

For example a schematic angular-momentum density contains

\[
x\times u,
\]

whose magnitude on the spectator annulus is order one in \(\tau\), while the physical volume still tends to zero like \(\tau^{3/2}\).

Hence elementary angular-momentum moments do not produce a stronger terminal divergence than the energy flux.

## 8. Circulation is different but has no finite-variation budget

For a loop of fixed shape and radius \(R_0\) in similarity variables, the physical loop length is

\[
dl_{phys}\sim\sqrt\tau R_0.
\]

Since

\[
|u|\sim\tau^{-1/2}R_0^{-1},
\]

the circulation scale is

\[
\boxed{
\Gamma(t)=\oint u\cdot dl=O(1).
}
\]

Thus circulation is scale critical and could in principle remember the toroidal history without the shrinking \(\tau^{1/2}\) factor.

However scale criticality alone is not a finite-budget theorem.

The natural rate scale of a similarity-time-dependent circulation is

\[
\left|\frac{d\Gamma}{dt}\right|
\sim
\tau^{-1}|\partial_\theta\Gamma|.
\]

Its absolute physical-time integral corresponds to

\[
\int \tau^{-1}dt
=\int d\theta,
\]

which need not be finite on an infinite similarity-time interval.

Therefore

\[
\boxed{
\text{scale-critical circulation}
\not\Rightarrow
\text{finite total variation}.
}
\]

A recurrent toroidal signal may oscillate indefinitely unless an additional monotone/sign or viscosity-specific circulation theorem is available.

## 9. Boundary-history form in q

At fixed spectator radius \(R_0=e^{\rho_0}\),

\[
q=\rho_0-\frac\theta2.
\]

Hence

\[
d\theta=-2dq.
\]

The physical energy-flux Jacobian satisfies

\[
\tau^{-1/2}dt
\sim
 e^{-\theta/2}d\theta
\sim
 e^{q}\,dq
\]

up to the fixed \(R_0\)-dependent factor and orientation of the historical half-line.

Thus physical energy budgets see an **exponential historical weight**, whereas the weak-critical obstruction is an unweighted translation problem in \(q\).

This is the same structural mismatch already visible between finite enstrophy and strong \(L^3\) in M5-567.

## 10. Consequence for the toroidal anti-model

The quasiperiodic toroidal datum of M19-041 can remain order one for arbitrarily long \(q\)-history while all elementary physical energy/dissipation costs near the terminal time remain integrable because of the similarity Jacobian.

Therefore the following elementary route is closed:

\[
\boxed{
\text{persistent aperiodic critical boundary history}
\not\Rightarrow
\text{infinite physical energy/dissipation/energy-flux cost}.
}
\]

## 11. Sharpened R-critical frontier

The remaining candidate observables divide into:

1. **subcritical physical budgets** (energy, dissipation, ordinary flux), which are terminally integrable and cannot close the branch;
2. **scale-critical signed observables** such as circulation, which do not come with a certified finite total-variation or one-sign budget;
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