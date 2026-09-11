# M19-043 — Viscous Kelvin circulation has logarithmically nonintegrable variation scale and does not compare distinct scattering q-labels

**Date:** 2026-09-11  
**Status:** CALCULATION / R-CRITICAL SIGNED-OBSERVABLE AUDIT / CIRCULATION FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-042 shows that ordinary energy, dissipation and energy-flux budgets are subcritical under the terminal similarity Jacobian, while circulation remains scale critical.

The present module asks whether the exact viscous Kelvin identity supplies the missing finite-total-variation or rigidity theorem for the aperiodic toroidal scattering channel.

It does not.

## 2. Viscous Kelvin identity

Let \(\Gamma_t\) be a smooth closed material loop transported by the velocity \(u\).

For smooth incompressible Navier--Stokes,

\[
\boxed{
\frac d{dt}
\oint_{\Gamma_t}u\cdot dx
=
\nu\oint_{\Gamma_t}\Delta u\cdot dx.
}
\]

The pressure and Euler transport parts cancel in the material-loop derivative.

Define

\[
\Gamma(t):=\oint_{\Gamma_t}u\cdot dx.
\]

Then viscosity is the only source of circulation change.

## 3. Critical similarity scaling of the Kelvin source

On a critical spectator-scale tail near \(T_*\), let

\[
\tau=T_*-t.
\]

For a loop whose similarity radius and shape remain order one around a fixed large spectator radius \(R_0\),

\[
|u|\sim \tau^{-1/2}R_0^{-1},
\]

\[
|\Delta_xu|\sim \tau^{-3/2}R_0^{-3},
\]

and

\[
|dx|\sim \tau^{1/2}R_0.
\]

Therefore the Kelvin source has the critical size

\[
\boxed{
\left|\frac{d\Gamma}{dt}\right|
\lesssim
C\nu\tau^{-1}R_0^{-2}
}
\]

on the retained smooth spectator corridor.

## 4. Physical-time total variation is not finite

Integrating the absolute scale near \(T_*\),

\[
\int_{T_*-\varepsilon}^{T_*}
\tau^{-1}dt
=
\int_0^\varepsilon\frac{d\tau}{\tau}
=\infty.
\]

Thus the critical Kelvin estimate gives no finite total-variation budget:

\[
\boxed{
\int^{T_*}
\left|\frac{d\Gamma}{dt}\right|dt
\text{ need not be finite.}
}
\]

In similarity time

\[
\theta=-\log\tau,
\]

we have

\[
\boxed{
\left|\frac{d\Gamma}{d\theta}\right|
\lesssim
C\nu R_0^{-2}.
}
\]

This is a bounded speed over an infinite \(\theta\)-interval, not a finite variation estimate.

Hence bounded aperiodic oscillation is not excluded.

## 5. Large spectator radius does not solve the infinite-history problem

The factor \(R_0^{-2}\) becomes small when the spectator radius is large.

For any fixed finite similarity-time interval this makes circulation almost conserved.

But the recurrent scattering problem concerns an arbitrarily long/infinite similarity-time history.

The product

\[
R_0^{-2}\times(\text{infinite similarity time})
\]

has no useful finite upper bound.

Taking \(R_0\to\infty\) before the historical limit would compare a different family of loops and is not a justified material nonreuse argument.

## 6. One material loop versus different q labels

The scattering coordinate is

\[
q=\log r-\frac\theta2.
\]

At a fixed spectator boundary, different \(q\) values encode different historical crossing times.

A Kelvin theorem follows **one material loop** through time.

It does not state that two distinct material loops or packets that cross the spectator boundary at different historical times have equal circulation.

Therefore

\[
\boxed{
\text{Kelvin control along one material loop}
\not\Rightarrow
\text{rigidity across the whole function }A(q,\omega).
}
\]

This is especially important for the pure toroidal anti-model of M19-041: its variation in \(q\) may label different radial/material histories rather than temporal variation of one loop.

## 7. Leading toroidal material geometry

For a pure toroidal leading datum,

\[
A_r=0.
\]

The radial material drift produced by the leading critical velocity is zero.  In similarity variables the dominant radial motion is the background dilation, so \(q\) is asymptotically a material label to leading order.

Thus a nonconstant toroidal \(A(q)\) is naturally interpreted as a family of different material layers/labels carrying different circulation data, not as one loop whose circulation oscillates through all \(q\).

This makes the Kelvin shortcut even less applicable to the global \(q\)-profile.

## 8. What circulation could still do

A circulation-based closure would require an additional theorem, for example:

1. a genealogy theorem identifying a recurrent set of distinct \(q\)-layers with one material loop/flux class;
2. a one-sign viscous circulation production law;
3. a finite total-variation budget for the relevant material family;
4. a compactness theorem forcing a common asymptotic circulation invariant across \(q\).

None of these follows from the bare Kelvin identity.

## 9. Consequence for R-critical

The simplest signed observable has now been audited:

\[
\boxed{
\text{scale-critical circulation}
+
\text{viscous Kelvin identity}
\not\Rightarrow
\text{aperiodic scattering rigidity}.
}
\]

Together with M19-035, M19-041 and M19-042, this leaves the R-critical obstruction genuinely global:

\[
\boxed{
\mathcal T_{critical}^{global}:
\text{realization/rigidity of nonzero aperiodic radial--toroidal scattering cocycles over the recurrent hull}.
}
\]

Local asymptotic correction, unsigned energy budgets, and bare circulation conservation/variation are all insufficient.

---

\[
\boxed{\text{M19-043 COMPLETE; THE KELVIN CIRCULATION SHORTCUT IS CLOSED.}}
\]