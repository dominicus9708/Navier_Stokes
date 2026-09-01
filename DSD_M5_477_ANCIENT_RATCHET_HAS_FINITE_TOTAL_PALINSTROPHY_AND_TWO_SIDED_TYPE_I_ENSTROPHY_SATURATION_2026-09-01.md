# DSD M5-477 — Ancient ratchet has finite total palinstrophy and two-sided Type-I enstrophy saturation

Date: 2026-09-01

Status: **ANCIENT ENERGY-STRUCTURE SHARPENING / THE M5-475 TYPE-I DECAY MAKES THE VORTICITY-STRETCHING PRODUCTION INTEGRABLE AT BACKWARD INFINITY, SO THE MARKED ANCIENT ELEMENT HAS FINITE TOTAL PALINSTROPHY ON `(-infinity,0]` / AT THE SAME TIME THE NATURAL FIRST-HITTING TAYLOR CARRIER SURVIVES ON EVERY GEOMETRIC BACKWARD RECORD SCALE AND FORCES A MATCHING LOWER ENSTROPHY RATE `||Omega(tau_m)||_2^2 >= c |tau_m|^-1/2` / THUS THE ANCIENT ELEMENT DECAYS TO ZERO BUT SATURATES THE CRITICAL TYPE-I ENSTROPHY RATE ALONG AN INFINITE BACKWARD FIRST-HITTING SEQUENCE / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Ancient vorticity equation

For the viscosity-one ancient element,

\[
\partial_\tau\Omega
+V\cdot\nabla\Omega
=S\Omega+\Delta\Omega,
\]

with

\[
\nabla\cdot V=0.
\]

Taking the global `L2` inner product with `Omega` gives

\[
\boxed{
\frac12\frac d{d\tau}\|\Omega\|_2^2
+\|\nabla\Omega\|_2^2
=\int S\Omega\cdot\Omega\,dx.
}
\]

The identity is legitimate on every finite interval because the ancient element is smooth and `Omega in L2 cap Linfinity`.

---

## 2. Stretching production is integrable at backward infinity

Calderon--Zygmund gives

\[
\|S\|_2\le C\|\Omega\|_2.
\]

Also

\[
\|\Omega\|_4^2
\le
\|\Omega\|_\infty\|\Omega\|_2.
\]

Hence

\[
\begin{aligned}
\left|
\int S\Omega\cdot\Omega
\right|
&\le
\|S\|_2\|\Omega\|_4^2\\
&\le
C\|\Omega\|_\infty\|\Omega\|_2^2.
\end{aligned}
\]

M5-475 gives for `tau << -1`

\[
\|\Omega(\tau)\|_\infty
\le C(-\tau)^{-1},
\]

\[
\|\Omega(\tau)\|_2^2
\le C(-\tau)^{-1/2}.
\]

Therefore

\[
\boxed{
\left|
\int S\Omega\cdot\Omega
\right|
\le C(-\tau)^{-3/2}.
}
\]

Since

\[
\int_{-\infty}^{-1}(-\tau)^{-3/2}d\tau<\infty,
\]

the total backward stretching production is finite.

---

## 3. Finite total palinstrophy

Integrate the enstrophy identity from `-T` to `0`:

\[
\frac12\|\Omega(0)\|_2^2
-
\frac12\|\Omega(-T)\|_2^2
+
\int_{-T}^{0}\|\nabla\Omega\|_2^2d\tau
=
\int_{-T}^{0}\int S\Omega\cdot\Omega.
\]

M5-475 gives

\[
\|\Omega(-T)\|_2\to0
\qquad(T\to\infty).
\]

The stretching integral converges absolutely at `-infinity`, and it is finite on `[-1,0]` by smoothness. Letting `T -> infinity`,

\[
\boxed{
\int_{-\infty}^{0}
\|\nabla\Omega(\tau)\|_2^2d\tau
<\infty.
}
\]

Thus the ancient element has finite total vorticity palinstrophy dissipation over its entire backward history.

This is not in conflict with M5-472: scale-critical directional-diffusion charges at older and older physical scales acquire a summable factor when measured in the fixed finest-scale `L2` palinstrophy ledger.

---

## 4. Backward first-hitting times in the ancient coordinates

Let `tau_m<0` denote the ancient normalized time corresponding to the first-hitting level `m` generations before the marked time `tau=0`.

As in M5-475,

\[
\boxed{
|\tau_m|\asymp q^m.
}
\]

