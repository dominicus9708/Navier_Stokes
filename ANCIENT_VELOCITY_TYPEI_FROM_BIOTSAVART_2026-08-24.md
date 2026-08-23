# Ancient Velocity Type-I Bound from Biot–Savart — 2026-08-24

Status: **GLOBAL VELOCITY TYPE-I DECAY FOR THE RESTRICTED ANCIENT CLASS / LOW-FREQUENCY L3 TAIL STILL POSSIBLE / GLOBAL REGULARITY NOT PROVED.**

The restricted ancient survivor already satisfies

\[
\|\Omega(\tau)\|_\infty\lesssim |\tau|^{-1},
\qquad
\|\Omega(\tau)\|_2\lesssim |\tau|^{-1/4}.
\]

A direct Biot–Savart split converts these two vorticity bounds into the full velocity Type-I amplitude bound

\[
\|U(\tau)\|_\infty\lesssim |\tau|^{-1/2}.
\]

---

## 1. Biot–Savart split

For smooth decaying divergence-free velocity,

\[
U(x)
=\frac1{4\pi}\int_{\mathbb R^3}
\frac{\Omega(y)\times(x-y)}{|x-y|^3}\,dy.
\]

Therefore

\[
|U(x)|
\le C\int\frac{|\Omega(y)|}{|x-y|^2}dy.
\]

Split at radius `R>0`.

For the near field,

\[
\int_{|x-y|<R}\frac{|\Omega(y)|}{|x-y|^2}dy
\le
C\|\Omega\|_\infty R.
\]

For the far field, Cauchy–Schwarz gives

\[
\begin{aligned}
\int_{|x-y|>R}\frac{|\Omega(y)|}{|x-y|^2}dy
&\le
\|\Omega\|_2
\left(\int_{|z|>R}|z|^{-4}dz\right)^{1/2}\\
&\le C\|\Omega\|_2R^{-1/2}.
\end{aligned}
\]

Hence

\[
\boxed{
\|U\|_\infty
\le C\left(
\|\Omega\|_\infty R
+\|\Omega\|_2R^{-1/2}
\right).
}
\]

---

## 2. Optimize the split radius

Balance the two terms:

\[
\|\Omega\|_\infty R
\sim
\|\Omega\|_2R^{-1/2}.
\]

Thus

\[
R^{3/2}
\sim
\frac{\|\Omega\|_2}{\|\Omega\|_\infty},
\]

or

\[
R
\sim
\left(
\frac{\|\Omega\|_2}{\|\Omega\|_\infty}
\right)^{2/3}.
\]

Substitution gives the scale-sharp inequality

\[
\boxed{
\|U\|_\infty
\le C_{BS,0}
\|\Omega\|_\infty^{1/3}
\|\Omega\|_2^{2/3}.
}
\]

This is exactly scale invariant.

---

## 3. Insert the ancient decay rates

Use

\[
\|\Omega(\tau)\|_\infty
\le K_I|\tau|^{-1}
\]

and

\[
\|\Omega(\tau)\|_2^2
\le Z_+K_I^{1/2}|\tau|^{-1/2}.
\]

Therefore

\[
\|\Omega(\tau)\|_2
\le Z_+^{1/2}K_I^{1/4}|\tau|^{-1/4}.
\]

The optimized Biot–Savart bound becomes

\[
\boxed{
\|U(\tau)\|_\infty
\le
C_{BS,0}
Z_+^{1/3}K_I^{1/2}
|\tau|^{-1/2}.
}
\]

Thus the ancient survivor has a continuous global velocity Type-I bound.

---

## 4. Full p>=6 velocity decay

The global Sobolev bound already gives

\[
\|U(\tau)\|_6
\lesssim |\tau|^{-1/4}.
\]

Interpolating `L6` with `L∞`, for every `6<=p<=∞`,

\[
\boxed{
\|U(\tau)\|_p
\lesssim
|\tau|^{-\left(\frac12-\frac{3}{2p}\right)}.
}
\]

This is exactly the Navier–Stokes Type-I scaling for velocity in `Lp`.

In particular,

\[
|\tau|^{1/2-3/(2p)}\|U(\tau)\|_p
\le C_p
\]

uniformly backward.

---

## 5. Mild bounded ancient status

For every `tau<0`, the velocity is globally bounded.  On every compact negative-time interval, smoothness/local compactness gives the standard mild representation.  Hence the restricted limit lies in the bounded-mild-ancient framework used in Type-I blowup theory.

The Albritton–Barker Type-I equivalence theorem is therefore structurally aligned with this class.  Their separate Liouville theorem still needs a global `L3` bound along a backward sequence; the present estimates do **not** supply that low-frequency condition.

---

## 6. Why the critical 1/r tail remains compatible

The model

\[
|U(y,\tau)|\sim |y|^{-1}
\quad\text{for }|y|\gtrsim\sqrt{|\tau|}
\]

has

\[
\|U(\tau)\|_\infty
\sim |\tau|^{-1/2}
\]

at the inner edge of the tail and

\[
\|U(\tau)\|_6
\sim |\tau|^{-1/4}.
\]

Thus it exactly saturates both newly derived velocity bounds while remaining logarithmically non-integrable in global `L3`.

So the velocity Type-I estimate is a genuine strengthening of the ancient class, but it does not by itself remove the final low-frequency obstruction.

---

## 7. Similarity-variable consequence

Let

\[
T=-\tau,
\qquad
Y=y/\sqrt T,
\qquad
s=-\log T,
\]

and define the Leray velocity and vorticity

\[
V(Y,s)=\sqrt T\,U(y,\tau),
\qquad
W(Y,s)=T\,\Omega(y,\tau).
\]

Then the ancient decay estimates become uniform similarity bounds

\[
\boxed{
\sup_s\left(
\|V(s)\|_\infty
+\|V(s)\|_6
+\|W(s)\|_\infty
+\|W(s)\|_2
\right)<\infty.
}
\]

Thus the final ancient problem may be reformulated as a bounded complete trajectory of the autonomous Leray system, with an active core precompact in similarity radius and a possible critical `1/|Y|` tail.

---

## 8. Literature boundary

Known nonexistence results rule out exact backward self-similar Leray profiles under broad integrability assumptions, including `Lp` profiles with `p>=3` and several Lorentz/Morrey classes.  In particular, a **stationary** similarity profile lying in `L6` would fall in the classical nonexistence regime.

The current survivor, however, is only a bounded recurrent/nonstationary Leray trajectory.  A bounded autonomous trajectory need not have a stationary alpha-limit point.  Therefore one must not replace recurrent compactness by stationarity without an additional Lyapunov/rigidity argument.

Status: **THE RESTRICTED ANCIENT LIMIT HAS THE FULL CONTINUOUS VELOCITY TYPE-I DECAY `||U(t)||∞ <= C/sqrt(|t|)` AND THE CORRESPONDING `Lp` TYPE-I RATES FOR ALL `p>=6`. IN LERAY VARIABLES THIS BECOMES A UNIFORMLY BOUNDED TRAJECTORY IN `L6 cap L∞` WITH VORTICITY IN `L2 cap L∞`. EXACT STATIONARY SELF-SIMILAR PROFILES IN THIS INTEGRABILITY RANGE ARE KNOWN TO BE TRIVIAL, BUT THE REMAINING RECURRENT NONSTATIONARY LERAY-ORBIT RIGIDITY IS NOT YET PROVED. GLOBAL REGULARITY REMAINS UNPROVED.**