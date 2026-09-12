# DSD M19-178 — One-sided vorticity growth gives a backward spike thickness, but mean normalization and recurrence do not by themselves bound the instantaneous occupation distortion

**Date:** 2026-09-13  
**Status:** ACTIVE M19 CALCULATION / ANTI-SPIKE NO-GO + EXACT ONE-SIDED THICKNESS / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-176--177 isolate the mean-to-instantaneous hard-frame occupation distortion `kappa_occ` as the cleanest new quantitative constant in the dimension-one criterion.

A natural idea is to control it from the scalar linearized-vorticity mass

\[
Z_v(s)=\|\eta_v(s)\|_2^2
\]

by combining a differential inequality with the Cesaro normalization

\[
\langle Z_v\rangle=1.
\]

The present module shows precisely what this gives and why it is not enough.

## 2. One-sided growth inequality

M19-177 gives

\[
\mathcal C_U[W]
\le
\frac\nu8P+B_3(s)Z,
\]

with

\[
Z=\|\eta\|_2^2,
\qquad
P=\|\nabla\eta\|_2^2,
\]

and

\[
B_3(s)
=
C\nu^{-1}\|S_U(s)\|_3^2
+C\|\nabla\Omega(s)\|_3.
\]

Let

\[
B_+:=\sup_s B_3(s)<\infty
\]

on the retained compact smooth corridor.

Insert the upper bound into

\[
\frac12Z'+\nu P+\frac14Z=\mathcal C_U[W].
\]

Then

\[
\frac12Z'
+\frac{7\nu}{8}P
+\left(\frac14-B_+\right)Z
\le0.
\]

Discard the nonnegative derivative term. Define

\[
\boxed{
L_+
:=
2\left(B_+-\frac14\right)_+.
}
\]

Then

\[
\boxed{
Z'(s)\le L_+Z(s).
}
\]

## 3. Backward thickness of a spike

For `r>=0`, integrate the inequality from `s-r` to `s`:

\[
\log Z(s)-\log Z(s-r)
\le
L_+r
\]

whenever `Z>0`.

Hence

\[
\boxed{
Z(s-r)
\ge
 e^{-L_+r}Z(s).
}
\]

Thus a high instantaneous value cannot have appeared from an arbitrarily small past value in arbitrarily short forward time.

A spike of height

\[
H:=Z(s)
\]

carries at least

\[
\int_{s-R}^{s}Z(t)dt
\ge
H\int_0^R e^{-L_+r}dr.
\]

For `L_+>0`,

\[
\boxed{
\int_{s-R}^{s}Z(t)dt
\ge
\frac{H}{L_+}
\left(1-e^{-L_+R}\right).
}
\]

Letting `R` be moderately larger than `L_+^{-1}` gives an order

\[
\boxed{H/L_+}
\]

minimum past mass associated with one high spike.

## 4. Why a global mean does not bound the spike height

Suppose the Cesaro mean is normalized:

\[
\boxed{
\langle Z\rangle=1.
}
\]

The previous estimate controls the **mass cost of each occurrence** of a spike, but it says nothing about how often such spikes must occur.

If a height-`H` event has frequency of order `H^{-1}`, its order-`H` mass cost per occurrence is still compatible with mean one.

Thus

\[
\boxed{
\text{minimum spike thickness}
+\text{mean one}
\not\Rightarrow
\sup Z\le C.
}
\]

This is the same multiplicity/frequency firewall that appeared earlier in the ancestry-return analysis.

## 5. Explicit scalar anti-model

Fix a growth ceiling `L_+>0`.
For large `H`, construct a periodic positive scalar function with long period `T_H` as follows.

During a growth interval, let

\[
z_H(t)=z_0e^{L_+t}
\]

until it reaches height `H`.

Its growth exactly saturates

\[
z_H'=L_+z_H.
\]

After the peak, allow a rapid decay; the differential inequality imposes no lower bound on `z_H'`.

Keep the function very small for the remainder of a period and choose

\[
T_H\asymp H/L_+
\]

so that the period average is normalized to one.

Then

\[
\boxed{
\langle z_H\rangle=1,
\qquad
z_H'\le L_+z_H,
\qquad
\sup z_H=H\to\infty.
}
\]

After smoothing the corners, the same conclusion holds for smooth positive periodic functions.

