# Explicit Leray Active-Window Constants — 2026-08-24

Status: **EXPLICIT CONSTANT BRIDGE FROM FIRST-HITTING ANALYTIC THICKNESS TO THE LOG-FREQUENCY TAX / GLOBAL REGULARITY NOT PROVED.**

This note makes the constants in

`RECURRENT_LOG_FREQUENCY_VISCOUS_GRONWALL_GATE_2026-08-24.md`

explicit by converting the dynamic first-hitting terminal tube from

`TERMINAL_THICK_WINDOW_ACTION_OVERLAP_GATE_2026-08-24.md`

into the ancient Leray variables.

The output is an explicit lower bound for the long-Leray-time frequency ratio average

\[
c_{log}>0
\]

in terms of first-hitting analytic and stage constants.

---

## 1. Backward checkpoint constants

Let the ancient backward first-hitting checkpoints be `tau_m<0`, with

\[
\|\Omega(\tau_m)\|_\infty=q^{-m}.
\]

The stage-time estimates give

\[
\boxed{
 c_-q^m
\le
|\tau_m|
\le
c_+q^m,
}
\]

where one convenient pair is

\[
\boxed{
 c_-:=\frac{L_-}{q},
\qquad
 c_+:=\frac{L_+q}{q-1}.
}
\]

Define the checkpoint Leray vorticity amplitude

\[
\boxed{
\mu_m
:=
|\tau_m|q^{-m}.
}
\]

Then

\[
\boxed{
 c_-\le\mu_m\le c_+.
}
\]

---

## 2. Dynamic terminal thick tube

At each first-hitting checkpoint use the continuously dynamically normalized variables centered at the checkpoint maximum. The existing analytic terminal-tube lemma gives

\[
\boxed{
\delta_D
:=
\frac1{4(2B_++3\nu K_{2,+})}
}
\]

of dynamic normalized time and

\[
\boxed{
r_D:=\frac1{4K_{1,+}}}
\]

of dynamic normalized radius such that throughout the tube

\[
\boxed{|\widetilde\Omega|\ge\frac12.}
\]

Here `widetilde Omega` is vorticity divided by the instantaneous running maximum.

The dynamic scale rate obeys

\[
0\le b\le B_+.
\]

Therefore if `M_D(s)` denotes the running ancient-vorticity maximum along the dynamic window ending at the checkpoint value `M_0=q^{-m}`, then

\[
\boxed{
M_0e^{-B_+\delta_D}
\le
M_D(s)
\le
M_0.
}
\]

---

## 3. Bound the Leray amplitude across the whole terminal window

Let

\[
T=-\tau>0
\]

and

\[
\mu(s)=T(s)M_D(s).
\]

At the checkpoint,

\[
\mu(0)=\mu_m\in[c_-,c_+].
\]

Since dynamic time satisfies

\[
ds_D=M_D\,d\tau,
\]

going backward across a dynamic interval of length at most `delta_D` changes `T` by at most

\[
T(s)-T_0
\le
\frac{\delta_De^{B_+\delta_D}}{M_0}.
\]

Hence throughout the tube,

\[
\boxed{
\mu(s)
\le
\mu_+
:=
c_+
+
\delta_De^{B_+\delta_D}.
}
\]

Also `T(s)>=T_0` and `M_D(s)>=M_0e^{-B_+delta_D}`, so

\[
\boxed{
\mu(s)
\ge
\mu_-
:=
c_-e^{-B_+\delta_D}.
}
\]

Thus the full dynamic terminal tube lies in a Leray-amplitude corridor

\[
\boxed{
0<\mu_-\le TM_D\le\mu_+<\infty.
}
\]

---

## 4. Explicit Leray spatial thickness and vorticity floor

The Leray variables are

\[
Y=\frac y{\sqrt T},
\qquad
W(Y,s_L)=T\Omega(y,\tau).
\]

Dynamic normalized space is

\[
z=\sqrt{M_D}(y-y_c).
\]

Therefore a dynamic ball `|z|<=r_D` becomes a Leray ball of radius

\[
\frac{r_D}{\sqrt{TM_D}}.
\]

Using the upper amplitude bound gives the uniform Leray radius

\[
\boxed{
 r_L
:=
\frac{r_D}{\sqrt{\mu_+}}.
}
\]

Inside this ball,

\[
|W|
=TM_D|\widetilde\Omega|
\ge
\frac{\mu_-}{2}.
\]

Define

\[
\boxed{
w_L:=\frac{\mu_-}{2}.}
\]

Then throughout every converted terminal window,

\[
\boxed{
|W(Y,s_L)|\ge w_L
\quad\text{on a ball of radius }r_L.
}
\]

Hence the local Leray enstrophy satisfies

\[
\boxed{
 z_L
:=
\int_{B_{r_L}}|W|^2dY
\ge
w_L^2|B_{r_L}|
=
\frac{\mu_-^2}{4}
\frac{4\pi}{3}r_L^3.
}
\]

---

## 5. Explicit Leray-time duration

The Leray logarithmic time satisfies

\[
ds_L=\frac{d\tau}{T}.
\]

Together with

\[
ds_D=M_Dd\tau,
\]

we have

\[
\boxed{
ds_L=\frac{ds_D}{TM_D}=\frac{ds_D}{\mu(s)}.}
\]

Since `mu(s)<=mu_+`, a dynamic terminal interval of length `delta_D` produces a Leray interval of length at least

\[
\boxed{
\delta_L
:=
\frac{\delta_D}{\mu_+}.
}
\]

---

## 6. Explicit active-window time density

The checkpoint Leray times are

\[
s_m=-\log|\tau_m|.
\]

Their gap satisfies

\[
|s_{m+1}-s_m|
\le
\boxed{
G_L
:=
\log\left(
q\frac{c_+}{c_-}
\right).
}
\]

