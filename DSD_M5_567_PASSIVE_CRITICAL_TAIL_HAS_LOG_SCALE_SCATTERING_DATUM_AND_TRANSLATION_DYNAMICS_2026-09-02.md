# DSD M5-567 — Passive critical tail has a log-scale scattering datum and translation dynamics

Date: 2026-09-02

Status: **TAIL SCATTERING REDUCTION / THE `R^-2` INTEGRABILITY OF THE EXACT DILATION-CHARACTERISTIC RESIDUAL DOES NOT ONLY CONTROL ONE PACKET: IT PRODUCES AN ASYMPTOTIC CRITICAL SCATTERING DATUM `A(q,OMEGA)` FOR EVERY PASSIVE SPECTATOR TRAJECTORY, WHERE `q=LOG R-THETA/2` IS THE CHARACTERISTIC INVARIANT / THE FULL FAR FIELD IS `U=R^-1 A(LOG R-THETA/2,OMEGA)+O(R^-3)` IN THE RETAINED FIXED-ANNULUS NORM / SIMILARITY TIME SHIFT ACTS ON THE DATUM BY LOG-SCALE TRANSLATION `A_{SIGMA_tY}(q)=A_Y(q-t/2)` / EXACT SELF-SIMILAR, DSS, AND APERIODIC RECURRENT TAILS ARE THEREFORE CONSTANT, PERIODIC, AND APERIODIC TRANSLATION DYNAMICS OF THE SAME SCATTERING OBJECT / FINITE ENSTROPHY IS COMPATIBLE WITH ANY BOUNDED NONZERO DATUM BECAUSE OF AN EXPONENTIAL LOG-RADIUS WEIGHT, WHILE GLOBAL `L3` IS THE UNWEIGHTED LOG-RADIUS INTEGRABILITY CONDITION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Exact outward characteristic revisited

For a complete similarity solution `Y`, choose any starting pair

\[
(R_0,\theta_0)
\]

in the passive spectator regime and set

\[
R(\tau)=R_0e^{\tau/2}.
\]

Define

\[
V_{R_0,\theta_0}(\xi,\tau)
:=
R(\tau)
U_Y(R(\tau)\xi,\theta_0+\tau).
\]

M5-563 gives the exact equation

\[
\boxed{
\partial_\tau V
=
R_0^{-2}e^{-\tau}
\mathcal R[V,P].
}
\]

On the quiet spectator corridor,

\[
\boxed{
\|\mathcal R[V,P]\|_X
\le C_{spec}
}
\]

uniformly in the fixed-annulus norm `X`.

---

## 2. Existence of an asymptotic profile along every characteristic

For

\[
\tau_2>\tau_1,
\]

Duhamel gives

\[
\begin{aligned}
\|V(\tau_2)-V(\tau_1)\|_X
&\le
C_{spec}R_0^{-2}
\int_{\tau_1}^{\tau_2}e^{-s}ds\\
&\le
C_{spec}R_0^{-2}e^{-\tau_1}.
\end{aligned}
\]

Therefore `V(tau)` is Cauchy as

\[
\tau\to+\infty.
\]

There exists

\[
\boxed{
A_{R_0,\theta_0}(\xi)
:=
\lim_{\tau\to\infty}
V_{R_0,\theta_0}(\xi,\tau)
}
\]

with

\[
\boxed{
\|V(\tau)-A_{R_0,\theta_0}\|_X
\le
C_{spec}R_0^{-2}e^{-\tau}.
}
\]

---

## 3. The characteristic invariant

Along the outward path,

\[
\log R(\tau)
-\frac{\theta_0+\tau}{2}
=
\log R_0-rac{\theta_0}{2}.
\]

Define

\[
\boxed{
q
:=
\log R_0-rac{\theta_0}{2}.
}
\]

If one chooses another starting point on the same characteristic, the Duhamel limits agree because the later tail of the trajectory is identical.

Hence the asymptotic profile depends on the characteristic only through `q`.

We may therefore write

\[
\boxed{
A_Y(q,\cdot).
}
\]

After restricting the fixed-annulus variable to the unit sphere or an equivalent angular/radial phase representation, this is the **log-scale tail scattering datum**.

