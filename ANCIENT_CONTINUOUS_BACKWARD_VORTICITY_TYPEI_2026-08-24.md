# Ancient Continuous Backward Vorticity Type-I Bound — 2026-08-24

Status: **FIRST-HITTING INHERITANCE STRENGTHENED FROM A SEQUENCE TO ALL BACKWARD TIMES / GLOBAL REGULARITY NOT PROVED.**

This note strengthens `TYPEI_ANCIENT_FIRST_HITTING_INHERITANCE_2026-08-20.md`.

The earlier note recorded only a geometric sequence `tau_m -> -infinity` with

\[
\|\Omega(\tau_m)\|_\infty\lesssim|\tau_m|^{-1}.
\]

The first-hitting property actually gives the same critical decay, with a uniform constant, on **every time between consecutive backward checkpoints**.

---

## 1. Backward first-hitting times

Let

\[
W_j=q^jW_0,
\qquad
r_j=W_j^{-1/2},
\]

and in the fixed stage-`j` scaling define

\[
\tau_{j,m}
=W_j(t_{j-m}-t_j)<0.
\]

Assume the recurrent stage lengths satisfy

\[
0<L_-\le L_k\le L_+<\infty.
\]

The physical stage duration obeys

\[
\frac{L_k}{qW_k}
\le
\Delta t_k
\le
\frac{L_k}{W_k}.
\]

Hence

\[
|\tau_{j,m}|
=W_j\sum_{k=j-m}^{j-1}\Delta t_k.
\]

Using `W_j/W_{j-l}=q^l`,

\[
|\tau_{j,m}|
\le
L_+\sum_{l=1}^{m}q^l
\le
\boxed{
c_+q^m}
\]

with

\[
\boxed{
c_+=\frac{L_+q}{q-1}.}
\]

Likewise,

\[
|\tau_{j,m}|
\ge
\frac{L_-}{q}\sum_{l=1}^{m}q^l
\ge
\boxed{
c_-q^m}
\]

with one convenient choice

\[
\boxed{
c_-=rac{L_-}{q}.}
\]

Thus

\[
c_-q^m\le|\tau_{j,m}|\le c_+q^m.
\]

---

## 2. First-hitting cap between checkpoints

Take a time

\[
\tau\in[\tau_{j,m+1},\tau_{j,m}].
\]

This corresponds to a physical time no later than `t_{j-m}`.  Because `t_{j-m}` is the **first** time the vorticity maximum reaches `W_{j-m}`,

\[
W(t)\le W_{j-m}.
\]

Therefore in the stage-`j` scaling,

\[
\boxed{
\|\Omega_j(\tau)\|_\infty
\le
\frac{W_{j-m}}{W_j}
=q^{-m}.
}
\]

This holds on the whole slab between consecutive geometric checkpoint times, not only at the endpoint.

---

## 3. Convert the slab cap to 1/|tau|

For

\[
\tau\in[\tau_{j,m+1},\tau_{j,m}],
\]

we also have

\[
|\tau|
\le
|\tau_{j,m+1}|
\le
c_+q^{m+1}.
\]

Hence

\[
q^{-m}
\le
\frac{c_+q}{|\tau|}.
\]

Combining with the first-hitting cap gives

\[
\boxed{
\|\Omega_j(\tau)\|_\infty
\le
\frac{K_I}{|\tau|}
}
\]

for all backward slabs away from the terminal `O(1)` interval, where

\[
\boxed{
K_I=c_+q
=\frac{L_+q^2}{q-1}.
}
\]

Together with the global first-hitting cap `||Omega_j||_infty<=1`, one may write the convenient global form

\[
\boxed{
\|\Omega_j(\tau)\|_\infty
\le
\min\left\{1,\frac{K_I}{|\tau|}\right\}
}
\]

on the whole backward tower, after harmless adjustment of the constant on the first finite number of slabs.

---

## 4. Passage to the ancient limit

Under the local compactness/strong-vorticity passage established on the no-H/tight corridor, the estimate passes to the ancient limit:

\[
\boxed{
\|\Omega_\infty(\tau)\|_\infty
\le
\min\left\{1,\frac{K_I}{|\tau|}\right\}
\qquad(\tau<0).
}
\]

