# DSD M5-57 — Mollified Pump Crossing and Syndetic Inheritance

Date: 2026-08-27

Status: **DERIVED RECURRENCE TRANSFER / A GENUINE POSITIVE THRESHOLD PUMP MAKES A SUFFICIENTLY NARROW AMPLITUDE-MOLLIFIED ENTROPY NONCONSTANT / ONE MAY SELECT A TEMPORALLY TRANSVERSE UPWARD CROSSING / LOCAL SMOOTH W1 RECURRENCE REPRODUCES THAT CROSSING ON SYNDETIC RETURN SEGMENTS / GLOBAL REGULARITY UNPROVED.**

## 1. Anchor first-hit data

Let `lambda_c` be the normalized threshold used in the retained positive-defect first-hit class.

By definition of a genuine positive first hit, there are times

\[
t_-<t_c
\]

and a positive level `kappa_c` such that

\[
E_{\lambda_c}(t_-)<\kappa_c,
\qquad
E_{\lambda_c}(t_c)=\kappa_c.
\]

Hence the threshold observable is not constant on the anchor pump segment.

In particular

\[
\Delta E_c
:=
E_{\lambda_c}(t_c)-E_{\lambda_c}(t_-)>0.
\]

---

## 2. Narrow amplitude mollification preserves nonconstancy

Choose a standard nonnegative smooth approximate identity in the amplitude variable,

\[
w_\delta(\lambda)
=
\delta^{-1}w_0\!\left(
\frac{\lambda-\lambda_c}{\delta}
\right),
\]

with compact support near `lambda_c` and unit mass.

Define

\[
\bar E_\delta(t)
:=
\int w_\delta(\lambda)E_\lambda(t)d\lambda.
\]

The threshold entropy itself is a volume integral of the positive-part excess and is continuous in `lambda` on the fixed W1 phase cell. It does not contain the singular level-surface factor `1/|grad a|` that appeared in `Q_P'`.

Therefore, on the compact anchor time segment `[t_-,t_c]`,

\[
\bar E_\delta(t)
\to
E_{\lambda_c}(t)
\]

uniformly as `delta -> 0`.

Choose one fixed sufficiently small normalized `delta=delta_*` so that

\[
\bar E_{\delta_*}(t_c)
-
\bar E_{\delta_*}(t_-)
\ge
\frac12\Delta E_c>0.
\]

Thus the amplitude-mollified observable is genuinely nonconstant.

The width `delta_*` is fixed in normalized W1 units and is therefore scale-independent under the terminal-centered recurrence.

---

## 3. A transverse upward crossing exists

The retained pump segment is smooth before the terminal point, so

\[
t\mapsto \bar E_{\delta_*}(t)
\]

is continuously differentiable on the compact anchor segment.

Since its endpoint difference is positive, the mean value theorem gives a time `t_0` such that

\[
\boxed{
\partial_t\bar E_{\delta_*}(t_0)>0.
}
\]

By continuity there exist constants

\[
\tau_*>0,
\qquad
c_t>0
\]

such that on a smaller interval

\[
I_0=[t_0-\tau_*,t_0+\tau_*]
\]

we have

\[
\boxed{
\partial_t\bar E_{\delta_*}(t)
\ge c_t>0.
}
\]

Choose

\[
\kappa_*:=\bar E_{\delta_*}(t_0).
\]

The anchor pump therefore contains a robust upward crossing of the fixed mollified observable.

This is stronger than the weak first-hit sign `partial_t E >= 0` at one instant.

---

## 4. Pressure consequence on the anchor crossing interval

M5-56 gives the exact averaged ledger

\[
\partial_t\bar E_w
+
\nu\bar D_w
=
\bar J_w.
\]

Hence throughout `I_0`,

\[
\boxed{
\bar J_w
\ge
\nu\bar D_w+c_t.
}
\]

Thus the pressure flux strictly overpays the averaged viscous term on an interval of positive normalized time width, not merely at an isolated instant.

