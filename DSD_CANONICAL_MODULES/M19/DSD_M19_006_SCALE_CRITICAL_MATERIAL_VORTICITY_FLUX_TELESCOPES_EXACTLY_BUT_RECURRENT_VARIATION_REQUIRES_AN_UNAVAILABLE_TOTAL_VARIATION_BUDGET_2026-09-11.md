# M19-006 — Scale-critical material vorticity flux telescopes exactly, but recurrent variation requires an unavailable total-variation budget

**Date:** 2026-09-11  
**Status:** CALCULATION / R-AC SCALE-CRITICAL SIGNED TEST / EXACT FLUX COBBOUNDARY / TOTAL-VARIATION BARRIER

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-005 closes the remaining-time clock as a signed ancestry shortcut because parent conversion inserts the exact geometric discount.

The next candidate is materially transported vorticity flux.

Unlike stage duration, vorticity flux is scale critical under Navier--Stokes parabolic scaling. Therefore it does not acquire a geometric ancestry weight merely from rerecording at another scale.

This makes it the natural candidate for a signed R-AC conversion.

The present calculation shows:

\[
\boxed{
\text{scale criticality removes the geometric discount, but bounded flux recurrence still telescopes.}
}
\]

Hence infinitely many fixed signed variations require sign reversal and infinite total variation. No certified finite original-parent total-variation budget is presently available.

## 2. Physical material flux identity

Let \(S(t)\) be an oriented material surface transported by the incompressible velocity field, with boundary \(\partial S(t)\).

Define the signed vorticity flux

\[
\boxed{
\Phi(t)
:=
\int_{S(t)}\omega\cdot n\,dA.
}
\]

By Stokes,

\[
\Phi(t)
=
\oint_{\partial S(t)}u\cdot dl.
\]

For viscous incompressible Navier--Stokes,

\[
\boxed{
\frac{d}{dt}\Phi(t)
=
\nu\int_{S(t)}\Delta\omega\cdot n\,dA.
}
\]

The stretching contribution is cancelled by the material deformation of the surface element. This is the physical version of the material-flux identity already used in the M5/M18 lineage analysis.

## 3. Scale criticality

Under parabolic scaling at length \(r\),

\[
\omega_r(y,s)
=r^2\omega(ry,r^2s),
\]

while

\[
dA_y=r^{-2}dA_x.
\]

Therefore

\[
\boxed{
\Phi_r=\Phi.
}
\]

The material vorticity flux has homogeneity zero.

Thus a fixed normalized flux change corresponds to a fixed physical-parent flux change. There is no factor such as

\[
r_j,\quad R_j^{-1},\quad q^{-j}
\]

coming from scale conversion alone.

This is precisely the favorable homogeneity missing from the unsigned resources audited in M18-059.

## 4. Exact parent telescoping

Sample one persistent material lineage at times

\[
t_0<t_1<\cdots<t_N.
\]

Write

\[
\Phi_j:=\Phi(t_j),
\qquad
\Delta\Phi_j:=\Phi_{j+1}-\Phi_j.
\]

Because every \(\Phi_j\) is already a physical-parent scale-critical observable,

\[
\boxed{
\sum_{j=0}^{N-1}\Delta\Phi_j
=
\Phi_N-\Phi_0.
}
\]

No ancestry conversion factor appears.

Thus this is a genuine fixed-parent signed coboundary.

## 5. One-sign fixed increments are impossible on a bounded recurrent lineage

Suppose the compact persistent-lineage branch gives

\[
|\Phi_j|\le\Phi_*<\infty.
\]

If infinitely many events satisfied

\[
\Delta\Phi_j\ge\phi_*>0
\]

with no compensating negative increments, then

\[
\Phi_N\to+\infty,
\]

contradicting bounded recurrence.

Likewise an infinite one-sign negative drift is impossible.

Therefore

\[
\boxed{
\text{fixed recurrent flux variation}
\Longrightarrow
\text{compensating opposite-sign flux variation}
}
\]

on every bounded persistent flux lineage.

This is a genuine signed restriction unavailable to unsigned payers.

## 6. Fixed recurrent variation forces divergent total variation

Suppose there are infinitely many pairwise separated flux-change events with

\[
|\Delta\Phi_j|\ge\phi_*>0.
\]

Then

\[
\boxed{
\sum_j|\Delta\Phi_j|=\infty.
}
\]

Equivalently the flux path has infinite discrete total variation along the event sequence.

In continuous time,

\[
\operatorname{Var}_{[t_0,T^*)}\Phi
\ge
\int_{t_0}^{T^*}|\Phi'(t)|dt
\]

