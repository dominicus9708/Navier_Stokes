# DSD M5-475 — Marked ancient ratchet element has backward Type-I enstrophy and velocity decay

Date: 2026-09-01

Status: **ANCIENT-CLASS SHARPENING / ON THE BOUNDED FIRST-HITTING RATCHET LANE OF M5-474, THE GEOMETRIC RECORD STRUCTURE FORCES `||Omega(tau)||_infinity = O(|tau|^-1)` AND `||Omega(tau)||_2^2 = O(|tau|^-1/2)` AS `tau -> -infinity`; BIOT--SAVART THEN GIVES THE TYPE-I VELOCITY DECAY `||V(tau)||_infinity = O(|tau|^-1/2)` AND `||V(tau)||_6 = O(|tau|^-1/4)` / THIS PLACES THE MARKED ELEMENT IN A MUCH SHARPER TYPE-I FINITE-ENSTROPHY ANCIENT CLASS, BUT NO GENERAL 3D LIOUVILLE THEOREM IS KNOWN FOR THIS CLASS WITHOUT AN ADDITIONAL STRONG-CRITICAL TAIL CONDITION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. First-hitting generation geometry

Let the current first-hitting level be

\[
W_j=q^jW_0,
\qquad
r_j=\sqrt{\nu/W_j}.
\]

The stage `m` generations earlier has

\[
W_{j-m}=q^{-m}W_j,
\qquad
r_{j-m}=q^{m/2}r_j.
\]

Use the `j`-normalized variables of M5-474:

\[
Y=\frac{x-X_j}{r_j},
\qquad
\tau=\frac{\nu(t-t_j)}{r_j^2},
\qquad
\Omega_j=\frac{r_j^2}{\nu}\omega.
\]

Assume the inherited smooth non-escape first-hitting corridor has normalized stage lengths bounded above and below:

\[
0<L_-\le L_k\le L_+<\infty.
\]

The physical duration of stage `j-l` is comparable to

\[
\frac{r_{j-l}^2}{\nu}
=\frac{q^l r_j^2}{\nu}.
\]

Therefore the `j`-normalized backward time to stage `j-m` obeys

\[
\boxed{
 c_-q^m
 \le
 |	au_m|
 \le
 c_+q^m
}
\]

for fixed positive constants `c_-,c_+` depending only on `q,L_-,L_+`.

---

## 2. Backward Type-I vorticity `L-infinity` decay

By the record/first-hitting definition, during stage `j-m` the physical vorticity is bounded by a fixed multiple of `W_{j-m}`:

\[
\|\omega(t)\|_\infty
\le C_q W_{j-m}.
\]

In the `j` normalization,

\[
\|\Omega_j(\tau)\|_\infty
\le
\frac{r_j^2}{\nu}C_qW_{j-m}
=C_q\frac{W_{j-m}}{W_j}
=C_q q^{-m}.
\]

Since `|tau_m| ~ q^m`, this becomes

\[
\boxed{
\|\Omega_j(\tau)\|_\infty
\le
\frac{C}{1+|\tau|}
}
\]

through the old-stage intervals. Passing to the M5-474 ancient limit,

\[
\boxed{
\|\Omega_*(\tau)\|_\infty
\le
C(-\tau)^{-1},
\qquad \tau\ll-1.
}
\]

This is the natural vorticity Type-I rate.

---

## 3. Backward normalized enstrophy decay

The bounded-ratchet corridor assumes the own-scale normalized enstrophy bound

\[
\frac{r_{j-m}}{\nu^2}
\|\omega(t)\|_2^2
\le Z_*.
\]

Measured in the finer `j` normalization,

\[
\begin{aligned}
\|\Omega_j(\tau)\|_2^2
&=
\frac{r_j}{\nu^2}
\|\omega(t)\|_2^2\\
&=
\frac{r_j}{r_{j-m}}
\left[
\frac{r_{j-m}}{\nu^2}
\|\omega(t)\|_2^2
\right]\\
&\le
Z_*q^{-m/2}.
\end{aligned}
\]

Thus