At that physical first-hitting stage, use its own natural coordinates

\[
Z=\frac{x-X_{j-m}}{r_{j-m}}.
\]

The first-hitting Taylor-carrier theorem supplies a fixed ball/cylinder in which

\[
|\Omega^{own}_{j-m}(Z)|
\ge c_0>0
\]

on a set of fixed positive normalized volume `v0>0`.

---

## 5. Convert the Taylor carrier to the marked ancient normalization

The scale ratio is

\[
K_m:=\frac{r_{j-m}}{r_j}=q^{m/2}.
\]

Vorticity amplitude in the finer marked normalization is reduced by

\[
K_m^{-2}=q^{-m}.
\]

The carrier spatial volume is enlarged by

\[
K_m^3=q^{3m/2}.
\]

Therefore the carrier alone contributes

\[
\begin{aligned}
\|\Omega_j(\tau_m)\|_2^2
&\ge
c_0^2v_0
K_m^{-4}K_m^3\\
&=
c_*K_m^{-1}\\
&=
c_*q^{-m/2}.
\end{aligned}
\]

Passing to the ancient limit,

\[
\boxed{
\|\Omega(\tau_m)\|_2^2
\ge c q^{-m/2}.
}
\]

Since `|tau_m| ~ q^m`,

\[
\boxed{
\|\Omega(\tau_m)\|_2^2
\ge
c(-\tau_m)^{-1/2}.
}
\]

Together with M5-475,

\[
\boxed{
 c(-\tau_m)^{-1/2}
 \le
 \|\Omega(\tau_m)\|_2^2
 \le
 C(-\tau_m)^{-1/2}.
}
\]

Thus the Type-I enstrophy decay is saturated on every retained backward record scale.

---

## 6. Vorticity `Linfinity` is likewise saturated at the record points

At each old first-hitting maximum,

\[
\|\omega(t_{j-m})\|_\infty=W_{j-m}=q^{-m}W_j.
\]

Hence in the marked normalization

\[
\boxed{
\|\Omega(\tau_m)\|_\infty
\asymp q^{-m}
\asymp(-\tau_m)^{-1}.
}
\]

So both global enstrophy and maximum vorticity attain their exact critical Type-I orders along the record sequence.

---

## 7. Critical strain upper rate is logarithmic and sharp

Interpolation gives

\[
\|\Omega\|_3
\le
\|\Omega\|_2^{2/3}
\|\Omega\|_\infty^{1/3}.
\]

Therefore

\[
\|S\|_3^2
\le C\|\Omega\|_3^2
\le
C
\left(\|\Omega\|_2^2\right)^{2/3}
\|\Omega\|_\infty^{2/3}.
\]

Using the Type-I upper rates,

\[
\boxed{
\|S(\tau)\|_3^2
\le
C(-\tau)^{-1}
\qquad(\tau\ll-1).
}
\]

Hence each geometric backward time annulus contributes at most a fixed constant:

\[
\int_{-Cq^{m+1}}^{-cq^m}
\|S(\tau)\|_3^2d\tau
\le C\log q.
\]

M5-472 shows ratchet stages pay a fixed lower critical charge. Thus the marked ancient lane lives exactly at the logarithmic critical boundary rather than beyond it.

---

## 8. Interpretation

The ancient element has the simultaneous properties

\[
\Omega(\tau)\to0
\quad(\tau\to-\infty),
\]

but

\[
\sqrt{-\tau_m}\,
\|\Omega(\tau_m)\|_2^2
\asymp1,
\]

and

\[
(-\tau_m)
\|\Omega(\tau_m)\|_\infty
\asymp1
\]

on infinitely many backward record scales.

Thus it is not merely a decaying ancient solution. It is a **critically saturated backward cascade**.

---

## 9. Highest-value next target

Use the saturated sequence `tau_m -> -infinity` to perform the backward parabolic blow-down

\[
V^{(m)}(y,s)
:=
\sqrt{-\tau_m}\,
V(\sqrt{-\tau_m}\,y,
(-\tau_m)s).
\]

At `s=-1`, both `L2` vorticity and `Linfinity` vorticity have nondegenerate scale-invariant size. This should yield a nontrivial backward blow-down ancient profile.

Its terminal `s=0` slice probes exactly the low-frequency/passive spatial tail isolated in M5-476.

This creates a direct route from the marked ratchet cascade to a tail-rigidity/backward-uniqueness dichotomy.

---

## 10. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
