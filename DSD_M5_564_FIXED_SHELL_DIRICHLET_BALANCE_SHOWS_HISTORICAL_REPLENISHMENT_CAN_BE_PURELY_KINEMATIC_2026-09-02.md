# DSD M5-564 — Fixed-shell Dirichlet balance shows historical replenishment can be purely kinematic

Date: 2026-09-02

Status: **ANTI-SHORTCUT CORRECTION / M5-563 FIXED-SHELL HISTORICAL REPLENISHMENT IS REAL AS A GENEALOGICAL STATEMENT, BUT IT CANNOT AUTOMATICALLY BE CHARGED AS PHYSICAL CORE-TO-TAIL TURNOVER / ON A FIXED SIMILARITY ANNULUS, THE CRITICAL WEIGHTED DIRICHLET PROFILE HAS AN EXACT BALANCE IN WHICH THE LINEAR SIMILARITY DILATION PRODUCES AN INNER-BOUNDARY INFLOW AND OUTER-BOUNDARY OUTFLOW OF ORDER ONE, WHILE THE TRUE NAVIER--STOKES NONLINEAR/PRESSURE/VISCOUS SOURCE IS SUPPRESSED BY `R^-2` / A HOMOGENEOUS `-1` CRITICAL PROFILE CAN MAINTAIN A STATIONARY FIXED-SHELL `J_R` ENTIRELY THROUGH THIS KINEMATIC DILATION FLUX / THEREFORE FULL-STATE RECURRENCE FORCES A HISTORICAL SCALE CONVEYOR BUT DOES NOT BY ITSELF FORCE A NEW MATERIAL LINEAGE OR A POSITIVE PDE TURNOVER COST / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Why this audit is necessary

M5-562 showed that a typical nontrivial invariant state has recurrent positive activity on fixed remote shells.

M5-563 showed that an individual passive critical packet moves outward under the similarity dilation characteristic, so repeated activity of the same fixed shell must be historically supplied from smaller radii.

It is tempting to interpret that supply as a physical core-to-tail transfer event.

That interpretation is not automatic.

Similarity coordinates themselves contain a radial dilation transport.

The purpose of M5-564 is to separate:

1. kinematic replenishment caused by the changing similarity scale;
2. genuine Navier--Stokes nonlinear/pressure/viscous source action.

---

## 2. Fixed-radius critical profile

Fix a large similarity radius `R` and define on a fixed annular coordinate `xi`

\[
\boxed{
V_R(\xi,\theta)
:=
R\,U(R\xi,\theta),
}
\]

and

\[
\boxed{
P_R(\xi,\theta)
:=
R^2\Pi(R\xi,\theta).
}
\]

Unlike M5-563, `R` is now constant in time.

The similarity velocity equation becomes exactly

\[
\boxed{
\partial_\theta V_R
+\frac12\left(V_R+\xi\cdot\nabla V_R\right)
=
R^{-2}
\left[
\Delta V_R
-(V_R\cdot\nabla)V_R
-\nabla P_R
\right].
}
\]

Define

\[
\mathcal N_R
:=
\Delta V_R
-(V_R\cdot\nabla)V_R
-\nabla P_R.
\]

---

## 3. Gradient equation

Let

\[
G_R:=\nabla V_R.
\]

Differentiate the fixed-profile equation.

Since

\[
\nabla(\xi\cdot\nabla V_R)
=G_R+\xi\cdot\nabla G_R,
\]

we obtain

\[
\boxed{
\partial_\theta G_R
+G_R
+\frac12\xi\cdot\nabla G_R
=
R^{-2}\nabla\mathcal N_R.
}
\]

Thus the critical gradient has a linear dilation transport plus an `R^-2` PDE correction.

---

## 4. Localized weighted Dirichlet number

Choose a smooth radial cutoff `chi` supported in a slightly enlarged reference annulus, equal to one on

\[
A_1=\{1<|\xi|<2\}.
\]

Define

