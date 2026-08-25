# DSD W1 Global Scale-Invariant Gain Synchronization

Date: 2026-08-26

Status: **GLOBAL ZERO-FREE SCALE-INVARIANT RATIO BUILT FROM ENSTROPHY AND `L4` AMPLITUDE / LERAY DAMPING CANCELS EXACTLY / PRESSURE-AMPLITUDE AND VORTICITY-STRETCH NET GAINS MUST SYNCHRONIZE IN CESARO AVERAGE EVEN WHEN THEIR ACTIVE SETS DO NOT OVERLAP / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The pointwise ratio

\[
|\Omega|^2/|U|^4
\]

couples pressure acceleration and vorticity stretching at the correct Navier--Stokes scaling, but is singular at zeros of `U` or `Omega`.

A global zero-free analogue is obtained from quantities with the same physical scaling.

Set

\[
\boxed{
X_4(s):=\|U(s)\|_4^4,
\qquad
Z(s):=\|\Omega(s)\|_2^2.
}
\]

For a nontrivial compact minimal W1 orbit, both are strictly positive and bounded above and below.

Under physical Navier--Stokes scaling both `X4` and `Z` scale like one inverse length. Therefore

\[
\boxed{
\Theta_4(s)
:=
\log\frac{Z(s)}{X_4(s)}
}
\]

is scale-invariant.

---

## 2. Exact `p=4` amplitude balance

The standard Leray `Lp` identity gives at `p=4`

\[
\boxed{
\frac14X_4'
+\frac18X_4
+\nu D_4
=\Pi_4,
}
\]

where

\[
D_4
:=
\int |U|^2|\nabla U|^2
+2\sum_j(U\cdot\partial_jU)^2
\]

and `Pi4` is the `p=4` pressure work.

Divide by `X4/4`:

\[
\boxed{
\frac{X_4'}{X_4}
=-\frac12
-4\nu\frac{D_4}{X_4}
+4\frac{\Pi_4}{X_4}.
}
\]

Define

\[
G_4:=4\frac{\Pi_4}{X_4},
\qquad
H_4:=4\nu\frac{D_4}{X_4}.
\]

Then

\[
\boxed{
(\log X_4)'
=-\frac12+G_4-H_4.
}
\]

---

## 3. Exact enstrophy balance

The Leray enstrophy identity is

\[
\boxed{
\frac12Z'
+\frac14Z
+\nu P_\Omega
=Q_\Omega,
}
\]

where

\[
P_\Omega:=\|\nabla\Omega\|_2^2,
\qquad
Q_\Omega:=\int\Omega\cdot S\Omega.
\]

Divide by `Z/2`:

\[
\boxed{
\frac{Z'}Z
=-\frac12
-2\nu\frac{P_\Omega}{Z}
+2\frac{Q_\Omega}{Z}.
}
\]

Define

\[
G_\Omega:=2\frac{Q_\Omega}{Z},
\qquad
H_\Omega:=2\nu\frac{P_\Omega}{Z}.
\]

Then

\[
\boxed{
(\log Z)'
=-\frac12+G_\Omega-H_\Omega.
}
\]

---

## 4. Exact cancellation of Leray damping

Subtract the two logarithmic balances:

\[
\boxed{
\Theta_4'
=
(G_\Omega-H_\Omega)
-(G_4-H_4).
}
\]

The `-1/2` similarity damping cancels identically.

Thus `Theta4` measures only the mismatch between the normalized vorticity-formation channel and the normalized velocity-amplitude-formation channel.

---

## 5. Long-time synchronization on a compact recurrent orbit

Since the compact minimal W1 set gives

\[
0<Z_-\le Z(s)\le Z_+<\infty,
\]

and

\[
0<X_-\le X_4(s)\le X_+<\infty,
\]

we have a bounded ratio

\[
|\Theta_4(s)|\le C_\Theta.
\]

Therefore for every interval `[s0,s0+S]`,

\[
\left|
\int_{s_0}^{s_0+S}
\Bigl[(G_\Omega-H_\Omega)-(G_4-H_4)\Bigr]ds
\right|
\le 2C_\Theta.
\]

Dividing by `S` and sending `S->infinity` gives

\[
\boxed{
\lim_{S\to\infty}
\frac1S
\int_{s_0}^{s_0+S}
(G_\Omega-H_\Omega)ds
=
\lim_{S\to\infty}
\frac1S
\int_{s_0}^{s_0+S}
(G_4-H_4)ds.
}
\]

In fact each side equals `1/2`, because `log Z` and `log X4` are themselves bounded:

\[
\boxed{
\left\langle G_\Omega-H_\Omega\right\rangle
=
\left\langle G_4-H_4\right\rangle
=\frac12.
}
\]

---

## 6. DSD consequence: alternation is a cycle, not an escape

Suppose the pressure/amplitude-active core and the vorticity-stretching-active core do not overlap in space-time.

They cannot then be treated as independent recurrent mechanisms. Their normalized net formation gains must satisfy the bounded mismatch law

\[
\boxed{
\left|
\int_I
[(G_\Omega-H_\Omega)-(G_4-H_4)]ds
\right|
\le 2C_\Theta
}
\]

on every interval `I` up to the corresponding endpoint difference of `Theta4`.

Thus persistent dominance of one channel without compensating activity in the other is impossible on a compact W1 orbit.

The non-overlap case is therefore a **paired formation cycle**:

\[
\boxed{
\text{velocity-amplitude formation}
\leftrightarrow
\text{vorticity formation},
}
\]

with a bounded critical phase mismatch.

This is a stronger and cleaner DSD statement than merely saying the two event sets are both syndetic.

---

## 7. Generalization

For any `p>3`, define

\[
A_p:=\|U\|_p^p,
\qquad
X_p:=A_p^{1/(p-3)}.
\]

`X_p` has the same physical scaling as enstrophy `Z`.

The `Lp` balance gives

\[
(\log X_p)'
=-\frac12
-\frac{p\nu}{p-3}\frac{D_p}{A_p}
+\frac p{p-3}\frac{\Pi_p}{A_p}.
\]

Hence

\[
\log\frac{Z}{X_p}
\]

is a whole family of global scale-invariant synchronization variables.

The `p=4` member is the simplest algebraically and requires no fractional power of `A_p`.

---

## 8. What remains

The synchronization law does not by itself forbid a recurrent formation cycle. It proves instead that spatial or temporal segregation between pressure-amplitude and vorticity-stretching activity is not a new terminal branch: any segregation must be dynamically paired so that the scale-invariant ratio remains bounded.

The next closure target can therefore be stated as:

\[
\boxed{
\text{Can an unforced finite-energy prelimit sustain a recurrent}
\quad
\beta=0
\quad
\text{formation cycle with gain }1/2
\text{ in both channels?}
}
\]

A contradiction requires either a monotone critical functional or a finite critical budget; neither is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
