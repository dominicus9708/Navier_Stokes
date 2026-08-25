# DSD Bounded-Z Weak-L3 Endpoint Exclusion Gate — SUPERSEDED

Date: 2026-08-25

Audit correction: 2026-08-26

Status: **SUPERSEDED / TERMINAL EXCLUSION INVALID / INTERNAL DISTRIBUTION AND BIOT-SAVART ESTIMATES RETAINED / SEE `DSD_AUDIT_BARKER_PRANGE_CUBIC_LOG_RATE_CORRECTION_2026-08-26.md` / GLOBAL REGULARITY UNPROVED.**

## Correction

The original version of this file mis-transcribed the Barker--Prange quantitative Type-I lower bound.

The correct theorem-level quantity is the cubic integral

\[
\int_{B_R}|u(x,t)|^3\,dx
\gtrsim
c(M)\log\frac1{T^*-t},
\]

not the L3 norm itself with a logarithmic lower bound.

Equivalently,

\[
\|u(t)\|_{L^3(B_R)}
\gtrsim
c(M)^{1/3}
\left(\log\frac1{T^*-t}\right)^{1/3}.
\]

The internal weak-L3 plus Linfinity estimate gives

\[
\int_{B_R}|U|^3
\lesssim
C(M,Z_+)(1+\log R),
\]

which, at the Barker--Prange radius, has the same logarithmic order as the external lower bound.

Therefore the old claimed contradiction

\[
\text{bounded Z}+	ext{uniform weak-L3}
\Longrightarrow
\bot
\]

is not established.

## Retained valid ingredients

The following parts of the original calculation remain valid and may still be cited independently:

1. If normalized vorticity satisfies

\[
\|\Omega\|_\infty\le C_\Omega,
\qquad
\|\Omega\|_2^2\le Z_+,
\]

then Biot--Savart splitting gives a normalized velocity ceiling of the form

\[
\|U\|_\infty
\le
C\|\Omega\|_\infty^{1/3}\|\Omega\|_2^{2/3}.
\]

2. If additionally

\[
\|U\|_{L^{3,\infty}}\le M,
\]

then on a measurable set E of finite volume,

\[
\int_E|U|^3
\le
M^3+3M^3
\log_+\left(\frac{K_\infty |E|^{1/3}}{M}\right).
\]

3. Therefore on large balls the cubic integral grows at most logarithmically under uniform weak-L3 and Linfinity control.

These are estimates, not a singularity exclusion theorem.

## Correct dependency

For the full audit and the corrected W1 frontier, use

`DSD_AUDIT_BARKER_PRANGE_CUBIC_LOG_RATE_CORRECTION_2026-08-26.md`.

The original pre-correction content remains available in Git history.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]