# Vorticity first-hitting strain / energy-tax gate

Date: 2026-08-25

Status: **ACTIVE CALCULATION — GLOBAL REGULARITY NOT PROVED**

## 1. Why use vorticity first hitting

The velocity-gradient first-hitting calculation reduces compressed epochs to the pressure Hessian.  A cleaner pressure-free route is obtained from

\[
W(t)=\|\omega(t)\|_{L^\infty(\mathbb R^3)}.
\]

Let

\[
\overline W(t)=\max_{0\le s\le t}W(s),
\qquad
W_j=q^jW_0,
\qquad q>1,
\]

and define the first-hitting times

\[
t_j=\inf\{t:\overline W(t)=W_j\}.
\]

The natural viscous-vorticity radius is

\[
\boxed{
r_j=\left(\frac\nu{W_j}\right)^{1/2}.
}
\]

For the epoch

\[
I_j=(t_{j-1},t_j),
\]

define its dimensionless parabolic duration

\[
\boxed{
\Theta_j
:=W_{j-1}|I_j|
=\frac{\nu|I_j|}{r_{j-1}^2}.
}
\]

---

## 2. Maximum-vorticity growth contains no pressure

Where `omega != 0`, let

\[
\rho=|\omega|,
\qquad
\xi=\omega/|\omega|,
\qquad
\gamma=\xi^TS\xi.
\]

The exact magnitude equation is

\[
(\partial_t+u\cdot\nabla-\nu\Delta)\rho
=
\rho\left(\gamma-\nu|\nabla\xi|^2\right).
\]

At a maximum point of `rho`, diffusion and direction variation are favorable. Hence

\[
\boxed{
D^+W(t)
\le
W(t)\sup_x|S(x,t)|.
}
\]

On the contact set where `overline W=W` and `overline W'>0`, therefore,

