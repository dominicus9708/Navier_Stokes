# DSD M5-196 — Singular-Time Stokes Weight Dominates the W1 Type-I Coefficient Orders

Date: 2026-08-28

Status: **P1_B COEFFICIENT-ORDER BREAKTHROUGH / THE CHOULLI–IMANUVILOV–PUEL–YAMAMOTO SINGULAR-TIME LINEARIZED-NS CARLEMAN USES `phi=e^{lambda eta}/ell(t)^8` WITH `ell(t)~t` AT A TEMPORAL ENDPOINT; ALTHOUGH ITS FINAL VELOCITY-GRADIENT TERM IS NOT MULTIPLIED BY `s phi`, ITS CURL/VELOCITY COERCIVITIES `s phi |rot Z|^2` AND `s^2 phi^2 |Z|^2`, TOGETHER WITH THE DIVERGENCE-FORM SOURCE STRUCTURE, DOMINATE ALL FINITE W1 TYPE-I COEFFICIENT ORDERS `t^-1/2, t^-1, t^-3/2,...` NEAR THE TERMINAL FACE; THE M5-194 LARGE-STRAIN BARRIER IS THEREFORE NOT PRESENT AT THE COEFFICIENT-ORDER LEVEL FOR THIS SINGULAR WEIGHT / SPATIAL LOCALIZATION AND OBSERVATION/CUTOFF TERMS REMAIN THE MAIN YELLOW EDGE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Actual singular-time phase

The singular linearized Navier–Stokes Carleman estimate uses

\[
\boxed{
\phi(x,t)=\frac{e^{\lambda\eta(x)}}{\ell(t)^8},
\qquad
\alpha(x,t)=
\frac{e^{\lambda\eta(x)}-e^{2\lambda\|\eta\|_\infty}}
{\ell(t)^8},
}
\]

where

\[
\ell(t)=t\quad\text{near }t=0,
\qquad
\ell(t)=T-t\quad\text{near }t=T.
\]

Thus near a terminal face, after reversing time,

\[
\boxed{\phi\asymp t^{-8}.}
\]

The theorem controls schematically

\[
\boxed{
\|\nabla Z\|_{L^2_W}
+\|(s\phi)^{1/2}\eta\|_{L^2_W}
+\|s\phi Z\|_{L^2_W}
}
\]

with `eta=rot Z` and `W=e^{2s alpha}`.

Squared, the two decisive coercive channels are

\[
\boxed{
s\phi|\eta|^2
+s^2\phi^2|Z|^2.
}
\]

---

## 2. W1 Type-I physical coefficient hierarchy

Let reverse terminal time be

\[
t=T_*-t_{phys}\downarrow0,
\qquad
\rho^2=r^2+t.
\]

The compact W1 class gives the scale hierarchy

\[
\boxed{
|\nabla^k u|\lesssim \rho^{-1-k}.
}
\]

At the worst point `r=0`,

\[
|u|\lesssim t^{-1/2},
\quad
|\nabla u|\lesssim t^{-1},
\quad
|\nabla^2u|\lesssim t^{-3/2},
\quad\ldots
\]

Every finite spatial derivative therefore grows only by a finite algebraic power of `t^-1`.

---

## 3. Curl equation and divergence-form transport

For the same-tail difference `Z` and

\[
\eta=\operatorname{rot}Z,
\]

the relative curl equation has the form

\[
\partial_t\eta-\nu\Delta\eta
+(A\cdot\nabla)\eta
=\text{coefficient derivatives contracted with }Z,\nabla Z,\eta.
\]

Because

\[
\operatorname{div}A=0,
\]

the leading transport can be rewritten

\[
(A\cdot\nabla)\eta
=\operatorname{div}(A\otimes\eta).
\]

Thus in the negative-order parabolic Carleman estimate it enters through a derivative source `partial_j f_j` with

\[
f_j\sim A_j\eta.
\]

The corresponding RHS scale is

\[
|A|^2|\eta|^2.
\]

---

## 4. Leading Type-I drift is absorbed by `s phi |eta|^2`

At the center,

\[
|A|^2\lesssim t^{-1}.
\]

Meanwhile

\[
s\phi\gtrsim s t^{-8}.
\]

Therefore

\[
\boxed{
\frac{|A|^2}{s\phi}
\lesssim
\frac{t^7}{s}
\to0
\qquad(t\downarrow0).
}
\]

On any finite time interval away from the endpoint, the coefficient is finite and can be absorbed by choosing `s` large enough.

