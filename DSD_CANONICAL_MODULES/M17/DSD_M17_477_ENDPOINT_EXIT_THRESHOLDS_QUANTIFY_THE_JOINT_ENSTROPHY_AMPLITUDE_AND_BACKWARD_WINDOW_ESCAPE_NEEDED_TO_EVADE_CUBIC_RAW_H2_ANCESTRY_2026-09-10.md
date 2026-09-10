# M17-477 — Endpoint exit thresholds quantify the joint enstrophy, amplitude, and backward-window escape needed to evade cubic raw-H2 ancestry

**Date:** 2026-09-10  
**Status:** ACTIVE ENDPOINT ESCAPE-THRESHOLD THEOREM / M17-476 NONCOMPACT AUDIT

## 1. Purpose

M17-476 closes the compact common-mode source-return branch into fixed normalized raw-H2 or palinstrophy payments. Its remaining endpoint exits are not independent names: the M17-475 temporal-thickening formula gives an explicit quantitative relation among

- endpoint first moment;
- enstrophy ceiling;
- vorticity-amplitude ceiling;
- available backward CE-H/genealogy time window.

This module writes that relation at record \(m\) and compares it directly with the cubic raw-H2 ancestry weight \(R_m^{-3}\).

## 2. Recordwise endpoint data

Let a retained normalized record have endpoint \(t_{e,m}\) with
\[
A_m(t_{e,m})\ge a_m>0.
\]
Let a backward same-branch window of available normalized length be
\[
\tau_m>0.
\]
On that window define ceilings
\[
E_m^*:=\sup E_m(t),
\qquad
M_m^*:=\sup\|\Omega_m(t)\|_\infty.
\]

M17-469 gives the endpoint raw-H2 height
\[
\boxed{
h_m
:=H_m(t_{e,m})
\ge\frac{a_m^2}{E_m^*}.
}
\]

## 3. Exact lower bound from M17-475

M17-475 gives
\[
\int_{t_{e,m}-\tau_m}^{t_{e,m}}H_m(t)dt
\ge
\frac{h_m}{2}
\min\left\{
\tau_m,
\frac{\log2}{C\left(M_m^*+(E_m^*)^{1/8}h_m^{3/8}\right)}
\right\}.
\]

Since
\[
(E_m^*)^{1/8}h_m^{3/8}
\ge
(E_m^*)^{1/8}
\left(\frac{a_m^2}{E_m^*}\right)^{3/8}
=
a_m^{3/4}(E_m^*)^{-1/4},
\]
care is required: replacing the denominator by this lower bound would move in the wrong direction for a lower estimate. Instead apply M17-475 with the certified lower endpoint height
\[
\underline h_m:=\frac{a_m^2}{E_m^*}
\]
and use monotonicity of
\[
f(h):=\frac{h}{M+(E^*)^{1/8}h^{3/8}}
\]
for \(h>0\), since
\[
f'(h)=
\frac{M+\frac58(E^*)^{1/8}h^{3/8}}
{\left(M+(E^*)^{1/8}h^{3/8}\right)^2}>0.
\]
The terminal-window lower bound is also monotone in \(h\). Hence
\[
\boxed{
q_m^H
:=
\int_{t_{e,m}-\tau_m}^{t_{e,m}}H_mdt
\ge
c\frac{a_m^2}{E_m^*}
\min\left\{
\tau_m,
\frac{1}
{M_m^*+a_m^{3/4}(E_m^*)^{-1/4}}
\right\}.
}
\]
Here and below \(c>0\) absorbs the universal constants and \(\log2\).

## 4. Three explicit endpoint escape regimes

Using
\[
\frac1{x+y}\ge\frac12\min\left\{\frac1x,\frac1y\right\},
\]
the lower bound implies
\[
\boxed{
q_m^H
\gtrsim
\min\left\{
\frac{a_m^2\tau_m}{E_m^*},
\frac{a_m^2}{E_m^*M_m^*},
 a_m^{5/4}(E_m^*)^{-3/4}
\right\}.
}
\]

