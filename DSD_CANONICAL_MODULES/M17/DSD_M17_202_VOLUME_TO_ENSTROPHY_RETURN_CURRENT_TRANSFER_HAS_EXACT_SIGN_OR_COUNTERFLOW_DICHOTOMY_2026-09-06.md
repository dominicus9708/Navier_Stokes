# DSD M17-202 — Volume-to-enstrophy return-current transfer has an exact sign-or-counterflow dichotomy

Date: 2026-09-06  
Canonical ID: **M17-202**

Status: **MEASURE-TRANSFER DICHOTOMY / M17-201 FORCES A NEGATIVE VOLUME-WEIGHTED KAPPA RETURN CURRENT WHEN HIGH-KAPPA AMPLITUDE REPLENISHMENT IS PRESENT. ON A RETAINED POSITIVE-AMPLITUDE BAND `a <= rho <= M0`, WRITE THE POSITIVE/NEGATIVE PARTS OF `h` ON THE REGULAR `kappa=k0` LEVEL. IF THE ENSTROPHY-WEIGHTED CURRENT FAILS TO INHERIT A FIXED FRACTION OF THE NEGATIVE VOLUME CURRENT, THEN A FIXED POSITIVE AMOUNT OF OPPOSITELY DIRECTED `h>0` COUNTERFLOW MUST EXIST ON THE SAME KAPPA LEVEL. THUS THE VOLUME/ENSTROPHY MEASURE MISMATCH IS CONVERTED INTO AN EXPLICIT CROSSING-VELOCITY COUNTERFLOW, RATHER THAN AN UNSTRUCTURED SIGN ESCAPE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Regular return level

Fix a regular multiplier level

\[
\kappa=k_0
\]

inside a retained positive-amplitude region

\[
\boxed{a\le\rho\le M_0}
\]

with `a>0`.

Use the coarea measure

\[
\boxed{
d\nu:=\frac{dS}{|\nabla\kappa|}.
}
\]

Let the volume-weighted return current supplied by M17-201 be

\[
\boxed{
J_V:=\int h\,d\nu=-A<0.
}
\]

Thus `A>0` measures the required downward multiplier return.

---

## 2. Positive/negative crossing parts

Define

\[
H_+:=\int h_+d\nu,
\qquad
H_-:=\int (-h)_+d\nu.
\]

Then

\[
J_V=H_+-H_-=-A,
\]

so

\[
\boxed{H_-=H_++A.}
\]

---

## 3. Enstrophy-weighted current

The corresponding enstrophy current is

\[
\boxed{
J_E:=\int\rho^2h\,d\nu.
}
\]

Using

\[
a^2\le\rho^2\le M_0^2,
\]

we have

\[
\begin{aligned}
J_E
&=\int_{h>0}\rho^2h\,d\nu
-\int_{h<0}\rho^2(-h)\,d\nu\\
&\le M_0^2H_+-a^2H_-.
\end{aligned}
\]

Substitute `H_-=H_++A`:

\[
\boxed{
J_E
\le
(M_0^2-a^2)H_+-a^2A.
}
\]

---

## 4. Sign-or-counterflow dichotomy

Choose the fixed transfer target

\[
J_E\le-\frac{a^2}{2}A.
\]

If this holds, a definite fraction of the negative volume return is inherited by the enstrophy measure.

If it fails, then

\[
J_E>-\frac{a^2}{2}A.
\]

Using the upper bound above,

\[
(M_0^2-a^2)H_+-a^2A
>-\frac{a^2}{2}A,
\]

hence, for `M0>a`,

\[
\boxed{
H_+
>\frac{a^2}{2(M_0^2-a^2)}A.
}
\]

Therefore

\[
\boxed{
J_V=-A<0
\Longrightarrow
\left[
J_E\le-\frac{a^2}{2}A
\right]
\lor
\left[
H_+\ge c_{a,M_0}A
\right].
}
\]

If the amplitude is essentially constant on the level (`M0=a` in the ideal limit), the two measures are proportional and the sign transfers automatically.

---

## 5. Interpretation

The old measure firewall was

\[
\text{negative volume current need not imply negative enstrophy current}.
\]

The corrected form is sharper:

\[
\boxed{
\text{failure of sign transfer}
\Longrightarrow
\text{quantitative opposite-direction }h\text{ counterflow}.
}
\]

Thus the measure mismatch itself creates a new structured branch rather than arbitrary freedom.

---

## 6. Next gate

On a connected compact regular `kappa=k0` component, simultaneous negative net current and positive `h` counterflow force nontrivial spatial variation of `h`.

A weighted Poincare argument should therefore convert the counterflow branch into a positive tangential `|grad h|^2` occupancy, unless the positive and negative crossing populations live on disconnected components/interfaces.

---

## 7. DSD audit

- The result transfers only between volume and enstrophy measures on a fixed positive-amplitude band.
- It does not yet transfer to the transverse-flux measure.
- No sign is assigned to `h` pointwise.
- The constants deteriorate as the amplitude ratio `M0/a` becomes large; that degeneration is explicit rather than hidden.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
