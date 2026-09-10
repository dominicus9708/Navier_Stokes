# M17-479 — One-derivative-lower enstrophy growth thickening splits high enstrophy into persistent occupation or raw-H2 time concentration

**Date:** 2026-09-10  
**Status:** ACTIVE ENSTROPHY-SPIKE THICKENING THEOREM / M17-478 SHORT-TIME BRANCH

## 1. Purpose

M17-478 split normalized enstrophy escape into persistent occupation, short-time spikes, and low-frequency \(\dot H^{-1}\) decompactification.

This module treats the short-time spike branch directly from the vorticity enstrophy equation. The result is one derivative lower than M17-475 and does not require a vorticity-amplitude ceiling.

## 2. Enstrophy evolution

Let
\[
E(t):=\|\Omega(t)\|_2^2,
\qquad
P(t):=\|\nabla\Omega(t)\|_2^2,
\qquad
H(t):=\|\Delta\Omega(t)\|_2^2.
\]
For smooth whole-space Navier--Stokes,
\[
\frac12E'(t)+\nu P(t)
=\int \Omega\cdot\Sigma\Omega\,dx.
\]
Therefore
\[
\frac12E'
\le
\|\Sigma\|_\infty E.
\]
M17-385 gives
\[
\|\Sigma\|_\infty
\lesssim E^{1/8}H^{3/8}.
\]
Hence
\[
\boxed{
E'(t)
\le
C E(t)^{9/8}H(t)^{3/8}.
}
\]
The viscous palinstrophy term is negative and therefore cannot accelerate upward enstrophy growth.

## 3. Half-height crossing estimate

Suppose on \([t_-,t_+]\),
\[
E(t_-)=\frac e2,
\qquad
E(t_+)=e,
\]
and
\[
\frac e2\le E(t)\le e.
\]
From Section 2,
\[
E^{-9/8}E'\le C H^{3/8}.
\]
Integrating,
\[
\int_{e/2}^{e}z^{-9/8}dz
\le
C\int_{t_-}^{t_+}H^{3/8}dt.
\]
The left side equals
\[
8\left((e/2)^{-1/8}-e^{-1/8}\right)
=c_0e^{-1/8}
\]
with a universal \(c_0>0\). Thus
\[
\boxed{
 c_0e^{-1/8}
\le
C\int_{t_-}^{t_+}H^{3/8}dt.
}
\]

Let
\[
\delta:=t_+-t_-.
\]
By Hölder,
\[
\int_{t_-}^{t_+}H^{3/8}dt
\le
\delta^{5/8}
\left(\int_{t_-}^{t_+}Hdt\right)^{3/8}.
\]
Therefore
\[
\boxed{
\int_{t_-}^{t_+}H(t)dt
\ge
c\,e^{-1/3}\delta^{-5/3}.
}
\]

This is the enstrophy spike-formation raw-H2 lower bound.

## 4. Terminal backward-window dichotomy

Let \(t_e\) satisfy
\[
E(t_e)=e>0
\]
and suppose a backward same-branch window of length \(\tau>0\) is available.

There are two cases.

### Case A — persistent high-enstrophy occupation

If
\[
E(t)\ge e/2
\qquad
\text{for all }t\in[t_e-\tau,t_e],
\]
then
\[
\boxed{
\int_{t_e-\tau}^{t_e}E(t)^2dt
\ge
\frac{e^2}{4}\tau.
}
\]
If the M17-478 low-frequency \(\dot H^{-1}\) tightness hypothesis is certified, this is controlled by the unweighted record enstrophy-square ledger and cannot persist on a non-summable family of record times.

### Case B — a last half-height crossing occurs

Let \(t_-\) be the last time in the backward window with
\[
E(t_-)=e/2.
\]
The subsequent crossing to \(e\) has duration
\[
\delta\le\tau.
\]
Section 3 yields
\[
\int_{t_-}^{t_e}Hdt
\ge
c e^{-1/3}\delta^{-5/3}
\ge
c e^{-1/3}\tau^{-5/3}.
\]
Hence
\[
\boxed{
\int_{t_e-\tau}^{t_e}Hdt
\ge
c e^{-1/3}\tau^{-5/3}.
}
\]

