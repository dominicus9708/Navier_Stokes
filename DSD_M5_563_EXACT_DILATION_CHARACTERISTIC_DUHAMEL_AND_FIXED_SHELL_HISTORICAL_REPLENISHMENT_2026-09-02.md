# DSD M5-563 — Exact dilation-characteristic Duhamel law and fixed-shell historical replenishment

Date: 2026-09-02

Status: **EXACT CONVEYOR IDENTITY / ALONG THE OUTWARD SIMILARITY DILATION CHARACTERISTIC `R(TAU)=R0 EXP(TAU/2)`, THE CRITICAL RESCALED VELOCITY PROFILE `V=R U(R XI)` SATISFIES AN EXACT EQUATION WITH ALL NONLINEAR, PRESSURE, AND VISCOUS TERMS MULTIPLIED BY `R^-2` / THE WEIGHTED DIRICHLET SHELL NUMBER `J_R=R INT_A_R |GRAD U|^2` IS EXACTLY THE `H1` GRADIENT SIZE OF THIS FIXED-ANNULUS RESCALED PROFILE / ON THE PASSIVE SPECTATOR CORRIDOR, UNIFORM RESCALED DERIVATIVE/PRESSURE CONTROL MAKES THE DUHAMEL ERROR INTEGRABLE AND A GIVEN CRITICAL PACKET IS TRANSPORTED OUTWARD WITHOUT RETURNING TO ITS ORIGINAL FIXED SIMILARITY RADIUS / COMBINED WITH M5-562 FIXED-SHELL RECURRENCE, EVERY SURVIVING PASSIVE TAIL MUST THEREFORE BE HISTORICALLY REPLENISHED FROM PROGRESSIVELY SMALLER RADII / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Similarity velocity equation

The backward similarity velocity satisfies

\[
\partial_\theta U
+\frac12U
+\frac12(y\cdot\nabla)U
+(U\cdot\nabla)U
=-\nabla\Pi+\Delta U,
\]

with

\[
\nabla\cdot U=0.
\]

The linear similarity part is exactly the critical dilation operator.

---

## 2. Outward dilation characteristic

Fix a starting similarity time `theta_0` and radius `R_0>0`.

Set

\[
\boxed{
R(\tau)
:=
R_0e^{\tau/2},
\qquad
\theta=\theta_0+\tau.
}
\]

For a fixed annular coordinate `xi`, define

\[
\boxed{
V(\xi,\tau)
:=
R(\tau)
U(R(\tau)\xi,\theta_0+\tau).
}
\]

Also define the critical rescaled pressure

\[
\boxed{
P(\xi,\tau)
:=
R(\tau)^2
\Pi(R(\tau)\xi,\theta_0+\tau).
}
\]

The fixed reference annulus may be taken as

\[
A_1=\{1<|\xi|<2\}
\]

or a slightly enlarged annulus for cutoffs.

---

## 3. Exact characteristic equation

Differentiate `V`.

Because

\[
R'=\frac12R,
\]

we have

\[
\begin{aligned}
\partial_\tau V
&=
\frac12R U
+R\left(
\partial_\theta U
+\frac12y\cdot\nabla U
\right)_{y=R\xi}.
\end{aligned}
\]

Insert the similarity equation.

The two linear terms cancel exactly:

\[
\frac12RU
+R\left(-\frac12U\right)=0.
\]

Under

\[
U(R\xi)=R^{-1}V(\xi),
\]

we have

\[
\nabla_yU=R^{-2}\nabla_\xi V,
\]

\[
(U\cdot\nabla_y)U
=R^{-3}(V\cdot\nabla_\xi)V,
\]

\[
\nabla_y\Pi
=R^{-3}\nabla_\xi P,
\]

and

\[
\Delta_yU
=R^{-3}\Delta_\xi V.
\]

Therefore

\[
\boxed{
\partial_\tau V
=
R(\tau)^{-2}
\left[
\Delta_\xi V
-(V\cdot\nabla_\xi)V
-\nabla_\xi P
\right].
}
\]

Since

\[
R(\tau)^{-2}
=R_0^{-2}e^{-\tau},
\]

all exact PDE corrections to pure dilation carry an exponentially integrable coefficient along the outward characteristic.

---

## 4. Exact weighted-Dirichlet covariance

The spatial gradient transforms as

\[
\nabla_\xi V
=R^2\nabla_yU(R\xi).
\]

Since