Therefore no universal anti-spike constant follows from the one-sided growth inequality and recurrence alone.

## 6. Compact recurrence is still insufficient quantitatively

For each fixed compact recurrent component, continuity gives a finite maximum of `Z`.

But compactness by itself does not provide a universal relation between that maximum and the invariant/Cesaro mean.

A continuous observable on a compact recurrent flow may be sharply concentrated on a very small-measure neighborhood.

Hence

\[
\boxed{
\text{compact recurrence}
+\langle Z\rangle=1
\not\Rightarrow
\sup Z\le C_{univ}.
}
\]

One would additionally need a quantitative lower bound on the invariant measure/frequency of neighborhoods of high `Z`, or a two-sided temporal regularity bound.

## 7. Ergodicity does not fix the issue

On an ergodic component, Birkhoff gives that the frequency of visiting a measurable spike set equals its invariant measure.

But ergodicity alone does not provide a lower bound on that measure in terms of the spike height.

Therefore

\[
\boxed{
\text{ergodicity}
\neq
\text{uniform quantitative recurrence}.
}
\]

This is another permanent firewall.

## 8. What would suffice

Any of the following would convert the one-sided thickness into a usable occupation bound:

1. **uniform return-frequency bound:** a lower density for visits to a neighborhood of every hard state;
2. **quantitative invariant-measure ball lower bound:**
   \[
   \mu(B_\delta(U))\ge m(\delta)>0;
   \]
3. **two-sided logarithmic derivative bound:**
   \[
   |Z'|\le LZ;
   \]
4. **sliding-window observability:**
   \[
   Z(s)\le C\frac1\tau\int_{s-\tau}^sZ(t)dt
   \]
   together with a normalization compatible with the hard trace identity.

The first two are genuine dynamical information not currently certified. The third would require an instantaneous derivative-frequency ceiling. The fourth is the most promising route because the one-sided growth inequality already gives half of it.

## 9. Sliding-window estimate from the one-sided bound

For every `tau>0`, the backward-thickness estimate gives

\[
\frac1\tau\int_{s-\tau}^{s}Z(t)dt
\ge
Z(s)
\frac{1-e^{-L_+\tau}}{L_+\tau}.
\]

Therefore

\[
\boxed{
Z(s)
\le
\frac{L_+\tau}{1-e^{-L_+\tau}}
\cdot
\frac1\tau
\int_{s-\tau}^{s}Z(t)dt.
}
\]

Define

\[
\boxed{
C_{win}(\tau)
:=
\frac{L_+\tau}{1-e^{-L_+\tau}}.
}
\]

Then

\[
C_{win}(\tau)\to1
\qquad
(\tau\downarrow0).
\]

This is an **explicit local-window occupation estimate**.

## 10. The new issue created by window normalization

If one normalizes the hard frame by the sliding-window vorticity metric instead of the invariant Cesaro metric, the metric depends on time.

Re-orthonormalizing a frame at each time introduces a connection/Gram-matrix derivative into the collective trace identity.

Therefore one cannot simply replace the Cesaro metric by the window metric and reuse M19-175 without extra terms.

The next problem is precisely to price those connection terms.

## 11. Audit verdict

### Proved

1. Exact one-sided logarithmic growth ceiling for hard-mode vorticity mass.
2. Exact backward spike-thickness estimate.
3. Explicit sliding-window occupation constant `C_win(tau)`.
4. Mean normalization, compact recurrence and ergodicity alone do not produce a universal instantaneous occupation bound.

### Closed shortcut

\[
\boxed{
\text{one-sided anti-spike}+
\text{global mean}
\not\Rightarrow
\kappa_{occ}\text{ explicit}.
}
\]

### New promising route

Use the explicit sliding-window metric and control the time-dependent Gram/connection correction.

## 12. Next target

M19-179 should define the sliding-window hard metric

\[
G_\tau(s)
:=
\frac1\tau
\int_{s-\tau}^{s}
\Phi_{t,s}^*\,
(\operatorname{curl})^*(\operatorname{curl})
\Phi_{t,s}\,dt
\]

on the current hard fiber.

It should compute the exact derivative of `G_tau(s)` and determine whether the induced connection term has zero long-time trace or an explicit `O(L_+ tau)` cost.

If that cost is controllable while `C_win(tau)` is close to one, the arbitrary occupation constant can be replaced by explicit PDE quantities.