\[
\boxed{
\frac{\overline W'}{\overline W^2}
\le
\frac{\|S(t)\|_\infty}{W(t)}.
}
\]

Status: **PROVED for smooth pre-singular solutions in the standard Dini/running-maximum sense.**

---

## 3. Exact first-hitting burden

Integration gives

\[
\int_{I_j}
\frac{\overline W'}{\overline W^2}dt
=
\frac1{W_{j-1}}-\frac1{W_j}
=
\frac{1-q^{-1}}{W_{j-1}}.
\]

Thus

\[
\boxed{
1-q^{-1}
\le
W_{j-1}
\int_{I_j\cap\{\overline W=W\}}
\frac{\|S(t)\|_\infty}{W(t)}dt.
}
\]

A new vorticity level cannot be hit without a fixed normalized strain exposure.

---

## 4. Biot-Savart strain split at the natural radius

The strain is a Calderon-Zygmund singular integral of vorticity,

\[
S=\operatorname{p.v.}K*\omega,
\qquad
|K(z)|\lesssim |z|^{-3},
\]

with mean-zero angular kernel.

At radius

\[
r(t)=\left(\frac\nu{W(t)}\right)^{1/2},
\]

split `S=S_<r+S_>r`.

### 4.1 Near strain

Kernel cancellation gives

\[
|S_{<r}(x)|
\lesssim
r\|\nabla\omega\|_\infty.
\]

Define

\[
\boxed{
H_{\omega,1}(t)
:=
\frac{r(t)\|\nabla\omega(t)\|_\infty}{W(t)}
=
\frac{r(t)^3}{\nu}\|\nabla\omega(t)\|_\infty.
}
\]

Then

\[
\frac{\|S_{<r}\|_\infty}{W}
\lesssim H_{\omega,1}.
\]

### 4.2 Far strain

By Cauchy-Schwarz and `|K(z)| lesssim |z|^{-3}`,

\[
|S_{>r}(x)|
\lesssim
\left(\int_{|z|>r}|z|^{-6}dz\right)^{1/2}
\|\omega\|_2
\lesssim
r^{-3/2}\|\omega\|_2.
\]

Define

\[
\boxed{
Z_r(t)
:=
\frac{r(t)}{\nu^2}\|\omega(t)\|_2^2.
}
\]

Since `W=nu/r^2`,

\[
\boxed{
\frac{\|S_{>r}\|_\infty}{W}
\lesssim
Z_r^{1/2}.
}
\]

Therefore

\[
\boxed{
\frac{\|S(t)\|_\infty}{W(t)}
\lesssim
H_{\omega,1}(t)+Z_{r(t)}(t)^{1/2}.
}
\]

Status: **PROVED as a smooth Biot-Savart near/far estimate.**

---

## 5. Time-integrated derivative-or-enstrophy dichotomy

On contact times in `I_j`, `W(t)` lies between `W_{j-1}` and `qW_{j-1}`, so `r(t)` is comparable with `r_{j-1}`.

Define the normalized near-derivative occupancy

\[
\boxed{
\mathfrak H_j
:=
W_{j-1}
\int_{I_j\cap\{\overline W=W\}}
H_{\omega,1}(t)dt
}
\]

and the natural-window enstrophy cost

\[
\boxed{
\mathfrak Z_j
:=
\frac1{\nu r_{j-1}}
\int_{I_j}\|\omega(t)\|_2^2dt.
}
\]

Cauchy-Schwarz in normalized time gives

\[
W_{j-1}
\int_{I_j\cap\{\overline W=W\}}
Z_{r(t)}^{1/2}dt
\lesssim
\Theta_j^{1/2}\mathfrak Z_j^{1/2}.
\]

Hence

\[
\boxed{
1-q^{-1}
\lesssim
\mathfrak H_j
+
\sqrt{\Theta_j\mathfrak Z_j}.
}
\]

This is the main first-hitting gate.

For constants depending only on `q` and the kernel bounds,

\[
\boxed{
\mathfrak H_j<c_q
\Longrightarrow
\mathfrak Z_j
\gtrsim_q
\Theta_j^{-1}.
}
\]

Equivalently, a rapidly compressed first-hitting epoch that does not spend normalized time in strong local `nabla omega` concentration must pay an inverse-duration enstrophy cost.

Status: **PROVED.**

---

## 6. Conversion to the global energy ledger

For smooth divergence-free whole-space solutions with sufficient decay,

\[
\|\nabla u\|_2^2=\|\omega\|_2^2.
\]

The energy identity gives

\[
\nu\int_0^{T}\|\omega(t)\|_2^2dt
\le
E_0,
\qquad
E_0:=\frac12\|u_0\|_2^2.
\]

By definition,

\[
\boxed{
\nu^2r_{j-1}\mathfrak Z_j
=
\nu\int_{I_j}\|\omega(t)\|_2^2dt.
}
\]

The first-hitting epochs are disjoint. Therefore

\[
\boxed{
\sum_j r_{j-1}\mathfrak Z_j
\le
\frac{E_0}{\nu^2}.
}
\]

Let the energy length be

\[
\boxed{
L_E:=\frac{E_0}{\nu^2}.
}
\]

On the derivative-quiet subset

\[
Q:=\{j:\mathfrak H_j<c_q\},
\]

the inverse-duration lower bound implies

\[
\boxed{
\sum_{j\in Q}
\frac{r_{j-1}/L_E}{\Theta_j}
<\infty.
}
\]

This is a new necessary summability law for any derivative-quiet first-hitting cascade.

---

## 7. Excluded ultra-compressed quiet epochs

If infinitely many derivative-quiet epochs satisfied

\[
\Theta_j
\le
C\frac{r_{j-1}}{L_E},
\]

then

\[
\frac{r_{j-1}/L_E}{\Theta_j}
\ge
C^{-1}
\]

on infinitely many indices, contradicting the summability law.

Therefore

\[
\boxed{
\Theta_j
\lesssim
\frac{r_{j-1}}{L_E}
\text{ infinitely often}
\Longrightarrow
\mathfrak H_j\ge c_q
\text{ infinitely often}.
}
\]

In physical time,

\[
|I_j|=\Theta_j\frac{r_{j-1}^2}{\nu}.
\]

Hence the excluded quiet compression scale is

\[
\boxed{
|I_j|
\lesssim
\frac{r_{j-1}^3}{\nu L_E}.
}
\]

So an infinite sequence of hitting epochs at or below this cubic energy-controlled time scale cannot remain derivative-quiet.

Status: **PROVED RATE-CLASS EXCLUSION; NOT A FULL BLOWUP EXCLUSION.**

---

## 8. What survives

The vorticity first-hitting cascade now obeys

\[
\boxed{
\text{new vorticity level}
\Longrightarrow
\text{normalized }\nabla\omega\text{ occupancy}
\ \lor\ 
\text{natural-window enstrophy tax}.
}
\]

And the second branch is globally summable only under

\[
\sum_j
\frac{r_j/L_E}{\Theta_j}<\infty.
\]

Therefore the remaining escape routes are:

1. derivative-active epochs with nontrivial `mathfrak H_j`;
2. derivative-quiet epochs whose normalized durations are large enough to satisfy the weighted summability condition.

The next calculation should attack route 1 by converting the **time-integrated** `nabla omega` occupancy into either spacetime palinstrophy cost or a still higher derivative space-time needle.  This is stronger than the previous purely instantaneous derivative descent.

---

## 9. Audit verdict

- pressure-free vorticity first-hitting identity: **PROVED**;
- near/far Biot-Savart strain split: **PROVED**;
- derivative-or-enstrophy first-hitting dichotomy: **PROVED**;
- inverse-duration enstrophy tax on derivative-quiet epochs: **PROVED**;
- global weighted summability of quiet epochs: **PROVED**;
- infinitely many `|I_j| lesssim r_j^3/(nu L_E)` derivative-quiet epochs: **EXCLUDED**;
- all compressed epochs excluded: **FALSE / NOT DERIVED**;
- derivative-active branch contradicted: **NOT DERIVED**;
- global regularity: **UNPROVED**.
