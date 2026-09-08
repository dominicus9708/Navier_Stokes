# DSD M17-438 — Compact analytic zero-transition bundle has a uniform finite jet order and with M17-437 extends the `R^3/log R` closure to all finite-order zero crossings

Date: 2026-09-08  
Canonical ID: **M17-438**

Status: **CONDITIONAL ALL-FINITE-ORDER ZERO-TRANSITION CLOSURE / COMPACT ANALYTIC TRANSITION-BUNDLE THEOREM**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Inputs

M17-434 proves that a positive-flux own-scale sign-preserving coefficient phase can occupy at most `O(log R)` own-time units before exponential flux excursion defeats the cubic raw-`H2` ancestry discount.

M17-435 closes the resulting repeated sign transitions when each zero crossing is first-order regular and has bounded normalized transition speed.

M17-436 retypes failure of normalized transition-speed boundedness as coefficient/strain/amplitude/direction/vorticity high-jet decompactification.

M17-437 proves that every **fixed** record-matched finite spatial coefficient jet persists for a fixed own-time fraction under normalized high-jet compactness.

The remaining question is whether the first nonzero spatial zero-jet order may drift to infinity from record to record while all other normalized transition data remain compact.

## 2. Zero crossing is a zero loop

On exact CE-H,

\[
D_\xi\kappa=0.
\]

Therefore `kappa` is constant along each connected regular vortex loop at each time.

If one point of a connected retained loop crosses

\[
\kappa=0,
\]

then at that crossing time

\[
\boxed{
\kappa|_\Gamma\equiv0.
}
\]

Thus every regular sign transition is a spatial zero-loop state of the type analyzed by M17-417--419.

## 3. Compact normalized transition-state bundle

Fix one own-scale normalization at each crossing.

Let

\[
\mathcal K_{tr}
\]

be the collection/closure of normalized transition states, including the represented loop, coefficient, velocity/strain, amplitude, direction, and enough finite spatial jets to support the M17-437 estimates.

Assume:

1. `K_tr` is compact in a topology in which the relevant finite spatial jets and loop embedding vary continuously;
2. the regular loop amplitude has a uniform positive lower margin;
3. tubular/normal-chart geometry remains uniformly nondegenerate;
4. the normalized analytic radius needed for M17-418/419 does not collapse;
5. the normalized high-jet spacetime neighborhood needed by M17-437 remains compact.

Failure of any item is retained as the corresponding amplitude, chart, analytic-radius, high-jet, interface, or domain decompactification exit.

## 4. Infinite spatial flatness is impossible in the retained transition bundle

For one transition state `Z`, define

\[
M_p(Z)
:=
\max_{x\in\Gamma(Z)}|D^p\kappa_Z(x)|.
\]

Because

\[
\kappa|_\Gamma=0,
\]

pure tangential derivatives of the loop restriction vanish. The relevant nonzero jets contain transverse/mixed directions.

Suppose for some retained regular positive-amplitude state

\[
M_p(Z)=0
\qquad\text{for every finite }p.
\]

Then all Taylor coefficients of the analytic coefficient vanish at a loop point. By M17-419,

\[
\kappa=0
\]

on an open neighborhood, hence exact CE-H gives

\[
\Delta\Omega=0
\]

there. Spatial analyticity continues `Delta Omega=0` globally, and finite enstrophy forces

\[
\Omega=0,
\]

contradicting the retained positive-flux/nonzero-vorticity loop state.

Therefore every `Z in K_tr` has at least one finite nonzero coefficient jet.

## 5. Finite open cover of transition states

For integers `p>=1`, `n>=1`, define

\[
\mathcal G_{p,n}
:=
\{Z\in\mathcal K_{tr}:M_p(Z)>1/n\}.
\]

By continuity of `M_p`, each `G_{p,n}` is relatively open in `K_tr`.

Section 4 gives the countable open cover

\[
\boxed{
\mathcal K_{tr}
=
\bigcup_{p\ge1}\bigcup_{n\ge1}\mathcal G_{p,n}.
}
\]

Because `K_tr` is compact, this cover has a **finite subcover**.

Hence there exist finite constants

\[
\boxed{P_*<\infty,\qquad n_*<\infty}
\]

such that every transition state has at least one jet order

\[
1\le p\le P_*
\]

with a uniform normalized nondegeneracy margin selected from finitely many classes.

Thus

\[
\boxed{
\text{first nonzero transition jet order }p_m\to\infty
}
\]

is impossible while the normalized analytic transition bundle remains compact.

## 6. Uniform parent-length arc and own-time persistence