Thus the endpoint payment can be suppressed only through one or more of:

1. shrinking backward persistence \(\tau_m\);
2. growing enstrophy ceiling \(E_m^*\);
3. growing amplitude ceiling \(M_m^*\);
4. collapse of the endpoint first moment \(a_m\).

The last option means the endpoint branch itself is not the payer and the M17-476 bulk alternatives must be used instead.

## 5. Cubic ancestry test

The certified parent raw-H2 contribution is
\[
R_m^{-3}q_m^H.
\]
Therefore the exact endpoint closure criterion is
\[
\boxed{
\sum_mR_m^{-3}
\frac{a_m^2}{E_m^*}
\min\left\{
\tau_m,
\frac{1}
{M_m^*+a_m^{3/4}(E_m^*)^{-1/4}}
\right\}
=\infty.
}
\]
If this series diverges for a non-reusable certified record family, it contradicts M17-405.

If it converges, endpoint temporal thickening is compatible with the cubic ancestry ledger and no contradiction follows.

## 6. Fixed endpoint first moment

Assume
\[
a_m\ge a_*>0.
\]
Then, up to constants depending on \(a_*\),
\[
\boxed{
q_m^H
\gtrsim
\min\left\{
\frac{\tau_m}{E_m^*},
\frac{1}{E_m^*M_m^*},
(E_m^*)^{-3/4}
\right\}.
}
\]

Consequently, to obtain a **recordwise order \(R_m^3\)** normalized payment from one of the three lower bounds, sufficient pointwise thresholds are respectively
\[
\boxed{
\frac{\tau_m}{E_m^*}\gtrsim R_m^3,
}
\]
\[
\boxed{
E_m^*M_m^*\lesssim R_m^{-3},
}
\]
\[
\boxed{
E_m^*\lesssim R_m^{-4}.
}
\]
These are sufficient recordwise thresholds, not necessary conditions for series divergence.

In particular, bounded order-one \(E_m^*\), \(M_m^*\), and \(\tau_m\) produce only an order-one normalized payment and therefore remain cubic-ancestry summable.

## 7. Directional audit: large E and large amplitude are escape mechanisms

An important sign check is that endpoint first moment obeys
\[
A^2\le EH.
\]
For fixed \(A\), a **smaller** enstrophy ceiling forces a **larger** raw-H2 spike. Hence small \(E_m^*\) strengthens the endpoint payer.

Conversely, growth of \(E_m^*\) weakens the lower bound. Likewise growth of \(M_m^*\) shortens the certified minimum formation time in M17-475.

Therefore the noncompact exits are correctly oriented as
\[
\boxed{
E_m^*\uparrow,
\qquad
M_m^*\uparrow,
\qquad
\tau_m\downarrow.
}
\]
They are not interchangeable with the small-enstrophy regime.

## 8. What M17-477 does and does not close

Closed/refined here:

- the endpoint part of M17-476 no longer has three qualitatively vague exits;
- their exact joint effect is encoded by one explicit recordwise payment formula;
- the cubic ancestry comparison is now a weighted-series criterion.

Still OPEN:

- whether the CE-H survivor forces any lower bound on the series in Section 5 strong enough to diverge;
- whether \(E_m^*\), \(M_m^*\), or \(\tau_m^{-1}\) can decompactify at the required rates;
- non-reusable record allocation and genealogy persistence;
- finite-jet/zero-tube/trace exits;
- root-level branches.

## 9. Low-frequency firewall for the next audit

A tempting next step is to use
\[
\|\Omega\|_2^4
\le
\|u\|_2^2\|\nabla\Omega\|_2^2
\]
to convert enstrophy growth into palinstrophy. This requires a controlled whole-space kinetic-energy norm for the relevant first-generation ancient/record velocity.

That control cannot be silently imported: M17-407 already warns that high-frequency vorticity ledgers do not eliminate the low-frequency velocity tail. Therefore the next module must audit the provenance of any \(L^2_u\) bound before using this interpolation across the ancient record family.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