\[
\boxed{
J_{R,\chi}(\theta)
:=
\int\chi(\xi)|G_R(\xi,\theta)|^2d\xi.
}
\]

Up to fixed cutoff comparability, this is the weighted shell Dirichlet number

\[
R\int_{A_R}|\nabla U|^2dy.
\]

---

## 5. Exact fixed-shell balance

Multiply the gradient equation by `chi G_R` and integrate.

The time term is

\[
\frac12J_{R,\chi}'.
\]

For the dilation transport,

\[
G_R:\left(\xi\cdot\nabla G_R\right)
=\frac12\xi\cdot\nabla|G_R|^2.
\]

Therefore

\[
\int\chi G_R:\left(\frac12\xi\cdot\nabla G_R\right)
=
\frac14\int\chi\,\xi\cdot\nabla|G_R|^2.
\]

Since

\[
\nabla\cdot\xi=3,
\]

integration by parts gives

\[
\int\chi\,\xi\cdot\nabla|G_R|^2
=-3J_{R,\chi}
-\int(\xi\cdot\nabla\chi)|G_R|^2.
\]

Combining terms yields

\[
\boxed{
\frac12J_{R,\chi}'
+\frac14J_{R,\chi}
=
\frac14
\int(\xi\cdot\nabla\chi)|G_R|^2d\xi
+
R^{-2}
\int\chi G_R:\nabla\mathcal N_Rd\xi.
}
\]

This is the exact fixed-shell critical Dirichlet balance.

---

## 6. Inner and outer dilation boundary flux

For a standard annular cutoff:

- `chi` rises from zero to one across the inner transition;
- `chi` falls from one to zero across the outer transition.

Hence

\[
\xi\cdot\nabla\chi>0
\]

on the inner transition and

\[
\xi\cdot\nabla\chi<0
\]

on the outer transition.

Define

\[
\boxed{
\mathcal F_{dil}(R)
:=
\frac14
\int(\xi\cdot\nabla\chi)|G_R|^2d\xi.
}
\]

It is the net **similarity-dilation influx minus outflux** through the annular cutoff.

This term is order one at critical scale.

It carries no `R^-2` prefactor.

---

## 7. Genuine PDE source is subcritical at large radius

Define

\[
\boxed{
\mathcal S_{PDE}(R)
:=
\int\chi G_R:\nabla\mathcal N_Rd\xi.
}
\]

Then

\[
\boxed{
\frac12J_{R,\chi}'
+\frac14J_{R,\chi}
=
\mathcal F_{dil}(R)
+R^{-2}\mathcal S_{PDE}(R).
}
\]

On the passive spectator corridor, rescaled derivative/pressure bounds give

\[
|\mathcal S_{PDE}(R)|\le C_{spec}.
\]

Therefore

\[
\boxed{
R^{-2}\mathcal S_{PDE}(R)
=O(R^{-2}).
}
\]

At large radius, fixed-shell critical activity is therefore balanced primarily by the linear dilation boundary flux, not by a large physical PDE source.

---

## 8. Invariant-average identity

On a recurrent invariant component, the bounded localized observable `J_R,chi` has zero mean time derivative:

\[
\left\langle J_{R,\chi}'\right\rangle=0.
\]

Hence

\[
\boxed{
\frac14\left\langle J_{R,\chi}\right\rangle
=
\left\langle\mathcal F_{dil}(R)\right\rangle
+R^{-2}\left\langle\mathcal S_{PDE}(R)\right\rangle.
}
\]

For large spectator radius,

\[
\boxed{
\left\langle\mathcal F_{dil}(R)\right\rangle
=
\frac14\left\langle J_{R,\chi}\right\rangle
+O(R^{-2}).
}
\]

Thus recurrent shell activity naturally requires recurrent inward historical scale flux through the annulus.

But that flux is a similarity-coordinate transport term.

---

## 9. Exact critical model showing no PDE cost is necessary

Consider a formal velocity profile homogeneous of degree `-1`:

\[
U(\lambda y)=\lambda^{-1}U(y).
\]

Then

