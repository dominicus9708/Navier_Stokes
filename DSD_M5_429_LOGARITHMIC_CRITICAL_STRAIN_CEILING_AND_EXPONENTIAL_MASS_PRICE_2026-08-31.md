# DSD M5-429 — Logarithmic critical-strain ceiling and exponential critical-mass price

Date: 2026-08-31

Status: **QUANTITATIVE STRONG-THROUGHPUT BRIDGE / COMBINING FIRST-HITTING VORTICITY LIPSCHITZ CONTROL, THE AMPLITUDE CAP, AND THE M5-423 FAR-FIELD `dot H^{-1/2}` DUALITY GIVES A LOGARITHMIC UPPER BOUND FOR PARENT-NORMALIZED POINTWISE STRAIN IN TERMS OF THE GLOBAL CRITICAL NORM / CONSEQUENTLY A LARGE NORMALIZED STRAIN `B` REQUIRES CRITICAL MASS AT LEAST EXPONENTIAL IN `B` / FAST ORDER-ONE INTERFACE CHANGE OVER NORMALIZED TIME `delta tau` THEREFORE REQUIRES AN EXPONENTIAL-IN-`1/delta tau` CRITICAL-NORM ESCALATION UNLESS IT FALLS BACK TO THE NATURAL-TIME RECURRENT CORRIDOR / THIS IS A COST LAW, NOT A GLOBAL CONTRADICTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Setup

At a late first-hitting stage, normalize by the target natural scale `r` so that

\[
|\Omega|\le q,
\qquad
|\Omega(0)|=1.
\]

Let

\[
X(t)=\|u(t)\|_{\dot H^{1/2}}^2
=
\|\omega(t)\|_{\dot H^{-1/2}}^2.
\]

Because

\[
\omega(x,t)
=\frac{\nu}{r^2}\Omega\!\left(\frac{x-X_*}{r},\tau\right),
\]

critical scaling gives

\[
\boxed{
\|\Omega\|_{\dot H^{-1/2}}
=
\frac{X(t)^{1/2}}{\nu}.
}
\]

Set

\[
M:=\frac{X^{1/2}}{\nu}.
\]

---

## 2. Near/middle/far strain split

Write the normalized strain at the target using the Calderon--Zygmund kernel

\[
\Sigma(0)
=
\operatorname{p.v.}
\int K(Y)\Omega(Y)dY,
\qquad
|K(Y)|\lesssim |Y|^{-3}.
\]

For `R>=2`, split

\[
\Sigma
=
\Sigma_{near}
+\Sigma_{mid}
+\Sigma_{far}
\]

with

\[
|Y|<1,
\qquad
1<|Y|<R,
\qquad
|Y|>R.
\]

---

## 3. Near field from stage-wide analyticity

The Calderon--Zygmund kernel has zero spherical mean.

Hence the local principal value can be written using the vorticity increment

\[
\Omega(Y)-\Omega(0).
\]

M5-392 gives

\[
\|\nabla\Omega\|_\infty\le C_1.
\]

Therefore

\[
|\Omega(Y)-\Omega(0)|
\le C_1|Y|,
\]

and

\[
\begin{aligned}
|\Sigma_{near}|
&\lesssim
\int_{|Y|<1}
|Y|^{-3}C_1|Y|dY\\
&\lesssim C_1.
\end{aligned}
\]

Thus

\[
\boxed{|\Sigma_{near}|\le C_{near}.}
\]

---

## 4. Middle field gives the logarithm

On the middle annulus the first-hitting amplitude cap gives

\[
|\Omega|\le q.
\]

Hence

\[
\begin{aligned}
|\Sigma_{mid}|
&\lesssim
q\int_1^R\frac{dr}{r}\\
&=q\log R.
\end{aligned}
\]

Therefore

\[
\boxed{|\Sigma_{mid}|\le C_{mid}q\log R.}
\]

No sign or angular cancellation is used here; this is a robust upper bound.

---

## 5. Far field from M5-423 critical duality

M5-423 proves for the complete exterior kernel

\[
\boxed{
|\Sigma_{far}|
\lesssim
R^{-2}
\|\Omega\|_{\dot H^{-1/2}}.
}
\]

Thus

\[
\boxed{
|\Sigma_{far}|
\le
C_{far}MR^{-2}.
}
\]

---

## 6. Optimize the splitting radius