\[
\boxed{
\|\Omega_*(\tau)\|_2^2
\le
C(-\tau)^{-1/2},
\qquad \tau\ll-1.
}
\]

Equivalently,

\[
\boxed{
\|\Omega_*(\tau)\|_2
\le
C(-\tau)^{-1/4}.
}
\]

The ancient element therefore tends to zero in global enstrophy as `tau -> -infinity`.

---

## 4. Velocity `L6` decay

Because `div V_*=0` and `curl V_*=Omega_*`, homogeneous Sobolev gives

\[
\|V_*(\tau)\|_6
\le C\|\nabla V_*(\tau)\|_2
=C\|\Omega_*(\tau)\|_2.
\]

Therefore

\[
\boxed{
\|V_*(\tau)\|_6
\le
C(-\tau)^{-1/4}.
}
\]

This is the scale-critical Type-I rate for the `L6` velocity norm.

---

## 5. Velocity `L-infinity` decay from optimized Biot--Savart splitting

Biot--Savart gives

\[
V(x)
=\int K(x-y)\Omega(y)dy,
\qquad |K(z)|\lesssim |z|^{-2}.
\]

For any splitting radius `R>0`,

\[
|V(x)|
\lesssim
R\|\Omega\|_\infty
+R^{-1/2}\|\Omega\|_2.
\]

Optimize with

\[
R
\asymp
\left(
\frac{\|\Omega\|_2}{\|\Omega\|_\infty}
\right)^{2/3}.
\]

Then

\[
\boxed{
\|V\|_\infty
\lesssim
\|\Omega\|_\infty^{1/3}
\|\Omega\|_2^{2/3}.
}
\]

Insert the ancient decay laws:

\[
\|\Omega\|_\infty^{1/3}
\lesssim(-\tau)^{-1/3},
\]

\[
\|\Omega\|_2^{2/3}
\lesssim(-\tau)^{-1/6}.
\]

Hence

\[
\boxed{
\|V_*(\tau)\|_\infty
\le
C(-\tau)^{-1/2}.
}
\]

Thus

\[
\boxed{
\sup_{\tau<-1}
\sqrt{-\tau}\,
\|V_*(\tau)\|_\infty
<\infty.
}
\]

---

## 6. Relation to Type-I ancient theory

The marked element now satisfies simultaneously

\[
\|V_*(\tau)\|_\infty
\lesssim(-\tau)^{-1/2},
\]

\[
\|\Omega_*(\tau)\|_\infty
\lesssim(-\tau)^{-1},
\]

\[
\|\Omega_*(\tau)\|_2^2
\lesssim(-\tau)^{-1/2},
\]

plus the M5-474 first-hitting and material-ratchet marks.

This places the element in a sharp Type-I finite-enstrophy ancient class.

Known 3D ancient Liouville theorems do not, however, assert that every solution in this class is zero. Albritton--Barker obtain a Liouville conclusion under an additional strong `L3` backward-sequence condition, while the general bounded ancient problem remains open.

No such extra condition is silently assumed here.

---

## 7. What has actually improved

M5-474 gave only compact-backward-interval bounds.

M5-475 adds an explicit asymptotic history:

\[
\boxed{
\tau\to-\infty
\quad\Longrightarrow\quad
\Omega_*(\tau)\to0\text{ in }L^2\cap L^\infty,
\quad
V_*(\tau)\to0\text{ in }L^6\cap L^\infty,
}
\]

at the exact Type-I rates.

Thus the remaining ancient object is not an arbitrary eternal bounded flow. It emerges from zero at backward infinity at the critical scaling rate and later develops a marked first-hitting/ratchet event.

---

## 8. Highest-value next target

The next question is whether

\[
\Omega\in L^2\cap L^\infty,
\qquad
\Omega(\tau)\to0\text{ backward at Type-I rate}
\]

forces enough low-frequency/tail control on `V` to create

1. a backward sequence bounded in strong `L3`, or
2. a finite-energy active-cluster quotient plus a negligible harmonic tail.

Either would connect the marked element to an existing rigidity mechanism without claiming a new general bounded-ancient Liouville theorem.

---

## 9. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
