# DSD M5-194Y — Periodic Betchov-Residual Necessary Budget and Viscosity Normalization

Date: 2026-08-29

Parent: `DSD_M5_194X_LERAY_VORTICITY_ENSTROPHY_AND_PERIODIC_STRETCHING_PAYMENT_AUDIT_2026-08-29.md`

Status: **NORMALIZATION CORRECTION + FINITE SCALAR REDUCTION / RESTORING GENERAL VISCOSITY GIVES `1/2 Z' + nu Q + Z/4 = P_stretch` / COMBINING THIS WITH THE EXISTING POSITIVE-MIDDLE/BETCHOV-RESIDUAL SPLIT PRODUCES AN EXACT NECESSARY LOWER BUDGET FOR THE PERIOD-AVERAGED BETCHOV RESIDUAL / IF THE NORMALIZED VORTICITY AMPLITUDE IS BELOW THE `1/2` THRESHOLD, A NONZERO PERIODIC ORBIT MUST PAY A STRICTLY POSITIVE RESIDUAL OR PALINSTROPHY COST; ABOVE THAT THRESHOLD POSITIVE-MIDDLE PRODUCTION CAN PAY THE LINEAR LERAY DAMPING WITHOUT A FORCED RESIDUAL / GLOBAL REGULARITY UNPROVED.**

---

## 1. Viscosity normalization correction

M5-194X wrote the similarity vorticity ledger in the normalized convention `nu=1`.

For the repository's general viscosity `nu>0`, the backward Leray velocity equation is

\[
V_s-\nu\Delta V
+\frac12V
+\frac12(Y\cdot\nabla)V
+(V\cdot\nabla)V
+\nabla P=0.
\]

The vorticity equation is

\[
\Omega_s-\nu\Delta\Omega
+\Omega
+\frac12(Y\cdot\nabla)\Omega
+(V\cdot\nabla)\Omega
-(\Omega\cdot\nabla)V=0.
\]

Hence, after the large-sphere boundary terms vanish on the W1/spatial-Type-I derivative corridor,

\[
\boxed{
\frac12Z'(s)
+\nu Q(s)
+\frac14Z(s)
=\mathcal P(s),
}
\]

where

\[
Z=\|\Omega\|_2^2,
\qquad
Q=\|\nabla\Omega\|_2^2,
\qquad
\mathcal P=\int\Omega^TS\Omega.
\]

Thus every `Q` in M5-194X's global/period-averaged formulas should be read as `nu Q` when viscosity has not been normalized to one.

No qualitative conclusion of M5-194X changes.

---

## 2. Periodic stretching identity

For an `S`-periodic profile,

\[
Z(s+S)=Z(s),
\]

so

\[
\boxed{
\langle\mathcal P\rangle_S
=\nu\langle Q\rangle_S
+\frac14\langle Z\rangle_S.
}
\]

For a nonzero periodic orbit,

\[
\langle Z\rangle_S>0.
\]

---

## 3. Existing Betchov residual split

The repository proved the pointwise-in-time estimate

\[
\boxed{
\mathcal P(s)
\le
\frac12M(s)Z(s)
+\mathcal R_B(s),
}
\]

where

\[
M(s):=\|\Omega(s)\|_\infty
\]

and

\[
\boxed{
\mathcal R_B(s)
:=
\int_{\{\lambda_2<0\}}
\bigl(\Omega^TS\Omega+4\det S\bigr)_+\,dY.
}
\]

The first term is the positive-middle efficiency channel; `R_B` measures positive stretching occurring in the negative-middle geometry beyond what the global Betchov relation can cancel locally.

---

## 4. Exact period-averaged residual lower bound

Average the upper estimate and use the exact periodic stretching identity:

\[
\nu\langle Q\rangle_S
+\frac14\langle Z\rangle_S
\le
\frac12\langle MZ\rangle_S
+\langle\mathcal R_B\rangle_S.
\]

Therefore every nonzero periodic survivor satisfies

\[
\boxed{
\langle\mathcal R_B\rangle_S
\ge
\nu\langle Q\rangle_S
+\frac14\langle Z\rangle_S
-\frac12\langle MZ\rangle_S.
}
\]

This is the exact finite scalar residual-budget inequality.

---

## 5. Insert a uniform similarity-vorticity cap

The first-hitting alpha-limit carries a Type-I similarity-vorticity cap

\[
\boxed{
M(s)\le K_I
}
\]

on the inherited corridor.

Hence

\[
\langle MZ\rangle_S
\le
K_I\langle Z\rangle_S.
\]

Thus

\[
\boxed{
\langle\mathcal R_B\rangle_S
\ge
\nu\langle Q\rangle_S
+
\left(
\frac14-\frac{K_I}{2}
\right)
\langle Z\rangle_S.
}
\]

This formula cleanly separates the amplitude and derivative thresholds.

---

## 6. Sub-half amplitude regime