\[
dy=R^3d\xi,
\]

we obtain

\[
\begin{aligned}
\int_{A_1}|\nabla_\xi V|^2d\xi
&=
R^4R^{-3}
\int_{A_R}|\nabla_yU|^2dy\\
&=
R\int_{A_R}|\nabla U|^2dy.
\end{aligned}
\]

Hence

\[
\boxed{
\|\nabla_\xi V(\tau)\|_{L^2(A_1)}^2
=
J_{R(\tau)}(\theta_0+\tau),
}
\]

where

\[
\boxed{
J_R(\theta)
:=
R\int_{A_R}|\nabla U(y,\theta)|^2dy.
}
\]

Thus the exact shell quantity controlling failure of global `L3` is the fixed-annulus `H1` gradient size of the dilation-characteristic profile.

This is the central compatibility between the old tail shell ledger and the present recurrence argument.

---

## 5. Spectator residual norm

Write

\[
\boxed{
\mathcal R[V,P]
:=
\Delta V-(V\cdot\nabla)V-\nabla P.
}
\]

On the remote analytic spectator branch, exclude the already typed derivative-frequency, pressure, and active-remote exits and assume a uniform fixed-annulus bound in a norm `X` strong enough to control the weighted Dirichlet profile, for example

\[
\boxed{
\|\mathcal R[V(\tau),P(\tau)]\|_{H^1(A_1^+)}
\le C_{spec}
}
\]

on a slightly enlarged annulus `A_1^+`.

This is not a new free assumption: failure of such a bound is precisely a strong derivative/pressure/remote residual branch already separated in the historical and spectator audits.

---

## 6. Integrable Duhamel error

The exact equation gives

\[
V(\tau)-V(0)
=
\int_0^\tau
R_0^{-2}e^{-s}
\mathcal R[V(s),P(s)]ds.
\]

Therefore

\[
\boxed{
\|V(\tau)-V(0)\|_{H^1(A_1)}
\le
C_{spec}R_0^{-2}
\int_0^\tau e^{-s}ds
\le
C_{spec}R_0^{-2}.
}
\]

The bound is uniform for all future `tau>=0`.

Consequently the scaled critical profile has a finite asymptotic deformation budget along an outward spectator characteristic.

---

## 7. Persistence of a nontrivial packet along its outward path

Suppose initially

\[
\boxed{
J_{R_0}(\theta_0)
=
\|\nabla V(0)\|_2^2
\ge\eta^2.
}
\]

Choose `R_0` so large that

\[
C_{spec}R_0^{-2}
\le\frac\eta2.
\]

Then for every `tau>=0`,

\[
\|\nabla V(\tau)\|_2
\ge
\|\nabla V(0)\|_2
-\|\nabla(V(\tau)-V(0))\|_2
\ge
\frac\eta2.
\]

Hence

\[
\boxed{
J_{R_0e^{\tau/2}}(\theta_0+\tau)
\ge
\frac{\eta^2}{4}.
}
\]

A passive critical packet therefore keeps a fixed fraction of its weighted-Dirichlet strength while its similarity radius grows like

\[
\boxed{R\sim e^{\tau/2}.}
\]

---

## 8. One packet cannot return to the same fixed shell

The characteristic radius is strictly increasing:

\[
R(\tau)=R_0e^{\tau/2}.
\]

After a fixed time

\[
\tau>2\log2,
\]

the characteristic annulus has moved beyond the original dyadic shell.

The Duhamel correction changes its **profile**, but not the characteristic radius chosen to cancel the similarity dilation operator.

Therefore a later positive event at the original fixed radius `R_0` cannot be the same outward characteristic packet.

It must have a different historical origin at smaller radius.

---

## 9. Backward ancestor radius of a fixed-shell recurrence

Suppose the shell at radius `R_*` is active at a later time

\[
\theta_1=\theta_0+T.
\]

The pure dilation characteristic arriving at `R_*` at `theta_1` had radius at `theta_0`

\[
\boxed{
R_{anc}(T)
=R_*e^{-T/2}.
}
\]

For arbitrarily large recurrence gaps

\[
T_j\to\infty,
\]

we have

\[
\boxed{
R_{anc}(T_j)\to0.
}
\]

Thus recurrent fixed-shell activity at arbitrarily late times is historically fed from progressively smaller similarity radii.

---

## 10. Spectator-boundary replenishment lemma

Fix a spectator threshold radius

