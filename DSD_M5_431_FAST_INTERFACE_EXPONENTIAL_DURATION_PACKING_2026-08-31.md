# DSD M5-431 — Fast-interface exponential duration packing from the global critical ledger

Date: 2026-08-31

Status: **GLOBAL TIME-PACKING UPGRADE / AN ORDER-ONE ACTIVE SOURCE OR AXIS CHANGE OVER NORMALIZED DURATION `delta_j` REQUIRES ORDER-ONE INTEGRATED STRAIN ACTION / THE M5-429 LOGARITHMIC STRAIN CEILING CONVERTS THIS INTO AN EXPONENTIAL LOWER BOUND FOR THE `L^4` CRITICAL MASS USED DURING THE TRANSITION / COMBINED WITH THE M5-430 GLOBAL `L^4_t dot H^{1/2}` BOUND, DISJOINT FIRST-HITTING INTERFACES OBEY `sum r_j^2 delta_j exp(c/delta_j) < infinity` / HENCE INTERFACE DURATIONS CANNOT COLLAPSE FASTER THAN A LOGARITHMIC-IN-SCALE RATE ALONG AN INFINITE CORRIDOR / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Setup

Let stage `j` have natural scale

\[
r_j=\sqrt{\nu/W_j}.
\]

Suppose an order-one source/axis/active-state transition occurs on a normalized time interval

\[
J_j=[\tau_j^-,\tau_j^+]
\]

of length

\[
\boxed{\delta_j:=|J_j|.}
\]

The corresponding physical interval has length

\[
|J_j^{phys}|
=\frac{r_j^2}{\nu}\delta_j.
\]

Selected interface intervals from distinct first-hitting stages are disjoint in physical time.

---

## 2. Order-one state change requires integrated strain action

On the active carrier, M5-428 gives

\[
|D_\tau\Omega|
\lesssim
q\|\Sigma\|_\infty+C_2
\]

and

\[
|D_\tau\xi|
\lesssim
\|\Sigma\|_\infty+C_2/\lambda_0.
\]

Therefore, if the interface changes amplitude or direction by a fixed amount `delta_* >0`, then

\[
\delta_*
\le
C\int_{J_j}
\left(1+\|\Sigma(\tau)\|_\infty\right)d\tau.
\]

For sufficiently small `delta_j` the constant term cannot pay the whole change, so

\[
\boxed{
\int_{J_j}\|\Sigma(\tau)\|_\infty d\tau
\ge c_*>0.
}
\]

For non-small `delta_j`, the desired lower-rate conclusion is already trivial after changing constants.

---

## 3. Insert the logarithmic critical-strain ceiling

M5-429 gives

\[
\|\Sigma(\tau)\|_\infty
\le
C_0+C_1\log\left(2+M(\tau)\right),
\]

where

\[
\boxed{
M(\tau)
:=
\frac{X(\tau)^{1/2}}{\nu},
\qquad
X=\|u\|_{\dot H^{1/2}}^2.
}
\]

After shrinking the universal small-duration threshold if needed,

\[
\boxed{
\int_{J_j}
\log(2+M(\tau))d\tau
\ge c_1>0.
}
\]

---

## 4. Jensen converts logarithmic action into exponential average critical mass

Since `log` is concave,

\[
\frac1{\delta_j}
\int_{J_j}\log(2+M)d\tau
\le
\log\left(
2+
\frac1{\delta_j}\int_{J_j}M d\tau
\right).
\]

The lower bound from Section 3 therefore implies

\[
\log\left(
2+\langle M\rangle_{J_j}
\right)
\ge
\frac{c_1}{\delta_j}.
\]

Hence, for small `delta_j`,

\[
\boxed{
\langle M\rangle_{J_j}
\ge
c\exp(c/\delta_j).
}
\]

---

## 5. Upgrade to the fourth power

By Holder/Jensen,