The M5-56 weighted Cauchy inequality then forces the finite-band volume pressure payer

\[
\bar S_w
=
\int |U|w(|U|)|P|^2dy
\]

to remain quantitatively positive throughout a possibly smaller crossing interval.

---

## 5. Transfer under W1 recurrence

M5-44 identifies terminal-centered scale recurrence of the physical ancient-to-terminal cell with time translation of the compact W1 ancestor.

The retained recurrence is locally smooth on compact spacetime subsets before the terminal time.

The amplitude-mollified quantities in M5-56 are supported in the fixed active phase cell because the weight is centered at a positive normalized amplitude and the `1/r` tail eventually lies below that band.

Therefore local smooth convergence of a returned W1 segment implies convergence of

\[
\bar E_w,
\qquad
\partial_t\bar E_w,
\qquad
\bar D_w,
\qquad
\bar J_w,
\qquad
\bar S_w
\]

on the corresponding compact pump segment.

For all sufficiently accurate returns, the returned segment therefore inherits, after a small time shift if necessary,

\[
\boxed{
\partial_t\bar E_w
\ge
\frac12c_t>0
}
\]

on an interval of width bounded below by a fixed positive fraction of `tau_*`.

---

## 6. Minimality makes the robust crossings syndetic

M5-52 upgraded recurrence to syndetic recurrence because the W1 orbit lies in a compact minimal invariant set.

Take a sufficiently small neighborhood of the anchor pump state/segment for which the transverse crossing survives.

Returns to that neighborhood have uniformly bounded gaps in Leray time.

Consequently there is a sequence of crossing intervals `I_n` such that

\[
\sup_n
\operatorname{gap}(I_n,I_{n+1})
<\infty,
\]

while

\[
|I_n|
\ge \tau_1>0
\]

and

\[
\partial_t\bar E_w
\ge c_1>0
\quad\text{on }I_n
\]

for uniform normalized constants `tau_1,c_1`.

After passing to a disjoint subfamily if necessary, these intervals have positive lower time density.

Thus the finite-band pressure overpay from M5-56 is not merely recurrent at isolated times; it occurs on positive-density W1 time intervals.

---

## 7. Translation back to the terminal Zeno ladder

Under the M5-44/M5-47 inverse-Leray map, the syndetic W1 crossing intervals become nested terminal-centered pump intervals whose physical durations shrink parabolically.

Their normalized geometry and amplitude-band width remain fixed, while their physical scales tend to zero.

Thus the same finite-band pressure-payer geometry is reproduced at arbitrarily small physical scales near the terminal point.

This strengthens the same-trajectory multiscale statement:

\[
\boxed{
\text{the recurrent survivor must reproduce a robust finite-band pressure pump, not only a pointwise threshold event.}
}
\]

---

## 8. DSD audit

### GREEN

A genuine positive first hit makes the central threshold observable nonconstant.

### GREEN

Amplitude mollification approximates that entropy uniformly on the compact anchor segment and therefore preserves nonconstancy for sufficiently small fixed normalized width.

### GREEN

A nonconstant smooth pump segment contains a temporally transverse upward interval.

### GREEN

Local smooth recurrence transports the interval property, and minimality makes the return family syndetic.

### YELLOW

Positive-density strict pressure overpay is still not automatically a contradiction. The exact averaged entropy ledger may allow compensating downward intervals elsewhere on the recurrent orbit.

This compensation must be audited before treating the repeated positive intervals as a monotone defect.

---

## 9. Next proof gate

The next calculation is to integrate the averaged ledger over long W1 times and determine whether

\[
\bar J_w-\nu\bar D_w
\]

is a genuinely accumulating signed defect or merely the exact derivative of the bounded recurrent observable `bar E_w`.

If it telescopes, the natural first-order pressure-overpay branch is closed and one must seek a non-exact loop/cocycle or a one-sided obstruction to the compensating downstroke.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