If

\[
\boxed{K_I<\frac12,}
\]

then

\[
\frac14-\frac{K_I}{2}>0.
\]

Consequently every nonzero periodic orbit must have

\[
\boxed{
\langle\mathcal R_B\rangle_S
\ge
\left(
\frac14-\frac{K_I}{2}
\right)
\langle Z\rangle_S
>0,
}
\]

and in fact also pays the positive palinstrophy term

\[
\nu\langle Q\rangle_S.
\]

Thus the sub-half periodic branch is forced into a recurrent Betchov-residual/derivative cost.

If an independent corridor assumption says `R_B` is asymptotically negligible, the branch closes immediately.

---

## 7. Threshold case

If

\[
K_I=\frac12,
\]

then

\[
\boxed{
\langle\mathcal R_B\rangle_S
\ge
\nu\langle Q\rangle_S.
}
\]

A nonzero spatially varying vorticity profile has

\[
Q>0
\]

on a positive-measure set, so a residual-free periodic orbit is again impossible.

Only the impossible spatially constant `L2` vorticity limit could make `Q=0`.

---

## 8. Super-half amplitude regime

If

\[
K_I>\frac12,
\]

the coefficient

\[
\frac14-\frac{K_I}{2}
\]

is negative.

Then the lower bound does not force `R_B>0` unless palinstrophy is sufficiently large:

\[
\boxed{
\nu\frac{\langle Q\rangle_S}{\langle Z\rangle_S}
>
\frac{K_I}{2}-\frac14.
}
\]

Define the period-averaged vorticity frequency

\[
\boxed{
\Lambda_\Omega
:=
\frac{\langle Q\rangle_S}{\langle Z\rangle_S}.
}
\]

Then

\[
\boxed{
\langle\mathcal R_B\rangle_S
\ge
\left[
\nu\Lambda_\Omega
+rac14-rac{K_I}{2}
\right]
\langle Z\rangle_S.
}
\]

Thus a residual-quiet super-half survivor must satisfy the frequency ceiling

\[
\boxed{
\nu\Lambda_\Omega
\le
\frac{K_I}{2}-\frac14.
}
\]

This is a genuine finite scalar compatibility condition.

---

## 9. Residual-quiet periodic window

Suppose more quantitatively that

\[
\langle\mathcal R_B\rangle_S
\le
\varepsilon_R\langle Z\rangle_S.
\]

Then necessarily

\[
\boxed{
\nu\Lambda_\Omega
\le
\frac{K_I}{2}-\frac14+\varepsilon_R.
}
\]

Thus the Betchov-residual-quiet periodic branch lies in a low normalized palinstrophy-frequency window.

This connects directly to the repository's existing recurrent-frequency barriers and projective viscous-tax lower bounds.

---

## 10. Comparison with the middle-strain threshold gate

The existing periodic Betchov/middle-strain theorem independently gives

\[
\boxed{
\sup_{Y,s}\lambda_2^+(Y,s)>\frac14
}
\]

for every nonzero W1 periodic orbit.

There is no contradiction between that pointwise threshold and the low average vorticity-frequency window above.

A flow may have strong positive-middle strain on a small recurrent region while keeping its global `Q/Z` moderate.

Therefore the next closure must use **occupancy/action**, not threshold height alone.

---

## 11. DSD verdict

### EXACT REDUCTION

Every nonzero periodic alpha-limit satisfies

\[
\boxed{
\frac{\langle\mathcal R_B\rangle_S}{\langle Z\rangle_S}
\ge
\nu\Lambda_\Omega
+rac14
-rac12\frac{\langle MZ\rangle_S}{\langle Z\rangle_S}.
}
\]

Under `M<=K_I`, this simplifies to the explicit lower bound above.

### CLOSED CONDITIONAL REGION

- `K_I<1/2` plus residual-quietness is impossible;
- `K_I=1/2` plus residual-free dynamics is impossible;
- for `K_I>1/2`, sufficiently large average palinstrophy forces positive residual.

### SURVIVING FINITE WINDOW

A residual-quiet periodic survivor must have

\[
\boxed{
K_I>\frac12,
\qquad
\nu\Lambda_\Omega
\le
\frac{K_I}{2}-\frac14+\varepsilon_R.
}
\]

plus the positive-middle finite-core payer and the long-period/nonsummable-tail restrictions already derived.

---

## 12. Next audit target

Compare the **upper frequency window**

\[
\nu\Lambda_\Omega
\le
\frac{K_I}{2}-\frac14+\varepsilon_R
\]

with the lower frequency/action bound already generated by positive-middle transverse/projective motion on the pure recurrent corridor.

If the lower bound exceeds the upper bound, the residual-quiet periodic branch closes by a finite constant comparison.

If not, the remaining periodic survivor is compressed to a finite interval in the normalized frequency parameter rather than an unrestricted PDE class.
