# Pineau–Vicol Local Type-I / One-Slice Recurrence Gate — 2026-08-24

Status: **EXTERNAL 2026 REGULARITY INPUT + EXACT SCOPE AUDIT / GLOBAL REGULARITY NOT PROVED.**

This note imports Theorem 1.9 and Remark 1.11 of Pineau–Vicol, arXiv:2607.09619v2 (revised 2026-08-06), and records precisely what the present first-hitting/Leray route must still prove before that theorem can be used.

## 1. External theorem

Let `(u,p)` be smooth on

\[
B_1\times[-1,0)
\]

and suppose the local spatial Type-I bound

\[
\boxed{
|u(x,t)|\le \frac{C_u}{\sqrt{-t}+|x|}
}
\]

holds on the unit parabolic cylinder. Assume also a pressure bound on the fixed annulus

\[
A=\{1/2<|x|<3/4\}:
\qquad
|p(x,t)|\le C_p.
\]

Then there are constants

\[
\delta_0=\delta_0(C_u)>0,
\qquad
s_0=s_0(C_u,C_p)
\]

such that if at one time `bar t=-exp(-bar s)` with `bar s>=s0`,

\[
\sqrt{-\bar t}\,
\left\|
(-\bar t)\partial_tu
-\frac12u
-\frac12(x\cdot\nabla)u
\right\|_{L^\infty(B_1)}
\le\delta_0,
\]

then `(0,0)` is a regular point.

In self-similar variables

\[
V(Y,s)=\sqrt{-t}\,u(x,t),
\qquad Y=x/\sqrt{-t},
\qquad s=-\log(-t),
\]

this condition is exactly

\[
\boxed{
\|\partial_sV(\cdot,\bar s)\|_{L^\infty(B_{e^{\bar s/2}})}
\le\delta_0.
}
\]

Pineau–Vicol also state that the proof still works under the weaker Gaussian-weighted condition

\[
\boxed{
\int_{B_{e^{\bar s/2}}}
|\partial_sV(Y,\bar s)|(1+|Y|)e^{-|Y|^2/8}\,dY
\lesssim\delta_0.
}
\]

## 2. What recurrence does not give automatically

The present route produces a nonzero recurrent bounded Leray trajectory. Recurrence means that for suitable return times `T_n`,

\[
V(s+T_n)\to V(s)
\]

locally.

This does **not** imply

\[
\partial_sV(s_n)\to0.
\]

A periodic rigid rotation is the elementary counterexample: the state returns while its phase-space speed stays bounded away from zero.

Therefore Theorem 1.9 cannot be invoked merely from recurrence.

## 3. The actual speed-floor consequence

Suppose the two spatial hypotheses of Theorem 1.9 are verified for the candidate singular cylinder:

1. `|u| <= C_u/(sqrt(-t)+|x|)`;
2. the annular pressure is bounded.

Then a singular recurrent survivor must satisfy, for every sufficiently late Leray time `s`,

\[
\boxed{
\|\partial_sV(s)\|_{L^\infty(B_{e^{s/2}})}
>\delta_0,
}
\]

or, using the weaker version,

\[
\boxed{
\int
|\partial_sV(Y,s)|(1+|Y|)e^{-|Y|^2/8}\,dY
\gtrsim\delta_0.
}
\]

Thus once the spatial Type-I tail is proved, every surviving recurrent orbit has a **uniform nonzero Leray-speed floor**. The stationary limit is excluded immediately, and slow recurrence is excluded as well.

## 4. Important mismatch with the current velocity estimate

The current ancient calculation gives only the temporal Type-I estimate

\[
\boxed{
\|U(\tau)\|_\infty\lesssim |\tau|^{-1/2},
}
\]

which becomes

\[
\|V(s)\|_\infty\le C.
\]

This is weaker than Pineau–Vicol's spatial Type-I hypothesis. Their bound is equivalent in Leray variables to

\[
\boxed{
|V(Y,s)|\le \frac{C_u}{1+|Y|}
}
\]

through the expanding ball corresponding to `B_1`.

Therefore no unconditional import is made here.

## 5. New precise tail target

The external theorem identifies the exact spatial estimate worth proving next:

\[
\boxed{
|V(Y,s)|\lesssim (1+|Y|)^{-1}
}
\]

uniformly on late recurrent times, together with the pressure annulus bound.

The previously derived critical shell picture suggests precisely this borderline decay, but `V in L^6 cap L^infty` alone does not imply it.

Hence the remaining tail bridge is not merely `L^3` divergence. It is the dichotomy

\[
\boxed{
\text{spatial Type-I }1/r\text{ tail}
\quad\lor\quad
\text{supercritical annular vorticity/derivative concentration}.
}
\]

If the first branch holds, Pineau–Vicol converts singular recurrence into a uniform Leray-speed floor. The second branch must be routed to the existing vorticity/derivative remote-tail ledgers.

## 6. Relation to rotated self-similar results

The same paper proves that a globally rotated self-similar profile satisfying

\[
|V(Y)|\lesssim(1+|Y|)^{-1}
\]

is trivial when its constant angular speed is sufficiently small or sufficiently large; only intermediate angular speed remains open. Thus, once the spatial Type-I tail is supplied, rigidly rotating recurrent subcases can also import their RSS theorem.

Status: **THE 2026 ONE-SLICE REGULARITY THEOREM DOES NOT FOLLOW FROM RECURRENCE ALONE. IT BECOMES AVAILABLE AFTER A BORDERLINE SPATIAL TYPE-I TAIL AND PRESSURE-ANNULUS BOUND ARE PROVED. UNDER THOSE INPUTS, ANY SINGULAR RECURRENT SURVIVOR MUST MAINTAIN A UNIFORM POSITIVE SELF-SIMILAR-TIME SPEED AT EVERY SUFFICIENTLY LATE TIME.**