Hence the large Type-I transport does **not** require a small W1 amplitude in this singular-time framework.

---

## 5. First coefficient derivatives are absorbed by the velocity channel

The curl equation contains terms schematically such as

\[
(\nabla A)\nabla Z.
\]

As in the published linearized-NS proof, rewrite

\[
(\partial_kA_j)(\partial_j Z_m)
=
\partial_j\big((\partial_kA_j)Z_m\big)
-(\partial_j\partial_kA_j)Z_m.
\]

This creates a derivative source of scale

\[
f_j\sim (\nabla A)Z
\]

and a nonderivative source of scale

\[
f\sim (\nabla^2A)Z.
\]

The derivative-source square obeys

\[
|f_j|^2
\lesssim
\rho^{-4}|Z|^2
\le t^{-2}|Z|^2.
\]

The velocity coercivity is

\[
s^2\phi^2|Z|^2
\gtrsim
s^2t^{-16}|Z|^2.
\]

Thus

\[
\boxed{
\frac{t^{-2}}{s^2t^{-16}}
=\frac{t^{14}}{s^2}
\to0.
}
\]

The nonderivative source is even cheaper because the negative-order parabolic estimate places an additional inverse `s phi` power on it.

---

## 6. General finite coefficient-order ledger

Suppose a term after finite integration by parts has coefficient

\[
C_m\rho^{-m}
\]

multiplying either `eta` or `Z`, for a fixed finite `m`.

At `r=0`, its square is at worst

\[
C_m^2t^{-m}.
\]

Compared with the curl channel,

\[
\frac{t^{-m}}{s\phi}
\lesssim
s^{-1}t^{8-m},
\]

and compared with the velocity channel,

\[
\frac{t^{-m}}{s^2\phi^2}
\lesssim
s^{-2}t^{16-m}.
\]

For all coefficient orders actually produced by the first-order linearized NSE/curl system (`m` small and finite), the singular weight has a large margin.

Thus the terminal Type-I singularity is **subordinate to the chosen time-Carleman singularity** at the coefficient-order level.

---

## 7. What this repairs from M5-194

M5-194 showed that the polynomial-space/time estimate had only

\[
t|\nabla v|^2
\]

gradient coercivity and hence an arbitrary Type-I strain produced an equal-order obstruction.

The singular-time Stokes/curl estimate uses a different bookkeeping: the dangerous transport/strain terms are placed in derivative-source form and paid predominantly by

\[
s\phi|\eta|^2+s^2\phi^2|Z|^2,
\qquad \phi\sim t^{-8}.
\]

Therefore

\[
\boxed{
\text{M5-194 barrier is weight/formulation-specific, not a surviving coefficient-order obstruction.}
}
\]

---

## 8. Remaining main obstruction: spatial localization

The published singular-time theorem is on a bounded domain and contains either boundary/observation information or uses a localized subdomain `omega` where the spatial Carleman geometry degenerates.

For the W1 whole-space pair there is no physical obstacle boundary condition and no known interior observation at earlier times.

A spatial cutoff creates commutator forcing in an annulus, and this forcing cannot be discarded merely because the terminal data are flat.

Hence the current main YELLOW edge is

\[
\boxed{
\text{Can the spatial phase be arranged so that the cutoff/observation region is exponentially disfavored relative to the target region?}
}
\]

The coefficient-amplitude problem is no longer primary.

---

## 9. DSD audit

### Formation — GREEN

The exact singular phase and coercive channels come from an actual linearized Navier–Stokes Carleman theorem.

### Axis — GREEN

Time singularity strength, coefficient derivative order, curl channel, velocity channel, and spatial localization are kept distinct.

### Static aggregation — GREEN

No small Type-I amplitude is assumed; each coefficient order is compared to an explicit Carleman power.

### Dynamics — GREEN for coefficient-order absorption / YELLOW for whole-space localization

The singular terminal behavior itself is no longer the leading analytic obstruction.

### Cross-audit — GREEN

The argument does not re-use the polynomial-weight gradient absorption that failed in M5-194.

---

## 10. Next calculation

Design the bounded-domain spatial localization for a chosen exterior target ball and compute the spatial phase gap between:

1. the target interior where equality is to be proved;
2. the cutoff/commutator annulus;
3. the observation/degeneracy set of the singular-time Carleman.

A successful strict phase gap would make all artificial-source terms exponentially negligible as `s->infinity`, allowing terminal flatness to propagate backward locally.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
