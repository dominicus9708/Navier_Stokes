# DSD M17-391 — Persistent own-scale flux tubes have an `R`-weighted standard-energy ledger and fixed positive flux is still geometrically summable

Date: 2026-09-08  
Canonical ID: **M17-391**

Status: **ACTIVE FLUX-ENERGY LEDGER / PERSISTENT-TUBE THRESHOLD THEOREM / M17-390 COMPANION**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Goal

M17-388 gives the standard-energy deformation ledger

\[
\sum_jR_jK_j^2<\infty.
\]

M17-390 shows that order-one or logarithmic recurrence deformation is geometrically summable.

The present module asks whether retained vorticity flux is more expensive.

On a persistent own-scale tube, the answer is again an exact `R`-weighted standard-energy ledger.

Fixed positive flux at infinitely many geometric scales is still compatible with finite energy.

## 2. One physical own-scale tube

Work in physical variables.

Let `T_R(t)` be a regular vortex-tube segment at physical scale `R` with

\[
\ell_R(t)\ge c_\ell R
\]

and transverse cross-sectional area

\[
A_R(s,t)\le C_A R^2
\]

along the retained segment.

Let the oriented vorticity flux through a transverse cross-section be

\[
\Phi_R(t)
:=
\int_{A_R(s,t)}\Omega\cdot n\,dA.
\]

Because `div Omega=0` and the tube is regular, the flux is independent of the cross-section label `s` as long as there is no side leakage, nodal/interface break, or tube-genealogy loss.

If these hypotheses fail, retain the corresponding geometry/interface/genealogy exit instead of using the present estimate.

## 3. Snapshot enstrophy lower bound from flux

For each cross-section, Cauchy--Schwarz gives

\[
|\Phi_R|^2
\le
A_R
\int_{A_R}|\Omega|^2dA.
\]

Hence

\[
\int_{A_R}|\Omega|^2dA
\ge
\frac{\Phi_R^2}{A_R}
\ge
\frac{\Phi_R^2}{C_AR^2}.
\]

Integrate along the tube length:

\[
\int_{T_R(t)}|\Omega|^2dx
\ge
\frac{c_\ell}{C_A}
\frac{\Phi_R(t)^2}{R}.
\]

Therefore

\[
\boxed{
E_{T_R}(t)
:=
\int_{T_R(t)}|\Omega|^2dx
\gtrsim
\frac{\Phi_R(t)^2}{R}.
}
\]

This is the physical own-scale version of the flux/enstrophy bridge.

No CE-H identity beyond the regular tube geometry is needed for this Cauchy--Schwarz estimate.

## 4. Persistent own-scale time gives a standard-energy cost

Assume the tube geometry persists on a physical interval `I_R` with

\[
|I_R|\ge c_t\frac{R^2}{\nu}
\]

and the flux has a retained lower bound

\[
|\Phi_R(t)|\ge\Phi_R^*>0
\qquad(t\in I_R).
\]

Integrating Section 3,

\[
\int_{I_R}E_{T_R}(t)dt
\gtrsim
\frac{(\Phi_R^*)^2}{R}|I_R|.
\]

Thus

\[
\boxed{
\nu\int_{I_R}E_{T_R}(t)dt
\gtrsim
R(\Phi_R^*)^2.
}
\]

The structural weight is exactly

\[
\boxed{R\Phi^2.}
\]

This belongs to the ordinary finite-energy Navier--Stokes dissipation currency

\[
\nu\int\|\Omega(t)\|_2^2dt<\infty.
\]

## 5. Bounded-overlap flux ledger

Let

\[
\{(R_j,I_j,T_j,\Phi_j)\}_j
\]

be persistent own-scale tube episodes whose time intervals have bounded overlap and whose spatial tube contributions are counted without duplication at each episode.

Then

\[
\sum_jR_j\Phi_j^2
\lesssim
\nu\sum_j\int_{I_j}\int_{T_j(t)}|\Omega|^2dxdt.
\]

Under bounded temporal/spatial multiplicity `N_0`, the standard energy inequality gives

\[
\boxed{
\sum_jR_j\Phi_j^2
\le
C(N_0,c_t,c_\ell,C_A,\nu,u_0)
<\infty.
}
\]

This is the main M17-391 flux-energy ledger.

## 6. Fixed positive flux is not enough

Suppose

\[
\Phi_j\ge\Phi_*>0
\]

at every geometric scale

\[
R_j=R_0q^j,
\qquad
0<q<1.
\]

Then the mandatory energy cost is only

\[
\sum_jR_j\Phi_*^2
=
\Phi_*^2R_0\sum_jq^j
<\infty.
\]

Therefore

\[
\boxed{
\text{fixed positive flux through infinitely many geometric scales}
\not\Rightarrow
\text{energy contradiction}.
}
\]

This is the flux analogue of the M17-388/M17-390 recurrence firewall.

## 7. Exact flux growth threshold

If

\[
\Phi_j\sim R_j^{-\alpha},
\]

