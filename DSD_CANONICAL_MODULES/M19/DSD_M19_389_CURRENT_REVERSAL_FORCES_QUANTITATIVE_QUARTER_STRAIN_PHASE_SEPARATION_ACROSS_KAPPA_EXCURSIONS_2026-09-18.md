# M19-389 — Current reversal forces quantitative quarter-strain phase separation across kappa excursions

Date: 2026-09-18

Status: **NEW CANONICAL NECESSARY CONDITION / M19-388 IS GENERALIZED FROM A SINUSOIDAL WITNESS TO AN ARBITRARY MATERIAL POSITIVE-KAPPA EXCURSION. IF THE RESIDENCE-WEIGHTED SPATIAL ZERO-CROSSING CURRENT CANCELS OR REVERSES THE STRICTLY NEGATIVE MATERIAL-FLUX CURRENT ON ONE UPWARD/DOWNWARD CROSSING PAIR, THEN THE RELATIVE RESIDENCE FACTOR MUST FALL BY AT LEAST THE SQUARE OF THE FLUX AMPLIFICATION ACROSS THAT POSITIVE EXCURSION. EQUIVALENTLY THE POSITIVE-KAPPA PHASE MUST HAVE A QUANTITATIVE NEGATIVE QUARTER-STRAIN SURPLUS `int(sigma_bar_rho + kappa - 1/4)<=0`; IF THE RELATIVE RESIDENCE IS RECURRENT OVER THE FULL CYCLE, THE FOLLOWING NEGATIVE-KAPPA PHASE MUST PAY AN EQUAL-OR-LARGER POSITIVE QUARTER-STRAIN RESIDENCE. THUS CURRENT-SIGN REVERSAL REQUIRES A FORCED COMPRESSIVE/EXTENSIONAL PHASE SEPARATION, NOT ARBITRARY BOUNDED HYSTERESIS. THIS IS A NECESSARY PHASE LAW, NOT YET A CONTRADICTION. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. One positive-kappa excursion

Consider one material vortex-line label and two consecutive zero crossings

\[
\theta_u<\theta_d
\]

such that

\[
\kappa(\theta_u)=\kappa(\theta_d)=0,
\]

\[
\kappa>0
\qquad
(\theta_u<\theta<\theta_d),
\]

with an upward crossing at \(\theta_u\) and a downward crossing at \(\theta_d\).

Define the positive multiplier action

\[
\boxed{
I_+
:=
\int_{\theta_u}^{\theta_d}\kappa(\theta)\,d\theta
>0.
}
\]

The exact material flux law gives

\[
\frac d{d\theta}\log\Phi=\kappa,
\]

hence

\[
\boxed{
\frac{\Phi_d}{\Phi_u}=e^{I_+}.
}
\]

---

## 2. Relative residence factor

Let

\[
R:=\frac{L_\rho}{\Phi}.
\]

M5-684 gives

\[
\boxed{
\frac d{d\theta}\log R
=2\bar\sigma_\rho-\frac12.
}
\]

Therefore

\[
\boxed{
\log\frac{R_d}{R_u}
=J_+
:=
\int_{\theta_u}^{\theta_d}
\left(2\bar\sigma_\rho-\frac12\right)d\theta.
}
\]

Since \(L_\rho=\Phi R\),

\[
\frac{L_d}{L_u}
=
\frac{\Phi_d}{\Phi_u}
\frac{R_d}{R_u}
=
e^{I_++J_+}.
\]

---

## 3. Crossing-current sign comparison

For a regular isolated crossing pair, the time-integrated delta current at \(\kappa=0\) has one positive contribution from the upward crossing and one negative contribution from the downward crossing.

The material-flux current pair is proportional to

\[
\Phi_u-\Phi_d<0.
\]

The residence-weighted spatial current pair is proportional to

\[
\boxed{
\Phi_uL_u-\Phi_dL_d.
}
\]

This statement assumes the same crossing-Jacobian normalization on the pair; in the unequal-speed case insert the corresponding positive \(|h|^{-1}\) factors, which produces the same argument with an additional explicit crossing-speed ratio. The symmetric-speed case isolates the phase mechanism cleanly and is the canonical normal form below.

For cancellation or sign reversal of the negative material current we need

\[
\Phi_uL_u
\ge
\Phi_dL_d.
\]

Using \(L=\Phi R\),

\[
\Phi_u^2R_u
\ge
\Phi_d^2R_d.
\]

Hence

\[
\boxed{
\frac{R_u}{R_d}
\ge
\left(\frac{\Phi_d}{\Phi_u}\right)^2
=e^{2I_+}.
}
\]

Equivalently,