For each member of the finite subcover, continuity of the jet and retained loop geometry gives a fixed normalized lower margin on a parent-length arc.

Because only finitely many classes are used, the minimum of their positive margins remains positive.

Likewise M17-437 gives for each fixed `p<=P_*` an own-time persistence fraction

\[
\tau_p\ge c_pr^2.
\]

Taking the minimum over the finite set,

\[
\boxed{
\tau_{jet}
\ge c_*r^2
}
\]

uniformly for every transition state.

During this interval, either a lower-order record-matched jet becomes nondegenerate or the selected finite `p`-jet persists. In both cases M17-437/M17-418 give an order-one normalized raw-`H2` packet per own-scale loop segment.

## 7. Uniform spatial multiplicity per crossing

The retained parent-length loop and tubular bounded-overlap geometry give

\[
\boxed{
N_x^{cross}\gtrsim cR
}
\]

own-scale loop segments at every transition.

Each segment carries a fixed normalized raw-`H2` amount for at least the own-time fraction from Section 6.

Therefore every finite-order compact transition pays

\[
\boxed{
h_{cross}^{norm}\gtrsim cR.
}
\]

This is the same crossing cost as M17-435, now uniform across all finite spatial zero-jet orders in the compact transition bundle.

## 8. M17-434 supplies the number of transitions

Assume the own-scale positive-flux branch occupies a fixed positive parent-time amount and no coefficient-scale/flux/geometry exit absorbs a positive fraction of that time.

M17-434 bounds every sign-preserving own-scale phase by

\[
O(r^2\log R).
\]

Therefore

\[
\boxed{
N_{cross}
\gtrsim
c\frac{R^2}{\log R}.
}
\]

Combining with Section 7,

\[
\boxed{
H_{R,tr}^{norm}
\gtrsim
c\frac{R^3}{\log R}.
}
\]

## 9. Harmonic ancestry divergence

Apply the M17-405 ancestry weight:

\[
\boxed{
R^{-3}H_{R,tr}^{norm}
\gtrsim
\frac c{\log R}.
}
\]

For geometric records

\[
R_m\asymp q^m,
\qquad q>1,
\]

we have

\[
\log R_m\asymp m,
\]

so

\[
\boxed{
\sum_m\frac1{\log R_m}=\infty.
}
\]

Hence infinitely many representation-safe records satisfying the M17-438 retained hypotheses contradict the finite first-generation raw-`H2` ancestor.

## 10. Conditional all-finite-order transition closure

Under:

- positive parent-time own-scale occupancy;
- positive flux floor;
- parent-length regular loop geometry;
- compact normalized analytic zero-transition state bundle;
- compact normalized high-jet spacetime neighborhoods;
- amplitude retention;
- representation-safe parent-to-record genealogy;

all finite-order regular zero transitions are closed.

There is no separate escape by sending the first nonzero spatial transition jet order to infinity while keeping this compactness.

## 11. Exact surviving transition exits

A surviving sequence must force at least one of:

\[
\boxed{G_{normalized\ analytic/high\text{-}jet\ decompactification}},
\]

\[
\boxed{G_{jet\text{-}scale/record\text{-}scale\ mismatch}},
\]

\[
\boxed{G_{positive\ flux/parent\text{-}time\ occupation\ thinning}},
\]

\[
\boxed{G_{amplitude/nodal\ loss}},
\]

\[
\boxed{G_{tube/chart/topology\ loss}},
\]

or

\[
\boxed{G_{parent\text{-}to\text{-}record\ genealogy/interface/CEH/domain\ loss}}.
\]

The earlier `higher-order zero transition` entry is therefore no longer independent on the compact analytic finite-jet branch.

## 12. Scope firewall

M17-438 does not prove a uniform analytic-radius or all-high-jet bound from Navier--Stokes energy alone.

Those are explicit compactness hypotheses of this late branch.

If normalized analytic/high-jet compactness itself fails with the record, the branch is retyped as high-jet/analytic-radius decompactification and must acquire an integral payer before it can be contradicted.

## 13. DSD role

DSD is used only to separate `order of the first nonzero jet` from true loss of the normalized analytic state space.

The proof is compactness, a countable open finite-jet cover, M17-419 infinite-flat exclusion, M17-437 temporal persistence, and the M17-434/435 harmonic counting mechanism.

## 14. Audit verdict

**PASS as a conditional all-finite-order zero-transition closure.**

On a compact normalized analytic positive-flux transition bundle, every crossing has a uniformly controlled finite spatial jet and fixed own-time packet; repeated sign fragmentation therefore contradicts the raw-`H2` ancestor by the `1/log R` harmonic divergence.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
