# DSD M5-15 — Helical Two-Sector Transfer Floor

Date: 2026-08-26

Status: **DERIVED PRELIMIT STRUCTURAL REDUCTION / POSITIVE CRITICAL H^{1/2} NONLINEAR TRANSFER REQUIRES DEPARTURE FROM A PURE ONE-HELICITY STATE / NO UNIVERSAL QUANTITATIVE MINORITY-HELICITY FLOOR PROVED / GLOBAL W1 HELICAL NORM FINITENESS NOT ASSUMED / GLOBAL REGULARITY UNPROVED.**

## 1. Helical sector energies

On a smooth finite prelimit state with finite critical helical norms, use the Fourier curl eigenvectors

\[
ik\times h_\pm(k)=\pm |k|h_\pm(k),
\]

and write

\[
\widehat U=u_+h_+ + u_-h_-.
\]

Define

\[
X_\pm
:=\frac12\int |k|\,|u_\pm(k)|^2\,dk.
\]

Then

\[
\frac12\|U\|_{\dot H^{1/2}}^2=X_++X_-,
\]

up to normalization, while helicity is proportional to

\[
X_+-X_-.
\]

## 2. Sector evolution

Let `T_+` and `T_-` be the nonlinear contributions to `dX_+/ds` and `dX_-/ds`. Then

\[
\frac{dX_\pm}{ds}
+\nu Y_\pm
=T_\pm,
\]

with

\[
Y_\pm:=\int |k|^3|u_\pm(k)|^2\,dk\ge0.
\]

The Euler nonlinearity conserves helicity, hence its contribution to `X_+-X_-` vanishes. Therefore

\[
\boxed{T_+=T_-.}
\]

The nonlinear source in the total critical Sobolev ledger is twice one common sector transfer.

## 3. Pure one-helicity states

If at one instant

\[
u_-=0,
\]

then `X_-=0` has zero first derivative contribution from the quadratic energy pairing at that instant, so

\[
T_-=0.
\]

Since `T_+=T_-`,

\[
\boxed{T_+=T_-=0}
\]

at that instant.

Thus a strictly homochiral state cannot support a positive instantaneous nonlinear source in the `dot H^{1/2}` ledger. The same holds with the signs reversed.

## 4. DSD consequence

On the finite prelimit track,

\[
\boxed{
\text{positive critical Sobolev cascade}
\Longrightarrow
\text{departure from the homochiral boundary}.
}
\]

This is a qualitative phase-space boundary exclusion.

## 5. What is not yet proved

No universal quantitative estimate of the form

\[
\min(X_+,X_-)\ge c_*>0
\]

has been established.

A useful next estimate would have to degenerate quantitatively when one helical sector becomes small, schematically

\[
|T|
\le
C\,\mathcal M(X_+,X_-,Y_+,Y_-)\,(Y_++Y_-)
\]

with the multiplier tending to zero near a homochiral boundary.

No such closing estimate is proved here.

## 6. Domain audit

A positive-defect W1 omega-limit may carry a logarithmically nonintegrable `1/r` critical corridor. Therefore the global quantities `X_+`, `X_-`, and the full `dot H^{1/2}` norm need not be finite on the limiting state.

Hence M5-15 must be used on smooth finite prelimit states or on critically truncated/localized helical quantities. Passing the statement to the W1 limit requires precisely the kind of critical tightness that M5 is trying to prove.

Do not use the qualitative two-sector statement as if the full omega-limit had finite global helical energies without an additional argument.

## 7. Why this is still relevant

A helical-decimated model with one sign retained has sign-definite helicity equivalent to the critical `H^{1/2}` norm and is globally regular. The full system escapes that mechanism through two-sector interaction.

Therefore, after the domain correction, the next useful subproblem is a **critically localized quantitative helical-mixing estimate**, not a global W1 helical norm estimate.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