then

\[
R_j\Phi_j^2
\sim
R_j^{1-2\alpha}.
\]

For geometric `R_j`, the weighted series is non-summable at the power threshold

\[
\boxed{
\alpha\ge\frac12.
}
\]

Thus a sufficient per-generation contradiction scale is

\[
\boxed{
\Phi_j\gtrsim R_j^{-1/2}
}
\]

on infinitely many bounded-overlap persistent episodes.

Any weaker statement must be tested by the exact series

\[
\sum_jR_j\Phi_j^2.
\]

## 8. Disjoint tube multiplicity threshold

Suppose at scale `R_j` there are `M_j` pairwise disjoint persistent tubes, each with

\[
|\Phi_{j,k}|\ge\Phi_*>0
\]

and the same geometry constants.

Their enstrophy contributions add, giving

\[
\boxed{
\sum_jR_jM_j\Phi_*^2<\infty.
}
\]

Hence for a power multiplicity

\[
M_j\sim R_j^{-\beta},
\]

the geometric energy threshold is

\[
\boxed{
\beta\ge1.
}
\]

This agrees with the independent normalized-multiplicity threshold obtained in M17-390 from the exact similarity energy weight.

The disjointness/additivity hypothesis is essential. Overlapping descriptions cannot be counted as separate energy payers.

## 9. Relation to M17-368 and flux thinning

M17-368 obtains, on a retained intrinsic-scale tube under comparable geometry,

\[
E_T\gtrsim\phi^2r^{-1}.
\]

Section 3 is the corresponding physical geometric statement.

If a later coefficient-scale/parent dictionary identifies `r` with the physical own-scale radius `R` up to fixed constants, the formulas agree.

M17-371/372/379 drive strict-subscale flux toward a small quantity, schematically

\[
\Phi(R)\ll1
\]

and in the strongest retained branch to an `R^{5/2}`-type scale after the required representation/scale map.

Such flux thinning moves **away** from the M17-391 contradiction threshold.

For example, if

\[
\Phi(R)\lesssim R^{5/2},
\]

then

\[
R\Phi(R)^2
\lesssim R^6,
\]

which is extremely summable on geometric scales.

Therefore flux evacuation itself cannot close the energy contradiction route.

Its value is instead to force coefficient exposure, residence, turnover, or genealogy complexity as in M17-372--379.

## 10. Combined standard-energy ledger with M17-388

On a branch where the hypotheses of both M17-388 and M17-391 hold on a bounded-overlap family of physical own-scale episodes,

\[
\boxed{
\sum_jR_j
\left(
K_j^2+\Phi_j^2
\right)
<\infty.
}
\]

If there are disjoint tube multiplicities `M_j` with a common lower flux `Phi_*`, one also has

\[
\boxed{
\sum_jR_jM_j\Phi_*^2<\infty.
}
\]

Thus late CE-H dynamics now has two separate but standard-energy-certified physical currencies:

1. deformation action `K_j`;
2. retained flux `Phi_j` on a persistent tube.

Both carry the same geometric weight `R_j` after own-scale time integration.

## 11. Consequence for the current proof search

The following known lower bounds are insufficient by themselves:

- order-one recurrence strain;
- logarithmic accumulated deformation;
- fixed positive tube flux;
- logarithmically many coefficient scales;
- flux evacuation to a small power of `R`.

A standard-energy contradiction through the persistent-tube route requires a genuinely non-summable enhancement such as

\[
\boxed{
\sum_jR_jK_j^2=\infty,
}

\[
\boxed{
\sum_jR_j\Phi_j^2=\infty,
}
\]

or

\[
\boxed{
\sum_jR_jM_j\Phi_*^2=\infty.
}
\]

The natural power thresholds are respectively

\[
K_j\sim R_j^{-1/2},
\qquad
\Phi_j\sim R_j^{-1/2},
\qquad
M_j\sim R_j^{-1}.
\]

## 12. DSD audit role

The DSD role is a resource-accounting audit:

- do not treat fixed positive flux as scale-independent physical cost;
- multiply a snapshot tube lower bound by its actual own-scale physical time before comparing with the energy ledger;
- do not count overlapping tube descriptions as independent multiplicity;
- do not mistake flux thinning for an energy contradiction when it actually makes the direct energy cost smaller.

The canonical proof uses only divergence-free flux conservation, Cauchy--Schwarz, tube geometry, and the standard Navier--Stokes energy inequality.

## 13. Audit verdict

**PASS — certified flux-energy ledger and threshold refinement.**

The late CE-H compact persistent branch now obeys the combined standard-energy firewall

\[
\boxed{
\sum_jR_j(K_j^2+\Phi_j^2)<\infty
}
\]

under the stated bounded-overlap hypotheses.

The next target is therefore the turnover/gradient/coefficient-decompactification side: determine whether one of those branches forces deformation, flux, or disjoint multiplicity to grow at or above the critical `R^{-1/2}` / `R^{-1}` thresholds.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
