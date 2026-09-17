# M19-376 — Exponentially tilted quarter-strain residence is a kappa-velocity / line-residence hysteresis on recurrent material loops

**Date:** 2026-09-18  
**Status:** NEW INTERNAL REDUCTION / M17-186 RESIDENCE PAYER AUDIT / BOUNDED-STATE HYSTERESIS FIREWALL

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Starting point

M17-186 rewrites the non-gradient part of the M5-688 payer as the exponentially tilted quarter-strain residence excess

\[
Q_\sigma^{(2)}
=
\int e^{2k}
\left(\overline S_\sigma(k)-\frac14\overline F(k)\right)dk.
\]

Its geometric meaning on a regular material vortex loop is expressed through

\[
r_\lambda
:=
\bar\sigma_{\rho,\lambda}-\frac14.
\]

M17-186 gives the exact material-loop relation

\[
\boxed{
\frac d{d\theta}
\log\frac{L_{\rho,\lambda}}{\Phi_\lambda}
=2r_\lambda.
}
\]

We now audit the additional multiplier tilt \(e^{2\kappa}\).

## 2. Define the bounded residence ratio observable

For one persistent material loop label \(\lambda\), define

\[
\boxed{
Y_\lambda
:=
\log\frac{L_{\rho,\lambda}}{\Phi_\lambda}.
}
\]

On the compact recurrent loop branch with comparable positive line weight and material flux,

\[
|Y_\lambda|\le Y_*<\infty.
\]

The exact relation becomes

\[
\boxed{
\dot Y_\lambda=2r_\lambda.
}
\]

## 3. Kappa is one scalar on a CE-H vortex loop

Exact CE-H gives

\[
D_\xi\kappa=0.
\]

Therefore on each connected vortex loop at a fixed time,

\[
\kappa=\kappa_\lambda(\theta)
\]

is constant along the loop.

Define

\[
\boxed{
h_\lambda:=\dot\kappa_\lambda.}
\]

Then

\[
\frac d{d\theta}e^{2\kappa_\lambda}
=2h_\lambda e^{2\kappa_\lambda}.
\]

## 4. Exact recurrent integration by parts

Differentiate the bounded product

\[
e^{2\kappa_\lambda}Y_\lambda.
\]

We obtain

\[
\frac d{d\theta}
\left(e^{2\kappa_\lambda}Y_\lambda\right)
=
2e^{2\kappa_\lambda}
\left(
 h_\lambda Y_\lambda+r_\lambda
\right).
\]

On a recurrent invariant material-loop component the long-time mean derivative vanishes. Hence

\[
\boxed{
\left\langle
 e^{2\kappa_\lambda}r_\lambda
\right\rangle
=
-\left\langle
 e^{2\kappa_\lambda}h_\lambda Y_\lambda
\right\rangle.
}
\]

Thus the exponential tilt converts the zero-mean ordinary residence drift into a phase-correlation term.

## 5. Untilted residence has zero recurrent mean

Since \(Y_\lambda\) itself is bounded recurrent,

\[
\boxed{
\langle r_\lambda\rangle
=
\frac12\langle\dot Y_\lambda\rangle
=0.
}
\]

Therefore any nonzero exponentially tilted payer

\[
\left\langle e^{2\kappa}r\right\rangle
\]

is not a net monotone residence drift. It is created entirely by correlation between multiplier phase and the residence-ratio cycle.

## 6. Hysteresis interpretation

The pair

\[
(\kappa_\lambda,Y_\lambda)
\]

moves on a bounded recurrent state set.

The tilted payer is

\[
\boxed{
\left\langle e^{2\kappa}r\right\rangle
=
-\left\langle e^{2\kappa}hY\right\rangle.
}
\]

For a periodic orbit this is equivalently a closed-cycle integral:

\[
\begin{aligned}
\left\langle e^{2\kappa}r\right\rangle
&=
\frac1{2T}
\oint e^{2\kappa}\,dY\\
&=
-\frac1T
\oint e^{2\kappa}Y\,d\kappa.
\end{aligned}
\]

Hence the payer is a genuine \(\kappa\)-residence hysteresis/circulation, not a one-way finite resource.

The same conclusion extends to a recurrent invariant measure by the generator integration-by-parts identity above.

## 7. Relation to M5-688 / M17-186

M17-186 identifies

\[
S_\sigma-\frac14F
\]

as the \(\kappa\)-resolved extra line-residence growth relative to pure material-flux amplification.

On a persistent closed-loop family, the present calculation shows that the exponential tilt used by M5-688 does not convert this into a Lyapunov drift. It converts it into a bounded-state phase hysteresis.

Thus the schematic payer

\[
\boxed{
Q_\sigma^{(2)}
}
\]

must not be interpreted as an independently exhaustible positive reservoir merely because it is nonzero.

## 8. Combine with M19-375

M19-375 shows

\[
D_\sigma\le C P,
\]

so the explicit strain-gradient payer is palinstrophy-order and critical.

The present module shows that the principal non-gradient residence payer is a recurrent hysteresis.

Therefore two major M5-688 payer channels are now classified as

\[
\boxed{
\begin{aligned}
D_\sigma&:\quad\text{critical palinstrophy-order occupancy},\\
Q_\sigma^{(2)}&:\quad\text{bounded recurrent kappa--residence hysteresis}.
\end{aligned}
}
\]

Neither is presently a nonrecyclable finite resource.

## 9. What remains potentially useful

A contradiction would require an additional theorem showing at least one of:

1. the hysteresis has a one-sided orientation tied to a finite material resource;
2. the same loop/packet cannot reuse the same hysteresis architecture across scales;
3. the cutoff-transition or explicit CE-H geometric remainder has a finite cumulative budget;
4. the loop family must undergo representation-safe replacement whose cost does not geometrically discount.

Without such a theorem, repeated positive cycle-work is compatible with recurrent dynamics.

## 10. Verdict

\[
\boxed{
\text{exponentially tilted quarter-strain payer}
=
\text{bounded recurrent kappa--line-residence hysteresis}
}
\]

on the persistent material-loop subbranch.

This is a NO-GO for treating \(Q_\sigma^{(2)}\) as a new monotone resource.

---

\[
\boxed{\text{M19-376 COMPLETE; THE MAIN NON-GRADIENT STRAIN PAYER IS RECURRENT HYSTERESIS, NOT MONOTONE DEPLETION.}}
\]
