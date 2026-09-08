# DSD M17-433 — Quadratic flux participation refines the loop raw-H2 closure to `sum alpha Phi^2 / N_eff` and gives a super-log fragmentation escape threshold

Date: 2026-09-08  
Canonical ID: **M17-433**

Status: **ACTIVE QUADRATIC-FLUX CLOSURE CRITERION / M17-413--414--420--432 REFINEMENT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M17-413--414 derive the cubic raw-`H2` packet mechanism for one retained parent-length positive-flux CE-H loop.

M17-420 closes the retained compact single-loop branch by positive occupation of one fixed finite-jet class.

Corrected M17-432 shows that arbitrary label turnover is neutral only for flux-linear currencies. The raw-`H2` loop packet is quadratic in flux and can be diluted by fragmentation.

The present module inserts that quadratic dilution exactly into the M17-413--414 ancestry calculation.

## 2. Fragmented positive-flux family at one record

Fix one parent-normalized record with inverse descendant scale

\[
\boxed{R\gg1,\qquad r=R^{-1}.}
\]

At a good time, suppose the retained positive-flux loop/tube family is partitioned into disjoint material bands with fluxes

\[
\phi_i>0.
\]

Write

\[
\boxed{
\Phi:=\sum_i\phi_i
}
\]

and define the effective quadratic participation number

\[
\boxed{
N_{eff}
:=
\frac{\Phi^2}{\sum_i\phi_i^2}
\ge1.
}
\]

Equivalently,

\[
\boxed{
\sum_i\phi_i^2
=
\frac{\Phi^2}{N_{eff}}.
}
\]

`N_eff=1` corresponds to one dominant band; large `N_eff` corresponds to flux spread over many comparably small bands.

## 3. M17-413 packet payment with fragmentation

Under the retained M17-413 geometry for each participating band:

- parent-length loop arc;
- common own coefficient scale `r` on the loop;
- own-scale cross-sectional area control;
- tubular bounded overlap;
- representation-safe record genealogy;

one own-scale segment over one own-time pays

\[
h_{seg,i}^{norm}\gtrsim c\phi_i^2.
\]

Summing disjoint/bounded-overlap band contributions gives

\[
\boxed{
h_{seg,total}^{norm}
\gtrsim
c\sum_i\phi_i^2
=
c\frac{\Phi^2}{N_{eff}}.
}
\]

Thus fragmentation enters only through the quadratic concentration factor `1/N_eff`.

## 4. Restore the cubic space-time factor

As in M17-413, a parent-length loop at descendant scale `r=R^{-1}` supplies

\[
N_x\gtrsim cR
\]

same-scale spatial segments.

A usable good-time fraction `alpha` of one parent parabolic window supplies normalized temporal multiplicity

\[
N_t\gtrsim c\alpha R^2.
\]

Therefore

\[
\boxed{
H_{record}^{norm}
\gtrsim
c\alpha R^3
\frac{\Phi^2}{N_{eff}}.
}
\]

Applying the M17-405 ancestry weight `R^{-3}` gives

\[
\boxed{
R^{-3}H_{record}^{norm}
\gtrsim
c\alpha
\frac{\Phi^2}{N_{eff}}.
}
\]

This is the exact corrected record-level loop currency.

## 5. Cross-record closure criterion

For records `m`, define

\[
\alpha_m,
\qquad
\Phi_m,
\qquad
N_{eff,m}.
\]

Under finite-overlap parent-to-record genealogy and uniform geometric constants, the M17-405 finite ancestor is contradicted if

\[
\boxed{
\sum_m
\alpha_m
\frac{\Phi_m^2}{N_{eff,m}}
=\infty.
}
\]

Therefore the correct M17-413--420 loop closure criterion in the presence of quadratic flux fragmentation is

\[
\boxed{
\sum_m\alpha_m\Phi_m^2/N_{eff,m}=\infty,
}
\]

not merely `sum alpha_m = infinity` unless both `Phi_m` is uniformly positive and `N_eff,m` is uniformly bounded.

## 6. Uniform positive flux and positive occupation

If

\[
\alpha_m\ge\alpha_*>0,
\qquad
\Phi_m\ge\Phi_*>0,
\]

then closure reduces to

\[
\boxed{
\sum_m\frac1{N_{eff,m}}=\infty.
}
\]

Hence to evade the raw-`H2` ancestor purely by flux fragmentation, a necessary condition is

\[
\boxed{
\sum_m\frac1{N_{eff,m}}<\infty.
}
\]

So bounded fragmentation, logarithmically slow finite participation, or any sequence whose reciprocal is non-summable cannot evade the loop closure.

