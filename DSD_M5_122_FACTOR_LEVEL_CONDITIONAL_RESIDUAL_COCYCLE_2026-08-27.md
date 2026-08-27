# DSD M5-122 — Factor-Level Conditional Residual Cocycle

Date: 2026-08-27

Status: **INVARIANT DISINTEGRATION PUSHES THE MEAN CRITICAL PRESSURE-STRAIN RESIDUAL ENTIRELY ONTO THE CANONICAL TAIL FACTOR / NONINJECTIVE FIBERS CAN ONLY CONTRIBUTE ZERO-MEAN RESIDUAL FLUCTUATIONS AROUND THIS FACTOR-LEVEL COCYCLE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Inputs

Use the ergodic W1 invariant measure `mu`, canonical tail factor

\[
\pi:M\to\mathcal T,
\qquad
\nu=\pi_\#\mu,
\]

and disintegration

\[
\mu=\int\mu_Td\nu(T)
\]

from M5-119.

Use the critical pressure-strain residual

\[
\mathcal E_3(V)\ge0
\]

and the renormalized cubic charge

\[
\mathcal K(V)
\]

from M5-108/M5-120.

Define the conditional factor functions

\[
\boxed{
\overline{\mathcal E}(T)
:=\int_{\pi^{-1}(T)}\mathcal E_3(V)d\mu_T(V),
}
\]

and

\[
\boxed{
\overline{\mathcal K}(T)
:=\int_{\pi^{-1}(T)}\mathcal K(V)d\mu_T(V).
}
\]

`overline K` is bounded because `K` is bounded on compact `M`.

---

## 2. Equivariance of the conditional measures

The factor flow

\[
D_h:\mathcal T\to\mathcal T
\]

is invertible log translation.

The W1 forward flow satisfies

\[
\pi(S_hV)=D_h\pi(V).
\]

For `nu`-almost every `T`, the pushed measure

\[
S_h{}_\#\mu_T
\]

is supported on

\[
\pi^{-1}(D_hT).
\]

Moreover

\[
\int S_h{}_\#\mu_Td\nu(T)
=S_h{}_\#\mu
=\mu.
\]

Since `D_h` preserves `nu` and is invertible, uniqueness of disintegration gives

\[
\boxed{
S_h{}_\#\mu_T
=\mu_{D_hT}
}
\]

for `nu`-almost every `T`.

Thus the conditional fibers form a genuine measure-valued cocycle over the tail translation factor.

---

## 3. Integrate the pointwise residual inequality inside one fiber

M5-108 gives for every W1 state

\[
\boxed{
\mathcal E_3(V)\ge2\nu X_3(V).
}
\]

Integrate in time from `0` to `h` and then average over one initial fiber `mu_T`:

\[
\int_{\pi^{-1}(T)}
\int_0^h\mathcal E_3(S_sV)dsd\mu_T(V)
\ge
2\nu
\int_{\pi^{-1}(T)}
\int_0^hX_3(S_sV)dsd\mu_T(V).
\]

By conditional-measure equivariance, the left-hand side is

\[
\boxed{
\int_0^h\overline{\mathcal E}(D_sT)ds.
}
\]

---

## 4. Insert the exact core-tail cocycle

M5-120 gives statewise

\[
\int_0^hX_3(S_sV)ds
=
\frac13[\mathcal K(S_hV)-\mathcal K(V)]
+
\frac13
\int_{-h/2}^0\mathfrak c_\rho(T)d\rho.
\]

The tail-window term is constant across the whole fiber because every `V` in the fiber has the same canonical tail `T`.

Averaging the coboundary over `mu_T` and using equivariance gives

\[
\int\mathcal K(S_hV)d\mu_T(V)
=\overline{\mathcal K}(D_hT).
\]

Therefore

\[
\boxed{
\begin{aligned}
\int_0^h\overline{\mathcal E}(D_sT)ds
&\ge
\frac{2\nu}{3}
[\overline{\mathcal K}(D_hT)-\overline{\mathcal K}(T)]\\
&\quad+
\frac{2\nu}{3}
\int_{-h/2}^0\mathfrak c_\rho(T)d\rho.
\end{aligned}
}
\]

