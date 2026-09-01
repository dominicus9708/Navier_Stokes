# DSD M5-549 — Anchored parallel channel splits into an amplitude coboundary or material-surface migration cost

Date: 2026-09-01

Status: **ANCHORED PARALLEL-CHANNEL REDUCTION / AFTER M5-548 RESTRICTS EXACT STRAIN-DIFFUSION CANCELLATION TO THE REPRESENTATIVE MATERIAL LINEAGE, THE PARALLEL COMPONENT CAN BE ANALYZED EXACTLY ON THAT MARKER / IF ITS VORTICITY AMPLITUDE REMAINS UNIFORMLY NONDEGENERATE, `D_B log rho = sigma - 1 + (xi dot Delta W)/rho` IS A BOUNDED COBoundary AND RECURRENCE FORCES `mean[sigma + (xi dot Delta W)/rho]=1`; THUS PARALLEL STRAIN AND PARALLEL DIFFUSION CAN ALSO BALANCE WITHOUT EXCESS / IF THE MARKER AMPLITUDE DEGENERATES SO THE LOG COBoundary FAILS, M5-518--522 ROUTE THE LOST CARRIER THROUGH MATERIAL-SURFACE FLUX REDISTRIBUTION, WHICH PAYS A POSITIVE SURFACE-CURRENT/PALINSTROPHY COST / THE ANCHORED BRANCH IS THEREFORE REDUCED TO BOUNDED AMPLITUDE BALANCE OR REPEATED MIGRATION, NOT A FREE THIRD POSSIBILITY / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Exact scalar equation on the anchored material marker

Let `Y(theta)` be one anchored persistent material-lineage marker and write

\[
W(Y(\theta),\theta)=\rho(\theta)\xi,
\]

with

\[
\xi'=0,
\qquad
|\xi|=1.
\]

The similarity vorticity equation along the material trajectory is

\[
D_BW+W=\Sigma W+\Delta W.
\]

Take the scalar product with the fixed direction `xi`.

Define

\[
a:=\xi\cdot\Sigma W=\rho\sigma,
\]

and

\[
b:=\xi\cdot\Delta W.
\]

Then

\[
\boxed{
D_B\rho+\rho=a+b.
}
\]

This is exact on the representative anchored marker.

---

## 2. Logarithmic amplitude form

On intervals where

\[
\rho>0,
\]

divide by `rho`:

\[
\boxed{
D_B\log\rho
=
\sigma-1+
\frac{b}{\rho}.
}
\]

Equivalently,

\[
\boxed{
D_B\log\rho
=
\left(
\sigma+rac{\xi\cdot\Delta W}{\rho}
\right)-1.
}
\]

Thus the effective parallel strain-diffusion eigenvalue is

\[
\boxed{
\lambda_{\parallel}
:=
\sigma+rac{\xi\cdot\Delta W}{\rho}.
}
\]

and

\[
D_B\log\rho=\lambda_{\parallel}-1.
\]

---

## 3. Relation to the magnitude equation

Using

\[
W=\rho\xi,
\]

we have

\[
\xi\cdot\Delta W
=
\Delta\rho
-
\rho|\nabla\xi|^2.
\]

Therefore

\[
\boxed{
D_B\log\rho
=
\sigma-1
+
\frac{\Delta\rho}{\rho}
-
|\nabla\xi|^2.
}
\]

This agrees exactly with the M5-486 similarity magnitude equation.

No extra assumption has been introduced.

---

## 4. Uniformly nondegenerate marker branch

Suppose the retained marker satisfies

\[
\boxed{
0<\rho_-\le\rho(\theta)\le\rho_+<\infty
}
\]

on the recurrent anchored component.

Then

\[
\log\rho
\]

is a bounded scalar observable.

Invariant averaging gives

\[
\left\langle
D_B\log\rho
\right\rangle=0.
\]

Hence

\[
\boxed{
\left\langle
\sigma+rac{\xi\cdot\Delta W}{\rho}
\right\rangle
=1.
}
\]

Thus the parallel channel has its own exact recurrent balance.

---

## 5. Why this is another coboundary, not an excess

The previous identity can be rearranged as

\[
\sigma-1
=
-\frac{\xi\cdot\Delta W}{\rho}
+
D_B\log\rho.
\]

Therefore a positive mean axial stretching `sigma` can be offset by the signed parallel diffusion term together with bounded amplitude oscillation.

There is no sign forcing on

\[
\frac{\xi\cdot\Delta W}{\rho}.
\]

Consequently the parallel channel does not automatically provide the M5-546 strict excess.

On the nondegenerate anchored branch it is another exact bounded coboundary.

---

