# Factorized source/dissipation diagnostic certificate

Date: 2026-08-13

Status: **DERIVED DIMENSIONLESS CERTIFICATE FOR THE FACTORIZED INTERPOLATION/SOBOLEV CHAIN / NOT THE CANONICAL SHARP-GN CERTIFICATE**.

> **Audit update.** The inequality in this note remains valid with its own composite constant `C_chain`, but the canonical scalar source bound is now the direct sharp Gagliardo--Nirenberg estimate recorded in `2026-08-13-sharp-gagliardo-nirenberg-consolidation.md`.  The factor `(1+chi_mag)^(-1/2)` must not be multiplied on top of the sharp GN constant unless a separate sharp-GN stability/refinement theorem is proved.

This note is retained as a DSD diagnostic decomposition of why the elementary

\[
L^2\to L^3\to L^6\to\dot H^1
\]

chain loses sharpness.

---

## 1. Factorized source bound

Let

\[
E=\|\omega\|_2^2,
\qquad
P=\|\nabla\omega\|_2^2,
\]

\[
\eta_{\rm ang}
=\frac{P_{\rm ang}}P
\in[0,1]
\]

when `P>0`, and let

\[
\chi_{\rm mag}\ge0
\]

be the enstrophy-weighted magnitude heterogeneity channel.

For the factorized interpolation/Sobolev route one has

\[
\boxed{
|Q|
\le
C_{\rm chain}
E^{3/4}P^{3/4}
(1-\eta_{\rm ang})^{3/4}
(1+\chi_{\rm mag})^{-1/2}.
}
\]

The global enstrophy identity is

\[
\frac12\dot E+\nu P=Q.
\]

---

## 2. Factorized diagnostic certificate

Define

\[
\boxed{
\mathfrak D_{\rm chain}
=
\frac{\nu^4P}{C_{\rm chain}^4E^3}
\frac{(1+\chi_{\rm mag})^2}
{(1-\eta_{\rm ang})^3}.
}
\]

Then

\[
\boxed{
\left(
\frac{|Q|}{\nu P}
\right)^4
\le
\frac1{\mathfrak D_{\rm chain}}.
}
\]

Therefore

\[
\boxed{
\mathfrak D_{\rm chain}>1
\Longrightarrow
|Q|<\nu P
\Longrightarrow
\dot E<0.
}
\]

Conversely, a nondecreasing-enstrophy phase must satisfy

\[
\boxed{
\mathfrak D_{\rm chain}\le1.
}
\]

This implication is exact **for this stated source upper bound and constant**.

---

## 3. Canonical sharp-GN certificate

The preferred source estimate is now

\[
\boxed{
|Q|
\le
C_\sharp E^{3/4}P^{3/4}
(1-\eta_{\rm ang})^{3/4},
\qquad
C_\sharp=C_RC_{\rm GN}^3.
}
\]

Accordingly define

\[
\boxed{
\mathfrak D_{\rm GN}
=
\frac{\nu^4P}
{C_\sharp^4E^3(1-\eta_{\rm ang})^3}.
}
\]

Then

\[
\boxed{
\mathfrak D_{\rm GN}>1
\Longrightarrow
Q<\nu P
\Longrightarrow
\dot E<0.
}
\]

No `chi_mag` factor is inserted into this sharp certificate without an independent sharp-GN stability theorem.

---

## 4. DSD interpretation

Keep

\[
\boxed{
(E,P,\eta_{\rm ang},\chi_{\rm mag})
}
\]

as primary channels.

- `D_GN`: canonical sharp scalar certificate;
- `D_chain`: diagnostic certificate exposing the additional loss in the elementary interpolation/Sobolev factorization;
- `chi_mag`: magnitude-distribution diagnostic and multicore aggregation channel, not an automatic correction of `C_GN`.

This prevents double counting while preserving the structural information discovered by the decomposed route.

---

## 5. Scale invariance

Under Navier--Stokes scaling,

\[
E\mapsto\lambda E,
\qquad
P\mapsto\lambda^3P,
\]

while

\[
\eta_{\rm ang},
\qquad
\chi_{\rm mag}
\]

are invariant.  Therefore both `D_chain` and `D_GN` are scale invariant when their respective constants are fixed.

---

## 6. Claim boundary

Neither certificate proves that its value exceeds one for arbitrary data.  Local moving-window versions also contain shell, near/far strain, and cutoff terms.

Status: **SHARP/NONSHARP CONSTANTS SEPARATED / DOUBLE-COUNTING CORRECTED**.
