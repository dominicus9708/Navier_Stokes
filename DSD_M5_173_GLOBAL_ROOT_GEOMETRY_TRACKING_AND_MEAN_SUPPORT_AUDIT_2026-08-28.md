# DSD M5-173 — Global Root-Geometry Tracking and Mean–Support Audit

Date: 2026-08-28

Status: **P1_B^S PRINCIPAL GLOBALIZATION / THE M5-172 RICCATI TRACKING CAN BE EXTENDED MODEWISE TO THE FULL CROSS SPECTRUM USING THE EXACT GEOMETRY OF `sqrt D`; THE NONAUTONOMOUS STABLE-RATE ERROR IS GLOBALLY SUBORDINATE TO THE FROZEN PRINCIPAL DAMPING SYMBOL / HOWEVER THAT DAMPING SYMBOL IS NOT A FUNCTION OF THE SINGLE DIRICHLET FREQUENCY `A=1-4G^2-Delta_S2`, SO A GLOBAL `A`-COVARIANCE SIGN DOES NOT FOLLOW AUTOMATICALLY / THE MEAN-SUPPORT GAP IS NARROWED BUT NOT YET CLOSED / GLOBAL REGULARITY UNPROVED.**

---

## 1. Square-root geometry

Use the M5-167 discriminant

\[
D=d+iy
\]

and write its principal square root as

\[
\boxed{\sqrt D=u+iv,\qquad u>0.}
\]

For the actual three-dimensional spherical spectrum,

\[
d
=
(1+6\nu a)^2
-16\nu^2a^2c_\ell,
\qquad
c_\ell=2-\ell(\ell+1).
\]

The largest value of `c_ell` is `2`, so for sufficiently small `a`, in fact

\[
\boxed{d>1.}
\]

Since

\[
u^2-v^2=d,
\]

we obtain

\[
\boxed{u>1,\qquad |v|<u.}
\]

---

## 2. Exact damping-symbol form of the frozen slow root

M5-167 gives

\[
\lambda_s
=
i\omega
+
\frac{1+6\nu a-(u+iv)}{8\nu a}.
\]

The relation

\[
2uv=16\nu a\omega
\]

implies

\[
\omega=\frac{uv}{8\nu a}.
\]

Define

\[
\boxed{
\Gamma_a(\omega,\ell)
:=
\frac{u-1}{8\nu a}
\ge0.
}
\]

Then

\[
\operatorname{Re}\lambda_s
=
\frac34-\Gamma_a
\]

and

\[
\operatorname{Im}\lambda_s
=
\omega-\frac v{8\nu a}
=
\frac{v(u-1)}{8\nu a}
=v\Gamma_a.
\]

Hence the exact representation is

\[
\boxed{
\lambda_s
=
\left(\frac34-\Gamma_a\right)
+i v\Gamma_a.
}
\]

The common scalar `3/4` is a geometric similarity-growth term and cancels from normalized frequency quotients.

`Gamma_a` is the exact frozen principal damping symbol.

---

## 3. Global bound on slow-root variation

M5-172 proves

\[
(y_-)_\tau
=-\frac{\lambda_s}{\sqrt D}.
\]

Using the representation above,

\[
\frac{|\lambda_s|}{|\sqrt D|}
=
\frac{\sqrt{(3/4-\Gamma_a)^2+v^2\Gamma_a^2}}
{\sqrt{u^2+v^2}}.
\]

Since `u>1` and `|v|<u`, there is a viscosity-independent numerical constant `C` such that

\[
\boxed{
\left|
\frac{\lambda_s}{\sqrt D}
\right|
\le
C(1+\Gamma_a).
}
\]

Therefore

\[
\boxed{
|(y_-)_\tau|
\le C(1+\Gamma_a)
}
\]

for **all** cross frequencies, not merely inside a finite support corridor.

---

## 4. Global stable-root tracking

The deviation equation remains

\[
\delta_\tau
=
\Delta\delta-\delta^2-(y_-)_\tau,
\qquad
\Delta=rac{\sqrt D}{4\nu a}.
\]

Because `u>1`,

\[
\boxed{
\operatorname{Re}\Delta
\ge
\frac1{4\nu a}.
}
\]

Thus the flat-selected future kernel has mass `O(a)` uniformly over the entire spectrum.

