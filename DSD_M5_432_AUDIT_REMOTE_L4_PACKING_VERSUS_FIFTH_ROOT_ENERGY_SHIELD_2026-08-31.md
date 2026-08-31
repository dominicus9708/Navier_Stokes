# DSD M5-432 — Audit: `L^4_t dot H^{1/2}` remote packing versus the older fifth-root energy shield

Date: 2026-08-31

Status: **SCOPE CORRECTION / M5-430'S EIGHTH-POWER TIME-PACKING LEDGER IS VALID, BUT ITS ASYMPTOTIC CONSEQUENCE `L_j=o(r_j^{-1/4})` IS NOT THE SHARPEST AVAILABLE POINTWISE REMOTE-DISTANCE BOUND / THE OLDER NEAR-MIDDLE-FAR BIOT--SAVART ENERGY TERM ALREADY GIVES THE STRONGER INSTANTANEOUS FIFTH-ROOT SHIELD `L_j lesssim r_j^{-1/5}` FOR A FIXED-FRACTION FAR STRAIN PAYER / THEREFORE M5-430 MUST BE INTERPRETED AS A NEW TIME-INTEGRATED NON-DOUBLE-COUNTING CONSTRAINT, NOT AS AN IMPROVED REMOTE-DISTANCE EXPONENT / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Why this audit is needed

M5-430 proves

\[
\boxed{
\sum_jr_j^2L_j^8<\infty
}
\]

for persistent fixed-fraction remote-source events.

It then notes the necessary consequence

\[
L_j=o(r_j^{-1/4}).
\]

That consequence is mathematically correct.

However the repository already contains a stronger **instantaneous** energy-visibility bound for far-field strain, so the `1/4` exponent must not be advertised as the best remote-distance localization exponent.

---

## 2. Far strain from physical kinetic energy

The whole-space Biot--Savart strain can be integrated by parts in the far region so that one derivative falls on the kernel and the velocity is paired directly with a kernel of size

\[
|x|^{-4}.
\]

Cauchy--Schwarz gives

\[
\boxed{
|S_{>|R|}(x_*)|
\lesssim
R^{-5/2}\|u(t)\|_2.
}
\]

This is the physical version of the far-energy term already present in M5-371.

By the energy inequality,

\[
\|u(t)\|_2\le E_0^{1/2}.
\]

Hence

\[
\boxed{
|S_{>|R|}(x_*)|
\lesssim
E_0^{1/2}R^{-5/2}.
}
\]

---

## 3. Compare with natural target strain

At first-hitting natural scale

\[
r_j=\sqrt{\nu/W_j},
\]

the natural strain size is

\[
\boxed{
S_j^{nat}\asymp\frac{\nu}{r_j^2}.
}
\]

Suppose a fixed fraction of this strain is supplied from distances at least

\[
R_j=L_jr_j.
\]

Then

\[
\frac{\nu}{r_j^2}
\lesssim
E_0^{1/2}R_j^{-5/2}.
\]

Rearranging,

\[
R_j^{5/2}
\lesssim
\frac{E_0^{1/2}}{\nu}r_j^2.
\]

Therefore

\[
\boxed{
R_j
\lesssim
E_0^{1/5}\nu^{-2/5}r_j^{4/5}.
}
\]

Dividing by `r_j`,

\[
\boxed{
L_j
\lesssim
E_0^{1/5}\nu^{-2/5}r_j^{-1/5}.
}
\]

This is the fifth-root energy-visibility/shield law encountered earlier in the affine/remote analysis.

---

## 4. Compare exponents

M5-430 alone gives on a persistent infinite sequence

\[
L_j=o(r_j^{-1/4}).
\]

The instantaneous energy shield gives

\[
L_j\lesssim Cr_j^{-1/5}.
\]

Since

\[
\frac15<\frac14,
\]

and `r_j -> 0`, the fifth-root law is the stronger distance restriction.

Therefore

\[
\boxed{
\text{M5-430 does not improve the best pointwise remote-distance exponent.}
}
\]

---

## 5. What M5-430 still adds

The eighth-power ledger remains genuinely different:

\[
\boxed{
\sum_jr_j^2L_j^8<\infty.
}
\]

The fifth-root shield is a one-time upper bound at each stage.

The M5-430 statement is a **time-integrated non-double-counting condition** derived from the globally finite quantity

\[
\int\|u\|_{\dot H^{1/2}}^4dt.
\]

It therefore constrains how often and how persistently remote critical mass can be used, even inside the already allowed fifth-root spatial window.

The two statements should be retained in parallel:

\[
\boxed{
L_j\lesssim Cr_j^{-1/5}
}
\]

(pointwise energy visibility),

and

\[
\boxed{
\sum_jr_j^2L_j^8<\infty
}
\]

(persistent critical-mass time packing).

---

## 6. Evaluate the eighth-power cost at the fifth-root boundary

At the maximal energy-visible rate

\[
L_j\asymp r_j^{-1/5},
\]

M5-430 charges

\[
r_j^2L_j^8
\asymp
r_j^{2-8/5}
=
\boxed{r_j^{2/5}.}
\]

Since the first-hitting radii decrease geometrically,

\[
\sum_jr_j^{2/5}<\infty.
\]

Thus even persistent sources living near the fifth-root shield boundary are **not excluded** by the new global `L4` ledger.

This is an important firewall against claiming that M5-430 closes the remote branch.

---

## 7. Consequence for the next target

The surviving hard corridor can use remote source radii up to roughly

\[
R_j\sim r_j^{4/5}
\]

while paying a globally summable `L4` cost.

Therefore another pure distance-power estimate is unlikely to close the proof.

A successful next step must use additional structure such as

- source direction/flux geometry;
- material or Eulerian recurrence;
- a sharper time-persistence lower bound growing with `L`;
- or a coupling-efficiency law that charges more than `L^4` critical mass inside the fifth-root window.

---

## 8. DSD verdict

### CORRECTED INTERPRETATION

M5-430 = time-packing improvement, not pointwise distance-exponent improvement.

### STRONGEST CURRENT POINTWISE FAR-DISTANCE LAW

\[
\boxed{
L_j\lesssim Cr_j^{-1/5},
\qquad
R_j\lesssim Cr_j^{4/5}.
}
\]

### ADDITIONAL GLOBAL PACKING

\[
\boxed{
\sum_jr_j^2L_j^8<\infty.
}
\]

### STATUS

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