Combining the three regions,

\[
\boxed{
\|\Sigma\|_\infty
\le
C_0
+C_1' q\log R
+C_2' M R^{-2}.
}
\]

For `M` above a fixed constant, choose

\[
R^2\asymp\frac{M}{q}
\]

(up to harmless universal constants).

Then the far contribution is `O(q)` and

\[
\log R
=\frac12\log M+O_q(1).
\]

For bounded `M`, simply take `R=2`.

Therefore there are fixed constants depending only on the first-hitting ratio and analytic normalization such that

\[
\boxed{
\|\Sigma\|_\infty
\le
C_*
\left[
1+
\log\left(2+\frac{X^{1/2}}{\nu}\right)
\right].
}
\]

This is the parent-normalized logarithmic critical-strain ceiling.

---

## 7. Invert the estimate: large strain requires exponential critical mass

Suppose

\[
\|\Sigma\|_\infty\ge B
\]

with `B` larger than the fixed baseline constant.

Then

\[
B/C_*-1
\le
\log\left(2+\frac{X^{1/2}}{\nu}\right).
\]

Hence

\[
\boxed{
\frac{X^{1/2}}{\nu}
\ge
c\exp(cB)-2
}
\]

and therefore, after adjusting constants,

\[
\boxed{
X
\ge
c\nu^2\exp(cB).
}
\]

(The exponent constant absorbs the harmless factor two from squaring.)

Thus pointwise normalized strain escalation has an exponential critical-mass price under the first-hitting analytic/amplitude corridor.

---

## 8. Fast-interface consequence

M5-428 shows that an order-one change of active vorticity/source state in normalized time `delta tau` requires

\[
B
\gtrsim
\frac{c}{\delta\tau}-C
\]

unless the transition occurs on a fixed natural-time interval through the bounded-strain corridor.

Insert this into the exponential mass price.

For sufficiently small `delta tau`, a genuinely fast interface requires

\[
\boxed{
X
\gtrsim
\nu^2
\exp\left(\frac{c}{\delta\tau}\right).
}
\]

Thus a sequence of faster and faster interface collapses cannot remain a modest critical-norm perturbation.

It is automatically a very strong `C_strong/deloc mass` event.

---

## 9. Relation to the old CZ logarithmic middle term

M5-371 identified the logarithmic middle Calderon--Zygmund range as a possible source of large strain but correctly did not treat the logarithm itself as a contradiction.

The present note adds the critical far-field closure:

- extending the middle range to radius `R` costs `log R`;
- hiding the remaining exterior field beyond `R` requires the `dot H^{-1/2}` mass measured by M5-423;
- optimizing the two gives a logarithm of the global critical norm.

Thus the former qualitative nonlocal-strain branch now has an explicit critical-mass efficiency law.

---

## 10. Firewall

This estimate does not bound `X(t)` from above.

A hypothetical singularity is allowed to satisfy

\[
X(t)\to\infty.
\]

Therefore

\[
\text{large strain}
\Rightarrow
\text{exponentially large critical mass}
\]

is a quantitative routing theorem, not a contradiction.

Do not combine it with the small-data `dot H^{1/2}` estimate after `X` has become large.

---

## 11. Updated strong-throughput interpretation

The strong branch can now be divided by rate:

### Natural-rate transition

Bounded `Sigma` permits only fixed-speed source/axis/flux evolution. This returns to the recurrent/handoff compactness analysis.

### Faster-than-natural transition

The required strain grows like `1/delta tau`, and therefore

\[
\boxed{
X
\gtrsim
\nu^2e^{c/\delta\tau}.
}

This belongs to explicit strong/delocalized critical-mass escalation.

Hence there is no separate cheap fast-interface route.

---

## 12. Audit verdict

### DERIVED

\[
\boxed{
\|\Sigma\|_\infty
\lesssim
1+\log\left(2+X^{1/2}/\nu\right).
}
\]

### CONSEQUENCE

\[
\boxed{
\|\Sigma\|_\infty\ge B
\Longrightarrow
X\gtrsim\nu^2e^{cB}.
}
\]

### FAST INTERFACE

\[
\boxed{
\delta\tau\to0
\Longrightarrow
X\gtrsim\nu^2e^{c/\delta\tau}.
}
\]

### STILL OPEN

Excluding the allowed strong critical-mass divergence itself.

### STATUS

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
