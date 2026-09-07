# DSD M17-338 — Audit correction: physical and similarity kappa must be separated; M17-330/336/337 cross-generation scaling is quarantined

Date: 2026-09-08  
Canonical ID: **M17-338**

Status: **ACTIVE CORRECTION / SUPERSEDES THE CROSS-GENERATION INTERPRETATION OF M17-330, M17-336, AND M17-337**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Error found

M5-681/M5-682 and the late recurrent CE-H current calculations use the **similarity-variable coefficient** appearing in

\[
\Delta_y W=\kappa^{sim}W,
\]

with similarity vorticity `W(y,theta)` and material velocity

\[
B=U+\frac12y.
\]

M17-330/336/337 then applied the physical parabolic scaling law

\[
\kappa_R=R^2\kappa
\]

directly to that same symbol.

That identifies two different coefficient representations and is not legitimate.

## 2. Physical/similarity dictionary

Let physical time be

\[
t<0,
\qquad
r:=-t>0,
\]

and define

\[
y=\frac{x}{\sqrt r},
\qquad
\theta=-\log r.
\]

For physical vorticity `Omega(x,t)`, define similarity vorticity

\[
\boxed{
W(y,\theta)=r\,\Omega(x,t).
}
\]

Define the physical CE-H coefficient by

\[
\Delta_x\Omega=\kappa^{ph}\Omega.
\]

Because

\[
\Delta_yW=r^2\Delta_x\Omega,
\]

while

\[
W=r\Omega,
\]

we obtain

\[
\boxed{
\kappa^{sim}=r\,\kappa^{ph}.
}
\]

Thus `kappa^sim` is dimensionless, while `kappa^ph` has parabolic dimension `length^{-2}`.

## 3. Material derivative dictionary

Let

\[
h^{ph}:=D_t\kappa^{ph}
\]

along a physical material trajectory and

\[
h^{sim}:=D_B\kappa^{sim}
\]

along the corresponding similarity trajectory.

The trajectory derivatives satisfy

\[
D_B=rD_t
\]

on an unscaled pulled-back scalar.

Using

\[
\kappa^{sim}=r\kappa^{ph},
\qquad
D_t r=-1,
\]

we get

\[
\begin{aligned}
h^{sim}
&=rD_t(r\kappa^{ph})\\
&=r(-\kappa^{ph}+r h^{ph}).
\end{aligned}
\]

Hence

\[
\boxed{
h^{sim}
=-\kappa^{sim}+r^2h^{ph}.}
\]

Equivalently define the scale-homogeneous similarity combination

\[
\boxed{
\mathfrak h^{sim}
:=h^{sim}+\kappa^{sim}
=r^2h^{ph}.
}
\]

The `-kappa` term in M5-682 is therefore not an accidental lower-order term; it is part of the similarity-representation derivative dictionary.

## 4. Parabolic scaling acts differently on the two coefficients

Under physical Navier--Stokes scaling

\[
\Omega_R(x,s)=R^2\Omega(Rx,R^2s),
\]

we have

\[
\boxed{
\kappa_R^{ph}=R^2\kappa^{ph}.
}
\]

But form similarity variables for the scaled solution with

\[
s=t/R^2.
\]

Then

\[
\begin{aligned}
\kappa_R^{sim}
&=(-s)\kappa_R^{ph}\\
&=\frac{r}{R^2}\,R^2\kappa^{ph}\\
&=r\kappa^{ph}.
\end{aligned}
\]

Therefore

\[
\boxed{
\kappa_R^{sim}=\kappa^{sim}
}
\]

under the corresponding parabolic rescaling, up to the expected translation of similarity time

\[
\theta_R=\theta+2\log R.
\]

Thus record scaling acts as a **similarity-time translation**, not as `kappa^sim -> R^2 kappa^sim`.

## 5. Consequences for M17-330

M17-330 claimed that only the numerical level `kappa=0` is fixed and that `3/2` rescales to `3/(2R^2)`.

That statement is correct for a **physical coefficient level** `kappa^ph`, but M17-329's `3/2` is a **similarity coefficient level**.

Therefore the cross-generation comparison in M17-330 mixed representations.

Verdict:

\[
\boxed{
\text{M17-330 cross-generation threshold comparison: QUARANTINED.}
}
\]

Its narrower conceptual warning — do not mix physical and representation-dependent thresholds — remains useful.

## 6. Consequences for M17-336

M17-336 scaled the M5-681 stationary pair as

\[
F_R(k)=R^{-2}F(k/R^2),
\qquad
G_R(k)=R^2G(k/R^2).
\]