Each checkpoint carries a preceding active interval of Leray length at least `delta_L`. Because the checkpoint gaps are at most `G_L`, the union of these active intervals has lower asymptotic Leray-time density at least

\[
\boxed{
 d_L
:=
\min\left\{
1,
\frac{\delta_L}{G_L}
\right\}.
}
\]

Overlaps only increase the occupied density.

---

## 7. Explicit pointwise Leray frequency floor on active windows

Let

\[
Q_L=\|\nabla_YW\|_2^2,
\qquad
Z_L=\|W\|_2^2.
\]

Sobolev gives

\[
\|W\|_6^2\le S_3^{-1}Q_L,
\qquad
S_3=3(\pi/2)^{4/3}.
\]

Using the local enstrophy lower bound on a ball of radius `r_L`,

\[
Q_L
\ge
S_3|B_{r_L}|^{-2/3}z_L.
\]

Substituting the explicit `z_L`,

\[
\boxed{
Q_L
\ge
Q_*
:=
\frac{S_3\mu_-^2}{4}
\left(\frac{4\pi}{3}\right)^{1/3}
r_L.
}
\]

Let `Z_{L,+}` denote the global Leray enstrophy ceiling. The backward enstrophy decay gives the safe choice

\[
\boxed{
Z_{L,+}
\le
Z_+K_I^{1/2},
}
\]

where `Z_+` is the dynamic normalized enstrophy ceiling and

\[
K_I=\frac{q^2}{q-1}L_+.
\]

Therefore on every active window,

\[
\boxed{
\lambda_L
:=
\frac{Q_L}{Z_L}
\ge
\lambda_*
:=
\frac{Q_*}{Z_{L,+}}.
}
\]

---

## 8. Explicit logarithmic frequency-tax constant

The long-time frequency-ratio average consequently obeys

\[
\boxed{
 c_{log}
\ge
c_{log}^{exp}
:=
d_L\lambda_*.
}
\]

Substituting the explicit definitions,

\[
\boxed{
 c_{log}^{exp}
=
\min\left\{
1,
\frac{\delta_D}{\mu_+G_L}
\right\}
\frac{S_3}{4Z_{L,+}}
\left(\frac{4\pi}{3}\right)^{1/3}
\frac{\mu_-^2r_D}{\sqrt{\mu_+}}.
}
\]

where

\[
\boxed{
\begin{aligned}
\delta_D
&=
\frac1{4(2B_++3\nu K_{2,+})},
\\
r_D
&=
\frac1{4K_{1,+}},
\\
\mu_-
&=
\frac{L_-}{q}
e^{-B_+\delta_D},
\\
\mu_+
&=
\frac{L_+q}{q-1}
+
\delta_De^{B_+\delta_D},
\\
G_L
&=
\log\left[
q
\frac{L_+q/(q-1)}
{L_-/q}
\right].
\end{aligned}
}
\]

This is a completely tail-independent positive number whenever all first-hitting analytic/rate constants are finite and `L_->0`.

---

## 9. Fully explicit viscous Gronwall certificate

The preceding recurrent Gronwall note closes the vorticity-tight ancient branch if

\[
\sqrt2K_I
-
2\nu c_{log}
<
\frac12.
\]

A sufficient fully explicit condition is therefore

\[
\boxed{
\sqrt2
\frac{q^2}{q-1}L_+
-
2\nu c_{log}^{exp}
<
\frac12.
}
\]

All quantities in this inequality are now functions of

\[
\boxed{
q,
L_-,
L_+,
B_+,
K_{1,+},
K_{2,+},
Z_+,
\nu
}
\]

and universal Sobolev/geometric constants.

No spatial velocity-tail norm, Lorentz norm, or historical-shell amplitude enters this certificate.

---

## 10. Audit caveats

The conversion uses the dynamic terminal tube along each inherited first-hitting checkpoint. To promote the explicit constant exactly as written into a formal theorem, one should package two bookkeeping facts in one lemma:

1. the continuously dynamically normalized terminal tube survives passage through the fixed-stage ancient limit at each inherited checkpoint;
2. the dynamic scale rate `b` used in the tube satisfies `0<=b<=B_+` uniformly through those inherited windows.

Both are already assumptions/outputs of the smooth first-hitting analytic corridor, but their simultaneous passage has not previously been stated as a standalone lemma.

The density estimate does **not** require the active balls to remain at one fixed spatial center because `Q_L` is a whole-space quantity. This avoids an unnecessary center-tracking hypothesis in the frequency-tax step.

---

## 11. Interpretation

The recurrent viscous gain is no longer an abstract positive constant. A first-hitting endpoint repeatedly creates a definite amount of vorticity in a definite dynamic ball for a definite dynamic time. After Leray conversion, this creates

\[
\boxed{
\text{positive-density intervals with }
Q_L/Z_L\ge\lambda_*>0.
}
\]

The resulting logarithmic viscous dissipation directly subtracts from the Type-I stretching exponent in the ancient Gronwall inequality.

Status: **THE TERMINAL ANALYTIC THICK-TUBE CONSTANTS YIELD AN EXPLICIT POSITIVE LOWER BOUND `c_log^exp` FOR THE LONG-LERAY-TIME FREQUENCY RATIO. THE VORTICITY-TIGHT ANCIENT SURVIVOR IS EXCLUDED IF `sqrt2 q^2 L_+/(q-1) - 2 nu c_log^exp < 1/2`. THIS IS A TAIL-INDEPENDENT NUMERICAL CERTIFICATE, NOT YET A VERIFIED UNIVERSAL INEQUALITY FOR THE CURRENT CONSTANT RANGES. GLOBAL REGULARITY REMAINS UNPROVED.**