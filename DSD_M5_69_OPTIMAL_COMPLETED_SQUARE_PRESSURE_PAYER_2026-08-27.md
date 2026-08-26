# DSD M5-69 — Optimal Completed-Square Pressure Payer

Date: 2026-08-27

Status: **SHARP ALGEBRAIC OPTIMIZATION / THE M5-68 COMPONENTWISE PRESSURE-VARIANCE LOWER BOUND ADMITS AN EXACT COMPLETED-SQUARE DECOMPOSITION / THE PREVIOUS `nu^2(A+G)+4nu X` ESTIMATE IS VALID BUT NONOPTIMAL / THE SHARP UNIVERSAL ENVELOPE IS `S_comp >= 4nu^2(A+G)+4nu X`, PLUS AN EXPLICIT NONNEGATIVE BALANCE-MISMATCH GAP / GLOBAL REGULARITY UNPROVED.**

## 1. Starting inequality

Use

\[
B:=A_w+G_w\ge0
\]

and

\[
T:=D_w-B
=D_w-A_w-G_w>0.
\]

M5-68 gives

\[
\boxed{
(\nu D_w+X_w)^2
\le
S_{comp,w}T.
}
\]

Since

\[
D_w=T+B,
\]

the numerator becomes

\[
\nu D_w+X_w
=
\nu T+(\nu B+X_w).
\]

Hence

\[
\boxed{
S_{comp,w}
\ge
\frac{[\nu T+(\nu B+X_w)]^2}{T}.
}
\]

On a positive upstroke,

\[
X_w\ge0,
\]

so

\[
\nu B+X_w\ge0.
\]

---

## 2. Exact completed-square identity

Let

\[
c:=\nu B+X_w.
\]

Then

\[
\frac{(\nu T+c)^2}{T}
=
\nu^2T+2\nu c+\frac{c^2}{T}.
\]

Use the identity

\[
\boxed{
\nu^2T+2\nu c+\frac{c^2}{T}
=
4\nu c
+
\frac{(\nu T-c)^2}{T}.
}
\]

Therefore

\[
\boxed{
S_{comp,w}
\ge
4\nu(\nu B+X_w)
+
\frac{[\nu T-(\nu B+X_w)]^2}{T}.
}
\]

Returning to the original variables,

\[
\boxed{
S_{comp,w}
\ge
4\nu^2(A_w+G_w)
+4\nu X_w
+H_w,
}
\]

where

\[
\boxed{
H_w
:=
\frac{
[\nu(D_w-A_w-G_w)
-\nu(A_w+G_w)-X_w]^2
}{D_w-A_w-G_w}
\ge0.
}
\]

Equivalently,

\[
\boxed{
H_w
=
\frac{
[\nu D_w
-2\nu(A_w+G_w)
-X_w]^2
}{D_w-A_w-G_w}.
}
\]

---

## 3. Sharp universal envelope

Dropping only the explicit nonnegative remainder gives

\[
\boxed{
S_{comp,w}
\ge
4\nu^2(A_w+G_w)
+4\nu X_w.
}
\]

This improves the valid but weaker M5-66/M5-68 estimate

\[
S_{comp,w}
\ge
\nu^2(A_w+G_w)+4\nu X_w.
\]

The coefficient of the bulk-plus-angular formation term is strengthened by a factor of four.

No additional analytic assumption is used; this is only the optimal algebraic use of the same Cauchy/ledger inequality.

---

## 4. Equality condition for the algebraic envelope

The completed-square remainder vanishes exactly when

\[
\nu T
=
\nu B+X_w.
\]

Thus

\[
\boxed{
D_w-A_w-G_w
=
A_w+G_w+rac{X_w}{\nu}.
}
\]

Equivalently,

\[
\boxed{
D_w
=
2(A_w+G_w)
+
\frac{X_w}{\nu}.
}
\]

Therefore a pump that uses the minimal possible componentwise pressure variance must realize a precise balance between:

