# First-hitting amplitude + bounded normalized enstrophy automatically yields a terminal V2 reserve

Date: 2026-08-13

Status: **DERIVED GLOBAL NORMALIZED H1/V2 BOOTSTRAP ON A TERMINAL SUBWINDOW**.

The previous compactness route treated the normalized V2 channel

\[
\int|\Delta\Omega|^2
\]

as a separate bounded/unbounded branch.  On a first-hitting normalized amplification window, that separation can be simplified substantially.  If the normalized global enstrophy stays uniformly bounded, the exact amplitude cap `||Omega||_infinity<=1` gives a direct derivative-energy bootstrap that bounds V2 on a fixed terminal subwindow.

---

## 1. Hypotheses on the normalized backward window

Normalize by the later first-hitting checkpoint, so

\[
\boxed{
\|\Omega(s)\|_\infty\le1
}
\]

throughout the backward amplification interval.

Assume a fixed terminal interval

\[
[-2\delta,0]
\]

is available, with `delta>0` independent of the sequence.  The amplification-time noncollapse lemma supplies such a fixed interval on the fully bounded I/V/deformation branch.

Assume also

\[
\boxed{
E(s):=\|\Omega(s)\|_2^2
\le M_E
\qquad(-2\delta\le s\le0).
}
\]

This is the bounded normalized-global-enstrophy branch.

---

## 2. Uniform stretching-source bound

Let

\[
Q(s)=\int\Omega\cdot S_U\Omega dy.
\]

The strain/vorticity `L2` estimate gives

\[
\|S_U\|_2\le C\|\Omega\|_2.
\]

Also

\[
\|\Omega\|_4^2
\le
\|\Omega\|_\infty\|\Omega\|_2.
\]

Hence

\[
\boxed{
|Q(s)|
\le
C\|\Omega\|_\infty E(s)
\le
CM_E.
}
\]

---

## 3. First derivative energy has a good time slice

The global normalized enstrophy identity is

\[
\frac12E'(s)+\nu P(s)=Q(s),
\]

where

\[
P(s)=\|\nabla\Omega(s)\|_2^2.
\]

Integrate over

\[
[-2\delta,-\delta].
\]

Using `E<=M_E` and `|Q|<=CM_E`,

\[
\nu\int_{-2\delta}^{-\delta}P(s)ds
\le
\frac12M_E
+C M_E\delta.
\]

Therefore there exists

\[
s_0\in[-2\delta,-\delta]
\]

such that

\[
\boxed{
P(s_0)
\le
C
\frac{M_E}{\nu}
\left(
\frac1\delta+1
\right).
}
\]

Thus one does not need an a-priori `H1` bound at the left edge of the normalized window.

---

## 4. Second-derivative energy identity

The vorticity equation is

\[
\partial_s\Omega
+U\cdot\nabla\Omega
=\Omega\cdot\nabla U
+\nu\Delta\Omega.
\]

Multiply by `-Delta Omega` and integrate over `R3`.  Let

\[
Z(s)=\|\Delta\Omega(s)\|_2^2.
\]

Then

\[
\frac12P'(s)+\nu Z(s)
=I_{\rm adv}+I_{\rm str}.
\]

For the advection term, incompressibility removes the pure transport derivative and leaves

\[
|I_{\rm adv}|
\le
\|\nabla U\|_3
\|\nabla\Omega\|_3^2.
\]

Calderon--Zygmund and `L2-Linfinity` interpolation give

\[
\|\nabla U\|_3
\le C\|\Omega\|_3
\le
C M_E^{1/3}.
\]

Also

\[
\|\nabla\Omega\|_3^2
\le
C
\|\nabla\Omega\|_2
\|\nabla\Omega\|_6
\le
C P^{1/2}Z^{1/2},
\]

using

\[
\|\nabla\Omega\|_6
\le C\|\nabla^2\Omega\|_2
=C Z^{1/2}
\]

in the whole space.

Therefore

\[
\boxed{
|I_{\rm adv}|
\le
\frac\nu4Z
+C\nu^{-1}M_E^{2/3}P.
}
\]

For stretching,

\[
|I_{\rm str}|
\le
\|\Omega\|_\infty
\|\nabla U\|_2
Z^{1/2}
\le
C M_E^{1/2}Z^{1/2}.
\]

Hence

\[
\boxed{
|I_{\rm str}|
\le
\frac\nu4Z
+C\nu^{-1}M_E.
}
\]

Combining,

\[
\boxed{
P'(s)
+\nu Z(s)
\le
C\nu^{-1}
\left[
M_E^{2/3}P(s)+M_E
\right].
}
\]

---

## 5. Gronwall bootstrap

Start the differential inequality at the good time `s0`.  Since

\[
s_0\le-\delta,
\]

the interval `[ -delta,0 ]` lies strictly inside the evolution range from `s0` to zero.

Gronwall gives

\[
\boxed{
\sup_{-\delta\le s\le0}
P(s)
\le
C_{M_E,\nu,\delta}.
}
\]

Integrating the same inequality gives

\[
\boxed{
\int_{-\delta}^{0}
Z(s)ds
=\int_{-\delta}^{0}
\|\Delta\Omega(s)\|_2^2ds
\le
C_{M_E,\nu,\delta}.
}
\]

Thus the normalized terminal subwindow has an automatic V2 reserve.

---

## 6. Compactness consequence

The earlier V2 compactness lemma now applies automatically on this branch.  In particular, after localization to fixed interior balls,

\[
\Omega_j
\text{ is bounded in }
L_s^2H_y^2
\]

and

\[
\partial_s\Omega_j
\text{ is bounded in an appropriate negative Sobolev space}.
\]

Hence a subsequence is strongly compact in

\[
\boxed{
L_s^2H_{y,\rm loc}^1
}
\]

on a smaller fixed terminal cylinder.

Therefore the old branch

\[
\text{bounded global normalized enstrophy but unbounded terminal V2}
\]

is removed on first-hitting windows of noncollapsed duration.

---

## 7. Updated compactness dichotomy

The compactness route simplifies to

\[
\boxed{
\sup_{s\in I_j}\|\Omega_j(s)\|_2^2\to\infty
}
\]

or, after a subsequence,

\[
\boxed{
\sup_{s\in I_j}\|\Omega_j(s)\|_2^2\le M_E
\Longrightarrow
\text{automatic terminal }H^1/V2\text{ bound and strong local compactness}.
}
\]

Thus **normalized global-enstrophy concentration** becomes the principal compactness failure channel; V2 concentration is no longer independent on the bounded first-hitting branch.

---

## 8. Claim boundary

The lemma assumes the normalized global enstrophy is bounded throughout the chosen fixed backward interval.  It does not prove that this channel is automatically bounded for every hypothetical blowup sequence.

It also works on the smooth lifespan before the hypothetical first singular time, which is exactly the regime of the amplification checkpoints.

Status: **V2 BOOTSTRAP CLOSED ON BOUNDED FIRST-HITTING ENSTROPHY WINDOWS**.
