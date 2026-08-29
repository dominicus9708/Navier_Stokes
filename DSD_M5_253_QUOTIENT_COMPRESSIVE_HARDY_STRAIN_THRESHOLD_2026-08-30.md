# DSD M5-253 — Quotient Compressive-Hardy Strain Threshold

Date: 2026-08-30

Parent: `DSD_M5_252_RELATIVE_VORTICITY_HMINUS1_FREQUENCY_IDENTITY_2026-08-30.md`

Status: **EXACT ONE-SIDED FORM GATE / THE QUOTIENT STRAIN PAYER DEPENDS ONLY ON THE COMPRESSIVE PART OF THE CANONICAL-TAIL STRAIN; A SCALE-CRITICAL ONE-SIDED HARDY COEFFICIENT `K_-` CONTROLS THE ENTIRE NEGATIVE STRAIN WORK BY `4 K_- D_Q`; THEREFORE THE M5-250 STRAIN-DOMINANT BRANCH REQUIRES `K_- >= nu/12` / SMALL COMPRESSIVE CRITICAL TAILS CANNOT PAY ONE THIRD OF THE MEAN QUOTIENT DISSIPATION / LARGE-AMPLITUDE COMPRESSIVE TAILS REMAIN / GLOBAL REGULARITY UNPROVED.**

---

## 1. Input from M5-250

The strain-dominant quotient payer is

\[
\boxed{
-\left\langle\int Q^TS_BQ\,dY\right\rangle
\ge
\frac\nu3\langle D_Q\rangle.
}
\]

Only compressive directions of `S_B` can make the left side positive.

---

## 2. One-sided critical strain coefficient

Define

\[
\boxed{
K_-
:=
\sup_{s,Y\ne0}
|Y|^2
\bigl(-\lambda_{\min}(S_B(Y,s))\bigr)_+.
}
\]

For the canonical critical tail `B~1/r`,

\[
S_B\sim r^{-2},
\]

so `K_-` is scale invariant.

The divergence-free smoothing/cutoff convention for `B` is assumed to preserve a finite coefficient of this type; transition-annulus contributions are included in `K_-`.

---

## 3. Pointwise one-sided form bound

At every point,

\[
-Q^TS_BQ
\le
\bigl(-\lambda_{\min}(S_B)\bigr)_+|Q|^2.
\]

Hence

\[
\boxed{
-\int Q^TS_BQ
\le
K_-
\int\frac{|Q|^2}{|Y|^2}dY.
}
\]

Use the sharp three-dimensional Hardy inequality in its standard form

\[
\boxed{
\int_{\mathbb R^3}\frac{|Q|^2}{|Y|^2}dY
\le
4\int|\nabla Q|^2dY.
}
\]

Therefore

\[
\boxed{
-\int Q^TS_BQ
\le
4K_-D_Q.
}
\]

This estimate is global and uses exactly the finite-energy quotient.

---

## 4. Mean threshold

Average the pointwise-in-time form bound:

\[
-\left\langle\int Q^TS_BQ\right\rangle
\le
4K_-\langle D_Q\rangle.
\]

If the strain payer carries at least one third of viscosity as required by M5-250,

\[
\frac\nu3\langle D_Q\rangle
\le
4K_-\langle D_Q\rangle.
\]

For a nontrivial quotient `langle D_Q rangle>0`, cancel it:

\[
\boxed{
K_-\ge\frac\nu{12}.
}
\]

Thus

\[
\boxed{
K_-<\frac\nu{12}
\quad\Longrightarrow\quad
\text{strain cannot be the M5-250 dominant payer.}
}
\]

---

## 5. Interpretation

This is stronger than a bound involving `||S_B||_infty`, because it prices only the spectral sign that can actually transfer energy into the quotient.

The survivor must contain a scale-critical compressive direction satisfying

\[
\boxed{
|Y|^2(-\lambda_{\min}(S_B))_+
\gtrsim \nu.
}
\]

This is a literal large-critical coefficient condition.

---

## 6. Relation to earlier stationary-tail thresholds

Earlier stationary-tail audits found that arbitrary-large critical coefficients prevent simple Hardy absorption, whereas sufficiently small critical stationary tails are perturbative/Landau-like.

The present quotient calculation recovers the same qualitative boundary from a different exact identity:

\[
\boxed{
\text{small compressive critical strain}
\Rightarrow
\text{cannot sustain recurrent quotient dissipation through strain work}.
}
\]

No Landau classification is required for this form gate.

---

## 7. Stronger fractional payer version

More generally, if strain pays a fraction `theta_S` of the mean viscosity,

\[
-\left\langle\int Q^TS_BQ\right\rangle
\ge
\theta_S\nu\langle D_Q\rangle,
\qquad 0<\theta_S\le1,
\]

then

\[
\boxed{
K_-\ge\frac{\theta_S\nu}{4}.
}
\]

The `nu/12` threshold corresponds to `theta_S=1/3`.

---

## 8. What this does not prove

For

\[
K_-\ge\nu/12,
\]

Hardy absorption fails. This does not imply blow-up or contradiction.

A large compressive coefficient can genuinely support a negative quadratic direction of the relative Oseen operator.

Thus the remaining strain branch is precisely

\[
\boxed{
\text{large-critical compressive canonical-tail strain}.
}
\]

It should next be compared with the finite-stage `S_amp` witness inherited in M5-248 and with the positive-middle/projective ledgers, without identifying compression with vorticity stretching pointwise.

---

## 9. DSD verdict

### PROVED

\[
\boxed{
-\int Q^TS_BQ\le4K_-D_Q.
}
\]

Therefore strain dominance requires

\[
\boxed{K_-\ge\nu/12.}
\]

### CLOSED SUBBRANCH

\[
K_-<\nu/12
\]

cannot be the dominant strain payer.

### SURVIVOR

Large scale-critical compression `K_- >= nu/12`.

### OPEN

- route large compression into finite-stage strain/projective/derivative constraints;
- anti-damping low-frequency branch;
- signed residual-work branch;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