This is the finite-time **factor-level residual cocycle inequality**.

---

## 5. Differential form

The finite-time identity implies absolute continuity of `overline K(D_hT)` along almost every factor trajectory.

Differentiate in `h` at Lebesgue times.

Since

\[
\frac d{dh}
\int_{-h/2}^0\mathfrak c_\rho(T)d\rho
=\frac12\mathfrak c(D_hT)
\]

in translated notation, obtain

\[
\boxed{
\overline{\mathcal E}(T)
\ge
\frac{2\nu}{3}\mathcal L_D\overline{\mathcal K}(T)
+
\frac\nu3\mathfrak c(T)
}
\]

for `nu`-almost every tail state.

Equivalently,

\[
\boxed{
\overline{\mathcal E}
-\frac{2\nu}{3}\mathcal L_D\overline{\mathcal K}
\ge
\frac\nu3\mathfrak c.
}
\]

---

## 6. Invariant mean

Average over `nu`.

The factor coboundary vanishes by invariance:

\[
\int\mathcal L_D\overline{\mathcal K}d\nu=0.
\]

Hence

\[
\boxed{
\int_{\mathcal T}\overline{\mathcal E}d\nu
\ge
\frac\nu3
\int_{\mathcal T}\mathfrak c d\nu
=
\frac\nu3\mathscr R_3.
}
\]

This recovers M5-108 after disintegration.

The point is stronger structurally: the mean residual floor now lives on the factor itself.

---

## 7. What noninjective fibers can still do

Define

\[
\boxed{
\mathcal E_{fib}(V)
:=
\mathcal E_3(V)-\overline{\mathcal E}(\pi(V)).
}
\]

Then

\[
\boxed{
\int_{\pi^{-1}(T)}\mathcal E_{fib}(V)d\mu_T(V)=0.
}
\]

Unlike `E_3`, the fluctuation `E_fib` is signed.

Therefore a noninjective fiber cannot provide a second nonnegative residual budget in addition to `overline E`.

Its only remaining freedom is the conditional variance

\[
\boxed{
\operatorname{Var}_{\mu_T}(\mathcal E_3)
=\int|\mathcal E_{fib}|^2d\mu_T.
}
\]

This is the precise P1 remainder.

---

## 8. DSD four-chain audit

### Formation — GREEN

Conditional residual and conditional renormalized charge are defined only after the actual tail factor and disintegration exist.

### Axis — GREEN

Tail translation, fiber variation and nonnegative residual are different channels.

### Static aggregation — GREEN

The factor expectation is nonnegative; the fiber fluctuation is signed and has zero conditional mean.

### Dynamics — GREEN

Equivariance of conditional measures is proved before transporting the fiber averages.

### Cross-audit — GREEN

The invariant mean residual is recovered from the factor inequality and is not used to assume pointwise factor descent.

---

## 9. Major reduction

The earlier P0/P1 question

\[
\text{Does the residual payer descend to the tail factor?}
\]

is now answered at the only level needed for positive mean critical bookkeeping:

\[
\boxed{
\text{YES, its conditional mean always descends.}
}
\]

Full pointwise descent is unnecessary for the mean anomaly.

The unresolved fiber problem is strictly smaller:

\[
\boxed{
\text{Can same-tail strong-critical dynamics sustain nonzero conditional variance of }\mathcal E_3?
}
\]

Even a positive answer would not create a second anomaly; it would only redistribute the already existing factor-level residual among same-tail states.

---

## 10. New frontier

There are now two viable forward calculations:

1. **factor rigidity:** analyze the nonnegative translation-system inequality
   \[
   \overline{\mathcal E}
   -\frac{2\nu}{3}\mathcal L_D\overline{\mathcal K}
   \ge\frac\nu3\mathfrak c
   \]
   together with divergence-free/zero-flux constraints on the log cylinder;

2. **fiber variance:** derive a relative equation for same-tail differences `Z=V-W` and test whether nonzero residual variance forces a relative frequency/gradient channel beyond the already allowed parabolic scale escape.

The factor calculation is now the primary path because it carries the entire non-exact anomaly.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