\[
y\cdot\nabla U=-U,
\]

so the linear similarity term satisfies

\[
\boxed{
\frac12(U+y\cdot\nabla U)=0.
}
\]

At the pure linear-conveyor level, such a profile is stationary in similarity coordinates.

Its shell gradient energy scales as

\[
\int_{A_R}|\nabla U|^2dy\sim R^{-1},
\]

so

\[
\boxed{J_R\sim1.}
\]

at every dyadic scale.

For the fixed-annulus balance with zero PDE residual,

\[
J_{R,\chi}'=0
\]

is paid exactly by

\[
\boxed{
\mathcal F_{dil}(R)
=\frac14J_{R,\chi}.
}
\]

Thus a scale-critical shell stack can maintain fixed-shell recurrence by pure similarity dilation bookkeeping.

No new material label or order-one nonlinear source is required by this balance alone.

This is an algebraic critical-tail model, not a claim that a nonzero smooth entire homogeneous `-1` Navier--Stokes profile exists.

---

## 10. Correct interpretation of historical replenishment

M5-563's statement

\[
\text{fixed remote shell recurrence}
\Longrightarrow
\text{historical replenishment from smaller radii}
\]

remains correct.

M5-564 corrects its interpretation:

\[
\boxed{
\text{historical replenishment}
\not\Rightarrow
\text{physical core-to-tail turnover cost}.
}
\]

The historical ancestor at smaller similarity radius may simply be the predecessor of the same scale-conveyor architecture under renormalization.

This is a genealogy across scales, not necessarily a transport of physical energy from the center to infinity.

---

## 11. Why finite-memory does not automatically apply

The finite-memory ledger counts distinguishable material-flux lineages and replacement events.

The dilation boundary term

\[
\mathcal F_{dil}
\]

does not create a new material lineage.

It merely changes which physical scale is represented by a fixed similarity shell as the normalization length shrinks.

Therefore one cannot charge every recurrent shell crossing to

\[
R_j=1
\]

in the M5-488 replacement ledger.

Doing so would conflate similarity-scale genealogy with material-flux genealogy.

DSD audit forbids that identification.

---

## 12. What a genuine closure would now require

To turn the recurrent critical conveyor into a contradiction, one needs a theorem that uses something beyond the kinematic fixed-shell balance.

Possible genuine rigidity channels are:

1. show that a two-sided recurrent critical conveyor coupled to a smooth finite-enstrophy core must become exactly backward self-similar or discretely self-similar, then apply an appropriate Liouville theorem;
2. show that the transition between a smooth core and an asymptotically homogeneous `-1` tail requires a non-integrable PDE residual;
3. derive a global weighted flux identity whose boundary term cannot be paid indefinitely by the critical dilation stack;
4. prove enough spatial tail summability to recover global `L3` and invoke M5-561.

The local annular recurrence balance alone cannot do this.

---

## 13. Updated tail hard core

The surviving tail is now typed more precisely as

\[
\boxed{
\begin{gathered}
\text{nontrivial recurrent finite-enstrophy similarity core},\\
\text{global }L3\text{ failure},\\
\sum_kJ_k^{3/2}=\infty,\qquad\sum_kR_k^{-1}J_k<\infty,\\
\text{fixed-shell recurrence at arbitrarily remote finite radii},\\
\text{and an asymptotically passive dilation conveyor that can recycle}\n
\text{the weighted Dirichlet profile kinematically across scales.}
\end{gathered}
}
\]

This is narrower than the original diffuse-tail endpoint but remains logically consistent with the current estimates.

---

## 14. Highest-value next target

The next efficient question is whether known backward self-similar or discretely self-similar Navier--Stokes Liouville results already exclude a recurrent critical `-1` conveyor under the inherited global `L6`/finite-enstrophy assumptions.

If existing theorems require only conditions already inherited here, they may remove the stationary/log-periodic subbranches immediately.

If not, the exact gap should be recorded and the aperiodic recurrent conveyor isolated as the final tail endpoint.

---

## 15. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