with equality when the flux is absolutely continuous in the retained smooth interval; in any case fixed alternating increments force unbounded variation along the sampled partition.

Using the flux equation,

\[
\boxed{
|\Phi'(t)|
=
\nu\left|
\int_{S(t)}\Delta\omega\cdot n\,dA
\right|.
}
\]

Thus a contradiction would follow from a universal finite original-parent bound on the absolute diffusive flux variation.

## 7. The missing budget

The finite kinetic-energy dissipation budget controls

\[
\int_0^{T^*}\|\omega(t)\|_2^2dt<\infty.
\]

It does **not** directly control

\[
\int_0^{T^*}
\left|
\int_{S(t)}\Delta\omega\cdot n\,dA
\right|dt.
\]

A trace estimate for the surface integral naturally requires spatial derivatives above the energy-dissipation level and geometry control of the moving surface.

Those higher derivative totals are precisely the resources for which M18-059 found no finite original-parent budget.

Therefore the currently certified energy identity does not imply

\[
\boxed{
\operatorname{Var}_{[t_0,T^*)}\Phi<\infty.
}
\]

The signed scale-critical flux candidate consequently reaches a **total-variation barrier** rather than a contradiction.

## 8. CE-H tube form

On an exact CE-H material vortex tube in viscosity-one similarity normalization, M18 supplies

\[
D_B\log|\Phi|=\kappa
\]

as long as the oriented flux remains nonzero.

Hence between two material times

\[
\boxed{
\log\frac{|\Phi(t_2)|}{|\Phi(t_1)|}
=
\int_{t_1}^{t_2}\kappa\,d\theta.
}
\]

If

\[
0<\Phi_-\le|\Phi|\le\Phi_+<\infty
\]

on a recurrent persistent tube, then its long-time mean logarithmic drift vanishes:

\[
\boxed{
\langle\kappa\rangle_{tube}=0.
}
\]

This is consistent with the M18 residence/covariance architecture: positive flux recharge must be balanced by negative coefficient phases. It is not a one-sign drift.

## 9. Fixed multiplicative cycles also force total variation, not state drift

Suppose recurrent flux cycles alternate between levels whose ratio is bounded away from one, for example

\[
\frac{\Phi_{high}}{\Phi_{low}}\ge1+\delta.
\]

Then every completed up/down cycle satisfies

\[
\int_{cycle}|\kappa|d\theta
\ge
2\log(1+\delta).
\]

Infinitely many cycles imply infinite material \(|\kappa|\)-action along that lineage.

But no finite original-parent bound on this linewise absolute coefficient action is currently certified.

Thus replacing additive flux variation by logarithmic flux variation does not remove the same barrier.

## 10. Interaction with finite label storage

Finite-memory lineage saturation controls the **number of distinct fixed-flux populations** and prices replacement/export.

It does not make the total variation of the flux of one already persistent label finite.

Once the label is reused, oscillations such as

\[
\Phi_a\leftrightarrow\Phi_b\leftrightarrow\Phi_a\leftrightarrow\cdots
\]

are compatible with bounded storage.

Therefore

\[
\boxed{
\text{finite number of labels}
\neq
\text{finite variation of each label's flux}.
}
\]

## 11. M19-006 verdict

### Genuine gain

Material vorticity flux is a true scale-critical parent observable. Its signed increments do not suffer the geometric ancestry discount.

### Exact restriction

On a bounded recurrent persistent lineage, infinitely many fixed one-sign increments are impossible.

### Remaining barrier

The surviving mechanism is sign-reversing flux variation with

\[
\sum_j|\Delta\Phi_j|=\infty.
\]

No finite original-parent total-variation budget for this diffusive flux is presently certified.

Therefore

\[
\boxed{
\text{scale-critical signed flux}
\Longrightarrow
\text{one-sign exhaustion}
\lor
\text{infinite sign-reversing variation},
}
\]

and only the first branch is closed by bounded recurrence.

## 12. Next calculation

M19-007 should ask whether the remaining infinite flux variation can be priced by any already finite parent quantity.

The relevant candidates are:

1. kinetic-energy dissipation;
2. circulation/flux boundary trace estimates;
3. helicity-type scale-critical signed balances;
4. the finite-population strain/interface/coefficient defect decomposition of M19-001--004.

If none gives a finite total-variation budget, the correct conclusion is a signed-candidate exhaustion theorem and the R-AC attack must move from budget summation to a direct return-weight/transport theorem.

---

\[
\boxed{\text{M19-006 COMPLETE; SCALE-CRITICAL SIGNED FLUX ALONE DOES NOT CLOSE R-AC.}}
\]
