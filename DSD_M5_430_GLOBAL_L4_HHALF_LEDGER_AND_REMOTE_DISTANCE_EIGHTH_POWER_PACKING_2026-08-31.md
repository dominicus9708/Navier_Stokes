# DSD M5-430 — Global `L^4_t dot H^{1/2}` ledger and eighth-power remote-distance packing

Date: 2026-08-31

Status: **FIRST GLOBALLY LERAY-CONTROLLED CRITICAL-THROUGHPUT LEDGER IN THE LATE FRONTIER / ENERGY INTERPOLATION GIVES `u in L^4_t dot H^{1/2}` ON EVERY FINITE LERAY INTERVAL / COMBINING THIS WITH THE M5-421/M5-423 QUARTIC CRITICAL-MASS PRICE FOR A REMOTE SOURCE AND THE M5-418 POSITIVE NATURAL-TIME PERSISTENCE GIVES THE NON-DOUBLE-COUNTING SUM `sum r_j^2 L_j^8 < infinity` FOR PERSISTENT FIXED-FRACTION REMOTE SOURCE EVENTS / CONSEQUENTLY AN INFINITE PERSISTENT SOURCE SEQUENCE MUST SATISFY `L_j=o(r_j^{-1/4})`, EQUIVALENTLY PHYSICAL SOURCE DISTANCE `d_j=o(r_j^{3/4})` / THIS EXCLUDES A LARGE RANGE OF STRONG DELOCALIZATION RATES BUT NOT ALL CRITICAL CONCENTRATION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Critical norm

Define

\[
\boxed{
X(t)
:=
\|u(t)\|_{\dot H^{1/2}}^2
=
\|\omega(t)\|_{\dot H^{-1/2}}^2.
}
\]

M5-415 correctly notes that `X(t)` itself may diverge at a hypothetical singular time.

The new observation is that its **square is time-integrable at the Leray energy level**.

---

## 2. Energy interpolation

By homogeneous Sobolev interpolation between `L2` and `dot H1`,

\[
\|u\|_{\dot H^{1/2}}
\le
\|u\|_2^{1/2}
\|u\|_{\dot H^1}^{1/2}.
\]

Since for divergence-free whole-space velocity

\[
\|u\|_{\dot H^1}
=\|\nabla u\|_2
=\|\omega\|_2,
\]

we get

\[
\boxed{
X(t)
\le
\|u(t)\|_2\,\|\omega(t)\|_2.
}
\]

Squaring,

\[
\boxed{
X(t)^2
\le
\|u(t)\|_2^2\,\|\omega(t)\|_2^2.
}
\]

---

## 3. Global `L4_t dot H1/2` bound

Let

\[
E_0:=\|u_0\|_2^2.
\]

The Leray energy inequality gives

\[
\sup_{t<T_*}\|u(t)\|_2^2
\le E_0
\]

and

\[
\nu\int_0^{T_*}\|\omega(t)\|_2^2dt
\le C_EE_0
\]

with a harmless convention-dependent constant `C_E`.

Therefore

\[
\begin{aligned}
\int_0^{T_*}X(t)^2dt
&\le
E_0
\int_0^{T_*}\|\omega(t)\|_2^2dt\\
&\le
C_E\frac{E_0^2}{\nu}.
\end{aligned}
\]

Thus

\[
\boxed{
\int_0^{T_*}
\|u(t)\|_{\dot H^{1/2}}^4dt
\le
C_E\frac{E_0^2}{\nu}
<\infty.
}
\]

This is a genuine globally controlled spacetime quantity.

It does not imply `sup_t X(t)<infinity`.

---

## 4. Persistent remote-source event

At first-hitting stage `j`, let

\[
r_j=\sqrt{\nu/W_j}.
\]

Suppose a fixed fraction of the target natural strain is supplied, throughout a retained normalized time interval of length at least

\[
\delta\tau_*>0,
\]

by source content whose characteristic normalized distance from the target is at least

\[
L_j\ge1.
\]

M5-421/M5-423 give the critical duality price

\[
\boxed{
X(t)^{1/2}
\gtrsim
\nu L_j^2
}
\]

throughout that persistent source interval, after fixing the source fraction in the constants.

Hence

\[
\boxed{
X(t)
\gtrsim
\nu^2L_j^4.
}
\]

---

## 5. Convert normalized persistence to physical time

Use the first-hitting parabolic clock

\[
\tau
=\frac{\nu(t-t_j)}{r_j^2}.
\]

A normalized interval of length `delta tau_*` has physical length

