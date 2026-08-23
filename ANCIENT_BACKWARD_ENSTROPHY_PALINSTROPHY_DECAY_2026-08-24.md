# Ancient Backward Enstrophy / Palinstrophy Decay — 2026-08-24

Status: **BACKWARD DECAY STRENGTHENING OF THE RESTRICTED ANCIENT CLASS / CRITICAL LOW-FREQUENCY TAIL REMAINS / GLOBAL REGULARITY NOT PROVED.**

This note sharpens `ANCIENT_CONTINUOUS_BACKWARD_VORTICITY_TYPEI_2026-08-24.md` by retaining the scaling factor that was discarded in the first local-compactness estimate.

The result is a genuine decay of the ancient global enstrophy, not merely a uniform bound.

---

## 1. Fixed-scale enstrophy retains the dynamic scale ratio

At physical time `t<=t_j`, let

\[
M(t)=\|\omega(t)\|_\infty.
\]

On the vorticity-tight dynamic corridor,

\[
Z_{dyn}(t)
=M(t)^{-1/2}\|\omega(t)\|_2^2
\le Z_+.
\]

In the fixed stage-`j` scaling,

\[
\|\Omega_j(\tau)\|_2^2
=W_j^{-1/2}\|\omega(t)\|_2^2
=
\left(\frac{M(t)}{W_j}\right)^{1/2}Z_{dyn}(t).
\]

Therefore

\[
\boxed{
\|\Omega_j(\tau)\|_2^2
\le
Z_+
\left(\frac{M(t)}{W_j}\right)^{1/2}.
}
\]

---

## 2. First-hitting slabs convert the scale ratio to backward time

For

\[
\tau\in[\tau_{j,m+1},\tau_{j,m}],
\]

the first-hitting cap gives

\[
\frac{M(t)}{W_j}
\le q^{-m}.
\]

The previous continuous Type-I calculation gives

\[
q^{-m}
\le
\frac{K_I}{|\tau|},
\qquad
K_I=rac{L_+q^2}{q-1}.
\]

Hence

\[
\boxed{
\|\Omega_j(\tau)\|_2^2
\le
Z_+
\left(\frac{K_I}{|\tau|}\right)^{1/2}.
}
\]

Passing to the ancient limit yields

\[
\boxed{
\|\Omega(\tau)\|_2^2
\le
Z_+K_I^{1/2}|\tau|^{-1/2}
}
\]

for sufficiently negative `tau`.

Thus

\[
\boxed{
\|\Omega(\tau)\|_2
\lesssim
|\tau|^{-1/4}.
}
\]

In particular,

\[
\boxed{
\|\Omega(\tau)\|_2\to0
\qquad(\tau\to-\infty).
}
\]

---

## 3. Backward decay of the global H1 velocity norm

For divergence-free decaying velocity,

\[
\|\nabla U\|_2^2
=\|\Omega\|_2^2.
\]

Therefore

\[
\boxed{
\|\nabla U(\tau)\|_2
\lesssim
|\tau|^{-1/4}.
}
\]

The whole-space Sobolev inequality gives

\[
\boxed{
\|U(\tau)\|_6
\lesssim
|\tau|^{-1/4}.
}
\]

So the ancient velocity converges to zero backward in the global critical-homogeneous `H1`/`L6` sense.

---

## 4. Improved Lp vorticity decay

Combine

\[
\|\Omega(\tau)\|_2
\lesssim |\tau|^{-1/4}
\]

with

\[
\|\Omega(\tau)\|_\infty
\lesssim |\tau|^{-1}.
\]

For `2<=p<=infinity`, interpolation gives

\[
\boxed{
\|\Omega(\tau)\|_p
\lesssim
|\tau|^{-\left(1-\frac{3}{2p}\right)}.
}
\]

In particular,

\[
\boxed{
\|\Omega(\tau)\|_3
\lesssim
|\tau|^{-1/2},
}
\]

and therefore

\[
\boxed{
\|\Omega(\tau)\|_3^3
\lesssim
|\tau|^{-3/2}.
}
\]

This improves the previous crude `1/|tau|` bound for the cubic vorticity quantity.

---

## 5. Backward integrability of nonlinear enstrophy production

Riesz boundedness gives

\[
\|S\|_3
\le C_R\|\Omega\|_3.
\]

Hence

\[
\left|
\int S:(\Omega\otimes\Omega)dy
\right|
\le
\|S\|_3\|\Omega\|_3^2
\le
C_R\|\Omega\|_3^3.
\]

Therefore