Thus the restricted ancient survivor has a **continuous backward Type-I vorticity bound**, not merely a Type-I sequence.

In particular,

\[
\boxed{
\|\Omega_\infty(\tau)\|_\infty\to0
\qquad(\tau\to-\infty).
}
\]

---

## 5. Combine with the uniform global enstrophy bound

From `ANCIENT_LOCAL_COMPACTNESS_FROM_ENSTROPHY_TIGHTNESS_2026-08-24.md`, the limit also inherits

\[
\boxed{
\sup_{\tau<0}\|\Omega_\infty(\tau)\|_2^2
\le Z_+.
}
\]

Interpolation therefore gives, for every `2<=p<=infinity`,

\[
\boxed{
\|\Omega_\infty(\tau)\|_p
\le
Z_+^{1/p}
\left(\frac{K_I}{|\tau|}\right)^{1-2/p}
}
\]

for sufficiently negative `tau`.

In particular,

\[
\boxed{
\|\Omega_\infty(\tau)\|_3^3
\le
Z_+\frac{K_I}{|\tau|}.
}
\]

The same `L3` estimate holds for the strain up to the standard Riesz-transform constant.

---

## 6. Criticality of the remaining enstrophy production

The vorticity enstrophy production satisfies

\[
\left|
\int S:(\Omega\otimes\Omega)
\right|
\le
\|S\|_3\|\Omega\|_3^2
\le
C_R\|\Omega\|_3^3.
\]

Therefore the restricted ancient survivor obeys

\[
\boxed{
\left|
\int S:(\Omega\otimes\Omega)
\right|
\lesssim
\frac{Z_+K_I}{|\tau|}
}
\]

as `tau -> -infinity`.

This is exactly critical: `1/|tau|` is only logarithmically nonintegrable backward.  Thus the new decay substantially narrows the ancient class but does not by itself force zero enstrophy.

---

## 7. Why this matters for the Liouville endgame

The ancient survivor now satisfies simultaneously

\[
\boxed{
\sup_{\tau<0}\|\Omega(\tau)\|_2<\infty,
}
\]

\[
\boxed{
\|\Omega(\tau)\|_\infty
\lesssim|\tau|^{-1},
}
\]

and terminal nontriviality

\[
|\Omega(y_*,0)|=1.
\]

Any nontrivial survivor must therefore evade rigidity through the critical borderline between

- uniformly finite global enstrophy;
- vanishing backward vorticity amplitude;
- and possible increasingly large low-frequency/large-scale velocity support.

This matches the existing `ANCIENT_L3_TAIL_NECESSITY_2026-08-20.md`: the only remaining way to avoid the global-`L3` ancient Liouville theorem is a backward-growing low-frequency/critical velocity tail.

---

## 8. Updated restricted ancient target

The final ancient target is stronger than previously recorded:

\[
\boxed{
\begin{gathered}
U\text{ ancient suitable/mild},\\
|\Omega(y_*,0)|=1,\\
\sup_{\tau<0}\|\Omega(\tau)\|_2^2\le Z_+,\\
\|\Omega(\tau)\|_\infty
\le\min\{1,K_I/|\tau|\},\\
\text{plus the inherited no-turnover/projective restrictions.}
\end{gathered}
}
\]

The remaining Liouville obstruction is now explicitly a **critical low-frequency velocity-tail problem**, not a generic bounded-ancient-solution problem.

Status: **FIRST-HITTING CONTROL BETWEEN GEOMETRIC CHECKPOINTS UPGRADES THE ANCIENT INHERITANCE FROM A BACKWARD `1/|t|` SEQUENCE TO A CONTINUOUS `||Omega(t)||_infinity <= K_I/|t|` BOUND. COMBINED WITH UNIFORM GLOBAL ENSTROPHY, ALL VORTICITY Lp NORMS WITH `p>2` DECAY BACKWARD AT EXPLICIT RATES. THE REMAINING ANCIENT OBSTRUCTION IS CRITICAL AND LOW-FREQUENCY. GLOBAL REGULARITY REMAINS UNPROVED.**