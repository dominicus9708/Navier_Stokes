# M19-388 — A periodic kinematic witness shows bounded residence hysteresis can recycle indefinitely

Date: 2026-09-18

Status: **NO-GO / SHARP KINEMATIC WITNESS. THE EXACT MATERIAL LAWS `D log Phi = kappa` AND `D log(L_rho/Phi)=2 sigma_bar_rho-1/2` ALONE DO NOT PREVENT INDEFINITE RECURRENT RESIDENCE HYSTERESIS. AN EXPLICIT PERIODIC ONE-LABEL MODEL CAN HAVE ZERO NET KAPPA EXPOSURE PER CYCLE, BOUNDED PERIODIC FLUX AND RESIDENCE, STRICTLY NEGATIVE CURRENT-FLUX KAPPA CURRENT AT ZERO, AND — BY A PHASE-SHIFTED BUT BOUNDED RESIDENCE FACTOR — A POSITIVE RESIDENCE/VELOCITY COVARIANCE LARGE ENOUGH TO CANCEL OR REVERSE THE SPATIAL WEIGHTED ZERO CURRENT. THIS IS NOT A NAVIER–STOKES SOLUTION; IT IS A COUNTER-WITNESS TO ANY CLOSURE USING ONLY THE MATERIAL KINEMATIC LAWS AND COMPACT RECURRENCE. PDE-SPECIFIC CONSTITUTIVE CONTROL IS NECESSARY. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Periodic coefficient history

Fix constants

\[
A>0,
\qquad B>0.
\]

Let one abstract material label have the periodic multiplier

\[
\boxed{
\kappa(\theta)=A\sin\theta,
\qquad \theta\in\mathbb R/2\pi\mathbb Z.
}
\]

Then

