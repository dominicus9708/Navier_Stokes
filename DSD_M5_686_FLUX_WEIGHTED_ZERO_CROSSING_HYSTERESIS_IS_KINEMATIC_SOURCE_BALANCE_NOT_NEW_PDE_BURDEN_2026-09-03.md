# DSD M5-686 — Flux-weighted zero-crossing hysteresis is an exact kinematic source balance, not a new PDE burden

Date: 2026-09-03

Status: **INTERNAL AUDIT CORRECTION / THE STRICT NEGATIVE CURRENT THROUGH `kappa=0` FOUND IN M5-681 AND REINTERPRETED AS FLUX-WEIGHTED HYSTERESIS IN M5-685 IS ALREADY FORCED BY THE EXACT WEIGHT LAW `a'=kappa a` TOGETHER WITH RECURRENCE / FOR THE POSITIVE- AND NEGATIVE-KAPPA FLUX MASSES ONE HAS `M_+'=R_+ + G(0)` AND `M_-'=R_- - G(0)`; HENCE ON A RECURRENT FINITE-FLUX ENSEMBLE `Gbar(0)=-Rbar_+=Rbar_-=-1/2 int |k| Fbar(k) dk <0` WHEN THE MULTIPLIER IS NONTRIVIAL / EQUIVALENTLY EVERY POSITIVE-KAPPA EXCURSION AMPLIFIES THE MATERIAL FLUX BETWEEN ITS UPWARD AND DOWNWARD ZERO CROSSINGS / THIS REMOVES THE M5-685 HYSTERESIS SIGN AS AN INDEPENDENT CONSTITUTIVE OBSTRUCTION AND RETURNS THE TARGET TO A GENUINE PDE PAYMENT IDENTITY / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Current-flux weight and kappa current

Use the fixed base label measure of M5-685,

\[
d\mu_0(\lambda),
\]

and write the current material-flux weight as

\[
\boxed{
d\mu_\theta(\lambda)
=a_\lambda(\theta)d\mu_0(\lambda),
}
\]

with

\[
\boxed{
a_\lambda'=\kappa_\lambda a_\lambda,
\qquad
h_\lambda:=\kappa_\lambda'.
}
\]

The current-flux kappa distribution and current are

\[
F(k,\theta)
=\int \delta(k-\kappa_\lambda)a_\lambda d\mu_0,
\]

\[
G(k,\theta)
=\int h_\lambda\delta(k-\kappa_\lambda)a_\lambda d\mu_0.
\]

M5-681 already gives the exact kinetic equation

\[
\boxed{
\partial_\theta F+\partial_kG=kF.
}
\]

The point of this document is to audit what this equation alone already forces at `k=0`.

---

## 2. Positive-kappa flux mass

Define

\[
\boxed{
M_+(\theta)
:=\int_{\kappa_\lambda>0}a_\lambda d\mu_0
=\int_0^\infty F(k,\theta)dk.
}
\]

Using a smooth approximation to the Heaviside function and then passing to the distributional limit,

\[
\frac d{d\theta}
\left[a_\lambda H(\kappa_\lambda)\right]
=
\kappa_\lambda a_\lambda H(\kappa_\lambda)
+a_\lambda h_\lambda\delta(\kappa_\lambda).
\]

Therefore

\[
\boxed{
M_+'
=R_+ + G(0),
}
\]

where

\[
\boxed{
R_+(\theta)
:=\int_{\kappa_\lambda>0}
\kappa_\lambda a_\lambda d\mu_0
=\int_0^\infty kF(k,\theta)dk
\ge0.
}
\]

On a recurrent finite-flux ensemble, the long-time mean of the bounded quantity `M_+` has zero derivative. Hence

\[
\boxed{
\overline G(0)
=-\overline{R_+}.
}
\]

Thus the negative current through zero is already the exact payment required to remove the flux weight created in the positive-kappa half-space.

---

## 3. Negative-kappa flux mass

Similarly define

\[
\boxed{
M_-(\theta)
:=\int_{\kappa_\lambda<0}a_\lambda d\mu_0.
}
\]

Since