\[
\boxed{
J_+\le-2I_+.
}
\]

---

## 4. Quarter-strain phase condition

Insert the definitions of \(I_+\) and \(J_+\):

\[
\int_{\theta_u}^{\theta_d}
\left(2\bar\sigma_\rho-\frac12\right)d\theta
\le
-2
\int_{\theta_u}^{\theta_d}\kappa\,d\theta.
\]

Therefore

\[
\boxed{
\int_{\theta_u}^{\theta_d}
\left(
\bar\sigma_\rho+\kappa-\frac14
\right)d\theta
\le0.
}
\]

Equivalently,

\[
\boxed{
\int_{\theta_u}^{\theta_d}
\left(\frac14-\bar\sigma_\rho\right)d\theta
\ge I_+.
}
\]

Thus the positive-kappa amplification phase can reverse the residence-weighted current only if it carries a quantitatively sufficient **compressive quarter-strain deficit**.

The required deficit is at least the entire positive multiplier action \(I_+\).

---

## 5. Full recurrent cycle

Let \(\theta_{u,next}>\theta_d\) be the next upward zero crossing and suppose the relative residence returns after one complete material cycle:

\[
R(\theta_{u,next})=R(\theta_u).
\]

Then

\[
J_++J_-=0,
\]

where

\[
J_-
:=
\int_{\theta_d}^{\theta_{u,next}}
\left(2\bar\sigma_\rho-\frac12\right)d\theta.
\]

Since current reversal requires \(J_+\le-2I_+\),

\[
\boxed{
J_-\ge2I_+.
}
\]

Therefore the negative-kappa part of the cycle must satisfy

\[
\boxed{
\int_{\theta_d}^{\theta_{u,next}}
\left(\bar\sigma_\rho-\frac14\right)d\theta
\ge I_+.
}
\]

So the same amount of residence compression used during the positive-kappa phase must be rebuilt by an **extensional quarter-strain surplus** during the following negative-kappa phase.

---

## 6. Canonical phase architecture

A bounded recurrent current-reversal cycle therefore has the forced structure

\[
\boxed{
\begin{array}{c}
\kappa>0\text{ amplification phase}\\
\Downarrow\\
\displaystyle
\int(\tfrac14-\bar\sigma_\rho)\,d\theta
\ge I_+
\end{array}
}
\]

followed by

\[
\boxed{
\begin{array}{c}
\kappa<0\text{ retirement phase}\\
\Downarrow\\
\displaystyle
\int(\bar\sigma_\rho-\tfrac14)\,d\theta
\ge I_+.
\end{array}
}
\]

Thus bounded residence hysteresis is not arbitrary: it is a quantitatively locked compressive/extensional strain cycle.

---

## 7. Check against M19-388

For the periodic witness

\[
\kappa=A\sin\theta,
\qquad
R=e^{B\cos\theta},
\]

on the positive excursion \(0<\theta<\pi\),

\[
I_+=\int_0^\pi A\sin\theta\,d\theta=2A,
\]

and

\[
J_+
=\log\frac{R(\pi)}{R(0)}
=-2B.
\]

The general condition

\[
J_+\le-2I_+
\]

becomes

\[
-2B\le-4A,
\]

or

\[
\boxed{B\ge2A,}
\]

exactly reproducing the M19-388 cancellation/reversal threshold.

Thus M19-388 is sharp for this general crossing-pair inequality.

---

## 8. Relation to earlier extensional-compensator results

M19-368 already showed from the recurrent CE-H covariance ledger that the critical seed phase with \(\sigma\approx-1/2\) has the wrong sign to pay the required negative Rayleigh covariance and therefore needs a distinct extensional \(\sigma>1/4\) compensator.

M19-389 reaches the same qualitative architecture from a different exact route:

\[
\boxed{
\text{residence-current reversal}
\Longrightarrow
\text{positive-phase compression}
+
\text{negative-phase extension}.
}
\]

The agreement of these two routes strengthens the phase classification but does not make the extensional phase nonrecyclable.

---

## 9. What remains open

The quarter-strain phase separation is a necessary condition, not a contradiction.

A recurrent CE-H state may in principle alternate compressive and extensional strain indefinitely.

The next PDE-specific question is whether the required fixed phase actions can be supported while respecting

\[
D_\kappa\ge d_\kappa>0,
\]

\[
D_\sigma\le C P,
\]

and the critical palinstrophy genealogy without creating a nonreusable crossing/turnover event.

Equivalently, one should condition the M5-688 quarter-strain residence ledger on positive/negative \(\kappa\) excursions and compare the required action \(I_+\) with the finite base-transversal/genealogy architecture.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