\[
\boxed{
\left|
\int S:(\Omega\otimes\Omega)dy
\right|
\lesssim
|\tau|^{-3/2}.
}
\]

Since

\[
\int_{-\infty}^{-1}|\tau|^{-3/2}d\tau<\infty,
\]

the ancient nonlinear enstrophy production is absolutely integrable at backward infinity.

This is a substantial strengthening over the earlier logarithmic borderline estimate.

---

## 6. Backward palinstrophy budget

The ancient enstrophy identity is

\[
\frac12\frac d{d\tau}\|\Omega\|_2^2
+
u\|\nabla\Omega\|_2^2
=
\int S:(\Omega\otimes\Omega)dy.
\]

Because

\[
\|\Omega(\tau)\|_2^2\to0
\qquad(\tau\to-\infty)
\]

and the production is backward integrable, integration from `-infinity` to `-T` gives

\[
\boxed{
\frac12\|\Omega(-T)\|_2^2
+
u\int_{-\infty}^{-T}
\|\nabla\Omega(\tau)\|_2^2d\tau
\le
C T^{-1/2}.
}
\]

Consequently

\[
\boxed{
\int_{-\infty}^{-T}
\|\nabla\Omega(\tau)\|_2^2d\tau
\lesssim
T^{-1/2}.
}
\]

Thus the ancient solution has finite total backward palinstrophy and the remote backward tail of that budget tends to zero.

---

## 7. Dyadic-time palinstrophy decay sequence

On a dyadic backward interval

\[
[-2T,-T],
\]

the preceding bound gives

\[
\int_{-2T}^{-T}
\|\nabla\Omega(\tau)\|_2^2d\tau
\lesssim T^{-1/2}.
\]

Therefore there exists

\[
\tau_T\in[-2T,-T]
\]

such that

\[
\boxed{
\|\nabla\Omega(\tau_T)\|_2^2
\lesssim T^{-3/2}.
}
\]

Equivalently,

\[
\boxed{
\|\nabla\Omega(\tau_T)\|_2
\lesssim T^{-3/4}.
}
\]

This is the natural derivative scaling of the critical shell model.

---

## 8. Critical-shell saturation

Consider the schematic backward tail

\[
|U(r,\tau)|\sim r^{-1},
\qquad
|\Omega(r,\tau)|\sim r^{-2},
\]

starting at the natural radius

\[
r\sim\sqrt{|\tau|}.
\]

Then

\[
\int_{r\gtrsim\sqrt{|\tau|}}|\Omega|^2
\sim |\tau|^{-1/2},
\]

and

\[
\int_{r\gtrsim\sqrt{|\tau|}}|\nabla\Omega|^2
\sim |\tau|^{-3/2}.
\]

Thus the newly derived ancient enstrophy and palinstrophy rates are **exactly saturated** by the same critical `U~1/r` shell tail that makes the global `L3` velocity norm logarithmically divergent.

This identifies the final obstruction sharply: the remaining tail is not an artifact of weak estimates; it sits at the exact scaling boundary of all currently available ancient decay budgets.

---

## 9. Updated ancient rigidity target

Any nontrivial survivor must now satisfy all of

\[
\boxed{
\begin{aligned}
\|\Omega(\tau)\|_\infty&\lesssim|\tau|^{-1},\\
\|\Omega(\tau)\|_2^2&\lesssim|\tau|^{-1/2},\\
\|U(\tau)\|_6&\lesssim|\tau|^{-1/4},\\
\int_{-\infty}^{-T}\|\nabla\Omega\|_2^2d\tau&\lesssim T^{-1/2},
\end{aligned}
}
\]

while remaining nonzero at `tau=0`.

No general three-dimensional Liouville theorem located in the current literature search directly covers this class without an additional global low-frequency/velocity condition.  The known Albritton-Barker `L3`-sequence theorem would close the branch if one could rule out the critical low-frequency `1/r` velocity tail.

Status: **THE RESTRICTED ANCIENT SURVIVOR NOW DECAYS TO ZERO BACKWARD IN GLOBAL ENSTROPHY AND L6 VELOCITY, AND HAS FINITE BACKWARD PALINSTROPHY. ALL THESE RATES ARE EXACTLY SATURATED BY A `U~1/r`, `OMEGA~1/r^2` CRITICAL SHELL TAIL. THE FINAL RIGIDITY PROBLEM IS THEREFORE SHARPENED TO EXCLUDING OR NEUTRALIZING THIS LOW-FREQUENCY CRITICAL TAIL. GLOBAL REGULARITY REMAINS UNPROVED.**