---

## 4. Reconstruction of the tail from the scattering datum

Take a point `(r,theta)` with

\[
\rho=\log r
\]

large enough to lie in the spectator region.

Its outward characteristic invariant is

\[
q=\rho-\frac\theta2.
\]

Starting at this point and taking the future limit gives

\[
\left\|
 rU_Y(r\,\cdot,\theta)
-A_Y\left(\rho-\frac\theta2,\cdot\right)
\right\|_X
\le
Cr^{-2}.
\]

Therefore

\[
\boxed{
U_Y(y,\theta)
=
\frac1{|y|}
A_Y\left(
\log|y|-\frac\theta2,
\frac y{|y|}
\right)
+O_X(|y|^{-3}).
}
\]

The exact form of the angular/radial phase coordinate depends on the chosen fixed-annulus representation, but the characteristic invariant and decay order are canonical.

---

## 5. Time-shift covariance

Let

\[
Y_t:=\sigma_tY.
\]

Then

\[
U_{Y_t}(y,\theta)
=U_Y(y,\theta+t).
\]

For the shifted trajectory, a characteristic labeled by `q` corresponds in the original trajectory to

\[
q-\frac t2.
\]

Therefore

\[
\boxed{
A_{\sigma_tY}(q,\omega)
=
A_Y\left(q-\frac t2,\omega\right).
}
\]

Thus similarity time translation acts on the asymptotic tail by ordinary translation in log-scale scattering coordinate.

This is an exact covariance law for the scattering data.

---

## 6. Three recurrence types become one translation classification

The tail hierarchy can now be expressed entirely in terms of `A_Y`.

### Exact self-similar

If

\[
\sigma_tY=Y
\qquad\forall t,
\]

then

\[
A_Y(q-t/2)=A_Y(q)
\qquad\forall t,
\]

so

\[
\boxed{A_Y\text{ is constant in }q.}
\]

M5-565 closes the nontrivial stationary branch by the self-similar `L6` Liouville theorem.

### DSS

If

\[
\sigma_TY=Y,
\]

then

\[
A_Y(q-T/2)=A_Y(q).
\]

Thus

\[
\boxed{A_Y\text{ is periodic in }q\text{ with period }T/2=\log\lambda.}
\]

This recovers M5-566.

### Aperiodic recurrent

If the hull orbit is recurrent but not periodic, its tail datum undergoes an aperiodic translation dynamics in `q`.

This is the genuinely new remaining class.

---

## 7. Divergence-free constraint

Write the leading scattering amplitude as

\[
A(q,\omega)
=A_r(q,\omega)\omega
+A_T(q,\omega),
\qquad
A_T\cdot\omega=0.
\]

Since

\[
U=r^{-1}A(\log r-\theta/2,\omega)+O(r^{-3})
\]

and `div U=0`, the leading amplitude satisfies

\[
\boxed{
\partial_qA_r
+A_r
+\operatorname{div}_{S^2}A_T
=0.
}
\]

Integrating over the sphere gives

\[
\partial_q
\int_{S^2}A_r\,d\omega
+
\int_{S^2}A_r\,d\omega
=0.
\]

A bounded recurrent or periodic datum therefore has zero net radial flux:

\[
\boxed{
\int_{S^2}A_r(q,\omega)d\omega=0.
}
\]

This agrees with the absence of a velocity source at the origin.

---

## 8. Finite enstrophy is exponentially weighted in `q`

For a critical tail

\[
U\sim r^{-1}A(q,\omega),
\]

we have

\[
|\nabla U|^2
\sim r^{-4}\mathcal D[A](q,\omega),
\]

where `mathcal D[A]` is a quadratic log-radial/angular derivative density.

Using

\[
dy=r^3d(\log r)d\omega,
\]

the tail Dirichlet integral is schematically

\[
\boxed{
\int_{r>R}|\nabla U|^2dy
\sim
\int_{\log R}^{\infty}
 e^{-q}
\mathcal D[A](q,\omega)
\,dq\,d\omega
}
\]

up to the fixed time shift in `q`.