\[
\boxed{
h:=\kappa'=A\cos\theta.}
\]

The zero crossings are

\[
\theta_u=0,
\qquad
\theta_d=\pi,
\]

with

\[
h(0)=A>0,
\qquad
h(\pi)=-A<0.
\]

Thus `0` is an upward crossing and `pi` is a downward crossing.

---

## 2. Exact material-flux law

Impose the exact CE-H material flux kinematics

\[
\frac d{d\theta}\log\Phi=\kappa.
\]

With \(\Phi(0)=\Phi_0>0\),

\[
\boxed{
\Phi(\theta)
=
\Phi_0
\exp\big(A(1-\cos\theta)\big).
}
\]

Because

\[
\int_0^{2\pi}\kappa\,d\theta=0,
\]

we have

\[
\boxed{
\Phi(2\pi)=\Phi(0)=\Phi_0.
}
\]

The flux is therefore bounded and exactly recurrent.

At the zero crossings,

\[
\Phi_u=\Phi_0,
\qquad
\Phi_d=\Phi_0e^{2A}.
\]

Hence the downward crossing is flux-heavier, exactly as required by M5-686.

---

## 3. Periodic relative-residence factor

Let

\[
R:=\frac{L_\rho}{\Phi}
\]

and choose

\[
\boxed{
R(\theta)=e^{B\cos\theta}.
}
\]

Then \(R\) is positive, bounded and exactly periodic:

\[
e^{-B}\le R\le e^B.
\]

The exact M5-684 law requires

\[
\frac d{d\theta}\log R
=2\bar\sigma_\rho-\frac12.
\]

Since

\[
\frac d{d\theta}\log R=-B\sin\theta,
\]

choose

\[
\boxed{
\bar\sigma_\rho(\theta)
=
\frac14-\frac B2\sin\theta.
}
\]

This is also bounded and periodic.

Therefore the exact material residence law is satisfied identically.

---

## 4. Resulting line residence

The line residence is

\[
L_\rho=\Phi R.
\]

Hence

\[
\boxed{
L_\rho(\theta)
=
\Phi_0 e^A
\exp\big((B-A)\cos\theta\big).
}
\]

At the two zero crossings,

\[
\boxed{
L_u=\Phi_0e^B,
\qquad
L_d=\Phi_0e^{2A-B}.
}
\]

If

\[
B>A,
\]

then

\[
L_u>L_d.
\]

Thus larger residence is correlated with the upward coefficient velocity \(h>0\), producing the positive residence/velocity covariance identified in M19-385--387.

---

## 5. Current-flux zero current remains negative

For one periodic label, time-averaging a delta current at \(\kappa=0\) gives one contribution from each crossing. Because

\[
|h_u|=|h_d|=A,
\]

the Jacobian factors from \(\delta(\kappa)\) cancel symmetrically.

The current-flux zero current is proportional to

\[
\Phi_u-\Phi_d
=
\Phi_0(1-e^{2A})<0.
\]

Therefore

\[
\boxed{\overline G_\Phi(0)<0.}
\]

exactly as in M5-686.

---

## 6. Residence-weighted spatial current can cancel or reverse

The residence-weighted current has crossing contributions proportional to

\[
\Phi_uL_u
-
\Phi_dL_d.
\]

Using the formulas above,

\[
\Phi_uL_u
=
\Phi_0^2e^B,
\]

and

\[
\Phi_dL_d
=
\Phi_0^2e^{4A-B}.
\]

Hence

\[
\boxed{
\overline G_E(0)
\propto
 e^B-e^{4A-B}.
}
\]

Therefore:

- if \(B<2A\), the weighted current remains negative;
- if \(B=2A\), it cancels exactly;
- if \(B>2A\), it reverses sign and becomes positive.

Thus a **bounded periodic** relative-residence phase is sufficient to cancel or reverse the spatial current while the material-flux current remains strictly negative.

No residence blow-up is necessary.

---

## 7. Interpretation as covariance

At the two zero-crossing phases, the current-flux conditional distribution has weights proportional to

\[
\Phi_u,
\qquad \Phi_d.
\]

Since

\[
h_u=+A,
\qquad h_d=-A,
\]

and for \(B>A\),

\[
L_u>L_d,
\]

the conditional covariance satisfies

\[
\boxed{
\operatorname{Cov}_{\kappa=0}^{\Phi}(L_\rho,h)>0.
}
\]

For \(B>2A\) it is large enough to overcome the negative mean current term in the exact M19-385 identity.

This realizes the M19-387 bounded-hysteresis branch explicitly.

---

## 8. What the witness proves and does not prove

This construction satisfies the two exact material kinematic laws

\[
D\log\Phi=\kappa,
\qquad
D\log(L_\rho/\Phi)=2\bar\sigma_\rho-\frac12,
\]

and exact periodic recurrence of all scalar variables used above.

It therefore proves the NO-GO statement

\[
\boxed{
\text{material kinematics + bounded recurrence}
\not\Rightarrow
\text{elimination of residence hysteresis}.
}
\]

However, the witness does **not** claim to satisfy

\[
\Delta W=\kappa W
\]

or the full Navier--Stokes/CE-H constitutive law.

It is not a PDE solution and is not evidence for singularity existence.

Its role is only to show that a successful closure must use genuinely PDE-specific information beyond the two material scalar evolution laws.

---

## 9. Consequence for the frontier

The bounded residence-hysteresis branch of M19-387 is a genuine recyclable kinematic survivor.

Therefore the next valid target is not a generic compactness or finite-base-flux argument.

It must couple the periodic phase architecture to one of the PDE-specific charges:

\[
\boxed{
D_\kappa
\ge d_\kappa>0,
\qquad
\mathfrak A
=|W|^{10}[\nabla\kappa\times\nabla(D_B\kappa)],
\qquad
\text{or the M5-683 constitutive current.}
}
\]

Equivalently, one must show that a Navier--Stokes CE-H state cannot realize the abstract phase choice \((\kappa,\bar\sigma_\rho,R)\) required by this witness without paying a nonrecyclable spatial derivative/genealogical cost.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