\[
\boxed{
|J_j^{phys}|
\ge
c_\tau\frac{r_j^2}{\nu}.
}
\]

The stage intervals are disjoint in physical time, so selected subintervals `J_j^{phys}` are disjoint as well.

---

## 6. Eighth-power stage charge

On `J_j^{phys}`,

\[
X(t)^2
\gtrsim
\nu^4L_j^8.
\]

Therefore

\[
\begin{aligned}
\int_{J_j^{phys}}X(t)^2dt
&\gtrsim
\nu^4L_j^8
\frac{r_j^2}{\nu}\\
&=
\boxed{
 c\nu^3r_j^2L_j^8.
}
\end{aligned}
\]

Summing over disjoint persistent remote-source stages and using Section 3 gives

\[
\boxed{
\sum_j
r_j^2L_j^8
\le
C
\frac{E_0^2}{\nu^4}
<\infty.
}
\]

This is the desired globally controlled, non-double-counting remote-distance ledger.

---

## 7. Consequence for asymptotic remote distance

Since the summands are nonnegative,

\[
\boxed{
r_j^2L_j^8\to0.}
\]

Equivalently,

\[
\boxed{
r_j^{1/4}L_j\to0.}
\]

Thus every infinite sequence of persistent fixed-fraction remote-source events must satisfy

\[
\boxed{
L_j=o(r_j^{-1/4}).
}
\]

If the physical source distance is

\[
d_j=r_jL_j,
\]

then

\[
\boxed{
d_j=o(r_j^{3/4}).}
\]

So the source may be remote in **normalized** natural units, but its physical distance must still collapse to the singular point faster than `r_j^(3/4)` on every infinite persistent sequence covered by this ledger.

---

## 8. Power-law test

Suppose schematically

\[
L_j\asymp r_j^{-\beta}.
\]

Then one stage contributes

\[
r_j^2L_j^8
\asymp
r_j^{2-8\beta}.
\]

Because `r_j` decreases geometrically:

- if `beta<1/4`, the geometric series may converge;
- if `beta=1/4`, the terms remain order one and infinitely many such events are impossible;
- if `beta>1/4`, the terms grow and even more strongly violate the global ledger.

Thus

\[
\boxed{
\beta\ge\frac14
}
\]

is excluded for an infinite persistent fixed-fraction remote-source corridor.

---

## 9. Relation to M5-423 visibility radius

M5-423 gives

\[
L_{eff}\asymp
\left(\frac{X}{\nu^2}\right)^{1/4}
\]

for fixed source fraction.

The present theorem shows that a source actually living near this maximal critical visibility radius for a fixed natural-time fraction cannot do so at the rate

\[
L_{eff}\gtrsim r^{-1/4}
\]

infinitely often.

Thus the global Leray energy does constrain the growth of the critical visibility window once persistence is used.

---

## 10. Relation to the old summable one-stage costs

Earlier one-stage physical energy/enstrophy costs often scaled like

\[
r_j
\quad\text{or}\quad
r_j^2
\]

and were therefore summable with no contradiction.

The present ledger gains the factor

\[
L_j^8
\]

from two ingredients:

1. remote strain coupling requires critical norm `X ~ L^4`;
2. the globally controlled quantity is `X^2` in time.

This is why sufficiently rapid delocalization becomes non-summable even though a local natural packet alone remains cheap in Leray energy.

---

## 11. Scope firewall

The theorem requires a **persistent fixed-fraction remote source** for a fixed normalized time.

An instantaneous or rapidly changing source is not automatically covered; M5-428--429 route such behavior to strong strain and an exponential critical-mass price, but its duration must be included before using the global `L4_t dot H1/2` ledger.

The theorem also does not exclude slower normalized delocalization such as

\[
L_j=r_j^{-0.1}.
\]

The weighted series may still converge.

Therefore the full strong/delocalized branch is not closed.

---

## 12. Audit verdict

### GLOBALLY CONTROLLED LEDGER

\[
\boxed{
\int_0^{T_*}\|u\|_{\dot H^{1/2}}^4dt<\infty.
}
\]

### PERSISTENT REMOTE PACKING

\[
\boxed{
\sum_jr_j^2L_j^8<\infty.
}
\]

### ASYMPTOTIC LOCALIZATION

\[
\boxed{
L_j=o(r_j^{-1/4}),
\qquad
d_j=o(r_j^{3/4}).
}
\]

for every infinite persistent fixed-fraction remote-source sequence in scope.

### STILL OPEN

Slower critical delocalization, diffuse state novelty inside the allowed rate, and the final global regularity problem.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
