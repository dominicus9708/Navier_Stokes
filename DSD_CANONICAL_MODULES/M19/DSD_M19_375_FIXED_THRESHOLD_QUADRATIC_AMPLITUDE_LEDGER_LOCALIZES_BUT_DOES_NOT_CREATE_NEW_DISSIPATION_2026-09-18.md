# DSD M19-375 — Fixed-threshold quadratic amplitude ledger localizes the dynamic event problem but creates no new dissipation

Date: 2026-09-18

Status: **NEW INTERNAL CALCULATION / FOR `f_a=(rho-a)_+` AND `N_a=(1/2)int f_a^2`, THE CE-H AMPLITUDE TRANSPORT PLUS THE COMPONENTWISE WEIGHTED ELLIPTIC IDENTITY GIVE THE EXACT FIXED-THRESHOLD BALANCE `N_a' + D_a^(2) + (1/2)N_a + a M_a = S_a`, WHERE `D_a^(2)>=0` IS MAGNITUDE/DIRECTION GEOMETRIC COST AND `S_a=int_{rho>a}(rho-a)rho sigma` IS THE SIGNED AXIAL-STRETCHING PAYER. ON AN INVARIANT RECURRENT COMPONENT THE POSITIVE THRESHOLD DEFICIT IS EXACTLY PAID BY STRETCHING. INTEGRATING OVER ALL THRESHOLDS RECOVERS THE CUBIC-AMPLITUDE LEDGER, SO THIS IS A LOCALIZATION OF EXISTING CE-H DISSIPATION/PRODUCTION RATHER THAN A NEW FINITE CUMULATIVE RESOURCE. THE REMAINING LEVERAGE MUST BE A SAME-THRESHOLD INCIDENCE MISMATCH BETWEEN POSITIVE-RATE CROSSING/TURNOVER EVENTS AND AVAILABLE STRETCHING. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Fixed-threshold observable

Let

\[
f_a:=(\rho-a)_+,
\qquad
M_a:=\int f_a\,dy,
\]

and define

\[
\boxed{
N_a(\theta):=\frac12\int f_a^2dy.
}
\]

For fixed `a>0`, compact CE-H enstrophy bounds imply `N_a<infty`; on the recurrent hard hull it is a bounded state observable.

---

## 2. Material derivative

On CE-H,

\[
D_B\rho=(\sigma+\kappa-1)\rho,
\qquad
\nabla\cdot B=\frac32.
\]

Since

\[
D_B\left(\frac12f_a^2\right)
=f_a\mathbf1_{\rho>a}D_B\rho,
\]

integration over space gives

\[
N_a'
=
\int_{\rho>a}f_a\rho(\sigma+\kappa-1)dy
+\frac32N_a.
\]

Because `N_a=(1/2)int f_a^2`, this is

\[
N_a'
=
\int_{\rho>a}f_a\rho(\sigma+\kappa-1)dy
+\frac34\int f_a^2dy.
\]

---

## 3. Weighted elliptic deficit

The CE-H parallel amplitude equation is

\[
\Delta\rho=(\kappa+|\nabla\xi|^2)\rho.
\]

Multiplying by `f_a=(rho-a)_+` and integrating by parts, the multiplier vanishes on the threshold boundary. Hence

\[
\boxed{
\int_{\rho>a}f_a\kappa\rho\,dy
=-D_a^{(2)},
}
\]

where

\[
\boxed{
D_a^{(2)}
:=
\int_{\rho>a}|\nabla\rho|^2dy
+
\int_{\rho>a}f_a\rho|\nabla\xi|^2dy
\ge0.
}
\]

This is the global fixed-threshold version of the component identity used in M5-656--657.

---

## 4. Exact quadratic threshold ledger

Define the signed stretching payer

\[
\boxed{
S_a
:=
\int_{\rho>a}f_a\rho\sigma\,dy.
}
\]

Then

\[
N_a'
=
S_a-D_a^{(2)}
-\int f_a\rho\,dy
+\frac34\int f_a^2dy.
\]

Since on `rho>a`

\[
\rho=f_a+a,
\]

we have

\[
\int f_a\rho
=
\int f_a^2+aM_a.
\]

Therefore

\[
\boxed{
N_a'
+
D_a^{(2)}
+
\frac12N_a
+
aM_a
=
S_a.
}
\]

This identity is exact.

---

## 5. Recurrent mean

On an invariant recurrent component, `N_a` is bounded and has zero invariant mean derivative. Thus

\[
\boxed{
\langle S_a\rangle
=
\left\langle
D_a^{(2)}
+
\frac12N_a
+
aM_a
\right\rangle
>0
}
\]

for any nontrivial retained threshold layer.

Hence the positive threshold-local geometric/amplitude costs are exactly replenished by positive axial stretching on the same threshold layer.

This is not a contradiction.

---

## 6. Threshold integration

The family also recombines into a known higher-amplitude moment ledger.

Pointwise,

\[
\int_0^\infty\frac12(\rho-a)_+^2da
=\frac16\rho^3.
\]

Therefore

\[
\int_0^\infty N_a da
=\frac16\int\rho^3dy.
\]

Moreover

\[
\int_0^\infty D_a^{(2)}da
=
\int\rho|\nabla\rho|^2dy
+
\frac12\int\rho^3|\nabla\xi|^2dy,
\]

\[
\int_0^\infty aM_a da
=\frac16\int\rho^3dy,
\]

and

\[
\int_0^\infty S_a da
=\frac12\int\rho^3\sigma\,dy.
\]

Hence integrating the exact threshold ledger yields

\[
\boxed{
\frac16\frac d{d\theta}\int\rho^3dy
+
\int\rho|\nabla\rho|^2dy
+
\frac12\int\rho^3|\nabla\xi|^2dy
+
\frac14\int\rho^3dy
=
\frac12\int\rho^3\sigma\,dy.
}
\]

Equivalently,

\[
\boxed{
\frac d{d\theta}\int\rho^3dy
+
6\int\rho|\nabla\rho|^2dy
+
3\int\rho^3|\nabla\xi|^2dy
+
\frac32\int\rho^3dy
=
3\int\rho^3\sigma\,dy.
}
\]

Thus the fixed-threshold family is again a localization of existing CE-H amplitude/strain balance, not a new global resource.

---

## 7. Consequence for the M19-374 dynamic event family

M19-374 compresses recurrent relabeling to

\[
C_{rot}^{force}
\lor
C_{crit}^{higher-jet}
\lor
T_{sheath}^{\rho=a_0}.
\]

The present identity shows that merely proving these events force `D_{a0}^{(2)}>0` is insufficient: recurrent stretching `S_{a0}` can pay that positive cost exactly.

Therefore the meaningful next theorem must be an **incidence mismatch** at one fixed threshold, for example one of:

1. event windows force a uniform lower bound on `D_{a0}^{(2)}` while `S_{a0}` is too small;
2. event windows force a sign/phase condition on `S_{a0}` incompatible with the required positive recurrent mean;
3. force/higher-jet crossing creates a signed quantity not contained in the scalar threshold ledger;
4. sheath turnover can be paired with a finite nonrecyclable material resource rather than with instantaneous dissipation.

---

## 8. Firewall

Do not count `D_a^(2)` as a new dissipation independent of palinstrophy.

Do not infer contradiction from positive-rate threshold turnover plus positive `D_a^(2)` alone.

Do not sum threshold-local deficits as if each had an independent budget.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