\[
\frac d{d\theta}
\left[a_\lambda H(-\kappa_\lambda)\right]
=
\kappa_\lambda a_\lambda H(-\kappa_\lambda)
-a_\lambda h_\lambda\delta(\kappa_\lambda),
\]

we obtain

\[
\boxed{
M_-'
=R_- - G(0),
}
\]

with

\[
\boxed{
R_-(\theta)
:=\int_{\kappa_\lambda<0}
\kappa_\lambda a_\lambda d\mu_0
\le0.
}
\]

Recurrence gives

\[
\boxed{
\overline G(0)
=\overline{R_-}.
}
\]

Consequently

\[
\boxed{
\overline{R_+}+\overline{R_-}=0,
}
\]

which is the zero mean growth of the total retained material flux.

---

## 4. Exact absolute-multiplier formula

Combining the two half-space identities yields

\[
\overline{R_+}
=-\overline{R_-}.
\]

Therefore

\[
\int |k|\overline F(k)dk
=\overline{R_+}-\overline{R_-}
=2\overline{R_+}.
\]

Hence

\[
\boxed{
\overline G(0)
=-\frac12
\int_{\mathbb R}|k|\overline F(k)dk.
}
\]

This is stronger than the qualitative sign statement.

Whenever the recurrent current-flux population has nonzero multiplier activity,

\[
\int |k|\overline F(k)dk>0,
\]

one automatically has

\[
\boxed{
\overline G(0)<0.
}
\]

No constitutive formula for `h=D_B kappa` has been used.

---

## 5. Single-label crossing-cycle interpretation

Consider one material label with an upward zero crossing at `theta_u` and the next downward zero crossing at `theta_d`, with

\[
\kappa_\lambda>0
\qquad
(\theta_u<\theta<\theta_d).
\]

Then

\[
\boxed{
\frac{a_\lambda(\theta_d)}{a_\lambda(\theta_u)}
=
\exp\left(
\int_{\theta_u}^{\theta_d}\kappa_\lambda(\tau)d\tau
\right)>1.
}
\]

Thus the downward crossing is automatically flux-heavier than the preceding upward crossing of the same positive excursion.

For the subsequent negative excursion,

\[
\frac{a_\lambda(\theta_{u,next})}{a_\lambda(\theta_d)}
=
\exp\left(
\int_{\theta_d}^{\theta_{u,next}}\kappa_\lambda d\tau
\right)<1.
\]

If the full label cycle returns with the same flux weight, then exactly

\[
\boxed{
\oint \kappa_\lambda d\theta=0.
}
\]

The flux-weighted crossing hysteresis is therefore a direct consequence of integrating `a'=kappa a` around a sign-changing cycle.

---

## 6. Audit of M5-685

M5-685 correctly identified that

\[
\overline{
\int h\delta(\kappa)d\mu_0
}=0
\]

but

\[
\overline{
\int ha\delta(\kappa)d\mu_0
}<0.
\]

However, interpreting this sign difference as a new PDE-specific hysteresis burden was too strong.

The present calculation shows

\[
\boxed{
\text{base-measure zero current}
+ a'=\kappa a
+ \text{recurrence}
\Longrightarrow
\text{negative current-flux zero current}.
}
\]

Thus the sign bias is **kinematic/source-balance data**.

It does not by itself constrain the M5-682 constitutive formula strongly enough to close the survivor.

This is a DSD audit correction, not a reversal of M5-681.

M5-681 remains exact; the correction concerns only what extra information its strict current supplies.

---

## 7. Corrected frontier

A useful closure must now remove the part of the current that is already forced by

\[
\partial_\theta F+\partial_kG=kF
\]

and isolate a genuinely PDE-specific positive or sign-definite quantity.

The most promising candidate is the spatial variation of the CE-H Laplacian multiplier itself,

\[
\nabla\kappa,
\]

because M5-682 contains the weighted diffusion term

\[
L_\rho\kappa
\]

and M5-683 exposes the nonnegative density

\[
A_{\kappa\kappa}
=\int\delta(k-\kappa)\chi\rho^2|\nabla\kappa|^2dy.
\]

The next step is therefore to determine whether a nonzero compact CE-H recurrent state can make this diffusion charge vanish.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