Therefore any bounded recurrent datum can have finite global enstrophy because the log-radius measure carries the exponentially decaying factor `e^-q`.

This explains why finite enstrophy alone does not suppress a persistent critical scattering profile.

---

## 9. Global L3 is unweighted log-scale integrability

For the same leading tail,

\[
|U|^3
\sim r^{-3}|A(q,\omega)|^3.
\]

Since

\[
r^2dr=r^3dq,
\]

we get

\[
\boxed{
\int_{r>R}|U|^3dy
\sim
\int_{\log R}^{\infty}
|A(q,\omega)|^3dq\,d\omega.
}
\]

Thus the critical difference between finite enstrophy and global `L3` becomes transparent:

\[
\boxed{
\begin{aligned}
\text{finite enstrophy}
&\sim
A\text{ square-integrable with exponential }e^{-q}\text{ weight},\\
\text{global }L3
&\sim
A\in L^3(dq\,d\omega)
\text{ without exponential weight}.
\end{aligned}
}
\]

A bounded nondecaying recurrent scattering datum is therefore exactly compatible with the first condition and incompatible with the second.

---

## 10. M5-562 in scattering language

M5-562 proved that on every nontrivial invariant ergodic component,

\[
\|U_Y\|_3=\infty
\quad\mu\text{-a.e.}
\]

Hence, on the passive scattering branch,

\[
\boxed{
A_Y\notin L^3([q_0,\infty)\times S^2)
\quad\mu\text{-a.e.}
}
\]

for every sufficiently remote `q_0`.

Thus the old critical shell obstruction is equivalent to a nonintegrable log-scale scattering datum.

---

## 11. Boundary-history interpretation

Fix a spectator boundary radius

\[
R_{spec}=e^{\rho_{spec}}.
\]

A characteristic labeled by `q` crosses this boundary when

\[
q
=
\rho_{spec}-\frac{\theta_{cross}}2.
\]

Therefore

\[
\boxed{
\theta_{cross}
=2(\rho_{spec}-q).
}
\]

Up to the small spectator Duhamel correction, `A_Y(q)` is the outgoing critical profile recorded at the finite spectator boundary at historical time `theta_cross`.

The entire infinite tail can therefore be viewed as a re-encoding of the complete time history of one finite-radius boundary.

This is a major dimensional reduction of the tail genealogy.

---

## 12. Important topology firewall

The compact similarity hull is compact in a **local spatial topology**.

The scattering datum lives at spatial infinity.

Therefore the map

\[
Y\mapsto A_Y
\]

must not be assumed continuous merely from local hull compactness.

The exact covariance law is valid trajectory by trajectory on the spectator branch, but a topological recurrence statement for `Y` does not automatically imply recurrence of the entire infinite `q`-profile in a strong global scattering topology.

M5-562 avoided this problem by applying recurrence only to fixed finite shells, which are local observables.

This firewall remains necessary.

---

## 13. Revised final tail object

The passive ancient tail is now encoded by

\[
\boxed{
A_Y(q,\omega)
}
\]

with:

\[
\boxed{
\begin{aligned}
&A_{\sigma_tY}(q)=A_Y(q-t/2),\\
&\partial_qA_r+A_r+\operatorname{div}_{S^2}A_T=0,\\
&A_Y\notin L^3_qL^3_\omega\quad\text{on the nontrivial recurrent component},\\
&\int e^{-q}\mathcal D[A_Y]dq<\infty.
\end{aligned}
}
\]

Exact self-similar and DSS tails are merely constant and periodic special cases of this translation system.

---

## 14. Highest-value next target

The infinite-tail PDE problem has now been reduced to a finite-radius history problem:

> Can the recurrent finite core generate a bounded non-`L3` log-scale scattering record `A_Y(q)` for all historical times while all already-audited core/lineage/flux ledgers remain recurrent with zero excess?

Equivalently, characterize the outgoing spectator-boundary trace as a function of similarity time and determine whether the finite persistent lineage architecture can support a nondecaying translation-recurrent trace indefinitely.

This is more concrete than separately tracking infinitely many dyadic shells.

---

## 15. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
