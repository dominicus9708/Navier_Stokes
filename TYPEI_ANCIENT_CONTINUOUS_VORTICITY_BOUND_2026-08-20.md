# Continuous Backward Type-I Vorticity Bound in the Restricted Ancient Limit — 2026-08-20

Overall status: **ANCIENT-LIMIT CONSTRAINT STRENGTHENED — GLOBAL REGULARITY NOT PROVED.**

The previous first-hitting inheritance note recorded a geometric sequence of backward times at which the rescaled vorticity obeys `||Omega||_infty ~ 1/|tau|`. On the non-`H/T`, `P_V`-recurrent branch, the uniform upper and lower bounds on normalized stage lengths upgrade this sequence estimate to a bound for every sufficiently negative time.

---

## 1. Stage geometry

Let

\[
W_k=q^kW_0,
\]

and let `t_k` be the first time at which `||omega||_infty=W_k`. On the non-`H/T` recurrent branch assume

\[
0<L_-\le L_k\le L_+<\infty,
\]

where

\[
L_k=\int_{t_k}^{t_{k+1}}W(t)dt.
\]

Since

\[
W_k\le W(t)\le qW_k
\qquad(t_k\le t\le t_{k+1}),
\]

we have

\[
\frac{L_-}{qW_k}
\le t_{k+1}-t_k
\le\frac{L_+}{W_k}.
\]

Consequently the remaining time to the putative blowup satisfies

\[
\boxed{
\frac{c_-}{W_k}
\le T^*-t_k
\le\frac{c_+}{W_k}
}
\]

with constants depending only on `q,L_-,L_+`.

---

## 2. Pointwise-in-time Type-I vorticity bound before blowup

Take any sufficiently late time `t<T^*` and choose `k` with

\[
t_k\le t<t_{k+1}.
\]

Then by first hitting,

\[
W(t)<W_{k+1}=qW_k.
\]

Also

\[
T^*-t\le T^*-t_k\le\frac{c_+}{W_k}.
\]

Therefore

\[
\boxed{
(T^*-t)W(t)\le qc_+.
}
\]

A lower bound is not asserted at every time because `W(t)` may fluctuate downward inside a stage; the upper Type-I bound is the robust consequence needed here.

Thus the non-`H/T` recurrent branch satisfies the vorticity Type-I estimate

\[
\boxed{
\sup_{t_0<t<T^*}(T^*-t)\|\omega(t)\|_\infty<\infty.
}
\]

---

## 3. Passage to the fixed-center ancient scaling

Fix a late stage `j` and rescale around the limiting center `X_*` by

\[
U_j(y,\tau)=r_ju(X_*+r_jy,t_j+r_j^2\tau),
\qquad
r_j=W_j^{-1/2},
\]

\[
\Omega_j(y,\tau)=r_j^2\omega(X_*+r_jy,t_j+r_j^2\tau).
\]

For a backward time `tau<0`, the corresponding physical time is

\[
t=t_j+r_j^2\tau.
\]

The Type-I estimate above gives, after multiplication by `r_j^2`,

\[
\|Ω_j(\tau)\|_\infty
\le
\frac{C}{W_j(T^*-t)}.
\]

For `tau` sufficiently negative compared with the O(1) forward distance from `t_j` to `T^*` in stage-j units,

\[
W_j(T^*-t)
=W_j(T^*-t_j)-\tau
\asymp |\tau|.
\]

Hence

\[
\boxed{
\|Ω_j(\tau)\|_\infty
\le\frac{C}{|\tau|}
\qquad(\tau\le-\tau_0),
}
\]

uniformly in late `j`.

Any locally compact ancient limit therefore satisfies

\[
\boxed{
\sup_{\tau\le-\tau_0}
|\tau|\,\|Ω_\infty(\tau)\|_\infty<\infty.
}
\]

This upgrades the earlier discrete backward sequence to a continuous backward Type-I vorticity bound.

---

## 4. Logarithmic self-similar variables

For an ancient limit on `tau<0`, define

\[
z=-\log(-\tau),
\qquad
y=x/\sqrt{-\tau},
\]

\[
V(y,z)=\sqrt{-\tau}\,U(x,\tau),
\]

\[
\Xi(y,z)=(-\tau)\Omega(x,\tau).
\]

Then `V` solves the Leray-rescaled equation

\[
\boxed{
\partial_zV
+\frac12V
+\frac12y\cdot\nabla V
+(V\cdot\nabla)V
=-\nabla\Pi+\nu\Delta V,
\qquad\nabla\cdot V=0.
}
\]

The continuous Type-I vorticity estimate becomes

\[
\boxed{
\sup_{z\le z_0}\|\Xi(z)\|_\infty<\infty.
}
\]

The first-hitting stage times satisfy

\[
z_{m+1}-z_m=-\log q+O(1)
\]

with uniformly bounded spacing errors determined by `L_-/L_+`, and the corresponding rescaled vorticity amplitudes remain order one along a backward sequence.

Thus the restricted ancient candidate becomes a bounded/precompact backward orbit of the Leray flow in the non-`H/T` regime, rather than an arbitrary ancient solution.

---

## 5. What this does and does not prove

The estimate

\[
\sup_{\tau<0}|\tau|\|\Omega(\tau)\|_\infty<\infty
\]

is a Type-I vorticity bound, not by itself a known general 3D Liouville condition. It is compatible with the broad Type-I problem and therefore does not close global regularity alone.

Its value in the present route is that it supplies a uniform scale-invariant vorticity cap in logarithmic variables, to be combined with the extra `P_V`, covariance-saturation, middle-axis, and projection-kernel restrictions already derived.

Status: **THE RESTRICTED NON-H/T ANCIENT CANDIDATE HAS A CONTINUOUS BACKWARD TYPE-I VORTICITY BOUND, NOT MERELY A DISCRETE ONE. IN LERAY VARIABLES ITS RESCALED VORTICITY IS UNIFORMLY BOUNDED BACKWARD IN LOGARITHMIC TIME.**