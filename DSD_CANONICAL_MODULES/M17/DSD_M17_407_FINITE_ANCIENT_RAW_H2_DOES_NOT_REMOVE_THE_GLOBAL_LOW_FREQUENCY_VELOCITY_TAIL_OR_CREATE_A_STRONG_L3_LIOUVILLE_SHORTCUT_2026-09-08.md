# DSD M17-407 — Finite ancient raw-`H2` does not remove the global low-frequency velocity tail or create a strong-`L3` Liouville shortcut

Date: 2026-09-08  
Canonical ID: **M17-407**

Status: **ACTIVE NO-GO / LOW-FREQUENCY FIREWALL / ANCIENT-LIOUVILLE AUDIT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. New temptation after M17-404

M17-404 proves

\[
\int_{-\infty}^{0}
\|\Delta\Omega(t)\|_2^2dt<\infty.
\]

Together with the M5-475 Type-I decay

\[
\|V(t)\|_\infty\lesssim(-t)^{-1/2},
\qquad
\|V(t)\|_6\lesssim(-t)^{-1/4},
\]

one might try to infer a strong critical velocity bound such as

\[
V\in L^3(\mathbb R^3)
\]

with decay at backward infinity and then invoke a Liouville/critical regularity route.

This inference is not justified.

## 2. What M5-476 actually proves

M5-476 localizes the marked ratchet mechanism to a compact divergence-free vorticity packet

\[
\Omega_R^{loc}
\]

and defines its own Biot--Savart velocity

\[
V_R^{loc}=\mathcal B\Omega_R^{loc}.
\]

Because this localized packet is compactly supported, divergence free, and has zero spatial mean, its low frequency is regular enough that

\[
\boxed{
V_R^{loc}\in L^2\cap L^3\cap L^6.
}
\]

But M5-476 explicitly does **not** assert

\[
V\in L^2
\quad\text{or}\quad
V\in L^3
\]

for the full ancient velocity.

The remaining exterior field is asymptotically Galilean on the marked core and may contain a passive/low-frequency global tail.

## 3. Why vorticity `H2` does not control the velocity zero mode

In Fourier variables,

\[
\widehat V(\xi)
=
\frac{i\xi\times\widehat\Omega(\xi)}{|\xi|^2}.
\]

The raw-`H2` norm controls

\[
\int |\xi|^4|\widehat\Omega(\xi)|^2d\xi,
\]

which is a high-frequency quantity.

The velocity `L2` norm would require

\[
\int |\xi|^{-2}|\widehat\Omega(\xi)|^2d\xi<\infty,
\]

which is controlled by the behavior of `Omega-hat` near `xi=0`.

Thus

\[
\boxed{
\Omega\in L^2,
\quad
\Delta\Omega\in L^2
\not\Longrightarrow
V\in L^2.
}
\]

The new finite spacetime raw-`H2` budget does not repair this low-frequency deficit.

## 4. `L6` plus `L-infinity` cannot interpolate downward to `L3`

M5-475 gives

\[
V\in L^6\cap L^\infty
\]

at each sufficiently old time.

Interpolation between these spaces yields only exponents

\[
p\in[6,\infty].
\]

It cannot produce `L3`.

Therefore the decay

\[
\|V\|_6\to0,
\qquad
\|V\|_\infty\to0
\]

at backward infinity does not imply

\[
\|V\|_3\to0.
\]

## 5. Localized strong-critical smallness is not a global restart theorem

For every fixed compact rotational cluster, M5-476 gives a localized velocity with finite `L3`.

As the ancient Type-I amplitudes decay, such a fixed localized component may become small in strong critical norms.

However, the cutoff/Bogovskii localization does not evolve autonomously by Navier--Stokes, and the global exterior tail is not removed.

Thus one cannot restart the full ancient solution from the localized packet alone.

Symbolically,

\[
\boxed{
V_R^{loc}\text{ small in }L^3
\not\Longrightarrow
V\text{ small in }L^3.
}
\]

## 6. Correct consequence of M17-404

The legitimate new conclusion is the finite high-derivative ancestral ledger of M17-405.

It is **not** a global strong-critical velocity theorem.

Hence the current upstream resource hierarchy keeps two different firewalls:

\[
\boxed{
\begin{aligned}
\text{high-frequency raw-`H2`}
&\to\text{finite }R_m^{-3}\text{ ancestral ledger},\\
\text{global velocity low frequency}
&\to\text{passive/exterior tail remains OPEN}.
\end{aligned}
}
\]

## 7. What would be needed for a strong-`L3` route

A valid shortcut would require an additional theorem controlling the global low-frequency velocity component, for example a certified condition implying

\[
V(t)\in L^3
\]

with a uniform or vanishing backward critical norm.

M17-404 alone supplies no such condition.

## 8. DSD audit role

The DSD role is to distinguish derivative/high-frequency resources from global low-frequency state information. The Fourier calculation above is standard mathematics.

## 9. Audit verdict

**PASS-NO-GO.**

Finite ancient raw-`H2` strengthens the cross-generation derivative budget but does not close the ancient element by a strong-`L3` Liouville shortcut.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