Therefore
\[
\boxed{
G_{\rm high\ endpoint\ enstrophy}
\Longrightarrow
G_{\rm persistent\ enstrophy\ occupation}
\lor
G_{\rm raw\text{-}H^2\ time\ concentration}
\lor
G_{\rm backward\ window/genealogy\ loss}.
}
\]

## 5. Ancestry scaling test for the spike branch

At record \(m\), let endpoint height and backward window be \(e_m\) and \(\tau_m\). In the crossing case,
\[
q_m^H
\gtrsim
 e_m^{-1/3}\tau_m^{-5/3}.
\]
The parent raw-H2 contribution is therefore
\[
\boxed{
R_m^{-3}q_m^H
\gtrsim
R_m^{-3}e_m^{-1/3}\tau_m^{-5/3}.
}
\]
The exact series closure criterion is
\[
\boxed{
\sum_m
R_m^{-3}e_m^{-1/3}\tau_m^{-5/3}
=\infty.
}
\]

A sufficient recordwise threshold for order-one parent payment is
\[
 e_m^{-1/3}\tau_m^{-5/3}\gtrsim R_m^3,
\]
equivalently
\[
\boxed{
\tau_m
\lesssim
R_m^{-9/5}e_m^{-1/5}.
}
\]
This is only a sufficient pointwise threshold, not a necessary condition for series divergence.

## 6. Interpretation of the exponent sign

The lower bound
\[
q_m^H\gtrsim e_m^{-1/3}\tau_m^{-5/3}
\]
gets weaker as the endpoint enstrophy height \(e_m\) grows. This is not an error: the nonlinear strain upper bound itself grows with \(E\), so a larger enstrophy state can in principle rise faster for the same raw-H2 level.

The strong variable is instead the formation time. Rapid concentration
\[
\tau_m\downarrow0
\]
forces a large raw-H2 payment with exponent \(\tau_m^{-5/3}\).

Thus `high enstrophy` alone is not a terminal payer. The correct typed alternatives are persistent occupation, time concentration, or low-frequency/genealogy escape.

## 7. Relation to M17-475

M17-475 thickens an endpoint **raw-H2** spike and requires an amplitude ceiling to bound the nonlinear H-growth rate.

M17-479 thickens an endpoint **enstrophy** spike into a raw-H2 spacetime payment and does **not** require an amplitude ceiling, because the strain estimate
\[
\|\Sigma\|_\infty\lesssim E^{1/8}H^{3/8}
\]
closes directly at the enstrophy level.

The two theorems therefore form a two-step hierarchy:
\[
\boxed{
E\text{-spike}
\xrightarrow{\rm M17\text{-}479}
H\text{-spacetime concentration},
\qquad
H\text{-endpoint spike}
\xrightarrow{\rm M17\text{-}475}
H\text{-temporal thickness}.
}
\]

## 8. Remaining firewall

Neither M17-479 nor M17-475 defeats cubic ancestry by itself. The resulting normalized raw-H2 payment must still pass the M17-473/M17-405 weighted test
\[
\sum_mR_m^{-3}q_m^H=\infty.
\]

Persistent high-enstrophy occupation can be sent to M17-478 only when the low-frequency \(\dot H^{-1}\) genealogy is independently certified.

## 9. Next target

The endpoint/enstrophy part of the common-mode exit is now reduced to explicit weighted series. The next unresolved compactness exit is the zero-tube/trace finite-jet branch. The useful audit is to determine whether failure of the M17-470 level-flux persistence
\[
F(s)\gtrsim F(0)
\]
under bounded normalized jets and reach is actually possible, or whether it necessarily forces a finite-jet/normal-chart decompactification already present elsewhere in the frontier.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