\[
\frac1{\delta_j}
\int_{J_j}M^4d\tau
\ge
\left(
\frac1{\delta_j}
\int_{J_j}M d\tau
\right)^4.
\]

Therefore

\[
\boxed{
\int_{J_j}M^4d\tau
\ge
c\delta_j
\exp(c/\delta_j).
}
\]

The constant in the exponent has absorbed the factor four.

---

## 6. Return to physical `X^2 dt`

Because

\[
X^2
=\nu^4M^4
\]

and

\[
dt=\frac{r_j^2}{\nu}d\tau,
\]

we obtain

\[
\begin{aligned}
\int_{J_j^{phys}}X(t)^2dt
&=
\nu^3r_j^2
\int_{J_j}M^4d\tau\\
&\ge
\boxed{
 c\nu^3r_j^2
\delta_j
\exp(c/\delta_j).
}
\end{aligned}
\]

---

## 7. Global exponential duration packing

M5-430 proves

\[
\int_0^{T_*}X(t)^2dt
\le
C_E\frac{E_0^2}{\nu}.
\]

Summing the disjoint interface intervals gives

\[
\boxed{
\sum_j
r_j^2
\delta_j
\exp(c/\delta_j)
\le
C
\frac{E_0^2}{\nu^4}
<\infty.
}
\]

This is a globally controlled rate ledger for fast interface events.

---

## 8. Consequence: no super-logarithmically fast infinite corridor

Since every summand must tend to zero,

\[
r_j^2\delta_j e^{c/\delta_j}\to0.
\]

Taking logarithms schematically,

\[
\frac{c}{\delta_j}
\lesssim
2|\log r_j|+|\log\delta_j|+o(|\log r_j|).
\]

Therefore an infinite corridor cannot satisfy

\[
\delta_j|\log r_j|\to0.
\]

More quantitatively, after adjusting constants, any persistent infinite fast-interface sequence must obey a lower rate of the form

\[
\boxed{
\delta_j
\gtrsim
\frac{c}{1+|\log r_j|}
}
\]

along all sufficiently late events in the quantified corridor.

The exact numerical constant is not claimed sharp.

---

## 9. Power/log tests

### Power-fast interface

If

\[
\delta_j\asymp r_j^\alpha,
\qquad\alpha>0,
\]

then

\[
e^{c/\delta_j}
=e^{cr_j^{-\alpha}}
\]

overwhelms the prefactor `r_j^2`, so infinitely many such events are impossible.

### Logarithmic interface

If

\[
\delta_j\asymp\frac{a}{|\log r_j|},
\]

then

\[
r_j^2e^{c/\delta_j}
\asymp
r_j^{2-c/a}.
\]

Thus the borderline is logarithmic, with the exact threshold depending on the constants in the strain/action estimates.

---

## 10. Relation to M5-428

M5-428 gives the qualitative split

\[
\text{fast interface}
\to
\text{strong strain}
\to
\text{strong critical mass}.
\]

The present note adds a **globally summable rate price**:

\[
\boxed{
\text{duration }\delta_j
\to
\text{cost }r_j^2\delta_j e^{c/\delta_j}.
}
\]

Thus increasingly violent interface events cannot be arbitrarily dense near the singular time.

---

## 11. Firewall

The result does not exclude natural-time interfaces with `delta_j ~ 1`.

For those events the cost reduces to `O(r_j^2)`, which is geometrically summable.

It also does not prove a uniform positive lower bound on `delta_j`; the permitted logarithmic decay remains open.

Therefore the critical problem survives in the slow/natural-time throughput regime.

---

## 12. Audit verdict

### GLOBAL RATE LEDGER

\[
\boxed{
\sum_j
r_j^2\delta_j e^{c/\delta_j}<\infty.
}
\]

### EXCLUDED

Power-fast or super-logarithmically fast order-one interface collapse on infinitely many late stages.

### SURVIVING

Natural-time and logarithmically shrinking interface corridors, plus slower delocalization below the M5-430 `r^{-1/4}` threshold.

### STATUS

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