Those formulas apply to a scale-homogeneous physical `kappa` distribution/current, not directly to the M5-681 **similarity** `kappa` distribution/current.

For a genuinely transferred similarity hull, parabolic scaling primarily translates `theta`; it does not create an `R^2` amplification of the numerical `kappa^sim` current by the argument given there.

Therefore the claimed estimate

\[
-G_R(3/2)\ge R^2d-\frac32M
\]

is not certified for the M5-681/M17-314 similarity current.

Verdict:

\[
\boxed{
\text{M17-336: QUARANTINED pending an explicit physical-to-similarity ensemble map.}
}
\]

The genealogy/ensemble-transfer issue remains open rather than closed conditionally by that formula.

## 7. Consequences for M17-337

M17-337 constructed

\[
a^{-1/2}
\int h_-\delta(\kappa-a)\rho^2\,dy\,d\theta
\]

by combining physical parabolic scaling for `kappa,h` with the positive similarity threshold `a=3/2`.

Because `h^{sim}` is not the scale-homogeneous derivative at positive `kappa`, this calculation mixes representations.

At positive similarity level `a`,

\[
\boxed{
h^{sim}=r^2h^{ph}-a.}
\]

Thus a fixed-similarity-level crossing measures motion relative to the **moving physical threshold**

\[
\kappa^{ph}=\frac{a}{r},
\]

not simply physical `D_t kappa^ph`.

Verdict:

\[
\boxed{
\text{M17-337 critical-spatialization claim: QUARANTINED.}
}
\]

A corrected positive-level currency must use the exact dictionary above.

## 8. Why M17-326 zero crossing is special

At the zero level

\[
\kappa^{sim}=0
\quad\Longleftrightarrow\quad
\kappa^{ph}=0.
\]

Moreover the offset vanishes:

\[
\boxed{
h^{sim}=r^2h^{ph}\quad\text{when }\kappa=0.}
\]

Also

\[
\delta(\kappa^{sim})
=
\delta(r\kappa^{ph})
=r^{-1}\delta(\kappa^{ph}),
\]

and

\[
d\theta=\frac{dt}{r}.
\]

Therefore

\[
\begin{aligned}
h^{sim}_-\delta(\kappa^{sim})d\Phi d\theta
&=
r^2h^{ph}_-
\cdot r^{-1}\delta(\kappa^{ph})
\cdot d\Phi
\cdot r^{-1}dt\\
&=
h^{ph}_-\delta(\kappa^{ph})d\Phi dt.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal C_{-,0}^{sim}
=
\mathcal C_{-,0}^{ph}.
}
\]

This gives the missing exact representation bridge for the M17-326 zero-level crossing currency.

Thus M17-326 can survive, but its scale-criticality must be read through this zero-level dictionary rather than by treating all similarity `h,kappa` as physical homogeneous fields.

## 9. Positive similarity thresholds as moving physical thresholds

At a fixed similarity level

\[
\kappa^{sim}=a>0,
\]

we have

\[
\kappa^{ph}=\frac{a}{r}.
\]

The physical speed relative to this moving threshold is

\[
D_t\left(\kappa^{ph}-\frac{a}{r}\right)
=
h^{ph}-\frac{a}{r^2}.
\]

Multiplying by `r^2`,

\[
\boxed{
r^2
D_t\left(\kappa^{ph}-\frac{a}{r}\right)
=h^{sim}.}
\]

Thus fixed `a` current in similarity variables is a legitimate transition diagnostic, but it is a moving-threshold diagnostic in physical variables.

It must not be assigned the simple homogeneous scaling used in M17-337.

## 10. DSD-theory role

This correction is exactly the useful role of the DSD theoretical layer requested by the user:

- identify whether two quantities live in the same representation/channel;
- remove the representation map before declaring an invariant;
- keep the mathematical proof independent of DSD axioms.

The actual correction is entirely the standard physical/similarity change of variables.

## 11. Corrected active frontier

Keep active:

- M17-326 zero-level crossing currency, **with the representation dictionary in Section 8**;
- M17-331--335 as fixed-similarity-generation statements;
- M17-329 as the similarity-Jacobian correction.

Quarantine for cross-generation use:

\[
\boxed{
\text{M17-330 cross-generation threshold scaling},
\quad
\text{M17-336},
\quad
\text{M17-337}.
}
\]

The next valid cross-generation calculation must begin with

\[
\boxed{
\kappa^{sim}=(-t)\kappa^{ph},
\qquad
h^{sim}+\kappa^{sim}=(-t)^2h^{ph},
}
\]

and only then compare recurrent similarity quantities with record-blowdown physical quantities.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