Combining this with Section 3 and using the same small stable-branch bootstrap as M5-172 gives the global modewise estimate

\[
\boxed{
|\delta|
\le
C a(1+\Gamma_a).
}
\]

For very large `Gamma_a`, the ratio of the quadratic correction to the fast gap remains `O(a)`; the fast gap grows together with the principal damping, so the estimate does not break down at spectral infinity.

Hence

\[
\boxed{
\operatorname{Re}\frac{f_\tau}{f}
=
\frac34-\Gamma_a
+O\bigl(a(1+\Gamma_a)\bigr).
}
\]

For sufficiently small `a`, high-frequency modes therefore remain more strongly damped than the low common-growth channel.

---

## 5. What this resolves

The mean-support gap found after M5-172 cannot be blamed on a hidden nonautonomous fast-root instability at ultra-high frequency.

Even a tiny amount of spectral mass far above the parabolic support corridor has an exact stable principal rate subordinate to the frozen damping symbol.

Thus the remaining aggregation problem is not root tracking.

It is the relation between the damping symbol

\[
\Gamma_a(\omega,\ell)
\]

and the single Dirichlet frequency

\[
A
\simeq
1+4\omega^2+\ell(\ell+1).
\]

---

## 6. Why the `A` covariance sign is not automatic

M5-167 proves `Gamma_a` increases separately with `|omega|` and with `ell`.

However it is not an exact scalar function only of

\[
4\omega^2+\ell(\ell+1).
\]

Genealogical and angular frequency enter the square-root discriminant differently:

- angular frequency changes the real part `d`;
- genealogical frequency enters the imaginary part of `D`.

Therefore separate coordinatewise monotonicity does not by itself prove

\[
\operatorname{Cov}(A,\Gamma_a)\ge0
\]

for an arbitrary joint spectral measure.

A correlation between genealogical and angular spectral variables can obstruct a naive one-dimensional Chebyshev argument.

Thus the implication

\[
\boxed{
\text{modewise damping monotonicity}
\not\Rightarrow
\text{automatic global }A\text{-quotient monotonicity}
}
\]

is now an explicit DSD firewall.

---

## 7. Two legitimate remaining aggregation routes

The principal-lag problem is now reduced to one of two structures.

### Route A — variance-aware spectral split

Split the spectral measure into:

- a moderate region where `a A` is finite and M5-172 gives quantitative tracking;
- high-frequency dust, whose distance from the mean produces a large positive spectral variance

\[
\frac{\|(A-\mathcal N)F\|^2}{\|F\|^2}.
\]

Then absorb all first-order and tracking errors against that variance.

### Route B — use the exact damping observable

Replace the auxiliary Dirichlet frequency `A` by an observable built from the exact principal damping symbol `Gamma_a` and derive the corresponding log-convexity/transfer inequality directly.

Either route avoids `mean -> support` promotion.

---

## 8. External backward-uniqueness route remains separate

Classical backward-uniqueness results for parabolic equations with lower-order terms, including the Escauriaza–Seregin–Sverak framework, provide an external comparison point.

They are **not** inserted here as a proof of the flat-fiber result because the present same-tail relative equation contains a critical common background and the exact Stokes/vorticity hypothesis match has not yet been completed.

No theorem is cited as closing `P1_B^S` without that hypothesis audit.

---

## 9. DSD audit

### Formation — GREEN

The damping symbol is formed directly from the actual principal root.

### Axis — GREEN

Genealogical and angular frequencies remain separate coordinates until a justified aggregate observable is chosen.

### Static aggregation — GREEN

No separate-coordinate monotonicity is converted into a one-dimensional covariance sign without proof.

### Dynamics — GREEN modewise / YELLOW aggregate

Global modewise stable tracking is GREEN.  Aggregate flat-fiber uniqueness remains YELLOW.

### Cross-audit — GREEN

The M5-172 mean-support overreach remains corrected.

---

## 10. Updated frontier

The nonautonomous principal lag is no longer the main uncertainty.

The next calculation is now:

\[
\boxed{
\text{close the aggregate spectral step by either}
\quad
\text{variance-aware splitting}
\quad\text{or}\quad
\Gamma_a\text{-based log convexity}.
}
\]

Only after that can M5-171 be invoked to close `P1_B^S`.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