## 7. Generation-index threshold

Let the inverse record scales be geometric:

\[
R_m\asymp q^m,
\qquad q>1.
\]

Then

\[
m\asymp\log R_m.
\]

If

\[
N_{eff,m}\asymp m^p,
\]

then

\[
\sum_m\frac1{N_{eff,m}}
\asymp
\sum_m m^{-p}.
\]

Therefore

\[
\boxed{
\begin{aligned}
p\le1
&\Rightarrow \text{quadratic fragmentation still cannot evade closure},\\
p>1
&\Rightarrow \text{the reciprocal participation series may converge}.
\end{aligned}
}
\]

In scale language, a purely fragmentation-based escape requires at least super-logarithmic participation growth of the type

\[
\boxed{
N_{eff}(R)
\gtrsim
(\log R)^{1+\varepsilon}
}
\]

up to slowly varying borderline corrections.

The exact borderline is the reciprocal-series criterion, not a heuristic power law.

## 8. Combined flux thinning and fragmentation

Suppose on geometric records

\[
\Phi_m\asymp m^{-a},
\qquad
N_{eff,m}\asymp m^p,
\qquad
\alpha_m\asymp1.
\]

Then

\[
\alpha_m\frac{\Phi_m^2}{N_{eff,m}}
\asymp
m^{-(2a+p)}.
\]

Hence the borderline is

\[
\boxed{2a+p=1.}
\]

More precisely,

\[
\boxed{
2a+p\le1
\Rightarrow
\text{the harmonic-type series diverges and the loop raw-H2 branch closes},
}
\]

while

\[
2a+p>1
\]

is compatible with summability at this level.

Since `m ~ log R`, this says

\[
\Phi(R)\sim(\log R)^{-a},
\qquad
N_{eff}(R)\sim(\log R)^p
\]

obey the same critical line `2a+p=1`.

## 9. Any genuine power-law scale thinning is already enough to evade this particular series

If

\[
\Phi_m\sim R_m^{-\gamma}
\qquad(\gamma>0),
\]

then on geometric records

\[
\Phi_m^2
\]

decays geometrically.

Thus even with bounded `N_eff` and positive `alpha_m`,

\[
\sum_m\alpha_m\frac{\Phi_m^2}{N_{eff,m}}<\infty
\]

is possible.

Therefore the M17-413--420 raw-`H2` loop closure is highly sensitive to true positive-flux thinning: any fixed positive power of record scale defeats the constant-flux harmonic occupation mechanism unless another payer compensates.

This is an escape classification, not a construction of such thinning.

## 10. Relation to M17-391 standard-energy flux ledger

M17-391 gives, for disjoint persistent physical own-scale tubes,

\[
\sum_j r_j\sum_i\phi_{j,i}^2<\infty.
\]

In terms of total flux and participation,

\[
\boxed{
\sum_j
r_j
\frac{\Phi_j^2}{N_{eff,j}}
<\infty.
}
\]

This has an extra small physical-scale factor `r_j=R_j^{-1}` relative to the fully saturated M17-413 raw-`H2` ancestry criterion.

Hence M17-391 does not prevent the fragmentation rates identified above; the parent-length plus parent-time raw-`H2` mechanism is strictly stronger when its geometry and genealogy persist.

## 11. Corrected late-loop split

The retained quadratic loop branch is now

\[
\boxed{
\begin{aligned}
H_{compact/finite\ jet\ loop\ payer}
\Longrightarrow{}&
H_{\sum_m\alpha_m\Phi_m^2/N_{eff,m}=\infty}
\Rightarrow\text{contradiction}\\
&\lor G_{positive\ flux\ thinning}\\
&\lor G_{quadratic\ flux\ participation\ decompactification}\\
&\lor G_{good\ time\ occupation\ thinning}\\
&\lor G_{geometry/scale/genealogy/interface\ loss}.
\end{aligned}
}
\]

This separates three quantitatively different thinning mechanisms: time occupation, total flux, and quadratic flux concentration.

## 12. DSD role

DSD is used only to expose the correct algebraic currency under fragmentation and to prevent a flux-linear measure argument from being applied to a flux-quadratic PDE payer.

The mathematics is Cauchy--Schwarz flux lower bounds, countable additivity of disjoint raw-`H2` packets, and the M17-405 ancestry scaling.

## 13. Audit verdict

**PASS as the corrected quadratic-flux loop closure criterion.**

The exact late-loop record currency is `alpha Phi^2 / N_eff`. Pure label turnover is not the issue; quadratic flux dilution is.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
