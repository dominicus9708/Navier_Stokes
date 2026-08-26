# DSD M5-15 — Helical Two-Sector Transfer Floor

Date: 2026-08-26

Status: **DERIVED STRUCTURAL REDUCTION / POSITIVE CRITICAL H^{1/2} NONLINEAR TRANSFER REQUIRES DEPARTURE FROM A PURE ONE-HELICITY STATE / NO UNIVERSAL QUANTITATIVE MINORITY-HELICITY FLOOR PROVED YET / GLOBAL REGULARITY UNPROVED.**

## 1. Helical sector energies

In Fourier variables use curl eigenvectors

\[
ik\times h_\pm(k)=\pm |k|h_\pm(k),
\]

and write

\[
\widehat U=u_+h_+ + u_-h_-.
\]

Define the positive critical sector energies

\[
X_\pm
:=\frac12\int |k|\,|u_\pm(k)|^2\,dk.
\]

Then

\[
\frac12\|U\|_{\dot H^{1/2}}^2=X_++X_-,
\]

up to the chosen normalization, while helicity is proportional to

\[
X_+-X_-.
\]

## 2. Sector evolution

Let `T_+` and `T_-` denote the nonlinear contributions to `dX_+/ds` and `dX_-/ds`. Then

\[
\frac{dX_\pm}{ds}
+\nu Y_\pm
=T_\pm,
\]

where

\[
Y_\pm:=\int |k|^3|u_\pm(k)|^2\,dk\ge0.
\]

The Euler nonlinearity conserves helicity, hence its contribution to

\[
X_+-X_-
\]

vanishes. Therefore

\[
\boxed{T_+=T_-.}
\]

Consequently the nonlinear source in the total critical Sobolev ledger is twice one common sector transfer.

## 3. Pure one-helicity states

Suppose at one instant

\[
u_-=0.
\]

Then `X_-=0` has vanishing first derivative contribution from the quadratic energy pairing at that instant, so

\[
T_-=0.
\]

By `T_+=T_-`,

\[
\boxed{T_+=T_-=0}
\]

at that instant.

Thus a strictly homochiral state cannot support a positive instantaneous nonlinear source in the `dot H^{1/2}` ledger.

The same holds with `+` and `-` interchanged.

## 4. DSD consequence

M5-13 shows that a large W1 endpoint can evade viscous absorption only by sustaining a sufficiently strong nonlinear critical transfer.

M5-15 shows that such transfer cannot be supported at a purely one-helicity state.

Hence a surviving large-critical recurrent orbit must repeatedly depart from the homochiral boundary of phase space.

Schematically,

\[
\boxed{
\text{positive critical cascade}
\Longrightarrow
\text{two-helicity participation}.
}
\]

## 5. What is not yet proved

The present argument gives a qualitative boundary exclusion, not yet a universal quantitative estimate of the form

\[
\min(X_+,X_-)\ge c_*>0.
\]

To obtain such a floor one needs a trilinear estimate that degenerates quantitatively as one helical sector tends to zero, for example a bound schematically of the form

\[
|T|
\le
C\,\mathcal M(X_+,X_-)\,(Y_++Y_-)
\]

with

\[
\mathcal M(X_+,X_-)\to0
\quad\text{as}\quad
\min(X_+,X_-)\to0.
\]

No such closing estimate is proved in this file.

## 6. Why this is relevant

A helical-decimated model with one sign retained has a sign-definite helicity equivalent to the critical `H^{1/2}` norm and is globally regular. The full system escapes that mechanism only through two-sector interaction.

Therefore the next useful M5 subproblem is not another scalar energy estimate, but a **quantitative helical-mixing estimate**.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