## 6. First-hitting maximum sub-observation

At an instantaneous local maximum of `rho`,

\[
\nabla\rho=0,
\qquad
\Delta\rho\le0.
\]

Therefore

\[
\frac{\xi\cdot\Delta W}{\rho}
=
\frac{\Delta\rho}{\rho}
-|\nabla\xi|^2
\le0.
\]

If the same point is a genuine upward first-hitting point so that

\[
D_B\rho\ge0,
\]

then the amplitude equation gives

\[
\boxed{
\sigma\ge1.
}
\]

Thus first-hitting events necessarily carry order-one positive axial stretching at the marked maximum.

This is consistent with the earlier M5-453--455 production lower bounds and does not by itself yield a contradiction.

---

## 7. Degenerating marker branch

The logarithmic argument fails if

\[
\inf\rho=0
\]

along the representative marker.

M5-518 already audited that

\[
\rho(Y(\theta),\theta)\to0
\]

does **not** imply that the material-flux lineage disappears.

The active vorticity carrier may migrate to another location on the same material surface.

Therefore marker degeneration cannot be classified as lineage replacement without further work.

---

## 8. Route degeneration through the surface-flux law

M5-520 gives the exact material-surface flux-density equation

\[
D_Bf
+(1-\sigma_n)f
=
-\operatorname{div}_\Sigma J_\Sigma,
\]

where

\[
f=W\cdot n
\]

and

\[
J_\Sigma
=(\nabla\times W)\times n
\]

is the viscous surface current.

M5-521 shows that transporting a fixed amount of flux across a fixed material-label distance requires a fixed integrated surface-current action.

M5-522 then thickens such recurrent current into a positive three-dimensional palinstrophy charge.

Thus repeated marker degeneration/migration is not free.

---

## 9. Exact anchored dichotomy

The anchored lineage therefore satisfies

\[
\boxed{
\mathcal B_{anchor}
\Longrightarrow
\mathcal B_{amp}^{nondeg}
\lor
\mathcal B_{migration}^{surface}.
}
\]

### Nondegenerate amplitude branch

\[
\boxed{
\left\langle
\sigma+rac{\xi\cdot\Delta W}{\rho}
\right\rangle=1.
}
\]

The parallel channel is a bounded amplitude coboundary.

### Migration branch

Repeated loss of the representative amplitude while preserving material flux forces recurrent surface-current/palinstrophy cost.

No third quiet branch remains at the marker level.

---

## 10. Combine with the transverse scope correction

M5-548 leaves a positive-volume near-recycling tube around an active anchored marker but not global core cancellation.

M5-549 adds the exact scalar statement along the central lineage.

Hence the anchored structure is now:

\[
\boxed{
\begin{aligned}
&\text{transverse: exact at marker, near-recycled on active tube},\\
&\text{parallel: amplitude coboundary if marker nondegenerate},\\
&\text{otherwise: material-surface migration cost}.
\end{aligned}
}
\]

This is the correct branch-local structure after the DSD scope audit.

---

## 11. Why the migration branch is not yet closed

M5-522 converts recurrent surface current into positive palinstrophy.

But M5-544 shows the recurrent finite core can regenerate positive palinstrophy through its derivative nonlinearity.

Therefore migration cost is still a **priced** branch, not a contradiction.

To close it one must show that some part of the surface-current cost is not recyclable by the core production ledger.

---

## 12. Updated final-core alternatives

The most difficult anchored core has now been reduced to two mechanisms:

1. **balanced nondegenerate anchored marker** — transverse near-recycling plus the exact parallel amplitude mean `lambda_parallel=1`;
2. **recurrent material-surface migration** — positive viscous current and palinstrophy repeatedly move the active flux carrier.

Both live entirely inside the finite active core established by M5-543.

The endpoint non-`L3` spectator tail is no longer involved in this split.

---

## 13. Highest-value next target

For the nondegenerate anchored branch, combine the first-hitting inequality

\[
\sigma\ge1
\]

with the trace-free symmetric-strain geometry to obtain a **sharp local strain-energy floor**.

For a unit direction `xi`, writing

\[
\Sigma\xi=\sigma\xi+\tau
\]

and `tr Sigma=0` gives the pointwise matrix inequality

\[
\boxed{
|\Sigma|^2
\ge
\frac32\sigma^2
+2|\tau|^2.
}
\]

At recurrent first-hitting events this yields a fixed local strain cost, while the anchored transverse relation simultaneously ties `tau` to projected diffusion.

The next audit should determine whether two persistent noncollinear anchored lineages force a strain budget larger than the available enstrophy/Riesz budget, or merely another quantitative threshold.

---

## 14. Status

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]