\[
R_{spec}>R_{core}.
\]

Take a recurrent remote shell

\[
R_*>R_{spec}.
\]

Trace a later shell event backward along the dilation characteristic until it first reaches `R_spec`.

The transit time is

\[
\boxed{
T_{spec}
=2\log\frac{R_*}{R_{spec}}.
}
\]

On the spectator segment, the exact Duhamel error is bounded by

\[
C_{spec}R_{spec}^{-2}.
\]

Therefore if the later remote shell has scaled gradient size

\[
\|\nabla V_{remote}\|_2\ge\eta,
\]

and `R_spec` is chosen so that

\[
C_{spec}R_{spec}^{-2}\le\eta/2,
\]

then at the earlier spectator-boundary time there must have been

\[
\boxed{
\|\nabla V_{boundary}\|_2
\ge\frac\eta2.
}
\]

Equivalently,

\[
\boxed{
J_{R_{spec}}(\theta_1-T_{spec})
\ge\frac{\eta^2}{4}.
}
\]

Thus a positive remote recurrent packet cannot appear from an empty spectator corridor.

It requires a quantitatively nontrivial earlier packet crossing the finite spectator boundary.

---

## 11. Combine with M5-562 recurrence

M5-562 proved that for every arbitrarily remote shell cutoff there exists a fixed finite shell `R_*` and threshold `eta_*>0` whose weighted-Dirichlet activity recurs infinitely often on a typical nontrivial invariant orbit.

Apply the spectator-boundary lemma to every sufficiently remote recurrent event.

Then each such event has a historical ancestor satisfying

\[
\boxed{
J_{R_{spec}}
\ge c(\eta_*)>0
}
\]

at an earlier time.

Since the fixed shell recurs at arbitrarily large times, these boundary-crossing ancestor events also occur arbitrarily far along the complete genealogy.

Therefore

\[
\boxed{
\text{recurrent passive remote shell}
\Longrightarrow
\text{recurrent finite-radius historical replenishment}.
}
\]

---

## 12. Relation to the old persistent-passive survivor

The amplitude-sensitive historical gate left

\[
\text{persistent passive high-ratio tail}
\]

as an honest survivor because ordinary viscosity could pay its Hardy weighted-moment ledger at the correct short-time scale.

M5-563 does not contradict that calculation.

Instead it adds a new geometric fact:

- a persistent remote packet is carried outward;
- a typical recurrent invariant state repeatedly activates the same finite remote shell;
- therefore the persistent genealogy must be continually fed from smaller historical radii.

The correct surviving object is no longer an isolated outward packet.

It is a **conveyor with recurrent replenishment across finite similarity radii**.

---

## 13. What is still not proved

A replenishment event at `R_spec` is not automatically a new material-flux lineage.

It may be generated by:

1. an existing persistent lineage extending a weak tail outward;
2. diffusive regeneration;
3. pressure/nonlocal redistribution;
4. nonlinear transport from the active core;
5. a genuinely new/replacement source packet.

Only the fifth is immediately caught by the finite-memory label ledger.

Therefore the next step must **attribute the finite-radius replenishment flux/action to these PDE channels** rather than rename all replenishment as turnover.

---

## 14. Strong derivative/pressure failure fork

The Duhamel estimate required a uniform spectator residual bound.

If instead

\[
\|\mathcal R[V,P]\|_{H^1(A_1^+)}
\]

is not uniformly bounded on the selected remote packets, then one enters one of the already separated strong branches:

\[
\boxed{
H_{derivative/frequency}
\lor
H_{pressure/remote}
\lor
H_{active\ nonlinear\ tail}.
}
\]

Thus the quiet tail dichotomy is

\[
\boxed{
\text{remote recurrent critical shell}
\Longrightarrow
\text{strong remote residual exit}
\lor
\text{finite-radius historical replenishment}.
}
\]

---

## 15. Highest-value next target

The remaining tail question is now finite-radius:

> At the fixed spectator boundary `R_spec`, decompose the recurrent replenishment event into advective, pressure, viscous, and material-flux channels. Determine whether a fixed amount of recurrent weighted-Dirichlet replenishment can be supplied indefinitely by the already retained finite persistent lineages without either positive flux replacement, positive palinstrophy production, or an active remote/nonlocal exit.

This converts the previous infinite-tail endpoint into a bounded-radius source-attribution problem, matching the same finite-payer philosophy used in M5-497 and M5-553.

---

## 16. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