- the pressure-accessible normal crossing amount `T`;
- the pressure-inaccessible formation amount `A+G`;
- and the positive entropy speed `X/nu`.

This is more restrictive than the approximate `D approximately X/nu` heuristic in M5-65, because the previously discarded formation contribution is now retained exactly.

---

## 5. Full near-saturation conditions

For the **original** M5-68 inequality to approach equality, two independent requirements must hold.

### A. Cauchy alignment

The centered pressure fluctuation must become proportional to the normalized amplitude-crossing velocity:

\[
\boxed{
P-m_{P,k}(a)
\approx
c(t)
\frac{U\cdot\nabla a}{a}
}
\]

throughout the weighted active region, with the componentwise centering understood on each superlevel component.

### B. Balance matching

The completed-square defect must be small:

\[
\boxed{H_w\approx0.}
\]

Thus near-minimal payment requires both a geometric pressure/flux alignment and the scalar balance

\[
D_w
\approx
2(A_w+G_w)+X_w/\nu.
\]

These conditions are independent of the mere largeness of pressure.

---

## 6. Robust recurrent lower bound

On the robust M5-57 returned upstroke,

\[
X_w\ge c_1>0.
\]

If the retained positive-excess class supplies

\[
A_w\ge A_{w,*}>0,
\]

then every returned pump satisfies

\[
\boxed{
S_{comp,w}
\ge
4\nu^2A_{w,*}
+4\nu c_1.
}
\]

If in addition either

\[
G_w\ge G_*>0
\]

or

\[
H_w\ge H_*>0,
\]

then the lower requirement is strengthened by the corresponding fixed normalized gap.

---

## 7. A three-gap rigidity decomposition

The direct pressure branch now contains three separate nonnegative structural obstructions:

\[
\boxed{
\begin{array}{rcl}
A_w&=&\text{active bulk-gradient formation},\\
G_w&=&\text{angular/transverse amplitude formation},\\
H_w&=&\text{normal-crossing/entropy-speed balance mismatch}.
\end{array}
}
\]

The pressure payer itself has already been reduced to

\[
S_{comp,w}
=
\text{componentwise internal pressure variance}.
\]

Hence a near-minimal survivor must simultaneously make the pressure fluctuation highly aligned while controlling all three formation/balance channels.

---

## 8. Scaling audit

Each instantaneous quantity

\[
S_{comp,w},
\quad A_w,
\quad G_w,
\quad X_w,
\quad H_w
\]

has scaling degree `+1` under the covariantly transported recurrent pump scaling.

Therefore the sharpened inequality is exactly scale covariant.

The improvement changes the **rigidity constant and equality structure**, not the event-budget exponent.

Thus it strengthens the direct structural branch but does not by itself solve the finite critical-budget obstruction of M5-63/M5-64.

---

## 9. DSD audit

### GREEN

M5-65 through M5-68 remain valid; their linear lower bound was simply not algebraically sharp in the formation term.

### GREEN

The factor-four formation coefficient follows from an exact completed-square identity.

### GREEN

The new remainder `H_w` is manifestly nonnegative and has a precise equality condition.

### YELLOW

A direct no-loop theorem may now be attacked by proving that recurrent pressure-Poisson geometry cannot make both the Cauchy-alignment defect and `H_w` arbitrarily small while retaining the positive pump.

---

## 10. New target

The most rigid possible survivor lies on the simultaneous endpoint

\[
\boxed{
\begin{array}{c}
P-m_{P,k}(a)
\propto
(U\cdot\nabla a)/a,\\
D_w
=
2(A_w+G_w)+X_w/\nu,\\
X_w>0,\\
A_w>0,
\end{array}
}
\]

inside the localized core plus finite-neighbor-shell pressure-Poisson system.

If this endpoint can be excluded, compactness yields a uniform strict gap from it on the recurrent pump class. That would be the next direct-rigidity gain.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
