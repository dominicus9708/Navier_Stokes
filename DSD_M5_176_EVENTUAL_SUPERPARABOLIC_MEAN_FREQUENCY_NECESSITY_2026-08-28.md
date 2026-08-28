# DSD M5-176 — Eventual Superparabolic Mean-Frequency Necessity

Date: 2026-08-28

Status: **P1_B^S ESCAPE SHARPENING / M5-174 AND M5-175 IMPLY THAT A NONZERO STATISTICAL FLAT FIBER CANNOT RETURN TO ANY FIXED PARABOLIC MEAN CORRIDOR AT SUFFICIENTLY LARGE NORMAL AGE / HENCE EVERY SURVIVOR MUST SATISFY `z N(tau) -> infinity` / THE OLD `AT LEAST PARABOLIC` ESCAPE IS SHARPENED TO EVENTUAL SUPERPARABOLIC MEAN ESCAPE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Define the parabolic mean parameter

Let

\[
\boxed{p(\tau):=z(\tau)N(\tau),\qquad z=e^{-\tau}.}
\]

M5-174 gives, on every fixed corridor

\[
p\le\kappa,
\]

the estimate

\[
\boxed{
N_\tau\le C_\kappa z(1+N).
}
\]

---

## 2. Evolution of `p`

Because

\[
z_\tau=-z,
\]

we have

\[
p_\tau=zN_\tau-p.
\]

Inside the corridor `p<=kappa`, M5-174 yields

\[
\boxed{
p_\tau
\le
C_\kappa z^2+C_\kappa zp-p.
}
\]

At the upper boundary `p=kappa`,

\[
p_\tau
\le
C_\kappa z^2+C_\kappa\kappa z-\kappa.
\]

Therefore there exists a finite depth `tau_kappa` such that for every `tau>=tau_kappa`,

\[
\boxed{
p=\kappa\Longrightarrow p_\tau< -\frac\kappa2<0.
}
\]

Thus after `tau_kappa` the vector field points strictly inward at the upper corridor boundary.

---

## 3. No late upward crossing

Suppose there exists

\[
\tau_1\ge\tau_\kappa
\]

with

\[
p(\tau_1)\le\kappa.
\]

A first later upward crossing of `p=kappa` would require `p_tau>=0` at the crossing time, contradicting Section 2.

Hence

\[
\boxed{
p(\tau)\le\kappa\quad\forall\tau\ge\tau_1.
}
\]

---

## 4. A trapped corridor contradicts flatness

Within this trapped corridor,

\[
N_\tau\le C_\kappa z(1+N).
\]

Since

\[
\int_{\tau_1}^\infty z(\tau)d\tau<\infty,
\]

Gronwall gives

\[
\boxed{
\sup_{\tau\ge\tau_1}N(\tau)<\infty.
}
\]

Consequently

\[
\int_{\tau_1}^\infty zN\,d\tau<\infty,
\]

contradicting the M5-175 necessary condition for a nonzero flat fiber.

Thus a nonzero statistical flat fiber cannot enter any fixed corridor `p<=kappa` after the corresponding depth `tau_kappa`.

---

## 5. Eventual superparabolic escape

Because `kappa>0` was arbitrary, for every finite `kappa` there is a finite `T_kappa` such that

\[
\boxed{
p(\tau)>\kappa\quad\forall\tau\ge T_\kappa.
}
\]

Therefore

\[
\boxed{
\lim_{\tau\to\infty}z(\tau)N(\tau)=+\infty.
}
\]

Equivalently,

\[
\boxed{
N(\tau)\gg e^\tau
}
\]

in the eventual mean sense.

If `Omega_mean:=sqrt(N)`, then

\[
\boxed{
\Omega_{mean}(\tau)\gg e^{\tau/2}.
}
\]

Thus the M5-154 parabolic scale is not merely reached: every surviving statistical flat fiber must eventually outrun every fixed multiple of it.

---

## 6. DSD audit

### Formation — GREEN

`p=zN` is a derived dimensionless mean-frequency parameter, not a new independent budget.

### Axis — GREEN

The normal decay of `z` and the cross-frequency growth of `N` are explicitly separated in `p_tau=zN_tau-p`.

### Static aggregation — GREEN

No representative frequency or support statement is inferred from `N`.

### Dynamics — GREEN

The argument is a first-crossing barrier plus the already-proved M5-175 energy necessity.

### Cross-audit — GREEN

The conclusion does not assume the escape it proves.  It also resolves the initial-time concern in M5-171: the argument is formulated as a late-return exclusion for every fixed corridor, not as a single corridor chosen at infinity.

---

## 7. Updated frontier

`P1_B^S` can now survive only through

\[
\boxed{
zN\to\infty.}
\]

The next step must therefore target **superparabolic spectral migration**, not the finite-parabolic corridor already closed by M5-174.

Promising remaining structures are:

1. analytic spectral-tail versus mean-superparabolic migration;
2. an exact high-frequency damping observable adapted to `Gamma_z` rather than `A`;
3. a backward-uniqueness/log-convexity theorem for the stable Fuchsian system that controls the spectral-infinity boundary directly.

`P1_B^P` remains separate.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
